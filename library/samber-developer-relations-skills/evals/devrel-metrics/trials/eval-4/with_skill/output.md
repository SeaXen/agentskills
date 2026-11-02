Routing first: this is a **devrel-metrics** job (prove DevRel value to exec, handed a pipeline target). Not devrel-analytics (instrumentation) — one gap gets handed to it below.

Next action: get the attribution rule below signed off by CRO + sales ops **before the quarter's touches start aging**. Rule agreed after the period starts is already a narrative. About 1 week of work: 2 days restatement, 1 day backfill, 2 small asks.

---

# What the $1.2M actually is

Three defects. Each fatal in a different room.

1. **Post-hoc rule.** Joining rule written after quarter closed. Redrawn next quarter, produces any number its author needs.
2. **"Sourced" is a claim Sales contests and wins.** Deals sit in reps' names in the CRM. First forecast review where Sales attribution claims the same $1.2M, one number dies. Not Sales'. Sourced is exclusive; DevRel never owns last touch on six-figure deal. Influenced is shared by definition.
3. **Counts selection, not influence.** Companies buying observability send engineers to observability workshops. Spreadsheet cannot separate "workshop caused deal" from "buying accounts attend workshops." No lookback window. No stage condition. Badge scanned during open deal counts same as badge from year before.

Plus latency: 8-month cycle means closed revenue last quarter credits workshop work from ~3 quarters earlier. Any quarterly DevRel-revenue number reads 2-4 quarters stale. Fine — if the sheet says so and carries leading indicator.

# The play

Do not refuse the revenue number. CRO will have one either way — program measured by sales gets revenue-adjacent number assigned. Proposing honest version beats having dishonest one assigned.

You keep delivering quarterly number to QBR. Change what it may claim: **DevRel-influenced pipeline, under written rule, fixed for fiscal year.** Restate the $1.2M once, under that rule, as baseline.

Pitch to CRO, one breath:

> "You keep a quarterly number. To survive Sales claiming the same deals, it says influenced, not sourced, under a rule fixed for the fiscal year — same math every quarter, auditable down to each touch. Last quarter's $1.2M restates to $X under it. Here's the number that reads inside the quarter while pipeline matures."

# Assumptions (normally confirmed one question at a time)

- Funded driver: sales enablement — workshops fill enterprise funnel. CRO's words. If real driver is "all of them," sponsor problem first: route to devrel-strategy, no sheet yet.
- Reader: CRO at QBR, decides budget. Promotes business impact to primary.
- Data in hand: CRM (opportunities, stages, values), workshop attendance lists (email, account, date). Sales-ops cooperation unconfirmed — CRO's own demand is the leverage.
- Stage 2 = qualified. Confirm; rename in rule if not.

Two answers reshaping the sheet: product-usage data joinable to accounts (would add usage-depth metric), sales ops carrying a touch field (refusal deletes influenced pipeline outright — named as deleted, never parked at bottom of sheet).

# Spine

Pick before any metric. Three options:

- **Driver-anchored** — one primary per funded goal. Legible straight to budget line. Hides where developers leak. Recommended: fight is the budget line, and it is the spine CRO already speaks.
- **Journey-stage** — one metric per leak point. Best if question were "where do we lose them." Gives up metric-to-budget line.
- **Function-split** — one number per team member. Gives up causality. Fatal here: causality is the contested thing.

Never stack two spines — double-counts work, doubles sheet.

Tier order for Hollowbrook: business impact promoted ahead of its ratio (reader renews budget). Rest in efficiency order: engagement, enablement, product impact. Reach ships no headline: workshop attendance lives only inside metric 4's story.

---

# The deliverable: measurement framework document

Validate section by section — driver first, then attribution rule. Wrong driver caught at first heading costs a paragraph; at last, the document.

