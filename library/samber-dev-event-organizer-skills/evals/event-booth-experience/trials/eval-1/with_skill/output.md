# DevCascadia floor brief (draft for the printer deadline)

**Bottom line:** don't move the booths to a side room, and don't run first come first served. Keep the sponsors in the main hall on the path attendees already walk. Fix the lunch queue by controlling where it forms, not by hiding the booths. Assign every table before the plan is printed.

## Decisions on your two ideas

**1. Side room: ❌ rejected.**
- The only published placement rule is to put sponsor tables near food or the hangout space so foot traffic passes them, not off to the side. This comes from the DevOpsDays organizing guide.
- A side room makes every booth opt-in. Attendees only visit if they choose to leave the hall. The sponsors on your three tiers bought floor presence, and a side room cuts it.
- Nobody has measured booth-position lead data at developer conferences, so don't promise sponsors any figure either way. The honest framing is "on the main path" versus "off a spur".
- Your co-organizer's concern is real: a lunch queue that blocks a circulation route is a fire lane and egress problem. Address that directly instead (see the layout section).
- ⚠️ Fallback if the hall can't hold both: move the lounge, or a coffee bar, into or beside the side room, so there is a draw inside it. That is hub-and-spoke, and it costs more effort than the main-hall plan.

**2. First come first served: ❌ rejected.**
- It feels fair, but it rewards whoever arrives first, not whoever paid more.
- It also means a negotiation at 08:00 on setup day, and the last sponsor ends up in the dead corner with a legitimate complaint.
- Use a numbered, pre-assigned map instead (see "Making assignment fair" below).

## Layout: racetrack loop, buffet queue off the loop

The hall is a dedicated hall, so the default circulation-path siting is promoted to a racetrack perimeter loop. One circulating path means no booth sits on a spur, and position matters less, which makes it easy to defend to any sponsor.

- **Route:** entrance and lounge at one end, buffet at the far end. Booths line the path between them, so lunch traffic and the walk back from the lounge pass every booth.
- **Buffet queue:** give it a marked holding zone that does not sit on the loop. Ask the venue and the fire reviewer whether a double-sided buffet or two service lines shortens the queue. Keep booths out of the queue's footprint. This is the real fix for your co-organizer's concern.
- **Lounge by the entrance:** couches are a natural draw, so booths near them will see dwell traffic. Don't count that as a premium guarantee.
- **Tier zoning:**
  - Keep premium-zone positions only if your sponsor packages actually sold better position. Check with `event-sponsor-pricing`.
  - If the three tiers differ only in table size, drop zoning. One position class for all is simpler and fairer.
  - If they did sell position, draw the top tier from the entrance and lounge end and the buffet approach.
- **Power reach:** warehouse halls often have power only in a few places. Where power reaches may decide where the booths that need it can sit. Get this answered before the map is drawn.

## Making assignment fair (and print-safe)

1. The printed plan carries **numbered plots**, not names. Printing doesn't wait on who sits where.
2. Assign plots by tier zone first. Within a tier, either use signing date, or run a published draw that sponsors can watch.
3. Publish the assignment rule before sponsors choose. Collect preferences by a stated deadline.
4. Send the assignments to sponsors well before load-in so nobody argues on the day.

## Tier-to-spec catalog (all eight rows are mandatory)

All cells below are **self-set and illustrative** except the 96"x30" table, which is one published shape from one event. Replace them with your own values. Substitute your real tier names.

| | Top tier | Middle tier | Floor tier |
|---|---|---|---|
| Footprint | Full 96"x30" table plus plot | Full table | Half of a shared table |
| Furniture | Table, cloth, two chairs | Table, cloth, two chairs | Shared table, one chair |
| Position class | Premium zone, or general if you drop zoning | General floor | General floor |
| Power | One drop, request by the deadline | One drop, request by the deadline | None; bring a charged device |
| Network | Event WiFi, bring a fallback for live demos | Same | Same |
| Vertical limit | **Set by the venue and fire review**; nothing suspended | Same | Nothing free-standing |
| Signage | Inside the plot; nothing overhanging the aisle | Same | Table-top only |
| Staffing | Two on the floor whenever open | Two | One |

⚠️ The vertical limit and signage rows are the two that organizers skip and regret. I'm deliberately not stating a number, because the right height and aisle clearance depend on your venue and jurisdiction. Fill them from the venue and the fire reviewer, and don't print the plan with blanks.

**Power:** count the booths that need a drop, not the booths. Most need a socket at most. Ask the venue what a drop is, what it costs, and by when it must be requested. Publish that deadline as a row in the schedule.

## Master schedule (offsets from R, when registration opens on day one)

Illustrative, except where your venue answers differ. Settle the venue questions in the next section before you fix any of this.

```
R − 3 weeks    Shipping window opens (address and routing published)
R − 2 weeks    Power and A/V requests close; nothing accepted after
R − 1 hour     Move-in, one shared window for all 11 sponsors
R − 15 min     Floor walk: aisles clear, nothing overhanging, every booth staffed
R              Floor open
Last session   Teardown opens, never before
+ 90 min       Room clear; leftovers go to the named storage contact
```

- 11 booths on a single shared window is the default. Switch to staggered slots by zone if the warehouse has one dock door, or if the venue's access hours are short.
- Don't use an overnight build unless the venue grants out-of-hours access and secure storage for sponsors' equipment.

## Staffing and conduct provisioning

- Every booth is staffed for the whole time the floor is open, with a named person per shift. State a maximum as well as a minimum.
- Tell sponsors to send "somebody that can tell your story and participate with the community".
- Booth staff wear badges that identify them as booth staff.
- Include the attire standard from the code-of-conduct template as a provisioning line before sponsors book.
- Name one organizer on duty and tell every sponsor who it is. Any conduct matter leaves this brief and goes to your incident process.

## Traffic mechanic: passport card

- One card, one stamp per booth, a prize for a completed card.
- A stamp is given for arriving. Never require a conversation or a signature, or it becomes a forced pitch.
- If a booth would scan the attendee, that is lead capture, which `event-sponsor-fulfillment` owns, with consent attached.
- The passport matters most for your quieter booths. Measure whether completed cards came from attendees who were not already touring booths.

## Before the printer: three weeks

**Do this week:**
1. **Book the fire marshal or venue safety review now.** Get it before the print run, not before doors. A plan changed after printing means moving a sponsor who is already set up.
2. Ask the venue, in writing: where power and network reach; what a drop costs and its request deadline; access hours; shipping fees; secure storage; whether rigging is permitted.
3. Check your sponsor packages for what "floor presence" promised per tier (`event-sponsor-pricing`).
4. Check the buffet queue plan with the fire reviewer.

**Questions I still need from you.** Answer in order, as each decides a rung above:
1. Did the tiers sell position, or only table size?
2. Where do power and network already reach in the hall?
3. Is the hall's dock a single door?
4. Do you have a hard print date inside the three weeks?
5. Is this a one-off, or will next year reuse the plan?
6. How much effort can you spend: volunteer hours on the dock, and your willingness to tell a top-tier sponsor where they sit?

**Measure after the event:** dead-booth count (ask the sponsors), tables you had to move by hand on the day, and booths not ready at the floor walk. Record them and start next year's plan from them.

After the plan is approved, hand the brief to `event-sponsor-fulfillment` to run per sponsor.