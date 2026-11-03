# GroktoCrawl — Firecrawl-compatible stack eval (Hermes)

**Repo:** https://github.com/groktopus/groktocrawl (MIT, ~8 Docker services)

## What it is

Self-hosted **Firecrawl v2 API**: scrape, search, crawl, agent, answer, Qdrant semantic index, portal UI `:8082`, API `:8080`. Not a Hermes plugin.

## Hermes wiring (if deployed)

- Env: `FIRECRAWL_API_URL`, `FIRECRAWL_API_KEY`
- Config: `web.search_backend` / `extract_backend`: `firecrawl`
- Hermes issue #36113 — `categories` on `web_search` with GroktoCrawl `/v2/search`

## vs existing stack

| Need | Existing | GroktoCrawl |
|------|----------|-------------|
| Page fetch | web_extract, browser | Playwright, adapters |
| Search | Brave/Tavily, web_search | SearXNG + Qdrant |
| Light reads | agent-reach (eval) | Heavy 8-container stack |

## Defer on constrained host

RAM/heat, remap :8080 if busy, LLM in `.env`. Verdict: evaluated-not-installed unless recurring crawl/monitor need.

## Docs trail

Obsidian `Knowledge/GroktoCrawl.md`; Mnemosyne global insight for hot recall.