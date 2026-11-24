# Repository Instructions

These instructions apply to AI assistants working in this repository, regardless of provider or tool.

## Shared Conventions

* Read [Contributing](CONTRIBUTING.md) and [Coding Style](docs/coding-style.md) before making changes.
* Before writing, moving, or splitting documentation, read [Documentation](docs/documentation.md).
* Root conventions apply throughout the repository. Read any additional instructions in the area you are changing. Local guidance can extend root conventions and must explicitly identify any exceptions.
* Read the README of each directory you work in. When adding, moving, or removing a directory, update the affected READMEs as [Documentation](docs/documentation.md#directory-readmes) describes.
* Keep changes focused on the requested task and preserve unrelated work.

## Git and Review

* Follow the branch and pull request workflow in [Contributing](CONTRIBUTING.md). Work on a separate branch and avoid direct changes to the default branch.
* Keep commits atomic and commit messages succinct.
* Keep an existing pull request's title and description current when its scope changes.
* Prefix AI-generated pull request comments and replies with `AI:`.

## Verification

* Run the relevant documented checks and report their results. Run project commands in the [dev container](.devcontainer/README.md) when a container engine is available.
* State which checks could not be run and why.
* Update documentation when behavior or workflows change. Describe only tooling and automation actually available in the repository.
