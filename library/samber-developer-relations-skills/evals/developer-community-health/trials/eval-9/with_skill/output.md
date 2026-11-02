# Sablefish community health dashboard — redesign

Read `developer-community-health` (SKILL.md) plus its three references and the absence-factor script in full before building this. Below is the rebuilt framework: root-cause diagnosis, the "active members" fix, the 19→8 metric sheet, the threshold mechanism that replaces the frozen cutoffs, named ownership, a cutover plan, and a ready-to-use report template.

## ℹ️ Assumptions made instead of a live interview

The skill calls for a one-question-at-a-time interview before building the sheet. Since this needs to land as one complete deliverable, I made the calls below instead of asking — flag any that are wrong and the sheet updates, nothing here is load-bearing on the parts you didn't state:

| # | Question | Assumption |
|---|---|---|
| 1 | Community shape | Both: a contributor base on GitHub (forge) + a chat/support venue run by the community team (assumed Discord/Slack-shaped — swap in the real one) |
| 2 | B2B or individual-adoption | Individual-adoption / open source — you said "open-source ETL tool," not "accounts" |
| 3 | Primary outcome | **Support deflection** — the community answers usage questions so maintainers spend time on the roadmap, not repeat support threads. Contribution funnel is the secondary outcome, tracked but not primary |
| 5/6 | Data access / what's already collected | Forge API (GitHub) and a venue analytics export, both already flowing into the current 19-metric dashboard |
| 7 | Effort ceiling | Existing team, no new budget implied |
| 9 | One-off vs compounding | Compounding — you inherited a standing dashboard, the intent is to keep running it |

If venue, outcome, or B2B-ness is wrong, only the "active community participants" source and the primary-outcome framing need to change — the rest of the structure holds.

## What's actually broken

Three distinct failures, not one — worth naming separately because each has a different fix:

1. **Threshold rot.** Cutoffs frozen at launch, never re-derived. This is a named failure mode in the skill itself: *"A threshold nobody has revisited... fires every month, gets muted, and the metric quietly stops being read."* Half going red monthly and getting muted is exactly that pattern completing itself.
2. **Same metric, two formulas, one name.** Also a named failure mode: *"One person counts 'active' as posted-or-reacted, another as posted-only... Fix it by publishing the formula beside the number, not by arguing in the meeting."* These aren't actually duplicates once correctly scoped — they measure two different pillars. The meeting keeps arguing because they share a name, not because either number is wrong.
3. **No owner.** Also named: *"If nobody is named for the review, it stops being refreshed by month three."* A metric with no owner and no attached action is decoration, not a health metric — the skill's Pass threshold requires both on every row.

19 metrics also blows the skill's own ceiling of 8 by more than double — a sheet that size is why nobody can hold the whole thing in their head to notice #1 and #3.

## Fix 1 — kill the "active members" argument

Stop calling either number "active members." They are two different metrics, in two different pillars, owned by two different teams, and both are worth keeping:

| | Community team's number | Data team's number |
|---|---|---|
| New name | **Active community participants** | **Active contributors** |
| Formula | posted OR reacted, distinct non-bot identities | posted only — authored a commit, opened a PR, or opened/commented on an issue |
| Pillar | Activity (venue health — is the room alive) | Activity (forge health — is the codebase getting worked) |
| Source | Venue analytics panel | GitHub API |
| What it's for | Deciding whether to recruit more answerers, seed threads, run an AMA | Deciding whether to open the reviewer rung, chase bus-factor risk |

Neither is "the" active-members number. Publish both, side by side, formula printed next to each, every month. The argument was never about arithmetic — it was about one label doing two jobs.

## Fix 2 — cut 19 → 8

Cutting rule (from the skill): keep a metric only if it passes the "so what" test — *if it moved 20% next month, would anyone with a name do something differently?* — and cover all four pillars with at least one each. Send me the current 19 and I'll sort each one into this table directly; until then, here's the target sheet and the pruning heuristic to apply:

**Near-certain cuts** in any 14-month-old, never-pruned dashboard, per the skill's failure modes: total member count (only goes up, says nothing), raw message/post volume with no baseline, any auto-sentiment-classifier score, per-member leaderboards (privacy exposure, and not a health signal), any metric with no formula documented next to it (if nobody can currently say the formula from memory, it's already failed the audit).

**The 8 that survive**, one line each so a reader sees the whole sheet at once:

| Metric | Pillar | Definition / formula | Source | Owner | Action if breached |
|---|---|---|---|---|---|
| Median time to first human response | Responsiveness | GitHub issue/PR opened → first non-bot human reply, median | GitHub API | Community lead | Recruit answerers in the timezone gap; check for a travel/absence window before treating as a trend |
| Zero-reply rate | Responsiveness | Issues/PR threads with no human reply within 7 days ÷ total | GitHub API | Community lead | Weekly sweep of unanswered threads |
| Change request closure ratio | Responsiveness | Closed (merged + rejected) ÷ opened PRs, same window | GitHub API | Maintainer lead | Triage backlog if ratio holds under 1 for 2+ periods |
| Contributor absence factor | Contributor funnel | Smallest number of people producing 50% of commits (`bash scripts/contributor-absence-factor.sh -r <repo> -s "6 months ago"`) | git history | Maintainer lead | Open the reviewer rung to the next 2-3 contributors |
| Second-contribution rate (90 days) | Contributor funnel | First-time contributors who return within 90 days ÷ first-time contributors, monthly join cohorts | git/forge history | Maintainer lead | Review first-response time for newcomer PRs |
| Active contributors per period | Activity | Distinct non-bot people who authored a commit/PR/issue in the period | GitHub API | Data team lead | Diagnose before acting — check for a release burst first |
| Active community participants | Activity | Distinct non-bot people who posted or reacted in the venue in the period | Venue analytics | Community lead | Diagnose before acting — check for a release burst first |
| Recommendability | Sentiment | "Would you recommend Sablefish to other people?" — NPS-style, promoters % minus detractors %, quarterly pulse (2-item survey, see `references/survey-instruments.md`) | Quarterly survey | Community lead | Interview 5 detractors |

