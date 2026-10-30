# Service styles, and what each one can carry

## Contents

1. Collect the counts first
2. What each style carries
3. The venue and supplier answers that decide a style
4. When a restriction cannot be covered
5. A worked brief, and its negative counterpart

## 1. Collect the counts first

**Sourced:** dietary requirements go into the brief as counts, not as a note, and they are collected from every person who will be fed - attendees, speakers, volunteers, organizers and sponsor staff - before the order is placed.

Two things follow that are easy to skip:

- **The population is wider than the registration list.** Volunteers and organizers eat, and they are the group most reliably left off, because nobody registers them through the attendee flow. Ask the volunteer and team leads directly.
- **The number that eats is not the number that registered.** Take the expected-show-up figure from `samber/dev-event-organizer-skills@event-no-show-management`. The gap between the two is a buffer, and it is stated separately or it disappears into an order nobody can explain afterwards.

Which categories the event commits to is not yours: `samber/dev-event-organizer-skills@event-accessibility-inclusion` decides the list and the depth. Ask for it. The categories the guide names are recorded there, not duplicated here.

## 2. What each style carries

The question is never which style is nicest. It is which one can carry the counts from step 1 without depending on anyone's vigilance. Sourced statements below are marked as such; every unmarked line is this skill's own construction.

**Individually packaged labelled meals** - each meal is its own item with its own label.

- Carries a restriction as an object rather than as an instruction. The label travels with the food, and the person it protects can read it.
- Highest throughput per volunteer, because service is handing something over.
- Portable, which matters when the grid's gap is short or people want to eat where they are talking.
- Costs: packaging waste, and the weakest rung for a meal meant to be a shared moment.
- This is the style the separate named-checklist fulfilment model in `samber/dev-event-organizer-skills@event-attendee-experience` structurally assumes - a checklist matches names to items, and items have to exist as items.

**Self-serve buffet with posted allergen labelling** - a line, a set of dishes, a card per dish.

- **Sourced practice:** post allergen detail where people can read it before the line forms - the guide's own version is a menu posted at check-in - so a restricted attendee plans rather than interrogates a server mid-queue.
- Carries a restriction only as far as the label plus self-selection. Cross-contact between adjacent dishes and shared serving utensils is the residual risk, and it is not removed by a better card.
- Its named failure, from the sibling that owns distribution: a restricted dish in the general line gets taken by the wrong person, and the person it was for goes without.
- Good throughput, genuinely social, and the rung most venues default to.

**Family-style shared platters** - platters on tables, people serve themselves and each other.

- **Sourced:** this is one of the two styles the guide names, and it needs a longer pre-service setup window than plated or individual meals. The buffer figures and the delivery question belong to `samber/dev-event-organizer-skills@event-vendor-sourcing`. Do not restate them here.
- Carries a restriction worst of the four: one shared serving utensil crossing two platters undoes the labelling.
- Buys the thing no other rung buys - a meal that requires sitting with people and reaching for the same dish.
- **Sourced trap:** chafing dishes burn fuel and some venues restrict them for exactly that reason. Confirm before the style is chosen and priced, because the whole staffing and setup plan rests on it.

**Plated per-guest service** - a plate per person, matched to that person.

- Turns a restriction into somebody's plate rather than somebody's vigilance. That is its real property, and it is a strong one where restrictions are dense or severe.
- Requires seated capacity for the whole population at once, which is an exclusion mechanism whenever the room is smaller than the headcount.
- **Sourced:** some suppliers, university catering in particular, require their own staff to serve. Ask before planning a volunteer rota around a plated service.
- Slowest service window of the four, and the one that constrains the grid rather than fitting into it.

## 3. The venue and supplier answers that decide a style

Ask all of these before ranking anything. Each is decided by the building or the supplier, not by you, and each is invisible until asked (**sourced**, except where marked):

- Is a caterer mandated? Venues, "especially universities", frequently require their own catering service. A mandated caterer collapses this decision to whatever styles that supplier offers.
- Is open flame or a chafing dish permitted? A no deletes family-style outright.
- May outside food and drink enter the building at all? (Construction: the same question asked of breaks and of anything an organizer plans to buy themselves.)
- Who is allowed to serve - your volunteers, or the supplier's staff only?
- What comes back, when, and to whom: platters, chafing dishes, tablecloths, with a pickup time and a named person rather than an open-ended arrangement.
- Can the supplier meet the dietary counts inside the standard order, or does accommodation mean a separate small order? That is a real cost and staffing difference, and it is a selection criterion rather than a detail.

Route each answer to `samber/dev-event-organizer-skills@event-vendor-sourcing`, which owns the exclusivity gate and the contract. This list exists so the style you choose survives contact with it.

## 4. When a restriction cannot be covered

**Sourced:** the guide gives two paths, and they are not interchangeable.

1. **A one-off addition to the standing order** - the supplier makes something extra for the affected people. The default, because the person still eats with everybody else.
2. **Tell the affected attendee in advance, and give them a delivery credit** so they can arrange their own meal. Honest, and clearly second: it moves the work onto the person the accommodation was for, and it separates them from the room at the moment everybody else is eating together.

Construction, and worth holding to: the second path is only acceptable when the first is genuinely unavailable, and only _in advance_. Discovering it at the serving table is not a fallback; it is a failure.

## 5. A worked brief, and its negative counterpart

Both examples below are illustrative: a shape to fill, not a recorded event. Write the brief with the user's own figures. The shape carries no numbers of its own on purpose, since every quantity in a real brief comes from the interview, the accessibility bar or `samber/dev-event-organizer-skills@event-no-show-management`, and none of them can be defaulted.

**Positive.** A one-day, single-track conference, with:

- A lunch gap short enough that a long queue would eat most of it.
- A room that seats well under the whole population at once.
- Chafing dishes refused by the venue.
- An outside caterer permitted.

> **Service style:** individually packaged labelled meals, one item per person, name-matched for every declared restriction.
> **Why:** the room seats a minority of the population, so any seated style excludes the rest. Open flame is refused, so family-style is deleted from the menu and from its axis lines rather than ranked. The gap is short enough that a buffet queue would consume most of it for whoever is at the back.
> **Counts:** the expected-show-up figure from `samber/dev-event-organizer-skills@event-no-show-management`, with the gap to the registration count stated separately as buffer. Declared restrictions collected across attendees, volunteers, organizers and speakers, one count per category the accessibility bar committed to.
> **Fallbacks:** a one-off addition to the standing order for every declared restriction. Where the supplier cannot cover one, the affected person is told far enough ahead to make their own arrangement and given a delivery credit - never discovered at the table.
> **Declaration:** allergen detail printed on each item's label and posted at the pickup point.
> **Service window needed:** handed to `samber/dev-event-organizer-skills@event-schedule-design` as a requirement, not as a grid edit.
> **Distribution:** handed to `samber/dev-event-organizer-skills@event-attendee-experience`, which picks the fulfilment model against the contract.

**Negative - the same event, done the way it usually goes wrong.**

> "Buffet, order for everyone who registered, we'll ask about allergies on the day."

Four failures in one line:

- The headcount is the registration count rather than the expected-show-up number, so the order is over by the whole no-show gap.
- The counts were not collected before ordering, so the supplier priced a menu that may not cover them, and the volunteers and organizers are not in the number at all.
- There is no declaration, so the buffet rung being described is the one this skill deletes.
- "On the day" is the moment at which every remaining option is a delivery credit nobody can spend.
