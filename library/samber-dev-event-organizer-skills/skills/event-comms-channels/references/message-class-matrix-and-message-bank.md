# Message-class matrix and message bank

Contents: the message-class taxonomy · the worked routing matrix · escalation tiers · a negative example · eight message-bank templates.

## Message-class taxonomy

The nine classes below are this skill's own construction, not a published taxonomy. Classify by the two things that decide routing, how fast a message has to land and who it concerns, never by who wrote it.

| Class               | Deadline                         | Concerns                                                  | Example                                                       |
| ------------------- | -------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| Disruption          | Minutes                          | Everyone affected, often including people not yet on site | Venue change, room closed, livestream down, session cancelled |
| Live change         | Minutes to an hour               | Everyone in one room, or everyone on site                 | Talk starts 20 minutes late, track swapped rooms              |
| Day logistics       | Hours                            | Everyone on site                                          | Lunch is open, badge desk closes at 17:00, last shuttle       |
| Pre-event practical | Days                             | Every registrant                                          | Know-before-you-go, directions, what to bring                 |
| Programme news      | Days to weeks                    | Every registrant, and often the public                    | Schedule published, speaker added, workshop opened            |
| Social / community  | No deadline                      | Whoever opted in                                          | Introductions, dinner plans, hallway-track threads            |
| Sponsor and partner | Days                             | Every registrant, sometimes one segment                   | A sponsor workshop, a partner discount                        |
| Incident statement  | Set by the authority, not by you | Decided case by case                                      | A public statement after an incident                          |
| Wind-down           | Days                             | Everyone on every channel being closed                    | Recordings are up, this channel closes on the 14th            |

Two classes are not yours to write: the incident statement (authority and wording sit with `samber/dev-event-organizer-skills@event-code-of-conduct`) and anything on the mailing list (copy and cadence sit with `samber/dev-event-organizer-skills@event-attendee-email-sequences`). You still place them on the matrix, because a matrix with holes gets filled in by whoever is holding a phone.

## Worked routing matrix

Illustrative and this skill's own construction, worked for a two-day, three-room conference with a livestream, five volunteer writers, and the roster at Menu 1's chat-plus-status-page rung. Rows are message classes. Cells name the channel that carries the message first.

| Class               | First channel                           | Also                                                | Never                                                                       |
| ------------------- | --------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| Disruption          | Status page, then a push pointing at it | Public broadcast, on-site screens, PA               | Chat only - the people it concerns are not in the building                  |
| Live change         | Chat broadcast channel                  | On-site screens; PA if it affects a room in session | Email - hours-scale channel, minutes-scale message                          |
| Day logistics       | Chat broadcast channel                  | On-site screens                                     | Status page - it is not an incident and it trains people to ignore the page |
| Pre-event practical | Email                                   | Channel directory link inside it                    | Chat only - not everyone joined                                             |
| Programme news      | Email                                   | Public broadcast                                    | Chat only                                                                   |
| Social / community  | Chat open channel                       | -                                                   | Email and broadcast - this is the noise the split exists to keep off them   |
| Sponsor and partner | Email, batched                          | A named sponsor channel where one exists            | The broadcast channel, one message per sponsor                              |
| Incident statement  | Whatever the authority names            | -                                                   | Anywhere at all, from anyone else                                           |
| Wind-down           | Every channel being closed, plus email  | -                                                   | One channel only                                                            |

The single load-bearing rule in that table: **a minutes-scale message never rides an hours-scale channel, and an hours-scale message never rides the disruption path.** Both directions do damage - the first is missed, the second desensitizes the channel that must not be missed.

## Escalation tiers

Only for the matrix rung of Menu 2. The four tiers are this skill's own construction, not a published escalation model. Each names a trigger, a wait and the next channel, so escalation is a rule anyone on shift can execute rather than a judgement call by whoever notices.

- **Tier 0** - the message goes on its first channel. No escalation.
- **Tier 1** - if the class is Live change or above and the change affects a session already in progress, escalate to the in-room channel (screen or PA) immediately, with no wait. Nothing scheduled beats something happening now.
- **Tier 2** - if the class is Disruption and the situation is still unresolved after a fixed interval you set in advance, repeat on the status page with a timestamp, even when there is nothing new. Silence during an outage reads as abandonment: "still working on it, next update in 30 minutes" does not.
- **Tier 3** - if the disruption changes whether or where someone should travel, escalate to the push channel with the widest reach you have, regardless of cost or noise. This is the one tier allowed to wake people up.

Set every interval before the event and write it on the matrix. An interval chosen during an outage is chosen badly.

## Negative example

A real-shaped failure, constructed to show what the matrix prevents:

> The venue moves a workshop room at 08:40. A volunteer posts it in the chat's open channel, where it lands between two threads about coffee. Twenty minutes later a second volunteer, not seeing it, posts the same change in the broadcast channel with a different room number, taken from an earlier draft.
>
> Nobody puts it on the screen outside the old room. At 09:00, attendees who never joined the chat are standing in the wrong place, the people who did join have two contradictory answers, and the one authoritative surface - the status page - says nothing.

Four faults across three menus:

- No routing rule said this class goes to the broadcast channel first (Menu 2).
- No owner meant two writers with two sources of truth (Menu 3).
- The dynamic on-site surface was never in the roster (Menu 1).
- The status page existed but carried no rule about when to use it (Menu 1's promotion condition, taken without its escalation tier).

## Message-bank templates

The eight templates below are unsourced: this skill's own construction, and deliberately flat. They are field sets, not finished copy, and none is ready to send as written.

The register that voices them is `samber/dev-event-organizer-skills@event-cultural-identity`'s output. Rewrite the wording into that register, keep every field, then run a humanizer pass on anything attendees will read.

Draft them before the event. Fill the bracketed fields on the day.

1. **Delay** - "[Session] in [room] now starts at [time], about [n] minutes late. Nothing else on the schedule moves. Next update by [time] if that changes."
2. **Room change** - "[Session] has moved from [old room] to [new room], starting [time]. Signs are up at [old room]. If you are already seated in [old room], you have [n] minutes."
3. **Venue change** - "Read this before you travel. [Event] on [date] is now at [address], not [old address]. [Transport note.] Doors from [time]. Full details and updates: [status page URL]."
4. **Session cancelled** - "[Session] at [time] is cancelled. [One-line reason if it can be said without naming a person.] [Replacement or 'the room is open for the hallway track'.] Sorry for the change."
5. **Livestream interrupted** - "The livestream for [track] is down as of [time]. We are working on it and will post here again by [time] whether or not it is fixed. Recordings will still be published."
6. **Lost property** - "Found: [item, described without anything identifying]. Claim it at [location] until [time]. After that it goes to [venue lost property / an organizer's bag]."
7. **Last call** - "[Thing] closes in [n] minutes at [location]. After that, [what happens instead]."
8. **Closing and wind-down notice** - "That is a wrap on [event]. [One line of thanks in the register.] Recordings go up by [date]. This channel [stays open read-only / closes on date / moves to X] - see [link]."

Two rules across all eight:

- State the new fact before the apology. A message that apologizes first buries the information.
- Give the next update time whenever the situation is unresolved. A message with no next-update time generates the questions the channel then has to answer one by one.
