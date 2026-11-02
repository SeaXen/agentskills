# Otterpost docs budget: forecast + reporting plan

**Bottom line for the VP up front:**
- The 14-page candidate list should ship as **10 pages**, not 14 — 4 of the concept queries collapse into 3 consolidated pages without losing query coverage. That alone cuts the ask by ~30%.
- Realistic **Year-1 organic traffic across all 10 pages: roughly 2,000–7,000 sessions total** (180–570/month by month 12), and it's *not* evenly spread — the 7 product-specific pages carry nearly all of it. This is an **Estimated** range (see method below), not a measured number — nobody has pulled real search data on Otterpost yet because the pages don't exist.
- Your suspicion about the "what is X" queries is correct, and it's the single most important thing in this forecast: **forecast near-zero clicks for the concept pages.** Their job isn't traffic, it's being the thing an AI answer gets assembled from. Traffic and value are no longer the same axis for that half of the list — that's not a hedge, it's a documented shift (below).
- "Pages published" is the wrong headline metric for the quarterly report. It tells the VP what the writing team did, not whether the budget worked. Replacement metrics and a template are at the end.

Everything below is the full keyword map this forecast is built on, per the developer-keyword-research skill's standard shape.

---

## Scope

- **Product**: Otterpost, transactional email API (SMTP + HTTP send, webhooks for delivery events).
- **Axes**: language/SDK (Node.js, Python — assumed from "first hour" usage, confirm), deployment (cloud API only, no self-host assumed).
- **Adoption mode**: both. Individual (a developer wiring up sending) dominates the error/reference/how-to pages; company adoption (a champion checking vendor fit) drives the evaluation/comparison/migration set below.
- **Owned surfaces**: docs site, blog (assumed — confirm before routing anything to the blog).
- **Sources available this round**: none. No search-console export, docs-search log, ticket export, or issue tracker was supplied, and the pages don't exist yet, so there's no first-party query data to pull. This is a **pre-launch keyword map** — every evidence item below is Estimated, not Measured.
- **70% first-party evidence floor**: lowered to 0% explicitly, for the reason above. Do not present this map to the VP as validated demand — present it as a prioritized bet with a stated method, and re-run the forecast against real data (Search Console + docs-search logs) once the first wave has been live 60–90 days. That re-run is what turns "Estimated" into "Measured" for the next budget cycle.

## Ranked clusters

Sorted by outcome per page-hour, highest first. Evidence is Estimated throughout (source: Ahrefs long-tail distribution pattern — ~93% of technical queries sit under 10 monthly searches — plus reasoning about incumbent strength; no first-party or tool pull was possible this round).

| Cluster | Primary query | Variants | Family | Evidence | Incumbent | Target surface | Priority |
|---|---|---|---|---|---|---|---|
| Webhook signature verification failed | `otterpost webhook signature verification failed` | "invalid webhook signature otterpost", "webhook 401 otterpost" | Error | Estimated, low but high-intent volume once there's an install base; no source to pull yet (2026-09-20) | none — product-specific, doesn't exist elsewhere | Error entry | P1 |
| Send transactional email with Node.js SDK | `send email otterpost node.js` | "otterpost node example", "otterpost sdk quickstart" | Reference lookup | Estimated 10–40/mo at maturity, scales with signups | none — only Otterpost can document its own SDK | Reference page w/ runnable example | P1 |
| Set up DKIM for your sending domain | `otterpost dkim setup` | "otterpost verify domain", "otterpost dns records" | Task how-to | Estimated 10–30/mo; this is the #1 activation blocker for every ESP (domain verification) | none product-specific; generic DKIM explainers don't cover Otterpost's DNS UI | How-to guide | P1 |
| Rate limits | `otterpost rate limits` | "otterpost throttling", "otterpost 429" | Evaluation | Estimated 15–50/mo; evaluation queries convert disproportionately (this is company-adoption — also listed below) | pricing page, no numbers (assumed) | Trust/limits page | P1 |
| Email authentication for transactional senders (DKIM/SPF/DMARC, Otterpost-specific) | `otterpost dkim spf dmarc` | folds in "what is dkim", "what is spf", "what is dmarc" as variants — see Do not target | Concept (product-anchored) | Estimated 5–20/mo direct clicks; real value is citation, not clicks | Cloudflare Learning Center, Google Workspace Help, dmarcian — strong, not stale | Explanation page, product-anchored | P2 |
| SMTP vs API sending | `smtp vs api sending` | "smtp relay vs http api email", "why use an api for transactional email" | Concept (decision-shaped) | Estimated 20–60/mo — broader category term, but architecture-decision queries hold up better against AI summarization than pure definitions | mostly other ESPs' own self-serving blog posts — genuine winnability gap | Explanation / decision page | P2 |
| Bounce rates and bounce types on Otterpost | `otterpost bounce rate` | folds in "what is a bounce rate", "hard bounce vs soft bounce" — see Do not target | Concept (product-anchored) | Estimated 5–15/mo direct clicks; citation value only | Mailchimp/Twilio/Validity resource hubs — strong on the generic term | Explanation page, product-anchored | P2 |
| Otterpost vs Postmark | `otterpost vs postmark` | "otterpost alternative to postmark", "postmark alternative" | Comparison | Estimated 20–60/mo, driven mostly by Postmark's own existing demand | Postmark's own comparison content, and third-party "alternatives" roundups | Comparison page | P3 |
| Migrate from SendGrid to Otterpost | `migrate sendgrid to otterpost` | "sendgrid alternative otterpost", "switch from sendgrid" | Migration | Estimated 10–30/mo — small audience, largest single outcome per conversion (also company-adoption set) | none — new page | Migration guide (review every 6mo) | P3 |
| Otterpost with Next.js | `otterpost next.js integration` | "send email next.js api route otterpost" | Integration | Estimated 15–40/mo | none product-specific | Integration guide | P3 |

