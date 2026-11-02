# Quarrystone Pricing Reset — Research Plan

**Window:** Wed 2026-09-23 → Tue 2026-12-15 (12 weeks, leaving a 1-week buffer inside the 3-month deadline for sign-off).
**Scope:** this plan covers research through a decided price. Step 6's cohort announcement and migration (see the guardrail table's last row) is a separate, sequenced follow-on — don't compress it into these 12 weeks.

## Why the budgeted plan needs reordering, not cancelling

Two problems, both fixable without losing the money already committed.

**Problem 1 — the strongest evidence you have isn't in the plan.** Research methods rank, by evidence strength: *own usage-value correlation and win/loss data > Gabor-Granger > Van Westendorp > competitor prices* (self-set ranking, this skill's method). By cost/effort, the same data is also the cheapest: reading instrumentation you already collect costs a day; a fielded panel costs weeks and a respondent budget. Quarrystone has two years of usage telemetry on 90 real paying accounts and complete churn records — the single highest-evidence, lowest-cost source available to any company — and the current plan spends its entire budget on the two weakest-to-medium sources (a stated-preference survey and a competitor page scrape) while never touching it. That's backwards on both axes at once.

**Problem 2 — the panel is undersized for what it's being asked to do.** Van Westendorp needs roughly 100+ respondents per segment to produce a usable acceptable-range curve. 300 people across 4 segments is 75/segment on average — under that floor before any screening drop-off, non-response, or low-quality-response filtering, which typically costs another 10-20%. Field it as specified and at least one segment's curve will be too noisy to act on. Fix this before fielding, not after: either grow the panel to ~450 (110-120/segment with headroom) or collapse to 3 segments and hold 300. Flag this to whoever owns the panel budget this week — it's a two-line email now, a wasted field wave in week 8.

