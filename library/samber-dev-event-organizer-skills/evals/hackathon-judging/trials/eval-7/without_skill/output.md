**The sheet shows 1.0, 2.0, 2.7, 3.5, 4.3 and 5.0, in finalist order.**

This assumes -6 and 18 are the lowest and highest totals the draft scheme can produce, not just the lowest and highest among your six finalists. I only have your six numbers, so confirm those bounds.

**Conversion**

`published = 1 + 4 × (raw − floor) / (ceiling − floor)`

Here floor = -6, ceiling = 18, and the range is 24.

| Finalist | Raw | Published (1-5) |
|---|---|---|
| A | -6 | 1.0 |
| B | 0 | 2.0 |
| C | 4 | 2.7 |
| D | 9 | 3.5 |
| E | 14 | 4.3 |
| F | 18 | 5.0 |

- **Use the scheme's bounds, not the finalists' range.** If you stretched the finalists' own min and max to 1 and 5, a weak cohort would still produce a 5. If the real ceiling is above 18, say 24, the same totals shift down (18 becomes 4.0). Publish the floor and ceiling in the rubric.
- **Do not publish raw totals.** The rubric reports every criterion on 1-5, and a negative number on a team's sheet reads as a bug.
- **Report one decimal.** Rounding to whole numbers puts D and E both at 4 and C and D both at 3 or 4, which removes the differences the scheme was built to show. If you must use integers, the result is 1, 2, 3, 4, 4, 5.
- **Apply the wrapper cap after conversion.** A project that is only a system prompt in a chat UI gets a hard maximum of 2.0 on this criterion, whatever else it scores. A negative-point penalty alone can be outweighed by points from polish and demo quality. A cap on the published number cannot.
- **Rank on the published number, and do not average the cap away.** Otherwise a wrapper can still reach mid-table through the other criteria. Add a rule that any entry capped on technical depth cannot place above any uncapped entry scoring 3.0 or more on it. Whether that rule fits your overall weighting is your call.