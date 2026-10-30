# Comms and escalation

The channel-separation pattern, how to map it onto whatever medium the event has, the two escalation paths side by side, a worked role-to-channel assignment, the sourced cross-industry conventions for the live authority ladder, and the radio discipline you still set yourself.

## The published pattern: separate the organizing team's channel

Source: MLH hackathon organizer guide, communication-platform page (`MLH/mlh-hackathon-organizer-guide`). The guide specifies a minimum channel list for the event's communication platform. Every channel on it faces participants - team formation, carpool search, introductions, mentors, and one for asking organizers questions - except one: **Admin**, "channel for your organizing team", with the guide adding "we recommend creating an admin voice channel as well".

Two things are load-bearing in that, and neither is the product:

1. **The organizing team's coordination space is structurally separate from every participant-facing channel** - including the participant channel used to _reach_ organizers. That one is a public space organizers monitor; it is not the space they coordinate in. Conflating them is what puts a discussion about a failing speaker in front of the people affected by it.
2. **The pair - a written form and a live form.** The written channel leaves a log a shift handoff or a post-event review can read. The live channel carries real-time coordination that nobody will type. Neither substitutes for the other.

The source runs this on a chat platform because it describes a hackathon whose participants are already online. Nothing about the pattern requires that platform, or any platform.

## Mapping the pattern onto your medium

| Medium        | Written form                     | Live form                 | Where it breaks                                                           |
| ------------- | -------------------------------- | ------------------------- | ------------------------------------------------------------------------- |
| Chat platform | A team-only text channel         | A team-only voice channel | Needs everyone on a device and in coverage; scrolls past whoever was busy |
| Radios        | Nothing - radio leaves no record | Assigned channels         | No log at all; pair it with a written channel or a shift log on paper     |
| Phone group   | The group thread                 | A call or a shared line   | One person's silenced phone is an invisible failure                       |
| Same room     | A shared paper log at the desk   | Talking                   | Stops working the moment anyone leaves the room                           |

Choose by where staff physically are and whether coverage holds there, not by what the team already uses for planning. A planning tool that works for six months of preparation can be the wrong thing at 09:00 in a basement.

## The two escalation paths

They are different mechanisms and belong on the cue sheet as two rows, not one.

**Routine escalation - published practice.** DevOpsDays organizing guide, "Running registration" section (`devopsdays/devopsdays-web`, `content/page/organizing.md`): "Make sure any such staff have a way of getting ahold of the organizer on duty for any questions they can't answer on their own." The context matters - the guide recommends staffing the registration desk with people who are not attending talks, precisely so the front line is stable and always present. That front line will hit things above its authority: a ticket dispute, a policy question, a situation nobody anticipated.

**Incident escalation - authored elsewhere.** Safety, medical and security incidents go into the printed emergency plan: named scenarios, an emergency-contacts section including the venue's own security and a non-emergency line, and a physical printed copy on site. That document is `samber/dev-event-organizer-skills@event-risk-management`'s work. This skill's job is that the on-duty person and the channel exist and function when it is opened - not to re-author which scenarios it covers.

|              | Routine                                                    | Incident                                                                                     |
| ------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Frequency    | Many times a day                                           | Rarely, ideally never                                                                        |
| Read by      | Staff who know the event and lack authority or information | Possibly someone opening the document for the first time                                     |
| Reached how  | The org channel, to whoever is on duty for that block      | The printed contact sheet, by whichever route is fastest                                     |
| Owned by     | This skill                                                 | `samber/dev-event-organizer-skills@event-risk-management` authors it; this skill executes it |
| Failure mode | Nobody knows who is on duty, so nothing escalates          | The document is in a shared drive and the network is the problem                             |

The routine path failing is the more common problem and the less visible one: escalations that never happen look identical to a quiet day.

## Worked role-to-channel assignment

A three-room event, one written and one live channel, one organizer on duty per block:

- **Organizer on duty** - on both channels for their whole block, and the named target for every routine escalation. Publishes their own handover on the written channel at the block boundary.
- **Room leads (one per room)** - live channel for anything time-critical in their room, written channel for anything the next shift needs to know. They escalate to the on-duty organizer, never to each other, so that one person holds the whole day's picture.
- **Registration desk** - live channel only. They are stationary and busy; asking them to watch a text feed is asking them to stop doing the job.
- **Tech owner per room** - live channel, and paired with their room lead so a technical failure produces one escalation rather than two.
- **MC** - reachable, not monitoring. Somebody who is on a stage cannot be reading anything.

