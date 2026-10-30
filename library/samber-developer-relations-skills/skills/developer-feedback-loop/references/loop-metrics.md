# Loop metrics

Read this before Step 1 (the leak trace) and Step 7 (the metric sheet).

## Contents

- Leak trace sheet
- Metric definitions
- What the evidence supports
- Statistics not to cite

## Leak trace sheet

Sample 20-30 requests from the last 60-90 days, at least three per channel, then fill the rest in proportion to each channel's volume. Take the most recent requests in each channel rather than memorable ones: memorable requests are the ones that already got attention. Keep duplicates in the sample and mark them - the duplicate rate is itself a finding. One row each.

- **Captured:** written anywhere durable beyond the original message (a ticket note, a direct message to a PM, an issue). With no record system yet this is still measurable, and usually low.
- **First human reply:** from staff. Peer answers are healthy community behaviour, but they are not the loop. Leave the cell empty for channels with no reply step (a sales call) and for requests nobody answered, and count the unanswered ones separately.

| # | Channel | Date asked | Captured in a record? | Reached product (agenda, comment, ticket)? | Decision recorded? | Requester told? | Days to first staff reply |
|---|---|---|---|---|---|---|---|

Read it as a funnel: captured ÷ asked, reached ÷ captured, decided ÷ reached, told ÷ decided. The stage that loses the most requests is the one to fix first. A "told" rate near 100% usually means only channels with a built-in reply path (public issues, an account manager) reached a decision at all - read it as a symptom, not a strength. A team losing most requests at capture needs capture rules, not a product council; a team whose requests reach product and then sit undecided needs the contract, not a new tool.

With fewer than 20 requests in 90 days, skip the ratios and read the rows; percentages on a dozen items are noise.

## Metric definitions

Keep three to five. Each has a definition, an owner and the action it triggers.

| Metric | Definition | Owner | Action when it slips |
|---|---|---|---|
| Time to first staff reply | feature request asked → first reply from staff (bots, auto-replies and peer answers excluded), median and 90th percentile | DevRel | rebalance the capture rota or shorten the promise |
| Capture rate | requests linked to a record within the capture window ÷ requests asked (from a quarterly re-trace) | DevRel | tighten the capture rule for the leaking channel |
| Decision rate | reviewed records leaving the review with a status ÷ records on the agenda | product | raise in the contract review; shrink the agenda |
| Closure rate | status changes communicated to requesters in their channel within the reply window ÷ status changes | DevRel, support | add the reply to the review's last agenda item |
| Shipped-from-feedback | changes shipped in the period that trace to a record, with the record linked in the release note | product, DevRel reports | none - it is the outcome line for the quarterly report |

Shipped-from-feedback needs an attribution rule written before counting: a change counts when a record existed before the work was scheduled and is linked from the release note. Without the rule, every shipped feature gets claimed.

Volume of feedback collected is not on the list. More requests is not better or worse by itself, and a sheet that celebrates volume rewards over-capture.

## What the evidence supports

- **First response is the only loop metric with even correlational outcome evidence.** In open-source pull requests, newcomers who got a first human response within a day continued contributing at a median 15.14% higher relative rate than those answered later - roughly 5-6 percentage points on a base near 40% (Hasan et al., MSR 2023, 111,094 PRs across 10 projects). The effect on existing contributors was small, the study is observational, and it measured code contributions, not feature requests - treat it as direction, not a target.
- **Bots do not count.** In a 50-PR manual sample from the same study, 35 of the first responses arriving within ten minutes were bots; bot response time explained 0.33% of pull-request lifetime variance against 64.7% for human response time. CHAOSS's time-to-first-response definition excludes bots.
- **Closure is widely skipped.** In a 2022 product-management survey run by a feedback-tool vendor and Product Collective (1,400+ respondents), 54% said they lack an effective system for updating customers on past requests.
- **No published benchmark exists for capture rate, decision rate, closure rate or shipped-from-feedback.** Vendor targets (for example "80% triaged within 48 hours") are opinions. Set targets from the team's own leak trace and label them self-set.

Starting targets this skill sets, to replace with the team's own trend after a quarter:

- capture window: 2 business days
- requester told: within 5 business days of a status change
- decision rate: every agenda record leaves with a status, revisit allowed twice

## Statistics not to cite

- "95% of companies collect feedback, 10% act on it, 5% tell customers" - credited to Gartner in a vendor deck from around 2010 that carries only the 95% and 10% parts; the 5% leg appears later on vendor blogs, and no Gartner source for the three-part figure is public.
- Precise churn or retention lifts from closing the loop quoted by feedback vendors - their own pages disagree with each other.
