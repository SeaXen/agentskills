# SeaDash compact full-rewrite pattern

Use when SeaDash has become too messy for incremental CSS/JS repair and the user explicitly asks to rewrite the app from the beginning while preserving the useful operator features.

## Scope lock

Before rewriting, identify the active surface:
- app root, usually `/mnt/tb/1Apps/SeaDash`
- single-file frontend, usually `index.html`
- stdlib Python backend, usually `server.py`
- live service, usually `seadash.service` on port `9090`

If the app root is not a git repo, do **not** claim a clean git push is possible. Finish and verify the working app, then report that repo initialization/remote selection is a separate required step.

## Good V1 rewrite target

Keep the app dependency-free and low-overhead:
- single `index.html` with vanilla JS/CSS
- existing Python backend and JSON config APIs
- no npm/React/build chain unless the user explicitly asks
- MedSea-like visual language: sticky 48px header, dark `#0a0e1a`/`#111827` surfaces, thin borders, compact chips, dense cards, minimal glow

Preserve high-value features:
- host snapshot KPIs
- Docker auto-discovery and restart controls
- manual app add/edit/delete
- public/local/explicit open-target logic
- favorites
- search
- filters for host/docker/manual/public/down
- grid/table toggle
- drag/drop reorder persisted into server config
- import/export and backup/restore hooks
- settings refresh interval

## API schema pitfall

Do not assume the old frontend data shape is still correct. SeaDash's backend may expose flat stats fields, for example:
- `cpu_pct`, `mem_pct`, `disk_pct`
- `mem_used_gb`, `mem_total_gb`
- `disk_used_gb`, `disk_total_gb`
- `net_rx_mbps`, `net_tx_mbps`
- `docker_running`, `docker_total`

Old UI code may expect nested fields like `stats.cpu_percent`, `stats.memory.percent`, or `stats.disk.percent`. After a rewrite, live-probe `/api/dashboard` and adapt the frontend to the actual payload before judging the cards as broken.

## Service worker/cache pitfall

If SeaDash has a service worker, bump the cache name and keep `/api/*` network-only / non-cached. Otherwise the browser can keep serving the old shell after a full rewrite.

Recommended pattern:
- new cache name such as `seadash-compact-v1`
- cache static shell only
- return early for `url.pathname.startsWith('/api/')`
- network-first for static assets

## Verification checklist

After writing the new shell, verify live in the browser, not just by reading code:
- `/api/dashboard` returns JSON and the frontend hydrates
- KPI values are real, not `—`
- card count matches expected app/container count
- Docker filter and `docker` search return Docker rows
- table toggle renders rows and headers
- Add/Edit modal opens and contains expected fields
- browser console has zero JS errors
- DOM geometry has no large overlap/clipping: header height, hero height, app card dimensions, side rail position, body scroll height
- if browser vision fails, use DOM probes and screenshot path rather than pretending visual inspection succeeded

## Git/export note

For a non-git SeaDash directory, do not invent a repository/remote silently. Report the blocker plainly and ask for permission to initialize/create/select the GitHub repo if the user asked for `git push clean`.
