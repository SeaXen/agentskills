# AceRoute — what depends on Hermes vs optional apps

Repo: `/mnt/tb/1Apps/AceRoute`, `:8866`, host-network Docker.

## Durable without OmniRoute / SearXNG / plugins

| Tab | Data source | Notes |
|-----|-------------|--------|
| **Tools** | `HERMES_STATE_DB` → `aceroute.db` volume | Not `hermes-telemetry` / `telemetry.db` |
| **Skills** | `HERMES_SKILLS_DIR` + `hermes journey --json` usage merge | |
| **Journey** | `hermes journey --json` (+ CLI mutations when writable) | |
| **Sessions** | Live `state.db` (`aceroute_sessions.py`) | |
| **Requests** | `messages` where `role=assistant` | LLM turns |
| **Messages** | All active `messages` | |
| **Models** | `sessions.model` aggregates | `/api/models/*` |
| **Search** (Hermes mode) | `ACEROUTE_SEARCH_SOURCE=hermes` → `state.db` + `web_tools_debug_*.json` + `config.yaml` backends | Default in docker-compose |

## Optional / legacy

| Piece | Needs |
|-------|--------|
| Search (legacy) | `ACEROUTE_SEARCH_SOURCE=omniroute` + OmniRoute `call_logs/` + `storage.sqlite` |
| SearXNG Engines card | `SEARXNG_URL`; hidden when Hermes-only unless `ACEROUTE_SHOW_SEARXNG=1` |
| 🔍 Test Search (legacy) | OmniRoute `:20128` proxy |
| 📥 Test Extract | Tavily (or configured extract API key) |

## Env cheat sheet

```yaml
HERMES_STATE_DB=/root/.hermes/state.db
ACEROUTE_DB_PATH=/app/data/aceroute.db
ACEROUTE_SEARCH_SOURCE=hermes
ACEROUTE_SHOW_SEARXNG=1   # optional
WEB_TOOLS_DEBUG=true      # richer Search metrics + debug sections
```

## User intent

When the user says they want data to survive removing plugins/apps, implement and document **Hermes `state.db` + app-owned SQLite** paths; do not require OmniRoute log mounts for core analytics.