**Next action:** answer the 3 questions at the bottom. Then run `event-format-selection` (about one sitting).

⚠️ **I am not giving you challenge themes, prizes or judging yet.** The kickoff skill suspends the hackathon lane until the format is fixed, and yours isn't. You said "maybe a hackathon", and track count and delivery mode are open. Guessing a shape would produce a plan for an event you might not run. Those parts are ready to run once the format is recorded.

## What I took from your message

I didn't ask any of these. Correct any that are wrong.

| # | Question | Answer I recorded |
|---|---|---|
| 1 | Which block is this session in? | (a) The event doesn't exist yet and you're deciding whether to run it. |
| 2 | Is the format fixed? | (a) Nothing is fixed. A hackathon is a candidate, not a decision. |
| 3 | One-off or edition N? | (b) A one-off, and also a first edition. One property. |
| 4 | Who funds and organizes it? | (b) Braukette funds and owns it. Three employees organize. |
| 5 | Today's goal vs the project's goal? | Today: a full plan. Project: decide whether to do it at all. |
| 6 | Is there a date? | (d) No date. The only anchor is "next spring", roughly March to May 2027. |
| 7 | One-off or standing, and effort ceiling? | (a) A one-off, hours only. |

## Route

**`samber/dev-event-organizer-skills@event-format-selection`**

- **Why this one:** answers 2(a) mean the format gate can't be applied. The skill's rule is to route to the format skill and stop.
- **What it returns:** shape, track count and delivery mode. You record the result, and the next session reads it instead of asking again.
- **Suspended until then:** `hackathon-brief-design` (themes), `hackathon-judging`, `hackathon-cash-prize`, `hackathon-team-formation` and `hackathon-mentoring`. Also `event-venue-sourcing`, `hybrid-event-design` and `virtual-event-production`. They are unreachable for now, not missing.

⚠️ **One tension to decide.** Your real blocker is "is this worth doing?". The "standing up a new event" chain puts `event-market-fit` ahead of `event-format-selection`. I followed the unfixed-format rule and routed to format selection. If you'd rather settle the go/no-go first, say so and I'll flip the order.

## Short-list

It collapses to the single route above, because the format rule overrides the ranking. Your answers also removed three kinds of work entirely:

- **Sponsorship sale:** removed because it is a one-off with hours only, and there is nothing to sponsor yet.
- **On-the-day operations:** removed because there is no day yet.
- **After and between editions:** removed because there is only one edition.

## Chain

Dependency order. Each skill hands its result to the next.

1. `event-market-fit` and `corporate-event-strategy`: hand over a go or no-go and what Braukette wants from this.
2. `event-first-edition`: hands over a scope for edition one.
3. `event-format-selection`: hands over the shape, track count and delivery mode.
4. `event-date-selection`: hands over a date, which every other plan hangs off.
5. `event-planning-timeline`: hands over the work-back plan.
6. `event-budget`: hands over a break-even figure against your approved budget.

## Not now

| Skill | Unblocks when |
|---|---|
| `hackathon-brief-design` (themes) | The format record says the shape is a hackathon. |
| `hackathon-judging` | The brief exists, because judging scores what the brief asks for. |
| `hackathon-cash-prize` | The judging is defined. It also covers who can lawfully receive a prize. |
| `hackathon-team-formation` and `hackathon-mentoring` | The brief exists and the delivery mode is known. |
| `event-venue-sourcing` | The delivery mode is in-person or hybrid. |

## Gap

None for this session. Later, if teams need Braukette's API or SDK to build against, `samber/developer-platform-skills` is worth installing. That would be a recommendation, not a dependency. A challenge built on your API is still `hackathon-brief-design`.

## Routine (dry run, nothing created)

You get one routine only, because the event doesn't exist yet.

```
Routine: kickoff re-invocation
Trigger: 2 weeks from the go/no-go answer (no event date exists yet to anchor it)
Runs: samber/dev-event-organizer-skills@dev-event-kickoff
Output channel: a dated line in event-context.md
Cost: near zero per firing
Stops: when doors-open is fixed, then swap in the work-back checkpoint
```

If you approve it, I'd need your calendar tool or a repo to attach it to.

## Draft `event-context.md`

⚠️ **I did not write this file.** It belongs at the root of the Braukette project, and this working directory is a different repo. Tell me the path and I'll create it.

```markdown
# Event context
_Last updated: 2026-10-12_
## Identity
- Event: Braukette user-community event. Name not chosen.
- Edition: first, one-off.
- Funding model: company-owned. Three engineers organize.
## Format
- Shape: not fixed (hackathon is a candidate). Track count: not fixed. Delivery mode: not fixed.
- Properties: one.
## Dates
- Doors open: none. Window: spring 2027. Nothing announced.
## Money
- Budget: approved, amount unrecorded.
## State
- In flight: nothing.
- Decided: nothing.
- Open: whether to run it at all; the shape.
- Constraints: one-off; hours only; window spring 2027.
## Session log
- 2026-10-12 - "full hackathon plan" → event-format-selection → recorded answers 1-7.
```

## Questions for you

1. **Format:** is a hackathon the only shape you want considered, or are you open to alternatives such as a meetup or workshop day? If it's only a hackathon, `event-format-selection` still fixes track count and delivery mode.
2. **Budget:** what is the approved figure, even roughly?
3. **Purpose:** what should Braukette get out of this? Examples are product feedback, user retention, hiring or visibility. This decides the go/no-go.

Once you've answered, I'll record the answers and start `event-format-selection`.

**Pass bar:** the context file isn't written to disk (above), so that item is open. The other items pass.