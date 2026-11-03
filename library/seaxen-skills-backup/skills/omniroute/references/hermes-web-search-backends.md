# Hermes Web Search Backend Configuration

## Backend Architecture

Hermes has two separate tool capabilities:
- `web_search` — search for URLs/titles/descriptions
- `web_extract` — fetch full page content from URLs

Each can use a different backend. Configuration priority:
1. `web.search_backend` / `web.extract_backend` (per-capability override)
2. `web.backend` (shared fallback)
3. Auto-detect from env vars (cascade order below)

## Auto-Detect Cascade (hardcoded)

When no explicit backend is set, `_get_backend()` picks the first with a key present:

```
tavily → exa → parallel → firecrawl → searxng → brave-free → ddgs
```

**This order is hardcoded in `tools/web_tools.py` lines 157-171. Not user-configurable.**

xAI is NOT in the auto-detect cascade. Must be set explicitly (`web.search_backend = xai`).

## Registered Backends

| Backend | Env Key | Search | Extract | Notes |
|---|---|---|---|---|
| tavily | `TAVILY_API_KEY` | ✅ | ✅ | Paid, best quality |
| exa | `EXA_API_KEY` | ✅ | ✅ | Paid, AI-native |
| parallel | `PARALLEL_API_KEY` | ✅ | ✅ | Paid |
| firecrawl | `FIRECRAWL_API_KEY` | ✅ | ✅ | Paid, or tool gateway |
| searxng | `SEARXNG_URL` | ✅ | ❌ | Free, self-hosted, search-only |
| brave-free | `BRAVE_SEARCH_API_KEY` | ✅ | ❌ | Free tier, search-only |
| ddgs | (package) | ✅ | ❌ | Free, no key needed |
| xai | (OAuth/key) | ✅ | ❌ | Via xAI Grok OAuth or XAI_API_KEY |
| **omniroute-search** | (auto from DB) | ✅ | ❌ | **Custom user plugin** — routes through OmniRoute `/v1/search` with failover across 5+ providers. Survives updates at `~/.hermes/plugins/omniroute_search/` |
| **serper** | `SERPER_API_KEY` | ❌ | ❌ | **NOT A HERMES BACKEND — zero code** (PR #53149 pending to add it) |

## Key Resolution

`_env_value()` checks:
1. `os.environ[key]` (includes Bitwarden-injected values at runtime)
2. `get_env_value(key)` from `~/.hermes/.env`

**Bitwarden BSM** applies secrets to `os.environ` at Hermes startup. Keys stored ONLY in Bitwarden (not in .env) work at runtime but won't show in standalone subprocess checks.

## Config Commands

```bash
# Clear all (use auto-detect)
hermes config set web.backend ''
hermes config set web.search_backend ''
hermes config set web.extract_backend ''

# Set explicit backend
hermes config set web.backend exa
hermes config set web.search_backend searxng
hermes config set web.extract_backend exa

# Set SearXNG URL (also needs in .env for plugin resolution)
hermes config set SEARXNG_URL http://127.0.0.1:8080
```

## Recommended Split for Self-Hosted SearXNG + OmniRoute

**Option A — Direct SearXNG (simpler):**
```
web.search_backend = searxng   → free, unlimited, 8 engines
web.extract_backend = ''       → auto: tavily (from Bitwarden)
```

**Option B — OmniRoute search (failover):**
```
web.search_backend = omniroute-search  → auto-failover: searxng → serper → brave → exa → tavily
web.extract_backend = ''               → auto: tavily (from Bitwarden)
```

Option B is better for reliability — if SearXNG goes down, OmniRoute falls through to other providers automatically. Option A has one less hop.

## No Runtime Fallback

Hermes does NOT retry with a different backend on failure. If the selected backend fails, the tool returns an error. The cascade is for **initial selection only**, not failover.

## xAI Web Search (Grok)

xAI uses Hermes-managed OAuth (via `hermes auth`) stored in `~/.hermes/auth.json` under `providers.xai-oauth.tokens.access_token`. Alternatively accepts `XAI_API_KEY`. Search-only (no extract). Must be set explicitly:

```bash
hermes config set web.search_backend xai
```

Config knobs under `web.xai` in config.yaml:
```yaml
web:
  xai:
    model: "grok-build-0.1"
    allowed_domains: ["x.ai"]     # max 5
    excluded_domains: ["bad.com"] # max 5
    timeout: 90
```

## Common Pitfalls

### SEARXNG_URL must be in .env, not just config.yaml
The SearXNG plugin resolves via `get_env_value()` which checks `~/.hermes/.env` then `os.environ`. Setting `SEARXNG_URL` via `hermes config set` writes to config.yaml but the SearXNG provider code reads from `.env`/env. If `web_search` returns `SEARXNG_URL is not set`, check that the value exists in `~/.hermes/.env`.

Fix:
```bash
# hermes config set writes to config.yaml AND .env for known keys
hermes config set SEARXNG_URL http://127.0.0.1:8080
# Verify it landed in .env:
grep SEARXNG_URL ~/.hermes/.env
```

### BRAVE_API_KEY ≠ BRAVE_SEARCH_API_KEY
Hermes expects `BRAVE_SEARCH_API_KEY`. A Bitwarden secret named `BRAVE_API_KEY` won't be recognized by the brave-free backend. Rename in Bitwarden if needed.

### serper is not a Hermes backend
`SERPER_API_KEY` exists in many Bitwarden vaults but Hermes has zero code for it — not as a plugin, not as a config key, not anywhere in the codebase. It's used by LangChain and other frameworks, not Hermes.

### SearXNG is search-only
`web_extract` with searxng backend returns: `SearXNG is a search-only backend and cannot extract URL content.` Pair with exa/tavily/firecrawl for extract.

### Bitwarden keys invisible in subprocess diagnostics
When debugging web backends from a standalone `python3` subprocess (not inside the running Hermes process), Bitwarden-injected keys like `TAVILY_API_KEY`, `EXA_API_KEY` won't be visible because Bitwarden only applies them at Hermes startup via `load_hermes_dotenv()`. The `.env` file may show `EXA_API_KEY=` (empty) even though the key exists in Bitwarden.

**Do not trust standalone subprocess `os.environ` checks for Bitwarden-backed keys.** Instead, call `web_search` or `web_extract` directly from within the Hermes session to verify.

## Pending PRs (as of 2026-07-01)

| PR | Title | Relevance |
|---|---|---|
| #53149 | feat(web): add 9 search providers — serper, baidu, bocha, serpapi, jina, google-cse, sogou, 360-search | Would add native serper to Hermes |
| #53158 | feat(web): multi-source fallback chain and search_engine parameter | Would add built-in fallback between backends |
| #55694 | feat(web): federated search plugin — aggregate multiple backends with LLM ranking | Would search across multiple backends simultaneously |

If #53149 lands, the `omniroute-search` custom plugin may become unnecessary for serper access. If #53158 lands, the failover benefit of the OmniRoute plugin could be replicated natively.

### hermes config set web.backend '' may not fully clear
If `web.backend` was previously set to a non-empty value and you set it to `''`, the empty string may still persist in config.yaml as `backend: ''`. The code checks `configured = (cfg.get("backend") or "").lower().strip()` — empty string passes through to auto-detect. This is correct behavior, but if Bitwarden also injects keys, the auto-detect cascade order determines the result.
If `web.backend` was previously set to a non-empty value and you set it to `''`, the empty string may still persist in config.yaml as `backend: ''`. The code checks `configured = (cfg.get("backend") or "").lower().strip()` — empty string passes through to auto-detect. This is correct behavior, but if Bitwarden also injects keys, the auto-detect cascade order determines the result.
