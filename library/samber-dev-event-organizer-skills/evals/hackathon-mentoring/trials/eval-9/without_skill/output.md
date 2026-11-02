# Laying 19 mentors onto the shift grid

**Next action:** build a mentor × slot table, with tracks as rows and your existing shift slots as columns. Fill it scarcest-cell-first. Don't copy the volunteer grid cell for cell.

## Why mentors differ from volunteers

- Volunteers are interchangeable. Mentors are not: a hardware gap can't be filled by an ML mentor.
- Mentor demand isn't flat. It peaks at kickoff and just before submission, and it dips overnight.
- 19 mentors can't give 3 tracks two-deep coverage for 30 hours. The grid has to carry a demand curve, not a flat headcount.

## Steps

1. **Fix the slot count.** If your shifts start every 3h45 (4h with a 15-minute overlap), 30h gives exactly 8 slots. That gives 8 slots × 3 tracks = 24 cells. Confirm this against your grid.
2. **Build the mentor roster.** Per mentor, record:
   - primary track
   - secondary track, if tagged
   - hours available
   - overnight yes or no
   - max shifts, defaulting to 2
3. **Set target depth per cell.** Use the template below. It is an assumption, so adjust it to your event.
4. **Fill the cells with the fewest eligible mentors first.** That is usually accessibility, or overnight hardware. Place single-tag mentors before multi-tag ones. Keep multi-tag mentors as floaters and gap-fillers.
5. **Run the checks** (below).
6. **Attach backups.** Reuse your backfill list, but tag each entry by track. Name one backup per track, plus one cross-track floater.

## Depth template (assumed)

| Slot | Phase | Hardware | ML | A11y | Floater |
|---|---|---|---|---|---|
| S1 | Kickoff and team formation | 2 | 2 | 2 | 0 |
| S2 | Early build | 2 | 2 | 2 | 0 |
| S3 | Evening | 1 | 1 | 1 | 1 |
| S4 | Late evening | 1 | 1 | 1 | 1 |
| S5 | Deep night | 1 | 0 | 0 | 1 |
| S6 | Deep night | 1 | 0 | 0 | 1 |
| S7 | Morning | 1 | 1 | 1 | 1 |
| S8 | Final push and submission | 2 | 2 | 2 | 0 |

- **Total:** 34 mentor-shifts, which is about 1.8 per mentor.
- **In practice:** 15 mentors take 2 shifts and 4 take 1.
- **Overnight:** hardware keeps a dedicated mentor, because boards and soldering need hands-on help. The floater covers ML and accessibility questions.
- **Per-track need:** hardware 11, ML 9, accessibility 9, floaters 5. You need roughly 6, 5 and 5 single-track mentors, plus at least 3 multi-tag mentors for floating.

## Checks before you publish

- Every cell has at least one confirmed mentor.
- No mentor works more than 2 shifts, and none works two back-to-back.
- Each mentor has at least 8 hours of rest between a night shift and their next shift.
- No track has both mentors rotating out in the same slot, where depth is 2.
- At every handover, the outgoing mentor stays for the 15-minute overlap and hands over the list of teams still stuck. Use one shared note per track.
- Every track's backup mentor is not already on shift in that slot.

## Failure rules

- When a mentor drops, the cross-track floater covers the gap first, then the track backup.
- Never let a volunteer cover a mentor cell. Volunteers triage requests into a "needs mentor" queue per track.

## Open questions

These change the numbers:

1. How many of the 19 are tagged per track, and how many have two tags?
2. What is the start clock time? It decides which slots land overnight and which mentors can take them.
3. Do mentors accept partial shifts, such as 2h, or only full 4h blocks?

Send me the tag counts and start time, and I'll produce the filled grid.