## Before the numbers: one thing to flag

This is the third time "Meridian Stack" and this exact five-number report have come up. Three days ago (2026-09-20) I built a different replacement for the same VP challenge — an outcome framework organized around five leadership questions, with "weekly active developers" as a north star and October designated as the baseline month. If that one already went out or is already in motion, sending a second, differently-structured framework next month will confuse the VP more than the original five vanity numbers did. Tell me which one to actually ship — the two overlap enough (both cut stars/followers/downloads-as-vanity, both lean on activation + retention, both need a 3-4 week instrumentation runway) that I'd merge them rather than run both, and I've noted below exactly where they'd merge.

The framework below was built with the `devrel-metrics` skill's method (tier ladder, journey spine, written attribution rule) rather than freehand, which is why it looks more structured than a typical monthly report — that structure is what survives the next "what's this for."

## Assumptions I made without an interview

The skill this is built from normally interviews you one question at a time before touching a metric. Since you asked for the finished deliverable, I answered those questions myself from context and flagged every guess. Correct any of these before you send:

- **Funded driver: developer adoption**, not sales enablement — inferred because your VP of *Engineering* is the reader, not VP Sales or Marketing.
- **Adoption shape:** self-serve entry (npm install, signup) with a possible sales-assisted enterprise tier — typical for infra, unconfirmed.
- **No CRM/sales-ops cooperation confirmed.** I did not build "influenced pipeline" into the sheet because of this (see Attribution rule). If sales-ops will actually give you a touch field on opportunities, that changes row 6.
- **No product-analytics instrumentation exists yet** for activation/retention (no `first_success` event). I've marked those rows "baselining" rather than inventing a number.
- **Solo or near-solo DevRel function**, no confirmed engineering days on tap — the instrumentation plan below assumes you're negotiating for ~1-2 eng days, not a sprint.

## Spine: journey-stage, not driver-anchored

Two spines fit a first framework like this one; I ruled out function-split outright since you're running this solo.

| Spine | Makes visible | Hides | Wrong pick when |
|---|---|---|---|
| **Driver-anchored** (one metric per AAARRRP goal) | Direct line from metric to a named business goal | Doesn't show *where* in the funnel developers drop | You already have a charter naming 2-3 funded goals |
| **Journey-stage** (one metric per stage developers leak at) | Exactly where adoption breaks — the question "what's this for" is really asking | Cross-team causality; less legible if the reader thinks in OKRs, not funnels | The team is staffed by function, not by stage |

**Recommendation: journey-stage.** Your VP's actual question — "what is any of this for" — is a leak question, not a goal-alignment question. A funnel (aware → install → first success → still-using → paid-influence) answers it in one sentence: "here's where we lose people, and here's what we're doing about that step." Driver-anchored would require naming a charter that doesn't exist yet.

---

# DevRel measurement framework — Meridian Stack, Q4 2026

## Driver and goals

**Funded driver:** developer adoption — assumed from VP Engineering ownership, confirm before sending.
**Owner:** you, DevRel.
**Goals this horizon (one per journey stage that matters, capped at three):**
1. Raise the share of installs/signups that reach a real first success.
2. Keep developers who succeed once still running Meridian Stack a month later.
3. Give the business an honest, non-inflated number for what DevRel routes toward revenue.

## Metric sheet

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|---|---|---|---|---|---|---|---|
| 1 **P** | First-success rate, 14 days | Enablement | Share of new npm installs/signups reaching one specific, pre-agreed success event (e.g. first successful API call or first deployed instance) within 14 days | Product analytics, `first_success` event — **pre-condition: event must be instrumented, does not exist yet** | baselining | Set after 3 monthly reads (baseline) | You, + 1 eng day from platform team | Cold-run the quickstart yourself, fix the top failing step before new content ships |
| 2 | Monthly npm downloads, paired with unique dependents | Engagement | Downloads in the period (not cumulative), alongside count of unique packages/repos declaring it as a dependency | npm registry API (weekly pull) + GitHub dependency graph | Pull last 3 months now — npm keeps this history | Flag if month-over-month change exceeds ±15% with no known cause (baseline) | You | Cross-check against dependents count before reacting — npm counts HTTP 200s, CI and mirrors included, not people |
| 3 | Time to first response, GitHub issues/PRs | Engagement | Median hours from an issue/PR opening to first *human* response, bots excluded (CHAOSS Starter Project Health definition, adopted verbatim) | GitHub API — 14-day retention window, snapshot monthly from now on | Pull what's available now | Flag when trailing median exceeds 2× its own rolling average (baseline) — **not** "24 hours" or "2 business days," both are someone else's folklore, not a target | You + eng on-call | Add a triage rotation or a bot-assisted first response |
| 4 **P** | 30-day retention of the first-success cohort | Product impact | Share of the cohort from row 1 still active (weekly call/install) 30 days after their first success | Product analytics, same event as row 1 | baselining — needs row 1 shipped, expect a real number ~10-12 weeks out | Set at first real reading | You + Product | Interview 5 lapsed accounts before proposing a fix |
| 5 | Qualified conversations logged | Engagement | Conversations meeting a fixed bar (has the problem, influences the decision, agreed a next step), logged per event with company + next step | Manual log, bar defined in writing before the next conference | 0 — new log starting this quarter | Below-30/period: report the raw list, not a rate (small-N floor) | You | A conference producing zero logged conversations twice running is cut from next year's list |
| 6 **P** | DevRel Qualified Leads routed | Business impact | Connections passed to another team (sales, product, recruiting, partnerships), receiving team named, logged per period | Manual log, fed by row 5 | baselining | No volume target in period 1; reviewed quarterly for pattern. **Counter-metric:** % the receiving team confirms as useful | You | If receiving teams confirm <50% as useful, tighten the routing bar |
| 7 | Qualitative evidence | — | Verbatim developer quotes + friction findings, with source, date, confidence tag (high/med/low by independent-source count), and the fix shipped | Manual log from support threads, cold runs, community | 0 — new row | Fewer than 2 per period (baseline) | You | Schedule developer interviews |

