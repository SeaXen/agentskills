# AceRoute — Sessions page v2 (parity with Models)

Repo: `/mnt/tb/1Apps/AceRoute` · `:8866` · Hermes `state.db` only.

## When to extend (user signals)

- "Audit sessions tab / as much as possible features / beautiful design"
- Expect **same operator tier** as Models: podium, insights, multi-chart grid, sort/export, rich drawer, cross-tab links

## Backend (`aceroute_sessions.py`)

**Dashboard** — `collect_sessions_dashboard(days, fresh=False)`:

- `leaderboard` — top 3 sessions by `total_tokens`
- `insights` — heaviest/busiest/most-tools session titles, top source/model
- `by_source` / `by_model` — sessions + **tokens + messages + cost_usd** (not counts only)
- `top_by_tokens`, `window_note`, `fresh=1` bypasses 40s TTL

**List** — `collect_sessions_list(..., sort=)`:

| `sort` | ORDER BY |
|--------|----------|
| `recent` | `started_at DESC` (default) |
| `tokens` | total token sum DESC |
| `cost` | actual+estimated cost DESC |
| `tools` | `tool_call_count DESC` |
| `msgs` | `message_count DESC` |

**Export** — `sessions_export_csv` → `GET /api/sessions/export?days=&source=&model=&q=` (up to 500 rows, sort=tokens)

**Detail** — `collect_session_detail` adds `token_pie` (in/out/cache/reasoning) for drawer Chart.js

**Messages cross-tab** — `collect_messages_list(..., session_id=)`:

- When `session_id` set: **no** `timestamp >= since` filter — full session timeline in Messages tab

## Frontend (`dashboard.js` Sessions block)

**State:** `sessionsState` — `source`, `model`, `q`, `sort`, `drawerPie`, `drawerRole`

**Toolbar:** window · sort select · live search · ✕ clear · ↻ refresh (`fresh=1`) · ⬇ CSV · source chips · **model chips**

**UI layers (match Models):**

1. 8 stat cards (`model-stat-glow`) incl. cache+reasoning, msg token Σ
2. `#sessionsLeaderboard` — reuse `.model-podium-card` (🥇🥈🥉)
3. `#sessionsInsights` — `.model-insight-chip` row
4. `.sessions-charts-grid` (5): volume/day · tokens+cost dual-axis · cost trend · source doughnut · model bar
5. Table: duration, sticky head, `.sess-model-cell` → `openModelFromSession`, **Msg** → `openMessagesForSession`

**Drawer:**

- `#sessionsDrawerActions` — Messages, Model, copy session ID
- KPI grid + token pie + role bar chart (`sessionsDrawerPie`, `sessionsDrawerRole`)
- Reuses `kpiCell()` from Models block (defined later in file — OK at runtime)

**Cross-tab:**

```javascript
openMessagesForSession(id)  // messagesState.session_id, switchPage('messages')
openModelFromSession(model) // openSessionsForModel + switchPage('models') + openModelDrawer
```

## Large JS edits — splice pattern

When replacing a whole page block in monolithic `dashboard.js`:

1. Write fragment to `static/js/<page>_v2.js` with markers `// ── Section ──`
2. Python splice: `start = dash.index('// ── Sessions')` … `end = dash.index('// ── Requests')`
3. `node --check static/js/dashboard.js`
4. Bump `index.html` `dashboard.js?v=N`

Do **not** hand-patch 200+ lines in one `patch` call unless necessary.

## Verification

```bash
cd /mnt/tb/1Apps/AceRoute
python3 -m py_compile aceroute_sessions.py app.py
curl -s 'http://127.0.0.1:8866/api/sessions/dashboard?days=7&fresh=1' | python3 -c "import sys,json; d=json.load(sys.stdin); print('lb',len(d.get('leaderboard',[])), 'insights',bool(d.get('insights')))"
curl -s 'http://127.0.0.1:8866/?v=30' | grep -E sessionsLeaderboard|sessions-charts-grid
```

Backend ship: `docker compose up -d --build --force-recreate`. Static: `./static:/app/static:ro`.

## Git

- `dc526ba` — Sessions page v2

## Related

- `references/aceroute-sessions-tab-state-db.md` — v1 APIs + Dockerfile/static pitfalls
- `references/aceroute-models-page-v2.md` — UI patterns to mirror
- `references/aceroute-requests-messages-models-tabs.md` — analytics grains