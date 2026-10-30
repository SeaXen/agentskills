# Setup, teardown and booth staffing rules

Contents: the published sponsor answers; the venue questions that must be settled first; the master schedule and a worked example; staffing and conduct provisioning; what this skill hands to `samber/dev-event-organizer-skills@event-sponsor-fulfillment`.

## The published sponsor logistics FAQ

One real event publishes an answered sponsor logistics FAQ. From the DevOpsDays Des Moines sponsor page, a standing template across its 2019-2025 editions:

| Question                                      | The published answer                                                              |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| What dates/times can we set up and tear down? | An hour before registration on the first day of the event                         |
| How do we ship to the venue?                  | Contact the organizers directly - no self-service shipping instructions published |
| Whom should we send?                          | "Somebody that can tell your story and participate with the community"            |
| Electricity - how much, and are there fees?   | Contact organizers, who set expectations with venue staff                         |
| WiFi - how much, and are there fees?          | Included at the event, no additional cost                                         |
| Additional A/V equipment                      | Contact organizers                                                                |

Read two things out of that table rather than past it:

- **The setup window is genuinely that short.** One hour before registration, on the day, for everyone: a real published community-conference practice, not a corner cut. It is the published anchor for the single-shared-window rung, and it is one city's stated window, not a cross-event standard.
- **Every non-trivial answer routes to a human.** That is the pattern, not an omission: a small event's floor logistics genuinely depend on venue facts the organizer holds and the sponsor cannot look up. Design for that routing rather than trying to eliminate it: publish what is fixed, and name the person for everything else.

## The venue questions that come first

The schedule cannot be designed before these are answered. Put these questions to the venue directly:

- How soon can sponsors start shipping to the venue, to what address, and what fees apply to received shipments?
- What are the exact hours the organizing team has access to the space?
- Is there secure overnight storage - for the organizers' equipment _and_, explicitly, for sponsors'?

The DevOpsDays organizing guide also assigns one local organizer as the venue's primary operational contact, for chair layout, table arrangement and A/V. That is a named role, not a duty that falls to whoever signed the contract. Give the floor plan the same owner.

The third question is load-bearing for the setup menu: an overnight or pre-day build is not a rung the organizer may simply choose. If the venue does not grant out-of-hours access with secure storage, the rung does not exist. Remove it from the menu rather than leave it sitting at the bottom, where it reappears as a promise to a large sponsor.

Two further review categories are venue- and jurisdiction-specific, and **this skill states no universal threshold for either** because none exists:

- **Electrical safety sign-off** for temporary power distribution across the floor. Ask what supervision the venue requires and who is permitted to run a drop.
- **Venue-imposed labour rules** for load-in, rigging and dock work, which at larger commercial venues can require the venue's own or a union crew for work the organizers assumed they would do themselves. The operational point is reversibility: this cannot be renegotiated mid-setup. Ask in writing during negotiation.

## The master schedule

One schedule for the whole floor, not a schedule per sponsor. Per-sponsor communication of it belongs to `samber/dev-event-organizer-skills@event-sponsor-fulfillment`.

Write every row as an offset from a fixed anchor rather than as a clock time, so the schedule survives the doors moving:

1. **Shipping window opens** - the earliest date the venue accepts deliveries.
2. **Request deadlines** - power, extra A/V, anything the venue must be told about in advance. This is the row that most often does not exist, and the one whose absence surfaces on the morning.
3. **Move-in** - one or more windows, per the setup menu's chosen rung.
4. **Floor ready** - the moment before doors, when the organizer walks the floor.
5. **Floor open** - the hours booths must be staffed.
6. **Teardown starts** - never before the last session ends.
7. **Out and collected** - when the room must be clear, and what happens to anything left.

### Worked example (positive)

Anchored on R, the moment registration opens on day one. The R−1h move-in is the published anchor; everything else is illustrative, showing the shape.

```
R − 3 weeks    Shipping window opens (venue address + routing published)
R − 2 weeks    Power and A/V requests close  - nothing accepted after this
R − 1 hour     Move-in opens, all sponsors, one shared window   [published anchor]
R − 15 min     Floor walk: aisles clear, nothing overhanging, every booth staffed
R              Floor open
Last session ends
               Teardown opens  - not before
+ 90 min       Room clear; anything left goes to the named storage contact
```

### Negative counterpart

> **Sponsors: please arrive early on the day to set up. Teardown after the event.**

- _Early_ is not a time, so sponsors arrive across whatever spread their own guesses produce, and the ones who guessed latest are still unpacking when doors open.
- Nothing names a shipping window, so a crate arrives at a venue that will not accept it.
- No request deadline exists, so a power ask lands the morning of.
- Sponsors hear _after the event_ as _after the last talk I care about_, which is how teardown noise lands inside the closing session.

That last one also quietly breaks the perk the sponsor bought: floor presence for the whole event.

## Staffing and conduct provisioning

This skill sets what booth staff must do and wear **before the floor opens**. It never adjudicates a violation, never issues a sanction, and never touches the ejection mechanic - those are `samber/dev-event-organizer-skills@event-code-of-conduct`'s, and the contractual ejection right lives in `samber/dev-event-organizer-skills@event-sponsor-agreement`.

- **Who to send.** The published instruction is unusually direct: "Somebody that can tell your story and participate with the community." Publish it in the sponsor brief in those terms. At a developer event the person who can answer a technical question is worth more to the sponsor than the person trained to qualify one, and saying so up front is cheaper than managing the consequence.
- **Attire and conduct standard.** The clause most sponsor contracts now carry originates at `confcodeofconduct.com`, which states that booth staff - volunteers included - should not use "sexualized clothing, uniforms, costumes, or environments." `samber/dev-event-organizer-skills@event-code-of-conduct` carries it in its own policy reference. Put it in the booth brief as a **provisioning line**, stated before anyone books a stand rather than discovered at enforcement time. **No developer-conference-specific attire policy exists outside general code-of-conduct templates**, so pointing at the template that does exist fills that gap without writing a new rule.
- **Minimum staffing.** Require every booth staffed for the whole time the floor is open, with a named person per shift, and state the maximum too. An unstaffed booth in the middle of the floor is a dead spot the traffic pattern was designed around; an over-staffed one crowds the aisle it fronts. State the rule as a coverage obligation and let the sponsor size the rota.
- **Credentials.** Booth staff need badges that identify them as booth staff. This is what makes the conduct policy's scope clause operable on the floor - a policy that binds sponsor staff needs sponsor staff to be identifiable as such.
- **Escalation.** Give the floor one named organizer on duty and tell every sponsor who it is. Anything that becomes a conduct matter leaves this skill immediately and enters the incident pipeline.

## What this skill hands over

The output of this section is a **generic floor brief**: the schedule, the tier spec catalog, the staffing and conduct rules, and the named contact - written once per edition, for every sponsor.

`samber/dev-event-organizer-skills@event-sponsor-fulfillment` takes it from there, per signed sponsor: answering that sponsor's FAQ from this brief, staging their specific booth against their tier's spec, gating delivery on confirmed payment, and capturing evidence. Its own description already claims "the day-of sponsor experience (setup and teardown windows, shipping, booth staffing, power, WiFi, A/V)". The split: this skill designs those things once; that skill executes them per sponsor. Never write a per-sponsor tracking matrix here.
