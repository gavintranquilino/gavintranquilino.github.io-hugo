# Contributing

Read the [Coding Style](docs/coding-style.md) and [Documentation](docs/documentation.md) conventions before making changes. Check for additional guidance in the area you are changing.

## Branches and Pull Requests

* Start each piece of work on a short-lived branch from the repository's default branch.
* Use pull requests for most changes and avoid direct commits to the default branch. Prefer a small pull request even for documentation or configuration changes.
* Keep each pull request focused on one coherent change. Open a draft when early feedback would help.
* Keep commits atomic and write succinct commit messages that describe the change.
* Before review, bring the branch up to date with the default branch and resolve conflicts.
* Keep the pull request title and description current as its scope changes.

## Making Changes

* Follow root conventions and any applicable component guidance. Local exceptions must be explicit.
* Keep unrelated cleanup out of the change.
* Update documentation in the same pull request as the behavior or workflow it describes.
* When adding, moving, or removing a directory, update its README and its parent's README as [Documentation](docs/documentation.md#directory-readmes) describes.
* Discuss substantial design choices in a lightweight proposal when they need agreement before implementation. Routine changes can be discussed in the pull request.
* Explain why a new dependency is needed and consider its maintenance, license, and effect on users.
* Identify generated files and document the command and prerequisites used to regenerate them. Change their source and regenerate the output rather than editing generated output by hand.
* Keep secrets, credentials, and machine-specific configuration out of version control. Provide example configuration with placeholders when setup needs it.

## Verification

* Run the relevant checks documented by the project or component before requesting review. Run builds, tests, and checks in the [dev container](.devcontainer/README.md) so that results match CI.
* Add or update tests when behavior changes. Choose verification appropriate to the change and its risk.
* For documentation changes, check links, examples, and instructions.
* Report what you checked and any checks you could not run, with the reason.
* When introducing tooling, document its prerequisites and how to run the same checks locally.

Pull requests run the checks described in [Tools](tools/README.md) and a production Hugo build in the development image. The [root README](README.md#preview-build-and-check) gives the commands to run locally.

## Review

A pull request should explain the problem, the resulting behavior, and how the change was verified. Include limitations or follow-up work when they affect review. The [pull request template](.github/pull_request_template.md) provides sections for changes, testing, and impact. Disclose when AI tools contributed to the change.

Address review feedback and complete applicable checks before merging. Follow the repository's configured review requirements.
