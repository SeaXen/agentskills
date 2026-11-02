Assumed answers (no live interview — you asked for the deliverable straight away). Flag anything wrong, dashboard adjusts fast:

- Venue: Discord only, no forge/repo tied to it — chat-only community.
- Adoption: individual/community-scale, not per-account B2B. **Unconfirmed — matters for the numbers, see Gap below.**
- Primary outcome (SPACES): not named yet. **Biggest gap — see below.**
- Stage: one person (you) running it part-time, no dedicated headcount.
- Owner of dashboard: you.
- Hard date: board deck in 14 days.
- Effort ceiling: one-off deliverable now, standing monthly cadence after.

## Route

Community is 35 days old. `developer-community-health`'s own rule: no health baseline before day 90. Straight answer is "not now, ask again on day 90."

Board doesn't wait for day 90. So this dashboard borrows `developer-community-launch`'s day-30/day-90 leading-indicator framework (built for exactly this stage) and presents it in `developer-community-health`'s report shape (what a board deck expects). Every number below is marked **baselining** — first real trend line exists after 3 monthly reads (~day 120), not this deck.

**Gap, real one:** primary outcome was never named. Support, product feedback, acquisition, contribution, engagement, success — pick one before the next review or every metric below stays generic. Put it on the VP's desk as a question, not yours to guess.

## Do this today (before anything else)

Discord doesn't retain history far back on the free tier, and the last 5 weeks likely aren't recoverable in clean form. Backfill is probably impossible — starting the log late costs you the whole first month's data, permanently.

1. Server Settings → Enable Community (if not already) → turn on Server Insights.
2. Flag every staff/employee account (you + any other Norbury person in the server) in a small list — needed for every metric below.
3. Start a weekly manual tally today: messages per channel, who answered what, new-joiner posts. 15 min/week.

## Metric sheet — Norbury Systems Discord

| Metric | Pillar | Formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Active participants / week | Activity | distinct non-bot posters, 7-day window | manual tally + Server Insights | baselining (day 1: today) | none yet — read 3 weeks before setting one | You | — |
| Non-staff share of messages | Activity | non-staff msgs ÷ total msgs, weekly | manual tally, staff-flagged | baselining. Today's known point: 3/day are yours alone, out of ~20/day total = ~15% from you personally | Pass >50%, warn 30–50%, fail <30% (adapted practitioner baseline, self-set cutoffs — not CHAOSS-published) | You | If team messages dominate, go quiet for a week and let members answer first |
| Top-5 members' share of activity | Activity / concentration | top 5 posters' msgs ÷ total msgs | manual tally | baselining | Pass <50%, warn 50–80%, fail >80% (same adapted source) | You | If it fails, community is 3–5 people, not 118 — reframe the board story accordingly |
| Questions answered within 24h | Responsiveness | question msgs w/ human reply <24h ÷ total questions, bots excluded | manual tally | baselining | Pass >90%, warn 75–90%, fail <75% (adapted, self-set) | You | Reply queue check every evening |
| New members posting within 7 days of joining | Contributor funnel | joiners who post once in first week ÷ joiners that week | manual join-log vs first-post timestamp | baselining — needs the log started today, cohort readable in ~7 days | Pass >40%, warn 20–40%, fail <20% (adapted, self-set) | You | Review welcome message / first-touch flow |
| Recommendability | Sentiment | "Would you recommend this community?" Likert, NPS-style | pulse survey | not run — too early, one month of chat data can't carry a real survey yet. First pulse: day 90 | n/a until first read | You | — |

At most 8 metrics allowed by design, one per pillar minimum — this sheet has 6, covers all four (Activity, Responsiveness, Funnel, Sentiment).

## What the board deck should actually say

Say this, not a growth story:

> 118 members, week 5. Too early for a verdict — health baselines need 90 days by design (Nielsen 90-9-1, CHAOSS starter model). Instrumentation is live as of [today's date]. First real trend line: [date, ~3 months out]. Leading indicators tracked now: [table above, minus the two baselining columns].

Day-90 pass table above is a **starting hypothesis** adapted from published community-management baselines, not an industry standard — say so if asked, don't defend a number nobody chose on purpose.

## Do NOT put in the deck

These are the exact failure modes that make a community dashboard look confident and be worthless:

- Total member count as a headline — only ever goes up, says nothing.
- Raw message count with no baseline — 140 messages/week means nothing without a "compared to what."
- Auto-sentiment score on Discord chat — scores blunt bug reports as angry, jokes as hostile. Skip it; you have no survey yet, don't fake one.
- Per-member leaderboard — privacy exposure, and rewards volume over value.
- "Engagement rate" as an undefined percentage — if nobody can recompute it, it's not a metric.

## Next 14 days

1. Today: enable Server Insights, flag staff accounts, start the weekly tally (15 min).
2. Get the VP to name the one SPACES outcome (Support / Product / Acquisition / Contribution / Engagement / Success) — blocks every threshold above from staying generic.
3. Days 2–13: log weekly, no ratio talk yet — you're building the baseline, not reading it.
4. Day 14: present the sheet above as "instrumentation + leading indicators," dated, no verdict.
5. Day 90: real health read against 3 periods of trailing data — that's when `developer-community-health`'s full framework applies.

Next concrete action: enable Server Insights and start the staff-flag list — 10 minutes, do it now.