# ForgeDay registration: access needs form

**Verdict: the goal is good, the design isn't.** Keep the capacity planning. Change how you collect the data. The current plan has four problems.

## What's wrong

1. **A required health question is a legal problem.** Health data is a special category under GDPR Art. 9. You'd need explicit, freely given consent. A mandatory field fails that test, because the attendee can't buy a ticket without answering (Art. 7(4)). Berlin is covered by GDPR and the BDSG.
2. **You don't need diagnoses.** Capacity planning needs to know what people need, not what condition they have. "Select any disabilities or medical conditions" collects the most sensitive data and gives you little you can act on.
3. **A single dropdown can't capture this.** People have several needs at once, and no list of conditions will be complete.
4. **Pre-booking all-gender restrooms outs people.** It forces attendees to disclose something about their identity just to use a toilet. Make these standard and signed for everyone. They need no booking.

## What to do instead

1. **Make the section optional.** Title it "Access and comfort", with a line saying skipping it never affects the ticket.
2. **Ask about needs, not conditions.** Use multi-select checkboxes:
   - Step-free access / wheelchair space
   - Reserved seating (near an exit, front row, or aisle)
   - Quiet room (I may use it)
   - Captions or a sign-language interpreter
   - Dietary or allergy needs
   - Other: "Contact me"
3. **Don't offer a free-text box for details.** It invites diagnoses. Use a "please contact me" tick box instead.
4. **Treat the quiet room as a planning signal, not a booking.**
   - The room is walk-in. Ask "I may use it" so you can size it.
   - Reserve a block of seating and release unclaimed seats on the day.
   - Check last year's numbers or similar events for a baseline, and add a buffer. I don't have a reliable benchmark for the share of attendees who'll use these.
5. **Make all-gender restrooms universal.** Sign them, and keep a few single-user ones if the venue allows. No question is needed.
6. **Use a separate follow-up address, not info@.**
   - Create `access@forgeday.dev`, owned by one or two named people.
   - A shared info@ spreads health details across everyone with access and sits in mail archives.
   - Handle details by phone or in a short call where possible.
7. **Keep the answers out of the main registration database.**
   - Store them in a separate, access-restricted table, or leave them on the platform.
   - Use aggregate counts for planning.
   - Keep names attached only for people who ticked "contact me".
   - Never put them on badges, attendee lists, or anything shared with sponsors.
8. **Set a retention limit.** Delete individual answers shortly after the event, for example 30 days. State the period in the notice.

## Checks on the platform

- Can it make custom questions optional, and can you export or delete answers?
- Do you have a data processing agreement (Art. 28) with it?
- Where does it host data, and does it pass answers to third parties?
- Does it show answers to sponsors, or put them in the attendee export by default?

## Consent text (draft)

> **Access and comfort (optional).** Tell us what would help you at ForgeDay. We use your answers only to plan the venue and to contact you if you ask. Only the access team sees them, and we delete them 30 days after the event. You can withdraw consent anytime at access@forgeday.dev. Skipping this never affects your ticket.

Put the consent on its own tick box, separate from the terms and conditions. Link it to your privacy notice.

## Still open

- **Do you need a DPIA or a DPO?** At 400 attendees you probably don't need a DPO under the BDSG thresholds. Have a privacy lawyer or the Berlin data protection authority's guidance confirm that, and confirm the consent wording. This is not legal advice.
- **Who owns the access@ mailbox?** Pick the named people before launch.

Want me to turn the checkbox list and consent text into a final form spec for the platform?