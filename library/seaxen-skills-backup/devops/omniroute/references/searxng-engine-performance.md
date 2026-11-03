# SearXNG Engine Performance & Optimization

## Engine Stats — Post-Optimization (2026-07-01)

From `http://192.168.0.222:8080/stats` after adding bing, qwant, mojeek, yandex, github, arxiv, google scholar, pubmed, npm, pypi:

| Engine | Score | Results | Response (s) | Reliability |
|---|---|---|---|---|
| google | 5.0 | 10 | 0.6 | **100%** |
| bing | 3.7 | 10 | 0.4 | **100%** |
| brave | 2.2 | 23 | 0.8 | **100%** |
| qwant | 5.2 | 10 | 1.2 | **100%** |
| mojeek | 1.9 | 10 | 1.0 | **100%** |
| yandex | 5.4 | 10 | 1.0 | **100%** |
| wikipedia | — | — | 0.3 | **100%** |
| wikidata | — | — | 2.2 | **100%** |
| duckduckgo | — | — | — | **0%** CAPTCHA |
| startpage | — | — | — | **0%** parsing error |
| yahoo | 0 | — | — | **0%** HTTP error |

**46 results per query** (was ~10 with defaults). 8 engines at 100% reliability.

## Engine Stats — Before Optimization (defaults only)

| Engine | Score | Results | Response (s) | Reliability |
|---|---|---|---|---|
| google | 3.0 | 10 | 0.5 | **100%** |
| wikipedia | 6.9 | 1 | 0.2 | **100%** |
| brave | 1.4 | 21 | 0.6 | 85% |
| startpage | 3.3 | 10 | 1.3 | 70% |
| wikidata | — | — | 0.9 | 70% |
| duckduckgo | 3.3 | 10 | 0.8 | **55%** |

## Reliable engines (100% from this server)

- **google** — fastest reliable, best overall
- **bing** — fastest response (0.4s), different index from Google
- **brave** — most results per query (23), independent index
- **qwant** — EU-based, privacy-focused
- **mojeek** — independent UK crawler, own index (not Google/Bing derivative)
- **yandex** — strong for non-English, good image search
- **wikipedia/wikidata** — reference/knowledge, supplementary

## Unreliable engines from server IPs

- **duckduckgo** — CAPTCHA blocked from datacenter IPs. Works fine from residential.
- **startpage** — HTML parsing errors (startpage changes layout frequently). 70% at best.
- **yahoo** — HTTP protocol errors. Inconsistent.

These are included in config but often fail. The 8 reliable engines provide sufficient coverage.

## Optimization applied

See `references/searxng-deployment.md` for the full optimized `settings.yml`.

Key changes from defaults:
- Added: bing, qwant, mojeek, yandex, github, arxiv, google_scholar, pubmed, npm, pypi
- Autocomplete: google (was disabled)
- image_proxy: true (was false)
- HTTP/2: enabled
- Pool connections: 100 (was default)
- Request timeout: 6s

## Important: Preferences UI vs settings.yml

The SearXNG Preferences page (`/preferences`) saves settings **per-browser cookie only**. It does NOT persist to `settings.yml`. For permanent changes:

1. Edit `/mnt/tb/1Apps/searxng/config/settings.yml` directly
2. Restart: `cd /mnt/tb/1Apps/searxng && docker compose restart`

## JSON API format

SearXNG returns JSON at:
```
http://host:port/search?q=QUERY&format=json
```

Required `settings.yml` entry for API use:
```yaml
search:
  formats:
    - html
    - json
```

## Stats dashboard

`http://192.168.0.222:8080/stats` — shows per-engine scores, result counts, response times, and reliability percentage. Check after any engine changes to verify new engines are working.
