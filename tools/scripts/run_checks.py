#!/usr/bin/env python3
"""Run the repository checks, as continuous integration does.

Run every check:

    python3 tools/scripts/run_checks.py

Run selected checks by name:

    python3 tools/scripts/run_checks.py links whitespace

Each check runs even when an earlier one fails. The exit status is nonzero
when any check fails.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parents[1]

# Add new checks here so that local runs and continuous integration stay the same.
CHECKS = {
    "acronyms": [SCRIPTS / "check_acronyms.py"],
    "links": [SCRIPTS / "check_links.py"],
    "whitespace": [SCRIPTS / "check_whitespace.py"],
    "frontmatter": [SCRIPTS / "check_frontmatter.py", "--strict"],
    "tooling": ["-m", "unittest", "discover", "-s", str(SCRIPTS.parent / "tests")],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the repository checks.")
    parser.add_argument("checks", nargs="*", metavar="CHECK", help=f"checks to run: {', '.join(CHECKS)} (default: all)")
    names = parser.parse_args().checks or list(CHECKS)
    unknown = [name for name in names if name not in CHECKS]
    if unknown:
        parser.error(f"unknown check: {', '.join(unknown)}. Choose from {', '.join(CHECKS)}.")

    failed: list[str] = []
    for name in names:
        print(f"== {name}", flush=True)
        if subprocess.run([sys.executable, *CHECKS[name]], cwd=ROOT).returncode != 0:
            failed.append(name)
        print(flush=True)

    if failed:
        print(f"Failed: {', '.join(failed)}")
        return 1

    print(f"Passed: {', '.join(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
