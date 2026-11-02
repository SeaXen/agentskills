Skill + all three references read. Deliverable below.

---

# Sanity check: Vantablue advocate targets

## Verdict

Right instinct, wrong instrument. Four per-person **activity quotas**, comp-loaded, no counter-metrics, no attribution rule, no baselines. Skill predicts all four failure modes by name: thin posts, chatter, premature closes, throwaway accounts (Strathern's law: "when a measure becomes a target, it ceases to be a good measure"). Funded driver at Vantablack is **developer adoption** — none of these four metrics measures adoption. All measure effort.

## Per-metric check

**1. 6 blog posts/month each — 🔴 cut**
- Tier: reach, and pre-reach — counts effort, not even views. "Activity log as a report. Survives exactly one budget review."
- Feasibility: 6/month = 72/year each, 288 team-wide. Quality CI-orchestration post (benchmarks, migration guide, deep dive) = 8-20h. That is ~45% of one FTE just writing. Stacked with quotas below, >100% load. Physically incompatible → thin posts, or quota miss.
- Audience cannot consume 24 posts/month from one vendor.
- So-what test fails: hit the number, nothing follows.

**2. 40 community messages/week each — 🟠 convert**
- Tier: engagement. Undefined term = gameable. Staff-to-staff chatter counts; four advocates can hit 40/week talking to each other.
- Volume itself (8/business day) feasible. Question is whether community generates enough inbound. If not, target manufactures noise.
- Convert: % of non-staff questions answered, median first-response time, resolved-thread rate. Team-level.

**3. 20 GitHub issues closed/month each — 🟠 convert**
- "Closed" counts duplicates, wontfix, stale-stomps. Comp on closures → premature closes, reopen storm later.
- Issues closed ≠ issues resolved — resolution often belongs to engineering. Advocate owns triage and response.
- Better: CHAOSS Starter Project Health. Median time to first response (bots excluded), closure ratio near ≥1 (self-set, not a published standard). Counter-metric: reopen rate.

**4. 500 signups/quarter attributed per person — 🔴 delete, worst of set**
- Per-person attribution is structurally unavailable. DevRel touches sit off-web (hallway, podcast, colleague rec). ~70% of AI-assistant traffic arrives no-referrer → "direct". Self-reported first touch names surfaces, not staff members. No honest rule assigns one signup to Advocate B over C.
- Rule written after the quarter = narrative. With comp attached = monthly credit dispute. Same signup touched by blog (A), Discord answer (B), conference chat (C): zero-sum fight.
- Arithmetic: 4 × 500 = 2,000/quarter attributed ≈ 154/week. If honest program-attributed share is a minority of signups, target is unreachable or gamed — UTM spam, throwaway accounts.
- Also wrong tier for an adoption company: signup without activation is near-vanity.

## What's missing

1. **Enablement tier — the tier DevRel owns and best ROI.** For CI orchestration: signup → first green pipeline within 7 days; median time to it; quickstart step drop-off. Nothing in your set measures whether developers *succeed*.
2. **Product impact — required minimum one.** 30-day retention (still running pipelines), second-project rate. Nothing measures whether they *stay*.
3. **Attribution rule, written before period starts.** Determines what "attributed" may even claim. Currently absent while comp hangs on it.
4. **Baselines + threshold provenance.** All four numbers are inventions. Every threshold must carry tag: `sourced`, `baseline`, or `hypothesis`. Folklore number presented as target = credibility loss when checked once. No three prior periods = mark "baselining", set threshold at next review. First two cycles: direction + range, never point.
5. **Counter-metrics + definitions.** Comp-loaded volume needs quality pair (posts → organic entries per post; closes → reopen rate; signups → 30-day retention). "Signup", "message", "closed" all undefined.

Also missing: team-vs-program distinction (per-person identical quotas turn colleagues into competitors), kill rule, burst-vs-trend guard, blind spots, qualitative rows, reporting cadence. And the quotas reward none of Vantablack's actual adoption levers — docs quality, DX, quickstart fixes — a docs rewrite beats 6 posts and counts zero.

## Replacement sheet (team-level)

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|--------|------|-----------|--------|----------|-----------|-------|--------------------|
| 1 **P** | First-success rate, 7d | Enablement | share of new accounts running first green pipeline on own repo ≤7d of signup | product analytics, `first_green_pipeline` | baselining | set at next review | enablement advocate | cold-run quickstart, fix top failing step |
| 2 | Median time to first green pipeline | Enablement | signup → success event, median | product analytics | baselining | set at next review | enablement advocate | instrument step drop-off |
| 3 **P** | 30-day retention of first-success cohort | Product impact | still running ≥N pipelines/week at day 30, monthly cohort | product analytics | baselining | set at next review | team lead | interview 5 lapsed accounts |
| 4 | Docs search terms, no result | Engagement | count + top terms per month | docs search log | baselining | set at next review | docs advocate | write missing page (metric names own fix) |
| 5 | Median time to first human response | Engagement | issues + community threads, CHAOSS definition, bots excluded | forge API, community export | baselining | trailing median (any 24h/48h line = hypothesis, not standard) | repo advocate | triage rotation |
| 6 | Self-reported first touch | Engagement | one signup question, stable option list | signup survey | baselining | response rate <40% = hypothesis | team lead | shorten question |
| 7 | Publishing cadence + organic entries per post | Reach + counter | team posts/month floor; quality read = organic entries per post | blog platform, comments | baselining | set at next review | content advocate | cut lowest-quartile format |
| 8 | Friction findings + verbatims | Qualitative | findings with fix shipped + date; quotes with source | manual log | — | <2/quarter | all | schedule user conversations |

All thresholds honest state today: **baselining**. Do not set numbers until three prior periods exist.

## Attribution rule (draft)

- Standing instrument: one signup question, stable options, free text. Reported as *self-reported first touch* — direction, not precision.
- Tagged links per post/campaign: artifact-vs-artifact comparison only. Never program totals.
- Signup credit assigned to **surfaces, never individuals**. No per-person attribution exists — say so in writing.
- If pipeline ever measured: *influenced* only, 180-day lookback, shared credit, fixed for fiscal year. Never sourced.
- Blind spots, published: word-of-mouth, docs read without signup, AI assistants answering from docs, partner-mediated reach.

## Comp design

1. Team gate first: ≥1 outcome metric (first-success or 30-day retention) not below baseline. No team bonus on activity quotas alone.
2. Individual layer: function-split ownership (Thengvall awareness/enablement/engagement) — each advocate owns *one different* number matching their role. Not four identical quotas.
3. Volume ≤50% of individual score. Counter-metric can claw back (reopen rate, retention, organic entries).
4. No individual comp on attributed signups. Full stop. Unmeasurable + zero-sum = dispute machine.
5. Review quarterly for gaming; re-baseline thresholds after three periods.

## Pass-threshold check on your draft

- 5-8 metrics: count passes, shape fails
- Six fields per metric (definition, source, baseline, threshold, owner, action): 0 of 4
- ≥1 product/business-impact metric: fail
- "So what" + ownership tests: posts fail both; per-person signups fail ownership
- Attribution rule written, methods + lookback named: fail
- Counter-metric on every incentivized volume: fail — comp attached to all four
- Thresholds tagged sourced/baseline/hypothesis: fail — four unlabeled inventions
- Blind-spots section: fail

## Assumptions + open questions

Assumed: driver = developer adoption (your stated context); self-serve signup motion; team adoption inside orgs. Answers that would reshape the sheet:

1. Signups self-serve only, or sales-assisted org tier too? (Account-level metrics enter if yes.)
2. Does a success event exist in product analytics today? If not, that is an engineering ask — ~days, one-time.
3. Actual current signups/quarter, community inbound/week, issue inflow/month? (Feasibility check on every number you picked.)
4. Whose budget line — product or marketing? Decides whether an influenced-pipeline row enters at all.
5. First hard date numbers must land by?

Once you validate a sheet, I record baselines + attribution rule to memory so next quarter starts from recorded history, not re-derivation.