Everything below sequences around those two fixes: own data first (it's fast and it tells you *what* to ask the panel), then the panel, with competitor data running in parallel throughout as a bound, never a target.

## Workstream 1 — Own data (Weeks 1-3)

This is the workstream that was missing. It runs first because its output — candidate value-metric architectures — determines what the Van Westendorp/Gabor-Granger instrument even asks about. Fielding a price survey before this step means guessing the unit.

**1a. Floor.** Take each usage-instrumentation field you already log (data ingested/day, GB retained, queries run, retention window, seats/active users, alert rules, dashboards viewed) and price its full marginal cost: compute, storage, egress, third-party spend, support hours at that volume. Model the **90th-percentile account**, not the average — log-search is typically consumption-heavy, and usage-only SaaS pricing runs a 62% median gross margin against an 80% software median (sourced: Aleph x Benchmarkit 2026, 342 companies) because infrastructure sits directly in COGS. If Quarrystone's ingestion/storage costs scale with data volume, budget for that gap now rather than discovering it at the first cost review. Add the free-tier's total marginal cost as a line item if Quarrystone has one.

**1b. Ceiling.** Log-search has real self-host alternatives (Elasticsearch/OpenSearch, Loki, ClickHouse-based stacks). Price the lowest of: self-hosting one of those (infra + operator time + upgrade risk + on-call, in the customer's terms), building a minimal equivalent, the cheapest comparable vendor from Workstream 2, or doing nothing. Whichever is lowest is the number your buyers actually reason with — not your own cost-plus math.

**1c. Usage-value correlation.** For each candidate metric above, regress it against retention and expansion across the 90 accounts' two-year history. You're looking for the threshold where the product becomes "load-bearing" — the usage level past which an account essentially never churns. This tells you which unit tracks value, not just cost, and is the evidence a competitor price scrape can never produce.

**1d. Churn and win/loss.** Pull every logged churn reason and bucket it (price, missing feature, support, product-market fit, acquired/shut down). Where the reason isn't already captured, run short structured interviews with the last 2 quarters of churned and lost-deal accounts — the goal is the actual alternative they named (self-hosted stack, a named competitor, internal build, nothing), not a satisfaction score. Aim for 15-20 interviews; this is the only source in the whole plan that captures real objections rather than stated preference.

**Output by end of Week 3:** the floor, the ceiling, and 2-3 candidate value-metric architectures (unit, sample bill, what it gives up), each scored against the five tests (moves with value, already counted, forecastable, non-gameable, cost-correlated) and flagged for the seat-collapse pattern if seats are a candidate — flat seat count against rising ingested-data volume is the tell, and it's common in log-search tools used mostly by machines/CI with a small human dashboard surface.

## Workstream 2 — Competitor scrape (Weeks 1-4, intern, runs in parallel)

Keep the intern working — this is legitimately cheap (trivial cost per the method table) and useful, just scope its role correctly: **a ceiling bound, never a justification for a number.** Reading a competitor's page is evidence of what someone else guessed, and ranks last on evidence strength.

Give the intern a fixed schema per competitor, not just "the price": published price per unit, the unit itself (per-GB, per-seat, per-host, hybrid), free-tier limits, annual discount %, what's gated at which tier, and whether a self-hosted/open-source edition exists. That schema is what turns a spreadsheet of 7 numbers into an actual ceiling input for step 1b, and into the packaging-ladder gate comparison later. Flag anything "contact sales" at an entry tier as a data gap, not a number — it tells you that vendor's self-serve motion failed, not what they charge.

**Output by end of Week 4:** a 7-row comparison table (unit, price, free limit, gates, self-host availability), dated.

## Decision gate — pick the metric(s) to test (end of Week 3/4)

Before writing a single survey question, get sign-off on 1-2 candidate value-metric architectures from Workstream 1c/1d. Van Westendorp and Gabor-Granger only produce a usable number when respondents are pricing a concrete unit ("$X per GB ingested per month," not "what would you pay for Quarrystone"). This is the step that makes the panel spend worth fielding at all — skip it and the survey tests an abstraction nobody can price.

## Workstream 3 — Van Westendorp + Gabor-Granger panel (Weeks 4-9)

**Fix the sample size first** (see Problem 2 above) — resolve panel size vs. segment count this week, before instrument design, since it changes recruitment lead time.

**Segment design and the anchoring trap.** With only 90 paying accounts, a 300-450 person panel is necessarily mostly non-customers — trial users, free-tier users, churned accounts, and cold prospects matching the ICP. That's fine, but keep current paying customers as a *separate analysis lens*, not blended into the general pool: their answers anchor on the price they already pay and will systematically compress the acceptable range. If "four segments" currently means buyer type (individual / team / platform-team / enterprise-procurement) rather than customer-status, add customer-vs-prospect as a cross-cut in the analysis, not a fifth fielding segment.

**Instrument.** Four Van Westendorp questions (too cheap / cheap-good value / expensive / too expensive-stop considering) plus a Gabor-Granger ladder ("would you buy at $X"), both phrased against the concrete unit(s) chosen at the decision gate, with a realistic usage scenario per segment (e.g., "your team ingests ~50GB/day"). Gabor-Granger outranks Van Westendorp on evidence strength for near-zero extra fielding cost once the panel is already recruited — add it rather than choosing one over the other. Pretest on 10-15 respondents before full fielding to catch confusing scenario framing.

**Field weeks 6-7. Analyze weeks 8-9:** Van Westendorp's acceptable range and optimal price point per segment, Gabor-Granger's demand curve per segment, both cross-checked against the Workstream 1 floor and Workstream 2 ceiling. If the panel's range sits *below* the floor computed in 1a, that's a cost-structure or metric problem, not a signal to price low — say so rather than splitting the difference.

## Synthesis and memo (Weeks 9-12)

Write the pricing memo (value metric → ladder → free limits → price points → mechanics → predictability → change plan → measurement) one section at a time, sign-off before moving to the next — a wrong metric at section 2 is cheap to catch there and expensive to catch at section 9. Price points get placed using all four sources in this priority order: own usage-value correlation and win/loss data first, competitor bounds second for sanity-checking (not the reverse), Gabor-Granger third, Van Westendorp range fourth as the widest, weakest bound. Label every number sourced or self-set when it goes in the memo — a self-set baseline repeated without that label becomes a fake benchmark the moment someone quotes it in a board deck.

## Guardrails — what each source may and may not decide

| Source | Use it to | Never use it to |
|---|---|---|
| Usage-value correlation (own data) | Choose the value metric; find the load-bearing threshold | — |
| Churn/win-loss interviews | Confirm real objections and named alternatives | Stand in for a sample size you don't have (15-20 is directional, not statistical) |
| Competitor scrape | Bound the ceiling; check gate placement | Justify a chosen number — it's someone else's guess |
| Gabor-Granger | Build a demand curve at the chosen unit | Override what your own margin floor requires |
| Van Westendorp | Set an acceptable range per segment | Set the final number alone — it's the weakest-evidence, widest-range method in this set |

## Pass thresholds before the memo ships

- A target customer can estimate their monthly bill from public materials in under two minutes, within ±20% of the real invoice — test on 3 real usage profiles pulled from the 90 accounts (self-set baseline).
- Margin at the proposed price clears your target at the 90th-percentile account, not the average.
- Every rung below enterprise has a written trigger event and a public price.
- The change plan (Step 6, scheduled to start after Week 12) names every cohort — existing paying, free/trial, self-hosted, under-contract — with a grandfathering decision and no reversed public commitment.
- Track from launch: free-to-paid conversion by cohort (developer-tool median is ~5%, roughly half the non-developer median — sourced, Lenny's Newsletter), net revenue retention (~100% good / ~120% great for bottom-up motions), and billing-support ticket volume as the cleanest proxy for whether the new pricing is actually predictable.

## After Week 12

The research plan ends in a decided memo, not a shipped price change. Step 6's rollout — cohort-by-cohort announcement, grandfathering window, migration FAQ — needs its own notice period, longer for any accounts on annual terms, and should be scheduled as a distinct phase after sign-off rather than folded into this window.