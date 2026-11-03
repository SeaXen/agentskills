# AceRoute Hermes-only Search tab

## Goal

Search analytics survive removal of **OmniRoute call_logs**, **SearXNG**, and optional Hermes plugins. Persisted signals come from **Hermes core** only.

## Env (default in docker-compose)

```yaml
ACEROUTE_SEARCH_SOURCE=hermes
HERMES_STATE_DB=/root/.hermes/state.db
HERMES_LOGS_DIR=/root/logs
HERMES_CONFIG_PATH=/root/.hermes/config.yaml
# Optional: show SearXNG engines card (off in hermes-only mode)
# ACEROUTE_SHOW_SEARXNG=1
ACEROUTE_HERMES_LOG_CACHE_SECONDS=45
```

Legacy OmniRoute logs: `ACEROUTE_SEARCH_SOURCE=omniroute`.

## Module: `aceroute_search.py`

| Function | Source |
|----------|--------|
| `collect_hermes_search_logs(days)` | `state.db` assistant `tool_calls` + tool rows for `web_search` / `x_search`; merge `web_tools_debug_*.json` when present |
| `collect_hermes_extract_logs(days)` | `web_extract` / `browse_page` tool messages + debug |
| `collect_hermes_web_providers(logs)` | `config.yaml` `web.search_backend` / `web.extract_backend` + usage counts |
| `hermes_search_meta()` | Injected into `/api/overview` as `analytics_source: hermes` |

Pair assistant tool_calls with tool results via `tool_call_id`; parse JSON from `<untrusted_tool_result>` wrappers.

## App wiring

- `_get_logs()` → hermes collectors when `is_hermes_search_mode()`.
- `/api/health` providers → `collect_hermes_web_providers`, not OmniRoute SQLite.
- SearXNG engines → hidden unless `ACEROUTE_SHOW_SEARXNG=1`.
- `POST /api/search-test` → returns `mode: hermes` message (no OmniRoute proxy).

## Dockerfile pitfall

New Python modules must be in `COPY` line:

```dockerfile
COPY app.py collectors.py aceroute_tools.py aceroute_search.py ./
```

Missing file → `ModuleNotFoundError: aceroute_search` at uvicorn startup.

## UI

- `#searchHermesNote` under overview cards (backends + debug hint).
- `searchResultsMeta`: "Hermes search & extract • state.db + debug logs".
- Bump `dashboard.js?v=` after JS changes (immutable cache).

## Tab dependency map (user question)

| Tab | Durable without OmniRoute/SearXNG |
|-----|-----------------------------------|
| **Search** (hermes mode) | Yes — `state.db` + debug |
| **Tools** | Yes — `state.db` → `aceroute.db` |
| **Skills** | Yes — skills tree + `hermes journey` |
| **Journey** | Yes — `hermes journey --json` |

Configured backend name (e.g. `omniroute-search` in config) is a **label**, not a dependency on OmniRoute log files.

## Verification

```bash
python3 -m py_compile app.py aceroute_search.py
python3 -c "from aceroute_search import collect_hermes_search_logs; print(len(collect_hermes_search_logs(30)))"
curl -s 'http://127.0.0.1:8866/api/overview' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['analytics_source'], d['total_searches'])"
```

## Git

AceRoute `d12a6d7` — `feat: Hermes-only Search tab from state.db`.