**Verdict: "12% behind" is not valid as measured.** It misaligns the dates and mixes two bases. I can't give a band yet, because your message has no row values: no current count, no last-year curve. Below is what I can fix and compute now. Paste the two CSVs to get the final numbers.

## 1. Readings, cleaned

**Assumptions** (tell me which are wrong):
- Paid event, third edition, last year is the reference. I did not run the script.
- Today is 2026-10-26, which is 45 days out.
- The 14 cancellations and 28 codes do not overlap.
- Each code was issued in a known week.

**Date alignment**
- Align on days-out, never on calendar date.
- Doors are 2026-12-10 this year and 2025-12-03 last year.
- Oct 1 this year is **70 days out**. Oct 1 last year was **63 days out**. Your co-organizer compared two points a week apart.
- The matching date for last year's Oct 1 is **Oct 8 this year**.
- Today (45 days out) matches **2025-10-19** last year.
- Weekly rows rarely land on the exact day. Interpolate linearly between the two surrounding rows.

**Effect of the week mismatch**
- The pooled lead-time curve is an illustration, not your data. It has 26.0% of registrations in at 70 days out and 29.5% at 63 days out.
- 26.0 / 29.5 = 0.88, so an event running exactly level with last year looks about **12% behind** on this comparison.
- Last year's own curve will give a different figure. It is likely smaller or larger, and I can't tell you which until I see it.

**Cleaning this year's series to net of codes and refunds**
1. Subtract the 28 codes **in the week each was issued**. Do not subtract them from the final total, or an early batch will fake a sales week.
2. Subtract the 14 cancellations in the week each happened.
3. **161 → 158:** the cumulative column already fell by 3 that week. A fall in cumulative is refunds, not negative demand.
   - Check whether those 3 are already counted in the 14. If they are, subtracting all 14 again double-counts them.
4. Annotate the holiday week as a holiday lull. Name it on the curve and do not adjust its numbers.
5. Leave last year's series alone, since it is already net.

**Direction of the two corrections**
- The date correction makes this year look **less** behind.
- The gross-to-net correction makes it look **more** behind, because up to 42 registrations leave this year's count.
- The 12% claim ignored both. The net result needs your numbers.

## 2. References and method

| Reference | Role | Projection |
| --- | --- | --- |
| `last-year.csv` as is | Main run, aligned on days-out | Multiplicative once at least 15% of the curve is in. The pooled curve has about 43% in at 45 days. |
| `last-year.csv@±N` | Only if the early-bird close or speaker announcement moved a week or more | Same. This run and the as-is run both come from last year, so together they count twice in the median. Say so if that sets the mid. |
| `assets/curve-pooled-lead-time.csv` | Second reference, low end | Same |

- I am not using a straight line from today to doors. It reads a back-loaded curve as a shortfall.
- If today's reading follows an early-bird close or an announcement, also run `--as-of` on the last reading before it.
- The script needs Python 3 and nothing else. The command, with its columns:

```
python3 scripts/forecast-registrations.py --actuals actuals-net.csv \
  --reference last-year-net.csv --reference assets/curve-pooled-lead-time.csv \
  --target <plan> --threshold <break-even> --capacity <room> --ceiling <cap> \
  --checkpoint <lock>:<days-out> --error-band 0.15 --types ticket-types.csv
```

CSV columns are `days_out,cumulative`.

## 3. Band

Pending. A band needs today's net count and last year's net curve. With two references it is the lowest, median, and highest single-reference projection. It is never an average. With no forecast history I use `--error-band 0.15`, and I won't call that figure sourced.

## 4. Lock-date table

Pending. I need each commitment's date and whether it can move after the lock.

| Commitment | Rule I will apply |
| --- | --- |
| Catering headcount | High end of attendance, divided by (1 + the caterer's flex) |
| Hotel block | Low end if the hotel confirms in writing that rooms can be added at the group rate |
| Badges | High end of registrations plus comps |
| Venue cancellation step | Set by the go/no-go review, not by the forecast |

## 5. Milestone table

Pending. I need your milestones. Each gets an expected on-hand range declared before the reading. A tripwire fires only when a reading lands outside that range.

Default response order:
1. Push brief to `event-marketing-plan`.
2. Budget-tier downgrade to `event-budget`.
3. Go/no-go escalation to `event-risk-management`, only if the mid projection misses the threshold at the review before the next fee step.

I will not move price dates or add a surprise discount to rescue the forecast.

## 6. Capacity

Pending. Capacity is compared against attendance including comps, not registrations. For a paid event, registrations close at capacity minus the comps expected to attend.

## 7. Attendance by ticket type

- The 28 codes go into the types file as a `count` row. They are not in the sales count.
- Speakers and sponsor staff take a self-set rate and are labelled that way until measured at check-in.
- Paid tickets: choose between 90–97% (Event Tech Live) and about 83% median (PheedLoop). Use the one whose population matches yours.
- Never discount late registrants.
- Walk-ins and day-two attendance are unknown without your own prior check-in counts.

## What you need to send

Reply with:
1. This year's weekly cumulative rows (gross), with the week each code was issued and the week each cancellation happened.
2. Last year's weekly rows.
3. Plan target, break-even, room capacity, and your lock dates with flex.

Next step: paste the two weekly tables. I'll then run the script and fill sections 3–7. It takes about 10 minutes once the data is in.