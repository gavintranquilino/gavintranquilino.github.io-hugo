# Tools

Scripts that check the repository locally and in continuous integration, plus utilities that edit older content. The checks need only Python 3 and Git and run from any working directory. They check tracked and untracked files and skip files ignored by Git. The front-matter check scans `content/projects/*.md` directly.

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/run_checks.py` | Runs every check, or the checks named on the command line |
| `scripts/check_acronyms.py` | Checks that acronyms used in Markdown are defined in the [Glossary](../docs/glossary.md) |
| `scripts/check_links.py` | Checks that relative Markdown links in repository documentation point to existing files, headings, and anchors |
| `scripts/check_whitespace.py` | Checks the line-ending, final-newline, and trailing-whitespace rules from `.editorconfig` |
| `scripts/check_frontmatter.py` | Checks required project metadata, duplicate keys, title and subtitle markup, and date syntax |
| `tests/test_checks.py` | Regression tests for strict failures, check scope, and relocated utility paths, registered as `tooling` |

`scripts/acronym-ignore.txt` lists uppercase words the acronym check should accept that are not acronyms. Define real acronyms in the glossary instead of listing them here.

## Running Checks Locally

Run the checks from the repository root before requesting review.

```sh
python3 tools/scripts/run_checks.py
```

To run selected checks, name them.

```sh
python3 tools/scripts/run_checks.py links whitespace
```

The [checks workflow](../.github/workflows/checks.yml) runs each check as a separate job named `check/<name>`, such as `check/acronyms`. It also builds the Hugo site in the development image as `build/hugo`. It runs on every pull request, on pushes to `main`, and when started manually from the Actions tab. Run `hugo --gc --minify` in the [dev container](../.devcontainer/README.md) to verify the same build locally.

To add a check, add its script to `scripts/`, list it in the table above, register it in `CHECKS` in `scripts/run_checks.py`, and add its name to the `check` list in the workflow.

## Fixing Failures

Each check reports the file, and the line where possible, for each problem.

### Acronyms

Portfolio text in `content/` and the personal backlog in `TODO.md` are outside this check's scope. Repository documentation follows the shared glossary rules.

* For a real acronym, add it to the Acronyms and Abbreviations table in the glossary.
* For a word that is not an acronym, such as an all-caps label, add it to `scripts/acronym-ignore.txt` with a comment explaining why.
* Write code, commands, and file names in backticks. The check skips code spans, code blocks, link targets, URLs, and file names.

### Links

This check excludes `content/`, whose links use Hugo routes and processed assets rather than repository-relative documentation paths. Preview project pages and check their published links manually.

* Correct the path relative to the linking file, or the fragment to match the target heading. A heading's anchor is its text in lowercase, with punctuation removed and spaces replaced by hyphens.
* Links to other websites are not checked, so that the check works offline and does not fail when an external site is unavailable.

### Whitespace

* Configure your editor to follow `.editorconfig`, which most editors support directly or through a plugin.
* Convert CRLF line endings to LF. The `.gitattributes` file normalizes line endings when files are committed.

### Front Matter

Run `python3 tools/scripts/run_checks.py frontmatter` to fail on invalid metadata. The runner supplies `--strict` to the underlying checker. Direct calls without `--strict` report issues without failing for compatibility with the original utility.

* Add the required `title`, `date`, `imageUrl`, `subtitle`, and `bulletPoints` keys.
* Remove duplicate top-level keys and HTML tags in `title` or `subtitle`.
* Double-quote dates in `YYYY-MM-DD` form.
* Follow the report with a Hugo build. This lightweight checker does not parse the complete YAML schema or validate calendar dates.

## Maintenance Utilities

Run these from the repository root with Python 3, preferably inside the dev container. Both edit files in place and default to this repository's `content/projects/` regardless of the working directory. Review the resulting diff before committing.

| Command | Effect |
| --- | --- |
| `python3 tools/scripts/normalize_frontmatter.py` | Strips HTML from project titles and subtitles and quotes unquoted dates |
| `python3 tools/scripts/convert_image_links.py` | Converts Markdown images using `/img/...` to the processed `img` shortcode |
| `python3 tools/scripts/convert_image_links.py /path/to/projects` | Converts images in a different project directory |

These are the former `scripts/normalize_frontmatter.py` and `data_processor.py`. The checker was formerly `scripts/lint_frontmatter.py`. Maintenance utilities do not run automatically in CI.

## Tooling Tests

`tests/` contains standard-library regression tests for the checks and relocated utilities. Run them with `python3 tools/scripts/run_checks.py tooling`. They use temporary content fixtures and do not edit the site's project pages.
