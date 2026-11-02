# ElixirConf Nordics: schedule grid (two days, four rooms)

The grid is built but no talks are placed in it yet. You gave me counts, not the talk list. You also didn't give room capacities, walking distances, venue windows or speaker windows. The interview and the clash passes depend on those, so I used the assumptions below, and each one is listed under "What I need from you".

## 1. Slot standard

| Slot | Length | Holds |
|---|---|---|
| Standard | 50 min | A 40-minute talk including Q&A, plus 10 minutes of buffer inside the slot |
| Lightning | 50 min | 3 × 15-minute talks plus 5 minutes of buffer |
| Keynote | 50 min | Welcome or thanks plus a keynote of about 40 minutes |

- Your 6 lightning talks fill 2 lightning slots.
- Tell speakers both numbers, the talk length and the slot length. Otherwise they will use the whole slot.
- The 40-minute talk length is my assumption. Say so if your speakers were briefed on something else.

## 2. Fixed points

- **Opening keynote:** Day 1, 09:00–09:50, Room A. It opens the programme and pulls everyone into one room.
- **Closing keynote:** Day 2, 16:00–16:50, Room A. It occupies the last slot of the last day, which is the weakest slot to leave to ordinary sessions. A plenary there brings everyone back together.
- **Single-day speakers:** none were given. Place any you have before anything else.

## 3. Breaks, plenary points and the hidden AV block

| Day | Time | Item |
|---|---|---|
| 1 | 09:50–10:20 | Coffee |
| 1 | 12:50–14:00 | Lunch (published as 70 minutes) |
| 1 | **13:00–13:25** | **AV recalibration, internal blocker, not on the programme** |
| 1 | 14:50–15:20 | Coffee |
| 2 | 10:20–10:50 | Coffee |
| 2 | 12:30–13:40 | Lunch (70 minutes, matching Day 1) |
| 2 | 14:30–15:00 | Coffee |

- **Where the AV block sits:** attendees see only "Lunch". The 25 minutes cost no programme time because the rooms are empty at lunch anyway.
- **Margins around it:** 10 minutes after the morning sessions end, so speakers and attendees can clear out. 35 minutes before the 14:00 start, so afternoon speakers can run their tech checks on freshly calibrated AV.
- **If it overruns:** the speaker tech checks are cut first. The 14:00 start does not move.
- **Lunch length on both days:** I made both lunches 70 minutes so Day 2 doesn't look different. That is a cosmetic choice, not a requirement.
- **What the venue must confirm:** the recalibration must be allowed to run in all four rooms at once. If it needs rooms one at a time, it still fits in the 70 minutes.
- **Run-of-show:** this block is internal-only and goes into the staff version of the run-of-show, not the public grid.

## 4. Room assignments

I have no capacities, so these are defaults. Check them against your venue before anyone is placed.

- **Room A:** assumed largest. It hosts both keynotes and both lightning slots, because lightning slots usually draw the most people.
- **Rooms B and C:** standard sessions.
- **Room D:** morning sessions only. Its afternoon cells are left open (see section 5).
- **Midpoint swap:** if your rooms differ a lot in size, swap which track holds the larger room at the Day 1 / Day 2 boundary. That way one track doesn't sit in the smaller room for both days.
- **Keynote capacity:** Room A must seat every attendee for both keynotes. If it can't, you need an overflow room with a live feed.

## 5. The grid

Cells hold slot IDs, not talks. S01–S34 are the 34 standard slots in reading order, LT1 and LT2 are the lightning slots, and OPEN marks a cell with no session.

**Day 1**

| Time | Room A | Room B | Room C | Room D |
|---|---|---|---|---|
| 09:00–09:50 | **Opening keynote (plenary)** | | | |
| 09:50–10:20 | Coffee | | | |
| 10:20–11:10 | S01 | S02 | S03 | S04 |
| 11:10–12:00 | S05 | S06 | S07 | S08 |
| 12:00–12:50 | S09 | S10 | S11 | S12 |
| 12:50–14:00 | Lunch (internal: AV recalibration 13:00–13:25) | | | |
| 14:00–14:50 | LT1 (3 lightning talks) | S13 | S14 | OPEN |
| 14:50–15:20 | Coffee | | | |
| 15:20–16:10 | S15 | S16 | S17 | OPEN |

