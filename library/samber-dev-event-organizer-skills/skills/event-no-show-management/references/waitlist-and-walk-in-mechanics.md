# Waitlist, ceiling arithmetic and walk-in lane mechanics

## Contents

- The ceiling arithmetic, worked
- A negative example
- Waitlist ordering rules and what has to be published
- The promotion brief handed to `samber/dev-event-organizer-skills@event-attendee-email-sequences`
- Walk-in lane requirements at the desk
- What this skill does not do

## The ceiling arithmetic, worked

Do this in five lines and show all of them, because the ceiling has to survive being questioned by whoever signs the venue contract.

**Positive example (illustrative) - a free community event, 250-seat room, catering guaranteed 10 days out.**

1. Hard capacity: 250 seats (venue contract; fire code states 260, so 250 is the binding number).
2. Aimed attendance: 250 - the room is the goal, there is no reason to aim below it.
3. Expected show-up rate: ~50% for a free-registration event (sourced; free band 40-60%, hackathon-network trendline ~50% across 323 events).
4. Registration ceiling: 250 ÷ 0.5 = **500 registrations, and not one more** - this is the sourced 2x ceiling, reached from both directions.
5. Expected show-ups handed to catering: **250**, with the 250-registration buffer named separately so nobody orders 500 lunches.

The ceiling is a number in the registration form's configuration and a named person who closes it, not an intention. Write down who that person is.

**Negative example (illustrative) - the same event, done wrong.**

> "Free events see 40-60% no-shows and hackathons report a 30-50% drop-off, so call it 45%. We're aiming for 250 but we'd love a full room, so let's leave registration open and see where it lands - we can always squeeze people in."

Eight faults in two sentences:

1. **Two different figures averaged into one.** The 40-60% band and the 30-50% range measure different things from different sources; 45% answers neither question.
2. **The one figure written as an instruction was ignored.** The ~50% trendline exists specifically to set a multiplier; the two descriptive figures do not.
3. **No ceiling.** "Leave registration open" is the one posture the source explicitly forbids, and it is the difference between absorbing a gap and guaranteeing that registered people are turned away.
4. **"Squeeze people in" is an occupancy decision** made by someone with no authority to make it, against a limit the venue contract and its insurance assume.
5. **No waitlist**, so everyone above the line is lost rather than held.
6. **No date** on anything - no close date, no promotion date, no catering lock date, though the guarantee locks in 10 days.
7. **No arithmetic shown**, so the number cannot be corrected next edition or defended this one.
8. **No handoff.** Catering will be given whatever number is on the registration page on the day someone thinks to ask.

Both examples are illustrative, not observed events. The capacity, the dates and the quoted reasoning are invented to carry the method. Only the ~50% rate, the 40-60% band, the 30-50% range and the do-not-go-over-double ceiling inside them are published figures, each with its own scope.

## Waitlist ordering rules and what has to be published

Two ordering rules are defensible.

- **Signup order (FIFO), drained on a named date.** The default: it needs no justification, and no one skipped can argue with it.
- **Proximity to the venue** (MLH hackathon organizer guide): "Try to give priority to hackers who are closer to your event since they are more likely to actually show up." The guide states it as a reason rather than a measured show-up gain, so any gain you expect from it is self-set.

Whichever you pick, publish it at the moment the waitlist opens. Three reasons, in the order they will hit you:

1. Someone skipped will ask, and an ordering rule explained afterwards reads as one invented afterwards.
2. Proximity ordering is an allocation decision made on registrants' location data. You have to be able to state that it is being used, and it is not the kind of rule that can be changed quietly mid-window once people have registered against it.
3. A proximity rule visibly disadvantages people who travel. On an event whose positioning claims regional or international draw, or whose accessibility posture is published, that is a contradiction someone will find. Decide whether you can defend it before you adopt it, not after.

Also fix, at the same moment:

- The date the list is drained.
- How long a promoted person has to claim the seat before it moves on.
- Who decides.

A promotion with no claim deadline is a seat held indefinitely for someone who has already stopped reading.

## The promotion brief handed to `samber/dev-event-organizer-skills@event-attendee-email-sequences`

Every promotion is a transactional send, and `samber/dev-event-organizer-skills@event-attendee-email-sequences` owns its copy and cadence in full. Hand it a brief, not a draft. The five slots below are this skill's own template, not a sourced format:

- **The trigger** - what event causes the send (the list is drained on date X; a specific seat came free; the pre-doors release opens).
- **The audience** - who exactly receives it, and whether it is everyone on the list or a promoted subset.
- **The deadline in the message** - the claim window, expressed as a date and time.
- **What changes for the recipient** - they are in, and what they now have to do.
- **The overbooking ratio in use**, so that sibling knows whether "everyone who registered" or "everyone confirmed after the cut" is the real audience for every _other_ send in the arc.

Also tell it when the ceiling closed registration, because a last-call acquisition email sent after the form closed is a broken promise arriving from your own domain.

## Walk-in lane requirements at the desk

The sourced mechanic (MLH hackathon organizer guide, `check-in-process.md`): "Consider having a separate form for late registrations, even if they have to wait until after all preregistered attendees have had time to check-in. Everyone checking in should still complete your full registration form."

Three properties are load-bearing and none is optional:

- **Separate form.** A late arrival goes through a different intake than the pre-registered queue, so the fast queue stays fast.
- **Held back.** The lane opens only once the pre-registered check-in window has closed. Running both at once is how the opening rush becomes a queue out of the building.
- **Full form regardless.** Skipping it costs the headcount, the code-of-conduct agreement, the dietary and accessibility data, and the emergency contact list - every one of which matters more on the day than it did at registration.

What this skill gives the desk: the expected walk-in volume and the ratio behind it, and the time the lane opens. What the desk gives back: how many actually came through it. Everything about staffing, queuing and badge sorting is `samber/dev-event-organizer-skills@event-attendee-experience`'s, which already builds a pre-sorted pickup with its own walk-in lane as its default check-in model.

## What this skill does not do

- **A live, per-seat promotion during the event** - releasing a specific no-show's seat to a specific waitlisted person while doors are open. Untested. The walk-in lane fills the room from below instead, and does so without anyone tracking which named person failed to arrive. Ticketing-platform waitlist automation (timed claim windows, automatic rollover to the next person) is the nearest established mechanic: every documented version of it runs before the event, against cancellations and expired holds, never during it. One platform's own copy calls it a recovery mechanism for post-sale inventory gaps, not an in-event promotion strategy. The closest real-world analog to a live named-seat swap is airline gate standby, which sits outside this domain entirely.
- **A refundable deposit returned on attendance.** Out of scope as an attendance mechanic; see the argued refusal in SKILL.md.
- **Comped and scholarship seats' own show-up rate.** Plan them at the general free-seat rate, and count them separately so that next edition has a rate of their own.
