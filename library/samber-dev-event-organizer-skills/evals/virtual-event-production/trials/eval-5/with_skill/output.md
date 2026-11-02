# Sanity check: Pinewood Data Conf virtual budget

**Verdict: don't take this to the board yet.** Neither number holds up as stated. I haven't seen your plan or the cost breakdown, so I can't check your arithmetic. This covers the two assumptions.

## 1. The 650 attendance figure (60% of 1,100)

The 60% is an assumption with no evidence behind it. The published evidence doesn't support "people show up less."

| Conference | In-person | Virtual | Change |
|---|---|---|---|
| PyCon US (2019 → 2021) | 3,393 checked in | about 2,650 | about 22% fewer |
| KubeCon+CloudNativeCon NA (2019 → 2020) | 11,891 registrations | 22,816+ registrations | nearly doubled |

- **The direction can go either way.** Removing travel cost and geography can grow the audience as easily as losing the room shrinks it.
- **Your 60% lies outside both published results.** PyCon retained about 78%, and KubeCon grew to about 190%.
- **Two cases are not a distribution.** They show the direction is open. They don't give you a rate to use instead.
- **The two figures aren't comparable.** PyCon's is check-ins and KubeCon's is registrations. I'd check which kind your 1,100 is before comparing anything.

**What to do before the board:**
1. **Plan a range, not a point.** Use a low, base and high case. Build the base case from this event's own signals: registration pace against last year, the mailing list, ticket price, and how far the audience reaches now that travel is gone.
2. **Check what 1,100 counts.** It might be registered, checked in, or paid. Compare it with the same kind of number this year.
3. **Size capacity to the high case.** A 650-person plan that actually draws 1,900 can hit the platform's concurrent-viewer ceiling. Ask the vendor in writing what happens at the ceiling: a queue, a refusal, or an upgrade invoice.
4. **Separate what scales with attendance from what doesn't.**
   - Moderation staffing scales with concurrent tracks, not headcount.
   - Bandwidth scales with rooms and viewers.
   - Revenue scales with paid tickets.
   - If your plan ties the first two to 650, rework them.

## 2. The hybrid cost baseline

Don't use it as the baseline. The published cost evidence prices the virtual layer of a hybrid run, not a standalone virtual event.

- **Capture was shared with the room.** In a hybrid, cameras, mixing and crew serve the room and the stream together, so the virtual layer only carries the increment. In your event the virtual production is the whole event. Those shared costs now sit entirely in your budget, and I can't tell from here by how much.
- **Some of your costs are ones the hybrid never had.** These include remote-speaker connectivity checks, local backup recordings, in-session moderation, failure drills and a rehearsal on the real platform.
- **The direction of the error is unknown.** It could be too low or too high. That is the problem, because a board can't rely on a number whose error has no known sign.

**Rebuild the budget bottom-up from decisions:**
1. **Interaction posture.** Is this a feed people watch, or an event people are inside? This reorders every line below.
2. **Platform posture and a real quote.** Get written answers to the vendor questions: concurrent ceiling, account requirement, captioning, recording ownership, data residency and retention.
3. **Moderation, by name per concurrent session.** Add a technical watcher where a session can't be re-run. Skip this line if there is no interaction surface.
4. **Speaker readiness.** Cost a written home-setup note as the baseline. Add individual tech checks and local backup recording for unrepeatable sessions, live demos and speakers with unknown connections.
5. **Failure drill.** Cost a published fallback line, plus a rehearsed handoff for the likeliest failure.
6. **Rehearsal on the real platform.** This is the line that gets cut first. A rehearsal on a different tool tests nothing.
7. **Captions.** The accessibility bar is set by your accessibility owner. The platform only delivers it.

**Tier split for the budget:** the feed survives every tier. A lean tier drops the interaction surface and its staffing first.

## 3. What I need from you to finish the plan

I'd ask these one at a time:
1. Is there an interaction surface (open chat or Q&A), or is it a feed people watch?
2. How many sessions run at once, and what is the shortest gap between them?
3. What did the format decision promise, and to whom: paid virtual tickets, a sponsor deliverable naming the stream, an access commitment?
4. Which sessions are unrepeatable, which carry live demos, and which speakers have an unknown connection?
5. What is the last date the platform choice can still be reversed?
6. Which source is the hybrid cost breakdown, and what did it cover?

## Provisional board framing

- Present attendance as a range with the assumptions stated.
- Present the cost as a bottom-up estimate with open vendor quotes.
- Flag the hybrid-layer figure as a reference point only.
- Mark any KPIs you add as self-set, not industry standards.