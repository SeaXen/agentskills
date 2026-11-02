# Ferrowind DevRel Monthly Report — September 2026

## 1. Headline numbers, corrected

**Enterprise conversations: 4 → 11 (+7 absolute)**
❌ Dropping the "175% growth" framing. Both numbers are small-N (well under the ~30-event floor where a percentage is stable), and all 11 conversations trace to one conference that landed in the same month as the 2.0 launch and the Show HN. A ratio computed on two small, confounded numbers isn't a growth rate — it's noise dressed up as a trend.

✅ Reporting instead: **+7 conversations, absolute, with source split.**

| Source | Count |
|---|---|
| Conference (in-person) | [fill in — expect most of the 11] |
| Inbound (post-launch/Show HN, not conference) | [fill in — the real signal for "does content drive conversations" independent of a paid trip] |

Log each of the 11 with date, account, and next step — at this volume the raw list *is* the report, not a rate. A qualified conversation only counts if it clears: developer or buyer who has the problem the runtime solves, can influence the purchase decision, and left with a named next step. Filter the 11 against that bar before publishing the split above — an unfiltered "11 conversations" and 11 that clear the bar are different claims.

**External PRs: 2 → 6 (+4 absolute)**
Same treatment: report the delta, not a 200% figure. "External" = contributor with no Ferrowind affiliation (employee or contractor) — fix that definition now, in writing, so next month's count is comparable. Expect a launch-month spike here too (2.0 draws drive-by contributors who won't return); don't call a trend until you have two more clean, non-launch months behind this one.

## 2. The competitor's "300 PRs/year" — response for your CEO

❌ Keeping this out of the report, and out of any comparison, for three concrete reasons:

1. **Different unit.** Their number is a trailing annual aggregate; yours is a single month. Annualizing your 6 to "72/year" and comparing it to their 300 is not a fair read of either number — you'd be comparing a launch-month spike to their steady-state average.
2. **Unverified definition.** It's self-reported on their engineering blog with no stated counting method — no confirmation it means "opened," "merged," or excludes their own contractors the way your definition will.
3. **Scale/maturity mismatch.** Two different products at two different points in their contributor lifecycle. A competitor's absolute number never tells you what normal looks like for *your* project — only your own trailing history does.

**Script for the CEO, next time it comes up:**

> "Their 300/year is self-reported with no published definition — we don't know if it's opened, merged, or how they define 'external.' We're not going to chase an unverifiable number. What we *can* commit to: a fixed, defined metric — external PRs opened vs. merged, monthly, 'external' meaning no Ferrowind affiliation — and we benchmark ourselves against our own trailing 3-month average. That's the number that tells us if we're actually building a contributor base, not just matching someone else's press release."

If the CEO needs *a* number now: your own trailing-3-month average, once you have three clean months. Not before.

## 3. Measurement framework v1 — proposed, needs your sign-off

One assumption to confirm before this is final: **funded driver = developer adoption feeding company-led enterprise sales** (a Rust edge runtime with a sales-assisted enterprise tier reads that way from the conversation-and-PR mix, but confirm — if this is funded from a marketing line instead, influenced pipeline moves from "reported" to "primary, targeted").

Goals this horizon: (1) convert developer attention into qualified enterprise conversations, (2) build a real external contributor base around the runtime.

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|---|---|---|---|---|---|---|---|
| 1 **P** | Qualified enterprise conversations | Engagement | raw list; bar = has the problem + can influence decision + named next step | conversation log | baselining (M-1: 4, M0: 11) | none yet — set at 3rd period | DevRel lead | none until trend visible |
| 2 | Active external contributors | Engagement/OSS | ≥1 merged PR, trailing 90d, no Ferrowind affiliation | forge API | baselining | none yet | OSS maintainer | none until trend visible |
| 3 | External PRs, opened vs merged | Engagement/OSS | raw count/month; external = no Ferrowind affiliation (fixed definition) | forge API | M-1: 2, M0: 6 (launch month, noted) | none yet — small-N, report raw list with dates | OSS maintainer | if 0-1 for 2 months post-launch, review contributor onboarding friction |
| 4 **P** | First-deploy success rate, 7d | Enablement | share of new signups completing a working prod deploy within 7 days | product telemetry — **not yet instrumented** | pre-condition unmet | — | Eng/DevRel | instrument the success event → hand to devrel-analytics |
| 5 | Median time to first successful deploy | Enablement | signup → success event, median | product telemetry — same pre-condition | pre-condition unmet | — | Eng/DevRel | same as above |
| 6 **P** | 30/60/90d cohort retention, conference-sourced accounts | Product impact | still active at each mark, by month cohort | product analytics + CRM tag | baselining — needs cohort tagged *before* next conference | — | DevRel lead | tag this month's 11 now, or the cohort is unrecoverable |
| 7 **P** | Influenced pipeline | Business impact | opp influenced if a contact recorded a program touch in the 180 days before stage 2; shared credit, never sourced | CRM | €0 recorded, rule new | reported, not targeted, for 2 quarters | Sales ops + DevRel lead | delete by name if CRM touch field/sales-ops cooperation doesn't materialize |
| 8 | Verbatim evidence | Qualitative | quotes/friction findings, source + date + fix shipped, confidence-tagged | manual log from the 11 conversations | 0 (new row) | fewer than 2/quarter | DevRel lead | schedule follow-up conversations |

**Attribution rule:** self-reported first touch at signup (standing instrument); tagged links per campaign for artifact comparison only, never totals; influenced pipeline per row 7's rule, 180-day lookback, shared credit with Sales/Marketing — never presented as sourced.

**Known blind spots:** rows 4-5 have no instrumented success event yet — that's an instrumentation request to `devrel-analytics`, not a metric gap to paper over. Row 7 depends on sales-ops agreeing to a CRM touch field; if that doesn't happen this quarter, it leaves the sheet by name rather than sitting at the bottom unfilled. Word-of-mouth among enterprise buyers and hallway conversations at the conference that never got logged are invisible to every method here.

**Review:** next reporting date in 30 days (rows 1, 2, 3, 8). Full framework + first real thresholds at the 3rd period (~December 2026), once rows 1-3 have enough history to tell a burst from a trend. Confirm the funded-driver assumption above before that review — it decides whether row 7 gets promoted.