# Lumen Devs Day: registration forecast and what to tell the venue and caterer

**Don't cancel and don't move online this week.** Your realistic final is about **245 registrations (range 150-335)**, which is about **150 people in the room (range 75-240)**. That doesn't reach the 400 you told sponsors, so reset the sponsors now.

⚠️ **I could not run `scripts/forecast-registrations.py`.** The sandbox denied the commands and the file writes. Every figure below is hand-computed with the script's arithmetic (linear interpolation on the curves, multiplicative pickup). Re-run these before you quote anything to the venue or caterer:

```
python3 -I scripts/forecast-registrations.py --actuals actuals.csv \
  --reference assets/curve-pooled-lead-time.csv \
  --reference assets/curve-free-hackathon-target.csv \
  --target 400 --threshold 100 --capacity 350 \
  --checkpoint venue-step:21 --checkpoint caterer:5 --types types.csv
```

`actuals.csv` is `81,0` then `32,80`. `types.csv` has one `free` row (share 1.0) at show rate 0.72, then a second run at 0.50.

## 1. Assumptions (you didn't get to answer the interview)

- ℹ️ The 80 registrations are net of comps. There are no refunds or batch releases, and no spike you need to adjust for.
- ℹ️ Sales opened 49 days ago, so 81 days out. Today is 2026-10-26, doors are Friday 2026-11-27, and the venue step is Friday 2026-11-06.
- ℹ️ The event is free with open registration, in a 350-seat room. I counted no speaker or sponsor comps, so add them in the types file.
- ℹ️ Your target of 400 means attendees, not registrations.
- ℹ️ There is no prior edition. The neighbouring organizer's 500 is not yet a usable reference, because I don't know whether it counts registrations or attendance, or have its curve.
- ℹ️ Walk-ins are unknown. Generic curves end at doors and leave them out.

## 2. References and method

The method is booking-curve pickup forecasting from hotel and airline revenue management. No event-specific forecasting method is established.

| Reference | Share expected on hand at 32 days | Method | Projection |
|---|---|---|---|
| Pooled lead-time curve (observed, 467 events) | 52.7% | Multiplicative (over the 15% threshold): 80 / 0.527 | **152** |
| Free-hackathon target timeline (target-shaped, not observed) | 24.0% | Multiplicative: 80 / 0.24 | **333** |

- **The pooled curve gives the low end.** Free events register late, with a median of 16 days out against 41 for paid events. The pooled curve therefore expects too many people on hand by now.
- **The pooled curve is probably too pessimistic for you.** It assumes about 20% of sign-ups happened before the day you opened. Renormalizing from your opening day gives about 198, which sits inside the band. I am not adding it as a third reference.
- **The hackathon curve is a stand-in.** It is a goal timeline, not observed data, and it closes at 7 days out by design. Treat 333 as the optimistic bound.
- **I ran no straight line.** 80 over 49 days is 1.6 a day, so it would project about 130 more. The skill deletes that method: every sourced curve is back-loaded.

## 3. The band

Registrations net of comps: **low 152 / mid ~243 / high 333.**

- The ends are the lowest and highest single-reference projections. The mid is the median of the two, and no history exists to widen the band.
- **Attendance**, using free show rates of 50% (industry band) to 72% (PheedLoop median):
  - Low: 76-109
  - Mid: 122-175, so about 150 on a central rate
  - High: 167-240
- **The 400 target needs about 555-800 registrations** at those show rates. That is 1.7 to 2.4 times the high end of the band.
- **The 20% of target is mismatched math.** 80 registrations against 400 attendees mixes units. Against the ~650 registrations a 400-person room needs at about 61% show-up, you are at 12%.
- **The "40-50% a month out" guide is a paid-conference ladder.** It is a DevOpsDays checkpoint for paid events with a full sales window, and a free event registers later than that. Even if it did apply, the skill's response to running short is a push brief first, not cancelling.

## 4. Lock dates

| Commitment | Date | Commit figure | Band end and reason |
|---|---|---|---|
| Venue 60% step | Fri 11-06 | Don't cancel. Hold the go/no-go review before this date. | Set by the go/no-go poll, not by the newsvendor rule |
| Caterer guarantee | ~Sun 11-22 (confirm in contract) | **Provisional ≤240 covers**, re-run on the day. If the caterer allows +X% flex, commit 240 / (1+X). | High end of attendance. A person with no lunch costs more than a spare cover, so the cap is the high end. |