**Day 2**

| Time | Room A | Room B | Room C | Room D |
|---|---|---|---|---|
| 09:30–10:20 | S18 | S19 | S20 | S21 |
| 10:20–10:50 | Coffee | | | |
| 10:50–11:40 | S22 | S23 | S24 | S25 |
| 11:40–12:30 | S26 | S27 | S28 | S29 |
| 12:30–13:40 | Lunch | | | |
| 13:40–14:30 | LT2 (3 lightning talks) | S30 | S31 | OPEN |
| 14:30–15:00 | Coffee | | | |
| 15:00–15:50 | S32 | S33 | S34 | OPEN |
| 16:00–16:50 | **Closing keynote (plenary)** | | | |

**Count check:** 34 standard + 2 lightning slots (6 talks) + 2 keynotes = 42 talks. That is 36 filled room cells, 4 open cells, and 40 room cells in total.

**Open cells:** the 42 talks leave 4 of the 40 room cells empty, and I put them in Room D on both afternoons. That keeps the dark cells together instead of scattering empty rooms through the day. You can use them as an open or hallway space, or as overflow if a session needs a second run. Or fill them if more talks arrive.

## 6. Clash detection

- **Done by construction:** same-room overlap. Each cell holds one session, so there are none.
- **Not run yet:** room availability windows, speaker unavailability, speaker double-booking, and the multi-speaker intersection. Each needs data I don't have.
- **Rule when you fill the grid:** re-run all of these after every move. Compute the intersection of all co-speakers' windows for any multi-speaker talk before slotting it.
- **Placement order:** put the hardest-constrained speakers first, meaning those with one possible day or a late arrival. A speaker who lands the morning of a day can't open it.
- **Audience-overlap pass:** this is optional. Use it if two tracks clearly share an audience, so you don't schedule them head to head.

## 7. Buffer

- **Method:** a 10-minute buffer inside each standard slot, and 5 minutes inside each lightning slot.
- **Walking check:** not done, because I don't have walking distances. 10 minutes covers a short walk plus an AV swap. If rooms are on different floors or more than about 5 minutes apart, the grid needs a published gap between slots, not a hidden one.
- **Lightning is tight:** 5 minutes for 3 talks leaves only a couple of minutes per changeover. Use a hard timer and have the three speakers' slides loaded onto one machine in advance.

## 8. Track-start alignment

I used synchronized starts because there are only four rooms. The keynotes and lunches gather everyone, which resets any drift that builds up in individual rooms. Switch to staggered starts if the corridor between rooms is narrow, so room changes don't all happen at once.

## 9. Pacing read (my judgment, not a measurement)

- **After lunch:** the first row of each afternoon starts with a lightning slot in Room A. A change of format fits the post-lunch alertness dip better than another dense talk.
- **Last slot:** the closing keynote fills the last slot of Day 2. Put your strongest standard talks in the row just before it (S32–S34).
- **Day 2 morning:** the first row is a strong slot, so don't waste it.
- **Not sourced to developer conferences:** the post-lunch-dip and weak-last-slot findings come from lab and economics-conference data. Treat them as direction, not numbers for your event.

## 10. Disruption priority order (for the run-of-show)

1. Protect the keynote slots.
2. Protect the headline sessions the audience came for.
3. Fix a problem by disturbing as few other sessions as possible.
4. Lock the revised grid for the rest of the block. Don't keep reshuffling through the day.

## 11. Publication posture

Release early and iterate. Attendees travel to you, so don't wait for a perfect grid. Publish once talks are placed and the mechanical clash checks pass, then revise it openly. I have no date to give you, and you haven't told me what the publication date is serving: ticket sales, travel booking, or a sponsor commitment.

## What I need from you

1. Talk list with track tags, and each speaker's availability window. Multi-speaker talks need every co-speaker's window.
2. Room names, seated capacities, and walking minutes between rooms.
3. Venue contract windows: doors, catering, room hire times.
4. Whether any keynote speaker or other session is fixed to a particular time or day.
5. Whether the AV recalibration needs all four rooms at once and exactly 25 contiguous minutes.
6. The publication date and what it serves.