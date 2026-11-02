# GoNorth production plan: record all 14 talks, no live stream

**Status:** this is a draft for your review, not an order list. The skill asks for a section-by-section review before anything is bought, because changes after ordering cost money. I made the assumptions below instead of interviewing you, so please correct them first.

## Assumptions to confirm (correct any that are wrong)

1. **Capture posture: recorded for later, no live stream.** I'm treating "no live stream" as final. That means no uplink, no encoder, and no rehearsal-for-streaming.
2. **Recurring event.** Calling this a "first edition" suggests there will be more. I weighted the plan toward a written brief, a trained crew and reusable gear.
3. **Speaker consent for recording and YouTube publication.** I assume a per-talk consent record exists or will exist. I'm not re-collecting it, and nothing gets published that it doesn't cover.
4. **Captioning and hearing loop.** This is an accessibility decision, not mine. I carry it as a separate budget line below.
5. **Venue unknowns.** I don't know the last date the venue can add anything, the changeover time between talks, or whether you can get into the rooms the day before. Each affects the plan, and the venue questions in section 4 cover them.

## 1. Capture posture and coverage tier

**Posture:** recorded for later, in both rooms.

| Room | Tier | Why |
|---|---|---|
| **A** (180 seats, PA and desk) | Fixed camera on the board feed. The camera operator may reframe between talks only. | You get clean audio from the desk, and the plan needs almost no work on the day once set. |
| **B** (80 seats, no PA) | Fixed camera plus a lavalier microphone into a standalone recorder. | There is no board, so the microphone and recorder are the board. |

- **Camera count:** two camcorders and two rooms means one camera per room. There is no vision mixing and no second angle, and you don't need either.
- **Slides:** this is a developer conference, so slides carry the talk. A wide shot of a screen is unreadable on YouTube. Both rooms therefore also record the slide feed as a separate file, and you combine it with the camera in the edit. This is the one step up from the default tier, and it is cheap.
- **What I'd skip:** a smartphone as the plan for either room, and any streaming. A phone at the back captures room audio, and a talk nobody can hear isn't an archive. Keep a phone only as an emergency fallback.
- **No house technician as the plan.** If the venue has one, keep them, but the recording still needs an owner on your side.

## 2. Signal path and redundancy

### Room A

```
Speaker mic ─► Desk ─┬─► PA (room hears it)
                     └─► Line out ─► Standalone recorder ─► SD (main audio)
Speaker laptop ─► HDMI splitter ─┬─► Projector (room sees it)
                                 └─► USB capture ─► Recording laptop (OBS) ─► slides file
                                                    (its screen is the crew monitor)
Camcorder ─► SD (video, plus its own mic as a sync and fallback track)
```

### Room B

```
Speaker lavalier (wireless) ─► Receiver ─► Standalone recorder ─► SD (main audio)
                                            (built-in stereo mics add room sound for audience questions)
Speaker laptop ─► HDMI splitter ─┬─► TV
                                 └─► USB capture ─► Recording laptop ─► slides file
Camcorder ─► SD (video, plus its own mic as a sync and fallback track)
```

**Audio:** the archive audio comes from the desk in Room A and the lavalier in Room B. It never comes from the camcorder's microphone, which is only there to line up the files in the edit.

**Redundancy:** each item protects against a named failure.

| Failure | Protection | Owner |
|---|---|---|
| The microphone or its cable dies mid-talk. | A second microphone within reach on a different channel, spare batteries and a spare cable per run. Room B keeps the second wireless kit ready. | Room audio person |
| The recording was silently black or silent for 40 minutes. | The crew monitor: the slide laptop screen, the camcorder's flip screen and headphones on the recorder. Someone checks all three at the start of every talk. | Production owner |
| The main audio file turns out to be unusable. | The camcorder's own audio as a fallback. It's poor, but it's a listenable talk. | Camera operator |
| Files exist but can't be found, or can't be lined up. | Naming and clock convention (below), plus one test playback before doors open. | Production owner |
| A bulk copy at 18:00 fails or hogs the network. | Copy files off between sessions, over USB, not the network. | Production owner |
| A one-off talk, such as the keynote, can't be repeated. | For any such talk, run an extra recorder (use the spare) as a fully independent second audio recording. | Production owner |