**High-value clusters the ratio demoted, and what promotes them:** Migration (`migrate from SendGrid`) sits at P3 despite being the single largest potential outcome (a won switch), because it costs the most to write and maintain (borrowed engineering time, review every release). Promote it to P1 the moment a competitor ships a breaking change or a pricing hike — that's the one window where migration content converts fast and cheap.

## Company-adoption set

Kept separate so the ratio above doesn't bury it — these are champion-typed queries, not user queries.

| Cluster | Primary query | Family | Evidence | Target surface | Priority |
|---|---|---|---|---|---|
| Rate limits | `otterpost rate limits` | Evaluation | Estimated 15–50/mo, disproportionate conversion value | Trust/limits page | P1 |
| Otterpost vs Postmark | `otterpost vs postmark` | Comparison | Estimated 20–60/mo | Comparison page | P2 |
| Migrate from SendGrid to Otterpost | `migrate sendgrid to otterpost` | Migration | Estimated 10–30/mo, highest value-per-conversion on the map | Migration guide | P2 |

## Fix first

- **DKIM concept vs. DKIM setup**: two different pages, two different intents — don't let the how-to page re-explain DKIM. The task how-to ("Set up DKIM for your sending domain") should link to the concept page for the explanation and stay focused on the Otterpost-specific DNS steps. This is the one cannibalization risk in this list if both get written independently.
- No existing Otterpost pages were checked against this list (none were supplied) — re-run step 2 (screening) against the actual current docs site before writing anything, in case any of these already exist as thin stubs.

## Do not target

- **"What is DKIM" / "what is SPF" / "what is DMARC" as standalone generic pages** — owned by neutral, deep standards explainers (Cloudflare Learning Center, Google Workspace Help, dmarcian, M3AAWG) that are not stale, not version-mismatched, and already complete. Same refusal logic as a reference lookup owned by upstream documentation — there's no winnability edge on the raw term. Redirect that demand into the one product-anchored companion page above instead of competing head-on.
- **"What is email deliverability" as a standalone page** — same reasoning; the big ESPs (Twilio SendGrid, Mailchimp, Postmark) already run deep content-marketing operations on this exact term. Fold it as framing inside the bounce-rate and authentication pages rather than building a dedicated page for it.

*(Not SERP-verified live this round — no browsing was done against current results. Confirm with the merge test in the skill before finalizing; this is a judgment call from incumbent reputation, not a measured refusal.)*

## Backlog

None parked this round — no shipping-capacity ceiling was given, so all 10 recommended pages are shown above with a P1/P2/P3 phasing that can double as a two-quarter plan. Once you confirm actual writer-hours/quarter, cut the P3 row down further and park the rest here with today's date.

---

## The traffic forecast, in full

The VP's question — "how much traffic will these 14 pages bring" — is actually two different questions once you split the list, and collapsing them into one number would be the wrong deliverable.

