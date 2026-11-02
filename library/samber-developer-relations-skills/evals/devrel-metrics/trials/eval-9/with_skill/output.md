# DevRel measurement framework — Saltmarsh Data, 2026 H2 → Q1 2027

Built per the `devrel-metrics` skill. Everything below is the deliverable; three assumptions gate it and are listed at the end for confirmation at the first monthly read. Nothing in the structure changes if the wording of your charter goals differs — only the labels on the two primaries.

---

## The spine call (decide this before trusting the sheet)

You asked for two views: AAARRRP-stage tracking **and** a developer drop-off map. The skill is explicit: never stack two spines — a sheet carrying both AAARRRP goals *and* journey stages as separate metric sets double-counts the same work and doubles the sheet. You get both views from **one sheet, two readings** instead.

| Spine | Makes visible | Hides | Legible to | Wrong pick when |
| --- | --- | --- | --- | --- |
| **Driver-anchored (AAARRRP)** — one primary per funded goal | line from metric to budget line | work that serves no named goal | the funder who wrote the charter | charter names no goals |
| **Journey-stage** — one metric per leak stage | where developers drop off | which goal the fix serves | product/funnel owners | nobody has named the goals |
| **Function-split** — one metric per person | individual ownership | cross-function causality | the team itself | three people, three silos |

**Pick: driver-anchored.** Your charter already names two funded goals — the strongest signal there is. The drop-off view is served three ways without a second spine:

1. Every metric carries an **AAARRRP stage label** (a label, not a second metric set).
2. Row 2 *is* the drop-off metric — step-level abandonment inside activation.
3. The quarterly **journey read** (Reporting section) plots stage-to-stage conversion from the same logged data the sheet already reads.

The function-split's real appeal — each of your three people owning a number — is absorbed by the **Owner** column: docs owns 3 rows, the advocate 3, the community manager 1, one shared.

---

## 1. Driver and goals

- **Funded driver (confirm wording):** developer adoption — more developers building on Saltmarsh and staying. Owner: whoever holds the charter budget (name to be filled in).
- **Goal 1 (primary, Activation):** raise the share of new developers reaching first success on their own data.
- **Goal 2 (primary, Retention → Referral):** raise the share who stay active and start a second project.
- Each goal traces to a journey leak: Goal 1 → activation drop-off; Goal 2 → retention/referral drop-off.

Tier re-ranking that shaped this sheet: the build-this-week deadline promoted engagement and enablement (already collectable); unconfirmed sales-ops cooperation **deleted** business impact outright (blind spots, not bottom-ranked); the one engineering ask is reserved for the success event, the best value-per-effort on the ladder.

## 2. Metric sheet

**Pre-conditions** (stated before any row ships):

- One instrumented `first_success` event in product analytics — the single engineering ask this framework makes. Without it, rows 1–3 and 7 are instrumentation requests to `devrel-analytics`, not metrics.
- Access to the docs search log, the community export, the forge API, and an editable signup form. All assumed present; all cheap.

| # | Metric | Tier | Stage | Definition | Source | Baseline | Threshold | Owner | Action if breached |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 **P** | First-success rate, 14 days | Enablement | Activation | share of new signups triggering `first_success` (first query/pipeline run on data they connected, returning results) within 14 days of signup | product analytics | baselining from Oct 2026 | direction: up. Band set at Jan 2027 review `(baseline)` | docs | cold-run the getting-started path monthly; fix the worst failing step before any new content ships |
| 2 | Step drop-off, getting-started path | Enablement | Activation | share of starters abandoning at each documented step, monthly | product + docs analytics | baselining | set at Jan 2027 review `(baseline)` | docs | fix the single worst step, re-run, re-measure |
| 3 **P** | 30-day retention, first-success cohort | Product impact | Retention | share with ≥1 success event in days 22–30 after first success, monthly cohorts | product analytics | baselining | set at Jan 2027 review `(baseline)` | advocate | interview five lapsed developers before proposing any fix |
| 4 | Docs searches with zero results | Engagement | Awareness → Acquisition | monthly count plus top-10 terms | docs search log | baselining; term list useful day one | every top term enters the content backlog; count threshold at review `(baseline)` | docs | top three missing terms become the next three content items |
| 5 | Median time to first human response | Engagement | Engagement | median hours to first non-staff, non-bot human response on developer questions, community + repo issues | community export + forge API | baselining | `(hypothesis)` "2 business days" is VMware's internal guideline quoted in a CHAOSS case study, not a CHAOSS target; test against own trailing median, replace after 3 periods | community | weekly triage of everything unanswered >7 days; if this ever becomes a target, pair with a solved-rate counter-metric to prevent premature shallow answers |
| 6 | Self-reported first touch | Engagement | Awareness | distribution of the one signup question, stable option list, free text kept | signup form | baselining | response rate below 40% `(hypothesis — circulating figure, unmeasured)` → reposition the question | advocate | read free text quarterly for channels the list missed |
| 7 | Second-project rate, 90 days | Product impact | Referral | share of first-success developers starting a second project or integration within 90 days, monthly cohorts | product analytics | baselining | set at Jan 2027 review `(baseline)` | advocate | interview second-project developers for blockers; below ~30 events/period report the raw list, not a rate |
| 8 | Verbatim + friction log | Qualitative | Product | quotes and cold-run/support friction findings with source, date, confidence tag, and fix shipped | manual log | baselining; aim 4 entries/quarter | fewer than 2 entries in a quarter `(baseline after first full period)`; each finding tagged high/medium/low confidence; <5 independent data points = hypothesis, not conclusion | all three, rotating | schedule two developer conversations |

