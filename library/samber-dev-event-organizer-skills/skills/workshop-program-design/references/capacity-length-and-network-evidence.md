# Capacity, session length and network evidence

Contents: the three ceilings · the demand-vote mechanic · every published session length · density ratios and what they are not · the named live-failure causes · the venue's written network questions · what this reference deliberately does not give you.

## The three ceilings

Capacity is not a preference. It is the lowest of three numbers, and which one binds is the useful output - state it, because it is also the thing to fix if you want a bigger room next time.

- **Room ceiling.** Seats, with the furniture the exercise actually needs. A workshop layout packs looser than theatre rows, and power at the seats is a separate question from seats. The DevOpsDays organizing guide's band for a technical event's breakout rooms is a mix holding 10-20 and 20-40, with chairs that can form a circle - see `samber/dev-event-organizer-skills@event-venue-sourcing`'s space program.

  Two rooms in a published 2017 workshop-day grid were named _Small Room_ and _Workspace_, which is a reminder that a venue's own room names carry no capacity information at all.

- **Coverage ceiling.** How many people the instructor plus whatever the facilitator menu bought can reach before someone quietly gives up. The one published convention runs the other way, from learners to helpers: the Carpentries' one helper per eight to ten learners on top of two instructors. Invert it for a starting ceiling only when two instructors teach, then adjust for the exercise's failure density, and state the sizing logic with the number.

- **Exercise-throughput ceiling.** How many people can get real hands-on time given what is genuinely finite: boards, cables, licence seats, per-participant logins, physical stations, or a shared cluster's capacity. This is the ceiling most often missed, because it is invisible on the registration page and appears only when the twenty-first person needs the ninth device.

  MLH's hardware guidance implies it throughout - dedicated stations for fabrication, assembly, testing and specialised electronics, each with its own equipment list - without ever converting it into a headcount.

## A demand-vote capacity mechanic

A published 2017 workshop day put four parallel workshops in each of two blocks and asked attendees to choose before the day: _"Please vote for your favorite workshops!"_, with the stated purpose _"This will help us determine which rooms to place them in."_ Current DevOpsDays chapters run Open Spaces instead: same-day self-selection into breakout topics, which sets an unconference agenda rather than sizing workshop rooms. Treat the pre-event vote as one 2017 instance, not standing practice.

That is demand-driven room assignment, and it inverts the usual order. Instead of guessing a capacity and hoping the right number of people want it, collect expressed interest and match the sessions to the rooms you have. It costs one question in whatever pre-event mail already goes out, and it is the only method here that produces a capacity number from evidence rather than from a guess.

Its limit is worth naming: a vote ranks demand, it does not lift any of the three ceilings. A workshop that wins the vote and needs one device per participant is still capped by devices.

When demand exceeds the ceiling, add a section rather than raise the cap. A university system running online Carpentries workshops held each one under 50 learners, and when sessions overfilled they opened another concurrent section rather than adding seats, with "around four" helpers per session. That 50 is one online programme's seat count, not a standard, and four helpers for 50 is thinner than the convention it ran under. Some conferences push the question to the proposer instead: HRI's call asks for "any limits in terms of maximum number of participants (e.g. for group activities)" - a field `samber/dev-event-organizer-skills@event-cfp-design` owns.

## Every published session length

Report these as instances. There is no average here, and computing one across these events, formats and years would be false precision.

| Instance                                                  | Length                      | What it was                                                                                                                                            |
| --------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DevOpsDays Amsterdam 2017, workshop-day morning block     | 09:00-11:30 (150 min)       | Four parallel workshops, hands-on technical                                                                                                            |
| DevOpsDays Amsterdam 2017, workshop-day afternoon block   | 12:00-14:30 (150 min)       | Four parallel workshops, after a catered lunch                                                                                                         |
| DevOpsDays Singapore 2025, Team Topologies workshop       | 180 min                     | Published as _"Agenda (180 minutes)"_, structured as _"four 45-minute segments"_                                                                       |
| DevOpsDays pre-event workshop day, published slot options | 45 / 90 / 120 / 180 min     | See `samber/dev-event-organizer-skills@event-format-selection`'s precedents reference                                                                  |
| PyCon US tutorials                                        | 3 hours, separately paid    | Same source                                                                                                                                            |
| The Carpentries                                           | two days, or four half days | _"a two full day or four half day format"_ (Carpentries instructor training); a standalone training, not a conference session                          |
| Software Carpentry, setup at the start                    | 30-60 min                   | _"Plan for the first 30-60 minutes of the workshop to be spent on installation and setup, because it's going to happen anyway."_ Older instructor tips |
| MLH, team-formation workshop                              | under an hour               | _"Team formation workshops generally don't last over an hour."_ Not a technical hands-on session - a social mechanic                                   |

Three patterns, stated as observation:

