# Caldermoor Conf: is a conference run by volunteers different from a company's, and can you skip "who's in charge"?

**Short answer:** Mostly the same, with one change that cuts against the suggestion. Keep the informal culture, but name an organizer on duty for every block. "Whoever's closest" fails, and it fails worse with your setup.

I read the run-of-show skill and its three references and followed them. Where I make a call without your input, I say so.

## 1. Is it different from a company's conference?

The skill tested the community-versus-vendor split. It holds for hosting and for little else.

| Area | Differs for you? | Why |
|---|---|---|
| Hosting (MC) | ✅ Yes, legitimately | Community events can spread hosting across organizers, or use one MC. DevOpsDays writes "one or more MCs" as a valid design. A vendor event typically uses one briefed, rehearsed host with a full script. |
| Transitions, radio range, handoffs losing context | ❌ No | A transition takes the same seconds whoever paid for the venue. |
| Who decides during a problem | ❌ No, and it matters more | See section 2. |

**What changes your plan is scale and doubling up, not who paid.** Two things apply to you:

- **One room, five people.** You need little channel architecture, because you can see each other.
- **Three of the five are performing.** That is the real constraint. Two give talks and one MCs. Someone on stage isn't watching a channel, and an MC is "reachable, not monitoring".

## 2. Skipping "who's in charge"

**⚠️ Don't skip it, but you can drop the hierarchy.** Two ideas are being mixed here:

- **A boss.** You don't need one. Nothing in the skill asks for a chain of command.
- **A named organizer on duty per block.** You do need this.

The skill lists "no named on-duty person, on the theory that whoever is nearest decides" under *delete, do not demote*. It calls it a single point of failure "wearing flexibility as a costume". In practice one person ends up deciding everything and can't leave the building.

**Your setup makes it worse:**

- The person closest to a problem may be on stage, or about to be.
- With 3 of 5 performing, only 2 of you are reliably free at any moment. The "closest person" is often the MC or a speaker mid-talk.
- A volunteer at the door can't tell who decides. Escalations that never happen look identical to a quiet day.

**What to do instead (light version, about an hour of writing):**

1. **Named on-duty organizer per block**, published on the cue sheet where a door volunteer can read it.
2. **The on-duty person is not the MC, and is not on stage during their block.** The skill lists this as a reason to add a second person on duty (the "paired" rung). With 5 people and 3 performing, check that the schedule leaves a free person for each block.
3. **Separate the MC from the speaker introducers.** The MC runs the day's flow. Someone else introduces each speaker. Your two speakers can't introduce themselves, so rotate this among the others.
4. **A room lead who owns the room's clock.** This is a role I define, not published practice. In a one-room event the on-duty organizer can hold it. Write down what it may decide alone: hold a start, cut Q&A, fetch the tech owner. Write down what it must escalate.
5. **Pre-agree the live authority call.** One named person calls it and everyone else executes. The wording is agreed in advance, and the recipient acknowledges. The skill says to attribute this ladder to whoever decided it, so write "the five of us agreed on [date]", not "standard practice".

## 3. What I'd put in the run of show

### Roles (names are placeholders)

| Role | Who | Note |
|---|---|---|
| MC | ___ | One MC is fine. Not on-duty organizer, not a speaker introducer. |
| Speaker introducer | rotates, per session | Never the speaker being introduced. |
| Organizer on duty | ___ per block | Free of stage duties for the block. |
| Room lead | on-duty organizer, or a second free person | Authority written down. |
| Tech owner | ___ | One machine, one operator. |
| Door and registration | volunteers | Live channel only. They need to read who is on duty without asking. |

### Cue-sheet depth: timed grid with named owners

This is the default. It means a row per segment and per transition, each with a start time, room, named owner, tech owner and escalation. Move up to scripted transitions (queue position, one machine, a spoken line) if you run lightning talks, demos or back-to-back sponsor slots.

Do not use the public schedule as the staff document.

