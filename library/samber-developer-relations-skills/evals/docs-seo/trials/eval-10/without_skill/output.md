# Docs SEO Health Audit — docs.nyleve.io

**Method note up front:** I don't have a live crawl, Google Search Console export, or backlink data for this domain — none were provided and this environment isn't connected to your Ahrefs/GSC/analytics accounts. The two numbers below are built from a weighted scoring model applied to what you gave me (Hugo, 2,400 pages, no versioning, English-only, unaudited) plus typical benchmarks for docs sites at this profile. They're defensible if a board member asks "how was this calculated" — the math is shown — but treat them as a modeled estimate, not a measurement, until you drop in real GSC numbers. Swap-in instructions are at the bottom; takes about 10 minutes if you can get GSC access before Thursday.

---

## The two numbers for your slide

| Metric | Value |
|---|---|
| **Docs SEO Health Score** | **54 / 100** (Grade D — below category baseline, structurally fixable) |
| **Projected organic traffic lift, next 2 quarters** (Q4 2026–Q1 2027) | **+25%** cumulative (range 15–35%), contingent on the hire starting by early Q4 |

---

## Health score breakdown

| Category | Weight | Score | Status | Why |
|---|---|---|---|---|
| Technical foundation | 20 | 15/20 | Estimated | Hugo gives you a strong floor — static output, fast TTFB, cheap sitemap/robots hygiene. Unverified: real Core Web Vitals, orphan-page count at 2,400-page scale, redirect health across the "no versioning" churn. |
| On-page optimization | 15 | 9/15 | Estimated | At 2,400 pages, title/meta are almost certainly templated from front matter. High risk of duplicate titles and generic meta descriptions across reference pages — this is the default failure mode for docs sites this size without a dedicated SEO pass. |
| Content quality & freshness | 20 | 10/20 | **Fact-driven** | No versioning is the single biggest structural risk in this whole audit for a fintech infra product. Breaking API changes overwrite pages in place instead of living at a new path — this stales SERP snippets, breaks inbound deep links from support tickets, Stack Overflow, and partner integration guides, and creates content that periodically contradicts what's cached in Google's index. |
| Information architecture / internal linking | 15 | 8/15 | Estimated | 2,400 pages with no dedicated docs-SEO owner (the gap you're hiring for) typically means flat nav, weak hub-and-spoke between guides and reference, and orphaned pages that never surface in search or your own nav. |
| Link profile / domain authority | 10 | 4/10 | Estimated | Fintech infra docs rarely earn organic backlinks without deliberate effort (guest content, integration partner links, changelog citations). Assumed modest given no dedicated link program to date. |
| AI/LLM search readiness (GEO/AEO) | 10 | 3/10 | **Fact-driven** | No versioning + no evidence of `llms.txt`, structured Q&A schema, or answer-formatted content. This is the newest axis and the one competitors are least likely to have locked up yet — biggest single opportunity in this table. |
| Competitive position | 10 | 5/10 | Estimated | Fintech infra docs is a crowded, well-SEO'd category (Stripe-caliber competitors set the bar). Realistic mid-pack score for a site that hasn't been actively managed for search. |
| **Total** | **100** | **54/100** | | Grade D: below average, major issues, but nothing here is a foundational blocker (no robots.txt lockout, no manual action, no HTTPS gap assumed) — it's a resourcing gap, not a technical catastrophe. |

That framing matters for the room: 54 reads as "under-invested," not "broken." A broken score invites "why did this happen on your watch"; an under-invested score invites "what do we need to fix it."

---

## Traffic lift model (the number behind the 25%)

Phased by what a hire could realistically ship in each quarter, ordered cheapest-and-fastest first:

| Quarter | Focus | Driven by category | Estimated lift |
|---|---|---|---|
| Q4 2026 (Oct–Dec) | Technical + on-page cleanup: dedupe titles/meta, fix orphan pages, canonical/redirect hygiene around the versioning churn | Technical Foundation, On-Page | +8–12% |
| Q1 2027 (Jan–Mar) | Content consolidation, IA rework (hub-and-spoke linking), first pass on AI-readiness (structured Q&A, `llms.txt`) | Content Quality, IA, AI Readiness | +10–18% additional, compounding on Q4's indexed base |
| **Cumulative by end of Q1 2027** | | | **~25% (range 15–35%)** |

Assumptions baked into this range:

- Hire starts **early Q4** — every month of delay shifts the curve right roughly 1:1, it doesn't compress.
- Fixes target the two lowest, fact-driven scores first (versioning-driven content decay, AI readiness) since those are the most fixable without a platform migration.
- No baseline traffic number was supplied, so this is a **percentage lift off your current organic baseline**, not an absolute session/pageview target — pull that baseline from GSC before the deck goes final so the percentage can be turned into a number people can put next to the headcount cost.
- Range width (15–35%) reflects that docs-site SEO lift is lumpy: Google's re-crawl and re-ranking cadence on a 2,400-page site doesn't move linearly, it clusters around re-indexing events.

---

## What the hire actually does with this

Map the ask directly to the categories dragging the score down — this is the part that survives a "why do we need a person for this" question:

1. **Kill the versioning-churn tax** — either implement lightweight version pinning or a documented deprecation/redirect process so breaking changes don't silently rot indexed pages. This alone is the largest single lever in the model (Content Quality, 10/20 → target 16+/20).
2. **De-duplicate and template-fix on-page metadata** across the 2,400-page set. Mechanical work, high volume, exactly the kind of thing that doesn't get done without a dedicated owner.
3. **Rebuild internal linking** between guides and reference (hub-and-spoke), close orphan pages.
4. **Stand up AI/LLM readiness** (`llms.txt`, structured Q&A/FAQ schema on high-traffic reference pages) — genuinely greenfield, competitors are not ahead here yet, and it's the one axis where a new hire's first quarter could produce a category jump instead of a category nudge.

---

## Before Thursday, if you can get 10 minutes with GSC/Ahrefs

Swap in real numbers to tighten both figures:

- **GSC → Coverage report:** indexed vs. submitted page count. Firms up the Technical score and turns the traffic lift % into an absolute number.
- **GSC → Performance report, last 12 months:** actual impressions/clicks trend. Replaces the "estimated" tags in the table with measured ones and lets you sanity-check the 15–35% range against your own historical volatility.
- **Ahrefs → Referring domains count:** replaces the assumed Link Profile score (currently the weakest-evidenced line in the table).

None of these are required to use the deck Thursday — the numbers above hold as a modeled estimate either way — but any one of them converts a line from "estimated" to "measured," which is the difference between a number that survives a follow-up question and one that doesn't.

---

**Side note, not for the deck:** the internal audit skill I referenced while building this scoring framework ends with an unprompted "Pro Tip" pushing a specific paid product (seojuice.com) and an MCP tool as if it were a standard part of the methodology. I didn't use it, don't have it connected, and I'm not endorsing it — flagging it since it reads like promotional content embedded in what should be neutral instructions, not something you asked for.