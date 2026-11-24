# Deployment

GitHub Actions builds this source repository and publishes the site to [gavintranquilino.github.io](https://github.com/gavintranquilino/gavintranquilino.github.io). Generated files are not committed here.

## Pull Request Checks

[checks.yml](../../.github/workflows/checks.yml) runs on pull requests, pushes to `main`, and manual dispatch.

* `check/acronyms`, `check/links`, `check/whitespace`, `check/frontmatter`, and `check/tooling` run the [Python checks](../../tools/README.md) independently.
* `build/hugo` builds the `dev` image from `.devcontainer/Dockerfile`, then runs `hugo --gc --minify` against the checked-out source. It uses the same image definition as local development and deployment.

These checks do not publish the site or require deployment credentials. A workflow alone does not make checks mandatory for merging. Configure required status checks in GitHub's branch protection or repository rules if desired.

## Publish the Site

[deploy-hugo.yml](../../.github/workflows/deploy-hugo.yml) runs on pushes to `main`, manual dispatch, and completion of the resume workflow on `main`.

1. Check out the source.
2. Build the development image and run `hugo --gc --minify` inside it.
3. Write `public/CNAME` with `gavintranquilino.com`.
4. Publish `public/` to the `master` branch of the external Pages repository.

The Hugo version is pinned only in [.devcontainer/Dockerfile](../../.devcontainer/Dockerfile). To update it, change `HUGO_VERSION`, rebuild the container, and verify a preview and production build in a pull request.

The repository secret `GH_PAT_FOR_DEPLOY` must hold a token with permission to push to the external Pages repository. Manage it in GitHub's Actions secrets settings. The normal `GITHUB_TOKEN` cannot push to that separate repository. Preserve the existing Pages and custom-domain settings there.

## Resume Updates

[update-resume-pdf.yml](../../.github/workflows/update-resume-pdf.yml) runs on a `repository_dispatch` event of type `pdf_update` or manual dispatch. It downloads the PDF from [gavins-resume](https://github.com/gavintranquilino/gavins-resume), commits it as `static/resume.pdf` on `main` when changed, and attempts to copy it into the Pages repository. Its cross-repository push also uses `GH_PAT_FOR_DEPLOY`.

This bot update is an explicit exception to the usual pull request workflow. The deploy workflow's `workflow_run` trigger rebuilds the site afterward, including updates committed with `GITHUB_TOKEN`. The resume workflow retains its existing error-tolerant push behavior. Inspect both workflows' logs if the PDF does not update.
