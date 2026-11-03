# Hermes Web Tools Integration for Dashboards

## Architecture: Search vs Extract

Hermes has two independent web tool capabilities:

| Capability | Providers | OmniRoute? | Debug Logs? |
|---|---|---|---|
| `web_search` | SearXNG, Brave, DDGS, Tavily, Exa, Firecrawl, Parallel, xAI | Yes (via `omniroute-search` plugin) | Only if NOT using plugin |
| `web_extract` | Tavily, Exa, Firecrawl, Parallel | No (OmniRoute doesn't support extract) | Yes (direct Hermes) |

**Key insight:** SearXNG is **search-only**. Extract requires a separate provider with API key (Tavily, Exa, Firecrawl, Parallel).

## Search rotation vs Extract single-backend

- **Search** can rotate across providers via OmniRoute's `/v1/search` with automatic failover.
- **Extract** uses ONE backend only — no failover, no rotation. Set via `web.extract_backend` in config.yaml.
- If the extract backend is unset, Hermes auto-detects from env vars: Tavily → Exa → Parallel → Firecrawl.

## WEB_TOOLS_DEBUG initialization timing

The debug session is initialized at **module load time**:
```python
_debug = DebugSession("web_tools", env_var="WEB_TOOLS_DEBUG")
```

This means:
- Setting `WEB_TOOLS_DEBUG=true` in `.env` requires a **Hermes process restart** to take effect.
- The running process keeps the value it had when Python imported the module.
- Changing the env var without restarting has NO effect.

## OmniRoute search plugin bypasses debug logging

When `web.search_backend: omniroute-search` is set, search calls go through the plugin (`~/.hermes/plugins/omniroute_search/provider.py`), which calls OmniRoute's `/v1/search` directly. This **bypasses** Hermes' built-in `web_search_tool()` function entirely, so `_debug.log_call()` is never invoked.

**Result:** No debug logs for search when using OmniRoute plugin.

**Workaround:** Extract calls still go through Hermes' built-in path (since OmniRoute doesn't support extract), so those WILL be logged.

## Debug log format

Files: `web_tools_debug_<session_id>.json` in the logs directory.

### Search entry
```json
{
  "tool": "web_search_tool",
  "parameters": {"query": "...", "limit": 5},
  "error": null,
  "results_count": 5,
  "original_response_size": 1234,
  "final_response_size": 1200
}
```

### Extract entry
```json
{
  "tool": "web_extract_tool",
  "parameters": {"urls": ["https://example.com"], "format": "markdown", "char_limit": 15000},
  "error": null,
  "pages_extracted": 1,
  "pages_truncated": 0,
  "original_response_size": 5000,
  "final_response_size": 5000,
  "truncation_metrics": [{"url": "...", "original_chars": 5000, "truncated_chars": 5000, "truncated": false}],
  "processing_applied": ["truncate_and_store", "base64_image_conversion"],
  "ssrf_blocked": [{"url": "http://192.168.1.1", "reason": "private IP"}]
}
```

## Config detection from Docker container

To detect Hermes config from inside a Docker container:
1. Mount config: `- /root/.hermes/config.yaml:/data/hermes-config.yaml:ro`
2. Set env: `HERMES_CONFIG_PATH=/data/hermes-config.yaml`
3. In code: `config_path = os.getenv("HERMES_CONFIG_PATH", "~/.hermes/config.yaml")`
4. Parse YAML and check `web.extract_backend`, `web.search_backend`, etc.

## API key env vars for extract

| Provider | Env Var | Free Tier |
|---|---|---|
| Tavily | `TAVILY_API_KEY` | 1000/mo (5 URLs per credit for extract) |
| Exa | `EXA_API_KEY` | 1000/mo |
| Firecrawl | `FIRECRAWL_API_KEY` | 500/mo |
| Parallel | `PARALLEL_API_KEY` | Paid |

API keys should go in `.env` file (not inline in docker-compose.yml) and be passed via `env_file:` directive.
