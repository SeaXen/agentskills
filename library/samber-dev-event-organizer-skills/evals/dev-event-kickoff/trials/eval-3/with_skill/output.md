**Do not design the stream, shortlist venues or pick prizes yet. Run `event-format-selection` first.**

You haven't fixed the shape (conference or hackathon), the track count or the delivery mode. The kickoff skill says to route to the format skill and stop in that case. The three things you asked for sit behind gates that stay shut until that decision exists:

- Hybrid streaming design (`hybrid-event-design`) opens only after the format decision returns "hybrid". Your co-organizer's preference is an input to that decision, not the decision.
- Venue shortlist for 400 (`event-venue-sourcing`) opens only once a physical room exists in the format. Venue needs change a lot between a two-day conference and a hackathon.
- Prizes (`hackathon-cash-prize`) open only if the format includes a hackathon.

## 1. Route

`samber/dev-event-organizer-skills@event-format-selection`

- It decides shape, track count, session mix and delivery mode.
- Bring these inputs. How many of the ~2,000 members would join remotely? Can you fund a stream crew? Do members want talks or building time?
- Estimated time: 60 to 90 minutes with both organizers in the room.

## 2. Short-list (runs alongside or right after the format session)

Ordered by value per unit of effort. Every entry is ungated.

1. `event-market-fit`
   - Attacks: you don't know what the 2,000 members want (talks, building or both).
   - Cost: one session reading signals you already have, like past meetup attendance and a member poll. It books and publishes nothing.
2. `event-positioning`
   - Attacks: "some kind of gathering" has no stated purpose or audience, which the format choice needs.
   - Cost: one session. Nothing is published.
3. `event-date-selection`
   - Attacks: "next fall" is too wide a window for any other plan to hang off.
   - Cost: a session plus a calendar scan. Announcing a date is hard to undo publicly, so don't announce yet.
4. `event-planning-timeline`
   - Attacks: no work-back plan from doors-open, so you can't tell which decisions are urgent.
   - Cost: one session once the date is chosen.
5. `event-budget`
   - Attacks: no break-even figure, so every later choice (stream crew, venue, prizes) is a guess.
   - Cost: one modelling session. Rough numbers are enough at this stage.

**Re-rank notes**
- Your unfixed format (Q2 = nothing fixed) collapsed the session to one route.
- It also removed the gated rows from the short-list.
- I did not promote `event-sponsor-*`, because Q4 (who funds you) is unanswered.

## 3. Chain

Dependency order, from the "standing up a new event" chain:

1. `event-market-fit` hands over a demand verdict.
2. `event-positioning` hands over what the event stands for.
3. `event-format-selection` hands over shape, tracks and delivery mode.
4. `event-date-selection` hands over the date.
5. `event-planning-timeline` hands over the work-back plan.
6. `event-budget` hands over a break-even figure.
7. `event-venue-sourcing` is reachable only after step 3 returns a physical room.

## 4. Not now

- **`hybrid-event-design`, plus `event-production` for the signal path**: after `event-format-selection` returns delivery mode = hybrid.
- **`event-venue-sourcing`**: after the format includes a room and `event-budget` gives a venue ceiling.
- **`hackathon-brief-design` → `hackathon-team-formation` → `hackathon-mentoring` → `hackathon-judging` → `hackathon-cash-prize`**: after the format returns a hackathon, or a conference with a hackathon track.
- **`event-cfp-design`**: after the format returns a talks track.
- **`event-first-edition`**: after you confirm this is edition one (Q3 below). If so it jumps to rung 1.
- **`event-sponsor-value-proposition` and the other sponsor skills**: after Q4 and `event-budget` give a revenue target.
- **`event-risk-management`**: after a venue contract exists, because it needs the cancellation-fee dates.
- **Conference-scale skills** (booths, B2B matchmaking, VIP, press): after the format passes the conference-scale test. The test is more than one track, an expo floor, or a named-guest and press surface.

## 5. Gap

- Registration and ticketing platform operation (checkout, refunds, tax) is not covered. `event-ticket-pricing` sets prices and the refund policy only.
- Remote attendees' travel and accommodation for the in-person part is not covered. `event-venue-sourcing` reads room-block terms inside a venue contract only.

## 6. Questions still open

I can't ask these interactively in this run, so tap an answer for each:

1. **Q3. Edition?**
   - (a) first edition
   - (b) one-off
   - (c) edition 2 or later
   - (d) more than one property
2. **Q4. Funding and organizers?**
   - (a) volunteer community
   - (b) company-owned
   - (c) foundation or non-profit
   - (d) mixed
3. **Q6. Deadline?**
   - (a) fixed doors date
   - (b) a CFP, on-sale or announcement deadline
   - (c) a sponsor budget window that closes
   - (d) no date
   - If a date exists, give it.
4. **Q7. Effort ceiling?**
   - (a) one-off, hours only
   - (b) one-off, a week of work is fine
   - (c) standing, a few hours weekly
   - (d) standing, with paid staff or a funded budget

Q7 (a) would cut the short-list to the first two entries.

## 7. Context artifact

I did not write `event-context.md`. This session runs inside the `example-repo` repo, not your event project. Save the draft below at the root of your event repo:

```markdown
# Event context

_Last updated: 2026-10-12_

## Identity
- Event: Nimbus Users Group annual gathering, name not set.
- Edition: not confirmed (Q3 open).
- Funding model: not confirmed (Q4 open).

## Format (the gate source)
- Shape: not fixed (conference vs hackathon undecided).
- Delivery mode: not fixed (hybrid requested by co-organizer, undecided).
- Capacity target: ~400 in person.

## Dates
- Doors open: fall 2027, not chosen, not announced.

## State
- In flight: nothing.
- Decided: run an annual gathering.
- Open: format, delivery mode, date, funding, effort ceiling.
- Constraints: landing date, one-off vs standing and effort ceiling not recorded yet.

## Session log
- 2026-10-12 - "design hybrid stream, shortlist venues, hackathon prizes" → `event-format-selection` → format gate unfixed, gated rows suspended.
```

## 8. Routine (dry-run, nothing scheduled)

- **Kickoff re-invocation.** It is the only routine installed, because the event doesn't exist yet in routing terms.
- **Trigger:** the day `event-format-selection` returns.
- **Action:** re-run this kickoff, patch the format fields, re-route.
- **Output channel:** a calendar invite to both organizers titled "Event check-in - re-run the event organizer kickoff".
- **Stop condition:** retire it once a date is fixed and the work-back checkpoints from `event-planning-timeline` replace it.
- Say yes and I'll schedule it.

**Next, under 2 minutes:** answer Q3, Q4, Q6 and Q7 above, then book the format session with your co-organizer.