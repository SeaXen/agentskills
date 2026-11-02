# DataMesh Summit: buffer scheme

Status: buffer scheme only. I don't have the room list, talk list or speaker windows yet, so there is no full grid. Open items are at the end.

## 1. Verdict on the COO's model

Take the idea of reading buffer use as graded. Leave out all three numbers.

| COO input | Decision | Why |
|---|---|---|
| Buffer = 50% of lead time | ❌ Drop | It scales with session length. Your lateness comes from walking, which doesn't depend on session length. A 25-min lightning talk still needs the same 7-min stair walk. |
| 33% / 67% escalation | ❌ Drop | These come from a production line's variability. Nothing says a conference room overruns the same way. I replace them with thresholds in minutes, tied to the walk (section 4). |
| 85% room utilization | ❌ Drop | This is a line-capacity target. A 15-min gap on a 45-min session already gives 75% by construction. The real room rule is that expected audience must fit the seats, and overflow is worse than an empty room. |
| Graded buffer reading | ✅ Keep | Comfortable / tightening / blown shows drift while there is still time to act. |

The skill marks all three figures as ones that "must not be reused" outside manufacturing. If the COO pushes back, the answer is that your own data set the buffer. Last year's zero-gap grid ran about 10 minutes late, and the worst walk is 7 minutes.

## 2. The scheme

**Fixed, published 15-minute gap between every session, in every room. Zero-gap is off the menu.**

- **Cycle:** 45-min session + 15-min gap = 60 min. Sessions start on the hour.
- **Speaker brief:** 40 min talk + 5 min Q&A, hard stop at 45. Brief the session length and the gap separately, or speakers will spend the gap.
- **Why 15:**
  - The worst walk is 7 min (floor 1 ↔ 3, stairs).
  - Last year's ~10 min of lateness on zero gap is the observed all-in cost of a move: walking, queueing and finding a seat.
  - A 15-min gap covers that, plus about 5 min of speaker overrun.
- **Why published and uniform:**
  - Attendees can see the time and plan to leave on schedule.
  - A buffer hidden inside the slot reads as dead air, and an overrunning speaker spends it.
  - Uniform is simplest. A different gap per room pair would force ragged start times across five rooms.
- **Worked check:** if a talk overruns by 5 min, 10 min remain, which is 7 min of walking plus 3 min to sit. That works. An overrun of 8 or more min does not.

**Cost you must decide on:** 45 → 60 min per cycle means 25% fewer session slots per room per day. For example, 8 slots in 6 hours becomes 6.
- Choose between fewer sessions, a longer day, or shorter breaks.
- Do not add a track to compensate. That decision belongs to `event-format-selection`.

## 3. Room and floor placement

This keeps the 7-minute stair walk rare.

- Match rooms to expected audience first, then to adjacency.
- Put the keynote room and the highest-draw sessions on floor 1:
  - The largest crowds avoid the stairs and the slow lift.
  - Step-free attendees stay on the floor with the most content.
- Put tracks that share an audience on the same or adjacent floors. Never put two tracks that audience wants on floors 1 and 3.
- Group adjacent slots by topic where you can, so people stay in one room across two sessions.
- Make breaks and lunch long enough for the stairs. Lunch and plenaries also reset any drift that built up in the morning.
- The slow lift is untimed. Measure it under load (section 6). If it can't move step-free attendees between floors inside the gap, they need their sessions on one floor.

## 4. Graded buffer reading (my thresholds, set to match the walk)

I measure the gap left after the previous session actually ends. This is the minutes version of the COO's zones.

| Zone | Gap remaining | Meaning | Action |
|---|---|---|---|
| 🟢 Comfortable | ≥ 12 min | Overrun ≤ 3 min. 7 min walk plus ≥ 5 min to sit. | None. |
| 🟠 Tightening | 8–11 min | Overrun 4–7 min. Stair movers arrive with ≤ 4 min to spare. | Room volunteer shows the speaker a card at minute 40. |
| 🔴 Blown | ≤ 7 min | A floor 1 ↔ 3 mover cannot arrive before the next start. | Chair stops Q&A. Brief next speakers to keep their first 3 min low-stakes (judgment, unsourced). |

These thresholds are mine, not a benchmark. Revise them from recorded data after the event.

## 5. Track-start alignment

Synchronized starts, on the hour.
- Five rooms is small, and the 15-min gap spreads the movement.
- I assume the stairwell is wide enough to take a full room at once.
- **Flip to staggered** if the timed crowd walk (section 6) shows the stairwell jams. In that case, offset the floor-3 rooms by about 10 min. This is PyCon US's approach with five rooms.

## 6. Do before publishing

1. **Time the walks.** Measure floor 1 ↔ 2, 2 ↔ 3 and 1 ↔ 3 with a crowd (10+ people), not one person.
   - The 7 min is a walking-pace figure. A crowd on stairs is slower.
   - If the crowd takes more than 9 min, raise the gap to 20.
2. **Time the lift under load** for step-free access.
3. **Check turnover.** If any room switches format (workshop tables back to theatre rows) or needs a real AV reset, 15 min may not be enough for that room. That case calls for gaps sized per room pair.

## 7. Measurement (self-set)

Record these before the event, with the change each would trigger:

- **Gap consumption per room per block, by zone.** If a room is Tightening or Blown in more than half its transitions, raise the gap by 5 min next edition.
- **On-time start rate per room.** A room that drifts all day points to a buffer-sizing problem, not a speaker problem.
- **Post-event survey:** "Were you late to a session because of the walk?" Last year's ~10 min lateness is the baseline to beat.

## 8. Still needed to finish the grid

1. Rooms, seated capacities, and which floor each is on.
2. Venue-fixed windows: doors, catering, room-hire times.
3. Accepted talks with format and track tags.
4. All speakers' availability windows, including co-speaker windows for multi-speaker sessions.
5. Fixed points: keynotes, opening and closing, sponsor slots.
6. Whether any room hosts mixed formats.
7. Publication date, and whether the event repeats every year.

Assumptions I made: the rooms are spread as given, the 7 min is an uncrowded stair walk, and the 15-min gap fits within the venue contract's daily hours.