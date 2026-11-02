Using **devrel-metrics** (this is a "are these numbers defensible / what belongs on the slide" question, not an instrumentation or community-health one — routing noted per the skill).

# Verdict

- **305,000 "monthly users": not defensible.** Two independent failures, either one fatal: registry downloads are request counts, not people, by the registries' own documentation — and summing three registries mixes three different counting rules into one meaningless figure.
- **240,000 docs sessions: not defensible as a board absolute.** Google Analytics never executes for most of a developer audience, so the number is wrong by a factor you cannot state. It survives as an internal trend and as a ratio denominator.
- **What the CTO is actually telling you:** a technical reader checked your definitions once and they didn't hold. That's recoverable — this reader will value a sheet with written definitions and published gaps *more* than big numbers. An exec who finds one soft number discounts the rest; one told the gaps up front reads everything else as honest.

# Autopsy, number by number

## The 305k

**Downloads are requests, not people.** npm counts every HTTP 200 tarball response — CI pipelines, mirrors, caches, fresh Docker builds, every teammate's new machine, lockfile reinstalls. npm's own docs treat under ~50/day per package as mostly automation. One developer with a three-OS CI matrix generates hundreds of "users" a month; one misconfigured pipeline generates thousands. Your 305k spans somewhere between a few thousand and ~100k humans, and nothing in the data says where.

**The sum is invalid even as a download count.** Each registry counts by its own rule: npm includes mirrors and CI; PyPI excludes known mirrors by default; crates.io has its own methodology. Adding them adds incommensurable units — the 305k is not any registry's count of anything. The failure has a name in measurement practice: *never sum two registries and call the result users.*

**"Monthly users" is also the wrong end of the funnel.** Many installers never get an API key; some API users never touch your libraries. The honest unit chain is: install requests → unique cloners → API keys created → keys making successful calls. Board numbers should come from the end of that chain, which you own — your API logs.

## The 240k

**A third-party client-side script misses most of a developer audience.** The best-circulated measurement: Plausible found 58% of a tech audience blocking Google Analytics — 82.3% on Linux, 88.3% on Firefox (August 2021, one HN/Reddit-heavy site; treat as directional). If that rate applied to you, 240k counted implies ~570k actual; under a different audience, a different number. A board figure that is wrong by an *unknown factor that varies per page and per OS* is a placeholder, not a measurement.

**Even if accurate, it's the wrong tier.** Docs sessions answer "did anyone see it" — reach. Reach is the easiest tier to inflate and never a program goal; it exists to explain a downstream movement, not to be one.

# What survives of each

- **Downloads:** three separate per-registry monthly trend lines, never summed, labeled "install requests, CI included — not users." A sustained move in one registry with no release/content cause is a real diagnostic signal (broken release, CI config change, mirror behavior).
- **GA sessions:** month-over-month trend inside GA (the block rate is roughly stable, so *deltas* mean something) and step-to-step ratios inside GA — e.g., docs sessions → API-key signup page. Both steps share the same bias, so it mostly cancels. Never compare GA absolutes against registry numbers in one funnel; different denominators, different biases.

# The replacement

## Board slide (what goes where the two numbers were)

1. **API keys created this quarter** — volume input, exactly countable.
2. **% reaching first successful call within 7 days, split per language** — your new headline. The three ecosystems stay visible (your instinct to show all three was right; summing was the wrong operation on the wrong unit).
3. **% still calling at day 30** — the retention leg that revenue follows.
4. One attribution sentence from the signup survey, labeled self-reported.
5. Optional: three per-registry download sparklines, honestly labeled.

## Measurement framework — Nordholm, draft v1

*Built without the interview the skill requires — see assumptions below. Validate section by section.*

**Driver and goals** (assumed): developer adoption of a self-serve, usage-billed geospatial API; the client libraries are the adoption surface. Owner: you (DevRel lead), reader: board + CTO, quarterly.
Goals: (1) convert installers into developers with a working first call; (2) keep them calling.

*Spine: driver-anchored (one primary per goal). Alternative: journey-stage, if the CTO's real question is "where do we lose them" — it buys drop-off visibility at the cost of the metric→budget line. Recommend driver-anchored; the goals are already board-legible. Never both — that double-counts.*
*Re-ranked ladder: quarterly board + existing API telemetry collapse the effort on enablement and product impact → both promoted to primary. Reach demoted to supporting-only.*

