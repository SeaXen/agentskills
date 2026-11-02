**Answer: don't give the caterer 315 tomorrow. Give a provisional 365 covers (day one) now and commit on the day-7 re-run. The guarantee is due 7 days out, which is 33 days from now, so waiting costs nothing.**

I could not run the bundled script. The sandbox blocked writing its input CSVs. Every figure below is the script's method done by hand, with the same interpolation, shift and median rules. Re-run it on the inputs in section 2 before you quote a number outside the team.

## Why 315 is wrong

1. **Codes inside the count.** The 210 includes 35 codes, so 175 tickets were actually sold. Speakers and sponsors are counted once, separately, as comps.
2. **Straight line.** "210 in 80 days, so 105 more" assumes even sales. Last year took 305 of its 480 registrations in the last 42 days, and it had only about 188 (39%) at this point.
3. **Registrations, not covers.** The caterer needs people who show up, not tickets. That means show rates by ticket type plus comps.
4. **315 is short even in the low case.** The low-end attendance is about 390. Even with the caterer's 10% added, 315 reaches only 346, which leaves 44 people unfed.

## 1. Assumptions (please correct any that are wrong)

- Readings 22, 50 and 118 were already net of codes. Only the 210 was not.
- The 35 codes are part of the 70 planned comps (40 speakers, 30 sponsor staff). Comps are counted once, in the types file.
- Refunds are treated the same way in both years. You didn't say.
- Show rates are placeholders, not your data. Paid is 90% (low end of the sourced 90–97% band). The PheedLoop median is about 83%, which would cut mid attendance to about 426. Students 75%, speakers 97% and sponsor staff 70% are self-set. Replace them with last year's check-in counts if you have them.
- No break-even or plan number was given, so there is no threshold read.
- No overbooking: paid events close at the cap.
- Day-two attendance is unknown. Last year's per-day check-ins were not given.

## 2. Readings and references

| Days out | This year (net of codes) | Last year |
| --- | --- | --- |
| 120 | 22 | 18 |
| 90 | 50 | 40 |
| 60 | 118 | 105 |
| 50 | | 150 (early-bird closed) |
| 42 | | 175 |
| 40 | **175** (210 − 35 codes) | about 188 (interpolated) |

This year's early-bird closed at 42 days out, 8 days closer to doors than last year's. The 40-day reading is two days after the close, so it holds the early-bird rush.

| Reference | Share of final on hand at 40 days | Method | Projection |
| --- | --- | --- | --- |
| Last year shifted by −8 days (`last.csv@-8`) | 32.6% | Multiplicative | 538 |
| Last year as is | 39.1% | Multiplicative | 448 |
| Generic pooled lead-time curve | 46.6% | Multiplicative | 376 |

- **Multiplicative pickup.** Every reference had more than 15% of its final on hand, so multiplicative pickup applies throughout.
- **Shifted run.** Lined up on the early-bird close, we are 12% ahead of last year. Unshifted, we look 7% behind.
- **Shift caveat.** The shift also moves last year's late surge 8 days later. Treat 538 as the optimistic end.
- **Pooled curve.** It is generic, from other events, and sets the low end.
- **Spike check.** The 60-day reading is before the early-bird rush, so it is only a sensitivity run. Projected from it, the three references give 377 / 539 / 646. That is too wide to narrow anything.

## 3. Band (final registrations, net of comps)

**Low 376 / mid 448 / high 538.**

- The ends are single references. The mid is the median, which is last year's unshifted run.
- No `--error-band` was applied: there is no forecast history. This is the first forecast, so record it unedited.

## 4. Lock dates

| Commitment | Date | Commit | Band end | Reason |
| --- | --- | --- | --- | --- |
| Catering, day one | 7 days out (provisional now, re-run that day) | **365 covers**, flexing to about 402 with the caterer's +10% | High end, capped by the room | One missing lunch costs more than one spare cover. 402 ÷ 1.10 = 365 keeps the 10% for a late surge. |
| Catering, day two | 7 days out | Unknown | n/a | No per-day check-ins. Ask for a later day-two guarantee and count day-one check-ins first. Never copy day one. |

**How 402 comes from the room.** Close paid registration at 390 (450 seats minus the 60 comps expected to attend). That gives 390 × 0.8775 + 60 = 402 people. Without a cap the high-end attendance is 531, which no room can seat.

## 5. Milestones and tripwires

Expected registrations on hand if pace holds:

| Days out | On hand | Tripwire |
| --- | --- | --- |
| 30 | 204–233 | Below 204: send a push brief to `event-marketing-plan` with the gap, this milestone as the deadline, and the segment furthest behind. Mark the push on the curve. Above 233: run the capacity step. |
| 14 | 279–347 | Same rules, re-derived at the reading. |
| 7 (catering lock) | 322–406 | Re-run and commit. |

- **Owner:** you. Declare these ranges now, before the readings arrive.
- **Early-bird lull:** a reading inside the 30-day range is the post-close lull. It is not a collapse.
- **No price moves:** do not move price dates or add discounts to rescue a low reading.
- **Threshold:** you gave no break-even. Send one to `event-risk-management` if you want the go/no-go criterion.

## 6. Capacity

Attendance, comps included, against 450:

| | Low | Mid | High |
| --- | --- | --- | --- |
| Attendance | 390 | 453 | 531 |
| Share of room | 87% | 101% | 118% |

- **Close registration at about 390 paid.** Use 380 if you want a seat held for every one of the 70 comps.
- **When it fills:** last year's curve reaches 390 about 7 days out, the shifted run about 9 days out, and the pooled curve never does. That is probably after the catering lock.
- **Actions:** tell `event-venue-sourcing` now, and ask for the deadline on any bigger-room or second-room option. Tell `event-no-show-management` the planned close figure. Plan a waitlist to open around 9 days out.
- **After the cap binds,** registrations only measure the cap. Forecast the waitlist instead.

## 7. Attendance by ticket type (low / mid / high)

| Type | Registrations | Show rate (label) | Attendance |
| --- | --- | --- | --- |
| Standard (85%) | 320 / 381 / 457 | 90% (sourced, low end of the paid band) | 288 / 343 / 411 |
| Student (15%) | 56 / 67 / 81 | 75% (self-set) | 42 / 50 / 61 |
| Speakers | 40 | 97% (self-set) | 39 |
| Sponsor staff | 30 | 70% (self-set) | 21 |
| **Total** | | | **390 / 453 / 531** |

- **Walk-ins:** unknown. You gave no prior count.
- **Late registrants:** no discount applied. Within an event they show up at nearly the same rate as early ones.

## What to send the caterer

- Tomorrow: "about 365 for day one, final guarantee at 7 days out, sell-out likely, day two to follow."
- At 7 days out: re-run with the new reading and commit that figure.

**Files for the re-run** (put them in a scratch directory outside the repo):

- `act.csv`: `120,22 / 90,50 / 60,118 / 40,175`
- `last.csv`: your last-year series, with a `0,480` row for doors
- `types.csv`: the table in section 7
- Command: `python3 -I scripts/forecast-registrations.py --actuals act.csv --reference last.csv@-8 --reference last.csv --reference assets/curve-pooled-lead-time.csv --capacity 450 --ceiling 390 --checkpoint ...`, with one `--checkpoint NAME:DAYS_OUT` each for catering:7, d14:14 and d30:30 (the 7, 14 and 30-day milestones)