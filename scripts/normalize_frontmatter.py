#!/usr/bin/env python3
"""Normalize front matter in content/projects markdown files.

Actions:
- Strip HTML tags from title/subtitle values.
- Quote unquoted ISO date values.
"""

from __future__ import annotations

import re
from pathlib import Path

TITLE_RE = re.compile(r"^(title\s*:\s*)(.+?)\s*$")
SUBTITLE_RE = re.compile(r"^(subtitle\s*:\s*)(.+?)\s*$")
DATE_UNQUOTED_RE = re.compile(r"^(date\s*:\s*)(\d{4}-\d{2}-\d{2})\s*$")
HTML_TAG_RE = re.compile(r"<[^>]+>")


def clean_value(raw: str) -> str:
    value = raw.strip()
    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        value = value[1:-1]
    value = HTML_TAG_RE.sub(" ", value)
    value = " ".join(value.split())
    return f'"{value}"'


def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    if not lines or lines[0].strip() != "---":
        return False

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return False

    changed = False

    for i in range(1, end_idx):
        line = lines[i].rstrip("\n")

        m = TITLE_RE.match(line)
        if m:
            new_line = f"{m.group(1)}{clean_value(m.group(2))}"
            if new_line != line:
                lines[i] = new_line + "\n"
                changed = True
            continue

        m = SUBTITLE_RE.match(line)
        if m:
            new_line = f"{m.group(1)}{clean_value(m.group(2))}"
            if new_line != line:
                lines[i] = new_line + "\n"
                changed = True
            continue

        m = DATE_UNQUOTED_RE.match(line)
        if m:
            new_line = f"{m.group(1)}\"{m.group(2)}\""
            if new_line != line:
                lines[i] = new_line + "\n"
                changed = True

    if changed:
        path.write_text("".join(lines), encoding="utf-8")

    return changed


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    projects = root / "content" / "projects"

    changed_count = 0
    for md in sorted(projects.glob("*.md")):
        if normalize_file(md):
            changed_count += 1
            print(f"updated: {md}")

    print(f"normalized files: {changed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
