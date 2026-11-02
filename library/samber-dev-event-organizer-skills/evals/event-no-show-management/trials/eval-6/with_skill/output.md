# Brightwater Tech Day: registration ceiling

**Set the ceiling at 416 registrations. Never go above 500, and never plan on the 40 standing places.** The room admits 250 people at once, and the door gets a hard stop at 250. 700 is not an option.

## The capacity number

- **Binding limit: 250.** That is the venue contract. The 268 on the fire certificate is the building's legal maximum. The contract is stricter, so the contract wins.
- **The 40 standing at the back do not count.** The room limit is a gate in this skill, not something to trade for a fuller room. Standing room needs written approval from whoever the venue names, obtained before registration opens and never at the door.
- **If the venue approves standing in writing,** the limit moves and I redo the arithmetic below. Until then it stays 250.

## Why not 700

- **Past double.** Free-event guidance (MLH, 323 events, about 50% show-up) says to aim for double and "do not go over double". For you that means 500 at most. 700 is 2.8x.
- **Expected attendance.** At the 50% show-up figure, 700 registrations put about 350 people in a 250 room. Using the check-in-verified sample (about 28% free-event no-shows), it is about 500.
- **Standing room doesn't fix it.** 250 plus 40 is 290, and 350 still overshoots.
- **It's the "no ceiling" posture.** The skill deletes "register everyone and squeeze people in". The people turned away at the door are people who registered, and that costs more trust than an empty chair.

## The arithmetic (free-registration event)

| Step | Value | Source |
|---|---|---|
| Hard capacity | 250 | Venue contract |
| Show-up rate, point estimate | ~50% | Sourced (MLH trendline, 323 events) |
| Show-up rate, free-event band | 40–60% | Sourced (Event Tech Live) |
| Sourced 2x ceiling | 250 ÷ 0.5 = **500** | Upper bound only |
| Ceiling safe across the whole band | 250 ÷ 0.6 = **416** | Self-set |
| Expected attendance at 416 | 208 at 50%, 250 at 60% | |

- **Why 416 and not 500.** At 500 registrations, a normal 60% show-up puts 300 people in the room. That is over the limit with no margin.
- **Why the 2x figure is a ceiling here.** It was measured on free hackathons, which have the loosest commitment to a seat. For a different format, treat it as an upper bound, not a target.
- **The check-in-verified sample is more optimistic.** It shows about 72% free-event show-up. At that rate 416 registrations give about 300 people. The door cap and the waitlist rule below cover this case.
- **The "about 240" is not a measurement.** Nobody counted, so it is not a registered-versus-attended ratio. I can't build your own multiplier from it, so I'm using the sourced figures.
- **This edition is your measurement.** Count registrations and door entries so next year's ceiling comes from your own data.

## Plan

1. **Close registration at 416.** Name one person who closes the form. Write the ceiling into the form configuration.
2. **Waitlist above 416.** Order it first-come, first-served (FIFO), and publish that rule when the list opens.
   - **Promotion.** Promote in one batch on a fixed date before the catering guarantee locks, and give promoted people a claim deadline.
   - **Batch size.** Size the batch from the confirmed count on that date.
   - **Hard cap.** Total accepted never exceeds 500, and expected attendance must stay under 250.
   - **Emails.** Pass the trigger, audience, deadline and ratio to `event-attendee-email-sequences`.
3. **Door counter at 250, with a count in the hall.** Last editions went uncounted. Someone with a clicker or the badge scanner stops admission at 250. Decide before the day where the 251st person waits and who tells them.
4. **Walk-in lane.** Open it only after pre-registered check-in closes, on a separate form. Everyone completes the full registration form, and admission stops at the door cap. Give `event-attendee-experience` the expected volume. I can't predict it without data, so treat it as unknown and count it.
5. **Catering.** Hand `event-budget` the expected show-up of about 210 (50% of 416), not 416. State the buffer of about 206 separately. Your past editions suggest 240, but that was not counted, so confirm against the guarantee date.
6. **Deposit.** I don't recommend one. The two data points are single events, and refunds, accounting and the barrier for people who need free seats all cost something. The established lever is a nominal fee, which belongs to `event-ticket-pricing`.
7. **Record these numbers for next edition:** capacity 250, show-up rate used (50%), ceiling 416 with the arithmetic, the waitlist rule, and the final registered, attended, walk-in and promoted-who-arrived counts.

## Questions for you

- Does the venue contact approve standing in writing, and for how many? That is the only thing that changes the 250.
- When does the catering guarantee lock? It sets the waitlist promotion date. If it locks next week, the waitlist stops moving the catering number.
- Is the event really free, or is a nominal fee possible? A fee takes the ceiling to about 250 and removes the overbooking.
- How many registrations exist today?

I haven't verified the 40-person rear-area claim or checked the contract text. I'm relying on the figures you gave.