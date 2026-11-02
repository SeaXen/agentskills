# Budget defense case: worked example

Fictional: a developer database company. The CFO proposes cutting the DevRel program 40% in the annual plan. Program cost $620k a year, salaries in. A cut list exists from the budget allocation, ranked by return per dollar. Review in three weeks; support and sales leads have agreed to answer.

## 1. Results table (goal-ledger spine, framework metrics)

Goal-ledger spine because this CFO builds the plan from company goals; a bet portfolio fits a line-by-line review.

| Company goal                       | Metric                                                                | Last 4 quarters | Label                         |
| ---------------------------------- | --------------------------------------------------------------------- | --------------- | ----------------------------- |
| Self-serve revenue +30%            | developers in DevRel-touched cohorts reaching first success per month | 410 → 690       | influenced (touched cohort)   |
| Support cost flat while users grow | tickets per 100 new signups                                           | 14 → 9          | measured                      |
| Enterprise pipeline                | pipeline influenced, 180-day rule                                     | $1.1M           | influenced, shared with sales |

## 2. Tiered cut scenarios (cumulative prefixes of the cut list)

Ranked cut list: 1) two sponsored conferences $80k, 2) swag and travel $44k, 3) contract video producer $90k, 4) community manager role $110k. Items 3 and 4 share no dependency; item 4 runs the forum the support dependency below rests on.

| Tier        | Lines cut          | Share of $620k | What stops                             | Metric expected to drop                                                                   | Reversible                                    | Savings land                            |
| ----------- | ------------------ | -------------- | -------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------- |
| A           | 1-2                | 20% ($124k)    | two conferences, swag, most travel     | DevRel qualified leads, about a quarter of them (estimate, from last year's lead sources) | yes, next sponsorship cycle                   | as contracts would have been signed, H1 |
| B           | 1-3                | 35% ($214k)    | above, plus produced video             | tutorial video output; first-success effect unknown                                       | yes, contract notice period                   | from contract end                       |
| 40% request | 1-3 plus part of 4 | 40% ($248k)    | above, plus the community manager role | forum first-response time; tickets per 100 signups likely rise                            | no: re-hiring and ramp take a quarter or more | from the exit date, minus severance     |

The 40% request lands $34k past tier B, inside a headcount line: the real decision is whether to remove the community manager role.

Recommendation: tier A. It cuts the lines with the weakest return and keeps every line that holds up a row of the results table.

## 3. Cost per outcome

- Cost per developer reaching first success: $620k / 6,600 a year in DevRel-touched cohorts = $94 (influenced, touched cohort, salaries in), against $210 per first success from paid acquisition (growth team, last two quarters, media plus that team's salaries).
- Support cost avoided: 5 fewer tickets per 100 signups × 21,000 signups × $28 per ticket = about $29k a year (modeled, unit cost agreed with finance from support's cost per ticket). Shown as avoided cost, never as revenue.

## 4. Dependency inventory (confirmed in writing)

| Team    | What it uses from DevRel                    | What happens if it stops                                                     | Confirmed by                   |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------ |
| Support | forum answers, error-reference pages        | about 1,000 extra tickets a year routed to support (support lead's estimate) | support lead, email 3 March    |
| Sales   | technical workshops for evaluating accounts | 2 open evaluations lose their technical sponsor (VP sales' estimate)         | VP sales, Slack thread 4 March |

A dependency the owning team has not confirmed stays out of the case.

## 5. Decision asked

Approve tier A (20%) instead of 40%. Options: tier A, tier B, 40%. Recommendation: tier A - it keeps the community manager role behind the support numbers in the results table, and the remaining events line gets its own Q2 read against its threshold, with a further cut there if it misses. Needed by the plan lock, 21 March.

## What the weak version looked like

```
// ✗ Weak - pleads, cannot be checked, offers nothing
DevRel is a long-term investment that is hard to measure. Cutting it would hurt our
community and brand. Industry benchmarks show programs our size spend more.

// ✓ Strong - tiers, numbers with labels, other teams vouching, one decision
A 20% cut stops two conferences and keeps docs and community, the two lines active
while first success grew (410 → 690 a month, influenced, touched cohort). Support and
sales confirmed in writing what a 40% cut breaks. Decision asked: approve 20%, by 21 March.
```
