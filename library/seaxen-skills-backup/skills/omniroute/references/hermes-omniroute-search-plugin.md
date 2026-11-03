# Hermes OmniRoute Search Plugin

## Overview

Custom Hermes web search plugin that routes `web_search` through OmniRoute's `POST /v1/search` endpoint. Gives Hermes automatic failover across all configured OmniRoute search providers.

## Files (user plugin — survives updates)

```
~/.hermes/plugins/omniroute_search/
├── plugin.yaml     # manifest (name: web-omniroute-search, kind: backend)
├── __init__.py     # registers OmniRouteSearchProvider (relative import)
└── provider.py     # WebSearchProvider subclass
```

**This is a user plugin at `~/.hermes/plugins/`** — survives `pip install --upgrade hermes-agent`.

The older bundled copy at `/usr/local/lib/hermes-agent/plugins/web/omniroute_search/` was removed to avoid conflicts. User plugins override bundled ones on name collision.

## Backend name

`omniroute-search`

## Activation

```bash
hermes config set web.search_backend omniroute-search
```

## API key resolution

1. `OMNIRROUTE_API_KEY` env var (via `.env` or Bitwarden)
2. Auto-discover from `/mnt/tb/1Apps/omniroute/data/storage.sqlite` → first active API key

No configuration needed if OmniRoute is local — the plugin reads the key directly from the DB.

## URL resolution

1. `OMNIRROUTE_SEARCH_URL` env var
2. Default: `http://192.168.0.222:20128`

## How it works

```
Hermes web_search("query")
  → plugin calls POST http://192.168.0.222:20128/v1/search
  → OmniRoute auto-selects cheapest provider (searxng at $0)
  → Falls back to serper → brave → exa → tavily on failure
  → Plugin normalizes response to Hermes standard format
  → Returns {success, data: {web: [{title, url, description, position}]}}
```

## Response normalization

OmniRoute returns a richer format than Hermes expects. The plugin maps:
- `results[].title` → `title`
- `results[].url` → `url`
- `results[].snippet` → `description` (falls back to `content`)
- `results[].position` → `position`

## Setup schema

The plugin exposes a `get_setup_schema()` for `hermes tools` with:
- Name: "OmniRoute Search"
- Badge: "free · multi-provider failover"
- Env vars: `OMNIRROUTE_SEARCH_URL`, `OMNIRROUTE_API_KEY`

## Troubleshooting

### "OmniRoute API key not found"
- Check that OmniRoute is installed at `/mnt/tb/1Apps/omniroute/data/storage.sqlite`
- Or set `OMNIRROUTE_API_KEY` in `.env`
- Ensure at least one API key is active in OmniRoute

### "Model \"search\" is not allowed for this API key"
- The OmniRoute API key needs `"search"` in `allowed_models`
- Fix: see `omniroute-search-api.md` → "API key requirement" section

### "Could not reach OmniRoute"
- Check `docker compose ps` in `/mnt/tb/1Apps/omniroute`
- Verify port 20128 is listening
- If remote, set `OMNIRROUTE_SEARCH_URL`

### Plugin not found after Hermes update
This should not happen — the plugin is at `~/.hermes/plugins/omniroute_search/` which survives updates. If it does disappear, check that the directory exists and `plugin.yaml` is present.

## User plugin structure (already migrated)

The plugin lives at `~/.hermes/plugins/omniroute_search/` with three files:

### plugin.yaml
```yaml
name: web-omniroute-search
version: 1.0.0
description: "OmniRoute Search — routes web_search through OmniRoute's /v1/search with failover"
author: Sagar
kind: backend
provides_web_providers:
  - omniroute-search
```

### __init__.py
Uses **relative import** (not absolute):
```python
from .provider import OmniRouteSearchProvider

def register(ctx):
    ctx.register_web_search_provider(OmniRouteSearchProvider())
```

### provider.py
Same as the bundled version. Key details:
- `_omniroute_api_key()` auto-discovers from local SQLite DB
- `_omniroute_search_url()` defaults to `http://192.168.0.222:20128`
- Imports: `agent.web_search_provider.WebSearchProvider`, `hermes_cli.config.get_env_value`

## ⚠️ PITFALL: User plugin imports use relative paths
The `__init__.py` must use `from .provider import ...` (relative), not `from provider import ...` (absolute). Absolute imports fail when the plugin is loaded by the user plugin discovery system.
