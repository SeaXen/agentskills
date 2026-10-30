# Company-run format catalog

What each shape on the ladder actually is. The sizing constraints in the skill body bind here too: state no headcount, city count, agenda length, or price.

Contents: the five shapes, then the three distinctions readers most often get wrong, then the routing table.

## The five shapes

### Invite-only dinner or roundtable

- **Room** - one table, or one room around one table. Everyone can hear everyone.
- **Invitation model** - named individuals, invited personally, usually by someone they already know inside the company. There is no registration page and no waitlist; a list is worked, not published.
- **Agenda shape** - a dinner has a host and a subject; the conversation is the format. A roundtable adds a facilitator and a stated question the room is there to answer. That is the only real difference between the two: same room, same invitation model, different reason to convene.
- **What it buys** - depth against named accounts, and candour the same people will not offer on a stage or in a survey.
- **What it cannot do** - reach anyone not on the list, produce recorded content, or survive being scaled up. Two dinners are not a small conference; they are two dinners.
- **Live risk** - the compliance axis. Hosted hospitality for a named guest lands on that guest's employer's gift and anti-bribery policy before it lands on yours, and an accepted invitation cannot be withdrawn without insult.

### Executive summit

- **Room** - a curated room whose guest list is gated on seniority or on a shared situation, small enough that the guests are the program as much as the speakers are.
- **Invitation model** - invitation-only with an application or nomination step, which is what separates it from a dinner: the list is assembled rather than known in advance.
- **Agenda shape** - a short spine of framing content with structured peer discussion around it. The reason to attend is the other guests, not the sessions.
- **What it buys** - depth across a list too long for one table, plus access to people who would not attend a conference.
- **What it cannot do** - carry a public launch, or serve a developer audience that evaluates products hands-on. A seniority-gated guest list assumes a purchasing hierarchy that developer-led adoption routinely inverts (see the transposition note in the precedents reference).
- **Live risk** - the same hospitality exposure as a dinner, at lower intensity per guest but across more guests.

### Single-city user conference

- **Room** - a venue that holds a program: a stage, breakout space, and somewhere for the hallway track.
- **Invitation model** - public registration, usually with a paid or gated tier. The audience opts in.
- **Agenda shape** - a keynote spine with sessions around it. Internal structure is not decided here: track count, session-format mix and delivery mode all belong to `samber/dev-event-organizer-skills@event-format-selection`.
- **What it buys** - the only shape on the ladder that becomes an owned annual property with its own name, its own audience and its own institutional memory.
- **What it cannot do** - reach people unwilling to travel, or move a named account whose decision-maker does not attend conferences.
- **Live risk** - a venue commitment that stops being reversible long before the date.

### Multi-city roadshow

- **Room** - the same modest room repeated, usually a hotel function room or a partner's office.
- **Invitation model** - public per city, marketed locally, with the same content offered in each.
- **Agenda shape** - a compressed version of one conference day, built once and re-run. The marginal structure is the point: later stops reuse one deck, one crew and one run-of-show while the first stop absorbs the setup.
- **What it buys** - reach into geographies a single-city event never touches, at the best reach-per-effort ratio on the ladder.
- **What it cannot do** - build a property. A roadshow has stops, not editions, and next year's roadshow inherits little from this year's beyond the deck.
- **Live risk** - a registration-data and marketing-consent review per jurisdiction, and a marginal-city question that has no general answer. Set a stop rule before the first city.

### Floor-primary event

- **Room** - a hall where the floor, not the stage, is where the event happens.
- **Invitation model** - public, and often heavily comped, because the floor's value to exhibitors is the crowd.
- **Agenda shape** - three variants, ranked in the skill body's floor-shape menu: an own showcase floor, a program-plus-floor event, or presence on a third party's floor.
- **What it buys** - the highest reach on the ladder, and the only rung that can put you in front of an audience someone else assembled.
- **What it cannot do** - produce depth. Floor conversations are short, self-selected and rarely with the person who decides.
- **Boundary** - every physical question from here belongs to `samber/dev-event-organizer-skills@event-booth-experience`. The exception is the third-party rung: that skill serves the organizer who owns the hall, not a company exhibiting a stand on someone else's floor, so this collection supports that rung no further - say so.

## Three distinctions readers get wrong

1. **Roundtable versus dinner** - not a size difference. Both are one table of named invitees.
   - A roundtable has a facilitator and a question.
   - A dinner has a host and a subject.

   Pick the roundtable when you need an answer out of the room, the dinner when you need the relationship.

2. **Summit versus roundtable** - not a seniority difference either, though the summit is usually more senior. The real split is how the list is built.
   - A roundtable invites people already known to someone in the company.
   - A summit assembles a list through nomination or application.

   That is why a summit needs a runway and a roundtable does not.

3. **Roadshow versus conference series** - the split is what gets repeated.
   - A roadshow re-runs one program across places.
   - A conference series runs different programs across time.

   The roadshow's economics come from reuse, so a roadshow whose cities each get bespoke content has lost the only advantage the shape has.

## Routing table

Each shape raises a question this skill does not answer. Route it rather than improvising.

| Shape                               | Question it raises                                                 | Where it goes                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Any                                 | Why are we running this, funded from whose budget, judged on what? | `samber/dev-event-organizer-skills@corporate-event-strategy`                                                                   |
| Any with a program                  | Track count, session-format mix, delivery mode                     | `samber/dev-event-organizer-skills@event-format-selection`                                                                     |
| Any                                 | What may this event honestly claim to be?                          | `samber/dev-event-organizer-skills@event-positioning`                                                                          |
| Dinner, roundtable, summit          | Hosted travel, hospitality and guest care                          | `samber/dev-event-organizer-skills@event-hospitality` and `samber/dev-event-organizer-skills@event-vip-management`             |
| User conference, roadshow           | Venue requirements and contracts                                   | `samber/dev-event-organizer-skills@event-venue-sourcing`                                                                       |
| User conference, floor-primary      | What a sponsor buys and what it costs                              | `samber/dev-event-organizer-skills@event-sponsor-value-proposition`, `samber/dev-event-organizer-skills@event-sponsor-pricing` |
| Floor-primary (own floor)           | Layout, tier specs, setup windows, staffing, traffic               | `samber/dev-event-organizer-skills@event-booth-experience`                                                                     |
| Floor-primary (third party's floor) | Running your own stand on someone else's floor                     | Not covered by this collection - say so                                                                                        |
| Several shapes in one year          | Whether they belong together as a set                              | `samber/dev-event-organizer-skills@event-portfolio-strategy`                                                                   |
