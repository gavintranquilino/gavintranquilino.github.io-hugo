#!/usr/bin/env python3
"""Check that acronyms used in Markdown are defined in the glossary.

An acronym is an uppercase word of two or more characters, such as PR or HTTP2.
Each one must appear in the first column of a table in docs/glossary.md or be
listed in tools/scripts/acronym-ignore.txt.

Code, link targets, URLs, HTML comments, and file names such as README.md are
not checked, since they are not prose. Portfolio content and the personal
project backlog in TODO.md are outside the repository documentation scope.

Run from anywhere in the repository:

    python3 tools/scripts/check_acronyms.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GLOSSARY = ROOT / "docs" / "glossary.md"
IGNORE_FILE = ROOT / "tools" / "scripts" / "acronym-ignore.txt"
MARKDOWN_SUFFIXES = {".md"}

ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9]+\b")
TABLE_FIRST_CELL_RE = re.compile(r"^\|\s*([^|]+?)\s*\|", re.MULTILINE)
TABLE_SEPARATOR_RE = re.compile(r"^:?-+:?$")

# Patterns for text that is not prose. Each match is blanked out before
# checking, keeping newlines so that reported line numbers stay correct.
FENCE_RE = re.compile(r"^ {0,3}(```|~~~).*?^ {0,3}\1[^\n]*$", re.MULTILINE | re.DOTALL)
NON_PROSE_RES = [
    re.compile(r"<!--.*?-->", re.DOTALL),  # HTML comments
    re.compile(r"(`+).+?\1", re.DOTALL),  # Inline code spans
    re.compile(r"\]\([^)]*\)"),  # Inline link targets
    re.compile(r"^\s*\[[^\]]+\]:\s*\S+.*$", re.MULTILINE),  # Reference link definitions
    re.compile(r"<?https?://[^\s>)]+>?"),  # Bare URLs and autolinks
    re.compile(r"\b[\w.-]*\w\.[A-Za-z][A-Za-z0-9]*\b"),  # File names such as AGENTS.md
]


def normalize(term: str) -> str:
    """Return a term in a form suitable for comparison."""
    return re.sub(r"[^A-Za-z0-9]", "", term).lower()


def blank(match: re.Match[str]) -> str:
    """Replace matched text with spaces, keeping its newlines."""
    return re.sub(r"[^\n]", " ", match.group(0))


def prose(text: str) -> str:
    """Return Markdown text with code, links, and file names blanked out."""
    text = FENCE_RE.sub(blank, text)
    for pattern in NON_PROSE_RES:
        text = pattern.sub(blank, text)
    return text


def load_glossary() -> set[str]:
    """Return the normalized terms defined in the glossary's tables.

    A compound term such as "HTTP API" also defines each of its words.
    """
    terms: set[str] = set()
    for cell in TABLE_FIRST_CELL_RE.findall(GLOSSARY.read_text(encoding="utf-8")):
        cell = cell.strip(" `")
        if not cell or cell.lower() == "term" or TABLE_SEPARATOR_RE.match(cell):
            continue
        terms.add(normalize(cell))
        terms.update(normalize(word) for word in re.split(r"[\s/]+", cell) if word)
    return terms


def load_ignore_list() -> set[str]:
    """Return the normalized words listed in the ignore file."""
    if not IGNORE_FILE.exists():
        return set()
    lines = IGNORE_FILE.read_text(encoding="utf-8").splitlines()
    return {normalize(line) for line in lines if line.strip() and not line.lstrip().startswith("#")}


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
        and not path.is_relative_to(ROOT / "content") and path != ROOT / "TODO.md"
    )


def main() -> int:
    if not GLOSSARY.exists():
        print(f"Glossary not found: {GLOSSARY.relative_to(ROOT)}", file=sys.stderr)
        return 2

    known = load_glossary() | load_ignore_list()
    failures: list[str] = []

    for path in markdown_files():
        text = prose(path.read_text(encoding="utf-8", errors="replace"))
        for line_number, line in enumerate(text.splitlines(), start=1):
            missing = sorted({word for word in ACRONYM_RE.findall(line) if normalize(word) not in known})
            if missing:
                failures.append(f"  {path.relative_to(ROOT)}:{line_number}: {', '.join(missing)}")

    if failures:
        print(f"Acronyms not defined in {GLOSSARY.relative_to(ROOT)}:")
        print("\n".join(failures))
        print(
            f"\nDefine each acronym in the glossary. If a word is not an acronym, "
            f"add it to {IGNORE_FILE.relative_to(ROOT)} with a comment explaining why."
        )
        return 1

    print("All acronyms are defined in the glossary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
