Here's the review.

**Bottom line:** everything you listed is fine for the GitHub-rendered page and wrong for every other consumer of that same file — and because this is a 6-package monorepo where 4 packages publish to PyPI, "every other consumer" isn't hypothetical, it's your PyPI project pages.

### 1. Two READMEs, one of them is dead weight

GitHub's precedence for the repo homepage is root `README.md` first, `.github/README.md` only as a fallback if no root README exists. Since you have both, `.github/README.md` renders nowhere — `.github/` is not one of GitHub's recognized community-file locations for `README` (unlike `CONTRIBUTING.md`, issue templates, etc., which *do* fall back to `.github/`). So the drift you're seeing isn't two files serving two audiences that quietly diverged — it's one live file and one dead file, and whoever's been maintaining "the README" has been editing whichever one they happened to open. Decide which is canonical, delete the other (or generate one from the other in CI), and stop having two things to keep in sync at all.

Before deleting either: grep every package's `pyproject.toml` for its `readme = "..."` field. If any of the 4 PyPI packages point at `.github/README.md` rather than root, *that's* the file actually shipping to PyPI right now, regardless of which one "looks great on GitHub."

### 2. `docs/img/arch.png` — relative path, breaks off-GitHub

GitHub resolves `![architecture](docs/img/arch.png)` against the repo tree, so it works there. PyPI's `long_description` is rendered standalone with no git context — a repo-relative path resolves to nothing, so every PyPI project page that embeds this README shows a broken-image icon where the architecture diagram should be. This is the single most common "looks great on GitHub, dead on PyPI" bug, and it hits all 4 PyPI listings at once if they all reuse the root README as-is.

Fix: point the image at an absolute, version-pinned URL — `https://raw.githubusercontent.com/<org>/toolbelt/<tag>/docs/img/arch.png` — not a branch name that'll drift, and not a relative path. Same fix applies to any other relative links/images in the file (badges, other diagrams).

### 3. The 6MB demo GIF

Two separate problems stacked on one asset:

- **Same broken-link issue as the PNG** if it's referenced by relative path — dead on PyPI.
- **Packaging bloat** if the GIF file itself lives in the repo and isn't excluded from the sdist. Check `MANIFEST.in` / your build backend's include globs (`[tool.hatch.build]`, `include`/`exclude` in setuptools config, etc.) — if `docs/` isn't excluded, `python -m build` happily zips a 6MB binary into a source distribution meant to carry code. Confirm with `tar tzf dist/*.tar.gz | grep -i gif` (or the equivalent for whichever package's sdist embeds it) after a build.

Fix: host the GIF externally (GitHub's own asset CDN via a release/issue upload, or your docs site) and reference it by absolute URL. That solves both problems at once — no relative path, no bytes in the sdist.

### 4. `<details><summary>` config table

GitHub Flavored Markdown supports raw `<details>`/`<summary>` and renders it collapsed-by-default, which is why it looks great there. PyPI runs Markdown through `readme_renderer`, which sanitizes HTML against an explicit tag allowlist before rendering — recent versions of that allowlist do include `details`/`summary` for GitHub parity, but I haven't verified the specific version pinned in your build environment, and I'd rather flag it than assert it. Don't take it on faith either way: run `twine check dist/*` after building — it validates that the long_description actually renders, and will surface a stripped/mangled result if the installed `readme_renderer` version doesn't allow those tags. If it fails, the config table won't disappear, it'll dump flat and unstyled into the page — better than nothing, but worth knowing before someone lands on the PyPI page and finds a wall of unformatted table markup.

### 5. Monorepo fan-out — the part that turns 4 small bugs into 4× the blast radius

With 6 packages in one repo, check whether all 4 PyPI-published ones point their `readme` field at this same root file, or each has its own scoped README. If they share it, a user looking at `pypi.org/project/toolbelt-<subpackage>` — who wants docs for one package — gets the whole monorepo's marketing page: architecture diagram (broken), demo GIF (broken or bloating their download), and a config table that may or may not render, none of it scoped to the package they're actually installing. That's worth fixing independent of the rendering bugs: package-level PyPI pages should carry package-level docs, with the root README doing the "here's the whole toolbelt" tour on GitHub only.

### Suggested gate

Given this is a recurring class of bug (looks fine locally/on GitHub, breaks on the thing that actually matters — PyPI), it's worth a cheap pre-release check rather than catching it by hand next time: a pre-commit or CI step that greps every README wired into a `readme =` field for repo-relative image/link paths (`\]\([^h].*\)` style pattern, i.e. anything not starting `http`) and fails the build. Pair it with `twine check dist/*` in CI (if not already there) so the HTML-sanitization question in #4 gets answered by a machine on every release instead of by eyeballing the rendered page after the fact.