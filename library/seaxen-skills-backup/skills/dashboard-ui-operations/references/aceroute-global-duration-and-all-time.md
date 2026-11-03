# AceRoute global duration + true all-time mode

Repo: `/mnt/tb/1Apps/AceRoute`, live `:8866`, Hermes `state.db` analytics.

## UI pattern (operator dashboards)

- **One global duration** in header **Settings** (`⚙`), not per-page `<select>` rows.
- Presets map in `static/js/dashboard.js`: `DURATION_MAP` with `all: 36500`.
- Default preset: **`all`**; persist under `aceroute_global_duration_v2` (bump key when fixing bad migrations).
- `syncGlobalDaysToStates()` must update Home/Costs/Channels/Ops/Sessions/Requests/Messages/Models/Tools state before `refreshCurrentPage()`.
- Bump `dashboard.js?v=` in `index.html` after JS edits (`./static` is bind-mounted into the container).

## Backend contract

- FastAPI: dashboard routes need **`ge=1, le=36500`** and default **`Query(36500, ...)`** for all-time-by-default.
- **`days >= 36500`** (or shared `ALL_TIME_DAYS`) → `since = 0` (no timestamp filter), response includes `window_mode: "all"`, `window_days: 0`.
- Do **not** fake all-time with `3650` or clamp UI `all` to `365d` — oversized or rejected `days` produced **422** or **null totals** and a **half-rendered** UI (labels/charts empty, some text fields OK).

Shared helpers live in `aceroute_sessions.py`: `is_all_time`, `window_fields`, `_since_ts`, `_delta_prev_bounds`, `_sqlite_day_modifier`. Import in `aceroute_extra_pages.py` and `aceroute_tools.py` (do not duplicate `_since_ts` in tools).

### Period-over-period deltas when all-time

Compare **last 30d vs prior 30d** (`_delta_prev_bounds`), not `days * 2` (which breaks when `days` is all-time).

### Tools cache pitfall

`build_tools_dashboard` returns `window_days: 0` for all-time. `collect_tools_dashboard` must match cached payload using **`query_days`** (the request param), not `window_days` alone.

Background `ToolsAnalyticsCache.refresh()` should build with `ALL_TIME_DAYS` when UI default is all-time.

### Sessions all-time performance

`collect_sessions_dashboard` may cap row scan (`LIMIT 6000` recent sessions) for chart aggregation; Home/Costs totals still use SQL aggregates with `since=0`. Document in `window_note` if capped.

## Deploy pitfall (Docker)

`docker-compose.yml` mounts **`./static:/app/static:ro`** only. Python (`app.py`, `aceroute_*.py`) is **copied in the image** — backend changes require:

```bash
cd /mnt/tb/1Apps/AceRoute && docker compose build aceroute && docker compose up -d aceroute
```

Frontend-only edits apply after hard refresh; API validation changes do not until rebuild.

## Verification (required before “done”)

1. `python3 -m py_compile app.py aceroute_sessions.py aceroute_extra_pages.py aceroute_tools.py`
2. `node --check static/js/dashboard.js`
3. Live smoke (after rebuild):

```bash
for p in home costs channels ops sessions requests messages models; do
  curl -sS "http://127.0.0.1:8866/api/${p}/dashboard?days=36500" | python3 -c "import sys,json; d=json.load(sys.stdin); print(p, d.get('window_mode'), d.get('error'), (d.get('totals') or {}).get('sessions'))"
done
curl -sS "http://127.0.0.1:8866/api/tools?days=36500" | python3 -c "import sys,json; d=json.load(sys.stdin); print('tools', d.get('window_mode'), (d.get('summary') or {}).get('sessions'))"
```

4. Browser: `?v=<bump>` + hard refresh; confirm Settings shows **All time** and KPI/charts populate.

## Symptom → first check

| Symptom | Likely cause |
|--------|----------------|
| KPIs `0` / `—`, chart axes only | API **422** (`days>365`) or null totals from bad `days`; curl APIs before blaming Chart.js |
| Slow first load on all-time | Full-table scans; use SQL aggregates + cache TTL (`ACEROUTE_SESSIONS_CACHE_SECONDS`) |
| Tools wrong window after UI change | Stale cache comparing `window_days` instead of `query_days` |