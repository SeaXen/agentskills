# Slide: Developer Cohort Re-Engagement

**Title:** *Developers We've Touched Keep Coming Back*
**Subtitle:** *First re-engagement baseline — three touchpoint cohorts, tracked through Q3 2026*

## The visual — cohort triangle, not a single %

Use the classic cohort-retention table. One row per quarter a developer *first* showed up in an event/attendee list; one column per later quarter they showed up again in *any* event/attendee list. Never collapse this into one blended number — cohorts have different amounts of follow-up time and averaging them hides that.

| First touched in | Cohort size (N) | Re-engaged Q1 2026 | Re-engaged Q2 2026 | Re-engaged Q3 2026 |
|---|---|---|---|---|
| Q4 2025 | N₁ | a / N₁ (__%) | b / N₁ (__%) | c / N₁ (__%) |
| Q1 2026 | N₂ | — | d / N₂ (__%) | e / N₂ (__%) |
| Q2 2026 | N₃ | — | — | f / N₃ (__%) |

Fill every cell as **raw count / N (%)** — never a bare percentage. With attendee-list cohorts this small, "36%" and "23/64" read very differently to a CMO deciding headcount, and showing the fraction pre-empts the "is that even a real sample?" question before it's asked.

Wait for Q3 2026 to close (Sep 30 — a week out) before pulling the final numbers, so all three cohorts get their most recent data point instead of presenting Q2's row one quarter short.

## Definitions box (small print, bottom of slide)

- **Touched** = appeared on an event/webinar/meetup attendee list we control.
- **Re-engaged** = appeared on *another* such list in a later quarter. This measures repeat attendance at DevRel touchpoints, not product usage, logins, or API activity — those aren't wired to this dataset.
- Where only registration data exists (not check-in), the cohort may include no-shows — note per row if a quarter is registrant-only vs. verified-attendance.
- Matched by email address across lists. Flag the match rate if any quarter's list lacks email (name/company-only badge scans, for instance) — a low match rate for an older quarter explains a lower number without it being a real drop-off.

## The caveat you say out loud, not just print

> "We've never run a pre-period, so there's no untouched control group here — this shows how long our own audience keeps re-engaging with us, not incremental lift over developers we didn't touch. This is the first time we've had *any* longitudinal read on our own audience. It's a baseline, not a causal claim."

Say this before anyone asks it as a gotcha. A CMO signing off on headcount will respect "here's exactly what this does and doesn't prove" far more than a number that cracks under one follow-up question.

## The bridge to the ask

> "This cost zero engineering time — it's a manual join across attendee lists we already had sitting in [Attio/CRM]. What it can't tell us is whether these developers are actually *using* the product, because that requires tying event identity to product telemetry, which needs engineering time we don't have this cycle. Next cycle's ask includes exactly enough eng time to close that gap."

This does two things for the defense: it proves the team can produce real signal with no engineering dependency (protects this cycle's headcount), and it turns the current method's biggest weakness into next cycle's concrete, scoped ask — rather than something a sharp CMO discovers on their own.

## Build steps (no engineering required)

1. Export each quarter's attendee/registrant list, dedupe by email.
2. For each Q4'25/Q1'26/Q2'26 cohort, filter later quarters' lists for email matches → fills the triangle above.
3. Note registrant-only vs. check-in-verified per quarter, and email-match rate per quarter, as the two footnote caveats.
4. Pull final numbers after Sep 30 close of Q3 2026, five weeks out is enough runway.