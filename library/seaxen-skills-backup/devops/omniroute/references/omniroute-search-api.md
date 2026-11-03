# OmniRoute /v1/search API

## Endpoint

```
POST http://192.168.0.222:20128/v1/search
Authorization: Bearer <omniroute-api-key>
Content-Type: application/json
```

## Request format

```json
{
  "query": "search query",
  "provider": "serper-search",   // optional — omit for auto-select (cheapest)
  "max_results": 5,
  "search_type": "web",          // or "news"
  "country": "us",               // optional
  "language": "en",              // optional
  "timeRange": "week",           // optional
  "domainFilter": ["github.com"] // optional
}
```

## Response format

```json
{
  "id": "search-<uuid>",
  "provider": "searxng-search",
  "query": "...",
  "results": [
    {
      "title": "...",
      "url": "...",
      "display_url": "...",
      "snippet": "...",
      "position": 1,
      "score": null,
      "published_at": null,
      "citation": { "provider": "searxng-search", "retrieved_at": "...", "rank": 1 },
      "metadata": { "author": null, "language": null, "source_type": "...", "image_url": null }
    }
  ],
  "answer": { "source": "...", "text": "...", "model": null },
  "usage": { "queries_used": 1, "search_cost_usd": 0 },
  "metrics": { "response_time_ms": 1234, "upstream_latency_ms": 1000, "total_results_available": 10 }
}
```

## Providers (12 total)

| Provider ID | Cost/query | Free quota | Auth |
|---|---|---|---|
| serper-search | $0.001 | 2,500/mo | x-api-key |
| searchapi-search | $0.004 | 100/mo | api_key |
| brave-search | $0.005 | 1,000/mo | x-subscription-token |
| linkup-search | $0.005 | 1,000/mo | bearer |
| youcom-search | $0.005 | — | x-api-key |
| google-pse-search | $0.005 | 3,000/mo | key |
| perplexity-search | $0.005 | — | bearer |
| exa-search | $0.007 | 1,000/mo | x-api-key |
| tavily-search | $0.008 | 1,000/mo | bearer |
| **searxng-search** | **$0** | **999,999** | none |
| ollama-search | $0 | 1,000/mo | bearer |
| zai-search | $0 | — | bearer |
| duckduckgo-free | $0 | ∞ | none (fallback only) |

Auto-select picks the **cheapest provider with credentials**. searxng-search and duckduckgo-free are $0 (searxng preferred as it's not fallbackOnly).

## API key requirement

The OmniRoute API key must have `"search"` in its `allowed_models` array. Without it, the endpoint returns:

```json
{"message": "Model \"search\" is not allowed for this API key", "type": "permission_error"}
```

### Fix

```bash
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "update api_keys set allowed_models = json_insert(allowed_models, '\$[#]', 'search') where name='Hermes';"
# Restart to reload:
cd /mnt/tb/1Apps/omniroute && docker compose restart omniroute
```

Note: `json_insert` uses `$[#]` to append — bash `#` must be escaped or the command run via sqlite3 directly (not through bash interpolation).

## Credential fallbacks

Some search providers reuse credentials from a related chat provider:

| Search provider | Reuses credentials from |
|---|---|
| perplexity-search | perplexity (chat) |
| ollama-search | ollama-cloud |
| zai-search | zai |

## Failover

When a provider fails, OmniRoute tries the next cheapest. The `fallbackOnly` flag on duckduckgo-free means it's never auto-selected over a configured provider — only used when nothing else works.

## Hermes integration status

**As of 2026-07-01, Hermes has a custom `omniroute-search` plugin that calls this endpoint.**

The plugin is at `/usr/local/lib/hermes-agent/plugins/web/omniroute_search/` and is activated with:
```bash
hermes config set web.search_backend omniroute-search
```

Current routing:
```
Hermes web_search  →  OmniRoute /v1/search → cheapest provider (searxng/serper/brave/exa/tavily)
Hermes web_extract →  tavily (auto-detected from Bitwarden key)
Hermes model API   →  OmniRoute /v1/chat/completions (http://192.168.0.222:20128/v1)
```

## Testing

```bash
OR_KEY=$(sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite "select key from api_keys where name='Hermes';")

# Auto-select cheapest
curl -s -X POST http://127.0.0.1:20128/v1/search \
  -H "Authorization: Bearer $OR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","max_results":3}'

# Force specific provider
curl -s -X POST http://127.0.0.1:20128/v1/search \
  -H "Authorization: Bearer $OR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","max_results":3,"provider":"serper-search"}'
```
