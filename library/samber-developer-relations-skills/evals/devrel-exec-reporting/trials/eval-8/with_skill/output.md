# DevRel - H1 - for the COO

**Provisional: no agreed metric framework. Attribution to DevRel: none claimed.**

## Assumptions and open items (remove before sending)

1. **Your headline fails three rules in the skill, so I did not write it.**
   - **"Drove" needs causal evidence.** The 900 to 1,400 figure is company-wide. The v3 SDK shipped in April and moved the same metric, and paid ads and the growth team were active too. I can write co-movement ("rose while"), not causation.
   - **$60 per activated developer divides cost by outcomes DevRel has not been credited with.** $180k / $60 = 3,000. That equals (1,400 − 900) × 6 months, so it counts every extra activation company-wide, assuming all six months ran at 1,400. March was a ramp, so the real figure is probably lower. I need the monthly series. Until the credit rule exists, the label is "all incremental outcomes, not attributed".
   - **$60 against $95 compares different cost bases.** DevRel's figure excludes salaries and the growth team's includes them. The $95 is also a paid-ads figure with its own attribution I haven't seen. I show both with the mismatch beside them and claim no win.
2. The arithmetic gives 55.6%, which I rounded to 56%.
3. I don't know your COO's goals, the decision you want, the DevRel salary total, or whether anything missed. Gaps are marked `<...>`. Each needs one answer from you before sending.

## Headline

Company-wide developers reaching their first successful API call rose from 900 to 1,400 a month (+56%, measured) since the developer advocacy program started in March. The v3 SDK shipped in April and also moved this number, so no share is credited to DevRel yet.

**Decision asked:** approve an attribution rule and a holdout read on activation, so H2 reports DevRel's share, by `<date>`.

## Results table

| Spine unit (COO goal) | Metric | This period | Baseline / threshold | Status | Label |
| --- | --- | --- | --- | --- | --- |
| Developer activation | Developers with first successful API call, per month, company-wide | 1,400 | 900 (pre-March) / `<target>` | none (no threshold set) | measured (product analytics); co-movement with the program and the v3 SDK, not attributed |

Cross-check these before sending:
- **Confounds:** the v3 SDK (April); any launch or seasonal spike in the half; paid-ad spend changes.
- **Month-by-month series:** one table of the six months, not just the endpoints. It shows whether the rise began in March or in April.

## Leading indicators carrying slow outcomes

| Lagging outcome | Leading indicator | Expected lag | Pull-through so far | Label |
| --- | --- | --- | --- | --- |
| Activated developers credited to DevRel | `<e.g. signups naming docs or a talk, or visits to the DevRel-owned quickstart>` | `<from your funnel data>` | link unproven, first read `<date>` | `<label>` |

The framework has no leading indicator yet. I did not invent one. Choosing it is a `devrel-metrics` task.

## What did not work

`<Needs your input. List each metric or bet that missed its threshold.>`

Because no thresholds exist, I can't write "no metric missed". The honest entry today is: **no thresholds were set, so misses can't be measured. Setting them is part of the decision asked.**

Dropped since last time: `<none, or name>`.

## Cost per outcome

DevRel program cost: **$180k this half (salaries out)**.

| Figure | Amount | Label | Cost basis |
| --- | --- | --- | --- |
| DevRel cost per extra activated developer | $60 | all incremental outcomes, not attributed (assumes 3,000 extra over six months) | salaries out |
| Paid-ads cost per activated developer | $95 | growth team's figure | salaries in |

**These two figures are not comparable, so I draw no conclusion from them.** Break-even check: at 3,000 extra activations, DevRel matches $95 once its salaries reach about $105k for the half. If DevRel salaries exceed that, the loaded cost is above the paid-ads figure. With salaries in on both sides, or out on both sides, the comparison becomes valid. I need the DevRel salary total or the growth team's media-only cost to complete it.

## Decision asked

Approve an attribution rule and a holdout read for H2. Options:
- **A.** Define DevRel-credited activation (signup-source question plus touched-cohort tracking) and read a holdout on a bounded push.
- **B.** Keep reporting company-wide activation only.

**Recommendation: A.** It is the only route to a defensible DevRel share, and the data to support the 56% rise would be recorded before the next push. Needed by `<date>`.

---

**Appendix**
- **Definitions:** "activated" = first successful API call, product analytics.
- **Attribution rule:** none agreed; none claimed.
- **Blind spots:** the SDK, paid ads and DevRel overlap in time, so the data can't separate them.
- **Activity:** `<one line: talks, posts, events>`.

## Pass-threshold check

- ✅ Every number is labelled.
- ✅ No causal verb is used.
- ✅ The cost comparison states its basis mismatch.
- ✅ The decision names options, a recommendation and a date placeholder.
- ⚠️ Not yet passing: the misses section, the leading indicator and the dates need your input.

**Which of the open items can you answer first?** The monthly series and the DevRel salary total change the most.