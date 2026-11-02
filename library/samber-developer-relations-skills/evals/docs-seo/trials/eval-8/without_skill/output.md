# Untangling Carrowmore's AI-bot blocking — root cause + fix

## What's actually happening

Two independent blocks stacked on top of each other, and nobody owns the combined effect:

1. **robots.txt** — infra hand-built a ~20-entry `Disallow` list of every AI user-agent name they could find, with no distinction between *bots that train models* and *bots that fetch a page to answer one user's live question and cite it*.
2. **CDN "Block AI bots" toggle** — a separate, blunt, dashboard-level switch that almost certainly blocks the same broad category at the network edge (often hard 403/challenge, not the advisory-only behavior of robots.txt). This was flipped by someone else, sat unnoticed for two months, and is likely the *dominant* cause since it can block even requests that would ignore or bypass robots.txt.

Nobody treated "block AI" as one policy with one owner. Two teams each solved it their own way, and the union of both blocks is broader than either intended.

## The distinction legal needs to see

Not all AI user-agents do the same thing. Most major vendors already publish **separate bots for training vs. retrieval**, specifically so publishers can choose one without the other:

**Bucket A — training-only crawlers (block these, satisfies legal)**
`GPTBot` (OpenAI), `CCBot` (Common Crawl, feeds many third-party training sets), `Google-Extended` (Gemini/AI Overviews training+grounding opt-out), `Applebot-Extended` (Apple Intelligence training), `Bytespider` (ByteDance), `Meta-ExternalAgent` (Meta), `anthropic-ai` (Anthropic training, where distinct from ClaudeBot), plus other pure-scrape bots (Diffbot, Omgili, Timpibot, ImagesiftBot). Keeping these disallowed site-wide costs nothing.

**Bucket B — retrieval/citation bots (unblock these — this is the marketing fire)**
`OAI-SearchBot` (ChatGPT search index), `ChatGPT-User` (live fetch when ChatGPT browses a page on a user's behalf), `ClaudeBot` / `Claude-SearchBot` / `Claude-User` (Anthropic crawl + live fetch), `PerplexityBot` (index crawler — Perplexity states this doesn't feed training) and `Perplexity-User` (live fetch), `Bingbot` (feeds Copilot via the Bing index), `Googlebot` (feeds AI Overviews grounding via the standard Search index). If any of these were on the 20-line list, that is the exact mechanism behind "the assistant says it can't find our docs" — no index entry, no live fetch, nothing to cite.

**Bucket C — ambiguous / dual-purpose**
A few smaller or newer AI vendors haven't published a clean training/retrieval split yet. Don't silently default these either way — list them out and get an explicit legal call per name, since "we didn't notice this one" is exactly how this incident started.

Also check now, as step zero: did the 20-line list or the CDN toggle accidentally sweep in **Googlebot or Bingbot themselves**? That's a common copy-paste mistake when someone grabs "list of AI bots" from a blog post, and it would explain lost visibility in classic search too, not just AI answers.

## Fix, in order

1. **Audit before touching anything.** Pull the live `docs.carrowmore.com/robots.txt`, and in the CDN dashboard find exactly which bot list the "Block AI bots" toggle uses (most CDNs bundle a managed list you can inspect but not see by default). Screenshot both — you'll want the before-state on record for legal.
2. **Rewrite robots.txt**: keep `Disallow` for Bucket A only, remove Bucket B entirely (or explicit `Allow: /`), keep a valid `Sitemap:` line so retrieval bots and indexers can find doc pages efficiently rather than blind-crawling.
3. **Turn off the CDN's blanket toggle.** If the CDN offers granular sub-categories (several now split "AI Crawlers: training" from "AI: Assistants/Fetchers"), use those instead of an all-or-nothing switch. If it's genuinely all-or-nothing, replace it with a custom bot-management/WAF rule matching Bucket A user-agent strings only.
4. **One config, one owner.** Don't let infra edit robots.txt and a separate team edit the CDN toggle independently — that's exactly how a two-month-unnoticed duplicate block happened. Put both under one reviewed change with legal + marketing sign-off on the Bucket A/B/C split.

## What to tell legal, precisely

"Block AI training" is achievable **prospectively, on a best-effort basis**, only for vendors that (a) publish a distinct training-crawler UA and (b) actually honor robots.txt — most reputable ones do, some don't. It is **not retroactive**: any content already crawled before today's fix, or scraped by a non-compliant bot, may already sit in a trained model's weights, and there's no mechanism to undo that. Frame the deliverable to legal as risk mitigation going forward, not a guarantee — calibrate expectations now so this isn't relitigated at the next audit.

## Verification

- Re-fetch robots.txt after deploy, confirm Bucket B is allowed.
- Testing with `curl -A "<bot-UA>"` isn't proof the CDN allows it — many bot-management layers verify by IP range/reverse-DNS, not just the header, so a spoofed UA can pass robots.txt review but still get edge-blocked. Use each vendor's own bot-verification tool where available.
- Ask ChatGPT, Perplexity, Claude, and Copilot about "Carrowmore API documentation" starting ~1–2 weeks post-fix, not immediately — indexes need to recrawl, and a competitor who's been getting cited for two months has a head start in the citation graph that won't disappear the day you unblock.
- Put ongoing AI-citation tracking in place (e.g., Otterly, Peec AI, ZipTie, LLMrefs) so the next regression is caught in days, not two months, instead of marketing noticing by accident.