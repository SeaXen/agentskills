# ByteForge Hack: waitlist date and food order

I couldn't run `forecast-registrations.py`. The sandbox refused to write the input CSVs to `/tmp`, so I worked the figures by hand with the script's own method (interpolate the reference curve on days-out, then divide). The [Re-run](#re-run) section at the end has the exact files and command.

## Answers

1. **Waitlist.** Don't open one. The forecast never reaches the registration ceiling, so no date triggers it. The waitlist opens the day registrations reach the ceiling that `event-no-show-management` sets. My provisional ceiling is **757 registrations**, and the high end of the forecast is 661.
2. **Food.** Provisionally **529 covers per meal slot**. This is the high end of the band at the 72% free-event show rate, plus 53 mentors and organizers. Re-run on day 7, when registration closes, and order the figure from that re-run on day 4. The count is known by then, so day 7 is when the number gets fixed.

## Assumptions

- **Posture.** Free hackathon, first edition, no prior curve, no peer curve.
- **Reading.** One data point only: 310 registrations at 20 days out. I assume it is net of comps and has no spike or batch release.
- **Close date.** Registration closes at 7 days out, so the final count is the count on day 7, not on doors day.
- **Comps.** 40 mentors at 95% (self-set) and 15 organizers at 100% (self-set) are counted separately from registrations.
- **Show rates.** I use 72% (PheedLoop free-event median) for planning and 50% (MLH hackathon trendline) as the low case. I show 90% only to test your co-organizer's claim. Neither source is your own data.
- **Open questions.**
  - Your go/no-go threshold is unknown.
  - Whether the caterer allows a flex after the order is unknown.
  - Your meal-slot count is unknown.

## 1. Readings

| Days out | Registrations | Note |
|---|---|---|
| 20 | 310 | Single reading, no annotation available. |

## 2. References and method

Registration closes at 7 days, so every curve must end at 7 days, not at doors. Each curve is rescaled to its own day-7 value so that it equals 100% at close.

| Reference | Share in at 20 days | Projection at close | Note |
|---|---|---|---|
| Free-hackathon target timeline (MLH) | 46.9% | **661** | This is a goal timeline, not observed sign-ups. Label it target-shaped. |
| Pooled lead-time curve, rebased to close | 66.4% / 85.6% = 77.6% | **400** | Observed data from 467 events. Free events register later than the pool, so this is the low end. |

- **Method.** Multiplicative pickup for both, because more than 15% of each curve is already in.
- **The chart you found, as is.** 310 / 66.4% is 467 at doors, in line with your 450. It is the wrong end of the curve. It counts the 14% of sign-ups that arrive after day 7, and you close registration before they can sign up. Rebased, the same curve gives **400**, which is lower than 450.
- **Why that chart is a weak fit.** It is a pooled event curve: 41-day median lead time for paid events, 16 days for free ones. A free student hackathon sits at the late end.

## 3. The band (final registrations at day 7, net of comps)

| Low | Mid | High |
|---|---|---|
| **400** | **530** | **661** |

- **Mid.** With only two references, the mid is just the midpoint of the two. Treat it as weak.
- **Width.** I added no error band because there is no forecast history.
- **Before any lock date.** Add a third reference: a peer organizer's hackathon export, or your own count from week 2.

## 4. Co-organizer's two claims

- **"90% will show."** 90-97% is the paid-event band. Free events run 40-60% (Event Tech Live) or about 72% median (PheedLoop). Free hackathons run about 50% (MLH, 323 events). Enthusiasm is not data.
- **"We need 550 registrations."** That is right only at 90% show-up: 500 / 0.9 = 556. At the evidence-supported rates you need far more registrations to reach 500 participants on site:

| Show rate | Registrations needed for 500 on site |
|---|---|
| 90% (paid band) | 556 |
| 72% (free median) | 694 |
| 50% (MLH hackathon) | 1,000 |

## 5. Attendance by ticket type

Mentors: 40 × 0.95 = 38. Organizers: 15 × 1.0 = 15. Comps total 53.

| Show rate (label) | Participants low / mid / high | Total on site low / mid / high | Capacity of 600 |
|---|---|---|---|
| 50% (sourced, MLH) | 200 / 265 / 330 | 253 / 318 / 384 | 42% / 53% / 64% |
| 72% (sourced, PheedLoop median) | 288 / 382 / 476 | 341 / 435 / 529 | 57% / 73% / 88% |
| 90% (co-organizer, paid band) | 360 / 477 / 595 | 413 / 530 / 648 | 69% / 88% / **108%** |

- **The goal of 500 participants.** The high end misses it at both free rates (476 at 72%, 330 at 50%). Only 90% on the high end exceeds it.
- **Verdict.** On the evidence, 500 on site is not reachable from this curve. The honest range is about 290-480 participants at 72%.
- **Demand.** The shortfall against the goal is an input to `event-market-fit`. I don't issue a demand verdict.
- **Day-two attendance.** For a 36-hour event, later meal slots will draw fewer people than the first, and you have no data on how many fewer. It is unknown, so I did not copy day one.

## 6. Capacity read and waitlist

- **Participant seats.** 600 − 53 comps = 545 participant seats.
- **Provisional registration ceiling.** At 72%, 545 / 0.72 = **757**. The final ceiling is `event-no-show-management`'s call; I pass it mine.
- **Result.** The high-end forecast of 661 never reaches 757, so there is no waitlist date.
- **If the ceiling were 605.** That is the ceiling at 90% show-up. The high-end hackathon curve would reach it about 8-9 days out, which is the only scenario where a waitlist opens. I count it as unlikely.
- **Standing rule.** The waitlist opens the day registrations reach the ceiling. Re-check weekly. Once a cap binds, forecast the waitlist, not registrations.

## 7. Milestones and tripwires

Declared now, before the readings arrive. Owner: the lead organizer, you.

| Date | Expected on hand | Tripwire | Response |
|---|---|---|---|
| 14 days out | 348-397 | Reading under 348 | Push brief to `event-marketing-plan`: the gap, the deadline of day 7, and the segment furthest behind (the student campuses). Mark the push on the curve. |
| 7 days out (close) | 400-661 | Under 400 | Same push brief already spent. Hand the band and your go/no-go threshold to `event-risk-management`. Route the demand question to `event-market-fit`. |

- **Declared late.** I could not declare a go/no-go threshold because you gave none. Pick one before the 14-day reading, not after.
- **Not allowed.** Moving the registration close or adding an unannounced incentive to rescue the number is out. The partner network fixes the close date.

## 8. Lock dates

| Commitment | Date | Commit | Band end | Reason |
|---|---|---|---|---|
| Registration close | 7 days out | Fixed by partner network | none | No decision here. The count at this date is the input to the food order. |
| Food, every meal slot | 4 days out | **Provisional 529 covers per slot** (476 participants + 53 comps). Re-run on day 7 and use that figure. | High end | One short meal is a student without food. A spare cover costs one portion. |

- **How to compute the final order.** Registrations at day 7 × 0.72, plus 53, rounded up. Adjust the rate with whatever show-up data you can find from the same partner network.
- **If the caterer allows a flex after the order.** Divide by one plus the flex. For example, with +10% allowed until 2 days out, order 529 / 1.10 = 481 and keep the flex for a late surge. I don't know your flex, so I did not apply one.
- **Per-slot numbers.** All slots lock together, so later slots will over-order. Ask the caterer for a lower guarantee on the last slots and a late adjustment. Count real attendance at the first meal.
- **At 90% as your co-organizer says.** The high-end figure would be 648, which is more than the 600 the venue holds. That is a reason to doubt 90%, not a food target.

## Re-run

Files: `actuals.csv` is `days_out,cumulative` with `20,310`. `pooled-rebased.csv` holds the rebased share curve: 183: 0.0245, 91: 0.181, 61: 0.356, 28: 0.652, 14: 0.869, 7: 1.0, 0: 1.0. The `--types` file uses participants as `share` at 1.0 with the show rate being tested, mentors as `count` 40 at 0.95, and organizers as `count` 15 at 1.0.

```
python3 -I scripts/forecast-registrations.py --actuals actuals.csv \
  --reference assets/curve-free-hackathon-target.csv --reference pooled-rebased.csv \
  --target 500 --capacity 600 --ceiling 757 \
  --checkpoint registration-close:7 --checkpoint food-order:4 --types types.csv
```

Check the outputs against the table above, then re-run with the day-14 reading and keep this forecast unedited.