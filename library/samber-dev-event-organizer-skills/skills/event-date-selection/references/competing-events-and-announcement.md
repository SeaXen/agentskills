# Competing events, venue windows, and announcement

Contents:

1. The competing-event scan, step by step
2. Dodge or piggyback: deciding per event
3. "Get Options": carrying windows into the venue conversation
4. The announcement gate checklist
5. Worked example (illustrative) and its negative counterpart

## 1. The competing-event scan, step by step

The DevOpsDays organizing guide frames this check as **"load balancing"** across the field, not turf protection: the field is better off when its events are spread out. An organizer who only asks "does this hurt me" misses the events that hurt the audience by stacking.

Run every step below for each candidate date at two radii:

- **Same date** - a direct clash: attendees, speakers, and volunteers must pick one event.
- **Same week, Monday to Sunday** - no overlap, but the events still split travel budgets, days off work, speaker availability, sponsor attention, and the local press cycle. Same-week hits are also where piggybacking lives, so record them even when nothing overlaps.

1. **List your own event family first.** Any event network with a shared homepage lists its scheduled editions; this is the cheapest hit and the one the DevOpsDays guide names directly. It is also the narrowest - it surfaces only events branded like yours.
2. **Widen to adjacent topics and different organizers.** This is the gap step 1 cannot close, and where most real conflicts live: your attendees choose between your event and _any_ event they would spend the same travel budget on, not only ones in your category.
3. **Consult a cross-topic public conference calendar.** A crowdsourced dataset such as confs.tech is one example of the kind of tool that does this - named as an example of the category, not as a dependency. Its coverage is contributed by organizers who already know about it, so absence from it proves nothing.
4. **Add a call-for-papers listing scan.** CFP aggregators surface events that have not yet announced dates publicly but have already claimed a window, which a calendar of confirmed events misses.
5. **Check local, non-topical events** in the host city across each candidate window: marathons, festivals, trade fairs, major sporting fixtures. They take venues, hotel inventory, transit, and local attention regardless of subject.
6. **Ask two or three people in the audience** what else they are planning to attend that season. This catches the events no aggregator lists - regional meetup series, company user conferences, internal engineering weeks - and it is usually the highest-yield ten minutes in the whole scan.
7. **Record every hit with the decision made on it**, not just the hits you avoided. The rejected-window reasoning is the part that cannot be reconstructed next year.

## 2. Dodge or piggyback: deciding per event

The DevOpsDays guide names **piggybacking** as a deliberate tactic, not a consolation: scheduling immediately before or after another major event in the same city so travelling attendees justify one trip for both. That makes proximity a two-sided variable, and the decision has to be made per event rather than by reflex.

Lean toward **piggybacking** when:

- The other event draws the same people to the same city.
- A meaningful share of your audience travels rather than commutes.
- Your event is small enough that being the second stop is an advantage rather than a comparison.

Lean toward **dodging** when:

- The two events compete for the same finite resource: the same sponsors' budgets in the same quarter, the same speakers, the same venue.
- The other event is close enough in subject that attending both feels redundant rather than complementary.

Two adjacency risks the tactic carries, both judgment calls rather than documented rules:

- Attendee fatigue after a large multi-day event.
- Sponsor budget already spent at the bigger show.

Ask a sponsor directly rather than assuming either way.

## 3. "Get Options": carrying windows into the venue conversation

The DevOpsDays guide advises lining up several candidate windows rather than fixing one date before approaching venues, because availability is uneven across a week and a month - "you might find that they can accommodate you better during some parts of the week than others."

Practical shape:

- Carry three to five surviving windows, each already cleared by the constraint checks, so any of them is genuinely acceptable. A window you would refuse is not an option; it is a bluff that collapses when the venue picks it.
- Present them as equivalent rather than ranked. A ranked list invites the venue to offer only the top one and decline.
- Ask what the venue's own quiet periods are. Off-peak windows are where rate flexibility lives, and the venue knows them better than any guess from outside.
- Treat a venue's counter-offer as a new candidate window and put it back through the constraint checks before accepting - an availability win that lands on an unchecked observance is not a win.

## 4. The announcement gate checklist

The hard prerequisite, from the DevOpsDays guide: **a date cannot be announced until there is a known way to handle money.** Discovering the gap late has caused rescheduled and cancelled events. Check all of these before publishing:

- A way to receive money exists: a ticketing arrangement, a payment processor, or an entity that can invoice sponsors - whichever the event's model actually needs.
- Someone is accountable for the money, by name.
- The date itself is decided internally and no longer under discussion.
- Every calendar category is checked or explicitly recorded as outstanding, and the user has seen the outstanding list.
- The dodge-or-piggyback call has been made on every competing event found.
- The trigger chosen from the announcement menu has its own precondition met - a signed venue contract for the venue-locked trigger, a confirmed anchor speaker or an openable CFP for the program-teased one.

Below any of these, the date can be decided but not published. An internal date is still a variable; a published one is a promise, and retracting it costs a recurring event far more than the wait would have.

## 5. Worked example (illustrative) and its negative counterpart

Both examples below use invented events and invented dates. They illustrate the shape of the reasoning only - every date, attendance figure and outcome in them is illustrative, and none should be reused as evidence.

### Positive: a professional-audience conference

A two-day platform-engineering conference for working engineers, audience mostly from three neighbouring countries, second edition.

- **Day type:** weekday, from the employer-time rule (DevOpsDays guide). Tuesday-Wednesday chosen over Thursday-Friday so that neither day is a boundary day.
- **Season:** last edition ran in late spring and sold out slowly; the team proposes the same season as a hypothesis, explicitly labelled as such rather than as a seasonal fact.
- **Constraint depth:** the multi-geography observance rung, promoted because the audience spans three countries. Public holidays verified from each country's official calendar for the specific year; one candidate window dropped because it straddled a public holiday in the country supplying the largest share of attendees.
- **Competing-event scan:** two adjacent-topic conferences found in the same season. One is in the same city two days earlier - the team schedules to abut it deliberately, so travelling attendees make one trip. The other is dodged: same sponsor pool, same quarter.
- **Windows carried to venues:** four, presented as equivalent. The venue offers a fifth in an off-peak week; it goes back through the constraint checks, clears, and is accepted.
- **Announcement:** venue-locked trigger. Money handling confirmed, contract signed, date published.

The deliverable records every rejected window with the constraint it failed - which is what makes next year's selection start ahead rather than from scratch.

### Negative: the same event, done by reflex

- **Day type:** Friday chosen "so people can travel home" - a boundary day serving neither pole, and endorsed by neither guide.
- **Season:** "August is dead, everyone's on holiday" asserted as fact, never tested against the event's own prior editions.
- **Holidays:** last year's observance dates reused. They were lunar and moved; the event lands mid-observance for a substantial part of the audience.
- **Competing-event scan:** only the event family's own homepage checked. The conflict that actually costs attendance comes from an adjacent-topic conference nobody looked for.
- **Piggybacking:** a large event in the same city the week before is treated as a threat and fled, discarding a documented tactic without considering it.
- **Venue:** one date fixed first, then venues called. Every venue is booked; the search stalls with no fallback.
- **Announcement:** date published to claim the slot before ticketing exists. Payment setup takes longer than expected, the on-sale slips twice, and the published date becomes a promise the team cannot yet keep.

Each line in the negative example maps to one failure mode in the skill body; read together they are the same event losing its audience one unchecked assumption at a time.
