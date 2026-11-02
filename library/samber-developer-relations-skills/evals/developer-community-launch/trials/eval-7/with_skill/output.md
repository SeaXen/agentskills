# Palebright GitHub Discussions — Measurement Plan

Two of the three things in the brief need correcting before they go on paper. Here's the plan, with the fixes built in.

## 1. Fix the lurker-share target first

⚠️ **"Get non-posters below 40%" is the wrong target — don't ship it.**

Jakob Nielsen's 90-9-1 rule (NN/g, 2006, the most-replicated finding in community measurement): across forums and wikis, roughly **90% of members never post, 9% post occasionally, 1% account for most activity.** Lurking is the baseline condition of every online community, not a defect to fix. Source: [nngroup.com/articles/participation-inequality](https://www.nngroup.com/articles/participation-inequality/).

Read against that baseline, the beta's "four in five just read" (80% lurk) is **already better than typical** — most communities never get below 90%. A target of <40% asks for a 60%+ posting rate, which no mainstream developer community sustains. Two concrete problems with shipping it anyway:

- **It's not reachable.** No comparable space (Discourse, Discord, GitHub Discussions on any OSS project) runs at that ratio. The VP would be judged against a number nothing passes.
- **It rewards the wrong behavior.** The fastest way to lower a lurker *percentage* is to stop acquiring members — directly at odds with the 2,000-member goal. A launch that hits 2,000 members and 35% never-posters (by suppressing joins) would "pass" while a launch that hits 2,000 members and 200 genuinely active contributors would "fail."

**Replacement:** target the count and rate of *active* members directly, not the inverse of the lurker share. This keeps the VP's real concern — "is anyone actually talking in there?" — without the broken math.

## 2. Corrected day-90 target set

| What the VP asked for | What ships instead | Why |
|---|---|---|
| 2,000 members by day 90 | Keep, but report as context only | Member count is a joins counter, not a health signal — a well-marketed room can hit 2,000 with 20 weekly posters and still be a failed launch |
| Non-posters < 40% | **≥ 20% of members active in the trailing 30 days** (≈400 people at 2,000 members), reported as an absolute count alongside the ratio | Matches the 90-9-1 baseline instead of inverting it; absolute count survives churn better than a percentage does |

## 3. Full day-90 threshold table

Metric definitions are published practice; cutoff values are practitioner baselines to recalibrate once Palebright has its own trailing data — treat them as a starting hypothesis, not a standard.

| Signal | Pass | Warning | Failing | Basis |
|---|---|---|---|---|
| Questions answered within 24h | > 90% | 75–90% | < 75% | Baseline practice |
| Posts written by non-staff | > 50% | 30–50% | < 30% | Baseline practice |
| New members posting within 7 days | > 40% | 20–40% | < 20% | Baseline practice |
| Monthly active / total members | **> 20%** (≥ 400 at 2,000 members) | 10–20% | < 10% | Baseline practice |
| Threads with ≥ 1 reply | > 80% | 60–80% | < 60% | Baseline practice |
| Engagement share of top 5 members | < 50% | 50–80% | > 80% | Baseline practice |

Reading rule: **two or more signals in "failing" → don't promote harder.** More joins into a quiet room lowers every ratio further. Re-run seeding instead, or trigger fold-back (§6).

GitHub Discussions specifics that affect two of these rows: any authenticated user who can see the repo can post (zero extra signup, so "new members posting within 7 days" isn't gated by an onboarding flow); the "mark as answer" feature gives a clean, native way to compute "questions answered within 24h" instead of eyeballing threads.

## 4. Why "check in at end of quarter" isn't enough on its own

A single day-90 check means the first time anyone looks, it's too late in the quarter to fix anything cheaply. Add earlier checkpoints:

| Checkpoint | What to look at | Signal |
|---|---|---|
| **Day 7** | Founding-cohort activity is running | Sanity check, not a metric |
| **Day 30** | Any post from outside the founding cohort · any question answered by a member, not staff · median first response time under a few hours | Behavioral, not ratios — too early for percentages. **Zero member-authored answers at day 30 predicts a failed day-90 gate.** Act then, not at day 90. |
| **Day 60** | Trend on the six ratios above, against a trailing baseline | Catch a bad trajectory with a month left to correct it |
| **Day 90** | Full pass table (§3) | Go / no-go call with the VP |

Source for the day-30 rule and the 48h-response evidence: Mozilla study cited in GitHub's Open Source Guides — contributors who got a response within 48h returned and contributed again at a much higher rate; "it only takes one negative experience to make someone not want to come back." [opensource.guide/building-community](https://opensource.guide/building-community/)

## 5. Baseline discipline

- **Compare every number to a trailing 30-day window, never to the launch spike.** The announcement week will over-perform on every metric; CHAOSS calls this burstiness — it decays on its own and is the most common false trend in community reporting. Don't let week one set expectations for week twelve.
- **Track joins and leaves separately.** Net member count hides churn; report both.
- **Report the active-member count next to every percentage**, not the percentage alone — with a ~90% lurker baseline, ratios move as fast from people leaving as from activity growing.

## 6. Fold-back criteria (set now, not at day 90)

Trigger: two or more day-90 signals in "failing," or zero member-authored answers still true at day 30 with no recovery by day 60.

Exit, in order of what's cheapest to give up:
1. **Archive to read-only** — keeps the existing answers searchable at near-zero effort.
2. **Convert to a plain support Q&A** — keeps the space, drops the community framing.

(The third option in the general playbook — merge into an existing space the audience already uses — only applies if Palebright has one; flag if it does.)

Decision owner: **name this person now.** Whoever owns the day-90 read should also be the one authorized to pull the trigger — otherwise the fold-back becomes a debate instead of a decision.

## 7. Who measures, how, from where

GitHub Discussions has no built-in ratio dashboard. Two options: pull the six metrics via the GitHub GraphQL API on a weekly cron (cheap to build once, reusable every quarter), or sample manually for one week per month if nobody owns the script. Either way, name the person and the cadence in the brief — "marketing will keep an eye on it" is the exact ownership gap that produces a ghost town.

## 8. Confirm before this is final

- **Primary outcome (SPACES):** this plan assumes **Support** (deflecting setup/integration questions) since that's the default reason a dev-tool opens GitHub Discussions. If the VP's real goal is roadmap feedback or advocacy instead, the metric weighting shifts — confirm which one is primary; the skill's own rule is exactly one, not a list.
- **B2B mix:** if any of the 2,000 are paying customers whose renewal doesn't depend on them posting, they need a separate signal path — a silent enterprise account isn't the same failure as a silent hobbyist. Flag if that applies.