```markdown
# DevRel measurement framework — Hollowbrook, FY26 Q3 onward

## Driver and goals

Funded driver: sales enablement — "workshops fill and accelerate the enterprise funnel."
Owner: CRO (funder), DevRel lead (framework).

Goals this horizon:
1. Prove enterprise influence defensibly — quarterly number that survives Sales.
2. Read the funnel inside the quarter — leading indicator while influenced pipeline lags.
3. Make workshops cause evaluations, not just attendance.

## Metric sheet

| # | Metric | Tier | Owner |
|---|--------|------|-------|
| 1 P | DevRel-influenced pipeline value | Business impact | DevRel lead |
| 2 P | Qualified conversations | Engagement | DevRel lead |
| 3 | Conversation-to-evaluation progression, 90 days | Product impact | DevRel lead |
| 4 P | Workshop-cohort accounts entering evaluation | Enablement | Workshop owner |
| 5 | Evaluations surviving security review | Product impact | Sales eng (DevRel reads) |
| 6 | Self-reported first touch at evaluation kickoff | Engagement | DevRel lead + sales ops |
| 7 | Verbatim evidence | Qualitative | DevRel lead |

### 1 P — DevRel-influenced pipeline value (Business impact)
- Definition: value of opportunities (open + closed-won) whose account recorded
  at least one qualifying touch in the 365 days before the opportunity reached
  stage 2. Qualifying touches: (a) workshop attendance; (b) question answered by
  DevRel in a public community venue; (c) self-reported first touch naming a
  program surface; (d) conversation logged by a DevRel member within 14 days.
  Touch counts only if recorded before the opportunity was created.
- Report shape: value plus raw list — account, opportunity, stage, value, touch
  type, touch date, days before stage 2. List is what survives audit.
- Source: CRM + program touch log.
- Baseline: baselining — restate CRO's quarter under this rule; retro-compute
  two earlier quarters from attendance lists for three periods.
- Threshold: reported, not targeted, for two quarters (baseline). Direction and
  range only after.
- Owner: DevRel lead.
- Action: influenced share leaves trailing band — audit touch-log completeness
  first; report coverage % beside the number every quarter.
- Pre-conditions: sales-ops agreement on touch storage; attendance captured at
  the door (email, account, date); rule signed off before quarter starts.

### 2 P — Qualified conversations (Engagement)
- Definition: per month, conversations with someone who has the problem,
  influences the decision, agreed to a next step. Fixed shape defined before
  the event: account, person, role, venue, next step, date.
- Source: program conversation log.
- Baseline: baselining — backfill three months from calendar + CRM notes,
  marked reconstructed.
- Threshold: set at next review (baseline).
- Owner: DevRel lead.
- Action: two months below band — review venue mix against where last
  quarter's conversations came from; reallocate.
- Role: leading indicator carrying the 8-month pipeline lag. Counter-metric: 3.

### 3 — Conversation-to-evaluation progression, 90 days (Product impact)
- Definition: share of metric-2 conversations whose account opens an evaluation
  within 90 days. Below 30 conversations in period: raw list with dates, no rate.
- Source: conversation log + CRM.
- Baseline: computable from same backfill.
- Threshold: baseline band after backfill; baselining until then.
- Owner: DevRel lead.
- Action: below band — interview five stalled accounts; feed top friction into
  workshop content.

### 4 P — Workshop-cohort accounts entering evaluation (Enablement)
- Definition: per monthly cohort, accounts (not individuals) opening an
  evaluation within 90 days of attendance. Dated list plus count; rate only
  when cohort exceeds 30 accounts. Attendance is reach: never reported alone.
- Source: attendance lists + CRM.
- Baseline: retro-computable for past cohorts from existing attendance data —
  three periods available now.
- Threshold: baseline; direction and range for two cycles.
- Owner: workshop program owner.
- Action: below band — rework evaluation call-to-action and follow-up path;
  interview attendees from stalled cohorts.
- Counter-metric: 5. Entering evaluation is gameable by dragging in-market
  accounts; survival checks quality.

### 5 — Evaluations surviving security/architecture review (Product impact)
- Definition: of evaluations opened by workshop-cohort and conversation
  accounts, share still active or won 30 days after security review starts.
  Raw list at enterprise volumes.
- Source: CRM stages + sales engineering.
- Baseline: baselining.
- Threshold: baseline at next review.
- Owner: sales engineering owns survival; DevRel reads.
- Action: DevRel-sourced evaluations dying at security review above average —
  workshop attracts wrong accounts or evaluation path has friction; hand named
  findings to sales engineering.

### 6 — Self-reported first touch at evaluation kickoff (Engagement)
- Definition: one question asked by AE at evaluation kickoff — "How did you
  first hear about Hollowbrook?" Stable option list, free text kept, one
  question only.
- Source: CRM field.
- Baseline: none — baselining.
- Threshold: none until three periods; report response rate alongside.
- Owner: DevRel lead; sales ops executes.
- Action: response rate collapsing — shorten or reposition question.
- Pre-condition: sales agrees to ask; CRO mandate covers it. Feeds touch (c).
  Read free text quarterly for channels the rule cannot see.

### 7 — Verbatim evidence (Qualitative)
- Definition: quotes from named-account developers (source, date) plus friction
  findings with fix shipped and date. Confidence tag per finding; below 5-10
  independent points, present as hypothesis.
- Source: manual log.
- Baseline: 4 per quarter (baseline).
- Threshold: fewer than 2 (baseline).
- Owner: DevRel lead.
- Action: schedule two account conversations.

## Attribution rule

Fixed for FY26. Any change is an announced restatement, never silent edit.

Methods in use:

1. Influenced pipeline — the quarterly claim. An opportunity is
   DevRel-influenced when, in the 365 days before it reached stage 2, at least
   one contact on the account recorded one of: workshop attendance at a
   program-run event; question answered by the team in a public community
   venue; self-reported first touch naming a program surface; conversation
   logged by a program member within 14 days of happening. A touch counts only
   if recorded before the opportunity was created — touches logged after an
   opportunity exists never count, for anyone. Claim is always "influenced
   pipeline value"; Sales and Marketing may claim the same opportunities.
   Sourced revenue is not something this team measures.
2. Self-reported first touch — standing instrument. Reported as
   "self-reported", never as attribution. Direction and discovery only.
3. Tagged links — per-artifact comparison only, never program totals.

Lookback: 365 days before stage 2 (self-set; covers 8-month cycle plus
pre-opportunity nurture). Stage condition: touch precedes stage 2.
Lookback and windows are self-set conventions, labeled as such if asked.

Stated once, not re-litigated: accounts that engage are already more likely
to buy; the rule cannot separate influence from selection. Read the number
as "engaged accounts that bought", not "deals workshops caused".

Latency: 8-month average cycle means influenced pipeline read this quarter
reflects workshop work from roughly three quarters back. Qualified
conversations and progression carry the interim. Named in every report.

Blind spots the rule cannot see: hallway and word-of-mouth inside accounts;
podcasts; docs and community consumption that never becomes a CRM contact;
partner-channel touches; workshop attendees who change companies.

## Reporting

- Monthly, operational, one page: touch-log coverage, qualified conversations,
  workshop cohort list and progression.
- Quarterly, QBR, decision: full sheet, influenced pipeline with raw
  opportunity list, verbatims. CRO's number lands here, same shape every
  quarter.
- Annually: re-derive sheet from driver; expect half the metrics to change.
- Compare like quarters. Flag workshop-heavy months as bursts, not trends.

Five-sentence summary the CRO can repeat:

"DevRel-influenced pipeline was $X this quarter under the written rule —
same rule every quarter, auditable down to each touch. The $1.2M from the
last QBR restates to $Y under it; the difference is retro-fitted touches and
the word sourced. Workshops put N accounts into evaluation, and M of those
survived security review. Qualified conversations — the number that reads
inside the quarter — were Z against baseline W. Nothing here claims a deal
Sales owns."

## Known blind spots

- No person-to-account identity map for community activity. Building one
  joins public community activity to CRM records — privacy review, hard to
  unbuild. Deliberately deferred. Cost: ~2 engineering days plus review.
- Usage depth inside DevRel-touched evaluations. Promotable if product usage
  data joins to accounts — request goes to devrel-analytics.
- Docs readers who never enter the funnel; partner-influenced deals.
- Influence versus selection unresolvable at our volume. Affordable causal
  check if ever needed: regional holdout on one workshop series. Record
  pre-periods now or the option dies.

## Review

Next review: before the QBR, then quarterly.
Kill rule: any metric that has not changed a decision in two consecutive
cycles is removed at the quarterly review. Scheduled event, not argument.
First kill-check applies after two quarters.
```

