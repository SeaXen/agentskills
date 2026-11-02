**The sheet shows 1.00, 2.00, 2.67, 3.50, 4.33 and 5.00, in that order.**

The raw totals come from a capability ladder with a negative rung. The skill says to normalize them with a cohort min-max pass to the published 1-5 scale before anyone outside sees them. Teams and the sponsor never see -6 or 18.

**Arithmetic.** The min is -6, the max is 18 and the range is 24. The formula is `(score − min) / 24 × 4 + 1`.

| Raw total | Sheet score |
| --- | --- |
| -6 | **1.00** (floor) |
| 0 | **2.00** |
| 4 | **2.67** |
| 9 | **3.50** |
| 14 | **4.33** |
| 18 | **5.00** (ceiling) |

Show two decimals, as the skill's own worked example does.

**Two things to settle before publishing.**

1. **Use the ×4 + 1 form, not ×5.** The reference text writes the formula as `× top_of_scale`. Applied literally to a 1-5 scale, that puts the worst team at 0, which is off the scale. The skill's worked example uses ×4 + 1, and so do the numbers above.
2. **Normalize over everything scored on this ladder, not only the finalists.** The six finalists give the 1.00 and 5.00 anchors only if they are the whole cohort. If the ladder was applied to all submissions, take min and max from all of them. Otherwise the same team's number changes depending on who made the cut.

**Does this make the wrapper outcome impossible?** Only partly.

- **What the ladder does:** the bottom rung ("simple chatbot, no added logic", -5) actively subtracts points. A wrapper falls below a plain-prompt project instead of just scoring low.
- **What it doesn't do:** min-max is relative. If every entry is weak, the worst still shows 1.00 and the best 5.00. A strong demo and presentation can also offset a low technical-depth score, so a wrapper can still reach mid-table.

If you want "impossible" rather than "discouraged", write it as a separate elimination gate, published with the category names. For example: "a generation too simple to meet the brief's stated ambition" or "the model is not central to the project". The skill keeps knockouts out of the weighted rubric so they read as disqualifying, not just low-scoring. Keep the numeric weights internal unless you have a reason to publish them.

I haven't built the rest of the plan (weights, allocation, tie-break ladder, conflict rule). I can do those section by section if you want.