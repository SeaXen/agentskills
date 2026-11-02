# KernelConf Berlin grid: pre-publication review

**Don't publish yet. The grid has at least one session that can't happen as scheduled, and the check your ops lead ran wouldn't have caught it.**

## 1. The check that was run

Your ops lead checked two things: no room holds two sessions at once, and no speaker appears twice at the same time. Those are the two arithmetic clash types, and the grid's own data is enough to check them. There are two more:

| # | Clash type | Run? |
|---|---|---|
| 3 | Two sessions in the same room | ✅ Done |
| 4 | One speaker in two simultaneous sessions | ✅ Done |
| 1 | Session outside its room's contract window | ❌ Not run |
| 2 | Session outside a speaker's availability, using the intersection for co-speakers | ❌ Not run |

Types 1 and 2 fail silently. Nothing on the grid looks wrong while the room is locked or the speaker is still in the air.

## 2. "Observability at 40k events/sec" fails twice

It's currently scheduled for 09:30-10:15 in Hall C.

| Constraint | Window | 09:30-10:15 fits? |
|---|---|---|
| Hall C contract | from 12:30 | ❌ Fails by 3 hours |
| Dario Venn | free from 08:00 | ✅ |
| Priya Raghunathan | lands 10:40, good from 11:30 | ❌ Fails by 2 hours |
| **Co-speaker intersection** | **from 11:30** | ❌ |
| **Room ∩ speakers (Hall C)** | **from 12:30** | ❌ |

- Dario alone passes. If anyone checked the speakers one at a time, starting with whoever is listed first, it would look fine.
- Priya would be in the air at the scheduled start.
- Hall C is a school breakfast service until noon.

## 3. Hall C's morning is the bigger problem

Hall C isn't available before 12:30 on the contract. So every session you've placed in Hall C before 12:30 fails type 1, not just this one. I don't have your grid, so I can't count them. Count them now.

Those sessions need a new room and slot, and Halls A and B have to absorb them. Check that they can. Three rooms with Hall C unusable until 12:30 leaves less room than the grid assumed.

One discrepancy to resolve with the venue first. You said breakfast runs until noon, but the contract says 12:30. I'd treat 12:30 as the limit until the venue confirms the room is actually clear and set up before then. If they confirm 12:00, you gain 30 minutes in Hall C.

## 4. Fixing the observability talk

- **Option A: Hall B (140 seats), 11:30 or later.** This is the better fit. Priya has only 50 minutes between landing and her stated availability, which is thin. Take 11:30 as a hard floor, not a target. Use the later of 11:30 and the first Hall B slot after the break.
- **Option B: Hall C, 12:30 or later.** It's valid, but the slot is likely to collide with lunch. If it lands right after lunch, it's also in the post-lunch dip. That makes it a weaker place for a dense, technical talk.
- **Capacity.** A talk on a 40k events/sec pipeline probably draws a crowd. That's my estimate, not a measured figure. Check last edition's counts. If it could plausibly overflow 90 seats, Hall C is the wrong room regardless of timing. Overflow gets turned away at the door. An over-large room only looks quiet.

Whichever slot you choose, you displace whatever sits there now. Compute that talk's speaker windows too (type 2) and re-run all four checks after every move. Each move invalidates the previous pass.

## 5. What else to check before it goes out

1. **Every other multi-speaker talk.** Compute each one's intersection of speaker windows and record it per session, before slotting.
2. **Every speaker's window, not just this one.** Do you have availability from all speakers for all 61 talks? Dario and Priya's constraints surfaced because they were mentioned. If your CFP form didn't collect availability, ask every accepted speaker now and wait for replies. A correction after publication is public.
3. **Travel windows.** A speaker who lands in the morning can't open the day. Check for other morning arrivals, and for anyone with a departure that cuts off an afternoon slot.
4. **Other room windows.** Hall A and Hall B contract start and end times, catering windows, and any parts of the day you only hold part of. I only know about Hall C.
5. **Room-capacity match.** Give each of the 61 sessions an expected audience estimate, then compare it against the seats (300/140/90). Clash-free doesn't mean the sessions fit their rooms.
6. **Buffer and walking time.** What's the published gap between sessions, and how far apart are the halls in walking minutes? A zero-gap grid is only acceptable if the rooms are right next to each other. Also, is a 09:00-18:00 day with three rooms emptying at once fine for your corridor?
7. **Turnover.** Does any room switch format between consecutive sessions (workshop to talk, or a panel)? If so, it needs more than the default gap.
8. **Fixed points and breaks.** Where are the opening, keynote, lunch and coffee breaks? Are they placed first, and do they sync all three tracks?
9. **Audience overlap.** Name any two sessions that the same attendees would want, and make sure they aren't head to head.
10. **Pacing.** Check what sits right after lunch and in the last slot of the day. Both are historically weak positions. This is a judgment read, not a measured result.

## 6. Publication on Monday

If you can finish steps 3 to 5 before Monday, publish then. If you can't, hold back. Delaying a few days costs less than a public correction after attendees have booked travel around the grid.

I'd publish and iterate (the sourced default). Include a visible "what changed" note if you change the grid after tickets are sold.

## 7. What I need from you

- The full grid (room, time, talk, speakers) as a CSV or paste, so I can run all four checks across all 61 talks.
- Every speaker's availability window, especially co-speakers.
- Walking time between halls, and the contract windows for Halls A and B.
- Whether the venue's 12:00 and 12:30 are the same constraint.

Once I have the grid, I'll return the flagged sessions and a corrected layout.