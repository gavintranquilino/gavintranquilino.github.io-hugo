# Gavin Tranquilino's Website

Source for [gavintranquilino.com](https://gavintranquilino.com), a personal portfolio built with Hugo. Project pages, images, templates, and styles live here. GitHub Actions builds the source and publishes the generated site to a separate repository.

The repository adopts the conventions and development environment from [template-devcontainer](https://github.com/gavintranquilino/template-devcontainer). See [Template Adoption](docs/guides/template-adoption.md) for project adaptations and maintenance.

## Start Here

* **Set up development:** Follow [Dev Container](.devcontainer/README.md). It includes the pinned Hugo version, Python 3, and Git.
* **Add a project:** Follow [Authoring](docs/guides/authoring.md).
* **Contribute:** Read [Contributing](CONTRIBUTING.md), [Coding Style](docs/coding-style.md), and [Documentation](docs/documentation.md).
* **Find documentation:** Open the [Documentation Map](docs/README.md).
* **AI assistants:** Read [Repository Instructions](AGENTS.md).

## Preview, Build, and Check

Run these commands from the repository root on your machine. A container engine and the dev container CLI are required. See [Dev Container](.devcontainer/README.md) for installation and Podman instructions.

```sh
devcontainer up --workspace-folder .
devcontainer exec --workspace-folder . hugo server --bind 0.0.0.0 --buildDrafts
```

Open <http://localhost:1313/>. Stop the preview with Ctrl+C. Before requesting review, run the repository checks and a production build.

```sh
devcontainer exec --workspace-folder . python3 tools/scripts/run_checks.py
devcontainer exec --workspace-folder . hugo --gc --minify
```

[Tools](tools/README.md) describes each check and how to run the Python checks without a container. Build output in `public/` and the generated cache in `resources/` are ignored by Git.

## Repository Layout

| Path | Contents |
| --- | --- |
| `hugo.toml` | Site settings and project permalinks |
| `content/_index.md` | Home page metadata and biography |
| `content/projects/` | Project pages with YAML front matter |
| `archetypes/` | Templates for new pages, including the project metadata schema |
| `layouts/` | Hugo page templates, shared partials, image render hook, and shortcodes |
| `assets/img/` | Source images processed and resized by Hugo |
| `static/` | Files copied as supplied, including CSS, JavaScript, and the resume |
| [`.devcontainer/`](.devcontainer/README.md) | Shared development image and setup |
| `.github/` | Pull request template, checks, deployment, and resume workflows |
| [`tools/`](tools/README.md) | Repository checks and content maintenance scripts |
| [`docs/`](docs/README.md) | Conventions and development guides |
| [TODO.md](TODO.md) | Personal project and site feature backlog |

## Deployment

[Deployment](docs/guides/deployment.md) explains the existing GitHub Pages publishing and resume workflows, including required secrets. Pull requests run repository checks and a Hugo build without publishing. Merging to `main` triggers deployment.

## Styling

[Styling](docs/guides/styling.md) explains the CSS module order and template entry points. Keep visual changes separate from tooling changes so their effect is easy to review.
