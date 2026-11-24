#!/usr/bin/env python3
"""Check that relative links in Markdown point to existing files and headings.

Each inline link, image, and reference definition with a relative target must
resolve to a file or directory in the repository. A link with a fragment, such
as guide.md#setup, must also match a heading or HTML anchor in the target
Markdown file. Links with a scheme, such as https: or mailto:, are not checked.
Hugo content is excluded because its links resolve against published routes
and assets rather than the repository's documentation tree.

Run from anywhere in the repository:

    python3 tools/scripts/check_links.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
MARKDOWN_SUFFIXES = {".md"}

# Code is blanked out before links are read, so examples in code are ignored.
# Newlines are kept so that reported line numbers stay correct.
FENCE_RE = re.compile(r"^ {0,3}(```|~~~).*?^ {0,3}\1[^\n]*$", re.MULTILINE | re.DOTALL)
CODE_SPAN_RE = re.compile(r"(`+).+?\1", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

INLINE_LINK_RE = re.compile(r"\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+[\"'(][^)]*)?\)")
REFERENCE_DEF_RE = re.compile(r"^ {0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)", re.MULTILINE)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
HEADING_RE = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_ANCHOR_RE = re.compile(r"<[^>]+\b(?:id|name)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)


def blank(match: re.Match[str]) -> str:
    """Replace matched text with spaces, keeping its newlines."""
    return re.sub(r"[^\n]", " ", match.group(0))


def without_code(text: str) -> str:
    """Return Markdown text with code and HTML comments blanked out."""
    for pattern in (FENCE_RE, CODE_SPAN_RE, HTML_COMMENT_RE):
        text = pattern.sub(blank, text)
    return text


def slug(heading: str) -> str:
    """Return the anchor GitHub generates for a heading."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # Keep link text only
    text = re.sub(r"[`*_~]|<[^>]+>", "", text).strip().lower()
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", text))


def anchors(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    """Return the heading and HTML anchors defined in a Markdown file."""
    if path not in cache:
        text = path.read_text(encoding="utf-8", errors="replace")
        found: set[str] = set(HTML_ANCHOR_RE.findall(text))
        counts: dict[str, int] = {}
        for heading in HEADING_RE.findall(without_code(text)):
            base = slug(heading)
            count = counts.get(base, 0)
            counts[base] = count + 1
            found.add(base if count == 0 else f"{base}-{count}")
        cache[path] = found
    return cache[path]


def markdown_files() -> list[Path]:
    """Return tracked and untracked Markdown files, excluding ignored files."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    paths = (ROOT / name for name in result.stdout.split("\0") if name)
    return sorted(
        path for path in paths
        if path.suffix in MARKDOWN_SUFFIXES and path.is_file()
        and not path.is_relative_to(ROOT / "content")
    )


def check_target(source: Path, target: str, cache: dict[Path, set[str]]) -> str | None:
    """Return a problem description, or None when the link resolves."""
    target = target.strip("<>")
    if not target or SCHEME_RE.match(target):
        return None
    path_part, _, fragment = target.partition("#")
    path_part = unquote(path_part)
    if not path_part:
        resolved = source
    elif path_part.startswith("/"):
        resolved = ROOT / path_part.lstrip("/")
    else:
        resolved = source.parent / path_part
    resolved = resolved.resolve()
    if not resolved.is_relative_to(ROOT):
        return f"{target} points outside the repository"
    if not resolved.exists():
        return f"{target} does not exist"
    if fragment and resolved.suffix in MARKDOWN_SUFFIXES and resolved.is_file():
        if unquote(fragment).lower() not in anchors(resolved, cache):
            return f"{target} has no heading or anchor named #{fragment}"
    return None


def main() -> int:
    cache: dict[Path, set[str]] = {}
    failures: list[tuple[str, int, str]] = []
    checked = 0

    for path in markdown_files():
        text = without_code(path.read_text(encoding="utf-8", errors="replace"))
        for pattern in (INLINE_LINK_RE, REFERENCE_DEF_RE):
            for match in pattern.finditer(text):
                checked += 1
                problem = check_target(path, match.group(1), cache)
                if problem:
                    line = text.count("\n", 0, match.start()) + 1
                    failures.append((str(path.relative_to(ROOT)), line, problem))

    if failures:
        print("Broken links:")
        for name, line, problem in sorted(failures):
            print(f"  {name}:{line}: {problem}")
        return 1

    print(f"All {checked} links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
