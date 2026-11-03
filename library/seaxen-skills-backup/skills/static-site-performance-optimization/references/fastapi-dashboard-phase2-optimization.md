# FastAPI dashboard phase-2 optimization

Use this when a small self-hosted dashboard is already functionally correct but still wastes browser or server work.

## Situation pattern
- FastAPI app serving one large dashboard page
- heavy inline JS in `index.html`
- CDN-hosted frontend dependency (for example Chart.js)
- Docker image larger than necessary because build context includes `.venv`, `.git`, caches, logs, or local DBs
- dashboard polls every section too often

## High-value changes

### 1) Add `.dockerignore` first
Typical entries:

```gitignore
.git
.gitignore
.venv
__pycache__/
*.pyc
*.pyo
*.pyd
.env
*.log
*.sqlite
*.db
.pytest_cache/
.mypy_cache/
.DS_Store
```

Why: the biggest easy image win is often not base image surgery but simply stopping Docker from copying local junk into the build context.

### 2) Externalize large inline JS
Move the monolithic inline `<script>` block from `index.html` into `static/js/dashboard.js` and load it with a versioned URL:

```html
<script src="/static/js/dashboard.js?v=3"></script>
```

Why:
- smaller HTML payload
- browser can cache JS independently
- cleaner future edits
- easier to diff and profile

### 3) Self-host critical CDN assets
If the page depends on a CDN script like Chart.js, vendor a known-good copy into `static/js/` and switch the tag:

```html
<script src="/static/js/chart.umd.min.js?v=1"></script>
```

Why:
- removes CDN dependency
- improves repeat-load caching on LAN dashboards
- avoids third-party latency or outage on internal tools

### 4) Add gzip for larger responses
For FastAPI:

```python
from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware, minimum_size=1024)
```

Use for:
- JSON endpoints
- JS/CSS payloads
- larger HTML responses

### 5) Add static cache headers
For FastAPI/Starlette, add middleware that sets cache policy by suffix:

- JS/CSS: `public, max-age=86400, immutable`
- images/icons: `public, max-age=604800, immutable`

This is especially useful when asset URLs already carry version query strings.

### 6) Split refresh cadence
Do not refresh all sections every minute.

Recommended pattern:
- core cards / health / recent queries: every 60s
- heavy analytics / charts / historical sections: every 3 min desktop, 5 min mobile

Why: this reduces backend log parsing, chart churn, and mobile CPU drain without making the dashboard feel stale.

## Verification pattern
After deployment, verify with real measurements:

1. image size before vs after
2. container CPU / RAM at idle
3. endpoint cold time vs warm cached time
4. static cache headers via `HEAD`
5. key page/API still returns 200

Example success pattern:
- cold overview endpoint still takes hundreds or thousands of ms
- repeated warm calls fall to low single-digit ms after cache
- image size drops materially after `.dockerignore`
- HTML file shrinks after JS extraction

## Important nuance
If `HEAD` checks do not show `Content-Encoding: gzip`, do not conclude compression failed. Confirm with a real `GET` that sends `Accept-Encoding`, or note that small files may not be compressed.