That last line is the one people get wrong: a role that is performing is not a role that is watching a channel. Assign a person next to them who is.

## Radio discipline: yours to set

Not established practice for a general-purpose organizer channel. Write it into the document, and present it as your own convention, not an industry standard.

Write your own rules for:

- Call signs and channel assignment by role.
- Push-to-talk etiquette.
- What happens when a channel is jammed or a battery dies mid-block.
- Whether a channel plan needs the venue's agreement.

The channel-separation pattern above carries over, but nothing radio-specific comes with it for a general organizer team. One named event's production crew does publish its own comm-discipline mechanics, scoped to that crew rather than the whole event: the Chaos Communication Congress's video crew (C3VOC) trains its volunteers on a party-line intercom between the mixer desk and camera positions - a single button held to talk on a named channel ("CAM"), a red light marking an inactive channel, and volume set per station - plus a single-extension escalation phone at the mixer desk for anything the camera or A/V crew can't resolve themselves, dialed by stating the room. Read this as channel-assignment-by-role and a named escalation contact actually working in a live multi-room event, not as a transferable radio protocol: the medium is a wired intercom and an internal phone extension, not handheld radios, and the scope is one production crew, not the general organizer channel this section is about. Say that your own conventions are yours, and check two things externally: whether the band you intend to use is licence-free in your jurisdiction, and whether the venue already runs a net you must join rather than talk over.

## The live authority ladder

Who may cut a segment short, who may delay a keynote, and how that authority is announced in the moment. `samber/dev-event-organizer-skills@event-risk-management` owns the pre-event register and the go/no-go dates that decide weeks out whether an edition happens at all, plus any safety, medical or security incident - a different mechanism from a day-of, non-safety call about one segment, and the two should not be described with the same words.

No single cross-industry standard covers this exact, non-safety call, but named conventions from three adjacent domains converge on the same shape: a short, pre-named list of roles holds the authority, one of them announces the call over a dedicated channel, and the wording used is agreed in advance rather than improvised.

- **Corporate and conference production - closest to a keynote-length call.** Production-company guidance on run-of-show documents (Meyer Pro Inc, an event-production firm) splits the decision into three named roles: the **Producer** owns the plan and any cross-cutting call - if a keynote runs long, the producer decides what gets trimmed to hold the schedule, and when stakeholders disagree the producer's call is final; the **Stage Manager** owns speaker flow and backstage readiness; the **Show Caller** executes the decision as live cue timing. A companion piece from the same source states that a run-of-show document must name the person or small group who owns final decisions on show day, with final direction flowing to the show caller or AV lead - the decision-maker and the executor are formally distinct, named roles, fixed in writing before the day starts.
- **Theatrical and broadcast stage management - the mechanic for announcing the call.** A Broadway production stage manager "calls the show": reading cues live from a script while a separate crew member relays those calls to backstage crew and performers in real time. A stage-management reference states the authority convention directly: from the start of tech until strike, the stage manager is in charge of everything related to the show, full stop, unless they explicitly delegate, and everyone defers to them unless told otherwise. The same reference documents the acknowledgment half of the mechanic: when the stage manager makes a call, the recipient answers immediately to confirm it landed - the same discipline as headset "copy" on a broadcast, and worth writing into your own push-to-talk etiquette above.
- **Live broadcast transmission - the lightweight version.** In a live TV transmission control room, the presentation director holds real-time authority alone: overriding automation, counting the show in and out of breaks, and adjusting the schedule when a segment overruns. One person, not a list - appropriate because the decision space (cut to break, extend, insert filler) is narrower than a multi-room event's.

Carry the shape, not the names: a short pre-named list, or at small scale one person; one of them "calls" while everyone else executes; the wording used to announce the decision is agreed in advance. No public conference-production team running a keynote-scale event publishes its own internal chain for this exact call. Decide yours, write it into your document, and attribute it to whoever decided rather than to any of the conventions above - none of them is your event's own ladder.
