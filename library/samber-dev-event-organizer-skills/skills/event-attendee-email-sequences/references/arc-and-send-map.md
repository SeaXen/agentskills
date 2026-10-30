# The attendee email arc, send by send

Every send below fires on a **date**, never on a per-recipient behaviour. The dates themselves arrive fixed from the marketing plan and `samber/dev-event-organizer-skills@event-ticket-pricing` - this file says what goes inside each send, not when it happens.

Contents: Announcement · Registration confirmation · Agenda release · Last call · Know-before-you-go · Day-before nudge · Post-event thank-you · The no-registration collapse · What never belongs in any of them

---

## 1. Announcement

**Fires on**: the announcement date fixed by the marketing plan.
**Segment**: the whole list, plus any prior-edition list that passes the consent check.
**One job**: this event exists, it is dated, here is where to look.

Must carry: event name, exact dates, city and venue-or-online, who it is for in one line, and a single link to the landing page. Nothing else competes for the click.

The forwardable variant: when attendees typically need an employer's approval, add one short paragraph the recipient can forward without editing - dates, total cost including travel, and what the company gets from sending someone. Keep it a paragraph inside the same email, not a second send.

Must not carry: a full agenda that does not exist yet, a countdown, or a price `samber/dev-event-organizer-skills@event-ticket-pricing` has not published.

## 2. Registration confirmation

**Fires on**: registration itself. Transactional, so it goes to everyone regardless of marketing consent.
**Segment**: the individual registrant.
**One job**: prove the registration worked, and say what arrives next and roughly when.

Must carry: what they registered for, the dates, any order or ticket reference, and one sentence setting the expectation that a practical-information email arrives about a week before. That sentence is what stops the know-before-you-go being mistaken for a marketing send later.

Must not carry: a promotional block. Mixing marketing content into a transactional send is how a transactional exemption stops applying.

## 3. Agenda / speaker release

**Fires on**: the agenda-release date fixed by the marketing plan.
**Segment**: everyone, though its purpose is the not-yet-registered.
**One job**: give someone who waited a concrete reason.

Must carry: two or three specific things now confirmed - a named speaker, a track, a workshop - and the link to the full program. Specificity is the whole value; "an amazing lineup" says nothing a reader can act on.

Optional and skippable: this send is the first thing to cut when the runway is short or the cadence budget is tight.

## 4. Last call

**Fires on**: the day before a cutoff `samber/dev-event-organizer-skills@event-ticket-pricing` owns - early-bird close, a price-tier change, or a capacity cap.
**Segment**: the not-yet-registered only, cross-referenced against the registered list.
**One job**: state one dated fact.

Must carry: what changes, exactly when, and the link. The date does the work; you do not need urgency language because the deadline is real.

Must not carry: an invented deadline, a manufactured scarcity claim, or a second last-call after the first. One cutoff, one email. If there is no real cutoff, there is no last-call email.

## 5. Know-before-you-go

**Fires on**: roughly one week before doors.
**Segment**: registered attendees, split by role - you write the attendee variant.
**One job**: everything needed to arrive prepared, in one place they can find again.

Its full structure has its own reference file. Two rules belong here:

- every fact in it comes from `samber/dev-event-organizer-skills@event-attendee-experience` rather than from you
- the code of conduct and accessibility sections are not optional

## 6. Day-before nudge

**Fires on**: the evening before, or early the morning of for a full-day event.
**Segment**: registered attendees.
**One job**: the one thing - when and where.

Must carry: check-in opening time, the address, and a single link back to the know-before-you-go. Three lines is a good length. This is the email people read on a phone while walking.

Must not carry: new information. Anything that appears here for the first time was missing from the email a week ago, and a third of the recipients will never see it.

## 7. Post-event thank-you

**Fires on**: one to three days after.
**Segment**: everyone who registered, including no-shows - a no-show who receives the recordings is next edition's attendee.
**One job**: thank people, deliver what was promised, and hand off to feedback.

Must carry: thanks, links to recordings or slides when they exist (or an honest date for when they will), and the feedback survey link. The survey instrument itself belongs to `samber/dev-event-organizer-skills@event-feedback`; you write the email around it.

Optional: the next edition's date, if it is actually fixed. A "save the date" for a date that later moves costs more than the goodwill it buys.

---

## The no-registration collapse

An event with no registration has no attendee list, so this arc does not apply. The identity-consistent output is the practical information published once on the event's own page, plus a single public announcement through whatever channels the marketing plan already uses.

That is the right answer for that posture, not a reduced version of a real sequence. Do not construct a list to make the arc apply.

## What never belongs in any of these emails

- **Anything the marketing plan or `samber/dev-event-organizer-skills@event-ticket-pricing` owns.** A date you would prefer, a price you inferred, a cutoff you moved.
- **On-site facts you did not receive.** A guessed check-in time in a reminder produces a queue at the wrong hour.
- **No-show mechanics.** Overbooking, waitlists, deposits and seat-release are structural fixes owned elsewhere; the reminder email is the only lever in this skill.
- **Speaker, sponsor or volunteer instructions.** Their versions of the week-before email exist, and other skills own them.
- **A second automated email that has not been announced.** Whenever a differently-branded tool will email attendees, name it and its timing in the send before it.
