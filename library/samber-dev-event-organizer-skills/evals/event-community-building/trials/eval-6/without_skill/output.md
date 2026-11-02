# RustReef community KPI sheet (v0.1, not final)

**Next action:** pull the 6 baseline numbers in the last section. Three targets can't be set without them. Two of the three board premises also need fixing first.

## Changes to the draft

| Draft item | Verdict | Why |
|---|---|---|
| (a) DAU + monthly messages as headline | ⚠️ Demote | Both measure volume, not health. An activation push inflates them without adding real participation. Slack also counts a passive reader as "active". |
| (b) Beat 30% industry retention with 45% | ❌ Don't commit | The 30% is unsourced, and "events industry blended retention" has no standard definition (denominator, window, and event type all vary). Set the target from our own prior-edition return rate. |
| (c) 5/12/45 thresholds, so we're failing | ❌ Don't act on it | I can't verify those thresholds. They look like a garbled version of Dunbar's 5/15/50/150, which describes personal social circles, not community health. Ask the consultant for the source. |
| "50 of 3,100 talk" | ⚠️ Not evidence of failure yet | 1.6% posting is within the range the common "90-9-1" heuristic predicts for open communities. That's a rule of thumb, not a law. The "50" also has no stated window. |

## KPI sheet

**Headline (3 numbers for the board)**

| # | KPI | Definition | Source | Target |
|---|---|---|---|---|
| 1 | 30-day contributor rate | Members who posted or reacted at least once in 30 days ÷ total members | Slack analytics export | Baseline + agreed uplift (TBD) |
| 2 | Edition-over-edition return rate | Attendees of edition N-1 who attend N ÷ attendees of N-1 | Ticketing data, matched by email hash | TBD from own baseline |
| 3 | Unanswered-question rate | Questions with no reply in 48h ÷ all questions | Help/Q&A channels, sampled | Lower than baseline (TBD) |

**Supporting (tracked, not headlined)**

| # | KPI | Definition | Why it's here |
|---|---|---|---|
| 4 | Weekly active posters | Distinct members who posted in 7 days | A steadier version of DAU |
| 5 | New-member first-week post rate | New joiners who post within 7 days ÷ new joiners | Measures onboarding, the cheapest place to intervene |
| 6 | Slack-attendee overlap | Members who attended ÷ 3,100; attendees who joined Slack ÷ 2,800 | Shows whether the conference feeds the community |
| 7 | Message volume (monthly) | Total messages | Context only. Never a target. |

**Guardrails**
- Don't set DAU or message-volume targets. Targets on them invite gaming.
- Report KPI 1 beside the median thread depth, so a push of drive-by posts is visible.
- Freeze each definition for 12 months. A change restarts the trend.
- Report the return rate with its denominator, e.g. "412 of 1,100".

## Return-rate target (replaces the 45%)

1. Compute our edition N-1 → N return rate.
2. Set the target at that baseline plus a modest, stated uplift. Treat any external benchmark as context only, with its definition and source cited.
3. Present 45% to the board only if the baseline makes it plausible. A target that sounds good against an unverified 30% is a weak commitment.

## Activation push: hold

Run a 2-week diagnosis first:
- Count how many of the 3,100 are people who attended once and never opened Slack, versus lurkers who read but don't post.
- The fix differs: lurkers need low-friction prompts, and dormant accounts need pruning or re-invites.
- Prune dead accounts before computing rates, or the denominator hides real engagement.

## Baseline pulls needed (≈1–2h)

1. Slack 30-day posters and reactors, last 6 months.
2. The "50" figure: what window and what definition.
3. Edition N-1 → N return counts from ticketing.
4. Slack-attendee overlap, by email.
5. Median first reply time and 48h-unanswered rate in 2–3 Q&A channels.
6. The consultant's source for 5/12/45.

Send me those and I'll set the three targets and finalize the sheet.