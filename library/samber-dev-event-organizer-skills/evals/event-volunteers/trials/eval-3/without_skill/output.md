# PyLisbon volunteer portal: recommended scope

**Recommendation:** build a small portal, not "the works". Your need is about 8–12 volunteers and about 15 shift slots per event. That is about 30 slots a year across two events. Accounts, profile pages and a full reminder engine cost more to build and maintain than they save at that size. The two features that earn their keep are **shift self-service** and **reminders**. Everything else is optional.

## Sizing (my estimates, please correct)

| Role | People | Window |
|---|---|---|
| Setup | 2 | 17:15–18:30 |
| Check-in table | 2–3 | 18:00–19:15 (arrival peak) |
| Room / AV / mic runner | 1–2 | 18:30–22:00 |
| Food, drinks, welcome | 1–2 | 18:30–22:00 |
| Teardown | 2–3 | 22:00–22:45 |

Allow for no-shows. Plan about 20% more sign-ups than slots.

## Tier 1: build this quarter (MVP)

1. **Event and shift setup (admin).** Create an event with date, venue, and roles. Each role has start and end times and a headcount. Clone last event's setup in one click.
2. **Public sign-up page, no password.**
   - The volunteer enters name and email, picks shifts, and gets a confirmation email.
   - A magic link in that email lets them view, swap, or cancel their shifts.
   - Skip passwords and "create account". Two events a year means people forget passwords every time.
3. **Self-service swap and cancel.**
   - The volunteer can cancel up to a cutoff, for example 48 hours before.
   - A cancellation frees the slot and alerts the organizer.
   - Inside the cutoff, they must contact an organizer.
4. **Reminder emails.** Send three, each from a template:
   - Confirmation, sent immediately.
   - T-7 days: "confirm you're still coming", with a one-click confirm or cancel. This gives you time to backfill.
   - T-1 day: logistics, covering arrival time, door, who to ask for, and a phone number.
   - Optionally a day-of text or WhatsApp message to the organizer group, which is more reliable than email on the evening itself.
5. **Organizer dashboard.**
   - A grid of role × time slot showing filled, open and unconfirmed.
   - A waitlist that promotes automatically when someone cancels.
   - CSV export.
   - A printable run sheet for the check-in table: who is where and a phone number.
6. **Privacy basics (EU).**
   - Collect name, email, and optionally phone.
   - State the purpose, for example "used only to organize this event".
   - Provide a delete-me link.
   - Purge data after about 12 months unless the person opts into the volunteer pool.

## Tier 2: only if Tier 1 shows a real need

- **Returning-volunteer pool.** Opt-in checkbox plus an "invite last time's volunteers" button. This is the useful part of a "profile", and it can be one table with no profile page.
- **Role preferences and skills.** For example "can run AV" or "speaks Portuguese and English at the door". Use a free-text note plus tags.
- **Calendar file (.ics)** attached to the confirmation email.
- **Post-event thank-you** email with a one-question feedback form.
- **Basic history.** Count of events attended, visible to organizers only.

## Don't build

- **Public profile pages per volunteer.** They add a privacy surface, moderation work, and nothing for anyone to browse.
- **Full accounts with passwords, social login, or roles and permissions.** You need one admin role.
- **In-app chat or messaging.** Use email and your existing community channel.
- **Gamification, badges, leaderboards.** At this scale they can read as pressure on unpaid people.
- **Hours tracking and certificates**, unless someone actually asks for them.
- **Your own email infrastructure.** Use a transactional provider such as Postmark, Resend, or SES.
- **Shift marketplaces and trading between volunteers.** Cancel, then waitlist, covers it.

## Cheaper alternatives to compare first

Run the same checklist against these before writing code:

- A shared sheet plus a form, with a scheduled email script, covers about 80% of Tier 1.
- Off-the-shelf volunteer tools such as Sign-up Genius-style products, Luma, or Meetup helper roles may cover sign-up and reminders already.
- If you build anyway, a single small app with Postgres and a transactional email API is enough. Two events a year need no queue infrastructure, only a scheduled job that runs hourly.

## Build order (about 1–2 weeks of part-time work)

1. Data model: event, role, shift, volunteer, signup. Use soft delete on signups.
2. Sign-up page, confirmation email, magic-link manage page.
3. Admin grid and CSV export.
4. T-7 and T-1 reminders, and waitlist promotion.
5. Test with a dry run: 10 fake volunteers, one cancellation, and one no-show.
6. Print the run sheet. Check that the check-in lead can read it on paper.

## Questions that would change this

1. Do you want volunteers across several PyLisbon events a year, or per-event only? Multi-event favors the Tier 2 pool.
2. How many organizers will use the dashboard, one or several?
3. Do volunteers get anything in return, such as free entry or a t-shirt? That affects the data you track.
4. Is the main failure today no-shows, last-minute gaps, or organizer admin time? Spend effort on whichever it is.
5. Is the goal to ship a product, or just to cover volunteers well? If it is the second, the sheet-plus-script option wins.