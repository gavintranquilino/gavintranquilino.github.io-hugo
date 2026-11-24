# Styling

The site uses custom Hugo templates and plain CSS, without a theme or frontend package manager. Use the [dev container](../../.devcontainer/README.md) to preview changes.

## Entry Points

* `layouts/_default/baseof.html` loads the shared stylesheet, header, footer, and page content.
* `layouts/index.html` renders the home page and the three project views.
* `layouts/projects/single.html` renders a project page or its configured redirect.
* `layouts/_default/list.html` renders section lists.
* `static/js/index.js` handles navigation, project view toggles, and slideshows.

## CSS Modules

`static/css/style.css` imports the files below from `static/css/modules/` in cascade order.

| Module | Responsibility |
| --- | --- |
| `00-tokens-theme.css` | Shared colors, theme values, and variables |
| `01-base-typography.css` | Base elements and typography |
| `02-header-nav.css` | Header and navigation |
| `03-sections.css` | Home page sections |
| `04-portfolio.css` | Project cards and view modes |
| `05-footer-links.css` | Footer and link presentation |
| `06-slideshow.css` | Slideshow presentation |
| `07-project-content.css` | Individual project content |
| `08-embeds-icons.css` | Embedded media and icons |

Prefer updating the existing module responsible for a component. When adding a module, update the imports and keep their order explicit.

## Review Changes

Preview the home page in all three project views and open a few short and long project pages. Check narrow and wide screens, navigation, keyboard focus, image captions, and embeds. Run the [repository checks](../../tools/README.md) and a production build before requesting review.

The current tooling has no automated visual regression checks. Include screenshots or a clear account of manual checks in a visual change's pull request.
