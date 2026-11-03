# AceRoute Hermes Tools analytics (state.db → aceroute.db)

## Source of truth

- **Use** Hermes core `~/.hermes/state.db` (sessions, messages, `tool_name`, token/cost fields).
- **Do not** depend on `hermes-telemetry` plugin `telemetry.db` for the Tools tab — optional enrichment only.

## AceRoute-owned cache

- Module: `aceroute_tools.py`
- Path: `ACEROUTE_DB_PATH` (Docker: `/app/data/aceroute.db`, volume `aceroute-data`)
- Sync: background ~120s + startup + `POST /api/tools/sync`
- Cache: `ToolsAnalyticsCache` (same family as Skills/Journey caches)

## API

- `GET /api/tools?days=30` — dashboard payload (groups, stacked daily, hourly, pairs, heavy sessions, window deltas)
- `GET /api/tools/session?session_id=...`
- `GET /api/tools/tool?tool_name=...&days=...` — tool drawer timeline + sessions
- `GET /api/tools/export?days=...&format=csv|json`
- `GET /api/tools/status`
- `GET /api/health` — includes `searxng_engines`, `searxng_source`, `searxng_note` (see `searxng` skill)

## UI tab (feature surface)

- Nav: `switchPage('tools')` — fourth tab on `:8866`
- **Layout:** two-row header per `dashboard-ui-polish` → `references/two-row-toolbar-and-stats-strip.md` (never merge toolbar + stats into one hero card)
- **Bar:** window, ↻ sync, ⬇ CSV, `{ }` JSON export, filter chips
- **Stats row:** tool calls (+ % vs prior window), API calls, sessions, tokens (+ %), distinct tools, top tool
- **Filters:** category pills (all / core / browser / mcp / other)
- **Charts:** stacked top tools/day, UTC hour activity, tokens/day, model mix
- **Tables:** tools rank → tool drawer, common sequences, heavy sessions, platforms
- **Sessions:** search + sort; session drawer prev/next; tool drawer with calls/day chart

## Search tab (same repo)

- Page title `AceRoute — Search`; per-tab titles in `switchPage`.
- **📥 Web Extract:** one-line `#extractInlineMeta`; table behind **Log** toggle when empty.
- Hermes debug cards: `analytics-card.is-empty-compact` + inline meta when no `WEB_TOOLS_DEBUG` rows.
- Filter chips: `.results-chip` with `join('')` (not `badge()` + spaces).

## Skills / Journey tabs

- Summary stats **one horizontal row** — `references/stats-inline-row-one-line.md`.

## Static JS cache-bust (pitfall)

`app.py` serves `/static/js/*` with `Cache-Control: public, max-age=86400, immutable`. After JS edits: bump `dashboard.js?v=` in `index.html`, rebuild Docker, verify with `curl` that new symbols exist in the served bundle.

## Verify

```bash
cd /mnt/tb/1Apps/AceRoute
python3 -m py_compile app.py aceroute_tools.py collectors.py
node --check static/js/dashboard.js
docker compose up -d --build --force-recreate
curl -s 'http://127.0.0.1:8866/api/health' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('searxng_source'), len(d.get('searxng_engines',[])))"
```

Browser: `http://127.0.0.1:8866/?v=<cachebust>`.

## Pitfall

Merging toolbar + stats into one hero card after the user asked for **two lines** — split siblings, trim meta copy.

## Repo commits (reference)

`04d5818` Tools two-row · `5264311` Tools analytics · `37a8659` SearXNG fallback · `aa2b42a` one-row Skills/Journey stats · `e4427cd` Search polish.