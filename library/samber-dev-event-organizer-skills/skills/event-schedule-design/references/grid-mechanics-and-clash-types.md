# Grid mechanics and clash types

The concepts below are what any grid has to represent, independent of the tool used. A scheduling tool like pretalx documents this model publicly; a spreadsheet can hold all of it.

## Contents

- The grid model
- The four clash types
- Availability: rooms versus speakers
- Multi-speaker intersection
- Breaks versus blockers
- Worked example: a slot that passes and a slot that does not
- What the model does not cover

## The grid model

- **Rooms are columns, time is rows.** A session occupies one room for one contiguous span.
- The grid has a **time resolution** - 5, 15, 30 or 60-minute intervals in the documented tool. A session's duration snaps to that interval.
- Choosing a coarse resolution is a design decision, not a display setting: a 30-minute grid cannot express a 20-minute talk plus a 10-minute gap as two distinct things, so the buffer has to live inside the slot (the default buffer rung in SKILL.md).

Practical consequence: pick the resolution from the shortest thing you need to express. If you run 15-minute lightning talks, a 30-minute grid forces you to pair them.

## The four clash types

The tool flags four _distinct_ conflict types rather than one generic "conflict":

1. **Session outside its room's availability window** - the room is not yours at that hour.
2. **Session conflicting with a speaker's stated unavailability** - the speaker is not available at that hour.
3. **Two sessions overlapping in the same room** - two things, one space.
4. **A speaker double-booked across two simultaneous sessions** - one person, two rooms.

Why the distinction matters more than the count: types 3 and 4 are arithmetic over data already on the grid, while types 1 and 2 depend on data you must have collected beforehand. A team that "checked for clashes" almost always means types 3 and 4 only. Types 1 and 2 are the ones that fail silently, because nothing on the grid looks wrong while the room is locked or the speaker is in the air.

Visual indicators surface both on the grid itself and inside the individual session editor, which is worth reproducing in any manual process. A conflict visible only in a summary report is a conflict nobody sees while they are moving the session that caused it.

## Availability: rooms versus speakers

Both rooms and speakers carry their own configurable availability windows, and they are genuinely separate constraints:

- A **room** window is contractual and usually blunt - the hours the venue lets you have that space, catering setups, a room you only hold for the morning.
- A **speaker** window is personal - travel, a return flight, a day job, a second commitment in the same city.

Speaker availability is collected **upfront during proposal submission**, through a calendar widget, rather than discovered during scheduling. This is the single highest-leverage mechanic in the whole model: it turns availability from something you find out about into something you schedule against. If your submission form did not ask, the equivalent is a direct request to every accepted speaker before the grid is laid - not after.

## Multi-speaker intersection

For a session with more than one speaker, the valid scheduling window is the **intersection** of all speakers' availabilities. A session cannot be placed in a slot where even one co-speaker is unavailable.

This is where a manual process most often breaks. The natural human check is per-speaker and sequential - "is Ana free? yes; is Ben free? yes" - which is the correct check, but it is easy to run it against only the speaker whose name appears first on the proposal. Compute and record the intersection as its own value for each multi-speaker session, before slotting, so the check has something to compare against rather than being re-derived under time pressure.

## Breaks versus blockers

Two distinct kinds of non-session grid item:

- **Breaks** - publicly visible items that occupy grid space like a session but carry no speaker or content: lunch, coffee, an evening reception. Attendees see them, and in a multi-track day they are also the plenary re-sync points.
- **Blockers** - internal-only items, never shown publicly, that reserve grid space: an AV reset, a room hold pending a decision, a slot deliberately kept empty against overrun.

Keeping the distinction is what lets you reserve time without publishing it. Anything you need the grid to protect but the audience does not need to see is a blocker, and collapsing blockers into breaks either publishes your internal margin or loses it.

## Worked example: a slot that passes and a slot that does not

A two-room morning, 15-minute grid resolution, 40-minute slots with a 5-minute published gap.

**Does not pass.** "Scaling Postgres at read-heavy loads", co-presented by Ana and Ben, placed 09:00-09:40 in Room B.

- Type 3: clear - nothing else is in Room B at 09:00.
- Type 4: clear - neither Ana nor Ben appears in another 09:00 session.
- Type 1: Room B is contracted from 09:30 (the venue uses it for breakfast service until then). **Fails.**
- Type 2: Ana is available from 08:00. Ben's window opens at 10:00 - he lands that morning. **Fails**, and the per-speaker check passed on Ana alone.

Both failures are invisible on the grid. Neither is caught by the check most teams actually run.

**Passes.** The same session placed 10:15-10:55 in Room B.

- Room B is available from 09:30 onward: clear.
- The Ana-Ben intersection is 10:00 onward: clear, and recorded as such against the session.
- Room B holds nothing else in that span; neither speaker is in another session then.
- The preceding Room B session ends at 10:10, leaving the published 5-minute gap intact.

The thing that changed was not diligence, it was order: the intersection was computed before slotting rather than checked after.

## What the model does not cover

The four types are the whole of what a tool can automate, and they say nothing about:

- **Audience overlap** - two sessions a shared audience would both want, running head to head. No availability data expresses this; it needs someone who knows the community reading the grid.
- **Room capacity** - nothing in the clash model compares expected audience size against seats. A grid can be entirely clash-free and still send an overflow crowd to the smallest room.
- **Pacing** - the model has no opinion about what the day feels like in sequence.

Treat a clean clash report as the floor, not the finish.
