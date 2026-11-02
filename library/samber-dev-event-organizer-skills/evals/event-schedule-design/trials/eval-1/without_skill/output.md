❌ **Do not publish yet.** The spreadsheet check is clean, but it only tests double-booking. It can't see availability limits, and your own facts show two of them breaking "Observability at 40k events/sec".

## What breaks

**1. Priya can't make 09:30-10:15.**
- Her flight lands at 10:40 and she's good from 11:30.
- The talk ends 75 minutes before she lands, so a co-presenter is absent for the whole slot.
- Dario is free from 08:00, so he's fine.

**2. Hall C isn't available at 09:30.**
- The venue contract gives you Hall C from 12:30, because a school breakfast service runs there until noon.
- Any session in Hall C before 12:30 sits in a room you don't have.
- This isn't limited to the one talk. Every Hall C session before 12:30 is affected.

## Fix before Monday

1. **Filter the grid for Hall C sessions starting before 12:30.** Move or swap each one. Decide how to treat 12:00-12:30: the contract says 12:30, so I'd treat Hall C as unusable until then.
2. **Reschedule the observability talk.**
   - Put it at 11:30 or later at the earliest.
   - Better is 12:30 or later, because a delayed flight would otherwise sink it.
   - Keep a fallback ready, such as Dario presenting solo or Priya joining remotely.
   - Confirm both speakers on the new slot.
3. **Check the capacity effect.** Losing Hall C until 12:30 removes about 3.5 hours of room time. Check that the displaced talks fit in Halls A and B, and that the day stays inside 09:00-18:00.
4. **Re-run the conflict check after the moves.** Moving talks can create new room or speaker clashes.

## Other checks before it goes out

- **Speaker availability for all 61 talks.**
  - Ask whether the spreadsheet has an availability column.
  - Run each speaker's arrival, departure and "good from" times against their slots.
  - Priya's constraint wasn't in the grid, so others may be missing too.
- **Room capacity versus demand.**
  - Hall C seats only 90.
  - Look for headline or popular talks in Hall C or Hall B (140).
  - Put the likely high-demand sessions in Hall A (300).
- **Contract constraints on Halls A and B.** Check them for other restrictions (blackout windows, setup times, early closes), not just Hall C.
- **Changeover time.** Look for back-to-back sessions with no buffer, especially for speakers who move between rooms (such as a speaker with two talks, or a chair).
- **Day boundaries.** Confirm no talk starts before 09:00 or ends after 18:00. Confirm breaks, lunch and keynotes are in the grid.
- **Co-presenter talks.** Check every other talk with multiple speakers against each person's availability, not just the first-listed one.
- **Late schedule changes.** After publishing, tell speakers what changed and when.

## Suggested next step

Send me the grid, or the speaker availability list. I'll cross-check all 61 talks against speaker windows, the Hall C restriction and room capacity, and give you a corrected list of conflicts.