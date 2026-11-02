# Driftwood Rust Days, 2nd edition: forecast at 95 days out

**Verdict: the forecast can't be made yet, and 432 is not supported.** The data can't produce a band at this point. Don't sign the top catering tier or a second hotel block on this evidence. The one thing that would change that is a rate expiring before the next reading, covered under the lock dates below.

I couldn't run `forecast-registrations.py` because the sandbox denied writing its CSV inputs. The figures below are hand-computed with the script's own rules. I haven't verified them by running it.

## Assumptions, to confirm

- Paid conference, 400-seat venue, plan of 350 net of comps.
- Last year's 150 seats and 180 final registrations are net of comps. If the 180 includes a waitlist or sponsor codes, the whole comparison shifts.
- The 22 are paid, sold registrations. No speaker, sponsor or volunteer codes and no batch release are mixed in.
- Last year's sales also opened about 10 days before the 95-day mark. If not, the two readings differ in time on sale.

## 1. Readings

| Reading | Value | Note |
| --- | --- | --- |
| This year, 95 days out | 22 | Sales open 10 days (opened about 105 days out). Launch measures reach, not demand. |
| Last year, 95 days out | 9 | Final 180, so 5.0% of the final was in. |
| Last year's room | 150 seats | A final of 180 against 150 seats suggests a cap or waitlist bound. Registrations then showed the cap, not demand, so 180 may understate or distort last year's curve. |

## 2. References and method

- **Last edition.** Only two points exist, 95 days out and doors. Interpolating between them is a straight line, which the skill deletes. Its share at 95 days is 5%, below the 15% floor. That forces additive pickup: 22 + (180 − 9) = 193. This year runs at 2.44x last year at the same days-out, outside the trust range of 0.5–2.0x, so 193 is only a lower bound and stays out of the band. The multiplicative figure, 22 / 0.05 = 440, is unstable: one registration moves it by 20.
- **Pooled lead-time curve.** It interpolates to 14.9% at 95 days, just under the 15% floor. It is a share curve with no counts, so additive pickup isn't available. Multiplicative gives 22 / 0.149 ≈ 148, unstable and out of the band. The curve is pooled, and paid events run slightly behind it.
- **Straight line.** Rejected. 22 in 10 days, projected to doors, gives about 230. It's wrong for the same reason it is on any back-loaded curve.

## 3. The band

None. Every reference is either unstable or only a bound, so the script would stop with "no usable projection". Bounds only: about 148 (pooled, unstable) to 193 (additive lower bound) to 440 (multiplicative, unstable). A spread of 148 to 440 is not a forecast.

**The co-organizer's math.** 2.4 × 180 = 432 treats a ratio of 22 to 9 as a stable pace. At 5% of the curve, that ratio rests on a 13-registration difference.

Three things make it weaker than it looks:

- Week two reads reach, not demand.
- The 150-seat cap may have bent last year's final.
- A bigger room changes the final, not the shape. This year's 400 seats don't mean demand scaled with them.

432 is also above 400 seats, and it counts registrations, not attendance.

## 4. Lock-date table

| Commitment | Commit now? | Commit figure | Band end and reason |
| --- | --- | --- | --- |
| Top catering tier | No | None yet | Catering usually locks days before the event and can often rise. A short lunch costs more than a spare cover, so the eventual commit leans high. The line can still grow, so there's no reason to buy the top tier 3 months early. Re-run on the lock date. |
| Second hotel block | No | Hold | Over-committing carries an attrition penalty, so commit toward the low end. Start small and grow the block only if the hotel confirms in writing that rooms can be added at the group rate. "The rates are good" is not a deadline. Ask the hotel for the rate-expiry date and the add-rooms terms. |

The exception: if the hotel rate genuinely expires before the early-bird reading, sign only the smallest starter block with written add-on rights. Size it from the low-end attendance once a band exists.

## 5. Milestone table

The early-bird close is about 74 days out. Reading it needs last year's count at 74 and 60 days out, which I don't have. The tripwire range must be declared before the reading, so get that export first.

| Milestone | Days out | Expected on hand | Tripwire response | Owner |
| --- | --- | --- | --- | --- |
| Early-bird close | ~74 | Pooled path only: ~35 (22 / 0.149 × 24%). Declare a range against last year's count before this date. | Below the declared low end: push brief to `event-marketing-plan` with the gap and the segment furthest behind. | Co-organizers |
| Next reading | ~60 | Declare from last year's count at 60 days | Same as above | Co-organizers |

- Expect a spike at the early-bird close and a lull after it. A lull is the deadline working, not demand falling.
- Run the forecast at the 74-day reading, and again with `--as-of` set to the last pre-spike reading.
- The 15% floor is crossed at about 90 days on the pooled curve, so the multiplicative projection becomes usable as soon as new readings arrive.

## 6. Capacity

No band, so no capacity read. If 432 were true, attendance would be about 370 from registrations (assuming 85% show), plus comps. That fits 400, so the room is not the constraint today. The co-organizer's figure is the open question, not the room.

## 7. Attendance by ticket type

Not computable without a band. Once there is one, run it through the `--types` file, with show rates labelled as sourced, own-data or self-set.

## What I need from you

1. Last year's full cumulative export by date. Weekly is enough, daily is better, and it must include the 74- and 60-day points. Say whether it's net of comps and refunds.
2. Whether the 150-seat cap was hit last year, and whether the 180 includes a waitlist or sponsor codes.
3. Last year's sales-open date, and what moved this year (early-bird close, speaker announcement, price).
4. The hotel's rate-expiry date and add-rooms terms, and the caterer's lock date and flex.
5. Whether the 22 are net of comps and free of any batch release.

Once the export is in, I can run the script with a real reference and give you the band, the commit figures and the declared early-bird range. At that point the demand question (is this edition on track to beat last year) goes to `event-market-fit`, and I don't issue that verdict here.