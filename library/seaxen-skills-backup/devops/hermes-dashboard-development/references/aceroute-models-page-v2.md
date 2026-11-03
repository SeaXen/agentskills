# AceRoute — Models page v2/v3 (operator surface)

Repo: `/mnt/tb/1Apps/AceRoute` · `:8866` · Hermes `state.db` only.

## User signals this pass addressed

- "As much as possible features" on **Models** tab with **beautiful** compact UI (Dr. Sagar: one-line bars, bright stats, no clutter).
- Prior: "nothing changed after refresh" → always verify **served** HTML/JS vs disk (`curl` + `dashboard.js?v=`).

## Backend (`aceroute_sessions.py`)

- `model_provider_family(model)` — rollup labels (OpenAI, Anthropic, MiniMax, OpenRouter, Codex/GPT-5, etc.).
- `collect_models_dashboard(days, fresh=False)` enriches each model row:
  - `provider`, `sessions_7d`, `stale` (no session in 7d), `cost_share_pct`, `cost_per_mtok`, `avg_cost_session`
  - `providers[]` aggregate list, `top_by_cost`, `leaderboard`, `insights`, `token_mix_top5`, `sparkline_7d`
  - `window_note`: sessions use `started_at`; requests/messages use `message.timestamp`
- `collect_model_detail`: `by_finish`, `by_role`, `token_pie`, `top_sessions_by_tokens`, timeline with cost
- `collect_models_compare(models, days)` → `GET /api/models/compare?models=a,b,c`
- `models_export_csv(days)` + `GET /api/models/export?days=&format=csv|json`
- `collect_sessions_list(..., model=)` + `GET /api/sessions?model=` for cross-tab drill-down

## Frontend (`dashboard.js` Models block)

**State:** `modelsState` — `q`, `provider`, `view`, `sortKey`, `sortDir`, `hideStale`, `compare[]`, pins in `localStorage`.

**Toolbar:** Models/Providers · window · filter · ◎ hide idle · ✕ · ↻ (`fresh=1`) · export · provider chips.

**Stats (8):** Models, Providers, Sessions, Requests, Cache+Reas, Total tok, API, Cost.

**Charts:** Activity+cost · top tokens bar · cost doughnut · **stacked token mix (top 5)**.

**Table:** compare checkboxes (max 3) · sparkline 7d · sortable headers · Req/Sess/Msg shortcuts.

**Compare panel:** bar chart + table when ≥1 model selected.

**Drawer:** dual charts (activity + token pie) · by role · heaviest sessions · cross-tab actions.

**Cross-tab:**

```javascript
openRequestsForModel(name)
openSessionsForModel(name)
openMessagesForModel(name)
```

## Design tokens (match other analytics tabs)

- Reuse `#page-models` `.sessions-bar-card` + `#modelsSummary.tools-stats-row` (8× `minmax(0,1fr)`).
- Share `.model-podium-card`, `.model-insight-chip` with **Sessions** v2.

## Verification

```bash
cd /mnt/tb/1Apps/AceRoute
python3 -c "from aceroute_sessions import collect_models_dashboard; d=collect_models_dashboard(7); print(d['totals'], d['models'][0].get('provider'))"
curl -s 'http://127.0.0.1:8866/api/models/dashboard?days=7&fresh=1' | python3 -c "import sys,json; d=json.load(sys.stdin); print('leaderboard',len(d.get('leaderboard',[])))"
```

After backend changes: `docker compose up -d --build --force-recreate`. Static: `./static:/app/static:ro` — bump `?v=` on every JS/HTML ship.

## Git

- `09cac92` — v2
- `2c79b16` — v3 (compare, podium, sparklines, mix chart)

## Related

- `references/aceroute-requests-messages-models-tabs.md` — grain model + tab APIs
- `references/aceroute-sessions-page-v2.md` — Sessions UI parity pattern
- `references/aceroute-sessions-tab-state-db.md` — `model=` on sessions list