Rows 1, 4, 6 are the primaries — one per goal. Every threshold is tagged. Nothing here is a cumulative total: stars, follower count and cumulative npm downloads are gone as goals (see below).

## Attribution rule

- **Self-reported first touch** — not yet standing. Add "How did you first hear about Meridian Stack?" to the signup flow (stable option list, free text kept). Reported as "self-reported first touch," never as attribution.
- **Tagged links** — per-conference, per-post short links, compared artifact-to-artifact only, never summed into a program total.
- **Influenced pipeline — deliberately not adopted this cycle.** No confirmed CRM touch field, no confirmed sales-ops cooperation. Row 6 (DevRel Qualified Leads routed) stands in as the honest, loggable alternative — this is Mary Thengvall's position: a program reporting to Engineering, not Sales, shouldn't invent a revenue number it can't defend. **If you can get 10 minutes with sales-ops and they'll add a touch field, this changes** — replace row 6 with influenced pipeline under a written 180-day lookback rule.
- **Pre/post lift** — reserved for one bounded push next quarter (e.g. a quickstart rewrite). Record the pre-period now, before touching anything.

**Blind spots this rule cannot see:** word-of-mouth inside a company; docs read without a signup; AI assistants answering from your docs with no visit at all (directionally, ~70% of AI-assistant traffic arrives with no referrer — Demand Curve, one newsletter's figure, treat as directional); anything reaching an enterprise buyer through a partner; enterprise pipeline DevRel actually influenced (undercounted until the CRM question above is resolved).

## Reporting

- **Monthly** (operational): rows 1-3 and 5 to yourself/product, one page, trend against baseline.
- **Quarterly** (decision): full sheet + qualitative evidence to VP Engineering.
- **Annually**: re-derive the whole sheet from the driver; assume half the rows change.

**Five-sentence summary for the VP:** "We're replacing five totals that only ever went up with a funnel that shows where developers actually drop off. Right now we don't yet know our first-success rate — that's the first thing we're instrumenting, and it's the number this whole sheet hangs off. Everything old (stars, followers, cumulative downloads) is now context, not a goal, because a number that can't fall can't tell you anything moved. We're not claiming sourced revenue; we're logging what we hand to other teams and checking whether they found it useful. This report will look thinner in October than September's — that's the baseline month, not a step backward."

## Known blind spots

- No activation/retention data exists yet — the two primary rows (1, 4) start empty. This is the honest cost of not having had a success event defined before now.
- No CRM cooperation confirmed — business impact is capped at "leads routed," not revenue influenced, until that changes.
- Docs analytics (search terms with no result, step-level drop-off) aren't in this sheet at all — you likely don't have docs search logs yet; that's a `devrel-analytics` instrumentation request, not a metric to fake here.

## Review

Next review: **2026-10-31** (end of the baseline month). Kill-rule status: every row is cycle 0 — none has had the chance to earn or fail the "hasn't changed a decision in two cycles" test yet.

---

## Pass-threshold check (self-graded against the skill's own bar)

- Metric count 5-8: **7. Pass.**
- Six fields per metric: **Pass**, all present in the table.
- At least one product- or business-impact metric: **Pass**, rows 4 and 6.
- No monotonic primary: **Pass**, primaries are a rate, a cohort-retention share, and a logged count-per-period.
- "So what" + ownership test per metric: **Pass**, every row names an action inside your or your immediate partners' control.
- Attribution rule written, names methods + lookback, uses "influenced" only where credit is shared: **Pass** — and it explicitly does *not* claim influenced pipeline this cycle, which is the honest call given unconfirmed sales-ops access.
- Every incentivized volume metric has a counter-metric: **Pass**, row 6 paired with the "% confirmed useful" check.
- Every threshold tagged sourced/baseline/hypothesis: **Pass**, no folklore numbers presented as targets.
- Blind-spots section non-empty: **Pass.**

## What actually needs to happen before October 31

1. **Week 1:** Get 1 eng day to instrument one `first_success` event — pick the single action that means "this person is actually using the product," not just installed it. Start the qualified-conversations log and the DevRel-Qualified-Lead log (both are just spreadsheets).
2. **Week 2:** Add the one-question "how did you hear about us" to signup. Pull the last 3 months of npm downloads, dependents, and GitHub response-time data — all available today, zero eng cost.
3. **Week 3:** Sit down with the VP specifically on the revenue-metric question (influenced pipeline vs. DevRel Qualified Leads) — this is a 15-minute conversation that determines row 6 for the next year, don't guess it twice.
4. **Week 4:** Send the transition report — real numbers for rows 2 and 3, "baselining" honestly labeled for 1, 4, 6, and 7.

This is the report that survives the next "what is this for" — because the answer is now in the sheet itself, not in the room after the VP asks.