Guardrails: cohort monthly, never daily. No cumulative counts anywhere (monotonic test). No absolute traffic numbers across sources — client-side analytics misses most of a developer audience (Plausible measured 58% blocking GA on a tech audience, Aug 2021 — directional), so reach reads as ratios inside one source. A launch or conference month is labelled as a burst, never drawn as a trend.

## 3. Attribution rule

Written now, before the period starts; held constant through 2027.

- **Self-reported first touch** (row 6) is the standing instrument. It may claim direction and channel discovery only — reported as "self-reported", never as attribution. No lookback: asked once at signup. Option list frozen across quarters; free text read quarterly.
- **Tagged links** compare artifacts only (two landing pages, two posts), never program totals. One tag per campaign, never reused; a 4-week pre-period recorded on the destination before any push, or no lift may be claimed.
- **Pre/post lift** reserved for one bounded push per half — first candidate: the getting-started rewrite. Claim direction and rough magnitude; no point estimates with decimals.
- **No revenue claims this year.** Influenced pipeline is deleted, not parked: reinstating it requires a CRM touch field, sales-ops cooperation, and this written rule — 180-day lookback before stage 2, "influenced" never drops, shared credit with Marketing, fixed for the fiscal year, any change announced as a restatement.

A large "direct" bucket is normal (~70% of AI-assistant traffic arrives with no referrer — one newsletter's figure, directional). Two teams never claim the same revenue as sourced.

## 4. Reporting

- **Monthly, operational** (team only): rows 1, 2, 4, 5 on one page with trend lines. First read late October 2026.
- **Quarterly, decision** (charter owner + exec): full sheet, qualitative log, and the **journey read** below. First: early January 2027 — this review sets every threshold marked baselining.
- **Annually:** re-derive the sheet from the driver; expect half the metrics to change.

**Journey read** (the drop-off map — same data, second view):

| Stage | Monthly logged count (context) | Conversion from prior stage | Sheet row explaining it |
| --- | --- | --- | --- |
| Awareness | docs/blog ratios within one analytics source | — | 6 |
| Acquisition | signups; % naming a program surface | visit → signup | 6 |
| Activation | `first_success` count | signup → success | **1, 2** |
| Retention | active at day 30 | success → active | **3** |
| Referral | second projects; non-staff answer share | active → second project | 7, 5 |
| Revenue | — | — | deleted (see blind spots) |
| Product | friction findings shipped to roadmap | — | 8, 4 |

**Five-sentence summary the funder can repeat:** "Developers who sign up reach first success [X]% of the time within two weeks, and the step map shows the leak is at [step]. Of those who succeed, [Y]% are still active at 30 days and [Z]% start a second project within a quarter. We know where they come from because we ask one question at signup and publish the method. We claim no revenue this year; the written conditions for an honest influenced-pipeline number are in the framework. Everything else we publish is an input to those numbers, not a result."

**Kill rule:** any metric that has not changed a decision in two consecutive quarterly cycles is removed at the next review. Stated here so removal is a scheduled event, not an argument.

## 5. Known blind spots

- **Influenced pipeline — deleted.** Needs a CRM touch field (~2 engineering days), a standing sales-ops contact, and fiscal-year rule discipline. Promote ahead of its ratio only if the budget sits on a sales or marketing line — that is the one confirmation that would change this sheet's shape.
- **Anonymous docs readers.** No identity link between docs reading and signup; docs impact reads as within-source ratios only.
- **Word of mouth and dark social** are invisible except through the signup question.
- **Source decay.** Forge traffic endpoints keep 14 days — snapshot monthly from day one or the history is gone; export community and search data monthly.
- **Referral stage is thin** until second-project cohorts accumulate; read row 7 as a raw list through 2026.

## 6. Review

- Monthly reads: late Oct, Nov, Dec 2026. Threshold-setting review: early Jan 2007 **[sic — 2027]**, after three baselining periods.
- Kill-rule status: all rows cycle 1 — nothing eligible yet.
- Next driver re-derivation: October 2027.

---

## Confirm at the first monthly read (assumptions this was built on)

1. Charter's exact goal wording and the budget-holder's name (swaps labels, not structure).
2. Whether sales-ops will share pipeline data — the only answer that reinstates a business-impact row.
3. That one engineering day exists for `first_success` — if not, rows 1–3 and 7 move to a `devrel-analytics` request and the sheet runs on 4, 5, 6, 8 until it lands.

## Pass-threshold check

✅ 8 metrics (within 5–8) · ✅ all six fields per row, baselines explicitly marked "baselining" · ✅ two product-impact rows · ✅ no monotonic primary · ✅ action attached to every threshold (so-what and ownership tests pass) · ✅ attribution rule written, methods named, lookbacks stated, "influenced" framing in the reinstatement clause · ✅ counter-metric on the one speed-gamable metric (row 5) · ✅ every threshold tagged `baseline` or `hypothesis`, folklore named as folklore · ✅ blind-spots section non-empty.