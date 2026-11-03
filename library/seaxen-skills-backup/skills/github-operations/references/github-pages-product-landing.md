# GitHub Pages product landing (docs/)

Use when the user wants a **marketing landing page** for an existing GitHub repo (not the app runtime). The app may already run elsewhere (e.g. Flask on `:6677`); Pages hosts static HTML only.

## Canonical layout

```
docs/
├── index.html       # landing
├── landing.css      # self-contained styles (or reuse app CSS variables)
├── .nojekyll        # empty file — skip Jekyll on user/org Pages
├── systor-logo.png  # reuse README / app static assets
└── screen-*.png     # screenshots already in docs for README
```

**Do not** put the Flask app in `docs/` — only static assets.

## Workflow

1. **Sync local clone with remote** before assuming assets exist locally:
   ```bash
   cd /path/to/repo && git fetch origin && git pull --ff-only origin main
   ```
   README often references `docs/screen-*.png` that only exist on `origin/main`.

2. **Match visual brand** to the running product when one exists:
   - Copy `:root` CSS variables from the app's `static/css/style.css` (GitHub-dark palette).
   - Link live demo URL if README already badges one (e.g. `https://systor.xuup.top/`).

3. **Content blocks that work** for self-hosted tools:
   - Hero + install one-liner (`git clone` + `sudo ./install.sh`)
   - Comparison table vs heavy alternatives (Prometheus/Grafana, etc.)
   - Feature grid aligned with real nav tabs/pages
   - Screenshots from `docs/` (lazy-load images)
   - Links: GitHub, releases tag, live demo, MIT license

4. **README updates** (same commit):
   - Badge linking to `https://<user>.github.io/<repo>/`
   - Short section: **Settings → Pages → branch `main` → folder `/docs`**

5. **Enable Pages** (CLI, after push):
   ```bash
   gh api -X POST repos/<owner>/<repo>/pages \
     -f build_type=legacy \
     -f 'source[branch]=main' \
     -f 'source[path]=/docs'
   ```
   Verify config:
   ```bash
   gh api repos/<owner>/<repo>/pages --jq '{html_url,source,public}'
   ```

6. **Verify deploy** (expect transient 404 for 1–5 min after first enable):
   ```bash
   curl -sI "https://<user>.github.io/<repo>/" | head -5
   ```
   Local preview before push:
   ```bash
   cd docs && python3 -m http.server 8766 --bind 127.0.0.1
   ```

## Pitfalls

- **404 right after enable** is normal until GitHub finishes the first build; do not revert files immediately.
- **`gh api .../pages` returns 404** before any Pages config exists; `POST` creates it. After config exists, use `GET` only.
- **Jekyll breaks plain HTML** if `.nojekyll` is missing (underscore paths, etc.).
- **Broken images on Pages** when `index.html` uses paths like `../systor/static/...` — keep all assets under `docs/` with relative names.
- **Do not conflate** Pages URL with the app's production URL; badge both if both exist.

## SeaXen / systor reference

| Item | Value |
|------|--------|
| Local clone | `/mnt/tb/1Apps/systor` |
| Remote | `SeaXen/systor` |
| Pages URL | `https://seaxen.github.io/systor/` |
| Live app demo | `https://systor.xuup.top/` (separate from Pages) |

Commit message pattern: `docs: add GitHub Pages landing site in docs/`