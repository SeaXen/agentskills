# Forecast sheet: what to change, and next year's error band

## Short answer

**Use the raw 14-day mid × 1.00 to × 1.12.** The raw mid is the floor, not the centre. Your old 14-day band had about the right width (−4% / +5%), but it was centred too low. The band is fitted to only three data points, so treat it as provisional.

Two parts of the plan need to change first, because they would hide the evidence you need for next year.

## Assumption to confirm

I assumed the forecast target is net registrations (492). That matches your "5%": the 14-day mid of 470 is 4.7% under 492. It does not match attendance (418, or 382 without comps), where you would have over-forecast. If the forecast was meant to predict attendance, say so, because the whole analysis changes.

The other numbers I derived:
- **Gross registrations:** 544 (492 plus 52 comps).
- **Non-comp show rate:** 382 / 492 = 77.6%.
- **Comp show rate:** 36 / 52 = 69.2%.
- **Overall show rate:** 418 / 544 = 76.8%.

## 1. Don't overwrite the old milestone numbers

Restating 470 as "492" for this year turns a forecast into the answer. You can no longer see how well the bands performed. Here is how the 2026 forecasts did against 492:

| Milestone | Mid | Band | Actual vs mid | In band? |
|---|---|---|---|---|
| 60 days | 410 | 360–470 | +20% | ❌ missed by 22 |
| 30 days | 455 | 420–500 | +8% | ✅ near the top edge |
| 14 days | 470 | 450–495 | +5% | ✅ 3 below the top edge |

Better layout for the sheet:
- Keep the columns "forecast as issued" (mid, low, high), per year.
- Add "actual cumulative registrations at that milestone" and "final".
- Add "error vs final", as a percentage.

The "corrected" numbers then become a derived column. They are never a replacement.

## 2. Average the realised curves, not the forecasts

You have forecast mids for each year. Averaging them bakes in the 8%, 6% and 5% under-forecast, so the "clean reference" would inherit the bias.

Instead:
1. Pull actual cumulative registrations at T-60, T-30 and T-14 from the ticketing export, for 2024, 2025 and 2026.
2. Divide each by that year's final net registrations. This gives the share of the final total already registered at each milestone.
3. Average those shares across the three years. Show the min–max range at each milestone next to the average.

Forecast = registrations so far ÷ average share. Three points support a range, not a precise line. Keep the spread visible.

Use one definition of "final" every year (net of comps, as now). Track comps separately, with their own show rate.

## 3. The error band

**Data:** under-forecast of 8%, 6% and 5%. All three have the same sign, and the error is shrinking.

**Bias:** the mean is 6.3%, and the most recent year is 5%. A band centred on the raw mid ignores a bias that has appeared three years running.

**Spread:** the standard deviation is only 1.5 points. With n=3 that is not trustworthy. A t-based 80% predictive interval is about +3% to +10% on the raw mid. I widened it to +0% to +12% for three reasons:
- the sample is tiny;
- the shrinking trend may be luck or a real model change;
- the years may not be comparable (see below).

**Recommendation for the 14-day milestone:**
- Band: raw mid × 1.00 to × 1.12, with centre about × 1.05 to × 1.06.
- Example: a raw mid of 470 gives a band of 470–526, centred around 495.
- All three past years fall inside this band, but it was fitted to them. Real coverage is unknown. I would expect around 80% at best.

**30 and 60 days:** you have one error each, so don't build bands from them yet. Provisional rules for next year:
- **30 days:** keep the width of your old band (about −8% / +10%) and shift it up by about 5%. Last year's mid was 8% low.
- **60 days:** the old band missed by 22. Use at least ±15%, shifted up by about 10%, and don't read much into the exact value. It's one observation.

Fill in the 2024 and 2025 errors at 30 and 60 days from your old sheets. Then you can replace the provisional rules with real ones.

## 4. Open questions

- Were the 8% and 6% measured at the 14-day milestone, like this year's 5%? If they were measured at another milestone, they aren't comparable to it. Errors fall as the event nears: 20%, 8% and 5% for 2026.
- Did the three editions differ in size, venue capacity, ticket-release phases or pricing? If so, the share-of-final curves may not be exchangeable.
- Was there a cap or sell-out? Capped demand would make registrations a poor proxy for demand.
- If capacity planning (catering, room size) uses attendance, forecast it separately: registrations × 77.6%, plus comps × 69%. Don't apply the registration error to it.

## Next steps

1. Export actual cumulative registrations at T-60, T-30 and T-14 for all three years.
2. Restructure the sheet as in section 1: keep issued forecasts, add actuals and error.
3. Build the average share-of-final curve with its range.
4. Apply the × 1.00 to × 1.12 band at 14 days, flagged "provisional, n=3".