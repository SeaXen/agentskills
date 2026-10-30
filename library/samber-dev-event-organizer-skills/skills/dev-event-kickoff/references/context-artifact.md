# Context artifact

`event-context.md` lives at the project root and is committed with the project when the project lives in git. One file, versioned, readable by every co-organizer. It is what makes the next session a warm start.

## Template

```markdown
# Event context

_Last updated: YYYY-MM-DD_

## Identity

- Event: name, and what someone attends it for.
- Edition: which one, and the date of the previous one if there was one.
- Funding model: volunteer community / company-owned / foundation / mixed.
- Positioning: what it stands for, against which alternative - from
  `samber/dev-event-organizer-skills@event-positioning` if it has run.

## Format (the gate source)

- Shape: meetup / hackathon / unconference / single-day / multi-day conference.
- Track count, and the session-format mix.
- Delivery mode: in-person / virtual / hybrid.
- Workshop hours: yes or no.
- Properties this team runs, if more than one.

## Dates

- Doors open, and whether it is announced.
- CFP open and close. On-sale date. Sponsor budget windows that close.
- The venue's cancellation-fee rungs and the go/no-go date before each.

## Money

- Budget status, break-even figure and where it is recorded.
- Ticket ladder status. Sponsor rate card status. Sponsors signed.

## Programme

- Call status, submissions in, accepted, grid published or not.

## State

- In flight: work started and not finished.
- Decided: settled calls, not to be re-litigated.
- Open: live questions.
- Constraints: the landing date, one-off versus standing, the effort ceiling.
  These three re-rank the short-list and the routines without re-asking Q6 and Q7.

## Team

- Name or role - decision rights on what.

## Session log

- YYYY-MM-DD - session goal → skill routed to → what changed here.
```

## Worked example (excerpt)

Both examples below are illustrative constructions showing the field shapes, not records of a real event.

```markdown
## Format (the gate source)

- Shape: single-day, single-track. No workshop hours.
- Delivery mode: in-person. Talks recorded and posted afterwards, no live stream.
- Properties: one. No second format under consideration.

## State

- In flight: call open, eleven submissions, no reviewers recruited yet.
- Decided: free entry, single track, no recording consent by default.
- Open: whether to accept a second sponsor.
- Constraints: doors 2026-11-07; standing, a few hours a week; four volunteers, no budget.

## Session log

- 2026-08-31 - "how do we pick talks" → `samber/dev-event-organizer-skills@event-talk-selection`
  → recorded the submission count and the missing reviewers as in-flight.
```

## Negative example - what not to write

```markdown
## Format (the gate source)

- Shape: TBD, probably a conference eventually.
- Delivery mode: we'd like it to be hybrid if we can.

## State

- Decided: nothing yet really.
- Constraints: we should be careful with budget.
```

Four failures:

- A `TBD` shape means the next session re-asks question 2 and every gate stays suspended - write "not fixed" and route to the format skill instead of recording an aspiration.
- "Probably a conference eventually" and "hybrid if we can" are wishes recorded in the field a gate is read from, which is how a router unlocks the wrong rows.
- "Nothing yet really" in a decided field is unfalsifiable, so nothing can be protected from re-litigation.
- "Careful with budget" gives the money model no number to work against; write the figure, or write that there is none.

## Archiving between editions

Before starting edition N, move the previous artifact aside rather than overwriting it - `event-context-2026.md` beside the live one is enough. `event-debrief` and `event-continuous-improvement` both read what the last edition actually decided, and an overwritten artifact leaves them reconstructing it from memory.
