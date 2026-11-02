# Composta Summit kickoff: routing and answers to your three asks

I ran `dev-event-kickoff`. I couldn't save `event-context.md`: the write was blocked, and `example-repo` isn't your event repo anyway. The full file is at the end, so copy it to your event repo root. Memory is unwritten for the same reason. It gets derived from that file once you approve it.

**Do next:** answer the three open questions in the last section. Two minutes. They unlock the format-gated skills.

## State

Cold start: no `event-context.md` exists, and I did not read the git history because this repo isn't your event project. What I took from your message:

- **Edition:** first, nothing has run. You are also weighing a second property.
- **Date:** about May 2027. That's seven months from 2026-10-12, so the exact date is not set.
- **Intent:** annual.
- **Still unanswered:** format, who funds and organizes it, effort ceiling, and whether demand has been validated.

## Your three asks

### (a) Continuous improvement from day one: cannot be set up yet

- `event-continuous-improvement` is gated `recurring`. Per the gate reference, that gate is about having an edition to read, not about intent to repeat. You intend to recur, but there is nothing to compare yet.
- Two dated debrief logs are the minimum input. The earliest it can run is after your edition-2 debrief.
- **Rigor you can build now:**
  - Plan for the edition-1 `event-feedback` instrument and the `event-debrief` (blameless retro). Schedule both before doors open. Their output is the dated log the trend skill later reads.
  - Route to those two once the timeline exists (see "Not now").
  - Keep the previous edition's `event-context.md` archived, never overwritten.
- I deleted the post-edition trend-read routine rather than demoting it. It cannot fire in a first edition.

### (b) Cross-promotion swap: your assumption is wrong

- `cross-event-promotion` is deliberately **not** recurring-gated. The gate reference says gating it would delete "the one acquisition lever a first edition can reach without a track record."
- Its scope fits: independent events, different organizers, reciprocal visibility, no cash. Examples are calendar cross-listing, newsletter or social swaps, ticket-code swaps and speaker-pipeline sharing.
- It is not `event-media-partnerships`, because your friend runs an event, not a media outlet.
- The skill scores partner fit, so audience overlap between compost-tech and climate-tech gets judged there, not assumed.
- **No measured referral value for event swaps exists.** The skill says every target is self-set, so don't expect a benchmark.
- **My inference, not the skill's:** the swap works better once you have a date and a page to point at. Run it after `event-date-selection` and `event-landing-page`.

### (c) Monthly meetup series: `event-portfolio-strategy`

- The `properties` gate opens the day you start weighing a second property, whatever edition the flagship is on.
- It covers what each property is for, the funnel between them, and cadence collisions against one team. It also covers shared brand, list, team and sponsors, plus add/kill criteria written upfront.
- `event-community-building` stays closed (`recurring`). It's the nearest "audience between editions" skill, and it doesn't open before edition 2.
- If a company funds this as a DevRel line item rather than an event in its own right, I'd recommend `samber/developer-relations-skills` for the meetup. That's a recommendation, not a dependency.

## Route

Each ask gets its own route, as listed above. Run `event-first-edition` first. Its step 1 sends you to `event-market-fit` if demand isn't validated beyond stated interest.

## Short-list (value per unit of effort, highest first)

1. **`event-market-fit`**: attacks the biggest risk, a niche topic with no precedent, where "no" deletes everything below. Costs reading signals you already have; nothing booked or published. Skip it if you already have a waitlist or a community asking.
2. **`event-first-edition`**: attacks scope and the decision-to-doors timeline. Costs a session, plus a pre-mortem with written go/no-go dates. Promoted by "first edition" (Q3a).
3. **`event-portfolio-strategy`**: attacks ask (c) before it collides with the summit's plan for the same team. Costs one session; it moves up because you're weighing more than one property (Q3d).
4. **`event-format-selection`**: attacks the unfixed shape, track count and delivery mode, the gate source for most other rows. Costs one session. This is the question that suspends the format-gated rows.
5. **`event-date-selection`**: attacks the date every plan hangs off. Costs a calendar scan; once announced, a date is reversible only at a public cost.
6. **`event-planning-timeline`**: attacks the work-back plan from about May 2027, track by track. Costs a session after the date exists.
7. **`cross-event-promotion`**: attacks registrations through the free lever in (b). Costs an organizer-to-organizer ask and a lightweight swap agreement.
8. **`event-budget`**: gives you break-even as a number with a date. Costs a modelling session.

## Chain

Dependency order for standing up a new event: `event-market-fit` → `event-positioning` → `event-format-selection` → `event-date-selection` → `event-planning-timeline` → `event-budget` → `event-venue-sourcing`.

Each link hands the next its verdict, shape, date, plan and budget.

