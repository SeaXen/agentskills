# Tracks and cross-track dependency gates

The track taxonomy and gate catalog behind the work-back plan. Milestone chains here are the general pattern - how long each chain runs is a format-driven question answered by `samber/dev-event-organizer-skills@event-first-edition`'s sourced runways, not by this file. Trim the taxonomy to the event: merge tracks a small event doesn't need rather than leaving empty ones on the plan.

## Per-track milestone chains

Each chain reads backward: the terminal milestone sits at or near doors-open, the head milestone is the track's first action. Write dates onto the chain only after the anchor date and the immovable external deadlines are fixed.

**Venue & logistics** - requirements sheet → search → shortlist and site visits → venue locked → contract signed → deposit paid (a latest-safe-date commitment, not an automatic next step) → build-up/tear-down plan → final logistics walkthrough.

**Program** - CFP designed → CFP opens → CFP closes → selection/voting → speakers confirmed → program announced. Selection needs real lead time before announcement: speakers need employer approval and travel arrangements, so the confirmation-to-announcement segment cannot be compressed to zero (a sequencing constraint stated in a major community-conference organizing guide). An invited-speaker program replaces the CFP segment of this chain - the trade-offs of that swap belong to `samber/dev-event-organizer-skills@event-first-edition`'s compression levers.

**Sponsors & partners** - budget-derived sponsorship target → tier design → prospectus assembled → outreach begins → agreements signed → invoicing → fulfillment obligations scheduled through the marketing and logistics tracks.

**Marketing & comms** - channel setup → announcement plan (each announcement is a dated milestone, not ambient activity) → sustained outreach → reminder sequence → final-two-weeks push.

**Ticketing & registration** - payment infrastructure live → pricing set → sales open → early-bird close → sales checkpoints → final headcount.

**Budget & finance** - draft budget → scope tiers costed (Good/Better/Best, if the ladder is in use) → revenue checkpoints → vendor payment deadlines → reconciliation.

**Team & volunteers** - track owners confirmed → delegation as workload grows → day-of volunteer recruitment → volunteer briefing.

## Cross-track gate catalog

A gate names two milestones in different tracks: the prerequisite and the milestone it blocks. Every gate on the plan must name both sides: "sponsors depend on budget" is a sentence, "prospectus assembled ⟸ draft budget approved" is a gate.

Sourced gates (from named organizing guides, generalized here to any edition):

- **Payment infrastructure live ⟸ blocks ⟹ date announced.** A major community-conference organizing guide states this as a hard rule - a date cannot be announced until the team can handle money - and reports rescheduled or cancelled events from skipping it. The general lesson: announcement is a gated milestone whose prerequisites span three tracks (venue, ticketing, comms).
- **Code of conduct published ⟸ first public listing.** Sourced sequencing from the same guide's ecosystem - the earliest hard administrative gate, ahead of venue and date. The CoC's content belongs to `samber/dev-event-organizer-skills@event-code-of-conduct`. First-edition specifics belong to `samber/dev-event-organizer-skills@event-first-edition`.
- **Sponsor prospectus timing ⟸ sponsors' fiscal-year budget cycles.** Larger sponsors commit budget a fiscal year ahead (same guide) - an _external_ deadline that pulls the whole sponsor track earlier than internal logic alone would place it. List external budget cycles among the immovable deadlines in interview Q3.
- **Venue locked ⟸ date announced publicly.** Date and venue are a joint negotiation, not a sequence - holding several candidate date windows open improves venue availability (a named practice in the same guide's date-selection advice - the decision itself belongs to `samber/dev-event-organizer-skills@event-date-selection`).

Derived gates (standard sequencing logic rather than published event-industry rules):

- **Draft budget approved ⟸ sponsor prospectus assembled** - tiers are priced off the budget gap, not invented.
- **Program announced ⟸ the program-driven sales push** - announcements are the moments sales spike, so marketing schedules its pushes onto program-track milestones (demand thresholds at those moments: `samber/dev-event-organizer-skills@event-market-fit`).
- **Speakers confirmed ⟸ program announced** - never announce a program still being negotiated.
- **Final headcount ⟸ catering and swag orders** - the canonical delayed-commitment pair: the order's latest-safe date is set by the vendor's real lead time, and headcount must be frozen just before it.
- **Track owners confirmed ⟸ any track's first milestone** - an ownerless track has no one to notice its slip.

## Latest-safe dates on the gate view

For every gate whose downstream milestone is an irreversible commitment (deposit, catering order, print run, contractor booking), record two dates: the earliest the commitment _could_ be made and the latest it _safely_ can. Plan to the latest-safe date whenever the cost of committing early and being wrong exceeds the cost of committing late and scrambling - the asymmetry test from the buffer policy in SKILL.md. The earliest-possible date is not a target: it is how teams quietly spend their reversibility.
