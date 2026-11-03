# 9router web backend integration

## Verified architecture

9router 0.5.50 exposes native web routes:

- `GET /v1/models/web`
- `POST /v1/search`
- `POST /v1/web/fetch`

The local deployment is host-networked at `http://127.0.0.1:20111`. API keys are stored in `/mnt/tb/1Apps/9router/data/db/data.sqlite`, table `apiKeys`, with active rows selected by `isActive=1`.

The tested catalog included:

- `serper/search`
- `tavily/search`
- `tavily/fetch`
- `jina-reader/fetch`
- `exa/search`
- `exa/fetch`

Direct provider requests returned HTTP 200 for Exa search/fetch, Tavily search/fetch, and Jina fetch.

## SearXNG port correction

9router's upstream default is `SEARXNG_URL=http://localhost:8888/search`. Before claiming SearXNG is unavailable, probe the actual host endpoint. This deployment's SearXNG is at `http://127.0.0.1:8080/search`; port 8888 is not listening.

Add the corrected value to the 9router compose environment and recreate the container while preserving `/mnt/tb/1Apps/9router/data`:

```yaml
SEARXNG_URL: http://127.0.0.1:8080/search
```

After recreation, test both health and the explicit provider:

```bash
curl http://127.0.0.1:20111/api/health
curl -X POST http://127.0.0.1:20111/v1/search \
  -H "Authorization: Bearer $NINEROUTER_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"searxng","query":"test","max_results":1}'
```

In 0.5.50, SearXNG may work when explicitly requested even if it is absent from `/v1/models/web`; treat the direct HTTP 200 as authoritative for runtime availability.

## Hermes integration pattern

Do not silently reuse an OmniRoute search backend when the requested default is 9router. Create a distinct Hermes backend name (for example `ninerouter-web`) implementing `agent.web_search_provider.WebSearchProvider` with both `supports_search()` and `supports_extract()` true.

Recommended defaults for this host:

```yaml
web:
  search_backend: ninerouter-web
  extract_backend: ninerouter-web
```

Use fallback lists in the backend rather than assuming a combo exists:

```text
search: searxng → tavily → exa → serper
fetch: exa → tavily → jina-reader
```

Resolve the 9router key from `NINEROUTER_KEY` first, then the local `apiKeys` table; never print the key. Normalize 9router search results to Hermes' `{success, data: {web: [...]}}` shape and fetch results to `{success, data: [...]}` with `url`, `title`, `content`, `raw_content`, and `metadata`.

## Verification and reload

- Compile the plugin with the Hermes venv Python; system Python may not have `agent.web_search_provider`.
- Test the provider directly against the live 9router endpoint before switching defaults.
- Enable the plugin, set scalar `web.*_backend` values with `hermes config set`, and verify persisted YAML.
- Gateway plugins are cached at startup. Restart the gateway after creating or modifying the provider; do not claim the new default is live before checking startup registration and a real tool call.

## Key mistake to avoid

9router and OmniRoute are separate gateways. OmniRoute's `/v1/search` and 9router's `/v1/search` are not interchangeable operationally: their model catalogs, SearXNG configuration, API-key databases, and fallback behavior differ. Inspect the actual local image and endpoint before deciding which gateway Hermes is using.