---

# Restating the $1.2M

1. CRO first, privately, before QBR slides. Never let him hear it second.
2. One slide, three numbers: $1.2M (post-hoc, sourced) then $X (rule-based, influenced) then delta explained: touches after opportunity creation removed, lookback applied, sourced becomes influenced.
3. One sentence of written agreement on the rule — email fine — before quarter starts.
4. Expect shrinkage. Smaller number you can defend beats bigger number that dies in forecast review. Raw opportunity list is what survives: account, stage, value, touch type, touch date.

# Sequence, first 2 weeks

1. Days 1-2: draft rule, walk it through sales ops. Use CRO mandate as leverage.
2. Days 3-4: restate CRO's quarter under rule; retro-compute two prior quarters. Three baseline periods done.
3. Day 5: stand up touch log + conversation log (fixed shape). Add kickoff question to sales process.
4. Week 2: validate framework sections with CRO — driver, then rule. Then first monthly read.

# Pass check

Framework scores 100% on the skill's threshold:

- ✅ 7 metrics, inside 5-8.
- ✅ Every metric: definition, source, baseline or explicit "baselining", threshold, owner, action.
- ✅ Product/business tier present: metrics 1 (business), 3, 5 (product).
- ✅ No monotonic primary — all period-scoped.
- ✅ "So what" and ownership tests: action named per metric; influenced pipeline reported-not-targeted by design.
- ✅ Attribution rule written: methods named, 365-day lookback, stage condition, "influenced" wherever credit shared.
- ✅ Incentivized volumes paired: conversations with progression (2 with 3), workshop-eval with survival (4 with 5).
- ✅ Thresholds tagged `baseline` or baselining; no folklore number presented as target.
- ✅ Blind spots non-empty.

Stored to project memory (marked pending owner validation). Next concrete step, under two minutes: email sales ops asking for 30 minutes on a CRM touch field — subject "CRM field for the CRO's quarterly DevRel number."