# Keyword map: Fernweh Analytics — Q4 docs targets

## Scope

**Product:** Fernweh Analytics, product analytics SDK. First-hour action: install the SDK and get first events flowing.

**Officially supported axes:** Node, Python, Swift. No other language/framework/runtime axis is confirmed, so none is used for expansion.

**Owned surfaces:** docs site confirmed (it has search logging). Blog, repo, changelog, forum: not confirmed by the team — treated as unavailable, not assumed to exist.

**Adoption mode:** both are present in the evidence, but company-adoption demand (comparison + migration) is the exact demand this run cannot act on — see Do not target and Company-adoption set.

**Shipping capacity — the binding constraint on this whole map:** ~2 pages/quarter, and zero budget for upkeep on anything already published. Per this skill's own rule, that ceiling doesn't just cap the ranked list, it deletes the standing-maintenance families outright: integration and migration guides need a re-test per framework release or a permanent "other vendor changed something" watch, which this team cannot staff. They're removed below, not parked.

**Legal constraint — independent of capacity, and just as absolute:** no page may name another vendor. Not a slow lane, a closed door. This kills every cluster that names a competitor or a partner product by name, regardless of its evidence strength.

**Sources used:**

- Tier 2 — docs-site search logs, 90 days (≈2026-06-22 to 2026-09-20), 7 queries, relayed by the product team. Labeled **User-provided** throughout (I did not pull the export myself), tier 2 regardless of label.

**Sources unavailable** (stated, not guessed around):

- Tier 1 — first-party query/Search Console data: not yet set up, per the brief.
- Tier 3 — support tickets / issue tracker: not mentioned, treated as unreachable this run.
- Tier 4 — product error telemetry: explicitly none.
- Tier 5 — public Q&A/forums: not pulled.
- Tier 6 — ecosystem counters (npm/PyPI/CocoaPods/SPM downloads): not pulled.
- Tier 7 — autocomplete/related searches: not pulled.
- Tier 8 — keyword-tool volume: not pulled; nothing here is ranked on it, so this doesn't gate anything.

Single-tier evidence base — everything below rides on tier 2 alone, with no cross-check from a second source. That's thin, but it clears the 70% first-party floor because tier 2 counts as first-party (tiers 1–4) and it's 100% of what's ranked. Re-run this map once Search Console and error telemetry exist; both would either confirm or reprioritize the two ranked clusters below.

**Unanswered interview items, defaulted rather than blocked on:** no committed launch date was given, so nothing here is treated as launch-urgent. One-off vs. compounding wasn't stated either, but the zero-upkeep budget forces a one-off-safe answer regardless of ambition: everything ranked below is a page that, once correct, mostly stays correct without a standing maintenance job.

## Ranked clusters

Sorted by outcome per page-hour, highest first. Both survivors are cheap (an hour each), low-maintenance, and name no vendor — the only shape of page this budget and this legal constraint both allow.

| Cluster | Primary query | Variants | Family | Evidence | Incumbent | Target surface | Existing URL or new | Priority |
|---|---|---|---|---|---|---|---|---|
| SDK init error 4013 | fernweh SDK init error 4013 | none logged — single phrasing observed | Error string | 310 docs searches / 90d (2026-06-22–2026-09-20, User-provided) | Estimated, not verified live: a proprietary Fernweh error code is unlikely to have any third-party page today | Error entry | new | P1 |
| Sampling rate default | fernweh sampling rate default | none logged — single phrasing observed | Reference lookup (config key default) | 220 docs searches / 90d (2026-06-22–2026-09-20, User-provided) | Estimated, not verified live: likely nothing indexed, possibly a stale community post | Reference page (config default + how to override) | new | P1 |

Both are named "P1" rather than ranked 1-then-2 by number, because the gap between 310 and 220 searches doesn't change the page shape, the cost, or the maintenance profile — ship whichever the writer can start first. If the 90-day log lets you confirm which SDK(s) each query actually came from, split before writing: error 4013 and the sampling default may not be identical across Node/Python/Swift, and a page that quietly assumes one SDK when the fix differs on another fails completeness on two-thirds of your supported base.

**High-value clusters this ratio demoted or removed, and what would change that:**

