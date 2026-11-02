Verdict: not enough. Your plan covers failed hardware and lost files, but not the failure you actually had last year, a recorder that stopped without anyone noticing. Fix that first.

## Gaps, ranked

1. **Nobody watches the recorders.** This is last year's failure, and nothing in the plan addresses it.
   - Assign one named person per room as a monitor. Put it on their schedule.
   - They check at the start of each session, then every 10 minutes: record light on, timecode running, file size growing.
   - Use headphone monitoring or a level meter to confirm the audio is live. A running recorder can still capture silence.
   - Check again at the end of each session, before the speaker leaves the stage.
   - Use a one-line checklist card per room.
2. **No redundant capture.** Spare gear in a cupboard only helps if someone notices the failure in time. A live second recording does not need that.
   - Run a second recorder in each room: a cheap audio recorder on the desk mixer feed, or a second camera.
   - 44 session recordings is the minimum. With two sources, one failure does not lose a talk.
   - Audio alone is enough to save a talk. Slides can be re-synced afterwards.
3. **Spares are in the wrong place.** The cupboard is at the back of the hall.
   - Keep one spare kit per room, not one for both.
   - Put it at the monitor's seat, powered and tested.
   - The swap has to take under 2 minutes. Between sessions you have maybe 10 minutes, and mid-talk you have none.
4. **Backup runs only at the end of the day.** A card that dies or goes missing before then has no second copy.
   - Copy each card right after each session, or at least at lunch and at day end.
   - Do not reformat any card until the copy is verified.
   - Rotate cards: one fresh card per room per half-day, labeled with room, day, and session numbers.
5. **No verification of the copy.** A copy that finished is not a copy that is good.
   - Compare checksums (`rsync -c`, or `shasum` on both sides).
   - Open each file and check duration against the schedule.
   - Listen to 10 seconds at the start, middle, and end of every file.
6. **The NAS is a second copy in the same building.** Fire, theft, and a bad office night all take both.
   - Add a third copy off-site: a cloud upload or a portable drive that goes home with someone.
   - Do this before the SD cards are wiped.
   - Rule of thumb: 3 copies, 2 media types, 1 off-site.
7. **Power and storage limits are unchecked.**
   - Do the arithmetic: card capacity vs. longest session at your bitrate, plus margin. Many cameras also split files or cap clip length.
   - Use mains power or a battery with 2x the expected runtime.
   - Check NAS free space against the full 2-day total plus overhead.

## Minimum change set

1. Name a monitor per room, and give each a checklist card.
2. Add a second audio recorder per room.
3. Move one spare mic and one spare camera to each room.
4. Copy cards after every half-day, verify, then wipe.
5. Add one off-site copy each evening.

## Time cost

About half a day to buy, label, and test the extra gear. After that it is roughly 5 minutes of monitor checks per session, and 20 to 30 minutes per evening for copying and verifying.

## Dry run

Do a full test the day before:
- Record 10 minutes in each room.
- Pull the power on the main recorder halfway through.
- Confirm the monitor notices and the second recorder still has the audio.
- Run the copy and verification steps on those test files.

Next: tell me the recorder and camera models, bitrate, and card sizes. I can then check capacity and clip-split limits and draft the per-room checklist card.