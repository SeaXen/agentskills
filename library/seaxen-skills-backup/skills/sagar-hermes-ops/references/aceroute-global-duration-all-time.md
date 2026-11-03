# AceRoute — global duration & all-time (pointer)

Full recipe: **`dashboard-ui-operations`** → `references/aceroute-global-duration-and-all-time.md`.

Quick facts for Dr. Sagar's `:8866` deploy:

- **Default range:** Settings → **All time** (`globalDurationKey: 'all'`, `days=36500` in API calls).
- **Backend:** `ALL_TIME_DAYS=36500`, `since=0`, FastAPI `le=36500`; rebuild image after Python edits (`docker compose build aceroute && up -d`).
- **Half-empty UI:** curl `?days=36500` first — old `le=365` → **422** and blank KPIs.
- **Home/Costs/Channels/Ops/Sessions/Requests/Messages/Models/Tools** all share one header Settings duration (no per-page selects).