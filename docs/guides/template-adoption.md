# Template Adoption

This repository adopts [template-devcontainer](https://github.com/gavintranquilino/template-devcontainer) as a shared foundation. The template supplies repository conventions, provider-neutral assistant instructions, editor and Git settings, Python checks, a pull request template, and a Linux dev container.

## Hugo Adaptations

* The root README and guides describe this site rather than template creation.
* The dev container installs standard Hugo 0.127.0 with checksum verification. CI and deployment build the same Dockerfile. The version remains pinned to preserve existing template behavior.
* Port 1313 is published with `appPort`, so the preview works from the dev container CLI as well as supported editors.
* `tools/scripts/` includes the existing front-matter checker, normalizer, and image converter. The checker runs in strict mode through the shared runner and CI.
* Repository documentation uses the glossary rules. Portfolio copy in `content/` and the personal backlog in `TODO.md` are excluded from the acronym check. Hugo content is excluded from the repository-relative Markdown link check because its paths use site routes and processed assets.
* `.editorconfig` includes the site's languages, and `.gitignore` excludes Hugo output and Python caches.
* The existing deployment and resume synchronization remain in place. The resume bot's direct updates to `main` are documented in [Deployment](deployment.md).

See [Coding Style](../coding-style.md) for the content-writing exception and language rules.

## Future Template Updates

Copying template files does not establish automatic inheritance. Compare future template changes with this repository in a separate branch. Preserve the Hugo additions, local check registration, and documented scope exceptions. Update related documentation and run the full [verification workflow](../../CONTRIBUTING.md#verification) before requesting review.

The template does not supply a license. This repository does not currently declare one. The owner must choose an appropriate license before offering reuse rights.
