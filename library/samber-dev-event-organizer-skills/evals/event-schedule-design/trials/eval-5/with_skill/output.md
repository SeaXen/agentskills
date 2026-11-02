# ScaleConf Nairobi: schedule design, status and decision needed

**The grid can't absorb 58 talks, and the fifth room doesn't change that.** Which talks fill the slots is a format and selection decision, so I stopped at a validated skeleton instead of forcing 58 into it. Your 900 USD would buy a fifth track, but it wouldn't solve the shortfall.

## 1. The slot math

| Option | Slots | Fits 58? |
|---|---|---|
| 4 rooms × 45 min (your plan) | 32 | ❌ 26 short |
| 5 rooms × 45 min (+900 USD) | 40 | ❌ still 18 short |
| 4 rooms × 30 min (25-min talk plus 5 min buffer) | 13 per room, 52 total | ❌ 6 short |
| 5 rooms × 30 min | 65 | ✅ 7 spare, and 900 USD plus a new track |

The skeleton has about 3 hours of plenary, lunch and breaks. Even with 30-minute slots and no other change, 4 rooms top out at 52.

## 2. Why I didn't add the fifth track

- The event-schedule-design skill treats a grid that won't fit as a reason to cut or reshape talks, not a reason to add a track.
- Track count and session-format mix belong to `event-format-selection`. Adding a track mid-build changes the content mix that decision was coupled to.
- A fifth track also splits the audience further, shrinks per-room attendance and adds a room to the clash and corridor checks.
- You said a fifth track "sounds fine". If you still want it, make that call upstream as a deliberate format decision. The 5 × 30 min row above is the version that fits.

## 3. Ways to reach 58, cheapest first

Pick one.

- **A. Waitlist 26 talks.** Keep 4 rooms and 45-min slots, and select down to 32. This costs 0 USD and changes nothing in the format. The cost is that 45% of accepted talks lose their slot, which is a speaker-communication problem. Acceptance outran capacity, so the fix belongs in `event-talk-selection`.
- **B. Lightning blocks.** Turn 13 of the 32 slots into 3 × 15-min lightning blocks (39 lightning talks plus 19 full talks = 58). It needs 39 speakers willing to cut to 15 minutes, and it makes the program 40% lightning. That is a format change, so decide it in `event-format-selection`.
- **C. Second day or evening block.** This is the only option that keeps every talk at full length. It adds venue, catering and travel cost, and it breaks the one-day constraint.
- **D. 5 rooms × 30 min.** This fits all 58 and costs 900 USD plus a fifth track. It has the most knock-on effects.
- **Mix.** For example, 5 rooms × 45 min (40 slots) plus 9 lightning conversions (+18) gives 58. This is the most complex option and I don't recommend it.

**Recommendation: A, or A plus a small B.** Cut to the 32 strongest, and convert a few slots to lightning only if specific speakers want it. Nobody has to rent anything, and no format decision has to be reopened. A one-day event of 45-minute talks with a waitlist also keeps the program stronger. Don't spend 900 USD to avoid 26 disappointing emails.

## 4. Validated skeleton (4 rooms, 45-min slots)

This works for options A and B. The times add up to 540 minutes and hold 8 slots per room, so 32 slots in total.

| Time | Block |
|---|---|
| 09:00–09:30 | Opening plenary (all rooms) |
| 09:30–10:15 | Slot 1 |
| 10:15–10:35 | Break |
| 10:35–11:20 | Slot 2 |
| 11:20–12:05 | Slot 3 |
| 12:05–13:05 | Lunch |
| 13:05–13:50 | Slot 4 (post-lunch dip: use lighter formats here) |
| 13:50–14:35 | Slot 5 |
| 14:35–14:55 | Break |
| 14:55–15:40 | Slot 6 |
| 15:40–16:25 | Slot 7 |
| 16:25–16:45 | Break |
| 16:45–17:30 | Slot 8 |
| 17:30–18:00 | Closing plenary |

- **Slot standard:** the slot is 45 minutes and the talk is about 40, with 5 minutes of buffer inside the slot. Tell speakers both numbers.
- **Plenaries:** the opening and closing bookend the day and reset any per-track drift.
- **Pacing (my judgment, not a measured number):** put dense content in the morning and lighter or lightning formats right after lunch. The last slot, 16:45, is the likely graveyard slot, so put a strong draw there.
- **Track starts:** I recommend synchronized starts with 4 rooms. Switch to staggered starts if the corridors jam. I can't confirm this without the venue layout.

## 5. What I can't finish without your answers

I haven't assigned talks to slots, run the clash passes or sized the buffer, because those need inputs I don't have:

1. **Option:** A, B, C, D or a mix?
2. **Rooms:** seated capacity of each, and walking minutes between them. This sets the buffer and decides whether 5 minutes inside the slot is enough.
3. **Venue contract:** door times, catering windows, and whether any room is held only for part of the day.
4. **Speaker availability:** each speaker's window, including the intersection for multi-speaker talks, plus any travel constraints.
5. **Fixed points:** keynotes, sponsor slots, and anyone who can only speak at one time.
6. **Publication date:** and whether attendees will travel to reach you. Release the grid early and treat it as a living document.

## 6. Disruption priority order (for `event-run-of-show`)

1. Protect the opening and closing plenaries.
2. Protect the headline talks people came for.
3. Minimize how many other sessions a fix disturbs.
4. Lock the revised grid for the rest of the block.

## 7. Next step

Send me your choice for item 1 and the answers to 2–6. I'll then run the full clash pass (room overlap, speaker double-booking, room and speaker availability windows), assign rooms by expected audience size and return the complete grid. If you choose A, I'll also help sort the 58 talks into 32 and 26 first.