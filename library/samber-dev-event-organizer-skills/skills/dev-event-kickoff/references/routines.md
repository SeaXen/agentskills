# Routine mechanics

The ranked candidate set, its axes and its promotion conditions live in the skill body, at the point where the choice is made. This file covers only the mechanics: the dry-run format, the calendar anchors, and cleanup.

## Dry-run format

Show every proposed routine in this shape and get approval before creating anything. The values below are illustrative; substitute the project's own:

```
Routine: ticket-pace check
Trigger: the 1st of each month while registration is open
Runs: samber/dev-event-organizer-skills@event-market-fit
Output channel: a dated section appended to event-context.md, plus a message in the
                organizers' channel when the pace index falls below its checkpoint
Cost: one reading per firing; no work unless the number is off
First fire: 2026-09-01
Stops: on the doors-open date
```

Two fields are the ones routines usually lack:

- **Output channel** - without one, the routine fires into the void and gets silenced, which buries the routine that mattered; if you cannot name where the result lands, drop it.
- **Stop condition** - without one, it outlives the edition it was built for; an event has a finish line, so almost every routine here should retire itself on a date.

## Calendar anchors

Prefer a date the project already has over an arbitrary schedule:

- Doors open → the work-back checkpoints, and the retirement date for most routines.
- CFP open and close → reviewer recruitment before, selection after.
- On-sale date and each pricing-tier boundary → the ticket-pace check.
- Each rung of the venue's escalating cancellation-fee curve → a go/no-go review placed _ahead_ of the rung, never on it.
- Sponsor budget windows → the pipeline and renewal sweep, timed to the window rather than to a month.
- The debrief date → the post-edition trend read, which cannot fire before it.

Two lead times are systematically underestimated on events:

- Anything needing a signature from outside the organizing team.
- Anything a volunteer has to do around a day job.

Set both triggers earlier than feels necessary.

## Cleanup

Retire, explicitly and out loud, before installing anything new:

- Routines tied to a date that has passed.
- Routines pointing at a renamed or removed skill.
- Routines that have fired repeatedly without producing an action.
- Every routine carried from edition N-1 without being re-anchored to edition N's dates - the commonest form of noise here, because it looks correct and fires at nothing.
