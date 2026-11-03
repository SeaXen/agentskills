# AceRoute — Requests page v2 (LLM turns)

Repo: `/mnt/tb/1Apps/AceRoute` · `:8866` · grain = `messages` where `role = 'assistant'`.

## When to extend (user signals)

- "Audit **request** page/tab / as much as possible / beautiful design"
- User may typo "session" — if the nav tab is **Requests**, ship Requests parity with Sessions/Models, not another Sessions pass.

## Backend (`aceroute_sessions.py`)

**Dashboard** — `collect_requests_dashboard(days, fresh=False)`:

- `totals.with_tool_calls`, `totals.avg_tokens`
- `by_source` (requests + tokens)
- `by_model` adds `tool_turns`, `provider` via `model_provider_family()`
- `timeline[].tool_turns` per day
- `leaderboard` — top 3 assistant rows by `token_count`
- `insights` — `top_model`, `top_finish`, `avg_tokens`, `tool_turn_pct`, `top_source`
- `fresh=1` bypasses `_REQ_CACHE` (40s TTL)

**List** — `collect_requests_list(...)`:

| Param | Behavior |
|-------|----------|
| `source` | Filter `s.source` |
| `finish` | Filter `COALESCE(m.finish_reason,'unknown')` |
| `tools_only=true` | `tool_calls` JSON non-empty |
| `sort` | `recent` (default), `tokens`, `tools` |
| `model`, `q` | unchanged |

Rows include `provider` from `model_provider_family`.

**Export** — `requests_export_csv` → `GET /api/requests/export?days=&model=&source=&finish=&tools_only=&q=` (500 rows)

**Detail** — reuse `collect_message_detail` / `openMessageDrawer`; ensure `tool_calls_count` + `timestamp_iso` on message dict.

## Frontend (`static/js/dashboard.js`)

**State:** `requestsState` — `model`, `source`, `finish`, `toolsOnly`, `q`, `sort`, `charts` (main/tok/finish/model/source)

**Toolbar:** window · sort · search · 🔧 tools-only · ✕ · ↻ (`fresh=1`) · ⬇ CSV

**Chip rows:** `#requestsModelChips`, `#requestsSourceChips`, `#requestsFinishChips` (from `by_finish`)

**UI layers (mirror Sessions/Models):**

1. 8 stat cards incl. tool turns, avg tok, tool %, top finish
2. `#requestsLeaderboard` — `.model-podium-card`, click → `openRequestDrawer(id)`
3. `#requestsInsights`
4. `.sessions-charts-grid` (5): volume+tool turns · tokens line · finish doughnut · models bar · sources bar
5. Table: provider pill, clickable model filter, **Sess** button, `.req-row` hover

**Drawer (shared message drawer):** KPI grid via `kpiCell`, Session/Model actions, assistant-turn badge for `role=assistant`.

## Monolithic JS — splice pitfalls (this session)

1. **Glued comment line** — `sessionsOverlayClick(){...}// ── Requests` with no newline breaks marker-based splice. Normalize newline before `// ── Requests`.
2. **Accidental section delete** — A broad `patch` replace can remove the entire Requests block. After any edit, run `grep -c 'function renderRequests' dashboard.js` and `node --check`.
3. **Insert pattern** — Write `static/js/requests_v2.js`, Python-insert after `sessionsOverlayClick` closing brace, before `// ── Messages`.
4. Bump `dashboard.js?v=N` in `index.html`.

## Python patch pitfalls

- `collect_model_detail` / multiple `conn.close()` — use long unique anchor (include `recent_sessions` query tail), not bare `conn.close()`.
- `model_provider_family` is defined **after** `collect_requests_dashboard` in file order; OK at **call time**, not import time.

## Verification

```bash
cd /mnt/tb/1Apps/AceRoute
python3 -m py_compile aceroute_sessions.py app.py
node --check static/js/dashboard.js
curl -s 'http://127.0.0.1:8866/api/requests/dashboard?days=7&fresh=1' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('insights'), len(d.get('leaderboard',[])))"
curl -s 'http://127.0.0.1:8866/?v=31' | grep -E requestsLeaderboard|requestsFinishChips
```

Deploy: `docker compose up -d --build --force-recreate` for API; static volume `./static:/app/static:ro`.

## Git

- `bdb3d25` — Requests page v2

## Related

- `references/aceroute-requests-messages-models-tabs.md` — grain model
- `references/aceroute-sessions-page-v2.md` — parallel operator tier
- `references/aceroute-models-page-v2.md` — podium/charts/drawer patterns