Give the opening and closing the deepest rows. The opening checklist is: what the event is, who the team is and how to reach them, wifi and logistics, the schedule, and short sponsor content. The closing should be pre-announced.

Give room resets their own timed row, started while the previous segment is still running.

Move to a **word-for-word MC script** only if this is a first edition where nobody has done it, the opening is recorded or livestreamed, or a sponsor line must be read verbatim.

### Comms: one organizers-only channel, kept separate from every attendee channel

- Use a team-only group chat for the written log, plus talking or a call for live. Your five can see each other, so nothing heavier is needed.
- Do not use the attendee channel for organizer traffic.
- Move up to radios or a call only if anyone on duty will be out of coverage or away from a screen, such as a basement venue.
- Put two escalation paths on the sheet:
  - **Routine:** a post hits something above its authority and goes to the on-duty organizer.
  - **Incident:** safety, medical or security goes to the printed emergency plan. That plan belongs to event-risk-management, and I did not write or change it.

### Rotation and handoff

- It's a one-day event, so split it into 2–3 blocks and put a named on-duty person on each.
- Use a **written handoff checklist** at each boundary, plus a **live channel check** before the outgoing person leaves.
- Every handoff needs an entry or an explicit "none" in each of six sections:
  1. Open problems
  2. Sessions off-plan
  3. People
  4. Venue and tech
  5. Decisions already taken
  6. Next block
- "None" separates "nothing to report" from "nobody checked".
- If a handoff lands mid-incident, hold the boundary until it closes. Otherwise use the denser incident template.
- Move up to an overlap window if a changeover can land during a live problem.

### Live disruption sequence

1. **Name it at the room.** The room lead calls what happened and starts the clock.
2. **Route it.** The post resolves what it can. Everything above its authority goes to the on-duty organizer on the org channel. Safety goes straight to the emergency plan.
3. **Decide against your published disruption order.** Do not decide against the room.
4. **Lock the revised grid** for the rest of the block.
5. **Say it out loud** in the room and on the channel.
6. **Write the wrong row down** on the text channel while it is still happening.

### Closeout

- Hand the venue back against the contract.
- Release staff explicitly, not by attrition.
- Capture what the document got wrong the same day.

### Checks before doors open

- ✅ Every staffed post can name the on-duty organizer for their block without asking anyone.
- ✅ Every segment has a named owner, and every shift boundary has a handoff record with an entry or "none" in each section.

I'd also track two metrics, both self-set and not benchmarks:

- **Transition dead air:** seconds at scripted versus unscripted transitions.
- **Escalations that reached the on-duty person:** zero usually means nobody could be reached, not that nothing happened.

## 4. What I still need

**I couldn't write the final cue sheet.** The skill says to get the grid and the disruption priority order before writing anything, and I don't have them. Here are the questions, in priority order:

1. **What is the published grid?** I need the times, and in particular when the two talks and the MC's blocks fall.
2. **Do you have a disruption priority order?** If not, I can draft one from the skill's default: protect the keynote or plenary, then the headline commitment, then minimize other sessions disturbed, then lock the grid. It's a program decision, so the five of you must confirm it. It should not be improvised at 14:00.
3. **Who is staffing the door, registration and tech?** Are these just the five, or other volunteers? For 200 people it matters.
4. **Is there a printed emergency plan, and who is named on it?** If not, that is event-risk-management's work and it blocks the incident path.
5. **What is your last-change deadline?** When do you print the sheet and brief people?
6. **Is this a one-off, a first edition, or recurring?** If recurring, I'd add a reusable template and a recorded handoff format.
7. **Is the opening recorded or livestreamed?** Does a sponsor have fixed wording?
8. **Does the venue have mobile coverage everywhere you'll be?** Does it run its own comms?

Once you send the grid, I'll present the sections one at a time (roles, cue sheet, comms and escalation, rotation) for your sign-off before anyone prints or briefs. After printing, every change costs a person holding the old version.