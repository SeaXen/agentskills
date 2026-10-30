# Floor plan and booth specs

Contents: what is published about floor placement; the tier-to-spec catalog and its rows; a worked catalog with a negative counterpart; power and WiFi distribution; the two review categories the floor plan triggers.

## What is published about placement

Only one placement rule is published, and it is a good one. Paraphrased, not quoted, from the DevOpsDays organizing guide, "Selecting a venue":

> Put sponsor tables near food or the hangout space so foot traffic naturally passes them, not off to the side.

The same guide names hallway-track space as a first-class use of the venue rather than spillover, and states that Gold-tier sponsors at minimum get a table. `samber/dev-event-organizer-skills@event-venue-sourcing` already carries this into its site-visit checklist: check sponsor-table placement against the food and hangout circulation path, and check where power and network reach those tables.

Published floor-layout guidance stops there. Racetrack loops, tier zoning and hub-and-spoke geometry come from exhibition-industry practice, and the ranking between them is self-set.

**No developer-conference-specific traffic-flow research exists, and no booth-position-to-lead-volume figures exist at usable quality.** What circulates instead is vendor-marketing-grade: a booth-display company's own case study, published to sell booth displays, rarely independently verified and never from a developer-conference context.

Do not quote a dwell-time or lead-lift number to a sponsor. When a sponsor asks what a corner position is worth, the honest answer is that nobody has measured it at an event like this one.

## The tier-to-spec catalog

The catalog is this skill's central artifact: it turns the abstract thing the ladder sold into something a sponsor can build against and a venue can be asked for. `samber/dev-event-organizer-skills@event-sponsor-pricing` gates its ladder on floor presence as one of four physical axes but never says what floor presence physically is. This catalog is that missing half.

One row per tier. Each row carries:

1. **Footprint** - the plot or table the sponsor gets, in the venue's own units. State it as a dimension, not as an adjective; "a large table" is not a spec a sponsor can plan a banner against.
2. **Furniture** - what is provided versus what the sponsor brings.
3. **Position class** - which zone of the floor this tier draws from (not the specific spot, which is assigned later).
4. **Power** - whether a drop is provided, and who supplies and pays for it.
5. **Network** - what connectivity is included and whether wired is available at all.
6. **Vertical limit** - the maximum height of anything the sponsor erects, and whether anything may be suspended or attached to the building.
7. **Signage rule** - what may be displayed, and what must stay inside the plot rather than overhanging the aisle.
8. **Staffing** - minimum and maximum people at the booth, and the credentials they need.

The last three are the rows organizers most often leave blank and most often regret. A tier with no vertical limit is how a sponsor arrives with a structure that blocks the booth behind it; a tier with no signage rule is how a banner ends up in the fire lane.

### Worked catalog (positive)

Built around the one real published spec. The full-table dimension is published; every other cell is illustrative, showing the shape rather than a recommended value.

|                | Top tier                                                 | Middle tier                          | Floor tier                   |
| -------------- | -------------------------------------------------------- | ------------------------------------ | ---------------------------- |
| Footprint      | Full 96"x30" table, premium-located                      | Full 96"x30" table                   | Half of a shared table       |
| Furniture      | Table, cloth, two chairs                                 | Table, cloth, two chairs             | Shared table, one chair      |
| Position class | Premium zone                                             | General floor                        | General floor                |
| Power          | One drop, venue-supplied - request by the stated date    | One drop, request by the stated date | None; bring a charged device |
| Network        | Event WiFi, no extra cost                                | Event WiFi, no extra cost            | Event WiFi, no extra cost    |
| Vertical limit | Free-standing banner behind the table; nothing suspended | Same                                 | Nothing free-standing        |
| Signage        | Inside the plot; nothing overhanging the aisle           | Same                                 | Table-top only               |
| Staffing       | Two on the floor whenever it is open                     | Two                                  | One                          |

The tier gating here mirrors what eight DevOpsDays city ladders actually gate on - shared table versus full table versus none - rather than inventing a new differentiation axis.

### Negative counterpart

> **Sponsor benefits: Gold and above receive a booth space with power and internet. Table provided.**

Every line a sponsor needs is missing:

- _Booth space_ - no dimension, so the sponsor sizes a banner wall for a plot that will not hold it.
- _Power_ - no amperage, no supplier, no request deadline, so the sponsor discovers on the morning that the venue charges for drops and needed notice it never got.
- _Internet_ - does not say wired or wireless.
- _Table provided_ - does not say how big, so two sponsors arrive expecting different things.
- Height limit - absent entirely, and it is the line that decides whether the booth behind this one can be seen at all.

The failure is not vagueness for its own sake. It is that whoever is standing there at 08:00 fills each blank later, under time pressure, in the sponsor's favour or the organizer's, inconsistently.

## Power and WiFi distribution

`samber/dev-event-organizer-skills@event-venue-sourcing` negotiates the room's aggregate capacity - per-attendee device and outlet ratios, whether capacity can be raised. It hands over a room. Distributing that room across individual booths is this skill's job.

**No formula converts an aggregate venue ratio into a per-booth allocation.** Venue ratios are attendee-density rules of thumb for a room full of laptops, not an exhibitor-load model, and the two units do not bridge. Anyone presenting a conversion formula is inventing one.

So set a process instead of a number:

1. **Ask the venue what a booth drop is, what it costs and by when it must be requested.** The published answer to a sponsor's electricity question routes back to the organizers, who set expectations with venue staff. That routing is the practice, not a fallback from it.
2. **Publish per tier what is included and what must be requested**, with the request deadline. An unstated deadline is the most common way a paid-for drop fails to exist.
3. **Count booths needing power, not booths.** Most do not. A table with a laptop and a banner needs a socket; a table with a screen and a demo rig needs a drop.
4. **Treat WiFi as a stated inclusion, not a guarantee of throughput.** Where event WiFi is included at no additional cost, that is a commercial statement about billing, not a capacity promise. Tell a sponsor running a live demo over it to bring a fallback.

## The two reviews the floor plan triggers

Both are real, both are jurisdiction- and venue-specific, and **neither has a universal number this skill will state.** Naming an aisle width, an egress distance or an amperage threshold here would be inventing a figure that is wrong in most of the places this skill is read.

- **Fire lane, egress and occupancy.** The floor plan usually needs sign-off from a fire marshal or the venue's own safety officer. What matters operationally is the reversibility: a plan signed off and printed is expensive to redraw, and fixing a lane found narrow on the morning means moving a sponsor who is already set up. Get the review before the plan is printed, not before the doors open, and route the actual dimensions to the venue's own stated requirements.
- **Rigging.** Anything suspended from the ceiling or attached to the building (hanging signage, a truss, an overhead banner) needs the venue's rigging approval and often its own contractor. This only arises on the custom and bespoke rungs of the booth-spec menu. A refusal the week of the event cannot be worked around; the structure simply does not go up, and a sponsor whose package promised it is owed a make-good.

Ask the venue both questions in writing during negotiation, while `samber/dev-event-organizer-skills@event-venue-sourcing` still has leverage, rather than after signature when the answer is whatever the venue says it is.
