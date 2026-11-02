# Copperline JS #2: reminder emails and post-mortem

You didn't paste the four drafts, and I can't see them. These are written from scratch. Paste yours if you want me to match your voice.

## First, the number

268 of 480 is a **56% show rate**. That's roughly normal for a free event. The usual range is about 40–60%. That's a rule of thumb from memory, not a figure I checked.

- The email side didn't cause a disaster.
- At 100% attendance you'd have had 180 people for 300 seats. The no-shows are the only reason the room worked.
- **Better reminders will make capacity worse.** If they lift attendance to 70%, that's about 336 people for 300 seats. Fix the capacity mechanics below first, or the new emails will hurt you.

## The four emails

Placeholders are in `[brackets]`. Every email has one job and one link.

### T-14: lock it in

**Subject:** You're in. Copperline JS, [date]
**Preview:** Add it to your calendar before you forget.

Hi [first name],

You have a seat at Copperline JS on **[day, date], [time], at [venue]**.

The seats are free, but the room only holds 300 and we had 480 RSVPs. Every seat that goes empty is a seat someone on the waitlist could have had.

1. [Add to calendar]
2. Can't make it? [Release your seat]. It takes 5 seconds and someone else gets in.

See you there,
[Name], Copperline JS

### T-7: give a reason to come

**Subject:** [Speaker] is on stage in 7 days
**Preview:** Here's the lineup and how to get there.

Hi [first name],

One week out. Here's what you're showing up for:

- **[Time]**: [Speaker 1], "[talk title]"
- **[Time]**: [Speaker 2], "[talk title]"
- **[Time]**: [Speaker 3 or panel]
- **After**: [drinks/food/networking]

**Where:** [venue, address], [transit/parking in one line]
**Doors:** [time]

Plans changed? [Release your seat] so someone on the waitlist can take it.

[Name]

### T-2: confirm or release

**Subject:** Still coming Thursday? Confirm your seat
**Preview:** Unconfirmed seats go to the waitlist at [time/date].

Hi [first name],

We're two days out and the room is full on paper, but we know not everyone makes it.

**[Yes, I'm coming]**: one click, and your seat is guaranteed.
**[I can't make it]**: one click, and your seat goes to someone on the waitlist.

If we haven't heard from you by **[day, time]**, we'll offer your seat to the waitlist. Confirmed seats are never released.

[Name]

### Morning-of: logistics only

**Subject:** Today, [time], [venue]. Your ticket is inside
**Preview:** Doors at [time]. Here's your QR code.

Hi [first name],

Copperline JS is **tonight**.

- **Doors:** [time]. Talks start at [time].
- **Where:** [venue, address] ([map link])
- **Bring:** this email's QR code: [QR]
- **Heads up:** seats not claimed by [time] go to the waitlist. If you're running late, [reply to this email].

Can't make it after all? [Release your seat].

See you tonight,
[Name]

## What else went wrong operationally

I'm inferring some of this from your numbers. Treat each as a question to check against what actually happened.

1. **No waitlist or deliberate overbooking policy.**
   - 480 RSVPs for 300 seats means the form never capped at capacity, or it capped on purpose with no plan for the gap.
   - Decide the number: cap registration at about 400–430 against 300 seats, and put everyone beyond that on a waitlist.
2. **No way to cancel.** Without a "release my seat" link, people who knew they weren't coming had nothing to click. That's the biggest single fix.
3. **No confirmation step.** The T-2 email above turns "RSVP'd three weeks ago" into a live headcount.
4. **No check-in data.**
   - You know 268 walked in, but do you know *who*?
   - Without scanned or ticked check-ins, you can't segment no-shows from attendees or follow up with either group.
5. **No tracking by sign-up date and source.**
   - Seats claimed 6 weeks out and seats claimed in the last 3 days almost always have different show rates.
   - Without that split, you can't tell whether the problem is the reminders or the sign-ups themselves.
6. **Free ticket with zero friction.**
   - A free RSVP costs nothing to abandon.
   - Options: a refundable deposit, a "why do you want to come" field, or a confirm step like the T-2 email.
7. **No calendar invite at sign-up.** The first email should have carried an `.ics` file or a calendar button.
8. **Nothing after the event.**
   - Did no-shows get a "sorry we missed you, here's the recording or slides" email?
   - Did attendees get a thank-you and a survey?
   - Did anyone ask no-shows why they didn't come? You have the real answer sitting in 212 inboxes.
9. **Door and venue unknowns.** Did you have a headcount at the door, a fire-code limit, and a plan for if 350 had turned up? Capacity is a safety question as well as a comfort one.
10. **Shared ownership.** One person owning all email, with no scheduled sends, no review, and no one else watching the numbers, is a process gap. It isn't a personal failing.

## For the team conversation

- Open with the 56% figure and the 480-vs-300 math. That's the real story: the emails were a minor factor, and capacity planning was the bigger gap.
- Own the cadence gap, since two emails was thin, but don't take blame for the whole 44%.
- Come with a plan: the four emails, a waitlist cap, a release link, and check-in tracking.

**Next step:** tell me your RSVP-form tool and email tool, and I'll turn the capacity and waitlist rules into a concrete setup.