- Hands-on technical sessions inside a conference ran 150 or 180 minutes in these instances: three data points, two from one event. Standalone training such as the Carpentries runs in days, a different format.
- Setup eats the front of every block. Count the machine check (at least 20 minutes, up to 30-60 by the same tips page) inside the length, not on top of it.
- The one sub-hour figure is attached to a format with no exercise in it, so do not read it as the short end of a range that includes the others.

MLH names two placement constraints for a workshop running inside a larger event rather than on its own day:

- _"Limit the number of workshops during an event as they consume valuable building time."_ - an argument for the do-nothing rung.
- _"Schedule them earlier in the event when hackers are most likely to need guidance."_ - a real scheduling input to hand to `samber/dev-event-organizer-skills@event-schedule-design`.

## Density ratios, and what they are not

The hackathon per-attendee figures - roughly four devices and at least two and a half outlets per attendee - come from a hackathon organizer guide, recorded in `samber/dev-event-organizer-skills@event-venue-sourcing`'s space program with that pole stated. They describe a room of people building for a weekend.

**Power has a workshop-specific convention; bandwidth does not.**

- **Power.** The Carpentries' room requirements ask for _"Power outlets for all participants. This may include setting up extension cords or power strips."_ The Smithsonian's Carpentries host checklist budgets _"One power strip for every 3 learners"_. MLH adds the hardware version: check that the venue's outlets actually work, and _"Provide sufficient surge-protected power strips at every station."_ Strips are the cheap fix for a room whose outlets are on the walls and whose participants are in the middle.
- **Bandwidth.** The Carpentries ask only for Wi-Fi _"that can withstand everyone using it together"_ - a requirement, not a figure. Borrow the hackathon figure as an upper bound and say that is what you are doing, exactly as `samber/dev-event-organizer-skills@event-venue-sourcing` instructs. The older Software Carpentry room check states the real test: _"Do you have enough bandwidth to handle fifty people hitting your version control repository at the same time? (How do you know?)"_

## The named live-failure causes

The named causes are unusually specific, and none of them is bandwidth.

- **The venue blocks device classes.** _"Work with venue infrastructure to ensure the network allows IoT and other devices, as these are often blocked by standard university networks."_ Written for hardware, true for anything unusual on the wire.
- **The venue blocks protocols.** A published workshop's own prerequisites depend on it: participants need an RDP client and, in the page's parenthesis, _"(RDP protocol allowed)"_.
- **The participant's own VPN.** _"Turn off VPN (we use websockets extensively)"_ - published by the workshop author as a known failure of a browser-based lab.
- **The participant's ad-blocker.** From the same note: _"pause AdBlock for the lab domain (there are no ads)"_.
- **A burst of simultaneous cold installs.** The published mitigation is the pre-download ask, with its reason attached: _"Encourage hackers to pre-download software drivers and IDEs ahead of time to reduce network load during the event."_
- **A shared exit address.** A room behind one venue address looks like one heavy user to every outside service: a container registry's anonymous pull limit or an API key's request quota trips for everyone at once. Pre-pulled images, signed-in registry accounts or per-participant keys remove it; more bandwidth does not.
- **Peak load that is not the download.** _"Secure robust, high-speed Wi-Fi and plan for peak usage (uploads, documentation, data streaming)."_

And one participant-side fallback, published by the workshop rather than the organizer: a session requiring internet access to a remote lab tells participants to _"(Use Wi-Fi or your own data)"_. Naming a fallback in the prerequisites is cheaper than any organizer-side remedy and it is the only one that survives the venue failing entirely.

## What to put to the venue in writing

`samber/dev-event-organizer-skills@event-venue-sourcing` already asks venues to answer in writing what sustained bandwidth a room can guarantee, on what circuit, with what fallback. For a workshop room, add three questions that the failures above make necessary:

1. How many simultaneous devices does this room's access point hold, and what happens at the limit?
2. Which protocols and ports are blocked, and can they be opened for a day?
3. Are unusual device classes blocked by default, and who can grant an exception on the day?

If the venue will not answer these, that is the promotion condition for removing the live dependency - the answer being unavailable _is_ the evidence.

## What this reference deliberately does not give you

Four numbers no published workshop convention gives. Derive each one for your own session rather than borrowing a figure that will read as measured once it is written down.

- **A participant ceiling for a hands-on workshop.** Not a number, not a band - take the lowest of the three ceilings above.
- **A per-seat bandwidth figure specific to a workshop room.** Borrow the hackathon figure as an upper bound and say that is what you are doing.
- **A relationship between session length and capacity**, though the two obviously interact through the throughput ceiling.
- **A full protocol for when the network fails mid-session.** The one published live fallback is the offline kit: older Software Carpentry instructor tips carry USB sticks with lesson files and _"installers for Canopy, Anaconda, RStudio, and other software (in case the room's WiFi won't handle the load)"_, plus _"some sort of WiFi hub (in case networking in the room isn't working)"_. The rest of the live response belongs to `samber/dev-event-organizer-skills@event-run-of-show`; agree it with that plan rather than improvising on the day.
