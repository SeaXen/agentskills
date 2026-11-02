# Quarrydata Summit homepage: now until June 2

I read the `event-landing-page` skill and its references and applied them. I haven't seen your positioning sentence, your marketing calendar or the current page. Where the answer depends on those, I've said so.

## Verdict on the three ideas

| Idea | Verdict | Why |
|---|---|---|
| Replace Submit a Talk with a "CFP closed, registration opens soon" banner | ⚠️ Remove the button now, but drop the banner | A "submissions are closed" notice is a placeholder in different words. "Soon" is dateless. State the fixed fact instead: "Tickets on sale June 2." |
| Register button now, pointing at a holding page | ❌ Don't | A button that opens "registration opens June 2" costs more trust than empty space. The skill names this failure: a Register button with nothing behind it. |
| Countdown timer with "$249 from June 2" | ❌ Don't | The price isn't confirmed, and the skill forbids inventing a rung or early-bird figure. Screenshots outlive corrections. The timer also adds nothing a dated line doesn't, and it can't swap the button when it hits zero. |

## What the homepage shows until June 2

Nothing is open for sale and nothing is open for submission. The primary slot is therefore one of two things:

- **Notify-me email capture (recommended).** It gives the June 2 announcement somewhere to land. Your marketing plan should rank the owned mailing list first among channels.
  - It needs three things before it ships: a consent basis, a short privacy line, and a way to delete a subscriber.
  - It also needs someone assigned to send the on-sale email on June 2.
- **Contact link only (fallback).** Use this if nobody can own those three items. It is honest, but it captures no demand.

The page shows:

- Hero with the event name, **September 9-10, Austin**, venue if known, and a one-line description.
- Your positioning statement and its contrast sentence ("There are many [archetype] events. This is not one of them."), word for word. I don't have them, so paste them in.
- One status line: **"Tickets on sale June 2."** Add the time and time zone if the on-sale is at a set hour.
- The notify-me box (or the contact link), a code of conduct, an accessibility page and a contact address.
- Optionally, a short "why attend / forward to your manager" block, written from the positioning statement. It makes sense for a ticketed event.
- Structured data (schema.org event JSON-LD) with the real name, dates, URL, image and location. **Leave out price and offers** until the pricing group confirms them.

The page omits:

- The Submit a Talk button and any CFP section. Also remove it from the nav, footer and any other page that links to it.
- Speakers, program and sponsor sections. Don't publish "coming soon" placeholders.
- The early-bird price and the countdown.

A section may carry a date instead, such as "Speakers announced [date]". Use one only if the date comes from your talk-selection schedule and you'll hit it.

## How to make it happen

Your site can't change on a date. The skill treats the manual path as the correct mechanism for this case. Only the enforcement moves from the renderer to a person with a calendar.

1. Copy each row below into the campaign calendar as a dated task, not a note.
2. Name one owner per row, plus a backup who also has edit access. The volunteer is a single point of failure.
3. Put the checklist text in the task so nobody has to re-derive the intent.
4. Set the reminder for the day before.

| When | State after | Owner | Checklist |
|---|---|---|---|
| **Today (already overdue, the CFP closed last Friday)** | CFP closed, tickets on sale June 2 | Volunteer | Remove the Propose button and CFP section. Remove CFP links from nav, footer and social bios. Add the "Tickets on sale June 2" line and the notify-me box. Update the structured data. Ask the CFP owner to put a closed message on the form itself. |
| **June 1** (reminder, day before) | Staged change ready | Volunteer + organizer | Pricing group has signed off the ladder. Ticketing is live and tested end to end, **keyboard-only**. The June 2 edit is prepared and reviewed. |
| **June 2, at the on-sale time** | On sale | Volunteer | Swap the notify-me box for a single Register button. Remove the "on sale June 2" line. Add the ticket ladder and refund policy exactly as the pricing group issued them. Add offers to the structured data. Send the on-sale email to the list. |
| **June 2, within an hour** | Verified | Someone other than the volunteer | Load the live page on a phone. Confirm Register works and no stale text remains. |
| **Speaker reveal, agenda release, early-bird close, doors (Sept 9), after Sept 10** | Per the skill's transition table | Named owner each | Add each date from your marketing plan. I don't have them. The end state is an archive with a status line and no live-looking CTA. |

If June 2 slips, edit the status line the same day. Until then, the line is a promise.

## Pre-launch gate (all four must pass)

1. Every CTA transition has a date and an owner, and each one fired. The table above covers this once the later dates are filled in.
2. A stranger can answer what, who, when, where and cost in one phone screen. Test it on someone who hasn't seen the event. Cost will read "tickets June 2" until then.
3. The structured data validates, and its dates match the visible page.
4. Registration completes by keyboard alone, and the notify-me form does too.

## Questions I need answered

- What is the exact CFP close date, and has the form itself been closed?
- Is June 2 firm, and at what time and time zone?
- Is this a first edition? That decides whether any archive section exists.
- What are the speaker reveal, agenda release and early-bird close dates?
- Who owns the notify-me list and the privacy line? If nobody does, use the contact-only fallback.

The skill is a rewrite-from-scratch guide and I didn't change any files.