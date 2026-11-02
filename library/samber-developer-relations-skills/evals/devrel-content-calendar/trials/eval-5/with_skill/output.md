# Q4 plan review — Loomstack

**Verdict: buckets right, timeline wrong. Fix 4 breaks + 5 missing fields before sending round.**

What survives ✅
- Three buckets (awareness, tutorials, migration/scaling) = correct pillar mix.
- Blog-first reach = correct for search-driven dev discovery.
- Serving converted users with depth = correct instinct.

## Breaks, damage order

⚠️ **1. Buyer gets zero slots.**
Your own context: devs search, platform leads sign. Plan spends 3 months on person who cannot sign. "Developers evaluate, someone else buys" = sales-enablement driver. That driver weights security posture, licence, release cadence, migration cost, support path, proof points. None slotted. Skill rule: one blended piece answers neither audience — give each audience own slots, label them.

⚠️ **2. Funnel used as timeline.**
Each month = one journey stage. Search arrivals hit wrong-stage month every week. Readers enter at any depth ("playground mindset", Ashley Faus — skill reference); journey labels = coverage check, not reader path. Cohort math worse: platform deal cycle outlasts quarter. "Converted in month 2" cohort ≈ empty by month 3. Real migration readers arrive next quarter.

⚠️ **3. One surface.**
Fails coverage floor: min 3 surfaces, 2 stages. Routing table: "how do I do X" → tutorial (docs), error string → troubleshooting page, approver comparison → evaluation page, not blog post. Skill calls blog-only "adoption blocked in docs nobody planned". Traffic argument circular: traffic follows content. Evaluator's highest-intent queries ("loomstack migrate", exact error strings) resolve to docs. Keep one canonical URL per topic — blog announces, docs holds, cross-link.

⚠️ **4. December placement.**
Nobody starts fleet migration mid-December: holidays, freeze. December = platform leads write 2027 plans. Proof points + eval material belong there. Plan late-Dec light.

⚠️ **5. Acceptance fields absent.**
No owner per slot, no named reviewer, no slack, no announcement cap, no evidence per topic (tickets, community repeats, docs searches returning nothing). Reviewer passes bind dev content plans — count passes before promising output. Until these exist, plan = wish list.

## Smallest change set

1. Convert month phases into mix ratios, run every stage every month.
2. Add approver track: 2–3 slots, Nov–Dec, ship as evaluation page on docs. Titles: security posture + release cadence; migration effort/cost guide; benchmark or case study; one forwardable one-pager devs send their lead. Note: benchmarks + migration guides fail late — budget engineering review passes.
3. Reroute: tutorials + migration guides → docs. Blog keeps awareness, engineering stories, announcements. Newsletter or community digest = third surface if exists.
4. Anchor migration content to release date, not calendar month.
5. Add per slot before sending: owner, named reviewer, evidence or hypothesis, 20% named slack, announcement cap (propose 2).

## Proposed ratios (slots, not hours)

| Axis | Proposal |
| --- | --- |
| Stage | discover 35 / try 30 / adopt 35 |
| Audience | individual dev 55 / platform lead 35 / both 10 |
| Surface | blog 45 / docs 40 / newsletter + community 15 |
| Shelf life | evergreen 65 / timely 35 |

Proposals, not law. Replace with your real numbers.

Monthly pattern, repeat 3×:
1. One awareness blog post, search-targeted, evergreen problem content.
2. One tutorial on docs.
3. One adopt/proof piece — alternate migration deep-dive and approver eval.
4. One light slot — digest, Q&A write-up, changelog.

## Metrics

Judge quarter on publish rate (target ≥80%), mix drift, activation. Not closed contracts — deal cycle longer than quarter, month-3 conversion read = false failure.

## Open questions

1. Q4 anchors: releases, launches, accepted talks (conference season lands Nov–Dec)? Anchors gate slot layout.
2. Capacity: writers available, reviewer passes per week?
3. Last quarter: what shipped, performed, slipped?
4. Off-limits: named competitors? embargoed customers?

Next: answer question 1. Re-slot takes about 1 hour once anchors + capacity known.

Separately: my project memory says Loomstack = LLM eval harness; you now say data pipeline runtime. Pivot or stale memory? Say which — I update memory on your answer.