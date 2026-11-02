Right skill. Cindersmith community already exists (GitHub + ~30 external contributors + Discourse forum) — not launch, moderation, triage-design, onboarding, champions or full devrel-metrics territory.

## The trap in your ask

You listed support deflection, product feedback, contribution growth, advocacy, retention, general engagement. That's CMX's own SPACES model (Support, Product feedback, Acquisition, Content, Engagement, Success) recited almost in order. CMX's instruction for SPACES: "just focus on one objective." Six objectives on one sheet, six vague sheets nobody refreshes past month two. Pick one now. Rest still get measured, just not as the headline.

**Recommendation: Support.** *"Users answer each other's usage/config questions on Discourse, so the core team's hours stay on the search engine, not on Q&A."* Reasoning: cheapest pillar to prove (both GitHub and Discourse have APIs, near-zero collection cost), fastest to a real first read, and the usual reason an infra project stands up a forum at all. ⚠️ Confirm or override — if the real pain is bus-factor with only 30 contributors, swap primary outcome to Content/contribution instead (sheet below barely changes, see note after the table).

## Vocabulary ruling

Two ladders in your own materials — casual/regular/core (product team) and Orbit's explorer/participant/contributor/advocate (your slides). Skill's rule: one vocabulary, or every cohort definition goes ambiguous.

**Use casual/regular/core going forward.** It's already the company's internal standard — cross-team legibility beats granularity. Drop Orbit wording from new slides. Translation table for anything already built on Orbit language:

| Casual / regular / core | Orbit equivalent | Operational definition (self-set) |
|---|---|---|
| Casual | Explorer, Participant | Posted/commented ≤1 time ever, no merged PR |
| Regular | Participant, Contributor | ≥2 active months in trailing 90 days, OR ≥1 merged PR, OR ≥5 forum replies |
| Core | Contributor, Advocate | ≥1 merged PR in each of last 2 quarters, OR named maintainer, OR public advocacy (talk/blog/tutorial about Cindersmith) |

Orbit itself is fine to cite as a stable, no-longer-developed reference framework — just not as a second live vocabulary next to the one your product team already uses.

## Metric sheet (8, all four pillars, at the ceiling)

Classification: open source / individual-adoption (not B2B) — unit is the person, cohort retention and concentration measures do real work here.

| Metric | Pillar | Formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Median time to first human response (Discourse) | Responsiveness — **primary outcome** | Question topic → first non-bot, non-staff-optional reply | Discourse Data Explorer / API export | baselining — pull retention-window history now | > 24h react / > 72h act-now (**folklore**, unsourced — recalibrate after 3 periods) | TBD | Rotate answer duty across timezones; "away" banner during team travel |
| Unanswered question rate (Discourse) | Responsiveness | Zero-reply question topics ÷ all question topics, 7-day window | Discourse export | baselining | < 10% healthy / > 25% act-now (**folklore**) | TBD | Weekly sweep of unanswered threads, rotating volunteer |
| Contributor absence factor (GitHub) | Contributor funnel | Smallest N contributors covering 50% of commits | `git log` via `scripts/contributor-absence-factor.sh` | **computable today**, full history, no retention cap — run now | 1 = single point of failure (**published definition, CHAOSS**; risk read is catalog interpretation, not a numeric standard) | TBD | Open reviewer rung to top N contributors |
| First-time participants per period | Contributor funnel | Distinct identities (GitHub + Discourse, post-identity-merge) with no prior activity | GitHub API + Discourse export + identity map | baselining — needs identity map first | none yet — read as trend, not ratio | TBD | If it drops 2 months running, check whether the on-ramp (good-first-issue flow) changed |
| Second-contribution rate within 90 days (GitHub) | Contributor funnel | Returning first-time PR/issue authors ÷ first-time authors, per monthly join cohort | GitHub API | **retroactively computable** — pull last 6 monthly cohorts now, no waiting | trailing median of those 6 cohorts (**self-set**) | TBD | Review first-response time on new contributors' first PR/issue |
| Non-staff share of activity | Activity | (Discourse replies + GitHub review/PR comments not by core team) ÷ total same set | Discourse export + GitHub API + staff-flag list | baselining — needs staff flag list first | staff share < 30% healthy / > 50% act-now (**folklore**, inverted for non-staff framing) | TBD | Publicly recognize top community answerers; core team stops answering first |
| Active participants per period | Activity | Distinct non-bot people posting/commenting/committing, both venues, post-identity-merge | GitHub API + Discourse export + identity map | baselining | none yet — absolute count, not ratio (community size denominator not established) | TBD | 2 consecutive drops → run diagnosis mode (activity trend, staff share, burstiness) before acting |
| Recommendability | Sentiment | "How likely to recommend this community/project?" — Likert, scored promoters% − detractors% | Quarterly 2-item pulse survey | baselining — first two pulses set the baseline, don't compare to external numbers | drop > 15 points off own baseline (**self-set**, after baseline exists) | TBD | Interview 5 detractors |

