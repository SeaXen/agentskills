Neither of your two ideas works for this channel, so I didn't apply them. The skill rules them out directly, and the drafts below follow the skill instead. I've marked every on-site fact I don't have as a placeholder.

## Why I didn't apply either idea

**1. Lowercase, name-free, colleague-style subjects.** Cold-email subjects work by disguising the sender, so a message from a stranger gets past a spam filter and gets opened. Your attendees registered, and they'll search their inbox for "TelaForge" to find the check-in details. A subject like "quick update" or "tomorrow" can't be found that way. Naming the event and the date plainly is the rule here. A first name in the subject is fine in this channel, but I left it out because you didn't want it.

**2. A workshop promo in the ticket confirmation.**
- The confirmation is a transactional email. It goes out under the purchase itself, not under marketing consent.
- A promo block can cost the email that status. A ticket purchase isn't consent to be marketed to.
- The high open rate is the reason to keep it clean. People open it because it proves their registration worked. The promo would use that trust and put the email's compliance status at risk.
- Open rates for confirmations aren't comparable to promotional sends either, so don't plan around that number.

**Where the workshop pitch can go instead:**
- **Announcement or agenda-release email.** The agenda release is built to give the undecided a concrete reason, which suits a workshop.
- **A factual line in the confirmation, only for people who already bought the add-on.** It would be part of their order summary, like "Workshop add-on: included".
- **A separate promo send** to addresses that ticked a recorded marketing opt-in at collection. Tell me where your list came from and I'll check it.

## Inputs I'm treating as given

- **Event:** TelaForge Assemble, user conference, Austin, September 14-15.
- **Year:** Not stated. Today is 2026-10-12, so this is presumably 2027.
- **Not given:** the venue, check-in hours, badge policy, accessibility provisions and workshop details. These come from `event-attendee-experience` and I haven't invented any. Items in `[brackets]` are placeholders.

## Deliverable 1: registration confirmation

**Subject:** TelaForge Assemble: you're registered for Sept 14-15, Austin
**Preview:** Your ticket details are below. Practical info arrives about a week before.

> You're registered for TelaForge Assemble, September 14-15 in Austin.
>
> **Your registration**
> - Ticket: [ticket type]
> - Attendee: [name]
> - Order reference: [order #]
> - Dates: Monday-Tuesday, September 14-15, [year]
>
> About a week before the event, we'll send one more email with the practical details: venue address, check-in hours, getting there, food, accessibility and the code of conduct. It's a logistics email, not a marketing one, so keep an eye out for it.
>
> If your name or ticket details are wrong, reply to this email and we'll fix them.
>
> [View your order]
>
> Looking forward to seeing you in Austin,
> [Organizer first name], TelaForge Assemble
> Questions? Reply here or write to [reply address].

The weekday labels assume 2027, when September 14 is a Tuesday, so check them against the real year. I'd drop them if you're unsure.

If someone bought the workshop add-on, add one line to their order summary: `Workshop add-on: [workshop name], included`. Nothing else is added.

## Deliverable 2: subject lines for the reminders

The skill's default is two reminders. A one-week-before email carries the full practical information, and an evening-before nudge carries one fact. It caps reminders at roughly 2 to 4 sends in total. Don't add a countdown chain of 7, 3, 2 and 1 days.

| Send | Fires | Subject | Preview |
|---|---|---|---|
| Know-before-you-go | About 1 week before doors (around Sept 7) | **TelaForge Assemble: what to know before Sept 14** | Doors [time], check-in at [location], full details inside |
| Day-before nudge | Evening of Sept 13 | **TelaForge Assemble tomorrow: doors at [time]** | Check-in is at [location], [address]. See you there. |

**Alternates**, each naming the event and a fact:
- **Know-before-you-go:** "TelaForge Assemble Austin: check-in, schedule, getting there"
- **Day-before nudge:** "TelaForge Assemble starts tomorrow in Austin"

**Why these shapes:**
- Each subject names the event, so it can be found by search.
- Each subject stays around 40-60 characters, so it isn't truncated on a phone.
- Each preview extends the subject with a usable fact instead of repeating it.
- The day-before email carries no new information. That's why it points back to the week-before email.

## Before anything sends

- **Humanizer pass.** I wrote the drafts to sound like a person, but run them through your humanizer skill and read them aloud once.
- **Confirm the year and weekdays** against the real calendar.
- **Fill the placeholders** from your on-site source of truth, not from memory.
- **Review the full send map** with someone else. A wrong date in a reminder sends people to the wrong day.

## Questions for you

1. Where did the list come from? Was it ticket purchases only, or a form with an explicit marketing opt-in box? That decides whether a separate workshop promo is allowed.
2. Is the workshop add-on part of the same order flow? If yes, I can write the order-summary line and a workshop-specific promo for the agenda-release email.
3. Do you want the full week-before email (all 14 sections) drafted next? I need the on-site facts to do it.