# Coding Style

These conventions apply throughout the repository, except to vendored or generated files and the content-writing exception below. The root `.editorconfig` applies shared encoding, line-ending, and whitespace settings in editors that support it.

## General Code Conventions

* Write code to be read. Use clear names that describe what a function does or what a value holds.
* Keep responsibilities focused and make dependencies, side effects, and ownership clear.
* Follow the surrounding code's conventions unless the change explicitly updates them.
* Use named constants when a literal's meaning would otherwise be unclear.
* Explain non-obvious decisions, constraints, and tradeoffs in comments. Avoid repeating what the code already says.
* Document public interfaces where callers need to understand inputs, outputs, failure behavior, ownership, or lifetime constraints.
* Use idiomatic language features and the project's chosen formatter when one is configured.

## Prose

This applies to documentation, code comments, and schema comments.

* Write plainly, as you would explain something to a colleague.
* Name who does what and prefer active voice.
* Say a thing once, in the place it belongs, and link to it elsewhere.
* Use the serial (Oxford) comma in lists of three or more items.
* Do not use em-dashes. Avoid colons, semicolons, and en-dashes in prose sentences. Split sentences where needed.
* Colons are fine in headings, labels, and lines that introduce a list or formula.

## Markdown

* Write full lines without hard wrapping at a fixed column width. Break at structural boundaries such as headings, paragraphs, and list items.
* Use spaces rather than tabs. Indent nested list content to align with the parent item's content, normally two spaces for bullets.
* Use one level-one heading for the document title and a consistent heading hierarchy.
* Use title case for headings.
* Capitalize the first word of list items. Preserve the exact spelling of code identifiers.
* Leave a blank line around lists and fenced code blocks.
* Specify a language for fenced code blocks when applicable, and use `text` for directory trees or plain output.
* Use descriptive link text and relative links for files within the repository.

## Diagrams

* Use a diagram when it explains relationships or behavior more clearly than prose.
* Keep editable diagram sources with the document or in an adjacent `assets/` directory.
* Use the project's chosen diagram format. Document rendering instructions when a tool is required.
* Render and inspect new or changed diagrams. Fix overlapping labels, unclear arrows, and unreadable layouts.
* Keep labels short and put detailed conditions or explanations in the surrounding text or tables.

## Language-Specific Rules

### Hugo Templates and Site Code

* Follow the surrounding Go template, HTML, CSS, and JavaScript conventions. Shared editor settings use four spaces. Existing code is not reformatted solely to change indentation.
* Keep shared rendering in `layouts/partials/` and reusable authoring markup in `layouts/shortcodes/`.
* Use the shared image partial for processed assets. Keep paths relative to `assets/img/`.
* Keep CSS responsibilities and import order explicit, as [Styling](guides/styling.md) describes.
* TOML and YAML configuration use two spaces for indentation. Keep project front matter in YAML, following [Authoring](guides/authoring.md).
* Verify template and configuration changes with a production Hugo build and a local preview. There is no configured frontend formatter or JavaScript linter.

### Python and Shell

* Python tools use the standard library, four-space indentation, and descriptive snake_case names. Resolve default repository paths from the script location so commands work after relocation and from other working directories.
* Check scripts must report actionable failures and exit nonzero when their registered check fails. Maintenance utilities that write content must be documented separately from read-only checks.
* Keep shell setup repeatable. Use `set -eu` and quote paths and variable expansions.
* Run the [repository checks](../tools/README.md) after tooling changes. Add focused regression tests when check behavior changes. No external formatter or Python package installation is required.

## Content-Writing Exception

Portfolio content in `content/` and the personal backlog in `TODO.md` retain the author's voice and existing heading style. The repository prose and acronym conventions do not require rewriting that material. Shared whitespace rules still apply, and project metadata must pass the front-matter check. Repository documentation, including this directory and the dev container instructions, follows the conventions above.
