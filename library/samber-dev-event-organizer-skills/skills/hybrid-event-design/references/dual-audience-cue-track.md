# The dual-audience cue track

The run of show itself belongs to `samber/dev-event-organizer-skills@event-run-of-show`. Everything here is an addition to that skill's artifact, written to be handed to it.

## Table of Contents

- [One document, one more column](#one-document-one-more-column)
- [What the column carries](#what-the-column-carries)
- [The gap rows](#the-gap-rows)
- [Rows where the room is told something out loud](#rows-where-the-room-is-told-something-out-loud)
- [The two-audience disruption gap: what's answered, and what is still yours to decide](#the-two-audience-disruption-gap-whats-answered-and-what-is-still-yours-to-decide)
- [A worked row](#a-worked-row)
- [A positive and negative pair of cue rows](#a-positive-and-negative-pair-of-cue-rows)

## One document, one more column

The rule is a column, not a document.

Two documents drift, and the drift is invisible until the day. The moment the room's rundown and the stream's rundown are separate files, the person who moves a row moves it on one of them, and the other stays correct-looking. A column cannot fail that way: the row is the unit, and the person changing what the room does is looking at what the stream does at the same time.

The synchronization rule follows from that: **the room's transition and the stream's transition are the same row.** A cue that appears in only one column is precisely where the two audiences diverge, and those rows are what to re-read at the briefing.

## What the column carries

Per row, three things and no more:

- **What the stream is showing** - the stage, the slides, a holding card, or nothing.
- **Who owns that** - a name, matching the run of show's convention of naming people rather than functions.
- **What the remote audience is being told**, if anything is said or posted at that moment.

Resist adding equipment detail to this column. Which camera and which encoder belong to `samber/dev-event-organizer-skills@event-production`'s own documents. Putting them here creates a second place they can be wrong.

## The gap rows

The rows that need the most attention are not sessions.

A room fills a break with corridor conversation, coffee and people finding each other. A stream fills it with silence, and a remote attendee cannot distinguish a scheduled break from a dead feed. That ambiguity is the single most avoidable remote failure, and it costs a row.

Give every gap a row with something in the stream column. In ascending order of what it costs:

- **A holding card that names what is happening and when the next session starts.** Near-zero, and it removes the ambiguity entirely.
- **A posted line in the remote channel at the start of each gap**, saying the same thing in text for anyone who has the channel open and the video muted.
- **Somebody speaking on the feed**, which is Menu 3's starved rung and the only option that makes a gap feel like part of the event rather than an interruption to it.

The first is enough on its own. An event that cannot manage a holding card during breaks should reconsider whether the parity rung it chose was real.

## Rows where the room is told something out loud

The second class of row worth flagging is anything the room hears that was never typed: a room change, a delay, a swapped speaker, a session running long.

This is a documented failure mode: a session running late in the room and the remote side never being told, with the staff busy in the room. It is an attention failure, and the cue sheet is where attention gets assigned in advance.

Mark those rows. Flag any row whose room column carries a spoken announcement, so the briefing can walk the flagged rows and confirm each one has a stream-column entry.

## The two-audience disruption gap: what's answered, and what is still yours to decide

`samber/dev-event-organizer-skills@event-schedule-design` writes a disruption priority order into the grid document and hands it over. `samber/dev-event-organizer-skills@event-run-of-show` restates it in its own words, and executes it: "protect the plenary or keynote first, protect the headline commitment the audience showed up for next, minimize how many other sessions the fix disturbs, then lock the revised grid for the rest of the block."

Read the audience in that sentence. It is singular. Every hybrid has two, and that order says nothing about which one wins when they compete. Hybrid conferences and AV crews have written about most of what this raises. Two pieces stay genuinely open.

**Does a dead feed on a keynote ever justify holding the room, or does the room always continue?** A 2021 Dagstuhl seminar's published hybrid-conference guidelines name this as a decision organizers must make explicitly, not a rule with a default answer. Any conference with active remote participation "needs to decide, for example, whether to pause the conference program if technical difficulties prevent remote attendees from participating," and those guidelines recommend "headroom in planning (e.g., using sufficiently long breaks)" as the mitigation rather than a pause policy. VLDB 2021 (roughly 180 in-person and 840 remote attendees) did not pause. When Zoom links failed, a backup video was missing, or a speaker changed presentation format mid-session, "the situation was fixed rapidly by the help of our Zoom technicians ... and session chairs," and "the conference continued running smoothly despite such minor hiccups." Treat keep-the-room-going-and-fix-in-parallel as the default, and a planned pause as the exception you state in writing, not the reflex.

**Who has the authority to cut the feed, and does that decision go through the same on-duty person as everything else?** C3VOC, the AV crew behind FOSDEM and the Chaos Communication Congress, draws this line in its own crew documentation: "While the stagemanager is responsible for the organizational issues such as information flow, crowd control, etc. the A/V Technican is responsible for the technical issues," and when a problem exceeds what the technician can fix alone, "this person knows how to contact (e.g. VOC Helpdesk, the person who is responsible the A/V Setup in the Saal, etc)." The call to give up on a feed sits inside the technical chain, escalated upward, not with the room's chair. SIGCHI's Hybrid Working Group guide adds the seniority constraint: "overall responsibility for the technical setup throughout the event should remain with organizers in senior roles, rather than student volunteers," who reported "high levels of stress when dealing with technical problems" without that backstop. Name the technician's own senior escalation point before the day, not the room lead.

**If the remote-side person and the room lead need the same technician, who gets them?** No organizing guide, AV crew handbook or conference postmortem states a rule for this. Documented practice shows jurisdiction avoiding the conflict rather than resolving it: C3VOC keeps the stagemanager off technical calls and the technician off content calls; VLDB 2021's report describes technicians and chairs working the same incidents in parallel, without ever describing what happens when their calls on one shared resource disagree. Decide this one yourself, in writing, before the day.

**When a session is moved to fix an in-room problem, does the remote programme follow it or lose that session?** Also unanswered as a policy question: no report or guide states it either way. What is documented is the separate matter of telling remote attendees something happened, which does not by itself settle whether the session moves with them.

**How is a moved or rescheduled session communicated to remote attendees who cannot see the room?** Two formally documented channels exist. IETF's RFC 7649 assigns this as a named duty of its meeting "Jabber Scribe": "Relay to the chatroom participants any logistical or procedural issues related to the meeting (e.g., known technical glitches at the physical meeting or delays in starting the session)," with network or streaming problems themselves routed to a separate published contact (`tickets@meeting.ietf.org`) rather than left to the scribe alone. SIGCHI's hybrid guide recommends the same shape for conferences generally: "a real-time point of contact for remote attendees, e.g., enabling conference attendees to reach out to a dedicated SV team or the remote engagement chair via real-time chat," warning against relying on "intermittently checked email" for this. FOSDEM's own 2015 incident is a real instance of the pattern: when the opening keynote failed to stream, the team posted publicly that they were "working hard to fix the remaining teething problems," pointed viewers to the live stream page, and noted that talks were still being recorded even while the stream was down. Give the remote side a named live-chat contact, not a channel someone checks between sessions, and use it the way FOSDEM did: say what broke, what still works, and where to watch.

Decide the two open pieces before the day: contested-technician priority, and whether a moved session follows the remote programme. Write them into the run of show alongside the inherited priority order and the documented defaults above, and record who decided them. Improvising them at the moment two things break is how a remote audience learns which one it is.

## A worked row

A single row, both columns, at a session boundary. Columns are shown stacked for readability. In the real document they sit side by side on one row.

Times are written as placeholders on purpose - no interval here is a recommendation, and changeover timing varies widely by venue and setup.

```
TIME      <slot end> - end of session, room 1
ROOM      Room lead cuts Q&A. Introducer moves to lectern.
          Next speaker already standing stage-left, slides loaded on the house machine.
          Introducer's line: name, talk title, one sentence.
STREAM    Cut to holding card at the room lead's call. Owner: Priya.
          Remote channel: "Next up at <next slot start> - <talk title>. Questions open now."
          Back to stage on the introducer's first word.
FLAG      Spoken announcement in room column - stream entry present.
```

The row is one decision made twice, in the same place, by people who can see each other's half.

## A positive and negative pair of cue rows

### Negative

```
TIME      <slot end>
ROOM      Session ends, next speaker up.
STREAM    (blank)
```

Nothing is wrong with this row until the day. Then the feed sits on an empty stage for the length of a laptop swap, and the remote audience - who cannot see the room, the next speaker walking up, or anyone reacting - starts refreshing.

If the swap runs long, some of them leave, and none of them can tell whether they left a break or a failure. The row is not wrong. It is silent, and silence is what a remote audience reads as broken.

### Positive

```
TIME      <slot end>
ROOM      Room lead cuts Q&A. Next speaker stage-left, slides loaded.
STREAM    Holding card with next talk title and start time. Owner: Priya.
          Line posted in remote channel at the same moment.
FLAG      Spoken announcement - stream entry present.
```

Same minute, same people, one more column. The remote audience knows what is happening, knows when it ends, and has somewhere to put a question while they wait.

The difference between the two rows is not equipment and not budget. It is that somebody wrote the second column while writing the first, rather than after.
