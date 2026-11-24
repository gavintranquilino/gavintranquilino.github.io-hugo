# Documentation

Read this page before writing, moving, or splitting documentation. Keep each fact in one place and link to it from elsewhere.

## Scope and Placement

Repository-wide guidance lives at the root or in `docs/`. Documentation about one component lives beside that component so it can change with the code. These rules apply to both single-project repositories and monorepos.

| Kind | Purpose | Location |
| --- | --- | --- |
| README | Explain a repository or component, its setup, and its common commands | At the root or beside the component |
| Repository convention | Define shared working rules | At the root or in `docs/` |
| Guide | Teach a task, concept, or workflow | In `docs/guides/` or beside the component it covers |
| Design document | Explain the current design and its tradeoffs | In `docs/design/` or a component's `design/` directory |
| Proposal | Discuss a change before it is decided | In `docs/proposals/` or a component's `proposals/` directory |

Create optional directories only when they have content. No particular source layout or external documentation system is required.

Root conventions apply across the repository. Local guidance can extend them and must clearly identify any exceptions. Put a component's setup and verification commands in its README. Explain shared workflows and component relationships at the root.

## Directory READMEs

READMEs let a reader understand any directory without opening its files, and browse from the root down.

* The root README explains the repository's purpose, structure, setup, and common workflows, with links to detailed instructions.
* Give a directory a README when its purpose or contents are not obvious from its name and its parent README. This normally includes top-level directories, components, and directories that group several kinds of content.
* A README describes what the directory contains, how its contents relate, and any instructions specific to it.
* A parent README lists its significant subdirectories with a one-line description each and links to their READMEs. Keep details in the child README rather than repeating them.
* Update the affected READMEs when adding, moving, or removing a directory.

The following directories do not need READMEs.

* Hidden tool configuration directories such as `.github/`. GitHub shows `.github/README.md` in place of the root README, so do not add one there.
* Generated, vendored, and build-output directories.
* Directories whose purpose is clear from their name and parent README, such as `assets/`, test fixtures, or nested package paths required by a language.

## Guides

* A guide explains its prerequisites, steps, and expected result.
* Document commands from the directory where they should run.
* Describe capabilities and tools that actually exist. Add instructions for optional tooling when that tooling is introduced.

## Design Documents

Keep the structure proportionate to the design. A lightweight design document should explain the following.

* **Purpose and scope:** The problem it addresses and the boundaries it covers.
* **Approach:** The components, interfaces, data flow, or behavior needed to understand the design.
* **Tradeoffs:** Important choices, alternatives, and constraints.
* **Open questions:** Unresolved decisions and assumptions that still need confirmation.

Describe the current design. Update the relevant document in the same pull request as a design change, and use Git history for earlier versions. Link to supporting code, guides, proposals, or external references where useful. No document number or external approval system is required.

## Proposals

Use a proposal when a change needs discussion before implementation. Routine changes can be discussed directly in their pull request.

* Use a descriptive filename such as `shared-configuration.md`.
* Put a status below the title, for example `**Status:** Draft`.
* Explain the problem, proposed change, and relevant alternatives or tradeoffs.
* Record the outcome when decided. Use Draft, Accepted, Rejected, or Superseded, with a link to the discussion or replacement when available.
* Keep the proposal as a decision record. Once implemented, put the current behavior in the relevant design document, guide, or README and link to it from the proposal.

Use the project's chosen place for task tracking, and document it when relevant. Keep design explanations readable independently of task status.

## Links, Assets, and Naming

* Keep [the documentation map](README.md) and relevant guide indexes up to date when documents are added, moved, or removed.
* Use relative links within the repository and check them after moving files.
* Keep supporting assets beside their document, using an `assets/` directory when helpful.
* Use lowercase, hyphen-separated names for documents and directories. Keep established entry-point names such as `README.md`, `CONTRIBUTING.md`, and `AGENTS.md`.
* Follow [Coding Style](coding-style.md) for prose, Markdown, and diagrams.
* Define shared terminology in the [Glossary](glossary.md) and link to definitions rather than maintaining duplicate copies.
