# ByteHarbor Days: espresso cart and premium zone

## Verdict

- ✅ **Espresso cart: yes, as the food and hangout anchor.** Don't make it a hub with booths radiating from it.
- ❌ **Premium zone for the sponsors you like most: no.** All 8 sponsors paid the same $4k for the same benefits, so a premium zone gives some of them something others paid for and didn't get.

**Next action:** decide whether you can get the cart cheaply (see "Cost" below). Then put the 8 tables on the path attendees already walk to the coffee.

## Why the premium zone fails

- Zoning by tier only works when the ladder sold floor-position differences. Yours sold none.
- Every sponsor will read the zone as arbitrary, and the 4 sponsors outside it have a legitimate complaint.
- Favoritism is not a tier. It also costs political capital (my assumption: you'd be telling some sponsors they sit worse than others).
- If you want to reward sponsors, sell the difference next edition. For example, offer a premium position or cart naming as a paid upgrade. Price that with `event-sponsor-pricing`.
- Don't let sponsors pick their own spot on arrival either. That rewards whoever arrives earliest.

**Do this instead:** map the floor, then assign spots by a published method, such as a random draw announced to all 8. Everyone can see it's fair. If one corner is weak, rotate positions next edition.

## Why the cart should not be the hub

Radiating everything from a rented central draw is the highest-effort layout, and it ranks last on efficiency.

- The cart is programming you must schedule and staff.
- Booths at the spoke ends still starve.
- It is the layout most likely to need a fire-lane review, because a coffee queue forms in the aisles.
- The conference you saw looked good because the draw was central. That doesn't show the sponsors' booths got traffic, and nobody has published data on booth position against leads at developer events. Don't promise sponsors a number.

The cart does one thing well: it gives attendees a reason to walk the floor. The published placement rule (DevOpsDays organizing guide) is to put sponsor tables near food or the hangout space, so traffic passes them instead of sitting off to the side. That is what the cart is for.

**Layout:**

1. **Racetrack or ring.** Put the cart on a path of the room's loop or ring. Tables go along the same path, so no booth sits off a spur.
2. **Cart position.** With 8 booths, a central cart with tables ringing it works. Treat it as a ring around a draw, not spokes.
3. **Same table everywhere.** Use one spec for all 8.
4. **Queue space.** Leave the cart queue its own space so it never blocks a booth or an exit.

## Cost: what to check first

I can't price this. Get the cart quote, then check:

- **Venue:** Does it allow outside vendors, or does catering have exclusivity? Does it allow the water and power the cart needs? Ask in writing.
- **Sessions:** If talks run in the same "one big room," grinder and steam noise lands inside sessions. Set cart quiet hours, or move it out of earshot.
- **Fire lane and egress:** Get the review before the floor plan is printed, not before doors open. I won't state aisle widths. Use the venue's own requirements.
- **Alternative:** If the venue already has coffee service, site the tables on that path. You get the same effect for near-zero cost.

At 300 developers and 8 identical sponsors, circulation-path siting alone is a legitimate answer. The cart is a nice-to-have. If it eats budget you'd rather spend elsewhere, skip it.

## Floor brief

### Tier-to-spec catalog

All 8 sponsors bought the same package, so there is one row. Dimensions and limits below are illustrative. The 96"x30" table is the one published DevOpsDays Des Moines shape. Confirm each cell against the venue before publishing.

| Row | Spec (all 8 sponsors) |
|---|---|
| Footprint | Full 96"x30" table |
| Furniture | Table, cloth, two chairs |
| Position class | General floor, assigned by published draw |
| Power | One socket per booth, on request. Deadline R−2 weeks. Ask the venue about cost and who pays |
| Network | Event WiFi, no extra cost. It is not a throughput guarantee: bring a fallback for live demos |
| Vertical limit | Free-standing banner behind the table, height set by the venue. Nothing suspended or attached to the building (no rigging review needed) |
| Signage rule | Inside the plot. Nothing overhanging the aisle or the cart queue |
| Staffing | 1 to 2 people whenever the floor is open |

Fill every cell. The vertical limit and signage rule are the two organizers skip and regret.

### Power and network

- Count the booths that need a drop. Most need only a socket.
- Publish the request deadline as a schedule row, not a sentence in an email.
- No formula converts the venue's attendee-density ratio into a per-booth load. Ask the venue what a booth drop is, what it costs, and by when it must be requested.

### Master schedule

This uses the single shared window. It is the default, and 8 booths fit through one door. Anchor R is registration opening on day one. The R−1h move-in is the published practice. Everything else is illustrative.

```
R − 3 weeks    Shipping window opens (venue address, routing published)
R − 2 weeks    Power, A/V and cart-adjacent requests close
R − 1 hour     Move-in opens, all 8 sponsors, one shared window
R − 15 min     Floor walk: aisles clear, cart queue space clear, nothing overhanging, every booth staffed
R              Floor open (cart opens)
Last session ends
               Teardown opens, not before
+ 90 min       Room clear
```

Switch to staggered slots only if the venue's access hours run short or the dock jams.

### Staffing and conduct provisioning

- **Who to send:** "somebody that can tell your story and participate with the community." This is the published wording.
- **Coverage:** Every booth staffed for the whole time the floor is open, with a named person per shift.
- **Credentials:** Badges that identify booth staff.
- **Attire:** No "sexualized clothing, uniforms, costumes, or environments" (`confcodeofconduct.com`). State it before sponsors book.
- **Escalation:** One named organizer on duty, whom every sponsor knows. A conduct matter leaves this brief and goes to the incident pipeline.

### Traffic mechanic

Use a passport or stamp card: one stamp per booth, plus a prize for a completed card.

- A stamp is given for arriving. Never require a signature or a conversation for it.
- The cart makes a natural redemption point, for example a free coffee for a completed card. That's your call on cost.
- The card's job is to route people to booths the layout can't reach. If each booth scans the attendee, you've built lead capture, which belongs to `event-sponsor-fulfillment` and needs a consent flow.

## What I assumed

I did not run the full interview. I filled these gaps with defaults:

- The room is one dedicated hall, and the cart doesn't compete with a session stage for sound.
- The venue allows an outside cart.
- You have no print deadline yet for the floor plan.
- No ceiling rigging is wanted.

Any "no" to the first two changes the layout. Please confirm or correct these four:

1. Is the expo in the same room as the talks, or separate?
2. Does the venue already provide coffee, and does it allow an outside cart?
3. What is the date the floor plan must be signed off and printed?
4. Is this a one-off, or does this year's plan become next year's starting point?

## Measure after the event

These measures are self-set:

- **Dead-booth count:** Ask sponsors which booths were walked past by almost nobody. Don't infer it. This is the number that says whether the layout was right.
- **Tables moved by hand on the day:** Count them.
- **Stamp-card completions from attendees not already touring booths:** This is the only thing the card exists to buy.
- **Cart:** Did queue spill block a booth or aisle? Record it for next year.

The cart is a lever for traffic, not proof that booths convert. Report the numbers honestly, even if booths fared no better than they would have without it.