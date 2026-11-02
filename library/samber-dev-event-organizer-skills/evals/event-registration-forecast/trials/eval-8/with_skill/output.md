**Take the 600-seat hall before it expires (6 days, so by 2026-11-01). Close paid registration at 545 net of comps. If you somehow stay in the 400 hall, close today.**

⚠️ The forecast script did not run. The sandbox denied writing its input CSVs, so I did the arithmetic by hand using the skill's multiplicative-pickup rule. To re-run it, put the CSVs in `/tmp/regforecast/` and run `python3 -I scripts/forecast-registrations.py --actuals … --reference … --capacity … --ceiling … --types …`. Recheck every figure below against that output.

Method: booking-curve pickup forecasting from hotel and airline revenue management. No event-specific forecasting method exists.

## 1. Readings and assumptions

- 372 paid registrations at 25 days out (event ≈ 2026-11-20). Comps are excluded: 30 speakers and 25 sponsor staff.
- Last year at 25 days out: 300, finishing at 420. That is a pace of 1.24x last year.
- Assumed, since I could not ask:
  - **Counting basis:** last year's 300 and 420 are on the same basis as today's 372 (net of comps and refunds).
  - **No spike:** nothing inflated the 372 (no early-bird close, announcement, or batch release in the last two weeks). A spike projected forward overshoots.
  - **Show rates:** paid 90% (sourced band 90-97%, median 83%), speakers 97% (self-set), sponsor staff 70% (self-set).
  - **Lock dates:** none given, so the lock table is provisional.
  - **Last year's curve:** I only have its 25-day and final points, no weekly export.

## 2. References and method used

At least 15% of the curve is in, so both references use multiplicative pickup.

| Reference | Share on hand at 25 days | Final |
|---|---|---|
| Own prior edition (300 of 420) | 71.4% | 372 / 0.714 = **521** |
| Pooled lead-time curve (generic, interpolated between 28 and 14 days) | 59.8% | 372 / 0.598 = **622** |

- The pooled curve runs behind paid events: its median lead time is 35 days against 41 for paid. It therefore over-projects this event. Treat 622 as an upper bound.
- I did not use a straight line to doors. Last year took 29% of its final in the last 25 days, so a straight line misreads the curve.

## 3. The band (net of comps)

- Low **521**, mid **571**, high **622**.
- The low and high are the two single-reference projections. The mid is the median of the two.
- There is no error history for the band: this is edition two with no recorded forecasts. Add a second prior-edition reference, such as a weekly export, before any lock date.
- The "forecast says 600" claim is wrong. The best-matched reference, your own edition, says about 520. 600 is only the top of a band whose high end is biased up.

## 4. Capacity

Attendance is registrations times show rate, plus comps attending. The comps add about 47 (29 speakers and 17.5 sponsor staff at the rates above).

| Registrations | Show 83% | Show 90% | Show 97% |
|---|---|---|---|
| 372 (today) | 356 | 382 | 416 |
| 521 (low) | 479 | 516 | 560 |
| 571 (mid) | 521 | 561 | 609 |
| 622 (high) | 563 | 607 | 658 |

*(the 97% column counts all 55 comps; the others count 47)*

- **400-seat hall:** it overflows at every point of the band, including the low end (479-560 people). Today's 372 already reaches 416 people at a 97% show rate.
- **600-seat hall:** the low and mid fit at 90% (516 and 561). The 622 high end exceeds the hall only above roughly 614 registrations at a 90% show rate. It is the biased end of the band.

## 5. When to close registration

A paid event closes at hall capacity minus comps expected to attend. It takes no overbooking from me. Overbooking ratios belong to `event-no-show-management`.

- **400 hall:** the ceiling is 400 − 55 = **345**. You are already 27 over it. Close today at 372.
- **600 hall:** the ceiling is 600 − 55 = **545**. At 545 registrations and a 97% show rate, the room holds about 584 people.
- Close on a count, not a date. At the pooled upper-bound pace, 545 arrives about 6 days out (share 545/622 = 87.6%). On your own edition's pace (final ≈ 521) it never arrives. Treat 545 as the tripwire.
- If you want to overbook beyond 545, take it to `event-no-show-management` first. I did not size it.

## 6. The room decision

Take the 600-seat hall. The reasons:

- The 400 hall fails even the low end of the band.
- Short costs more than over. A short hall means turning away paid attendees or a safety problem. A spare 80 seats costs only the price difference.
- Confirm in writing before signing that the 600 hall's price and minimums are reasonable if it fills to only about 500. I do not have those terms.
- Send the venue deadline (2026-11-01) to `event-venue-sourcing` today.

## 7. Your co-organizer's plan

- **"Close at 400, then keep selling":** this contradicts itself. If registration is closed, nothing sells.
- **"Close at 400":** 400 paid plus 55 comps is 455 people for a 400-seat hall, and the 345 ceiling was already passed at 372.
- **"10% will no-show":** that is a mid-band guess. Sourced paid no-show runs 3-17%, so it is not a safe margin. Even at 10% no-show, 400 paid plus 47 comps attending is about 407 people, still over 400.
- **Overbooking plus the bigger hall:** the two together double-count the cushion. The bigger hall is the cushion; overbooking is only for a hall that is too small.
- **"The forecast says 600":** see section 3.

## 8. Lock-date table (provisional; re-run on each lock date)

| Commitment | Commit | Band end | Reason |
|---|---|---|---|
| Venue option | Take 600 | n/a | Section 6 |
| Catering | 607 covers, divided by (1 + caterer's flex %) | High | A short lunch costs more than a spare cover |
| Badges | 622 + 55 | High | Everyone needs a badge |
| Hotel block | Low end (about 516 attendance) | Low | Over-commit carries an attrition penalty, if the hotel confirms in writing it can add rooms |

Catering uses the high-end attendance at a 90% show rate (607, section 4). Send catering counts in attendance terms, never as registrations.

## 9. Milestone tripwire

Declared now, before the reading:

- **Option expiry (19 days out, 2026-11-01):** expect **about 405-425 on hand**.
- This range assumes a linear interpolation of last year's curve between its two known points. Replace it with the weekly export when you have it.
- **Below 405:** the pace is behind the best reference. Send a push brief to `event-marketing-plan` with the gap and the segment furthest behind. Do not move prices or add an unannounced discount.
- **Above 425:** pace is ahead of the pooled upper bound. The 600 hall is clearly right.

The reading lands on the option's deadline, so decide on today's evidence, not the 19-day reading.

## 10. Record these forecasts

- Save these figures unedited: the reference set, band 521 / 571 / 622, and the commit figures. After doors, compute the signed error. That becomes next edition's error band.

## Next action

Call the venue today and ask for written terms on the 600 hall. In the same call, ask for last year's weekly registration export so the script can run on a real curve.