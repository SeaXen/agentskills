## Verdict

❌ **Not enough.** The line is the skill's negative example almost word for word. Every blank gets filled by whoever is standing at the booth at 08:00, and they will fill it differently for each sponsor. Sponsors start asking next week, so fix it before you publish.

## What's missing

**In the line itself**

1. **Platinum and Gold read as identical.** Platinum costs $12k and Gold $7k, but the line gives them the same thing. Say what the extra $5k buys, or the ladder has no floor-presence gate. If the two tiers really are identical on the floor, say that deliberately. Pricing the ladder isn't my call, so route that part to `event-sponsor-pricing`.
2. **Silver gets nothing, and the line doesn't say so.** Silver sponsors will ask. State "Silver: no booth space" in the same block.
3. **"Booth space" has no dimension.** Sponsors will size a banner wall for a plot that may not hold it.
4. **"Table provided" has no size.** Two sponsors will arrive expecting different tables. Also state the furniture: cloth, chairs, and what the sponsor brings.
5. **"Power" has no supplier, cost or request deadline.** Venues often charge for a drop and need notice. The deadline must be a published row, not a sentence in an email.
6. **"Internet" doesn't say wired or wireless.** WiFi "included" is a billing statement, not a throughput promise. Tell sponsors running live demos to bring a fallback.
7. **Vertical limit is absent.** This decides whether the booth behind a sponsor can be seen. The line also doesn't say whether anything may hang from the ceiling or attach to the building.
8. **Signage rule is absent.** Without one, banners end up in the fire lane or over the aisle.
9. **Staffing is absent.** You need minimum and maximum people, coverage for the whole time the floor is open, and a badge that identifies booth staff.

**Not in the line, but sponsors will ask next week**

10. **Position class.** Say which zone each tier draws from. Don't promise a specific spot or quote a "corner is worth X" figure. No usable data exists.
11. **Setup and teardown.** You need move-in windows, a shipping window and address, a power and A/V request deadline, and a rule that teardown never starts before the last session ends. Write these as offsets from a fixed anchor (R = registration opens), not clock times.
12. **Who to send and the attire standard.** Say who to send: someone who can tell the story and take part in the community, not just qualify leads. Put the attire line before anyone books: booth staff, volunteers included, should not wear sexualized clothing, uniforms or costumes (from confcodeofconduct.com).
13. **One named organizer on duty and a contact for logistics.** Nearly every non-trivial answer routes to a person, so name that person.

## Proposed replacement

Only 96"x30" is a published spec, from the DevOpsDays full table. Every other value is **illustrative**. Replace the `[venue: ...]` slots with the venue's answers.

> **Booth space (Platinum and Gold only; Silver has no booth)**
>
> | | Platinum ($12k) | Gold ($7k) |
> |---|---|---|
> | Footprint | 96" x 30" table, premium zone | 96" x 30" table, general floor |
> | Furniture | Table, cloth, 2 chairs | Table, cloth, 2 chairs |
> | Power | One drop, venue-supplied, [venue: cost / who pays]. **Request by R − 2 weeks. Nothing accepted after.** | Same |
> | Network | Event WiFi, no extra cost. Not a throughput guarantee: bring a fallback for live demos. Wired: [venue: yes / no] | Same |
> | Height limit | One free-standing banner behind the table, max [height]. Nothing suspended or attached to the building. | Same |
> | Signage | Inside your plot only. Nothing overhanging the aisle. | Same |
> | Staffing | 1 to 2 people whenever the floor is open, with booth-staff badges | Same |
>
> **Schedule (R = registration opens, day one)**
> - R − 3 weeks: shipping opens, address and routing published
> - R − 2 weeks: power and A/V requests close
> - R − 1 hour: move-in, all sponsors
> - R − 15 min: organizer floor walk
> - Teardown opens after the last session ends, not before
>
> **Send someone who can tell your story and talk with the community.** Booth staff must not wear sexualized clothing, uniforms, or costumes. Questions: [name, contact]. Organizer on duty: [name].

If you do differentiate Platinum, make it something physical, for example position class, a second chair, or a dedicated earlier move-in. Don't invent a new axis. That is a decision for you and `event-sponsor-pricing`.

## Questions to answer before you publish

These are venue facts or your decisions. I won't invent them.

1. What is a power drop, what does it cost, and by when must it be requested?
2. Is wired network available?
3. Does the venue allow rigging, and what are its access hours and storage? Without secure overnight storage, no overnight build.
4. What are the venue's shipping dates and fees?
5. Does the venue impose labour rules for load-in?
6. When must the floor plan be printed and fire-reviewed? Get the review before the print run.
7. What is the floor, physically (hall, room, corridor), and how many Gold and Platinum booths fit? This decides layout and whether "premium zone" means anything.

## Cautions

- **Don't state aisle widths, amperage or egress figures.** They are jurisdiction- and venue-specific. Quote the venue's own requirements.
- **Don't publish the spec until the venue has answered questions 1 to 4.** Otherwise you redraw it afterward and sponsors have already planned against the first version.
- **Publish this as one generic floor brief, not per-sponsor.** Answering each sponsor's logistics question belongs to `event-sponsor-fulfillment`, which should work from your brief.
- **Self-set elements** here: the Platinum/Gold differentiation, the staffing counts, and the request deadline. Revisit them after the first edition using dead-booth counts and tables moved by hand on the day.