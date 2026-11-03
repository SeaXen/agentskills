# 9router web search/fetch bridge

Verified against local 9router `0.5.50` on 2026-08-08.

## Live endpoint

```text
http://127.0.0.1:20111
```

`GET /v1/models/web` returned these active IDs:

```text
serper/search
tavily/search
tavily/fetch
jina-reader/fetch
exa/search
exa/fetch
```

Direct smoke tests returned HTTP 200 for:

- `POST /v1/search` with `model: exa`
- `POST /v1/search` with `model: tavily`
- `POST /v1/web/fetch` with `model: exa`
- `POST /v1/web/fetch` with `model: tavily`
- `POST /v1/web/fetch` with `model: jina-reader`

## Hermes bridge

The user plugin lives at:

```text
~/.hermes/plugins/omniroute_search/
```

Its search path remains:

```text
Hermes web_search → OmniRoute POST /v1/search
```

Its extraction path can use:

```text
Hermes web_extract → 9router POST /v1/web/fetch
```

The configured fallback order is:

```text
exa,tavily,jina-reader
```

The plugin auto-discovers the 9router key from:

```text
/mnt/tb/1Apps/9router/data/db/data.sqlite
```

For remote 9router, set `NINEROUTER_URL` and `NINEROUTER_KEY`. Override fallback order with `NINEROUTER_FETCH_MODELS`.

## Operational pitfall

The raw upstream 9router skill says IDs may end in `/search` and `/fetch`, but the POST request examples use the provider name (`exa`, `tavily`, `jina-reader`). Verify `/v1/models/web` on the running version and use the provider name accepted by that instance.

Hermes plugin/config changes require a gateway/session restart. Keep 9router extraction separate from `web_extract_plus`; the former is the default built-in web provider path, while the latter is the web-search-plus plugin tool.