- **Re-run on the caterer date.** By then about 90% of registrations are in, so the band narrows hard. The final figure is whatever that run gives, almost certainly below 240.
- **Hand the caterer attendance, not registrations.**

## 5. What to tell the venue

1. Say you are proceeding. Don't signal cancellation, because it weakens your hand.
2. Ask in writing for:
   - the exact fee schedule and step dates;
   - whether a smaller room or a closed balcony or section is possible without it counting as a cancellation;
   - whether the 21-day step can move or be reviewed, and the deadline for a room downgrade.
3. Tell them you will confirm the final room by 11-05.
4. Share a headcount of about 150-250 expected on the day, not 350 or 400.
5. If they say no to downsizing, you have still lost nothing. 350 seats at 240 attendees is 69% full.

## 6. What to tell the caterer

- The guarantee will land between 150 and 240 covers. The exact number comes on the lock date.
- Ask three things:
  - the flex: how far the guarantee can rise after the lock, and how late;
  - whether it can drop, and the floor;
  - whether they can push the lock to 3 days out, or offer tiered pricing.
- Don't quote registrations. Quote attendance.

## 7. Milestones and tripwires (declared now, before the readings)

| Days out | Date | Expected on hand | If it lands outside | Owner |
|---|---|---|---|---|
| 21 | 11-06 | 99-149 | Below 99: go/no-go escalation to risk-management, plus budget-tier downgrade. Above 149: re-run the forecast. | You, then risk-management |
| 14 | 11-13 | 113-200 | Below 113: push is not working. Hand the gap to event-marketing-plan. | event-marketing-plan |
| 5 | 11-22 | 136-333 | The wide range is by design: the hackathon curve closes at 7 days. Re-run the whole band that day. | You |

- **Proposed go/no-go criterion (confirm with the group before 11-06):** at least 100 registrations on hand at 21 days out is a go.
- **I have not set a break-even threshold,** because I don't know your costs. A miss against this criterion is an input to the poll, not a cancellation. The demand verdict itself belongs to event-market-fit.
- **Response order when running short:**
  1. Push brief: give event-marketing-plan the gap to the mid, the 11-06 deadline, and the segment furthest behind.
  2. Budget-tier downgrade of the scalable lines.
  3. Go/no-go escalation.
- **Don't rescue the forecast with a discount or a moved date.** Your event is free, so this barely applies. The rule still holds for any announced gate.

## 8. Capacity

- Room: 350 seats. High-end attendance is 240, which is 69%, or 48% at the 50% show rate.
- You never cross capacity, so no second room or larger-room option is needed, and there is no waitlist question.
- Only the sponsors' 400 would exceed the room.

## 9. Peer organizer: ask this week

This meets the skill's condition for a comparable-event curve: a first edition, a large lock date, and a peer reachable within the 11 days before 11-06.

Ask for:

- cumulative registrations by days-out, whatever the granularity;
- final registrations and check-ins, and whether 500 was either;
- comps and walk-ins;
- when they announced speakers and ran pushes;
- whether it was a repeat edition, plus city size and audience.

Run their curve as a third reference. If it shows they were also near 16% on hand at 32 days out, that is your best evidence against cancelling. Their 500 is **not** a forecast for you on its own.

## 10. Attendance by ticket type

| Type | Registrations (mid) | Show rate and label | Attendance |
|---|---|---|---|
| Free registrants | ~243 | 50-72%, sourced (Event Tech Live band; PheedLoop median) | **~122-175** |
| Speakers, sponsor staff, volunteers | not provided | self-set, none published | add separately |
| Walk-ins | unknown | no prior count | unknown |

Within the same event, late registrants show up at practically the same rate as early ones, so I applied no late discount.

## 11. Do this week

1. Reset sponsor expectations to about 150-250 attendees, with the reasoning above.
2. Email the venue and caterer the asks in sections 5 and 6.
3. Email the peer organizer the list in section 9 today.
4. Re-run the script at each reading, and keep each forecast unedited.
5. Hold the go/no-go review before 11-06, with the 100-registration criterion agreed in advance.