**Naming and clocks:**
- Name every file `gonorth-<room>-<YYYYMMDD>-<HHMM>-<talk-slug>`.
- Set the clock on every camcorder, recorder and laptop from one phone each morning.
- Never leave unlabelled SD cards. Label each card with room, device and a number.

**Camcorder risks (secondhand kit):**
- Check the maximum clip length, the automatic file-split size, and what battery life they really give.
- Buy spare batteries and a mains adapter for each.
- Confirm the SD card type each takes before buying cards.

## 3. Crew and training

**Six volunteers, no AV experience, so the full introduction training applies.** The shorter refresher is for returning crews, which you don't have yet.

| # | Name | Role |
|---|---|---|
| 1 | ____ | **Production owner**, floating between both rooms. Owns the signal path, the monitor checks, the file collection and the consent check. Not an MC, a speaker or registration. |
| 2 | ____ | **Room A audio.** Runs the desk, the recorder and the spare mic. |
| 3 | ____ | **Room A camera and slides.** Frames the shot and runs the slide capture. |
| 4 | ____ | **Room B operator.** Fixed camera, recorder, lavalier and slide capture. |
| 5 | ____ | **Room B room lead**, doing stage management. Handles speaker handover, the lavalier fitting, the timekeeping and the repeat-the-question rule. |
| 6 | ____ | **Floater and file runner.** Moves cards, labels, copies and backups, and covers breaks. |

**Check:** is volunteer 6 available all day? If production owns *only* production, you need all six. If you also need them on registration, the fixed-camera design still works, but the floater role is the first to go.

**Training plan (about 3 hours total, then the rehearsal):**
1. Basics session (1 hour): the signal path diagram, the six roles and the naming convention.
2. Hands-on session (1.5 hours) on borrowed or owned kit: levelling the tripod, framing, the recorder and headphones, OBS slide capture.
3. Walkthrough in the real rooms (section 8).

## 4. Venue technical spec, as questions for venue sourcing to put in writing

Don't state requirements. Ask, and get the answers in writing.

**Rooms and equipment**
1. In Room A: what is the desk model, and does it have a free line, record or aux output? What microphones exist (lectern, handheld, headset)? What are the projector's inputs (HDMI, VGA)?
2. In Room B: what is the TV's size and its inputs? Can the venue provide a projector instead, since an 80-seat room may not read a TV from the back?
3. Does either room already have lecture-capture equipment or installed cameras, and can we use it?
4. Are we permitted to use our own equipment, or must we use a nominated supplier?
5. Are there recording restrictions or fees?

**People and access**
6. Is a house technician included, for which hours, and what are they responsible for?
7. Can we get into both rooms the day before, or at what time on the day?
8. What is the latest date the venue can still add anything?

**Physical**
9. Can the camera stand at the back, off any fire route, and may we tape cables across walkways?
10. Where are the power sockets at the back of each room and at the speaker position?
11. How noisy is Room B (corridors, ventilation, outside), and can we close doors during sessions?
12. Is there lockable storage overnight?

**Not asked:** bandwidth and uplink, since nothing is streamed. Ask for them only if you add a stream later.

## 5. Supplier brief

You have no supplier and the plan is volunteer-run, so no brief is needed now. If you add a hired technician for Room A, the brief states the capture posture per room, board-sourced audio, the file delivery moment and these acceptance criteria:
- Every scheduled talk has a playable file with audible board-sourced audio.
- The files follow the naming convention.
- The files are handed over before the crew leaves.

## 6. What to buy, and the Media budget line

**Prices are my rough GBP estimates and need checking.** I haven't priced these.

