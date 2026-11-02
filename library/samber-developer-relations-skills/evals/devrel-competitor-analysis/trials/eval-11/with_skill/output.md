# DevRel benchmark: Ours vs Beacontree, Larkspur

Peer set: Beacontree, Larkspur (as given — 2 peers, below this skill's own 3-5 convention; see *Method and limits*). Findings below are the 8 gaps supplied, not an independent re-collection — no source URL/date is attached per cell, so treat this as a **gap-plan pass**, not a fresh full benchmark.

## Top 3 quick wins for the quarter 🎯

| # | Gap | Move | Owner | Target |
|---|---|---|---|---|
| 1 | Credit card required before first API key | Issue a free sandbox key, no card; gate billing behind usage, not signup | DX/Platform lead | 2026-10-15 |
| 2 | SDK quickstarts for 1 of 4 languages | Port the existing quickstart pattern to the other 3 — content adaptation, not new engineering | DX lead + Docs | 2026-11-30 |
| 3 | No public changelog feed | Expose the existing release notes as a changelog page with an RSS/Atom feed | Docs | 2026-10-31 |

These three share the same profile: high or clearly positive impact on a developer's first hour, and low cost because each reuses something that already exists (a billing flag, a quickstart template, a release process) rather than building something new. Docs-mode coverage (row below) scores a higher impact-per-cost ratio than the changelog, but it is a multi-quarter lift, not a quarter-sized one — see the note under the gap plan.

## Gap plan

Sorted by impact per unit of cost, highest first — not by impact alone and not cheapest first.

| Gap | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|
| Credit card required before first API key | high | low | **close** — free sandbox key, no card | DX/Platform lead | 2026-10-15 |
| SDK quickstarts cover 1 of 4 languages vs full coverage at both peers | high | low | **close** — port the existing quickstart to the remaining 3 | DX lead + Docs | 2026-11-30 |
| Docs are reference-only, no how-to or explanation pages | high | medium | **close, phased** — how-to + explanation for the top 5 highest-traffic features this quarter; full coverage is a Q1 2027 initiative, not a quarter-sized task | Docs lead | phase 1: 2026-12-15 |
| No public changelog feed | medium | low | **close** — publish with a feed off the existing release process | Docs | 2026-10-31 |
| No migration guide practice | medium | medium | **close** — start with the next major version, not retroactively | Eng + Docs | next major release |
| 3% of merged PRs from outside the company vs 31% at Larkspur | medium | high | **close, starved** — start the cheap parts now (good-first-issue labels, a contributing guide, a response-time SLA on issues); full parity is a contributor-onboarding program, not a task, and depends on whether the company wants to lean OSS-first at all | Eng/OSS lead | cheap parts by 2026-11-15; full-scope review 2027-01 |
| No community venue, 900 monthly active devs | medium | high | **ignore this quarter** — 900 MAU is below the point where a venue reads as active rather than empty (this analysis sets 2,000 MAU as its own revisit threshold, not an industry figure); substitute this quarter with visible answers on the public Q&A tag developers already use for us, plus tightening issue response time — same peer-community signal, task-sized cost | DevRel lead | substitute by 2026-11-30; venue review 2027-Q1 |
| 1 conference sponsored vs 14 at Beacontree | low | high | **counter** — Beacontree's sponsorship count buys distribution we don't have; matching it is not a plan. Counter with 2-3 CFP speaking slots at higher-fit events instead of sponsor spend | DevRel lead | CFP submissions by 2026-11-30 |

**Starved by the ranking:** the 31%-outside-contribution gap and the no-community-venue gap are both real evidence to a sophisticated evaluator, and both cost a program rather than a task, so the ratio sort pushes them down every quarter. Name what promotes each: outside contribution moves up if the company commits to an OSS-first motion or a lost evaluator names it as the reason; the community venue moves up once MAU clears the 2,000 threshold or an off-platform proxy (unprompted questions on a public Q&A tag) shows organic demand already forming.

## Method and limits

- This is a gap-plan pass over 8 findings already collected elsewhere, not a fresh signal-collection run — no source URL or observation date accompanies each cell, so traceability is below this skill's own 100% target. Re-verify each row before it goes into a board or budget document.
- Peer set is Beacontree and Larkspur only — 2, not the 3-5 this skill defaults to. A two-peer set risks inheriting both peers' shared blind spots; if a category leader or a demand-side alternative (e.g., "build it yourself against the raw API") sits outside this pair, add it before using this for a budget case.
- No timed quickstart, docs-mode inventory, Q&A tag data, or hiring signals were supplied — those rows are left out rather than filled with an estimate, per this skill's rule against blank-cell fabrication.
- Individual-developer vs. organization-buyer lane wasn't specified. Rows 1-4 (card wall, SDK quickstarts, docs modes, changelog) read as individual-adopter evidence; rows 5 and 6 (migration guides, outside contribution) double as organization-buyer evidence. If the buyer lane is the priority, migration-guide practice should be pulled forward ahead of the changelog feed.
- The 2,000 MAU community-revisit threshold and the "top 5 pages" docs-phase-1 scope are this analysis's own conventions, not industry benchmarks — move either if there's a specific reason to.
- What would change these verdicts: a lost evaluator naming the outside-contribution gap or the missing community venue as the reason they picked a peer would promote both out of "ignore/starved" immediately.