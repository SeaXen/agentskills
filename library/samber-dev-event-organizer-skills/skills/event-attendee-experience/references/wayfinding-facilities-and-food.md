# Wayfinding, facilities and food

Parts of this page are self-set defaults and parts are published practice, labelled as such. The labels are load-bearing - say which kind an answer came from.

## Wayfinding and signage - self-set defaults

Everything in this section is self-set, offered as a default worth trying rather than as reported practice. Organizer guides describe the artifacts - floor plans, a help desk, colour-coded restrooms on a map - and leave the design of a sign to the organizer.

- **Design from decision points, not from rooms.** Walk the floor plan as an attendee: every place where a person must choose a direction is a decision point, and every decision point gets a sign or a person. Compare two venues: one with twelve rooms down a single corridor has one decision point, while one with four rooms across two floors and a lift lobby has five.
- **Sign the destination, not the geography.** "Track B - Auditorium, 2nd floor" is read at walking speed. "Room VIA A&B" is a room number the attendee has never seen before and has to match against a programme they are holding folded in one hand.
- **Put the first sign before the first choice.** The most common gap is the entrance: an attendee who has just been given a badge is standing in the one place nobody thought to sign, because the desk volunteers can answer verbally. They can, until forty people arrive at once.
- **Honour the accessible route on the signs themselves.** A sign that names only the staircase makes the accessible route invisible even when it exists. The accessible route is set by the accessibility bar handed to you - showing it is wayfinding's job.
- **Sign the things people leave the programme for**: toilets, water, the quiet room, food, and the way back to the main hall. These are asked about far more than session rooms and are signed far less.
- **Colour-coding on a map does inclusion work.** PyCon US 2026 marks gender-neutral restrooms in purple on every floor plan - a wayfinding decision carrying a policy without a policy statement. This is the one signage practice with a source behind it.
- **Count the signs added by hand on the day and keep them.** They are the audit of this design, and the cheapest input to next edition's version.

## Networking space and the hallway track - self-set defaults

The requirement is published - the design is self-set. DevOpsDays names the space as a first-class venue requirement: "room to hang out: not everybody attends sessions, and some are more interested in the hallway track. If there is some room for the food or a quiet room that's a plus". How that room is laid out is left open. Self-set defaults:

- **Put it on the path, not off it.** A hallway track happens where people already are - between the session rooms and the food - and dies in a room people have to decide to enter.
- **Give it a reason to stand still**: high tables, power, and coffee that is available between breaks rather than only during them. Seating that is too comfortable turns a networking space into a laptop room, which is a different and also legitimate use - pick which one you are building.
- **Do not schedule it.** A scheduled networking session is a session. The hallway track is what the gaps in the grid are for, and the grid is another skill's.
- **Keep it acoustically separate from the quiet room.** They are opposite requirements and they get placed next to each other constantly, because both are "not a session room".

## Facilities: what a documented catalog looks like

The fullest published facility specification of the kind is PyCon US 2026's public onsite-information page:

- **Quiet Room** - named, located on a specific floor in a specific room, with published daily hours.
- **Nursing and wellness suite** - placed in the lobby directly across from registration. The placement is the design signal: a high-traffic, first-encountered location rather than a remote corner.
- **Gender-neutral restrooms** - colour-coded on every floor plan.
- **First-aid stations** - multiple named locations, each mapped.
- **Help desk** - near the main entrance, scoped to directions, lost-and-found and scheduling questions.

Not mentioned anywhere on those pages: first-timer orientation, a prayer or meditation room, childcare. Treat that as a gap in the published material, not as evidence the event has none.

The opposite pole is equally legitimate. FOSDEM 2026 runs 8,000+ attendees with one infodesk absorbing room locations, schedule questions, practicalities and lost-and-found, a permanently staffed free cloakroom, and a Red Cross team present the whole weekend.

Its own accessibility page draws that exact line for one of the four: "Unfortunately we can not offer a dedicated quiet space on the campus," pointing attendees to a public park five minutes away instead - a stated absence, not a gap. A prayer room, family room and sign-language interpretation remain absent from every practical, services and accessibility page with no page stating so either way - **a documentation gap to raise with the user, not a confirmed absence.** A page that does not cover something is much weaker evidence than a page stating "we do not offer this," which is exactly the distinction FOSDEM's own quiet-room line now draws.

## The quiet room's dual purpose

The quiet room is the one facility two skills depend on at once, and it is designed once. It has to serve:

- **Decompression** - the framing every source uses. Published checklists and event materials describe a quiet room as a place "to allow attendees a chance to decompress", and at least one large event ran quiet spaces specifically for social anxiety and introverts . It is care infrastructure, not overflow space.
- **Confidential intake** - the code-of-conduct runbook borrows it as the private space a responder can take a report in.

The two purposes constrain the same three properties, and a room that satisfies one and not the other fails silently:

| Property  | Decompression needs                      | Intake needs                                           | Design that serves both                                                                         |
| --------- | ---------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Location  | Away from noise and the main flow        | Reachable without a walk of shame past the whole event | Off a secondary corridor, one turn from a main route                                            |
| Enclosure | Quiet enough to actually rest            | A door that closes, walls that carry no sound          | A real room, never a curtained corner                                                           |
| Signage   | Visible enough to be used without asking | Not labelled as an incident space                      | Signed plainly as "Quiet Room", with the intake use known to staff and unadvertised on the door |

State this constraint wherever the room is located. The failure mode is not disagreement between the two skills - it is each assuming the other solved it.

## Food and dietary mechanics

**This skill deliberately refuses to rank the two fulfilment models.** They are not options with different value per unit of effort - they are two shapes of catering contract, and the contract picks one. Ranking them would be false precision.

**Model A - collect in advance, serve from a separate table** (MLH):

1. Ask everyone who will receive a meal - attendees, mentors and volunteers alike, not only ticket-holders - about restrictions before the event, early enough for the vendor to plan.
2. The category list to ask against: vegetarian, vegan, celiac and gluten-free, common allergies including lactose and peanut, kosher, halal. The categories your event actually commits to are set by the accessibility bar handed to you, not chosen here.
3. Store restricted meals at a **separate** table and check names off a printed list as they are handed out, specifically so they are not taken by the wrong person out of the general line.
4. Two honest fallbacks when the primary caterer cannot accommodate someone: order a one-off meal from the same vendor, or give the attendee a delivery gift card and tell them **in advance** that they are buying their own meal that day. Telling them in advance is what separates a fallback from a failure.

**Model B - live per-meal request** (PyCon US 2026): a named catering staff member takes special requests such as kosher and allergen-free at each meal. No pre-collected list to match, and it depends entirely on the caterer carrying that capability under contract.

Distribution choreography, which applies to either model (MLH):

- **Multiple serving tables, never one.** Even a small event turns a single table into a long wait.
- **Check people off at the head of the line.** It catches someone rejoining the queue and, more usefully, is where a restricted-diet attendee gets redirected to their own table.
- **Stagger the announcement by room or table** rather than one blanket call, which floods a single line at once. Close with a final call once the flow has thinned.

Dietary answers are health data in several jurisdictions. Collect only the categories you will act on, keep the printed distribution list to the meal service, and destroy it afterwards rather than filing it with the registration export.
