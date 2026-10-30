# Worked forecast

A paid two-day conference, second edition, room for 500. Last edition finished at 500 registrations net of comps. The team plans 550 this year, and break-even needs 350.

## Inputs

`last-edition.csv` (days_out, cumulative): 120,20 / 90,45 / 60,110 / 45,170 / 30,260 / 14,380 / 7,430 / 0,500.

`actuals.csv`: 120,25 / 90,55 / 60,120 / 45,165. Speaker announcement at 60 days out both years; early-bird close at 50 days this year, 45 last year.

`ticket-types.csv` (type, basis, amount, show_rate, label): paid, share, 0.85, 0.90 (sourced paid band, low end); student, share, 0.15, 0.75 (self-set); speakers, count, 40, 0.97 (self-set); sponsor staff, count, 30, 0.70 (self-set).

Caterer: guarantee 7 days out, can add 5% up to two days out. Hotel block: rate code expires 30 days out, 80% usage guarantee.

## Command

The early-bird close moved five days earlier, so last edition runs twice: as is, and shifted `@+5` so its early-bird spike sits on this year's date.

```
python3 scripts/forecast-registrations.py --actuals actuals.csv \
  --reference last-edition.csv@+5 --reference last-edition.csv \
  --reference assets/curve-pooled-lead-time.csv \
  --target 550 --capacity 500 --threshold 350 \
  --checkpoint catering:7 --checkpoint hotel-block:30 --error-band 0.1 --types ticket-types.csv
```

## Output, read line by line

```
Projecting from: 165 registrations at 45 days out
- last-edition.csv shifted +5d (now at 0.82x its count at this days-out): expected share 40.0%,
  pace index 75, multiplicative 412 -> uses 412
- last-edition.csv (now at 0.97x): expected share 34.0%, pace index 88, multiplicative 485 -> uses 485
- curve-pooled-lead-time.csv: expected share 42.8%, pace index 70, multiplicative 386 -> uses 386
Projected final registrations: low 347 / mid 412 / high 534 (spread, widened by +/-10%)
Checkpoints: catering (7 days out): 297-459 on hand
             hotel-block (30 days out): 188-278 on hand
Threshold 350: mid clears, low does not
Total expected attendance: 364 / 422 / 528
Capacity 500 (attendance incl. comps): low 73%, mid 84%, high 106%
```

- **The shift matters.** Unshifted, last edition says 485; aligned on the early-bird date it says 412. The 45-day reading already holds this year's early-bird spike, which last edition only reached at 45 days, so the unshifted ratio flatters this year. Lead with the shifted run, keep the unshifted one as a reference, and let the pooled curve set the low end. The mid lands on the shifted run because last edition counts twice in the median; say so.
- **Pace index 70-88 against the 550 plan.** The event is behind a plan that assumed growth and roughly level with, or below, last year. That is a gap against the target; hand it to `event-market-fit` as a signal only if the 30-day reading lands under 188.
- **Declare the 30-day range now: 188-278 on hand.** The reading after an early-bird close carries the lull; a figure inside the range is the deadline working, not demand falling.
- **Threshold: mid clears, low does not.** No escalation yet. Re-run at the go/no-go review before the 30-day cancellation-fee step; if the mid then misses 350, the escalation is promoted.
- **Capacity.** High-end attendance, 528 with 60 comps attending, passes the 500-person room by 6%. A paid event takes no overbooking, so paid registrations close at 440, the 500-person room minus the 60 comps expected in it: tell `event-no-show-management` and `event-venue-sourcing` now, and flag the larger-room option if the 30-day reading lands above 278.

## Lock-date table produced

| Commitment | Date | Commit | Band end | Reason |
| --- | --- | --- | --- | --- |
| Hotel block | 30 days out | 291 room-nights (low end, 40% out of town, 2 nights) | low | 80% usage guarantee; hotel confirmed it can add rooms |
| Catering, day one | 7 days out (provisional now, re-run on the day) | 503 covers, +5% flex to 528 | high | A short lunch costs more than a spare cover; 528 / 1.05 keeps the flex for a late surge |
| Catering, day two | 7 days out | Unknown: no per-day check-ins from last edition | - | Ask the caterer for a later day-two guarantee and count day-one check-ins first; never copy day one |

## Negative example: the straight line

```
// ✗ Bad - 165 sold in 75 days of sale, 45 days left: 165 / 75 x 45 = 99 more, final ~264
```

The straight line assumes registrations arrive evenly. Last edition took 330 of its 500 in the final 45 days. It would have read this event as missing break-even by 86 and triggered a downgrade the curve never justified.
