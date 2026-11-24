# Authoring

Use the [dev container](../../.devcontainer/README.md) for the commands below. Run them from the repository root on your machine.

## Create a Project

```sh
devcontainer exec --workspace-folder . hugo new content projects/my-project.md
```

Hugo uses `archetypes/projects.md` to create a draft with the required metadata. Edit `content/projects/my-project.md`, add images under `assets/img/my-project/`, and fill in the front matter.

```yaml
---
title: "My Project"
date: "2026-11-24"
draft: true
imageUrl: "my-project/cover.jpg"
thumbnailUrl: "my-project/thumbnail.jpg"
subtitle: "A short description of the project"
bulletPoints:
  - "What I built and why it matters"
weight: 10
---
```

* Keep `title` and `subtitle` plain text. Existing templates allow HTML in `bulletPoints`.
* Use double quotes around dates in `YYYY-MM-DD` form.
* `title`, `date`, `imageUrl`, `subtitle`, and `bulletPoints` must exist. The lightweight [front-matter check](../../tools/README.md#front-matter) checks these keys, duplicate top-level keys, title and subtitle markup, and date syntax. Hugo validates the complete YAML during builds.
* `thumbnailUrl` is optional. The home page falls back to `imageUrl`.
* Both image fields are relative to `assets/img/`, without an `img/` prefix.
* `weight` is optional and controls the home page ordering through Hugo's `ByWeight` sort.
* Remove `draft: true` or set it to `false` when ready to publish. Production builds omit drafts and future-dated pages. The preview includes drafts. Add `--buildFuture` to the preview command if needed.

Project URLs use the filename, as configured in `hugo.toml`. For example, `my-project.md` becomes `/my-project/`. Renaming a file changes its URL, so check existing inbound links before doing so.

## Images and Shortcodes

Use the `img` shortcode for images processed by Hugo.

```text
{{< img src="my-project/cover.jpg" alt="Describe the image" size="800x" quality="q85" >}}
```

`size` defaults to `400x`, `quality` to `q75`, and `loading` to `lazy`. Supply meaningful alt text. The shared image partial reports a build error when the referenced asset is missing. Ordinary Markdown image links are rendered directly and do not use this resizing pipeline.

Other existing shortcodes in `layouts/shortcodes/` include `slideshow` with nested `slide` entries, `my_video_embed`, `local_video`, `google_photos_album`, `custom_link`, and `icon`. Follow an existing project using the shortcode when adding an embed.

## Preview and Verify

```sh
devcontainer exec --workspace-folder . hugo server --bind 0.0.0.0 --buildDrafts
devcontainer exec --workspace-folder . python3 tools/scripts/run_checks.py
devcontainer exec --workspace-folder . hugo --gc --minify
```

Stop the preview before running the other commands. Open the changed project and its home page card. Check text, images, links, and mobile layout. Production builds exclude drafts, so inspect draft pages in the preview before publishing.

The home page's sections and biography come from `content/_index.md`. Keep repository documentation in `docs/`, because Markdown placed under `content/` becomes site content.

For older content, [Tools](../../tools/README.md#maintenance-utilities) documents the front-matter normalizer and image-link converter. They edit files, so inspect the diff afterward.