**Metric sheet** — 8 rows:

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|--------|------|------------|--------|----------|-----------|-------|--------------------|
| 1 **P** | First-success rate, 7d, per language | Enablement | share of new API keys making ≥1 successful authenticated API call within 7d of creation, split npm/PyPI/crates cohort | API logs | retro-compute 3 months if logs retained; else *baselining* | direction + range after baseline *(baseline)* | DevRel lead | cold-run each SDK quickstart on a clean machine per language; fix top failing step before new content ships |
| 2 **P** | 30-day retention of first-success cohort | Product impact | keys still making successful calls 30d after first success, by monthly cohort | API logs | as above | *baselining*, then below trailing band *(baseline)* | DevRel lead | interview 5 lapsed developers before proposing anything |
| 3 | SDK share of calls | Product impact | share of successful calls whose user-agent is an official library vs raw HTTP, per language | API logs (user-agent) | *baselining* | raw-HTTP share rising 2 months *(baseline)* | per-language library owner | that library's install/DX friction review — raw HTTP winning means the library is losing |
| 4 | Docs searches with no result | Engagement | count + top terms per month | docs search log | *baselining* | any top-5 term unresolved 2 months *(baseline)* | docs owner | ship a page or redirect for each top term that month |
| 5 | Docs→key-creation ratio | Engagement | GA sessions reaching key-creation ÷ GA docs sessions — ratio inside one source only | Google Analytics | retro-compute | down 2 consecutive months vs trailing band *(baseline)* | DevRel lead | audit the docs→signup path: speed, IA, link placement |
| 6 | Per-registry install requests | Engagement | three separate monthly lines, never summed, labeled "requests incl. CI, not users" | npm / PyPI / crates.io stats | 6+ months public history | reported, not targeted | DevRel lead | any ≥20% step-change in one registry with no release cause → check CI configs, mirrors, broken release |
| 7 | Self-reported first touch | Engagement | one question at key creation, stable options + free text | signup form | *baselining* | response rate <40% *(hypothesis — circulating figure, not measured)* | DevRel lead | shorten/reposition the question |
| 8 | Verbatim evidence | Qualitative | quotes + friction findings with source, date, fix shipped | manual log | 4/quarter | fewer than 2 *(baseline)* | DevRel lead | schedule two developer conversations |

*Pre-conditions: rows 1–3 need one agreed success-event definition + user-agent in logs (~1 engineering day total — hand the instrumentation spec to `devrel-analytics`, don't build it here); row 4 needs docs search; row 7 needs edit access to the key-creation form.*

**Attribution rule.** Self-reported first touch at key creation is the standing instrument — reported as "self-reported," never as attribution. Tagged links compare artifacts only, never program totals. Registry downloads and GA sessions are never attribution: a download has no person attached; a GA session has no identity. If a sales motion exists, the influenced-pipeline rule applies (180-day lookback, touch before stage 2, always the word *influenced*, shared credit, fixed for the fiscal year) — currently **deleted**, see blind spots. Rule changes are announced as restatements.

**Reporting.** Monthly operational read: rows 1–5, 7. Quarterly board read: full sheet + qualitative evidence. Annual: re-derive the sheet; assume half changes. Five-sentence summary for the CTO:

> Last quarter N developers created API keys and X% made their first successful call within a week — [best language] converts at [a]%, [worst] at [b]%, and the cold runs say [step] is where we lose them. Of those who succeed, Y% are still calling at 30 days, which is the number usage revenue follows. We know how they found us because we ask at signup; we report it as self-reported, not attribution. Registry downloads we track per registry as install requests including CI — we don't sum them or call them users. Docs traffic we read as trends and ratios inside Google Analytics, because most developers block the script.

**Known blind spots.**
- *Influenced pipeline deleted*: no CRM touch field and no sales-ops cooperation confirmed. Cost to add: a touch field, ~2 engineering days, standing quarterly cooperation. If the budget moves to a sales line, this row is promoted onto the sheet — that's the skill's rule, not a preference.
- Docs readers who never sign up: invisible, and under-counted even as traffic.
- AI assistants answering from your docs produce no session at all.
- GitHub unique cloners (your best people-adjacent download complement) expire after 14 days — snapshot monthly from day one. Registry time series last months, not years: same rule.

**Review.** Next quarterly board. Kill rule stated in the doc: any metric that hasn't changed a decision in two consecutive cycles is removed on schedule.

## Assumptions that would reshape this — the interview I owe you

1. **Driver** — assumed self-serve adoption. If the funder names sales enablement first, influenced pipeline moves from blind spots onto the sheet and row 6 drops.
2. **Sales motion** — assumed unknown/absent. Confirmed enterprise sales changes the business-impact row.
3. **API-log retention** — assumed ≥3 months (retro-computable baselines). Less, and rows 1–3 ship marked *baselining* with thresholds set next quarter.
4. **Docs search exists** — if not, row 4 becomes a `devrel-analytics` request, not a metric.

## Pass-threshold check (per the skill, reported explicitly)

- 8 metrics (≤8 ✅); six fields every row ✅; two primaries for two goals ✅
- Product-impact rows present (2, 3) ✅; no monotonic primary ✅
- So-what + ownership: named action and owner every row ✅
- Attribution rule written, methods + 180-day lookback named, "influenced" wherever credit is shared ✅
- Counter-metrics: row 2 counterweights row 1's definitional drift (fake "success" won't retain); downloads explicitly non-targeted ✅
- Every threshold tagged *(baseline)* or *(hypothesis)*; no hypothesis presented as target ✅; blind spots non-empty ✅

**100% — with the caveat that the driver assumption is unvalidated.** The two board numbers are not defensible and the CTO is right; the replacements above are numbers whose *definitions* are the answer to the follow-up question, not the vulnerability.