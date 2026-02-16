## Hugo site: notes + workflow

This repo is a Hugo site. It contains both the source content and the generated site output. The goal of this README is to document how to work on the site, build it, and publish it, plus explain what each folder does.

---

### Quick workflow (local)

1. Edit content or templates.
2. Preview locally.
3. Build the static site.
4. Publish the built output.

Commands:

```bash
# Local preview (drafts included)
hugo server -D

# Production build (outputs to public/)
hugo
```

Notes:
- `hugo server -D` watches files and auto-reloads.
- `hugo` writes the final static site into `public/`.

---

### Publish workflow (assumed)

Because `public/` exists in this repo, the current setup appears to be:

1. Build: `hugo` to refresh `public/`.
2. Commit both source changes and `public/` output.
3. Push to your remote host.

If your hosting is different (Netlify, GitHub Actions, etc.), change this section to match. The only thing Hugo requires is a build step that produces `public/`.

---

### Git workflow (assumed)

Typical flow when editing:

```bash
# Check what changed
git status

# Add changes (content, layouts, and public/ if you publish it from this repo)
git add .

# Commit with a short message
git commit -m "Update site"

# Push to your remote
git push
```

If you use branches or PRs, update this section with your preferred flow.

---

### File structure (diagram)

```text
.
├── archetypes/
│   └── default.md
├── assets/
│   └── img/
│       └── (image folders per project)
├── content/
│   ├── _index.md
│   └── projects/
│       └── (one markdown file per project)
├── layouts/
│   ├── _default/
│   │   ├── 404.html
│   │   ├── baseof.html
│   │   ├── section.html
│   │   ├── taxonomy.html
│   │   └── _markup/
│   ├── index.html
│   ├── partials/
│   ├── projects/
│   └── shortcodes/
├── public/
│   └── (generated static site output)
├── resources/
│   └── _gen/
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── data_processor.py
├── hugo.toml
├── README.md
└── TODO.md
```

---

### Folder and file descriptions

#### Root files

- `hugo.toml`: Hugo config (base URL, permalinks, renderer settings).
- `README.md`: You are here. Workflow + structure notes.
- `TODO.md`: Project ideas and feature backlog.
- `data_processor.py`: Helper script to convert Markdown image links to the `img` shortcode for project content.

#### Content and data

- `content/`: Markdown content for the site.
	- `content/_index.md`: Home page content.
	- `content/projects/`: One Markdown file per project; permalinks are set to `/:filename/`.

#### Templates and rendering

- `layouts/`: Hugo templates and partials.
	- `layouts/index.html`: Home page template.
	- `layouts/_default/`: Default templates (section, taxonomy, etc.).
	- `layouts/partials/`: Reusable template fragments.
	- `layouts/shortcodes/`: Custom shortcodes (used by content, e.g., `img`).
	- `layouts/projects/`: Project-specific templates (if any).

#### Assets and static files

- `assets/`: Hugo Pipes assets (processed by Hugo). Current usage: images per project.
- `static/`: Files copied verbatim to the output site (`/css`, `/img`, `/js`).

#### Generated output and caches

- `public/`: Build output from `hugo` (the live site HTML/CSS/JS).
- `resources/_gen/`: Hugo cache for processed assets.

---

### Helpful reminders

- If you add a new project, add a Markdown file in `content/projects/` and images in `assets/img/<project>/`.
- If images are referenced as `/img/...` in Markdown, run `data_processor.py` to convert them to the `img` shortcode format.
- `public/` should always be rebuilt after content or template changes if you publish from this repo.

---

### Next steps (optional)

If any of the assumptions above are wrong, tell me:
- how you actually deploy (GitHub Pages, Netlify, etc.)
- whether `public/` should be committed or ignored
- whether you use branches or a PR workflow

