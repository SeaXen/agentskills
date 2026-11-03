# AceRoute Sessions tab — Hermes `state.db` message analytics

## When to add (vs Tools tab)

| Surface | Source | User goal |
|---------|--------|-----------|
| **Tools** | `state.db` → synced `aceroute.db` | Tool frequency, categories, sequences, heavy sessions (tool-centric) |
| **Sessions** | Live read-only `state.db` | Conversation-centric: tokens, messages, per-session message timeline |

Add **Sessions** when the user asks for session/message/request breakdown, token use per session, or message-level drill-down — not only tool call stats.

## Backend (`aceroute_sessions.py`)

- `collect_sessions_dashboard(days)` — totals, by_source, by_model, daily timeline; 40s TTL cache
- `collect_sessions_list(days, source, q, limit, offset)` — session table rows
- `collect_session_detail(session_id, message_limit, message_offset)` — tool_breakdown, role_breakdown, messages with `content_preview` (500 chars), `token_count`

**API routes**

- `GET /api/sessions/dashboard?days=`
- `GET /api/sessions?days=&source=&q=&limit=&offset=`
- `GET /api/sessions/detail?session_id=&message_limit=`

## Dockerfile pitfall

Include `aceroute_sessions.py` in `COPY` line. Symptom: `ModuleNotFoundError: No module named 'aceroute_sessions'` on container start.

## Deploy pitfall — "refresh did nothing"

Container may serve **baked** `static/` from the image. Verify with `curl -s http://host:8866/ | grep dashboard.js` vs repo `index.html`. Fix: rebuild and/or mount `./static:/app/static:ro` (`b35482c`). Bump `dashboard.js?v=N`.

## Frontend pattern (AceRoute SPA)

- Nav: **Sessions** (`data-page="sessions"`, `PAGE_TITLES.sessions`)
- **One-line bar:** `.sessions-bar-row` (`nowrap`) — title, short meta, controls, source chips scroll inline. See `dashboard-ui-polish` → `references/sessions-one-line-bar-and-stats.md`.
- **One-line stats:** `#sessionsSummary` `repeat(8,1fr)` below the bar (separate block).
- Charts: sessions/day bar, input vs output tokens/day line
- Table row click → `#sessionsDrawerOverlay` (reuse journey drawer CSS)
- Drawer sections: Session meta, Tools breakdown, Messages scroll (`sessions-msg-scroll`, max-height ~420px)
- Lazy-load: `switchPage('sessions')` → `renderSessions()`; `closeSessionsDrawer()` when leaving tab
- Cache-bust: bump `dashboard.js?v=N` after JS merge

**v2 operator surface:** `references/aceroute-sessions-page-v2.md` (`dc526ba`).

## Verification

```bash
python3 -m py_compile aceroute_sessions.py app.py
python3 -c "from aceroute_sessions import collect_sessions_dashboard; print(collect_sessions_dashboard(30)['totals']['sessions'])"
curl -s 'http://127.0.0.1:8866/api/sessions/dashboard?days=30' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['totals']['sessions'], d['totals']['total_tokens'])"
curl -s 'http://127.0.0.1:8866/' | tail -3
```

Browser: Sessions tab, one-row stats, click row → messages populate.

## Git reference

- `6f85c9b` — Sessions tab
- `d4f75c5` / `b35482c` — one-line bar+stats, static mount
- `dc526ba` — Sessions v2