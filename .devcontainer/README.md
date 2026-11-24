# Dev Container

The dev container gives every contributor the same Linux development environment, whatever their operating system or editor. It includes the Hugo version that the deploy workflow uses, so a site that builds in the container builds the same way in CI. Preview, build, and check the site inside it, so that each contributor needs only a few tools on their own machine.

## What Is Included

The image is defined in the [Dockerfile](Dockerfile) and configured by [devcontainer.json](devcontainer.json).

* **Operating system:** Ubuntu 26.04 LTS.
* **Hugo:** The standard edition, at the version pinned by `HUGO_VERSION` in the Dockerfile. The download is verified against the release checksum.
* **Tools:** Git, Python 3 for the [repository checks](../tools/README.md), curl, `sudo`, and common command-line utilities.
* **User:** A non-root user named `dev`, which can run `sudo` without a password.
* **Workspace:** The repository is mounted at `/workspaces/<repository-folder-name>`. Changes made inside the container are changes to your local files.
* **Preview port:** Port 1313, which `hugo server` uses, is published on the host.
* **Setup script:** [post-create.sh](post-create.sh) runs once after the container is created.

## Prerequisites

Install these on your machine once.

* **A container engine:** [Docker Desktop](https://docs.docker.com/get-docker/) on Windows or macOS, or Docker Engine or [Podman](https://podman.io/) on Linux.
* **The dev container CLI:** Install [Node.js](https://nodejs.org/), then run `npm install -g @devcontainers/cli`.
* **uv (optional):** [uv](https://docs.astral.sh/uv/) runs the repository's Python tools on your machine without a separate Python installation, as [Working Outside the Container](#working-outside-the-container) shows.

No editor is required. Any editor can work on the mounted files while you run commands in a shell inside the container.

On Windows, use Docker Desktop with the WSL 2 backend, and clone the repository inside your WSL distribution rather than on a Windows drive. Files on a Windows drive are much slower inside the container.

## Quick Start

Run these commands from the repository root.

```sh
devcontainer up --workspace-folder .
devcontainer exec --workspace-folder . bash
```

`devcontainer up` builds the image and starts the container. The first build takes a few minutes, and later runs reuse the existing container. `devcontainer exec` opens a shell in the container, in the repository folder. Run `exit` to leave the shell. The container keeps running in the background.

To run a single command without opening a shell, pass it to `devcontainer exec`.

```sh
devcontainer exec --workspace-folder . python3 tools/scripts/run_checks.py
```

To shorten these commands, add a shell alias on your machine.

```sh
alias dcx='devcontainer exec --workspace-folder .'
```

With Podman, add `--docker-path podman` to each `devcontainer` command, and use `podman` in place of `docker` in other commands.

## Everyday Tasks

| Task | Command, from the repository root |
| --- | --- |
| Start the container | `devcontainer up --workspace-folder .` |
| Open a shell | `devcontainer exec --workspace-folder . bash` |
| Preview the site, including drafts | `devcontainer exec --workspace-folder . hugo server --bind 0.0.0.0 --buildDrafts` |
| Build the site as the deploy workflow does | `devcontainer exec --workspace-folder . hugo --gc --minify` |
| Run the repository checks | `devcontainer exec --workspace-folder . python3 tools/scripts/run_checks.py` |
| Rebuild after changing the dev container files | `devcontainer up --workspace-folder . --remove-existing-container` |
| Stop and remove the container | `docker rm -f $(docker ps -aq --filter "label=devcontainer.local_folder=$PWD")` |

While the preview server runs, open <http://localhost:1313/> on your machine. The page reloads when you save a file. Press Ctrl+C to stop the server. The `--bind 0.0.0.0` option is required because the server must accept connections from outside the container.

The build writes the site to `public/`, which Git ignores. Removing the container discards anything installed outside the workspace, such as packages installed with `sudo apt-get`. Add tools you want to keep to the Dockerfile.

## Using an Editor

Editors with dev container support can open the same container. This is optional, and every task works from a shell.

* **VS Code:** Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension, open the repository, and run **Dev Containers: Reopen in Container** from the Command Palette.
* **JetBrains IDEs:** Open the repository's `devcontainer.json` and choose to create a dev container from it.
* **Other editors:** Edit the files on your machine and run commands in a container shell.

## Working Outside the Container

The [repository checks](../tools/README.md) need only Python 3 and Git, so you can also run them on your machine. With uv, which provides Python automatically, run the following.

```sh
uv run --no-project tools/scripts/run_checks.py
```

Previewing and building the site need Hugo. Use the container for those, so that you build with the same Hugo version as CI.

## Customizing the Container

Change the shared dev container files in a pull request, so that every contributor and CI get the same environment.

* **Hugo version:** Change `HUGO_VERSION` in the Dockerfile and rebuild the container. The [checks workflow](../.github/workflows/checks.yml) and [deploy workflow](../.github/workflows/deploy-hugo.yml) build this image, so CI follows the change. Build and preview the site before opening the pull request, since Hugo releases can change template behavior.
* **Toolchains and system packages:** Add them to the Dockerfile in their own `RUN` instruction, and pin their versions. For example, install a compiler with `apt-get`, or copy a language's version manager or package manager from its official image.
* **Project setup:** Add steps to `post-create.sh` that need the mounted workspace, such as installing dependencies. Keep each step safe to run again.
* **Environment variables:** Add them to `containerEnv` in `devcontainer.json`. Keep secrets out of the repository and out of the image.
* **Ports:** List ports that the project serves in `appPort` in `devcontainer.json`. This repository uses `appPort` rather than the template's `forwardPorts`, because the dev container CLI ignores `forwardPorts`. Editors honor both.
* **Editor settings:** Add extensions and settings under `customizations` in `devcontainer.json`. Keep the container usable without them.

Document the site's build, preview, and check commands in the [root README](../README.md), and state that they run in the dev container.

The Dockerfile's stage is named `dev`. A runtime image could add build and runtime stages to the same Dockerfile and keep this stage for development.

## Troubleshooting

* **Changes to the Dockerfile have no effect:** Rebuild with `--remove-existing-container`, as shown in [Everyday Tasks](#everyday-tasks).
* **The preview page does not load:** Check that the server was started with `--bind 0.0.0.0`. If another program uses port 1313 on your machine, stop it and recreate the container with `--remove-existing-container`.
* **The preview does not reload after you save a file:** Some file systems do not report changes to the container. Add `--poll 700ms` to the `hugo server` command.
* **Git reports dubious ownership:** `post-create.sh` marks the workspace as safe. If you created the container before this step existed, rebuild it.
* **Files created in the container belong to another user:** The CLI matches the `dev` user's ID to yours on Linux. If you start the image another way, run it with your user ID, for example with `--user "$(id -u):$(id -g)"`.
* **Paths break in Git Bash on Windows:** Git Bash rewrites path arguments before Docker sees them. Run the commands in WSL, or set `MSYS_NO_PATHCONV=1`.
