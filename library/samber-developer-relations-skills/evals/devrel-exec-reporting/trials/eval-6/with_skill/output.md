# DevRel Quarterly Report (Q3, assumed) for the CTO

I followed `devrel-exec-reporting`. Two of your additions did not make the page, and the draft contains gaps only you can fill.

## Why the two additions are not in the body

- **Community sentiment score.** Your January framework doesn't contain it, and the skill never lets a report add a metric. A score invented this morning, with no baseline and no written rule, can't be compared with any earlier period. Averaging Discord emoji reactions also measures who reacts, not how the community feels. Mixed emoji have no agreed value, and there's nothing to compare against. If you want it, take it to `devrel-metrics` and baseline it for a quarter. I listed it as a next-period commitment below.
- **Blog pageviews (180k).** This is a reach figure, not an outcome for a CTO. Its label would be "measured (analytics)", and the skill puts activity and reach counts in the appendix only. I put it on the appendix count line and nowhere else. Adding it to the table would invite the question "what did it move?", and the report has no answer.
- **A thin page.** Four framework metrics, a miss and a decision make a complete page. Padding it would weaken the report.

## Assumptions to check before sending

1. The reader is the CTO, so I used the **developer funnel** spine. The skill recommends it for a CTO. I didn't have time to offer alternatives.
2. The period is "Q3". Fix the label.
3. No threshold or target was given for time-to-first-call or shipped features, so those rows carry no status. I won't invent a status colour.
4. No cost, salary basis or attribution rule was given, so the cost section is a gap, not a figure.
5. You gave no decision, so I drafted one. Replace it if you had another in mind.
6. I assumed no metric was dropped since January.
7. The "Likely cause" and "What changes" cells for the SDK miss are marked `[you fill]`. I won't guess at causes.

---

# DevRel - Q3 - for the CTO

Median time to first successful API call fell from 22 to 14 minutes, and 6 community-requested features shipped. SDK issue response, at 78%, is 2 points under its 80% threshold.
**Decision asked:** <decision below>, by `<date>`.

## Results table (developer funnel)

| Funnel stage | Metric (framework) | This period | Baseline / threshold | Status | Label |
| --- | --- | --- | --- | --- | --- |
| Onboarding | Time to first successful API call, median | 14 min | 22 min (prior period) / no threshold set | none, no threshold | measured (product analytics) |
| Support | SDK issues answered within 2 business days | 78% (`[n answered / N total]`) | threshold 80% | yellow | measured (issue tracker) |
| Product feedback | Community-requested features shipped | 6 | no baseline given | none, no baseline | measured (issue tracker) |
| Business impact | Pipeline influenced | $260k | `[prior period]` | none, no baseline | influenced (`[N]`-day rule, shared with sales) |

- **Time to first call:** this is co-movement, not a causal claim. The metric moved while `[quickstart / docs change, if any]`. Confirm that no API or onboarding change by engineering moved the same metric. Name it in this row if one did.
- **Issue response:** show raw counts on both sides if fewer than about 30 issues sit behind the rate. Add them to the row.
- **Features shipped:** the count covers community-originated requests that shipped, per the issue tracker.

## Leading indicators carrying slow outcomes

| Lagging outcome | Leading indicator | Expected lag | Pull-through so far | Label |
| --- | --- | --- | --- | --- |
| Influenced pipeline ($260k) | none in the framework | n/a | pending, next read `<date>` | influenced |

The framework has no leading indicator for pipeline. I did not invent one. I'm handing the gap to `devrel-metrics`.

## What did not work

| Metric or bet | What happened | Likely cause | What changes | Next read |
| --- | --- | --- | --- | --- |
| SDK issues answered in 2 business days | 78% against an 80% threshold | `[you fill]` | `[you fill]` | `<date>` |

Dropped since last time: none.

## Cost per outcome

Program cost `[amount]` (salaries `[in / out]`). Cost per developer reaching first call, or per feature shipped: `[amount]` (label), against `[the alternative the funder would buy, same cost basis]`. If no cost figure is available, say "not reported this period". Don't estimate one.

## Next period

1. Close the SDK response gap to 80% or better. Read: `<date>`.
2. Propose a leading indicator for pipeline through the framework process. Read: `<date>`.
3. Propose "community sentiment" to the framework, with a written rule and a baseline quarter. It is not reported until it's adopted.

## Decision asked

**Draft:** engineering assigns SDK-issue triage time to meet the 2-business-day target. Options: (A) a named engineer rotation of `[X]` hours a week, or (B) keep the current setup and accept about 78%. Recommendation: A, because it is the only framework metric under its threshold and engineering owns the SDK. Needed by `<date>`.

---

**Appendix**
- Definitions: median time to first call is `[start event] to [end event]`.
- Attribution rule, as written in the framework: `[paste]`.
- Blind spots: `[e.g. Discord-only questions that never reach the tracker]`.
- Activity: `[talks / posts / events]`. Blog pageviews: 180k (measured, analytics; reach, not a framework metric).

---

## Pass-threshold check

- ✅ Headline gives an outcome and a decision, in two sentences.
- ✅ Every number is labelled, and nothing is summed across labels.
- ✅ No causal verbs and no ROI multiple.
- ✅ Every metric comes from the framework.
- ✅ The only lagging outcome is marked "pending".
- ✅ The miss has a row.
- ⚠️ Cost and salary basis are open. They need your input.
- ⚠️ Dates, raw issue counts, the attribution rule and the miss cause are open. They need your input.