# Ashcombe — cohort retention slide, CMO budget defense

Tier: **Product impact** (cohort retention, 30/60/90-day family). Reader: CMO, headcount decision. Effort ceiling: zero engineering days. This shapes every choice below — the retroactive tagging plan you already have is the right instinct, but it needs one specific reframe before it goes on a slide in front of someone who signs the check.

## The reframe that makes this honest

You said two things that look like separate problems but are actually the same fix:

- "We've never recorded a pre-period for anything."
- "I can tag the cohort retroactively from event attendee lists."

A pre-period answers "were these same developers different before we touched them?" You don't have that, and you can't manufacture it retroactively — there's no time machine for baseline data that was never captured.

But you don't need it. Cohort retention doesn't have to be a before/after claim. It can be a **concurrent comparison**: touched developers vs. all developers, in the same quarter, measured the same way. That's not "our work improved retention" (a causal claim you cannot make with this data) — it's "developers we engaged directly retain at a different rate than the base population, in the same window." That claim only needs two things you already have: who was touched (attendee lists) and who was active when (whatever system already logs product usage — dashboard logins, API calls, CLI invocations, whatever your product already tracks without new instrumentation).

This also quietly solves your baseline problem. You don't need to wait three quarters going forward — you already have three quarters going backward. Reconstruct three already-elapsed cohorts now and you walk into the room with a trend on day one, not a "baselining" placeholder.

**One gating fact, check it before building anything else:** this only works if some system *already* logs developer activity — for touched and untouched developers alike — across the last three quarters, and someone can query it without engineering time (a support/product/sales-ops export counts; a new event does not). If that data doesn't exist anywhere already, this metric cannot ship for this deadline. Don't discover that in week 4 — confirm it in week 1, and if it's not there, skip to the fallback at the bottom.

## The slide

**Title:** Developers We Engage Directly Retain Differently Than the Base Population

**Chart — cohort-retention table, three touched cohorts against the same-quarter base:**

| Cohort (event-tagged) | At touch | +1 quarter | +2 quarters | +3 quarters |
|---|---|---|---|---|
| Q[n-2] touched (N=__) | 100% | __% | __% | __% |
| Q[n-1] touched (N=__) | 100% | __% | __% | — |
| Q[n] touched (N=__) | 100% | __% | — | — |
| **All developers, same quarters (baseline)** | 100% | __% | __% | __% |

"Active" = [pick the one existing, already-logged signal closest to "still using the product" — e.g., authenticated API call, dashboard login, CLI invocation. Use whatever definition your product team already uses elsewhere; do not invent a new one, that's an engineering ask.]

**One-line callout under the chart (fill in once computed):** "Developers we engaged directly at events retained at [X]%, [Y] points above the all-developer base, at [Z] quarters out."

**Mandatory footnote, small type, always visible:**
> ℹ️ First read of this metric — baselining, no target set. Comparison is against the concurrent all-developer base, not this group's own past behavior (no pre-period exists). Cohort = event attendees only; other touches (docs, social, community) not yet tagged. Event attendance is self-selected — developers who show up are already more engaged, so some gap is expected independent of any DevRel effect. Method: retrospective cohort-vs-baseline comparison, not a designed holdout — directional, not causal.

That footnote is doing real work. Say it once, out loud, before anyone in the room finds it themselves. An exec who spots an unstated gap discounts everything else on the slide; one you told up front reads the rest as honest.

## The metric's six fields, for your own sheet

| Field | Content |
|---|---|
| Definition | Share of the event-tagged cohort from quarter *Q* still recording an active-use event *N* quarters later, versus the same rate for all developers active in *Q* |
| Source | Event attendee lists (3 quarters, exported) joined to [existing activity log] on email/account ID |
| Baseline | The 3-quarter trend itself, reconstructed retroactively — this *is* your baseline |
| Threshold | None this cycle. Set a direction-and-range threshold at next review once this read exists (`hypothesis` until then) |
| Owner | You (or whoever owns the DevRel-to-CMO relationship) |
| Action | If the gap holds across ≥2 of 3 quarters: headcount ask = fund more of the touch type that correlates with the gap. If the gap is flat or shrinking: do not use this metric to argue headcount this cycle — lead with qualitative evidence instead, and say so |

Tag every number on the slide `baseline` (self-set, from your own history) — nothing here is `sourced` from outside, and nothing should be presented as an industry number.

## Small-N handling

Event-attendee cohorts at one company, per quarter, are plausibly under 30 people. Check each quarter's N before you compute a percentage. Below ~30, report the raw count ("11 of 15 Q1 attendees still active at 3 quarters") instead of a rate — a percentage on 15 people swings by 7 points per person and will not survive a follow-up question.

Don't blend the three cohorts into one average — they're different sizes and different ages since touch. Show the triangle, not a blended number.

## Five weeks, zero engineering days

1. **Week 1:** Confirm the gating fact — does an existing, queryable activity log cover touched and untouched developers for all three quarters? Pull the three event attendee lists.
2. **Week 2:** Get the activity-log export from whoever owns it (support/product/sales-ops — a data pull, not an engineering ticket). Join on email in a spreadsheet or BI tool you already have access to.
3. **Week 3:** Build the triangle. Compute the all-developer baseline for the same quarters. Flag any cohort under N≈30.
4. **Week 4:** Draft the slide and footnote above. Pressure-test it — have someone skeptical ask "how do you know this isn't just that engaged people show up to events?" and confirm your answer is the selection-bias line, not a dodge.
5. **Week 5:** Buffer. Rehearse the one-sentence summary below.

## The sentence the CMO can repeat without you in the room

"Developers we engage directly at events retain at a noticeably different rate than the base population, three quarters running — we can't yet call that causal, since engaged people self-select into events, but it's the first real signal this program has produced, and it tells us where to double down."

## Don't ship this alone

One metric on a headcount-defense slide reads as cherry-picked, whatever it shows. Pair it with one zero-effort companion you already have without any new work — the count of developers routed to another team (sales, product feedback, recruiting) from program touches, or a simple existing engagement number with a named downstream fix attached. Keep it to one supporting line; this isn't the moment to build the full sheet, just don't let retention stand completely alone.

## If the gating fact fails

If no existing system already logs developer activity for both touched and untouched developers, stop — this metric cannot exist by week five with zero engineering days, retroactive tagging or not. Say that explicitly in the room rather than presenting a number you built on a guess: "We identified this as our best product-impact metric, and confirmed we cannot build it without engineering time. Here's what it would take [name it], and here's what we're bringing instead this cycle." That is more credible in front of a CMO than a retention number nobody can defend under one follow-up question.