## Not now

- `event-feedback` and `event-debrief`: after `event-planning-timeline` fixes doors-open. Both get designed in edition 1.
- `event-continuous-improvement`: after two dated debrief logs exist (edition 2 debrief).
- `event-team-structure`, `event-community-building`, `event-growth-strategy`, `tech-podcast-youtube-channel`: after edition 1 finishes (`recurring` gate).
- Gated rows (`event-venue-sourcing`, `event-press-relations`, the hackathon lane and the rest): after `event-format-selection` returns.
- The six `event-sponsor-*` skills: after `event-budget` sets a target. They also need your funding answer and effort ceiling. Volunteer organizers would promote them (Q4a).
- `event-cfp-design`: after format and date are fixed.

## Gap

- None for these three asks. Ticketing platform operation is a collection gap if you need it later.

## Routines (dry-run only, nothing created, needs your approval)

Two proposed, not three:

- The ticket-pace check is deleted: no ticketing source detected.
- The go/no-go review waits for a signed venue and its cancellation rungs.
- The sponsor sweep waits for a known sponsor budget window.

```
Routine: kickoff re-invocation
Trigger: monthly, placeholder until a real date exists
Runs: samber/dev-event-organizer-skills@dev-event-kickoff
Output channel: dated line in event-context.md session log
Cost: near-zero per firing
First fire: 2026-11-12
Stops: on the doors-open date
```

```
Routine: work-back checkpoint
Trigger: each replanning checkpoint from event-planning-timeline
Runs: samber/dev-event-organizer-skills@event-planning-timeline
Output channel: dated section in event-context.md plus a message to the organizers' channel
Cost: one team reassembly per firing
First fire: not set until the timeline exists
Stops: on the doors-open date
```

Both triggers are placeholders. The kickoff cadence isn't anchored to an event date because none exists yet. Re-anchor both once `event-date-selection` returns. If your harness has no scheduled routines, use one calendar reminder: "Event check-in, re-run the event organizer kickoff."

## Three open questions

1. **Format:** (a) nothing fixed, (b) shape fixed and the rest open, or (c) fully fixed? If (c), give the shape, the track count and in-person, virtual or hybrid. "Developer conference" is the name, not the gate, so I did not infer a shape.
2. **Who funds and organizes it:** (a) volunteer community, (b) a company, (c) a foundation or non-profit, or (d) mixed?
3. **Effort ceiling:** (a) hours only, (b) a week of work is fine, (c) a few hours weekly, or (d) paid staff or a funded budget?

If format is (a) or (b), `event-format-selection` becomes the only route and the gated rows stay suspended. Those answers also settle the sponsor rungs, and the effort ceiling re-ranks everything above.

## `event-context.md` (copy to your event repo root)

```markdown
# Event context

_Last updated: 2026-10-12_

## Identity

- Event: Composta Summit - compost-tech developer conference (name from the organizer; shape not yet confirmed).
- Edition: 1. No previous edition. Intent: annual (stated, not a recurring-gate fact yet).
- Funding model: not answered.
- Positioning: not yet run through event-positioning.

## Format (the gate source)

- Shape: not fixed.
- Track count, session mix: not fixed.
- Delivery mode: not fixed.
- Workshop hours: not fixed.
- Properties this team runs: one planned (the summit). Monthly meetup series under consideration, undecided.
- Gates: format gates suspended until event-format-selection returns. Lifecycle: first open, properties open, recurring closed.

## Dates

- Doors open: about May 2027 (derived from "seven months" on 2026-10-12). Exact date not set, not announced.
- CFP, on-sale, sponsor windows, venue cancellation rungs: none recorded.

## Money

- No budget, ticket ladder, rate card or sponsors recorded.

## Programme

- Nothing started.

## State

- In flight: kickoff routing; three asks (continuous improvement, cross-promotion with a climate-tech meetup, monthly meetup series).
- Decided: run the summit every year. Cross-promotion with the friend's climate-tech meetup is reachable now.
- Open: demand validated beyond interest? Format. Funding and organizers. Effort ceiling. Add the meetup series?
- Constraints: landing date about May 2027; standing (annual); effort ceiling not answered.

## Team

- Not recorded.

## Session log

- 2026-10-12 - "continuous improvement / cross-promo swap / monthly meetup" -> first-edition, cross-event-promotion, portfolio-strategy routed per ask; continuous-improvement held (recurring gate closed) -> artifact drafted; format and funding left open.
```

Pass-bar check: scopes confirmed against each skill's description, and no route falls outside the § 3 tables. The artifact is drafted but not saved. One check is unmet: the interview ran 0 of 3 questions here, because there's no interactive question tool in this session, so I listed them as the open items above.