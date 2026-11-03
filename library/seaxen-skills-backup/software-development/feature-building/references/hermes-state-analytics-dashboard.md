# Hermes `state.db` analytics dashboard (AceRoute-class)

Class pattern: FastAPI + static SPA + read-only SQLite on `~/.hermes/state.db`, optional mirror DB for heavy sync (e.g. `aceroute.db`).

## Tab grain (Hermes-only)

| Tab | SQL grain | Notes |
|-----|-----------|--------|
| **Sessions** | `sessions` + message drawer | `started_at` window |
| **Requests** | `messages.role = 'assistant'` | LLM turns; no separate requests table |
| **Messages** | all `messages` | filter `model` via join `sessions` |
| **Models** | aggregate by `sessions.model` | enrich with assistant/tool message counts |
| **Tools** | synced mirror + tool messages | live `state.db` OK for read-only URI |

**Window semantics:** sessions filter on `started_at`; requests/messages on `message.timestamp` — document in UI meta (`window_note`).

## Backend modules

- One Python module per domain (`aceroute_sessions.py`, `aceroute_tools.py`, `aceroute_search.py`).
- `sqlite3.connect(f"file:{path}?mode=ro", uri=True)` for live reads.
- Dashboard cache TTL ~120s; expose `?fresh=1` for operator refresh.
- `collect_models_compare(models[], days)` for side-by-side (max 3–4 names).

## Docker pitfalls (user saw “nothing changed after refresh”)

1. **Static baked into image** — browser refresh does not update files inside the container until rebuild.
2. **Fix:** mount `./static:/app/static:ro` in `docker-compose.yml` so HTML/JS/CSS edit on host apply immediately.
3. **Backend changes** still need `docker compose up -d --build --force-recreate`.
4. **Cache bust:** bump `dashboard.js?v=N` in `index.html`; soften `Cache-Control` on `.js`/`.css` during active dev (e.g. `max-age=300` not `immutable` 24h).
5. **Verify served bits:** `curl -s http://HOST:PORT/ | grep dashboard.js` and `docker exec … grep sessions-bar-card /app/static/index.html`.

## UI layout (Dr. Sagar compact)

- **Toolbar card:** one row — title · truncated meta · actions · provider/source chips on **same row** with horizontal scroll (not wrapped block).
- **Stats:** 8 `mini-stat` cards on **one** `grid-template-columns: repeat(8, 1fr)` row; mobile horizontal scroll like Skills/Journey.
- **Models v3 extras:** podium top-3, insight chips, compare checkboxes (max 3), 7d sparkline column, sticky table head, drawer dual charts (activity + token pie).

## Large `dashboard.js`

- Append feature blocks via scripted splice (`// ── Models ──` … `async function refreshAll`) or `patch()` on JS; run `node --check` after edits.
- Avoid duplicating `kpiCell` / breaking function boundaries when patching drawer code.

## APIs to wire together

- Cross-tab: `openRequestsForModel` → `requestsState.model`; `openSessionsForModel` → `sessionsState.model` + `/api/sessions?model=`; `openMessagesForModel` → `/api/messages?model=`.
- Export: `/api/models/export?days=30` CSV; JSON via `format=json`.

## SearXNG engines empty

If `/stats` has no runtime data, fall back to `/config` engine list and show LISTED badge + note in UI.

## Git / path

Example app: `/mnt/tb/1Apps/AceRoute`, `:8866`, repo SeaXen/AceRoute.