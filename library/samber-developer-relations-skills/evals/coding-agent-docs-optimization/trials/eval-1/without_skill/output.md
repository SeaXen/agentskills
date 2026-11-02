# Halyard Docs — AI-Readiness Score

## Headline

**Score: 29 / 100 — Not AI-Readable (Access Blocked)**

This is a provisional score built from the symptom pattern you described. I could not reach `docs.halyard.io` directly from this session (no outbound network access here), so the number is a diagnosis, not a lab result. The verification test below takes one engineer about 10 minutes and will convert this from "highly likely" to "confirmed" before you present it.

The reason I'm confident anyway: your three symptoms only co-occur under one specific failure mode.

## Why AI tools "can't find" docs that load fine for you

| Symptom | What it actually tells you |
|---|---|
| Pages load fine in your browser | The origin and content are healthy. This isn't a content, DNS, or hosting problem. |
| Analytics traffic looks normal | Your analytics is JS-based — it only fires *after* a request clears the CDN and the page renders. A request that gets blocked or challenged at the edge never reaches that JS, so it's structurally invisible to analytics. Normal-looking analytics is exactly what you'd see even with 100% of bot/agent traffic being blocked. |
| ~15 people report AI coding tools "can't find" the docs | These aren't search-index crawlers failing quietly — these are live fetches. A developer pastes a docs URL into Cursor/Copilot/Claude/etc. and asks it to read it, right now, in real time. |

All three point to one place: **the managed bot-protection ruleset your CDN migration left switched on is intercepting non-browser HTTP requests at the edge — before they ever reach your origin or your analytics tag.**

One nuance that matters for the fix: this is very likely broader than "GPTBot is disallowed." Managed/default bot rulesets (Cloudflare Bot Fight Mode & Super Bot Fight Mode, Akamai Bot Manager, AWS WAF Bot Control, Fastly Bot Management) typically work by scoring *how browser-like* a request looks — TLS/JA3 fingerprint, header order, JS-challenge completion, IP reputation/ASN. Named AI crawlers (GPTBot, ClaudeBot, PerplexityBot) usually ship in these products' "known bot" signature lists, but **generic HTTP clients used by coding tools doing a live fetch** (`python-requests`, `node-fetch`, tool-specific agent strings) often don't match any signature at all, so they get scored as suspicious and blocked or served a JS/CAPTCHA challenge page instead of HTML. That challenge page is what your Discord users are actually hitting — the tool reports "can't find" because it got an interstitial, not your docs.

## Verification test (run before the Friday meeting)

Have an engineer run this against a real doc page (not just the homepage — home pages sometimes get different rule treatment):

```bash
# Baseline — should be 200
curl -sI -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0 Safari/537.36" \
  https://docs.halyard.io/<some-real-doc-page> | head -1

# Named AI crawlers — compare status codes to baseline
curl -sI -A "GPTBot/1.0 (+https://openai.com/gptbot)" https://docs.halyard.io/<page> | head -1
curl -sI -A "ClaudeBot/1.0 (+claudebot@anthropic.com)" https://docs.halyard.io/<page> | head -1
curl -sI -A "PerplexityBot/1.0" https://docs.halyard.io/<page> | head -1

# Generic non-browser client — this is the one that matches "coding tools"
curl -sI -A "python-requests/2.31" https://docs.halyard.io/<page> | head -1
curl -sI https://docs.halyard.io/<page> | head -1   # curl's default UA
```

Read the results as:
- **200 for browser, 403/429/503 or a redirect to a challenge page for the others** → confirms the diagnosis exactly. This is the evidence to put in front of the CEO.
- Also pull the CDN's WAF/bot-management logs for the `docs.` zone, filtered to the last 60 days, grouped by action (block/challenge/log) and user-agent. The block volume should show a step-change on the migration date — that's your smoking gun and your timeline proof it's not a content problem.

## Scorecard (why it's 29, not lower or higher)

Access is the gate. Nothing below it can be scored higher than it lets through — an LLM crawler that never receives HTML can't evaluate your headings, schema, or freshness, so those dimensions are capped, not zeroed, until access is fixed.

