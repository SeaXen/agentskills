# The venue technical specification and the AV supplier brief

Two documents leave this skill. They go to different people, at different times, and confusing them is how a venue ends up being asked for a camera crew and a supplier ends up being asked about rigging points.

- **The venue technical specification** goes back to venue sourcing, as questions the venue answers in writing during negotiation.
- **The AV supplier brief** goes to whoever contracts the supplier, as a specification the supplier quotes against and is held to.

The DevOpsDays organizing guide sets the bar a supplier has to meet: they "should be able to provide a camera or cameras and record the feed off the board into a computer". Both templates below are starting structures built backwards from the failure modes in the redundancy reference; treat them as structures to adapt rather than as a standard checklist.

Real published AV RFP templates exist from named AV production companies and industry associations, and the supplier brief below is cross-checked against them. The Catalyst Companies' AV RFP template groups audio, lighting, video, drape, load-in/out and schedule requirements similarly to sections 3-6 and 9 below, but treats streaming and recording as single bullets inside "video requirements" with no resolution, codec, platform or turnaround spec. MPI's RFP guidance is the only industry-association source that treats recording and hybrid delivery as a line item to specify up front rather than an afterthought. dmakproductions' AV conference checklist has dedicated camera and hybrid categories covering recording, livestreaming, camera positions and backup stream - the closest public echo of sections 3, 7 and 8 - but as checklist bullets, not specs with values. Meeting Tomorrow's RFP template and ShowREADY's AV RFP guide are built around vendor qualification (references, prior experience, escalation process) rather than technical specification, and neither names streaming or recording as a deliverable. No published AV RFP template, from a named supplier, an industry association, or a conference-organizer blog, covers capture posture per room or acceptance criteria at the depth sections 2 and 12 specify.

## Part 1 - The venue technical specification, as questions

Venue sourcing states the rule this follows: "Do not invent an equipment list or a bandwidth figure. Put it to the venue as a question it must answer in writing."

Ask, do not specify. An answered question becomes a contractual fact. An unanswered specification becomes an argument on load-in day.

**Connectivity**

1. What upstream bandwidth is _guaranteed_ to the room we will stream from - not the shared attendee figure, and not a best-effort number? Is a dedicated or reserved connection available, and at what cost?
2. Is a wired connection available at the production position, or is wireless the only option?
3. Is there a second, independent path to the internet (a different provider, a cellular fallback the venue provides)?
4. Who administers the network on the day, and are they reachable during our hours?
5. Is any port, protocol or destination blocked by default, and who lifts that?

Never fill in a bandwidth figure of your own. Ask for the guaranteed number, then check it against whatever your supplier or encoder documentation states.

**Room and rigging**

6. What is installed in each room already: projection, screens, a sound system, a mixing desk, microphones, a lectern, a confidence monitor?
7. Where are the rigging points, what load do they take, and who is permitted to rig - us, the venue, or a nominated contractor only?
8. Can cameras be positioned at the back and side of each room without blocking a fire route, and can cable runs be taped across those routes?
9. Where is the room's own audio output available as a feed, and in what form?
10. What lighting exists over the stage area, and is it controllable independently of the house lights?

**Space and access**

11. Is there a space that can serve as a production position or control room, in or adjacent to each room?
12. What are the load-in times, the access route, the lift dimensions, and the storage available between days?
13. What power is available at the stage and at the production position, on how many circuits?
14. Is a house technician included, for which hours, and what are they responsible for?

**Recording and streaming permissions**

15. Are there restrictions on recording or streaming from this space - a house AV monopoly, an exclusivity clause, a fee?
16. Is a supplier we bring ourselves permitted, or must we use the venue's nominated supplier?

Question 16 changes who you write Part 2 for, so ask it early.

## Part 2 - The AV supplier brief

Structure the brief so a supplier can price it line by line and so delivery can be checked against it afterwards. The last section is the one organizers omit and the one that makes the brief enforceable.

**1. The event, in five lines.** Dates, venue, rooms, sessions per room, audience size per room. Nothing else.

**2. Capture posture.** Per room: nothing, recorded for later, or streamed live. State it explicitly per room rather than implying it from the equipment list - this is the line that determines everything the supplier quotes.

**3. Coverage per room.** Camera count and whether operated or fixed, per room, per session block. If a room's tier changes between the plenary and the breakout sessions, say so.

**4. The audio chain.** Microphone type and count per room (lectern, handheld, lavalier, audience question mic), the mixing position, and the explicit requirement that the recording takes its audio feed from the board rather than from a camera microphone.

**5. Speaker-driven requirements.** Straight from what `samber/dev-event-organizer-skills@event-speaker-experience` collected: live demos needing a network drop, audio playback needing a feed into the mix, hardware props needing power or space, and every non-standard connector somebody will arrive with. List them; do not summarise them as "standard laptop connectivity."

**6. Recording deliverables.** Format, resolution, frame rate, audio channels, file naming convention, and how and when files are handed over. Name the handover medium and the moment it happens - before the crew disperses, not "afterwards."

**7. Streaming deliverables, if any.** Destination platform, expected concurrency, whether the supplier provides the uplink or uses the venue's, latency tolerance, and what happens on a drop.

**8. Redundancy required.** State the rung you chose, as a requirement rather than a hope: the independent second audio recording, the crew monitor on the encode output, the labelling and clock-sync convention, the collection cadence.

**9. Crew and hours.** Who the supplier provides, for which hours, including rehearsal and load-out. Name your own counterpart and state that they own the brief.

**10. Rehearsal.** When it happens, what is tested, and who attends. If streaming, published streaming guidance makes this a requirement rather than a preference.

**11. Accessibility deliverables.** Whatever accessibility decided - captioning feed, hearing loop, interpreter position and lighting. You are delivering someone else's decision; carry it verbatim rather than reinterpreting it.

**12. Acceptance criteria.** How delivery is judged, written before the event:

- Every scheduled session has a playable file with audible board-sourced audio.
- Files are named to the stated convention.
- Files are handed over at the stated moment.
- The streamed sessions ran with the stated redundancy in place.

This section is what turns a brief into something you can hold a supplier to, and it is the section that is always missing.

## Sending it

Send both documents through the people who own those relationships - the venue specification via venue sourcing, the supplier brief via whoever runs supplier selection and contracting. Do not open a direct negotiation channel of your own; two people negotiating with one venue is how a term gets agreed twice, differently.
