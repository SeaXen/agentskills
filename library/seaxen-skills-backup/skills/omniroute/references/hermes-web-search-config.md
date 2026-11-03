# Hermes Web Search Configuration Reference

## Auto-detect cascade (hardcoded in tools/web_tools.py)

When `web.backend` / `web.search_backend` / `web.extract_backend` are all empty:
```
tavily → exa → parallel → firecrawl → searxng → brave-free → ddgs
```

Picks the **first** backend whose key is present. No runtime fallback on failure.

## Resolution order for each capability

1. `web.search_backend` (per-capability override) — if set AND available, use it
2. `web.backend` (shared fallback) — if set AND available, use it
3. Auto-detect from env vars (cascade above)

## Registered web search backends

| Backend name | Key/Var | Search | Extract | Notes |
|---|---|---|---|---|
| tavily | TAVILY_API_KEY | ✅ | ✅ | Best extract quality |
| exa | EXA_API_KEY | ✅ | ✅ | Good for AI/tech |
| parallel | PARALLEL_API_KEY | ✅ | ✅ | |
| firecrawl | FIRECRAWL_API_KEY | ✅ | ✅ | Also supports gateway |
| searxng | SEARXNG_URL | ✅ | ❌ | Search-only, self-hosted |
| brave-free | BRAVE_SEARCH_API_KEY | ✅ | ❌ | NOT BRAVE_API_KEY |
| ddgs | (package installed) | ✅ | ❌ | Free, no key needed |
| xai | XAI_API_KEY or OAuth | ✅ | ❌ | Not in auto-detect cascade |

## ⚠️ Key naming pitfalls

- **BRAVE_API_KEY** ≠ **BRAVE_SEARCH_API_KEY** — Hermes expects `BRAVE_SEARCH_API_KEY`
- **SEARXNG_URL** must be base URL (`http://host:port`), NOT `http://host:port/search`
- **SEARXNG_BASE_URL** — not used by Hermes (only SearXNG's own Docker config)
- **SERPER_API_KEY** — Hermes has ZERO code for serper. It's not a registered backend.

## ⚠️ Config vs .env resolution

Different backends resolve keys differently:

| Backend | Resolved via |
|---|---|
| searxng | `get_env_value("SEARXNG_URL")` → checks os.environ then ~/.hermes/.env |
| tavily/exa/brave | Bitwarden → os.environ (at startup) |
| xai | `~/.hermes/auth.json` (OAuth) or `XAI_API_KEY` env |

Setting `hermes config set SEARXNG_URL ...` writes to config.yaml, NOT .env. The SearXNG plugin reads from .env. **Must set in BOTH places:**
```bash
hermes config set SEARXNG_URL http://127.0.0.1:8080
# AND edit ~/.hermes/.env to add SEARXNG_URL=http://127.0.0.1:8080
```

## ⚠️ Bitwarden keys and hermes config set

When you run `hermes config set KEY value` and Bitwarden is enabled, it applies all BWS secrets to os.environ. But keys that are EMPTY in .env (e.g., `EXA_API_KEY=`) remain empty — Bitwarden sets them in os.environ at startup, but `hermes config set EXA_API_KEY "$EXA_API_KEY"` copies the shell value (empty if not exported).

**Keys in Bitwarden but not in .env** will be available at runtime (Bitwarden sets os.environ at startup), but `hermes config set` won't capture them from the shell.

## Custom web search plugin pattern

To add a new search backend as a user plugin (persists across Hermes updates):

**Location:** `~/.hermes/plugins/<name>/`

**Files needed:**
```
~/.hermes/plugins/<name>/
├── plugin.yaml      ← manifest
├── __init__.py      ← register(ctx) function
└── provider.py      ← WebSearchProvider subclass
```

**plugin.yaml format:**
```yaml
name: web-<name>
version: 1.0.0
description: "..."
author: You
kind: backend
provides_web_providers:
  - <name>
```

**__init__.py:**
```python
from .provider import MyProvider
def register(ctx):
    ctx.register_web_search_provider(MyProvider())
```

**provider.py:** Subclass `agent.web_search_provider.WebSearchProvider`:
- `name` property — matches config value
- `is_available()` — cheap check, no network calls
- `supports_search()` / `supports_extract()`
- `search(query, limit)` → `{"success": True, "data": {"web": [...]}}`

**Config:** `hermes config set web.search_backend <name>`

See `templates/omniroute_search_provider.py` in the omniroute skill for a working example.
