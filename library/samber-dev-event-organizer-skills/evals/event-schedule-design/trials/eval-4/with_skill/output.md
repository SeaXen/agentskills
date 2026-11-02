# GoNorth schedule plan: single track, 130 people, one room

This is a draft for you to validate. I used assumptions where I had no answer, and they are listed at the end.

## What you actually need to do

The checklist is built for multi-track events. With one room and nothing running in parallel, most of it doesn't apply.

**Do these 5 things:**
1. ✅ Check that Tomas can physically be there when he speaks. This is the only clash check left.
2. ✅ Standardize one slot length so talks can be swapped.
3. ✅ Place the opening, closing, lunch and breaks first.
4. ✅ Put the buffer inside each slot, because one overrun delays the whole day.
5. ✅ Write the disruption order into the grid, then publish early.

**Delete these** (they are deleted, not parked at the bottom):
- ❌ **Clash matrix.** Nothing overlaps, so there are no same-room, double-booking or audience-overlap clashes. Only speaker availability stays.
- ❌ **Room capacity matching.** There is one room. Check once that its seated capacity is at least 130 plus speakers and staff.
- ❌ **Corridor flow and staggered starts.** Everyone moves at once between one room and the break area.
- ❌ **Room-turnover gaps.** One room and one format means nothing changes between sessions. This changes if you run a panel or workshop.
- ❌ **Walking-distance buffers.** There is no room-to-room walk.

## 1. Slot standard

- Each talk gets a **30-minute slot**: 25 minutes of talk plus 5 minutes of changeover and questions, all inside the slot.
- Tell speakers both numbers. Otherwise they will use the full 30.
- Opening is 10 minutes. Closing is 15 minutes.

## 2. Fixed points and the Tomas constraint

- **Opening 09:30.** Doors are at 09:00, so this gives 30 minutes to arrive and get coffee.
- **Closing 17:05–17:20.** This leaves 10 minutes of reserve before your 17:30 hard out. The room is yours until 18:00, so there is a further 30 minutes of margin after that.
- **Tomas Ek: slot T5, 12:00–12:30.**
  - He lands at 10:50, so he cannot open the day, and he should not be in the first morning block.
  - T5 gives about 70 minutes between arrival and stage, which covers the walk from the station, an AV check and some train slack.
  - It is the last slot before lunch. Lunch is the natural shock absorber if he runs late.

## 3. Breaks and sync points

Because it is one room, every break is a whole-audience reset.
- **Morning break:** 20 minutes.
- **Lunch:** 60 minutes, 12:30–13:30.
- **Afternoon breaks:** 20 and 15 minutes.
- **Longest stretch without a break:** 90 minutes (three talks, 11:00–12:30).

## 4. Room

- One room.
- The only check is that its seated capacity is at least 130 plus staff.

## 5. The grid

| Time | Item |
|---|---|
| 08:30 | Room setup (your window starts) |
| 09:00 | Doors, coffee |
| 09:30–09:40 | **Opening** |
| 09:40–10:10 | Talk 1 |
| 10:10–10:40 | Talk 2 |
| 10:40–11:00 | Break |
| 11:00–11:30 | Talk 3 |
| 11:30–12:00 | Talk 4 |
| 12:00–12:30 | **Talk 5: Tomas Ek** |
| 12:30–13:30 | Lunch |
| 13:30–14:00 | Talk 6 |
| 14:00–14:30 | Talk 7 |
| 14:30–14:50 | Break |
| 14:50–15:20 | Talk 8 |
| 15:20–15:50 | Talk 9 |
| 15:50–16:05 | Break |
| 16:05–16:35 | Talk 10 |
| 16:35–17:05 | Talk 11 |
| 17:05–17:20 | **Closing** |
| 17:20–17:30 | Internal reserve (unpublished) |
| 17:30 | Hard out |
| 18:00 | Room window ends |

## 6. Clash-detection depth

I ran one check: **speaker availability against slot time**.
- ✅ Tomas is placed after his arrival with margin.
- ⚠️ I have no other speaker's window. Ask all 10 others now.
- ⚠️ If any talk has co-speakers, compute the intersection of their windows. Do not check only the first name on the proposal.
- Re-run this check after every change, including changes made after publication.

## 7. Buffer

- It is a **slot-internal buffer of 5 minutes per talk**. There are no published gaps and no walking.
- Unpublished reserve: the 10 minutes at the end.
- The 5-minute figure is my default, not a benchmark.

## 8. Track-start alignment

This question doesn't arise with one room. Every start is "synchronized", and the plenary points are the opening, lunch and closing.

## 9. Pacing read (my judgment, not a measurement)

- **Post-lunch dip (13:30).** Sourced direction: the dip is circadian. Put your lightest or most interactive talk in T6, not the densest one.
- **Last-day, last-slot weakness (T11, 16:35).** Sourced direction: the last slot is the worst-attended position at the conferences studied. Put a strong, lively talk in T11 rather than the densest. The closing then lands on a high.
- **Start of day (T1).** Put an accessible, high-draw talk in T1 and T2 to set the tone.
- **Magnitudes.** I have no developer-conference numbers, so I cite no magnitudes.
- **Content tags.** I have not seen the talk list, so this is a placement rule, not a placement.

## 10. Disruption priority order

1. Protect the opening and closing.
2. Protect the headline talk the audience came for.
3. Disturb as few sessions as possible.
4. Lock the revised grid for the rest of the day instead of re-shuffling.

**Tomas fallback (a swap of exactly two sessions):**
- **Go/no-go at 11:30.** If Tomas is not at the venue, swap T5 and T6.
- The T6 speaker goes at 12:00 and Tomas goes at 13:30.
- Brief the T6 speaker beforehand that they may go 90 minutes early.
- Give Tomas a staff contact and ask him to message from the train.
- Executing this live belongs to `event-run-of-show`.

## 11. Publication

- **Release early and iterate.** Publish the grid as soon as you have validated it and every speaker has confirmed their window.
- Do not publish the Tomas fallback.
- I don't know your date. It depends on whether tickets, travel booking or a sponsor commitment sets the deadline, so give me that date.
- If attendees travel to GoNorth, do not wait for a "final" grid.

## Measure (my thresholds, not benchmarks)

Record these before the event:
- **Start-time drift per talk.** If drift builds up, enlarge the buffer, not the speakers' guilt.
- **No-show or drop-off per slot**, to find your own graveyard slot.
- **Post-event survey:** "Which talk did you almost skip?"

## Assumptions to confirm

1. Is there one catering window or a fixed lunch time? I assumed it can sit at 12:30–13:30.
2. How long does Tomas need from the station to the stage?
3. Is the format all talks with no panel or workshop?
4. Are there any other speaker constraints or co-speakers?
5. Do you have a publication deadline?

Validate in this order: fixed points and breaks, then the Tomas slot, then the full grid.