- *Migrate from Mixpanel* (77/90d) and *vs Amplitude* (61/90d) are exactly the two highest-value families on this skill's own value ordering (migration and comparison rank #1 and #2), and they carry real demand. They are not demoted by cost-ratio here — they're deleted outright by the legal constraint, which the ratio can't override. Promotion condition: legal clears vendor-naming content, or the team accepts a vendor-neutral version (see Do not target).
- *Segment integration* (140/90d) and *Snowflake export* (98/90d) are demoted twice over: legal blocks the vendor name, and even without that, a standing integration-maintenance job doesn't fit a zero-upkeep budget. Promotion condition: both constraints would need to lift together — legal clearance and added maintenance capacity.

## Company-adoption set

Empty, and left empty deliberately rather than backfilled to look complete. The only company-adoption-shaped signals in this log — comparison and migration, 138 combined searches — are the two clusters legal blocks. The team's best evidence source for this set (sales/solution-engineer question lists, per this skill's own sourcing table) hasn't been pulled. Two honest paths forward, neither fabricated into a ranked row:

1. Pull sales/SE question logs next cycle — that's where legal-safe company-adoption demand (limits, data residency, SLA, self-hosting) tends to surface, and none of those need a competitor's name.
2. If the switching/comparison demand needs to be served at all under the current legal rule, the only shape that survives is vendor-neutral: e.g., a "moving your analytics stack to Fernweh" page that describes the steps and data mapping without naming the tool being replaced, or a "how Fernweh differs" page that states Fernweh's own behavior without a claim about anyone else's. Both are weaker at capturing the literal "vs Amplitude" / "migrate from Mixpanel" searches, and both are speculative — nothing here confirms either would rank or convert. Flagging as an option, not adding it as a ranked row.

## Fix first

Not assessed. This run has no inventory of Fernweh's existing docs pages, so step 2 (screen what you already own) and any cannibalization check couldn't run. Assume net-new for both P1 clusters until that inventory is checked — run this screening as soon as Search Console access lands.

## Do not target

| Cluster | Reason |
|---|---|
| fernweh vs Amplitude (61/90d) | Legal: names a vendor, door closed regardless of evidence strength. |
| fernweh migrate from Mixpanel (77/90d) | Legal: names a vendor. Independently, migration is a standing-maintenance family this team's 2-pages/quarter, zero-upkeep budget can't sustain — deleted, not parked. |
| fernweh segment integration (140/90d) | Legal: names a vendor ("Segment"). Independently, integration guides need an ongoing watch on the partner's own changes, which this budget doesn't cover. |
| fernweh snowflake export (98/90d) | Legal: names a vendor ("Snowflake"). Same capacity problem as above. |

None of these are refused for the skill's three standard reasons (can't answer honestly / real fix is a product change / owned by upstream docs) — they're refused on the two constraints named in the brief. Naming the constraint here, not just the verdict, is what lets someone revisit this list correctly if either constraint changes later.

## Backlog

- **What is product analytics** (45 docs searches / 90d, User-provided) — parked 2026-09-20. Weakest family on both efficiency and value (Concept sits last on this skill's own ordering), and this quarter's 2-page capacity is already spent on the two P1 clusters above. It's also the hardest of the three to win outright: this is a broad category term that established product-analytics vendors' own explainer content almost certainly already holds, and unlike the P1 pair, winning it has nothing to do with owning the product. Worth noting: this query is coming from *inside the docs search log*, not a general web search — that's a signal of visitors landing on technical docs without category context, which argues for a short, cheap "Concepts" page over a competitive blog push, if and when a page-slot opens up next quarter.

## Pass threshold — self-check

1. Every ranked keyword carries source, count, date and a Measured/User-provided/Estimated label. ✅
2. ≥70% of ranked clusters draw top evidence from tiers 1–4: 2/2 ranked clusters are tier 2. 100%. ✅ (Flagged above: single-tier, unverified by a second source — thin, but it clears the floor as stated.)
3. No cluster ranked on keyword-tool volume alone — tier 8 wasn't used at all. ✅
4. Every cluster has exactly one canonical target surface, no collision — Error entry vs. Reference page, distinct. ✅
5. Do-not-target list is non-empty — four entries, each with the constraint named. ✅
6. The ranked table states its sort, names the high-value clusters the ratio (and, here, hard constraints) removed with the condition that would promote each, and the company-adoption set is explicitly filled with its actual state (empty, with reasons) rather than silently inheriting the ranked order. ✅

All six hold. This map is small on purpose — 7 observed queries, 2 shippable this quarter, 4 refused, 1 backlogged — because manufacturing a longer list from axes you can't yet evidence would be the matrix-explosion failure mode this skill warns against, not thoroughness.