# AceRoute — Requests, Messages, Models tabs (Hermes `state.db`)

## Grain model (explain this to the user)

Hermes has **no** separate `requests` table. Map analytics grains explicitly:

| Tab | Grain | SQL / rule |
|-----|--------|------------|
| **Sessions** | One chat thread | `sessions` row + message timeline in drawer |
| **Requests** | One LLM API turn | `messages` where `role = 'assistant'` |
| **Messages** | Every message row | `messages` all roles (`user`, `assistant`, `tool`, `system`) |
| **Models** | Aggregated by `sessions.model` | Session token sums + joined assistant/tool message counts |

**Requests ≠ HTTP proxy logs.** Do not wire Requests to OmniRoute `call_logs` when user wants Hermes-only AceRoute.

**Wording trap:** User may say "audit **session** page" while meaning **Requests** (LLM turns). Confirm nav tab.

## Backend (`aceroute_sessions.py`)

Functions added alongside Sessions:

- `collect_requests_dashboard(days, fresh)` / `collect_requests_list` — assistant messages; v2: `by_source`, `leaderboard`, `insights`, filters `source`/`finish`/`tools_only`/`sort`, `requests_export_csv`
- `collect_messages_dashboard` / `collect_messages_list` / `collect_message_detail`
- `collect_models_dashboard` / `collect_model_detail` — per-model totals, `by_source`, `top_tools`, `recent_sessions`

**APIs**

- `GET /api/requests/dashboard?days=&fresh=1` · `GET /api/requests?days=&model=&source=&finish=&tools_only=&sort=&q=` · `GET /api/requests/export`
- `GET /api/messages/dashboard?days=` · `GET /api/messages?days=&role=&q=` · `GET /api/messages/detail?message_id=`
- `GET /api/models/dashboard?days=` · `GET /api/models/detail?model=&days=` · `GET /api/models/export?days=&format=csv|json`
- `GET /api/sessions?days=&model=` — filter sessions when jumping from Models tab

Use 40s TTL caches (`_MSG_CACHE`, `_REQ_CACHE`, `_MODEL_CACHE`) — message table is large (~150k+ rows).

## UI pattern (reuse Sessions chrome)

- Nav: **Requests**, **Messages**, **Models** (`data-page`, `PAGE_TITLES`, `switchPage` lazy render)
- Same **one-line bar** + **8-col stats** as Sessions (`#page-requests`, `#page-messages`, `#page-models` share `.sessions-bar-card` CSS)
- Requests v2: **`references/aceroute-requests-page-v2.md`** (podium, 5 charts, finish/source/tools chips, CSV). Sessions v2: `references/aceroute-sessions-page-v2.md`.
- Messages: role chips (`user` / `assistant` / `tool` / `system`)
- Models: see **`references/aceroute-models-page-v2.md`** (provider rollup, sort, pins, export, 3 charts, cross-tab Req/Sess, drawer timeline)
- Requests/Messages table rows → `#messageDrawerOverlay` (`openMessageDrawer`) with **Open session** button

## Model drawer fields (user expectation)

Show: requests, tool messages, session `tool_call_count`, `api_call_count`, in/out/cache/reasoning tokens, cost, by source, top tools, recent sessions.

## Verification

```bash
cd /mnt/tb/1Apps/AceRoute
python3 -c "from aceroute_sessions import collect_models_dashboard; print(collect_models_dashboard(30)['totals'])"
curl -s 'http://127.0.0.1:8866/api/models/dashboard?days=7' | head -c 200
curl -s 'http://127.0.0.1:8866/' | grep -E 'page-models|dashboard.js'
```

## Git

- `6e2ddd8` — Requests + Messages · `bdb3d25` — Requests v2
- `0beb3a9` — Models · `09cac92` Models v2 · `2c79b16` Models v3 · `dc526ba` Sessions v2

## Related

- `references/aceroute-requests-page-v2.md` — Requests operator UI (full)
- `references/aceroute-models-page-v2.md` — Models operator UI (full)

- `references/aceroute-sessions-tab-state-db.md` — Sessions tab
- `references/aceroute-dependency-and-tab-sources.md` — what survives plugin removal
- `dashboard-ui-polish` → `references/sessions-one-line-bar-and-stats.md` — bar/stats layout