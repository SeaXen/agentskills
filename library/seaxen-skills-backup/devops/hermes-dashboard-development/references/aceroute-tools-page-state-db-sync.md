# AceRoute Tools page — `aceroute.db` synced from Hermes `state.db`

Use when adding or maintaining a **Tools** analytics tab on AceRoute (or a similar Hermes SPA dashboard) without depending on `hermes-telemetry` / `telemetry.db`.

## Source-of-truth rule

| Store | Role |
|-------|------|
| `~/.hermes/state.db` | Hermes **core** session + message store (`sessions`, `messages`) |
| `aceroute.db` | AceRoute-owned **aggregate cache** (fast reads, survives telemetry plugin removal) |
| `~/.hermes/telemetry/telemetry.db` | Optional plugin DB (`tool_calls` with `ok` + `latency_ms`) — **not required** |

User expectation: removing `hermes-telemetry` must **not** remove Tools analytics. Design against `state.db` first.

### Useful `state.db` fields

**`sessions`:** `tool_call_count`, `api_call_count`, token columns (`input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_write_tokens`, `reasoning_tokens`), `estimated_cost_usd` / `actual_cost_usd`, `model`, `source`, `title`, `started_at`.

**`messages`:** `role`, `tool_name`, `content`, `timestamp` — count tool usage via `tool_name` on tool-role rows.

Read Hermes DB **read-only**: `sqlite3.connect("file:...?mode=ro", uri=True)`.

## `aceroute.db` schema (minimal)

- `sync_meta` — `last_sync_at`, `last_session_started_at`, `hermes_state_db`
- `tool_sessions` — one row per session (upsert on sync)
- `tool_daily` / `tool_totals` — rebuilt each sync from message scan (do **not** incrementally add to daily totals or counts double)
- `token_daily` / `model_usage` — rebuilt from `tool_sessions` after sync

## Sync daemon pattern

- Module: `aceroute_tools.py` with `ToolsAnalyticsCache` (daemon thread, default **120s**)
- Startup: `ToolsAnalyticsCache.instance()` alongside other AceRoute caches
- Full tool message scan window: ~**400 days** of `messages.tool_name` (heavy but bounded); session rows incremental with 1-day overlap
- After session upserts: `DELETE FROM tool_daily` + `tool_totals`, reinsert from scan; then rebuild `token_daily` / `model_usage`

Env:

- `HERMES_STATE_DB=/root/.hermes/state.db`
- `ACEROUTE_DB_PATH=/app/data/aceroute.db`

Docker:

- Mount `~/.hermes:ro` for `state.db`
- Named volume `aceroute-data:/app/data` for writable `aceroute.db`
- `COPY aceroute_tools.py` in Dockerfile; do **not** commit live `aceroute.db` (gitignore / volume only)

## API surface

- `GET /api/tools?days=30` — dashboard payload + `sync` status
- `GET /api/tools/session?session_id=` — cached session row + live message window from `state.db`
- `POST /api/tools/sync` — force refresh
- `GET /api/tools/status`

## Frontend (AceRoute)

- Nav tab **Tools**; lazy-load on first open (`toolsState`, `renderTools()`)
- **Layout:** two rows — `dashboard-ui-polish` → `references/two-row-toolbar-and-stats-strip.md` (never merge bar + stats into one hero).
- Window select: 7 / 30 / 90 / 365 days; expanded UI/API: `references/aceroute-tools-tab-feature-bundle.md`
- Reuse **journey drawer** overlay for session + tool drill-down
- Bump `dashboard.js?v=N` after JS changes

## Verification

1. `python3 -m py_compile app.py aceroute_tools.py` + `node --check static/js/dashboard.js`
2. `curl /api/tools/status` → `hermes_state_exists: true`, `ready: true`
3. Browser: `active: tools`, `Chart.getChart(toolsActivityChart)`, rank row count > 0

Example live meta after deploy: `819 sessions • 51.8K tool calls • 6.15B tokens • 80 tools`.

## Pitfalls

| Issue | Fix |
|-------|-----|
| User asks for telemetry.db | Explain plugin DB is optional; use `state.db` + `aceroute.db` for durability |
| Incremental `tool_daily` ON CONFLICT DO UPDATE adds | Full rebuild of daily/totals tables each sync |
| Scanning only `since_ts` for tools | Use fixed lookback (e.g. 400d) for message-derived tool counts |
| Huge `state.db` first sync | Accept multi-second daemon refresh; serve stale cache until `ready` |

Commit reference: AceRoute `a431c6e` — `feat: add Tools page backed by aceroute.db from Hermes state.db`.