# Decision menu rationale

Contents: why layout/setup and booth-spec/traffic-mechanic behave differently under an efficiency ranking; the full reasoning behind each menu's ties, promotions, and deleted options.

- [Why two of the four menus don't diverge](#why-two-of-the-four-menus-dont-diverge)
- [Layout and traffic pattern](#layout-and-traffic-pattern)
- [Booth tier physical-spec depth](#booth-tier-physical-spec-depth)
- [Setup and teardown window architecture](#setup-and-teardown-window-architecture)
- [Traffic-driving mechanic](#traffic-driving-mechanic)

## Why two of the four menus don't diverge

On the layout and setup menus, value and effort disagree: the ordinary case, where an efficiency ratio genuinely resolves the choice. On the booth-spec and traffic-mechanic menus, value and effort rise together across every rung instead, and that has a consequence worth stating rather than hiding.

When no option is ever better on value _and_ cheaper on effort, no ordering of that menu can violate strict dominance, so the dominance check cannot catch a mistake there. Those two orderings rest entirely on where the returns flatten, and no general rule fixes that point. Treat both as judgment calls, and re-rank them hard against Q7 and Q10.

## Layout and traffic pattern

The compliance `==` between the racetrack and the tier-zoned floor is argued, not a dodge: both fix aisle geometry inside a dedicated hall and both clear in one pass on one plan. The tier map that distinguishes them is invisible to a fire marshal, who reads aisles and exits, not who paid for which table.

Circulation-path siting ranks second on compliance despite being the cheapest rung, because it is the only one that puts tables into a corridor that is _already_ an egress route. The narrowing shows up only when the route fills: the least reversible failure here, since moving a table on the day means moving a sponsor already set up.

- **Circulation-path siting** - the only rung with published practice behind it: put sponsor tables near food or the hangout space so foot traffic naturally passes them, not off to the side (DevOpsDays organizing guide). Near-zero effort, one placement rule applied to a floor plan that already exists. It buys the same "everyone passes everything" property as the loop, which is why it wins efficiency outright.
- **Racetrack perimeter loop** - booths around a perimeter with one circulating path, so no booth sits off a spur. Tops value: it is the only rung where position barely matters, which is also what makes it the easiest to defend to a sponsor who paid for a good spot.
- **Grid rows** - parallel aisles in a hall. Cheap and legible, and the geometry a fire marshal already expects, so its sign-off is closer to a formality than a negotiation. Its cost is that aisle interiors starve while the ends do well.
- **Zoned by tier** - premium tiers drawn from a premium zone. It ranks below grid rows on efficiency because its extra effort goes into defending an allocation to sponsors rather than moving attendees. The value it adds accrues to the top tier only, while its coordination cost scales with sponsor count.
- **Hub-and-spoke around a central draw** - the starved option: booths radiating from a central attraction. Real value, top effort, so efficiency never picks it: the draw itself is programming that must be scheduled and staffed, and the spoke ends starve anyway.
- **Conditional delete: zoned by tier.** When the ladder sold no floor-presence differentiation - one table spec for everyone - delete it from this menu and from the axis lines. Zoning then encodes a distinction the packages never made, and every sponsor correctly reads it as arbitrary.
- **Deleted, not demoted: an unmapped floor where sponsors pick their own spot on arrival.** It reads as lean and fair. It produces a negotiation at 08:00, rewards whoever arrived earliest rather than whoever paid most, and leaves the last sponsor in the dead corner with a legitimate complaint. It is not a cheap version of a plan; it is the absence of one.

## Booth tier physical-spec depth

Value and effort rise together across every rung here. No option is better on value and cheaper on effort, so no dominance relation exists on this menu at all, and the ordering is clean by construction rather than by care.

That is never a pass: it means the check cannot catch an error here, and the efficiency line rests on a judgment about where differentiation stops paying.

The compliance `==` between the standard-spec and shared-table rungs is a genuine zero on both, not a tie dodge: neither suspends anything from the ceiling or attaches anything to the building, so neither triggers a rigging review at all. On the two rungs that do, the reversibility is the point - a rigging sign-off refused the week of the event cannot be worked around, the structure does not go up, and a sponsor whose package promised it is owed a make-good.

- **Standard table spec per tier** - the default: two or three written specs, each carrying footprint, furniture, position class, power, network, vertical limit, signage rule and staffing. It wins efficiency because the step up from a shared row is the largest single value increment on the menu for the smallest effort step: it creates the gating axis the ladder needs. Eight DevOpsDays city ladders gate on exactly this - shared table versus full table versus none. One city's standing page specifies a full 96"x30" table, premium-located for its top tier (DevOpsDays Des Moines): one city's spec, not a standard, so use it as the shape, not the number.
- **Shared table row** - a single shared surface for everyone. Its effort is near zero, but it cannot gate a ladder at all: it collapses the very axis the published ladders differentiate on, so its value sits below the threshold where the deliverable exists. Legitimate only where the ladder sold no floor differentiation either.
- **Custom structure for the top tier only** - a built stand for the top tier, tables below. Promote it when Q2 says the top tier's price carries a floor-presence promise a table cannot visibly deliver _and_ Q5 says the venue permits rigging. Both halves are required; the first without the second is a promise you cannot keep.
- **Fully bespoke per sponsor** - the starved option: every sponsor builds their own stand to a plot spec. It tops value and effort together, so efficiency never picks it. Promote it at a vendor- or foundation-run event where sponsors expect to build and your job narrows to publishing plot size, power, height and rigging rules.
- **Deleted, not demoted: "a table will be provided", with no dimension, no height limit and no signage rule.** It reads as flexibility. It is how a sponsor arrives with a banner wall sized for a plot that will not hold it, and how the booth behind it stops being visible. Whoever is standing there at 08:00 fills each blank later, inconsistently.

## Setup and teardown window architecture

Value and effort genuinely disagree here, and on one pair in particular: tiered windows dominate the overnight build outright, better value _and_ less effort, so any ordering putting overnight above tiered would be a violation. The efficiency line does not put it there, and the demotion still needs an argument: the overnight build buys the calmest possible setup and is the only rung that removes the dock peak entirely.

What demotes it is not availability: the conditional delete settles that, and settling it twice would double-count one venue fact. What demotes it is a distinction the venue's storage answer does not cover: secure overnight storage means crates in a locked room, while a pre-day build leaves assembled stands out on a floor nobody staffs. Tiered windows deliver the same spread with the equipment never leaving its owner's sight.

The compliance `==` between overnight and staggered is argued: both are multi-slot schedules assessed under one dock-and-labour agreement, and the slot count changes your coordination, not the venue's review.

- **Single shared window** - the default, and it is published practice: setup an hour before registration on the first day, for everyone (DevOpsDays Des Moines, standing across its 2019-2025 editions). That is one city's published window, not a cross-event standard, but it is real practice rather than a corner cut.
- **Staggered by zone** - move-in slots per aisle or zone, spreading arrivals across the same total window. Cheap: it is the shared window plus a list.
- **Tiered windows** - premium tiers get an earlier or dedicated slot. The starved option: it dominates the rung above it on both axes and still loses efficiency to two cheaper rungs, which is exactly the pattern an efficiency ranking under-serves.
- **Conditional delete: the overnight pre-day build.** When Q4 says the venue grants no out-of-hours access or no secure storage, delete it from this menu and from the axis lines. It is not a rung the organizer may choose against the venue's answer. Left at the bottom, it reappears as a promise to a large sponsor that cannot be kept.
- **Deleted, not demoted: teardown starting before the last session ends.** It reads as an efficiency and it converts the closing session into a soundtrack of packing tape. It also silently breaks the perk the sponsor bought: floor presence for the whole event, including the part where the sponsor who stayed is the only one left to talk to.

## Traffic-driving mechanic

The per-booth raffle, where an attendee volunteers contact details to one sponsor for a prize draw, is deliberately not a rung here. It is real and in published use, and `samber/dev-event-organizer-skills@event-sponsor-fulfillment` already ranks it as a lead-capture posture, with the compliance axis it needs. On this menu's own question it would fail anyway: a raffle's pull stays confined to the booth already running it and moves nobody toward the booths that are not.

Value and effort rise together across all three remaining rungs, so - as on the booth-spec menu - no dominance relation exists and the ordering is clean by construction, not by care. The check cannot catch an error here, and the ranking rests on where returns flatten, which no general rule establishes.

No compliance-cost axis, and the absence is stated rather than left blank: no rung here collects anything beyond one winner's contact detail at claim time. The moment a passport is redesigned so each booth _scans_ the attendee, it stops being this menu's rung and becomes the lead-capture question `samber/dev-event-organizer-skills@event-sponsor-fulfillment` owns, with a consent flow attached.

- **Passport or stamp card** - the default: one card, a stamp per booth, a prize for a completed card. It wins efficiency because it is the only rung that makes every booth a required stop, which is precisely the value organic traffic cannot buy at any price: siting sets organic exposure, and it stops there. Its cost is one print run and a prize.
- **Organic traffic only** - the layout does the work and nothing else runs. It ranks above the hunt because its near-zero effort beats a live-scoring overhead whose increment mostly rewards attendees who were already engaged. Honest at a small event on a single circulation path.
- **Scavenger hunt with a live leaderboard** - the starved option: tops value and effort together, so efficiency never picks it. Promote it when Q7 says a screen and someone to run it already exist, or when the floor is large enough that a card alone does not route people through it.
- **Deleted, not demoted: a passport that requires a sponsor's signature or a conversation before the stamp is given.** It converts a traffic mechanic into a forced pitch, which is exactly what the published staffing guidance argues against - send "somebody that can tell your story and participate with the community" (DevOpsDays Des Moines), not someone processing a queue. A stamp is given for arriving, not for listening.
