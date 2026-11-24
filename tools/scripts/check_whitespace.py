#!/usr/bin/env python3
"""Check text files for the whitespace rules in .editorconfig.

Every text file must use LF line endings, end with a newline, and have no
trailing whitespace. Markdown files must not contain tabs. Binary files, which
contain a NUL byte, are skipped. Empty files are allowed.

Language-specific indentation rules belong in .editorconfig and are not
checked here.

Run from anywhere in the repository:

    python3 tools/scripts/check_whitespace.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NO_TAB_SUFFIXES = {".md"}


def repository_files() -> list[Path]:
    """Return tracked and untracked files, excluding ignored files."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    paths = (ROOT / name for name in result.stdout.split("\0") if name)
    return sorted(path for path in paths if path.is_file() and not path.is_symlink())


def problems(path: Path) -> list[str]:
    """Return the whitespace problems found in one file."""
    data = path.read_bytes()
    if not data or b"\0" in data:
        return []

    found: list[str] = []
    if b"\r" in data:
        found.append("uses CR or CRLF line endings instead of LF")
    if not data.endswith(b"\n"):
        found.append("does not end with a newline")

    check_tabs = path.suffix in NO_TAB_SUFFIXES
    for number, line in enumerate(data.decode("utf-8", errors="replace").split("\n"), start=1):
        line = line.rstrip("\r")
        if line != line.rstrip():
            found.append(f"line {number} has trailing whitespace")
        if check_tabs and "\t" in line:
            found.append(f"line {number} contains a tab")
    return found


def main() -> int:
    failures: list[str] = []
    files = repository_files()

    for path in files:
        failures.extend(f"  {path.relative_to(ROOT)}: {problem}" for problem in problems(path))

    if failures:
        print("Whitespace problems:")
        print("\n".join(failures))
        return 1

    print(f"All {len(files)} files pass the whitespace checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
