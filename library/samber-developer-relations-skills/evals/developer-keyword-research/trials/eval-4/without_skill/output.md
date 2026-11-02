# Fernweh Docs Keyword Map — Q4 2026 Planning

**Basis:** 90-day docs search logs, 951 total logged queries across 7 terms. No error telemetry or Search Console yet — this map runs on search-log volume alone; treat rankings as directional, not final, until those land.

## Demand snapshot

| Query | Count | Share | Intent | Vendor named? |
|---|---|---|---|---|
| fernweh SDK init error 4013 | 310 | 32.6% | Troubleshooting | No |
| fernweh sampling rate default | 220 | 23.1% | Reference lookup | No |
| fernweh segment integration | 140 | 14.7% | Integration/instructional | **Yes — Segment** |
| fernweh snowflake export | 98 | 10.3% | Integration/instructional | **Yes — Snowflake** |
| fernweh migrate from Mixpanel | 77 | 8.1% | Commercial investigation | **Yes — Mixpanel** |
| fernweh vs Amplitude | 61 | 6.4% | Commercial investigation | **Yes — Amplitude** |
| what is product analytics | 45 | 4.7% | Top-of-funnel educational | No |

**40.2% of logged demand touches a query that names a vendor.** That's the load-bearing fact for this quarter — it decides more of the plan than volume does.

## Constraint filter

**Legal.** "Don't name a vendor" reads literally: it doesn't distinguish a competitor (Amplitude, Mixpanel) from an integration partner (Segment, Snowflake). I've applied it to all four. If legal's actual intent is narrower — comparison pages only, integration partners fine — that changes this plan materially (adds 238 searches of clean addressable demand back in). Worth a direct question to legal before next quarter's picks, not an assumption I make for them.

**Zero upkeep budget.** This cuts two ways beyond legal:
- Error-code and default-value pages are safe *only* if scoped to Fernweh's own, self-owned surface (its error taxonomy, its SDK defaults) — nothing on the other side of the doc can drift without Fernweh's own release drift.
- Anything describing a third party's API (Segment's source config, Snowflake's ingestion, Mixpanel's event model) needs upkeep Fernweh doesn't control and the team can't staff. This kills those page types even ignoring legal.

**Platform matrix.** Node/Python/Swift only. Any SDK-behavior page (error codes, sampling) must be one page with three tabbed snippets, not three pages — the 2-pages/quarter budget can't absorb a 3x multiplier per topic.

## Prioritized map

| Query | Vendor block | Upkeep risk if built as literally searched | Verdict |
|---|---|---|---|
| SDK init error 4013 | Clean | Low (Fernweh's own error codes) | **Build** |
| Sampling rate default | Clean | Low (Fernweh's own SDK default) | **Build** |
| Segment integration | Blocked | High (third-party API surface) | **Reframe or defer** |
| Snowflake export | Blocked | High (third-party API surface) | **Reframe or defer** |
| Migrate from Mixpanel | Blocked | High (third-party event model) | **Reframe, lower value** |
| vs Amplitude | Blocked | N/A — can't be built at all | **Reject for docs** |
| What is product analytics | Clean | Low, but not a docs job | **Route elsewhere** |

## This quarter's 2 pages

**1. SDK initialization error reference** (310 searches, 32.6%)
Build as a lookup table of *all* init error codes, not a single "error 4013" microsite — a family page absorbs future codes without a rewrite, which matters since no one will be maintaining it. One page, tabbed Node/Python/Swift where the error surfaces differently. Zero vendor risk, zero legal review needed.

**2. Sampling rate reference** (220 searches, 23.1%)
Default value, how it's set per platform, what changing it does to volume/cost. Self-contained, Fernweh-owned, no cross-team dependency to confirm before writing — the safest kind of "guaranteed to ship" page when the writer only gets two shots this quarter.

Combined: 530 searches, 55.7% of logged demand, cleared with zero legal exposure and near-zero future maintenance debt.

## Backlog — next quarter, conditional

**Generic export/CDP page** (candidate for Segment + Snowflake combined — 238 searches, 25%, would be the single biggest item if buildable)
The insight worth acting on: most "integrate with Segment" and "export to Snowflake" searches don't actually require naming either — both usually resolve to "point their generic ingestion mechanism (webhook / HTTP tracking API / S3 batch) at ours." If Fernweh already exposes a generic webhook or batch-export API, document *that*, vendor-neutral, and both search populations self-serve off one page.

This is conditional on two unknowns I can't confirm from here: (a) does that generic export mechanism actually exist yet, and (b) is it stable enough to write once and never touch. If either answer is no, this drops off the list entirely — don't commit a quarterly slot to a page that depends on unshipped functionality.

**Generic migration checklist** ("coming from another analytics tool" — partial credit against the 77 Mixpanel searches)
Event-taxonomy mapping worksheet, identity-resolution guidance, no named source product. Weaker than a real Mixpanel-specific guide would be, but legal-clean and low-upkeep. Lower priority than the export page — smaller volume, and the value delta vs. doing nothing is smaller.

## Rejected / not this team's problem

**"vs Amplitude" (61 searches).** This is a comparison query — the entire point is naming the competitor. No vendor-neutral version serves the actual intent. Legal's rule doesn't just block a page here, it blocks the *category*. If this demand matters, it's a marketing-site positioning-page problem with its own legal sign-off path, not a docs backlog item.

**"What is product analytics" (45 searches).** Top-of-funnel conceptual content belongs on the marketing/blog side, not in SDK docs, and at 4.7% of volume it's the weakest signal in the set. Flag to whoever owns content marketing; don't spend a docs-writer page on it.

## Before next quarter's pass

1. Ask legal directly whether the vendor-naming rule scopes to competitors or to any named third party — it's the single input that most changes this map.
2. Confirm whether a generic export/webhook mechanism exists before promising the CDP page a slot.
3. Once error telemetry or Search Console lands, re-cut this against actual error frequency and external query volume — right now "most searched in docs" is the only signal available, and it may not match "most common in production."