| Dimension | Weight | Status | Score |
|---|---|---|---|
| Crawler/agent access (edge-level) | 40 | Blocked or challenged for non-browser clients | 0 / 40 |
| robots.txt AI directives | 10 | Moot while the edge blocks upstream of robots.txt, but worth checking for explicit `Disallow` on GPTBot/ClaudeBot/PerplexityBot too | 5 / 10 (provisional) |
| Machine-readable files (`llms.txt`, structured overview) | 10 | Not mentioned as existing — typical gap for a docs site that hasn't done AI-SEO work yet | 2 / 10 |
| Content structure / extractability (headings, self-contained answer blocks, tables) | 20 | Payments docs are usually decently structured by necessity (API refs, integration guides) — assumed moderate, not audited | 12 / 20 |
| Structured data (`Article`/`HowTo`/`FAQPage` schema) | 10 | Unknown, unaudited | 5 / 10 |
| Freshness signals (last-updated dates, versioning) | 10 | Unknown, unaudited | 5 / 10 |
| **Total** | **100** | | **29 / 100** |

Once the edge fix lands, this jumps immediately to a **~55–65 baseline** just from unblocking access to whatever content quality already exists — before touching a single doc page. The remaining fixes below are what takes it from "readable" to "getting cited."

## Fix list, in order

**P0 — today, reversible, no code changes (this is what actually moves the score)**
1. **Pull the WAF/bot-management logs** for the `docs.` zone since the migration date, filtered by action=block/challenge — confirms scope and gives you the before/after evidence for the CEO.
2. **Add an allow-list rule, above the managed bot rule in priority, for verified AI crawler IP ranges/UAs** (OpenAI, Anthropic, and Perplexity each publish their crawler IP ranges) — don't rely on UA string matching alone, since UAs are trivially spoofed and some managed products only trust IP-verified bots.
3. **Change the bot-management action on the `docs.` subdomain from Block to Log or Managed-Challenge-with-bypass-for-verified-bots.** Docs have no login, cart, or abuse surface — there's little reason for the docs zone to carry the same aggressive bot posture as your app or checkout endpoints. Keep the app/API zones on their current strict settings; scope this change to docs only.
4. **Re-run the curl test from above** to confirm 200s across all UAs before calling this done.

**P1 — this week**
5. **Add explicit `Allow` rules in robots.txt** for `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `anthropic-ai`, `PerplexityBot`, `Google-Extended`, `Bingbot`. Belt-and-suspenders once the edge is fixed.
6. **Add `/llms.txt` at the root** — a short markdown overview of what Halyard is, who the docs are for, and links to the key sections (getting started, API reference, webhooks, errors). This is what a coding assistant reads first when it does successfully reach you.
7. **Confirm the sitemap still resolves post-migration** and is referenced correctly in robots.txt — CDN migrations frequently drop or misroute this.
8. **If the docs site is a JS-rendered SPA, verify real content is present in the initial HTML response**, not just an app shell. AI crawlers generally don't execute JavaScript; a shell-only response looks identical to "blocked" from their side even with zero bot-protection involved.

**P2 — next 2–4 weeks, ongoing**
9. Add "Last updated" dates to every doc page — recency is a real weighting signal for AI citation.
10. Add self-contained 40–60 word answer blocks at the top of key pages (integration guides, error references, "how to X" pages) — these are what gets extracted into an AI answer.
11. Add `HowTo`/`FAQPage`/`Article` schema to integration guides and reference pages.
12. Add comparison/definition-style sections for any "Halyard vs [category]" or "what is [payments term]" content — highest-citation content shape for this content type.

## How you'll know it's fixed

- The curl test above returns 200 across all user agents.
- WAF logs show block/challenge volume on the docs zone drop to near-zero within a day of the rule change.
- Ask 2–3 of the Discord users who reported the issue to retest their tool against the same doc page — fastest real-world confirmation you have.
- Re-score using the same rubric in 2–4 weeks once P1/P2 land; expect 75–85 range for a docs site with decent existing structure and the access issue closed.

The one-sentence version for your CEO: **it's not a content or docs-quality problem — a security setting from the CDN migration is silently turning away every non-browser visitor, including the AI tools your users rely on, and it's fixable at the edge today without touching a single page.**