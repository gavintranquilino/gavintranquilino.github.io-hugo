#!/usr/bin/env python3
"""Lightweight front matter validator for Hugo project pages.

Checks:
- required fields exist
- duplicate top-level keys
- HTML tags in title/subtitle
- date is quoted ISO format YYYY-MM-DD
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ("title", "date", "imageUrl", "subtitle", "bulletPoints")
HTML_TAG_RE = re.compile(r"<[^>]+>")
ISO_DATE_RE = re.compile(r'^"\d{4}-\d{2}-\d{2}"$')
FIELD_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):")


def split_front_matter(text: str) -> tuple[list[str], int] | tuple[None, None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None

    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[1:idx], idx + 1
    return None, None


def parse_top_level_keys(front_matter_lines: list[str]) -> list[tuple[str, int, str]]:
    keys: list[tuple[str, int, str]] = []
    for i, line in enumerate(front_matter_lines, start=2):
        if not line or line.startswith("#") or line.startswith(" ") or line.startswith("\t"):
            continue
        match = FIELD_KEY_RE.match(line)
        if match:
            key = match.group(1)
            value = line.split(":", 1)[1].strip()
            keys.append((key, i, value))
    return keys


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm_lines, _ = split_front_matter(text)

    if fm_lines is None:
        return [f"{path}:1 missing YAML front matter block"]

    keys = parse_top_level_keys(fm_lines)

    seen: dict[str, int] = {}
    values: dict[str, str] = {}
    for key, line_no, value in keys:
        if key in seen:
            errors.append(f"{path}:{line_no} duplicate key '{key}' (first at line {seen[key]})")
        else:
            seen[key] = line_no
        values[key] = value

    for field in REQUIRED_FIELDS:
        if field not in seen:
            errors.append(f"{path}:1 missing required field '{field}'")

    for text_field in ("title", "subtitle"):
        if text_field in values and HTML_TAG_RE.search(values[text_field]):
            errors.append(f"{path}:{seen[text_field]} HTML tag found in '{text_field}'")

    if "date" in values and not ISO_DATE_RE.match(values["date"]):
        errors.append(
            f"{path}:{seen['date']} date should be quoted ISO format like \"2026-03-22\""
        )

    return errors


def collect_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.glob("*.md") if p.name != ".gitkeep")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Hugo project front matter.")
    parser.add_argument(
        "--projects-dir",
        default="content/projects",
        help="Directory containing project markdown files (default: content/projects)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when issues are found.",
    )
    args = parser.parse_args()

    projects_dir = Path(args.projects_dir).resolve()
    if not projects_dir.exists():
        print(f"error: projects directory does not exist: {projects_dir}", file=sys.stderr)
        return 2

    files = collect_markdown_files(projects_dir)
    all_errors: list[str] = []
    for md_file in files:
        all_errors.extend(validate_file(md_file))

    if all_errors:
        print(f"Found {len(all_errors)} front matter issue(s):")
        for err in all_errors:
            print(f"- {err}")
        return 1 if args.strict else 0

    print(f"No front matter issues found in {len(files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