| Item | Qty | Est. cost | Note |
|---|---|---|---|
| Handheld recorders (Zoom or Tascam class) | 2 | £150–£300 | One per room. |
| Wireless lavalier kits | 2 | £150–£400 | Room B primary and spare, and a fallback for Room A. |
| HDMI splitters (1-in, 2-out) | 2 | £30–£50 | Check the splitter passes the speaker resolutions you need. |
| HDMI-to-USB capture devices | 2 | £30–£60 | |
| Adapters (USB-C, mini DisplayPort, VGA) and spare HDMI cables | kit | £40–£80 | For the speaker collection to surface odd connectors. |
| SD cards (for cameras, recorders) and spares | about 8 | £60–£100 | Check card types first. |
| Camcorder spare batteries and mains adapters | 2 sets | £60–£120 | |
| Headphones | 2 | £30–£60 | |
| Audio cables from the desk to the recorder, plus spares | set | £20–£40 | Exact cable depends on the desk output. |
| External SSDs for backup | 2 | £100–£160 | One master, one copy. Store them separately. |
| Gaffer tape, cable covers, extension leads, label tape | set | £50–£100 | |
| Recording laptops | 2 | £0 | Borrow. Confirm they run OBS and have USB ports. |

**Estimated total: about £700–£1,400.** Lean option: buy one wireless kit and one SSD, and use the recorders' built-in microphones as the Room B spare. That saves roughly £200–£400.

**Hold back:**
- A PA for Room B. At 80 seats on a flat floor, a speaker can usually be heard unamplified. Decide after the room walkthrough and the accessibility decision.
- A hearing loop or captioning. These are accessibility's decision (section 1, assumption 4). Keep a separate line for them.

**Media line, split three ways for the budget:**

| Part | What goes in it |
|---|---|
| **Recording** | Everything in the table above. It survives any cut. |
| **Captioning** | Placeholder until accessibility decides. YouTube's automatic captions are a free baseline, if accessibility accepts that standard. |
| **Live streaming** | £0. Not in scope. |

## 7. Speaker-driven checks

Take these from the speaker collection, not from me:
- **Live demos:** a demo needing a network drop is a risk for a recorded talk as well. Ask the venue about wired access, and have speakers record a fallback video.
- **Audio playback:** any speaker playing sound needs a feed into the mix.
- **Background music in demos:** warn speakers before the day, since YouTube can block or mute a video that carries it.
- **Stay in frame:** mark the camera's area on the floor with tape, and tell speakers to stay in it.

## 8. Rehearsal plan

There's no stream, but the signal path still gets tested end to end before the audience arrives. Run it in the real rooms, with the real kit, ideally the day before (venue question 7), otherwise at load-in.

1. Walk the signal end to end in both rooms: microphone to desk or lavalier, to recorder, to speakers, and the slide path to the capture laptop.
2. Record 60 seconds and **play it back in full**. A moving level meter is not proof.
3. Check every clock against one phone, and check the file names come out as intended.
4. Break something on purpose. Unplug the primary microphone and time the swap to the backup, using the person who will do it on the day.
5. Run one real changeover at the speed the grid allows: a laptop swap, a mic handover, and a recorder restart.
6. Confirm out loud who is at which position for the first block.

## 9. Post-event pipeline

| Step | When | Owner |
|---|---|---|
| Check every file exists and plays, before the crew leaves | End of day | Production owner |
| Copy to two SSDs, stored separately | That night | Floater |
| Line up camera, board audio and slides, and trim each talk | Within days | Named editor (name ___) |
| Check each talk against the consent record. Anything not covered stays unpublished. | Before upload | Production owner |
| Upload to YouTube and send each speaker their own link | Target ___ | Named editor |

**Edit estimate (my guess):** 30–60 minutes per talk for novices, so about 7–14 hours for 14 talks. The decision that stops this pipeline stalling is naming the editor and the publish date **now**, not after the event. Please give me both.

## 10. Measures (self-set, not benchmarks)

- **Capture completeness:** talks with a usable recording over 14. "Recorded but unusable" counts as a failure.
- **Failures caught by a backup vs failures that reached the audience.**
- **Days from event to published video**, and where it stalled.

## Your next steps

1. ✅ Confirm or correct the five assumptions at the top.
2. Send section 4 to whoever handles venue sourcing, and ask for written answers.
3. Fill in the names in section 3 and the editor and date in section 9.
4. Check the camcorders (card type, clip limit, battery) before buying any cards or batteries.

Once the venue answers come back (especially the desk outputs and the Room B display), I can turn the shopping list into exact products and cables.