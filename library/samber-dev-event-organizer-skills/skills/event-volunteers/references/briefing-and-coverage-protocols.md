# Briefing, communication and coverage protocols

What a volunteer needs to know before their first shift, where they say it when something goes wrong, and the rule that keeps a post staffed when the next person does not arrive.

## Briefing choreography

Write the briefing per role, as a numbered sequence with times attached. FOSDEM's heralding brief, which is the most complete published example:

1. Arrive at the info desk at least 15 minutes before the shift; collect t-shirt and room assignment.
2. Be in the assigned devroom at least 10 minutes before the first talk.
3. Check in with the video volunteer already in the room.
4. Meet each speaker 10 minutes before their slot.
5. Introduce them in 30-60 seconds - name, title, one interesting fact - manage time with visible time cards, run Q&A, and cover the transition to the next talk.
6. Handle exceptions through named channels: speaker no-show goes to the coordinators immediately, a technical problem goes to the video team on its own channel.

PyCon US's Session Chair brief is the same shape with different numbers: green room 15 minutes before the first session, or 30 minutes if new to the role. Its Session Runner brief runs on 15-minute intervals - meet the speaker 15 minutes before, test equipment, upload slides, walk them to the room 5 minutes before, hand off to the chair.

Three properties make these briefs work, and they transfer to any role:

- **Every step has a time**, expressed as minutes before the thing it precedes rather than as a clock time. The same brief then works for every shift on the grid.
- **Exceptions route to a named channel**, not to "find an organizer".
- **The buffer is in the brief**, so a volunteer reading it knows their 14:00 shift means arriving at 13:45.

## The three-channel communication design

FOSDEM runs three separate channels rather than one blended one. Copy the separation; the specific tools do not matter.

- **Real-time coordination during the event**: a public chat channel, with private per-role rooms branching off it for role-specific coordination.
- **Pre- and post-event announcements**: a mailing list, explicitly _not_ the channel used during the event itself.
- **Emergencies**: a published phone number, scoped in writing to urgent coordination, safety concerns, or being unable to reach anyone by chat.

One norm rides on top: route questions through the public channel rather than direct-messaging a named coordinator. It costs the asker nothing, and it means a question answered once is answered for the next shift too, and that a coordinator going offline does not take the answers with them.

The cross-role architecture - which channel routes to which team across organizers, MCs, AV and volunteers - is designed once in `samber/dev-event-organizer-skills@event-run-of-show`. This skill plugs volunteers into it rather than designing a parallel system.

## The no-show and replacement protocol

Publish this before the event, in the same document as the shift grid. FOSDEM's version is the clearest published coverage rule to copy:

1. **If you cannot make your shift**: post in the public volunteer channel as early as possible with your name, your task, your time slot, and whether you will be late or absent.
2. **If your replacement has not arrived**: wait 10 minutes, then contact the coordinators by chat, by the published phone number, or in person if you are near the info desk.
3. **The rule the grid depends on**: _do not leave until you have confirmation of a replacement._

The third line is the whole protocol. The failure a shift grid actually suffers is not that someone does not turn up - it is that the person currently on post leaves at the end of their shift into an empty handover, and nobody notices for forty minutes. A written rule shifts the default from "my shift ended" to "the post is covered".

Two supporting decisions to make at the same time:

- **Who confirms.** Name the coordinator who acknowledges a no-show report and finds the replacement. Without a named person, the report goes into a channel and stays there.
- **Where the reserve comes from.** Floaters are the answer at any scale that has them; below that, it is the organizing team, and the organizers holding that job should know it in advance rather than discover it.

## Contrast: how hard to make the commitment

Two events with published volunteer instructions differ here, and both work.

- **FOSDEM** writes a hard operational rule (above) and expects volunteers to execute it.
- **PyCon US** relies on soft language - "please do your absolute best to avoid canceling" - rather than an escalation protocol.

The soft version costs nothing to write and depends on the coordinator improvising on the day. Prefer the written protocol:

- Wherever posts are single-staffed.
- Wherever a gap is visible to attendees.
- Wherever the coordinator will be busy doing something else at the moment it is needed.

## The volunteer-facing code-of-conduct escalation script

Brief this to **every** volunteer, not only to the named response team. Any volunteer wearing an identifiable shirt is a person a distressed attendee will walk up to, which makes the whole roster the front line whether or not it was designed to be.

FOSDEM's five-step script, written specifically for a volunteer who witnesses or receives a report:

1. **Ensure immediate safety** - of the affected person first, and of yourself.
2. **Ask the behaviour to stop, only if it is safe to do so.** The source is explicit that volunteers are _not required to confront anyone_. Say this part out loud in the briefing; a volunteer who thinks confrontation is expected either freezes or escalates something they should not have.
3. **Report immediately**, in person or through the anonymous path, whichever the event's policy provides.
4. **Document what happened** while it is fresh - what was said and done, when, where, and who was present.
5. **Support the affected person** until the response team arrives.

DevOpsDays, whose entire published treatment of volunteers is a single line about checking on them a month out, still instructs organizers separately to "Train Staff and Volunteers" on the code of conduct so they understand how to handle potential violations. Two sources at opposite ends of the formality range agreeing on this is why it is a non-negotiable briefing item rather than a menu option.

The policy itself, the response-team composition, the reporting channels and the incident runbook are all specified in `samber/dev-event-organizer-skills@event-code-of-conduct`. Take them as given, brief them accurately, and do not rewrite them here - a volunteer briefed on a script that differs from the published policy is worse than one briefed on nothing.