All four pillars covered. 3 responsiveness / 2 funnel / 2 activity / 1 sentiment — matches the skill's own efficiency ranking (responsiveness buys the most decisions per hour of collection, sentiment the fewest, at highest effort).

Owners above are roles, not names, because I don't have your org chart — replace with actual people before publishing. That alone closes failure #3.

## Fix 3 — replace the frozen cutoffs

14 months = roughly enough history to skip straight to the mature mechanism instead of re-freezing new numbers:

- **≥6 periods of history exist for a metric** (true for anything the old dashboard already tracked in a compatible form): set a **deviation band** — flag a reading that leaves its trailing rolling mean ± a stated band (pick a % or a spread of standard deviations, write the choice on the sheet) — not a fixed number. Recompute the band every review. This is what stops a threshold from calcifying a second time.
- **Metric exists but wasn't tracked in this exact formula before** (zero-reply rate, second-contribution rate, either "active" split): mark **"baselining,"** pull the last 3-6 periods retroactively from raw GitHub/venue exports if the underlying event data is still queryable, and set the first real threshold once that history exists.
- Label every threshold's origin on the sheet itself (published / self-set / folklore) — the skill's own distinction. A cutoff copied from an "industry standard" blog post is folklore until your own trailing median replaces it; say so instead of presenting it as settled.

⚠️ Don't carry over any of the 19 old numeric cutoffs unexamined — re-derive every single one from this community's own trailing data, even where the old value happens to look reasonable. That's exactly how the first freeze happened.

## Cutover plan

1. Pull 6 months of raw GitHub + venue export data (the underlying events, not the old dashboard's rolled-up numbers) to seed baselines for the 8 metrics above.
2. Compute the two "active" numbers under their new names and formulas for the last 3 months, show both side by side once in the next monthly meeting, with formulas printed next to each — this is the moment the argument should stop recurring.
3. Archive the old 19-metric dashboard's historical values rather than deleting them (retention windows on some venues make backfill impossible later — snapshot before retiring).
4. Assign real names to the four owner slots above.
5. Publish the new 8-metric sheet with "baselining" marks where 3 periods don't exist yet, and real deviation bands where they do.
6. Set review cadence: monthly working read for community + maintainer leads, quarterly roll-up for whoever asked for the dashboard originally.

## Report template for the next cycle

```markdown
# Community health - Sablefish - {period}

## Primary outcome
Support deflection: the community answers usage questions so maintainers spend their hours on the roadmap, not repeat support threads.

## Metric sheet
| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Median time to first human response | Responsiveness | GitHub issue/PR → first non-bot reply, median | GitHub API | baselining | — | {name} | Recruit timezone-gap answerers |
| Zero-reply rate | Responsiveness | Zero-reply threads ÷ total, 7-day window | GitHub API | baselining | — | {name} | Weekly unanswered sweep |
| Change request closure ratio | Responsiveness | Closed ÷ opened PRs | GitHub API | baselining | — | {name} | Triage backlog |
| Contributor absence factor | Contributor funnel | Smallest N for 50% of commits | git history | baselining | — | {name} | Open reviewer rung |
| Second-contribution rate (90d) | Contributor funnel | Returning ÷ first-time, monthly cohort | forge history | baselining | — | {name} | Review newcomer PR response time |
| Active contributors / period | Activity | Posted-only, distinct non-bot | GitHub API | baselining | — | {name} | Diagnose burst vs trend |
| Active community participants / period | Activity | Posted-or-reacted, distinct non-bot | venue analytics | baselining | — | {name} | Diagnose burst vs trend |
| Recommendability | Sentiment | NPS-style, promoters% − detractors% | quarterly pulse | baselining | — | {name} | Interview 5 detractors |

## Reading - {period}
| Metric | This period | Baseline | Direction | Note |
|---|---|---|---|---|

## Findings
1. {finding} - evidence: {}. Confidence: {high/medium/low, why}.

## Actions
| Action | Owner | By when | Metric it should move |
|---|---|---|---|

## Watch list
{metrics still baselining, instrumentation gaps, events that distorted the period}

## Next review
{date}
```

## Findings on this redesign itself

1. The two "active members" figures were never actually in conflict — they measure different venues and different pillars under one shared, ambiguous label. Evidence: community team's formula includes reactions (venue-sourced), data team's excludes them (forge-sourced). Confidence: high — this is a direct read of what you described, not inferred.
2. Roughly half the old sheet going red monthly with muted alerts is the textbook signature of a threshold set once at launch and never re-baselined against the community's own trailing data. Confidence: high — matches the skill's own named failure mode exactly.
3. No owner on any of the 19 metrics means none of them currently pass the skill's Pass threshold (definition + source + baseline + threshold + named owner + action, on every row) regardless of whether the number itself is right.

## Next review

Propose **31 Oct 2026** — one full cycle out, enough time to pull 6 months of raw history, seed baselines, and run the "active" split live in one meeting before locking the sheet.

Once you confirm the primary outcome and the two flagged assumptions (venue name, B2B-vs-open-source), this is ready to persist as the standing framework — happy to save the primary outcome, metric sheet, and baselines to memory at that point so the next review starts from a recorded state instead of re-deriving it.