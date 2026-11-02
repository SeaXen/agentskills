**Verdict: do Plan A with one fix. Do a trimmed Plan B: add the first-timer/returning field, and keep dietary and accessibility data out of the newsletter tool.**

## Next action (5 min)
Add a `registered` field (yes/no) to your list. Every email depends on it.

## Plan A: non-opener resend
Keep it, with these rules:
1. **Exclude registrants first.** Resend only to people who are `registered = no` and didn't open. Without this, you pester people who already bought a ticket.
2. **Treat "non-opener" as noisy.** Apple Mail Privacy Protection marks many people as openers when they haven't read anything. Image blocking does the opposite. Expect some false positives and negatives.
3. **Resend once, at most.** Change the subject and the send time. Don't change the body much.
4. **Create urgency from real capacity.** Registration runs until you sell out, so there's no deadline. "Seats left" is your honest lever, but only quote a number you can verify.
5. **Measure by registrations, not opens.** Compare registrations in the 48 hours after the resend with a baseline. If the tool allows, split non-openers 50/50 between the old and new subject.

## Plan B: trimmed
Don't use dietary or accessibility data to segment every email. The reasons:
- **Legal.** Dietary needs can reveal religion or health, and accessibility needs reveal health. In Berlin that is special-category data under GDPR Art. 9, so you need explicit consent. A third-party newsletter tool then becomes a processor of that data.
- **No benefit.** Nothing in a promo email changes because someone is vegan. Only logistics change.

Do this instead:
1. **Dietary:** collect it in the registration form with a consent line. Export aggregate counts for the caterer. Don't sync it to the newsletter tool. Delete it after the event.
2. **Accessibility:** collect it as an optional free-text field, with the same consent line and the same exclusion from the newsletter tool. Email each flagged person individually, from the form export. Counts will be small, so a personal reply works better than a segment.
3. **First-timer vs returning:** sync this one to the newsletter tool. It is the only field that changes your content. It is not sensitive.

## Segments to build
You and one volunteer can maintain three fields and four filters:

| Field | Values |
|---|---|
| `registered` | yes / no |
| `attendee_type` | first-time / returning |
| `resend_done` | yes / no (stops double resends) |

| Segment | Filter | Content |
|---|---|---|
| Prospects | `registered = no` | Promo, seats left, resend to non-openers |
| First-timers | `registered = yes` and `attendee_type = first-time` | Orientation, how Berlin venue logistics work, a buddy offer |
| Returning | `registered = yes` and `attendee_type = returning` | What's new, bring-a-colleague perk |
| All registered | `registered = yes` | Logistics: schedule, venue, travel |

## Keep it maintainable
- Update `registered` weekly, or automatically if the form integrates with the tool. Before each promo send, check that the list is current.
- Add no more fields until one of these segments proves it moves registrations.
- Plan the sold-out switch now. Set `registered = waitlist` and move promo emails to a waitlist message.

**One question that changes the setup:** does your registration form push into the newsletter tool automatically, or do you import a CSV by hand? If it's manual, keep to one weekly sync and don't promise real-time segments.