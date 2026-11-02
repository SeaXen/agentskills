# Where to put the 4k: the production plan for edition 7

**Spend most of it on detecting and surviving silent failures. Don't buy more cameras.** You already own what a 3-room event needs. The lost afternoon came from nobody being able to see a recorder fill up, and capacity was a smaller part of that. The four-month turnaround is a pipeline problem, and money fixes only part of it.

Prices below are my rough estimates, not quotes. Replace them before ordering.

## 1. Capture posture and coverage tier

- **Assumed posture:** every room recorded for later, main room also streamed live. Please confirm the stream is a promise to someone (sponsor, remote audience) and not a hope. If it is only a hope, drop it. It is the first line a lean budget cuts, and it takes rehearsal and an operator with it.
- **Main room:** two cameras, vision mixing, live stream on top. You meet the preconditions: the crew is experienced and this is a recurring event.
- **Rooms 2 and 3:** one fixed camera each, with audio taken from the mixing board and not from the camera microphone. That gives you exactly your 4 cameras.
- A second operated camera in a breakout room is worth it only if slides carry the talk. Decide per session type.
- **Check:** a vision mixer or switcher for the main room. If you don't own one, that is your one probable equipment purchase, so tell me.

## 2. Signal path and redundancy

Redundancy is aimed at the failure you actually had, plus the ones next to it.

| Named failure | Protection | Owner |
|---|---|---|
| Recorder fills silently | Production-desk monitor on each room's recording output. Capacity and record light checked at the start of every session. Media sized so no device can fill within a day. | Per-room operator |
| Recording nominally exists but is unusable | Recorders in the SKILL's labelled-and-clock-synced pattern. One 60-second test played back in full each morning. | Production owner |
| Mix or encode chain fails | Independent audio recorder per room, fed from the board but outside the live mix | Production owner |
| Mic or cable dies mid-session | Second mic at the lectern, spare batteries, and a spare cable and adapter per room | Room audio operator |
| Files stranded after the event | Copy between sessions in chunks, never in one pass at 18:00 and never over the venue's attendee network | Production owner |

- Your multi-room setup, recurring edition, committed archive and past loss all meet the conditions for continuous chunked sync. Build the cheap version: a laptop or NAS at the production desk and a copy at each changeover.
- Don't buy a duplicate encode path.
- You have 2 recorders for 3 rooms, so one room likely has no recorder of its own. Do the recorders record video or audio? Tell me which, because the answer decides whether the third device is a recorder or a standalone audio recorder.

## 3. Crew and training

- **Training:** brief refresher only, since all 8 have done at least 4 editions. Hands-on only for any role someone has never held, such as vision mixing.
- **Main room (5):**
  - audio operator
  - two camera operators
  - vision mixer
  - a stream operator whose only job is the stream
- **Rooms 2 and 3 (1 each):** one person per room owns the fixed camera, the board audio and the monitor.
- **Floating (1):** an AV-technical lead who also owns the brief.
- That is 8 of 8 with no relief on a two-day event. Check this against breaks and meals. If the crew can't rotate, a ninth person or a paid stagehand is a better use of money than any gadget.
- Name the people for each position before the order goes in.

## 4. Venue specification (as questions for venue sourcing)

You bring your own equipment, so there is no supplier brief this year. The venue still has to answer in writing:

- What upstream bandwidth is guaranteed to the main room? Is there a wired port at the production position, and a second independent path?
- Where is the board audio output in each room, and in what form?
- Can you run cables and place cameras without blocking fire routes? Is there space for a production desk?
- Are there restrictions on recording or streaming here?
- What power is on offer, and is a house technician included? Keep the technician, but add your own owner.

Do not write down a bandwidth figure yourself.

## 5. Budget (4k)

| Line | Estimate | Why |
|---|---|---|
| Crew monitors and capture/splitters, 3 rooms | ~500 | Catches the next silent failure |
| Storage and media sized for a full day per room, plus the chunked-sync laptop or NAS | ~700 | Stops recorders filling and makes the cleanup copy fast |
| Independent audio recorders, 3 rooms | ~600 | Covers the room with no recorder and gives every room a second path |
| Spares: mic, batteries, cables, adapters, per room | ~400 | The only rung that saves a session live |
| Stream reserve (backup uplink, bonded cellular) | ~800, released only after the venue answers in writing | Don't buy an uplink fix for a problem the venue may already solve |
| Post-event editing reserve | ~800, released only after diagnosing the stall | See the pipeline below |
| Buffer | ~200 | |

Split the Media line into recording, captioning and streaming. Captioning is not in this plan. If accessibility decides captioning is needed, it will compete for this 4k and may force the stream reserve to go.

**Pipeline, four months to publish:**

1. Find where the last edition stalled: collection, editing, consent check, or publishing. This decides whether the editing reserve is spent at all.
2. Name one pipeline owner and a publish date before the event.
3. Verify every file plays before the crew leaves the building.
4. Check each session against the consent record before publishing. Anything not covered stays unpublished.
5. Publish the main room first, in light-edit form. Add title cards and trim, nothing more.
6. If editing hours were the bottleneck, spend the reserve on a freelance editor for rooms 2 and 3. If the bottleneck was ownership or consent checks, spend nothing.

## 6. Rehearsal (required because the main room is live)

1. Walk the signal end to end: mic to mixer to the room, the encoder and the crew monitor.
2. Record 60 seconds and play it back in full.
3. Check every device's clock against one reference and confirm the file naming.
4. **Break something on purpose.** Pull the primary mic and time the swap. Then fill a recorder in a test and confirm the monitor shows it.
5. Run a real changeover at the grid's actual speed.
6. Go live to a private destination and watch it on a device outside the venue network.
7. Name the position holders for the first block, out loud.

## Metrics to set (self-set, not benchmarks)

- **Capture completeness:** sessions with a usable recording over sessions scheduled. Target 100%. "Recorded but unusable" counts as a failure.
- **Failures caught by a redundancy** versus failures that reached the audience.
- **Event end to published video, and where it stalled.** Pick your own number to beat four months.

## Questions I need answered

1. Is the stream a promise to someone? To whom?
2. What do your 2 recorders record (video or audio)? Which room has none?
3. Do you own a vision mixer or switcher?
4. Where did last edition's four months go: collection, editing, consent, or publishing?
5. Has accessibility decided on captioning or a hearing loop?
6. When is the last date the venue can still add something? What is the event date?
7. Does the consent record cover recording and streaming for every session format?