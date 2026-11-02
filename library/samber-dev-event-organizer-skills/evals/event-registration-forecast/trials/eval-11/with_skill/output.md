**Recommendation: 447 room-nights, covering the night before day one and the night between the two days. Don't take the third night, and don't lock today.**

⚠️ I could not run `forecast-registrations.py`. The sandbox blocked writing the CSVs, so I did the arithmetic by hand with the script's stated method. Rerun it before the lock date with the full export, not just the one 40-day point.

**1. Readings and assumptions**
- Today is 40 days out with 240 registrations, net of comps.
- Last year's export gave 230 at 40 days out and 470 final. That is a single mid-curve point, with no early-bird or announcement dates.
- I assumed a paid event, with the same format and posture as last year.
- I don't know the comps, the ticket mix, or whether a spike sits inside the 240. Please check whether a push or announcement landed in the last week.
- Out-of-town share is 55%, from last year's postcodes. I assumed one guest per room.
- The hotel's answer on adding rooms later is unknown.

**2. References and method**
- Last year's edition: 230/470 = 48.9% on hand at 40 days. Multiplicative pickup applies, since more than 15% of the curve is in. 240 / 0.489 gives **490**.
- Pooled lead-time curve (PheedLoop, 467 events): 46.6% on hand at 40 days, interpolated between 30.5% at 61 days and 55.8% at 28 days. 240 / 0.466 gives **515**.
- I did not shift last year's curve, because I have no milestone dates.

**3. Band for final registrations, net of comps**
- Low **490**, mid about **503**, high **515**.
- The band is narrow because it rests on two references and no recorded forecast error. This is an unrecorded second edition, so don't read the narrow spread as confidence.
- The method comes from hotel-style booking-curve pickup forecasting.

**4. Lock-date table: hotel block**

| Case | Registrations | Show rate | Attendance | Room-nights (× 0.55 × 2 nights) |
| --- | --- | --- | --- | --- |
| Low | 490 | 83% (PheedLoop paid median) | 407 | **447** |
| Mid | 503 | 83% | 417 | 459 |
| High | 515 | 90% (low end of the paid band) | 464 | 510 |

- **Commit at the low end: 447 room-nights, about 224 per night.** The reason is that an over-committed block costs attrition under the 80% guarantee. An under-committed one costs only the chance to add rooms later.
- **That reasoning holds only if the hotel confirms in writing that rooms can be added at the group rate.** Ask today. If the answer is no, or silence, move to the mid, 459. The cost of coming up short then becomes attendees paying rack rate, and the gap between low and mid is only 12 room-nights.
- I applied no flex, since none is confirmed.
- **Don't lock today.** The cutoff is in 10 days, and the commitment is the figure from a run made on the lock date. 447 is provisional until then.

**Why not the co-organizer's three nights at the mid**
- Three nights at the mid is 417 × 0.55 × 3, about **688** room-nights.
- The 80% guarantee on 688 is about 550 room-nights.
- If the night after day two stays empty, expected use is about 459, which is 67% of the block. That is roughly 91 room-nights paid for and never used.
- A two-day event needs the night before day one and the night between. Add the third night only if your own data shows out-of-towners staying after day two. Ask the hotel for it as an option instead.

⚠️ **Capture risk.** My formula assumes every out-of-town attendee books through the block. At a 447 block, the 80% guarantee needs about 358 room-nights used. If less than roughly 80% of out-of-towners book through the block, you owe attrition even when the forecast is right. Look at last year's pickup. If you have no figure, commit lower than 447.

**5. Milestone: the 30-day lock reading**
- On the pooled shape, 54.3% is on hand at 30 days. That puts **266–280** registrations on hand, declared now.
- A reading below 266 fires a push brief to `event-marketing-plan` for the gap and, if rooms can't be added, a cut to the block. A reading above 280 means re-running and growing the block if the hotel allows.
- Owner: you, the organizer.
- Last year's own 30-day count would give a better range, so pull it from the export.

**6. Capacity**
- Not assessed: I don't have the room limit.

**7. Attendance by ticket type**
- Paid at 83% (PheedLoop paid median) to 90% (low end of the paid band): about 407–464 attendees. Both rates are sourced.
- Comps (speakers, sponsors, volunteers) are not in the 240 and carry no published rate. If any need hotel rooms, add them on top.
- Walk-ins and day-two attendance are unknown.

**Next steps**
- Ask the hotel in writing whether rooms can be added at the group rate.
- Rerun the script with the full export, adding last year's 30-day count.
- Record this forecast unedited, so you can compute the signed error after doors.