**For the 7 product-specific pages (error, reference, how-to, evaluation, comparison, migration, integration):** traffic is real, forecastable, and small — this is branded, long-tail, low-competition search. Combined estimate: **150–450 sessions/month by month 12**, scaling with signups (nobody searches "Otterpost webhook signature failed" until there are Otterpost users generating that failure — this traffic follows adoption, it doesn't precede it). Their value isn't primarily the session count anyway — it's activation speed and deflected support tickets, which this forecast doesn't capture and your support team's ticket volume will.

**For the 3 concept-derived pages (DKIM/SPF/DMARC, bounce rates, SMTP vs API):** forecast clicks near zero — **combined 30–120 sessions/month at maturity**, most of it on the "SMTP vs API" decision page, least on the pure definition pages. Two independent reasons stack here, and both point the same direction:
1. **Incumbent strength.** These terms are already owned by high-authority, non-stale category explainers. A new page realistically doesn't crack page one regardless of AI.
2. **The step itself is being displaced.** 84% of developers in Stack Overflow's 2025 survey use or plan to use AI tools, and JetBrains' 2025 ecosystem survey ranks "searching for development information" as the #2 task developers delegate to AI, right after writing boilerplate — the search step, not just the search result, is moving. Google's own AI Overviews reduce clicks to underlying sites by a similar order.

That doesn't mean these 3 pages are worthless — it means **click count is the wrong measure of their return.** As Rand Fishkin put it, describing this exact shift: "fewer visits, but the same level of influence" — the assistant still has to assemble its answer from something. The return on these 3 pages is whether Otterpost is *in* the answer when someone asks an assistant about DKIM in the context of transactional email, not whether they click through. Track that with citation monitoring, not sessions (reporting plan below).

**Confidence and how to tighten it:** every number above is Estimated — reasoned from category patterns (Ahrefs' long-tail distribution) and incumbent analysis, not pulled from any tool or export, because none was available for a product with no live pages yet. Before this goes in front of the VP as a committed number, spend one hour doing the cheap, real version of this check: pull Ahrefs/Semrush estimated volume for the 7 product-specific and comparison/migration terms using **competitors' equivalent pages as comparables** (e.g., what does Postmark's own rate-limits page or SendGrid's own migration page actually rank/get, today, for the equivalent query) — that's a legitimate tier-8 proxy you can run this week without waiting for Otterpost to have any of its own data.

---

## The reporting plan

**On "number of pages published" as the quarterly headline:** don't lead with it. It measures what the writing team shipped, not whether the spend worked — a team can publish 14 pages that get nothing, or 6 that move real numbers, and a page-count KPI can't tell those apart. It's also the easiest number to game (ship more, thinner pages) the moment it's the thing being judged. Keep it, but as a footnote line for parity with how other teams report, not as the outcome.

**What actually answers "did the budget work," to replace it as the headline:**

| Metric | What it shows | How to pull it |
|---|---|---|
| **Coverage** | Share of the 10 ranked clusters with a live page | Count against this map, each quarter |
| **Movement** | Striking-distance queries (avg. position 5–20) that crossed into top results | Search Console query export, cut to the 5–20 window, quarter over quarter |
| **Arrival** | First-party query counts for the exact target strings, after each page ships | Search Console, joined to landing page — this is also what converts this quarter's Estimated evidence into Measured evidence for the next map |
| **Citation rate** (the metric that speaks directly to your DKIM/bounce-rate suspicion) | Whether Otterpost shows up as a cited source when an assistant answers the query, independent of clicks | Monthly manual check: run the 10 primary queries through ChatGPT, Perplexity, and Google AI Overview; log cited/not-cited and who's cited instead. A paid tool (Otterly AI, Peec AI, or ZipTie) automates this across platforms once the list is worth tracking monthly instead of by hand |
| Pages published (footnote only) | Writing-team activity, for parity with other teams' reports | Simple count |

**Quarterly report template:**

> **Docs content — Q[X] 2026**
> - Shipped: N/10 pages (footnote: activity, not outcome)
> - Coverage: N/10 target clusters live
> - Movement: N queries crossed from striking distance into top results
> - Arrival: [exact session/query counts for shipped pages, Measured]
> - Citation rate: N/10 primary queries cited by at least one of ChatGPT/Perplexity/AI Overview, up/down from last quarter
> - Notable: [any concept-page citation win worth naming specifically — this is usually the most persuasive line in the deck, because it's the number that didn't exist as a KPI before AI search]

This gives the VP the same-shaped report other teams produce (a count, a trend line), but the number that actually justifies renewing the budget next quarter is Arrival + Citation rate, not page count — and it directly answers the question buried in "I suspect an assistant just answers outright now": yes, confirmed, and here's the number that tracks it instead of pretending it isn't happening.

---

## Pass threshold (stated per the skill's requirement)

1. Every ranked keyword carries an evidence item with source, count, date, and a label — **pass**, all labeled Estimated with method stated.
2. ≥70% of ranked clusters draw top evidence from tiers 1–4 — **fails as stated; floor explicitly lowered to 0% this round** (Scope section) because no first-party source existed for a pre-launch page set. Re-run this check after the first wave ships.
3. No cluster ranked on tool volume alone — **pass**; no tool was even queried this round, ranking is family-efficiency + incumbent reasoning.
4. One canonical target per cluster, no collisions — **pass**, including the DKIM concept/setup split under Fix first.
5. Do-not-target list non-empty — **pass** (2 entries, generic DKIM/SPF/DMARC/deliverability terms).
6. Sort stated, demoted high-value clusters named with promotion condition, company-adoption set has its own filled count — **pass**.