**If primary outcome is Content/contribution instead:** swap the two Discourse responsiveness rows for "time to first response on GitHub PRs/issues" (VMware's 2-business-day internal guideline, quoted in CHAOSS, applies here — code review, not forum Q&A) and "change request closure ratio." Funnel/activity/sentiment rows stay as-is.

## Instrumentation — what's live, what's not

- **Rung 1 — GitHub API / git history.** Near-zero effort, no retention cap, full backfill available today. Covers absence factor, both funnel-cohort metrics.
- **Rung 2 — Discourse's own API / Data Explorer plugin.** Cheap, not free — check your plan's data retention before assuming full backfill (self-hosted vs. hosted tiers differ). Covers both responsiveness metrics, half of activity.
- **Rung 3 — community-data platform.** Not needed. No named pipeline owner, no cross-venue identity blocker yet, no question the first two rungs have failed twice. Don't park it as "future work" — revisit only if that trigger condition actually shows up.

Traps to close before trusting a single number:
- **Bots.** Script already excludes `bot|\[bot\]|dependabot|renovate|github-action`. Add Discourse's own system/discobot accounts to an equivalent exclude list.
- **Identity.** 30 contributors + forum users is small enough for a hand-maintained GitHub-handle ↔ Discourse-username spreadsheet. Build it before running non-staff-share or cross-venue counts.
- **Staff flag.** List core-team GitHub handles + Discourse usernames now — blocking dependency for the non-staff-share metric.
- **Retention.** Snapshot Discourse's monthly numbers into your own store starting this month regardless of plan — backfill may not be possible later.

Privacy: GitHub + Discourse activity is public by nature of the project, so aggregate activity/funnel/responsiveness metrics carry low exposure. Sentiment survey stays a hard gate regardless — aggregate only, no per-member leaderboard, check the Discourse instance's own terms before any bulk export of message content.

## Day-0 runbook (this week, no waiting for "three periods")

1. Run `bash scripts/contributor-absence-factor.sh -r <repo path>` — first real number, today.
2. Pull last 6 monthly join-cohorts from GitHub API for second-contribution rate — real baseline, not "baselining."
3. Build the GitHub-handle ↔ Discourse-username identity map (spreadsheet, 30+ rows).
4. Build the staff-flag list (core team handles, both venues).
5. Check Discourse plan's data-retention window before assuming full backfill.
6. Draft the 2-item quarterly pulse survey (recommendability + open-text frustration) — first wave whenever convenient, no dependency on the above.

## Open gaps — not guessed, need your input

⚠️ **Owner** — every "TBD" cell above blocks Pass threshold. Name one person before the sheet counts as done.
⚠️ Community size / weekly volume, effort ceiling (hours/month), hard deadline, existing tracking, specific worry behind the ask, privacy/legal constraints on export — none stated. Assumed: OSS/individual-adoption, no deadline, compounding sheet (not one-off), monthly cadence, low effort budget. Flag any of these that's wrong and the sheet above shifts.

## Cadence & next review

Monthly working read, quarterly roll-up to whoever funds it. First live report with real numbers: **16 Oct 2026** (4 weeks — enough time for the Day-0 runbook plus one Discourse cycle).

Next action: run step 1 of the Day-0 runbook now — one command, real number in under a minute.