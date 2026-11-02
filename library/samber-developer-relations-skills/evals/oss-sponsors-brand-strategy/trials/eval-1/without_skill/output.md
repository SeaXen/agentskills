No web access was granted, so the benchmark figures below are from general knowledge of published OSPO/OSS-sponsorship surveys (Linux Foundation/TODO Group census, Tidelift, FOSS Contributor Survey) rather than a fresh pull — treat the specific numbers as directional, and verify before publishing if you want defensible citations.

---

## Short answer

$217k doesn't hold up as a single clean number. Three of the four line items mix fundamentally different things — "cost of running our own product," "money we didn't actually spend," and "salary for a full-time employee" — under one label that reads to an outside audience as "cash given away to the commons." A journalist, a competitor's DevRel team, or just a sharp comment on Hacker News will take the number apart in about five minutes, and the parts that don't hold up will make the parts that do (the $62k) look tainted by association.

## Line by line

**$90k — two engineers maintaining hollow-etl, loaded cost, on work time.**
Defensible as "investment in open source" only if hollow-etl has a real outside audience — external contributors, external issues, a license that lets others fork and use it, downstream dependents who aren't Hollowpine. If it's mainly an internal data tool that happens to carry an OSS license, this $90k is just "our ETL team's salary," and you'd be paying it whether or not the repo were public. Ask: would this cost exist, unchanged, if the repo were private tomorrow? If yes, it isn't incremental OSS investment — it's normal engineering spend wearing an OSS label. If there's real external usage, the honest framing is "we invest $90k/yr keeping a project the wider community depends on healthy," not "we invested $90k in open source" as if it were a novel outlay.

Separately: $90k loaded for two engineers for a full year is ~$45k/head. That's below a US loaded-cost floor for any level above junior, so this is very likely a *prorated* figure (e.g., each engineer spends ~25-30% of their time on hollow-etl). That's fine and arguably more honest than counting full salaries — but it needs a stated methodology, because right now the number can't be checked or defended if asked "how did you get to $90k."

**$40k — cloud credits "donated" to that same project's CI.**
You can't donate to yourself. This is Hollowpine paying for infrastructure that runs Hollowpine's own project's tests. Calling it a donation implies a gift to an external party; it's a hosting bill. Bigger question: are these credits cash Hollowpine actually spent, or free credits from a vendor's OSS/startup program that cost Hollowpine nothing? If the latter, $40k is a face-value number with zero real cost behind it — that's the single easiest line for a fact-checker to puncture. Reframe as "CI infrastructure cost for hollow-etl," and confirm it's real spend, not gifted credits, before it goes in the number.

**$25k — paid to Priya Raghunathan, maintainer of parquet-shim, hired in March as staff engineer.**
This is the most confused line in the set, because it silently switches accounting methods mid-sentence. Before March she may plausibly have been an independent maintainer receiving a stipend — that's a clean external-sponsorship dollar. After March she's a W-2 staff engineer, and a staff engineer's loaded cost is nowhere near $25k/year (more like $220-320k depending on market). So $25k is almost certainly *not* her cost to the company; it's either:
- a leftover pre-hire stipend for Jan-Feb only (in which case it's a two-month number being presented as a year figure), or
- an arbitrary slice standing in for "value of her OSS work" without a stated percentage of her time, or
- being counted the same way as the sponsorship bucket even though she's now internal, which double-counts against her actual salary (already sitting in engineering payroll, invisible in this $217k) while understating what the company is really spending to keep parquet-shim alive.

If Hollowpine hired the maintainer of a critical dependency, that's a genuinely good, on-brand story — but tell it honestly: "we hired parquet-shim's maintainer and dedicate X% of her time to it, worth ~$Yk," using the *same* loaded-cost-times-percentage method as the hollow-etl line. Don't let a stipend-era number survive past the point where it stopped being true.

**$62k — actual sponsorships to outside maintainers.**
This is the only line that's unambiguous. Real cash, to people who don't work for Hollowpine, for projects Hollowpine doesn't own. This is the number a reader can trust without a footnote.

## What I'd actually publish

Two options, both more defensible than $217k:

1. **Report $62k as the headline "external open source giving" number**, and separately disclose "$Xk in engineering time dedicated to open source maintenance (own + third-party)" as a second, clearly-labeled figure. Two honest numbers beat one number that can't survive a follow-up question.
2. **If the CFO wants one blended figure**, rebuild it with consistent methodology: (a) confirm hollow-etl has genuine external users before counting its cost at all; (b) replace "donated credits" with actual infra spend, not face value of free credits; (c) recompute Priya's line as (her % time on parquet-shim) × (her loaded cost), not a flat leftover figure; (d) keep the $62k as-is. Whatever that recomputed total is, label it precisely — "engineering time and cash directed toward open source" — not "invested in open source," which implies all of it is a gift to others.

## How it compares to other companies

Rough, well-known reference points (verify current figures before citing publicly — I don't have live search access this session):

- OSPO surveys (Linux Foundation/TODO Group) have repeatedly found most companies with a formal OSS program dedicate somewhere in the range of **0.5-2% of engineering headcount or budget** to OSS work (maintenance of owned projects + upstream contribution + sponsorship), with wide variance and a long tail of companies reporting effectively $0 in direct sponsorship.
- Direct cash sponsorship to outside maintainers specifically (the category your $62k sits in) is the rarer and smaller of the two — companies known for it publicly (Sentry, Vercel, Netlify, Bloomberg's OSPO) tend to disclose stipends in the low-tens-of-thousands per maintainer per year, and most companies of Hollowpine's size disclose nothing at all in this category.
- At 140 engineers, a rough engineering budget (loaded cost ~$180-220k/head) is on the order of $25-30M/year. $217k against that is ~0.7-0.9% — in the middle of the typical OSPO range. Even the defensible subset (~$62k sponsorship + a properly-computed maintenance figure) likely still lands in a respectable, comparable band — you don't need the inflated number to look good next to peers.

The practical implication: you don't need $217k to be competitive. A correctly-scoped, methodology-disclosed number in the $100-150k range (real sponsorship + honestly-computed maintenance time, minus the donated-to-self credits and the stipend-era artifact) will likely still sit at or above what most companies your size report, and it will survive scrutiny — which $217k, as currently built, will not.