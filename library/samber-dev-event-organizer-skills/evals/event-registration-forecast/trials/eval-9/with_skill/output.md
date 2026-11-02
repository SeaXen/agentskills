# Hollowmere DevFest: forecast review and next year's error band

**Short answer:** use a band that depends on days-out, not one number. Start at ±20% at 60 days out, ±10% at 30 days, and ±8% at 14 days. Don't average the three curves, and don't overwrite the old milestone numbers. Both moves would hide the error that tells you what the band should be. The reasons follow.

## 1. Assumptions

- The 492 is registrations net of comps, with refunds counted the same way in all three editions.
- Your 2024 (8%) and 2025 (6%) errors have no days-out attached. I read them as roughly 14-day figures, because only this year's 14-day miss (4.5%) rounds to your "5%".
- I haven't seen the 2024 and 2025 curves or which references you ran. The curve advice below is therefore a hypothesis to test, not a verdict.

## 2. Signed error at each milestone

This is the skill's step 12: forecast at the milestone against the final.

| Days out | Mid (band) | Final | Mid minus final | Error vs final | Error vs forecast | Final inside band? |
| --- | --- | --- | --- | --- | --- | --- |
| 60 | 410 (360-470) | 492 | -82 | -16.7% | 20.0% | ❌ missed the high end by 22 |
| 30 | 455 (420-500) | 492 | -37 | -7.5% | 8.1% | ✅ 8 below the high end |
| 14 | 470 (450-495) | 492 | -22 | -4.5% | 4.7% | ✅ 3 below the high end |

- ℹ️ **"5%" is the 14-day error only.** At 60 days you were off by about 17%, so one headline number hides most of the miss.
- ⚠️ **Three editions, three under-forecasts is bias, not noise.** The skill says a consistent sign means fix the reference choice, and a scattered sign means widen the band. Widening alone leaves the bias in place.
- ⚠️ **Coverage was thin.** The 14-day band only just held the final, 3 registrations from its edge. The 60-day band missed.
- ℹ️ **Hypothesis for the bias:** errors shrink as doors approach (17%, then 7.5%, then 4.5%). That fits a booking window that drifts later each year. Against an earlier curve, this year's share on hand at a given days-out is lower than the curve expects, so now ÷ expected share comes out low. Test it by checking whether the 2026 curve sits below 2025, and 2025 below 2024, at 60, 30 and 14 days. Each curve should be a share of its own final.

## 3. Your two plans

### Replacing the old milestone numbers with corrected ones: don't

- The earlier numbers are the only data for next year's band, and the skill says to keep forecasts as made, unedited. Overwriting them leaves a sheet with no error history.
- Do this instead:
  1. Leave the as-made columns untouched.
  2. Add columns for final, signed error, and inside band (yes/no).
  3. If you want corrected figures, add a separate backcast block. It reruns the improved method on the readings available at each milestone. Label it "backcast" and put it beside the as-made figures, never over them.
- The backcast also tests the fix. If the new method would have landed within about 5% at 60 days, the bias is gone. If it wouldn't, the cause is something else.

### Averaging 2024, 2025 and 2026 into one reference curve: don't

- The skill says to run each curve as its own reference and let the spread form the band. It also says to prefer the most recent edition when booking windows drift.
- Averaging puts the reference earlier than where 2026 behaved. If the drift continues, 2027 will register later than the average, and you under-forecast again.
- It also destroys the spread, which is the band's main input.
- Do this instead:
  - Run 2026 as the primary reference, aligned on days-out. Add a shifted run (`@±N`) if the early-bird close or speaker announcement moves.
  - Add 2025 as a second reference. Add 2024 only if the curves are comparable in format, price and room.
  - Low and high are the lowest and highest single-reference projections. The mid is the median across references, and a curve run twice counts twice. State that when presenting the mid.
  - If the bias is real, the final will sit near or above the 2026 projection. In that case treat the 2026 run, not the median, as the realistic mid.

## 4. Error band for next year

Pass `--error-band` per run, set by days-out. The script widens both ends by the same fraction.

| Forecast made at | `--error-band` | Basis |
| --- | --- | --- |
| 60 days out | 0.20 | This year's 20.0% vs forecast. |
| 30 days out | 0.10 | This year's 8.1%, rounded up. |
| 14 days out | 0.08 | The largest of your three yearly misses, 8% in 2024. |

- ⚠️ **Provisional.** The 60-day and 30-day values rest on one edition. The 60-day value has no safety margin. The 14-day value assumes your earlier errors were 14-day figures. Send me 2024 and 2025 errors by days-out and I'll replace the guesses.
- ⚠️ **It overlaps the reference spread.** The script widens the spread's ends. Because the spread already holds part of the error, the combined band is conservative. For example, 360-470 at ±20% becomes about 288-564. Recompute these values from the backcast errors once the reference set is fixed, and expect them to drop.
- ℹ️ **Sign.** All three misses were under. If you want an asymmetric band, widen only the high side by hand and keep the reference spread's low end. The script can't do that. Don't flip it to a symmetric ±5%. That would have missed at 60 and 30 days.
- ℹ️ **Lock dates.** Commit at the band end that the cheaper mistake points to. A catering guarantee commits toward the high end. A hotel block with an attrition penalty commits toward the low end. After three under-forecasts, the high end has been the safer reading of this event. See [references/lock-dates-and-commit-rules.md](references/lock-dates-and-commit-rules.md).

## 5. Attendance data from this edition

- ℹ️ Sold tickets: 382 attended out of 492, which is 77.6%. That is 418 attended minus the 36 comps who attended.
- ℹ️ Comps: 36 attended out of 52 registered, which is 69.2%.
- ❌ Don't use 418 ÷ 492 = 85%. It puts comps in the numerator but not the denominator.
- ⚠️ 77.6% sits below the sourced paid figures: the 83% PheedLoop median and the 90-97% Event Tech Live band. Put your own rates in next year's `--types` file as own-data, from one edition only. Comps go in as `count` basis.

## 6. Next steps

1. Add the final, error and coverage columns to the sheet, and keep the as-made forecasts.
2. Send me the 2024 and 2025 curves (days-out, cumulative, net of comps) and their as-made forecasts by days-out.
3. I'll run the drift check and the backcast, then replace the provisional band values with measured ones.
4. Before 2027 registration opens, record the fixed milestones (early-bird close, speaker announcement) so tripwire ranges are declared in advance.

Method origin, as the skill asks: this is booking-curve pickup forecasting from hotel and airline revenue management. No event-specific forecasting method is established.