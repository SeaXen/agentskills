## The keyword tool got the sort backwards

Search-volume tools measure Google demand. They have no visibility into two things that matter more for a 900-team paying-customer API business: **support cost** and **buyer fit**. That's exactly where this list breaks.

- The "bottom three" show 0/mo because they're branded, in-product error strings — nobody Googles `hookline replay failed webhook` before they're already a customer stuck on your dashboard. Zero organic volume is the *expected*, correct reading for this content type, not evidence it's worthless. It's not top-of-funnel content; it's support deflection, and support deflection has a hard-dollar ROI (ticket cost, CSAT, retention) that a keyword tool can't see at all.
- The "top four" score well on volume/KD but two of them are weak matches for who actually buys Hookline. `what is a webhook` (18k/mo, KD 71) pulls in students, curious PMs, and people researching the concept generically — not people evaluating a delivery API. It's also a SERP already owned by Svix, Hookdeck, and generic explainer sites with years of head start. High cost, low buyer-fit, long payback.

Treat "drop the bottom three, build the top four" as the wrong axis. The right axis is **buyer stage + cost to produce + who's already asking**, not raw search volume.

## Prioritized build order

| # | Piece | Volume/KD | Buyer stage | Why this slot |
|---|---|---|---|---|
| 1 🎯 | KB pages: `WEBHOOK_SIGNATURE_MISMATCH`, `429 too many requests`, `replay failed webhook` | 0/mo, KD n/a (no SERP = no competition, not "hard") | Existing customer, mid-incident | Cheapest content you'll ever ship — a page per error state, written once from the actual error copy. Directly reduces Zendesk volume for your highest-friction moments (auth failures and rate-limit confusion are classic churn triggers for API products). Ranks #1 instantly since nobody else writes about your error codes. Ship this week. |
| 2 🎯 | "Webhook Retry Best Practices (with exponential backoff examples)" | 390/mo, KD 34 | Implementation | Lowest KD of the four generic terms — realistic to rank without months of link-building. Doubles as documentation for your own retry behavior, so it's not throwaway marketing content, it teaches the product. |
| 3 | "Webhook Delivery Service: What to Look for (and how Hookline handles it)" | 2,400/mo, KD 62 | Consideration/decision | Closest term to your actual product category — highest commercial intent on the list. Worth the harder KD because it's bottom-of-funnel, not top. Build as your pillar/cornerstone page; the retry piece and error-code KB pages can interlink into it. |
| 4 | "Webhook Testing Tool" — comparison/round-up, or a lead-magnet if you have (or can ship) a free tester | 1,300/mo, KD 55 | Implementation/consideration | Decent intent, product-adjacent. If Hookline has any internal debugging/replay UI, spin a stripped-down free version — testing-tool content converts far better paired with an actual tool than as a standalone article. |
| 5 ⚠️ | "What Is a Webhook?" | 18,000/mo, KD 71 | Awareness (weak buyer fit) | Biggest number on the sheet, worst fit. Most of that traffic isn't shopping for a delivery API. Don't skip it forever — it's good for brand/AI-answer-engine citations long-term — but don't spend scarce content resources here before 1–4 are shipped and compounding. If you do it, make it a fast, well-structured 800-word definition, not a 3,000-word assault on an entrenched SERP. |

## Before you lock this, pull three things

**Zendesk (12 months).** Count tickets by the exact error strings on this sheet, *plus* adjacent ones not on it (timeout, idempotency-key conflicts, malformed payload, signing-secret rotation). Rank the KB backlog by ticket volume × resolution time — that reorders item 1 into which specific error page ships first, and probably surfaces 2-3 more pages this keyword sheet never considered because a generic tool can't see them.

**Docs search logs (6 months).** Pull the top zero-result and low-result internal queries. This is stronger signal than Search Console for what to write next, because it's searched by people already inside the paid product — a zero-result docs search is a support ticket that hasn't been filed yet. Cross-check the exact phrasing against your KB page titles/headers before publishing; match their words, not the keyword tool's.

**Search Console.** Don't just check the 7 terms on this list (expect ~0 impressions on the branded ones — that's fine). Instead pull your top 50-100 queries by impressions at position 5-20. That's where you already have partial topical authority the keyword tool doesn't show — often long-tail variants of retry/signature/rate-limit language — and those are the cheapest rankings to push into page 1 with a light content refresh, cheaper than any of the five pieces above.

## Sequencing

Ship 1 and 2 in the next two weeks — near-zero cost, immediate retention/support payoff, and 2 is genuinely low-difficulty. Start 3 as the bigger investment in parallel since it'll take longer to rank regardless. Slot 4 once you've decided whether a free tool is in scope — the article alone is a weaker bet than article+tool. Revisit 5 only after Search Console/Zendesk pulls are done and 1-3 are live; if the docs-search data surfaces higher-value gaps in the meantime, this is the one to bump for them.