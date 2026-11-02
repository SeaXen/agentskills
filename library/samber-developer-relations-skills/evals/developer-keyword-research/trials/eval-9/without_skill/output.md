# Otterpost — 14-Page Content Forecast & Quarterly Reporting Plan

## Bottom line

Forecast for the 14 pages, at steady state (month 9–12, not this quarter): **roughly 5,400–19,400 organic sessions/year and 110–980 signups/year**, wide range because half the list is generic glossary content competing against Mailgun/Postmark/SendGrid's existing resource centers. That half is also the exact content type Google AI Overviews and chat assistants now answer directly in the SERP — so don't budget or report on it as if it behaves like the other half. Recommend approving the budget, but reweighting the mix (below) and reporting outcomes, not just page count, alongside the page-count number the VP wants.

**Confidence: low-medium.** No live keyword-volume pull was available for this memo — assumptions are stated per line so they're falsifiable, not fabricated. Section 6 below is a cheap next step that converts every range here into a real number before the budget is finalized.

## 1. What the 14 pages are (and one caveat)

Only 3 of the 14 titles were provided. The other 11 are grouped by inference from "half the list is DKIM/SMTP-vs-API/bounce-rate style" — **validate this grouping against the real list before treating the numbers below as final.**

| Bucket | Est. count | Funnel stage | Examples given | Assumed siblings |
|---|---|---|---|---|
| A — Definitional/glossary | 7 | Awareness | "what is DKIM," "what is a bounce rate" | what is SPF/DMARC, what is an open rate, what is sender reputation, what is a soft vs. hard bounce |
| B — Comparison/consideration | 4 | Consideration | "SMTP vs API sending" | transactional vs. marketing email, self-hosted vs. API sending, Otterpost vs. [competitor] |
| C — Product/implementation | 3 | Decision/activation | — | how to reduce bounce rate via API, webhook events for delivery tracking, setting up DKIM for transactional email |

## 2. Traffic forecast

Point estimates would be false precision on a 14-page list built from 3 known titles. Ranges instead, with the assumption driving each number stated so the VP can challenge it.

| Bucket | Vol/keyword (mo., blended) | Ranking timeline | AI-Overview exposure | CTR after AI-Overview discount | Sessions/page/yr (steady state) | Conv. rate | Signups/yr (bucket total) |
|---|---|---|---|---|---|---|---|
| A — Definitional (×7) | 800–2,500 | 6–12+ mo. — competing with incumbent ESPs' resource centers, page ranks 4–10 realistically | **Very High** — classic "what is X" queries are Google's first AI-Overview target | 15–25% baseline cut 40–55% | 180–720 | 0.3–0.8% (mixed, low-intent audience) | 4–40 |
| B — Comparison (×4) | 100–500 | 3–6 mo. — moderate difficulty, Otterpost has home-field advantage in its own comparisons | High, but comparisons resist single-answer extraction; also the single highest AI-citation format (~33% of AI citations per GEO research) | 20–35% | 480–1,800 | 2–5% | 40–360 |
| C — Implementation (×3) | 50–300 | 4–12 wks — long-tail, low difficulty, product-specific | Low-medium — AI answers can't substitute working code | 25–40% | 720–2,400 | 3–8% | 65–576 |
| **Total (14 pages)** | | | | | **~5,400–19,400 sessions/yr** | | **~110–980 signups/yr** |

Two things that matter more than the range width:

- ⚠️ **Quarter 1 is near-zero.** New pages, zero backlinks, no ranking history. Most of this traffic lands in quarters 2–4. Don't let the first quarterly report look like a failure — set that expectation with the VP now.
- ⚠️ **Bucket A is 50% of the page count and ~2–4% of the forecasted signups.** That's the core tension in this budget ask: half the effort is going to the content least likely to convert *and* most exposed to being answered before the click ever happens.

## 3. The "AI just answers it now" concern is correct, and it's measurable

Your instinct on the definitional half is backed by data, not a hunch:

- AI Overviews now appear on **~45% of Google searches**, and Google's own numbers show they cut clicks to websites by **up to 58%** — concentrated exactly on informational "what is X" queries, which correlate "Very High" with AI Overview presence (vs. "Low-Medium" for transactional queries).
- This isn't unique to Google. ChatGPT-with-search and Perplexity answer "what is DKIM" or "what is a bounce rate" inline, citing sources rather than sending a click.

**The reframe, not the conclusion "kill these pages":** citation is not traffic, and it isn't worthless. Comparison content (Bucket B) has the single highest AI-citation share of any format (~33%), and even Bucket A content — if it's the kind an AI system extracts and cites — builds brand presence in answers your prospects see even when they never click through. The mistake would be to fund 7 separate thin glossary pages and *measure them on sessions*, when their real return is citation/share-of-voice, not clicks.

## 4. Recommendation: rebalance before you spend

1. **Consolidate the 7 Bucket-A topics into 1–2 hub pages** (e.g., one "Email Deliverability Glossary" with FAQ-schema'd sections for DKIM, SPF, bounce rate, etc.), instead of 7 standalone pages. Consolidated glossary/definition pages earn ~1.5x their page-share in backlinks — a hub is both cheaper to produce and a better link/citation magnet than 7 thin pages competing against themselves.
2. **Reallocate the freed budget into Bucket B and C** — where the forecast, the citation data, and the conversion rates all agree the return is better.
3. Net effect: publish fewer total pages than 14, which cuts against the "number of pages published" metric other teams report — flag that trade-off explicitly to the VP now (see reporting plan below) so it isn't a surprise in Q1.

## 5. Quarterly reporting plan

Give the VP the metric they asked for, but never let it stand alone — pair it with outcome metrics on the same table so "pages published" can't be read as the success signal by itself.

| Metric | Source | Why it's here |
|---|---|---|
| **Pages published (count)** | Manual/CMS | What the VP asked for, matches other teams' format |
| Organic sessions (new pages, cumulative) | GA4 + GSC | The actual thing being forecast in Section 2 |
| Keyword rankings gained (top 3 / top 10) | GSC | Leading indicator before traffic materializes — explains a quiet Q1 |
| AI citation presence (# pages cited, which engine) | DIY monthly check: run each page's target query through ChatGPT, Perplexity, Google, log in a sheet | Direct answer to the VP's "does an assistant just answer this now" concern — turns a suspicion into a tracked number |
| Signups/demo requests attributed to docs | GA4 event `signup_completed` with `source=docs`, UTM-tagged internal links | Ties content spend to pipeline, not just traffic |
| Bucket mix published (A/B/C split) | Manual | Makes the rebalancing in Section 4 visible quarter over quarter |

**Instrument this before the first page ships**, not after:
- GA4 event `docs_page_viewed` and `signup_completed` (property: `source`, `page_slug`) — object_action naming, consistent with existing tracking conventions.
- UTM convention for any distribution links (newsletter, social) so "docs traffic" isn't conflated with paid/referral.
- GSC property verified and filtered by URL path for these 14 pages specifically, so ranking progress is visible without wading through the whole site's queries.
- A standing spreadsheet for the monthly AI-visibility check (20 queries × ChatGPT/Perplexity/Google AI Overview × pass/fail + who's cited instead) — no paid tool needed to start this.

Report cadence: quarterly to the VP, but pull the GSC ranking and AI-citation numbers monthly internally — SEO/AI-citation movement is a leading indicator you want 8–10 weeks before the quarterly number lands.

## 6. What would sharpen this before you finalize the budget

- Pull real search volume + difficulty for all 14 actual keywords via GSC (if any already have impressions) or a keyword tool — this replaces every range above with a number. Under 2 hours of work, and it's the single highest-leverage thing to do before sign-off.
- Confirm the other 11 titles — the A/B/C split above is inferred from 3 examples and could be wrong in either direction.
- Run the AI-visibility check (Section 5) on the 3 known queries *today*, pre-publish — it'll show you, concretely, what you're up against on Bucket A before a single page is written.