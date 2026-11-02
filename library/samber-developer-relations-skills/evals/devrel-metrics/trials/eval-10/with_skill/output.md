All four reference docs read. Here's the deliverable — my answer as Brackenridge, applying the devrel-metrics skill.

---

**No — don't sign it as drafted. Sign a rewritten version tomorrow.** The metric *families* are mostly right; every *number* is wrong in the same way: all four thresholds are folklore figures presented as industry standards, on a platform three months old with no clean baseline to justify any point target.

## 1. All four numbers are folklore, not standards

| PM's OKR | Claimed basis | What it actually is |
| --- | --- | --- |
| 40% seven-day retention | "industry standard" | Round number circulating from talks and blog posts. No measurement behind it, no named publisher. |
| 20% monthly-active ratio | — | Same. A canonical folklore figure. |
| 30% self-serve activation | "typical for devtools" | Sits inside the "20–40%" band that circulates widely — practitioner claim, not study. Order-of-magnitude context at best. |
| First response < 24h | — | The only vendor-neutral publisher in this space (CHAOSS) deliberately sets **no numeric target** for any of its metrics. The "two business days" people quote is VMware's internal guideline, from a case study. 24 hours is even less anchored. |

Why refuse rather than shrug: a borrowed benchmark gets checked exactly once. The moment someone asks *"whose standard?"* and the answer is nobody's, they doubt every other number on the page — including the honest ones. Worse: at quarter-end you're graded against figures nobody derived from your product, your audience, or your three months of history. "Industry standard" for retention doesn't exist; benchmarks against another company's absolute numbers are meaningless anyway — audience, ecosystem and maturity change what normal looks like.

## 2. You have no baseline — and the history you do have is launch noise

- Threshold rule: **three prior periods before any target.** Without history, ship the metric marked "baselining" and set its threshold at the next review.
- You have ~3 monthly cohorts, but they're the *launch quarter*. Launches spike everything; treating launch-month cohorts as your baseline is this field's most common false trend.
- First two cycles: targets as **direction and range** ("from 22% into the 28–33% band"), never a point. Point targets only once the baseline is stable.
- Cohort **monthly, never daily** — daily cohorts at your volume are single digits, and every retention curve drawn from them looks flat regardless of what happened.

## 3. What the draft gets right

Keep the skeleton. Activation is the enablement tier — the thing DevRel most directly owns and moves. Retention is product impact — it satisfies the "at least one product/business-impact metric" rule. Community responsiveness is engagement. That mix is defensible for a self-serve devtools platform. The rewrite keeps all four families and fixes definitions, thresholds, owners.

## 4. The rewrite — what I'd sign

Every metric needs six fields: definition, source, baseline, threshold, owner, action. Today's draft has zero of them.

1. **7-day retention.** Freeze the definition of "active" in writing *before* the quarter starts — a rule invented after the quarter is a narrative, and a hard 40% target plus definitional freedom buys you "active" being defined downward by March. Compute the actual monthly-cohort number tonight. Lock: "into a band vs launch quarter; threshold set at first monthly review." The 40% goes on the sheet tagged `hypothesis`, or not at all.
2. **Monthly-active ratio.** Same treatment, plus: define the unit first — developer or account? API call or login? Each choice moves the number by tens of points, and the 20% figure is meaningless until "active" is pinned.
3. **Self-serve activation.** The one to invest in. Define one instrumented success event, in writing — e.g. "first successful authenticated API call within 7 days of signup." If that event isn't instrumented yet, this OKR is an *instrumentation request*, not a target; the blocking work is the event, not the number. Cite the 20–40% band as context only, target from your own first months.
4. **Community first response.** Measure the trailing median before setting anything. If it's 31 hours, "under 24" is a defensible stretch; if it's 6, the OKR is trivia. Small-N warning: below ~30 questions per period, report the raw list with dates, not a rate. And pair the speed target with a quality counter (share of questions *resolved*, not merely answered) — a response-time target alone buys fast, shallow answers.

Add what's missing entirely: **a named owner and a named action per OKR.** A metric with no action attached gets cut, not kept.

## 5. Tomorrow, concretely

- Pull the four actual numbers tonight — retention by monthly cohort, MAR, activation rate if the event exists, median first-response hours. Roughly an hour if telemetry is in place.
- Numbers exist → lock direction-and-range targets derived from them, each tagged `baseline`.
- They don't → lock definitions plus an instrumentation plan, mark all four "baselining," thresholds at the first monthly review. That is still a signable OKR — and the honest one.
- One ownership question to settle with the PM: 7-day retention is substantially product-owned. DevRel's movable lever inside one quarter is activation and time-to-first-success. If you co-sign a retention number, make activation *your* primary and report retention alongside it.

The line to give her: *"I'll sign tonight — same four metrics, targets derived from our own trailing months, thresholds locked at first review. I won't sign 'industry standard' numbers, because they aren't, and next quarter's us gets graded against them."*

One caveat that would change this advice: if this OKR sheet is what renews the DevRel budget or it's funded from a sales/marketing line, the sheet is also missing a business-impact row (influenced pipeline under a written rule, explicitly shared credit) — tell me who reads these numbers and I'll extend it.