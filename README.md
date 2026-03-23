# Hugo site: clean source workflow

This repository stores Hugo source files only. Generated output is built in CI and deployed automatically.

## Local workflow

1. Edit content, templates, or static files.
2. Preview locally.
3. Run a production build check.

```bash
# Local preview (drafts included)
hugo server -D

# Production build validation
hugo --gc --minify
```

## Git workflow

```bash
git status
git add .
git commit -m "Describe change"
git push
```

Do not commit generated directories such as `public/` or `resources/`.

## Deployment workflow

- `deploy-hugo.yml` builds and deploys to `gavintranquilino.github.io`.
- `update-resume-pdf.yml` syncs resume PDF into `static/resume.pdf`.

## Authoring conventions

### New project content

1. Create one markdown file in `content/projects/`.
2. Add project images to `assets/img/<project-slug>/`.
3. Use the `img` shortcode for in-content images.

Example:

```markdown
{{< img src="project-slug/cover.jpg" alt="Project cover" >}}
```

### Front matter guidelines

- Keep metadata plain text (no HTML in `title` or `subtitle`).
- Quote dates in ISO format (`"YYYY-MM-DD"`).
- Keep `imageUrl` and `thumbnailUrl` relative to `img/`.

## Utility scripts

- `data_processor.py`: converts markdown image links like `/img/...` to `img` shortcodes.

```bash
# default: content/projects under this repo
python3 data_processor.py

# optional custom directory
python3 data_processor.py /path/to/projects
```

## Structure summary

```text
content/      Markdown pages and project entries
layouts/      Hugo templates, partials, shortcodes
assets/       Hugo-processed source assets
static/       Static files copied as-is
public/       Generated output (ignored)
resources/    Hugo generated cache (ignored)
```

