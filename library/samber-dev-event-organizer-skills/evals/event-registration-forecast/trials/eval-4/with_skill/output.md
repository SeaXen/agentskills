**Tell the board: expect about 390–540 registrations, mid about 460. Do not promise 700. Tell the hotel: provisional ~290 room-nights, final figure on day 30, and ask for rooms "added at group rate" in writing.**

⚠️ **Not script-run.** The sandbox denied writing CSVs to `/tmp`, so I did not run `forecast-registrations.py`. I computed the pooled-curve numbers by hand from the shipped curve. I also had no prior-edition exports, only your two final totals. Re-run before the day-30 lock (command at the bottom). The figures below are provisional.

## 1. Assumptions to check
- 260 is net of comps, at 38 days out.
- The keynote went out at 45 days, so 165 were on hand then (260 − 95). 2025's keynote was also at 45 days, so it aligns directly. 2024's was at 50 days, so it needs a +5 shift.
- The week before the keynote I took as about 20 sold, so about 145 at 52 days. This is my inference.
- Every batch of 50 sells out within a day. Registrations therefore measure your release schedule, not demand. Demand above that is unobserved. This works against the board story in both directions.
- I assumed no comps and no capacity figure. You gave neither.

## 2. Reference and method
- Used only the pooled lead-time curve (PheedLoop, 467 events). At 38 days out it shows about 48% registered. At 45 days it shows about 43%.
- Both of your own editions are the better references. I can't use them without the daily exports.
- Straight-line projection is a banned method in this skill. It reads a spike as a run rate.

## 3. Band, net of comps
- **Low: ~386.** This projects from the last pre-spike reading, 165 at 45 days, and treats the keynote week as pull-forward.
- **High: ~540.** This projects from today's 260 at 38 days. It includes the spike, so it likely overshoots.
- **Mid: ~460.** This is the midpoint of two runs of one curve, which is weak. Treat it as a placeholder until your own exports are in.
- Sanity check: 2024 finished at 410 and 2025 at 480, so about +17% a year. That points to roughly 560 if the trend holds. It does not point to 700.

## 4. The co-organizer's 95 a week → 700+
- 260 + 95 × 5.4 weeks ≈ 775. That is the "pass 700" claim.
- The 95 was the keynote week. The prior run rate was about 20 a week. A spike projected forward overshoots, and the lull after it then reads as collapse.
- Reaching 700 needs about 440 more sales in 38 days, roughly 9 more batches.
- It also needs about 1.45× last year's 480 final. That is 30% above the high end of the band.
- Verdict for the board: give the 390–540 band with mid ~460, and say the mid will be re-set once the prior-edition curves are run.

## 5. Marketing's plan: no
- Do not extend the early-bird by two weeks. Do not add a secret 20% code. Moving a published price date or adding an unannounced discount is a deleted move in this skill.
- It trains buyers to wait for the next rescue. It also undercuts the scarcity your batches create.
- This week's slowdown is the expected lull after the keynote spike. It is not evidence of collapse.
- Pricing dates belong to `event-ticket-pricing`. Give marketing the tripwire below instead.

## 6. Milestone tripwire, declared now
- At 30 days out, the pooled curve expects about 54% of the final. That is 210–293 on hand across the band.
- 260 is already inside that range, and the count can't fall. So the real range is **265–295 on hand at day 30**. This is self-set.
- **Below 265:** the keynote spike was pull-forward, not demand. Send a push brief to `event-marketing-plan` with the registration gap, the deadline, and the weakest segment. Mark the push on the curve.
- **Above 295:** run the capacity check, because demand is running above the band.
- Escalate to `event-risk-management` only if the mid misses your break-even at the go/no-go review before the next cancellation-fee step. You gave no break-even, so I can't check this yet.

## 7. Hotel lock, day 30 (8 days from now)
- **Commit the low end.** Under-using the block has an 80% guarantee penalty attached. Short rooms only cost something if the hotel can't add more.
- Formula: attendance × out-of-town share × nights ÷ guests per room.
- Low attendance: 386 × 0.83 (sourced paid median) ≈ 320.
- 320 × 0.45 × 2 nights ÷ 1 per room ≈ **288 room-nights**. I rounded to **~290, about 145 rooms a night**. Comps are not included.
- Mid is about 346 room-nights and high about 403. The 700 plan implies about 523, with an 80% guarantee of about 418. If you land near 460, you would be roughly 70 room-nights short of the guarantee.
- "They can probably add rooms" is not a confirmation. Ask for written confirmation that rooms can be added at the group rate after day 30. Without it, a low-end block leaves late registrants paying rack rate.
- The 45% out-of-town share is last year's. A keynote may draw more travellers, so check it against this year's registration city data.

## 8. Capacity and attendance
- You gave no capacity, so I can't run the capacity check. Capacity compares attendance, including comps, not registrations.
- A paid event closes registration at capacity minus the comps expected to attend.
- Attendance at the 0.83 sourced paid median: about 320 (low), 384 (mid), 448 (high), before comps. Speakers and sponsor staff have no published rate, so use your own check-in counts.
- Day two: I can't forecast it without your per-day check-ins. Do not copy day one.

## What I need
1. The two daily exports and the early-bird close date.
2. Capacity and comp counts.
3. How many batches you released in each of the last three weeks.

Re-run command:
```
python3 scripts/forecast-registrations.py --actuals actuals.csv \
  --reference 2025.csv --reference 2024.csv@+5 \
  --reference assets/curve-pooled-lead-time.csv \
  --target <plan> --capacity <room> --checkpoint hotel-block:30 --error-band 0.15
```
Re-run at 30 days out. The hotel commit is the figure that run gives, not the one above. Also run it with `--as-of` set to the 45-day reading.

**Next, in about 2 minutes:** send me the two exports and the three numbers above.