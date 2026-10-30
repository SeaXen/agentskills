# Crew roles, training depth, and rehearsal

Six distinct AV crew roles are documented in C3VOC's angel-introduction repository, each with its own training chapter. The two-tier training ladder (full introduction for new crews, brief refresher for experienced crews) comes from the same repository.

## The six named roles

Each of these is a separate training chapter in the source, not a facet of one undifferentiated "AV volunteer."

| Role                  | What the split tells you                                                                                                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stage manager         | A distinct role from every AV-technical one. The person managing the stage is not the person managing the signal.                                                                            |
| Audio                 | Audio has its own dedicated role. It is the layer that decides whether the archive is usable at all.                                                                                         |
| Camera operator       | The person pointing and framing a camera.                                                                                                                                                    |
| Video / vision mixing | The person switching between camera feeds - **a different named role from the camera operator.** This is the split most organizers collapse, and the source is explicit that it is two jobs. |
| AV-technical lead     | A technical lead sitting above the individual operator roles. This is the role the skill's default staffing rung maps to.                                                                    |
| General crew          | Crew coordination, distinct from operating any one position.                                                                                                                                 |

**How to use the table.** It is a menu of jobs, not a required roster.

A one-room event with a fixed camera needs the technical lead and, if the room has live sound, the audio role: the other four do not exist yet. A two-camera room needs the camera and vision-mixing roles as separate people, because that is precisely the pair the source separates.

Add roles as the coverage tier climbs. Never assign a role with no work attached to it: an unoccupied named role is how a real gap gets hidden behind a full-looking roster.

## What each role actually does

Each role in the table above backs onto a training chapter with concrete operating detail, not just a job title.

**Stage manager** (`chapters/angel-stagemanager.tex`) owns lecture-hall operations end to end: coordination across every other team in the room (AV crew, heralds, translation), crowd management, timekeeping, and handling whatever unexpected problem comes up. The stage manager carries communication equipment for emergencies and works the same shift schedule as the AV technicians, because the two roles have to be in the room together.

**Camera operator** frames three shot types, each with its own rule (`chapters/shots.tex`):

- **Closeup** - head and upper body, eyes near the upper third line, space left above the head. A closeup that crops half the head, or leaves too little space above it, is flagged as a failure example in the source.
- **Medium** - one person with the lectern and some context, or two people together when both are on stage.
- **Overview/wide** - the complete stage, locked off and not moved during the shot. It is not used to show slides (lecture mode does that instead), and a dark-enough audience in frame is acceptable.

Before a shift, the operator levels the tripod against its water bubble and balances the tilt axis so the camera does not drift on its own (`chapters/camera-tripod.tex`), turns recording on, confirms the record indicator and remaining time, and keeps two SD cards loaded per camera as backup - recording must keep running through the break. On the lens, the operator works three manual rings, focus, zoom and iris, and controls zoom speed by how hard the button is pressed: a gentle touch gives a slow zoom (`chapters/camera-sony.tex`, `chapters/camera-panasonic.tex`, `chapters/camera-jvc.tex`). Anything wrong or misplaced gets reported to the AV technician rather than fixed solo.

**Video / vision-mixing** switches between camera feeds and slide sources and composes multi-source pictures, a separate job from operating a camera (`chapters/angel-av-video.tex`). The mixed feed is what goes out live and what gets recorded; there is no separate record signal. On a difficult talk, a director can assist. The role's own talk timeline runs in four phases, tracked separately for a one-camera and a two-camera room (`chapters/timeline-1cam.tex`, `chapters/timeline-2cam.tex`):

- **Preparation** - confirm the herald and the speaker, and signal ready to go live.
- **Introduction** - follow the herald, cut to the title slide, then move to lecture mode or a speaker closeup once the talk starts.
- **Content** - hold slides on screen long enough to be read twice, favor lecture mode when it is available, and anticipate what the speaker is about to do rather than reacting after the fact.
- **Q&A** - stay on whoever is speaking, including the herald relaying questions, and bring back the closing ("thanks") slide from time to time between answers.

**Audio** runs two separate mixer profiles for the stream/recording mix, sourced from two console-specific chapters that agree on the same core moves (`chapters/angel-av-audio.tex`, `chapters/audio-touchmix.tex`, `chapters/audio-allenheath-cq18t.tex`): mute unused microphones (bottom row), never mute a microphone during applause, adjust an individual channel with its fader or pull back the trim knob when it clips, and set hall loudness only on the fader labelled for the PA - the Allen & Heath chapter warns explicitly never to touch the fader labelled "NEIN" ("no"). Console navigation matters too: if the mute buttons read yellow, return to the Main Mix page before doing anything else; press the Phones button and use the rotary knob to set headphone level. Microphone choice has its own rule (`chapters/audio-headset.tex`): headsets for speakers, because the fixed mouth distance keeps level constant, handheld for heralds and Q&A. A correctly placed headset mic sits at the corner of the mouth, about 2 cm off the face, boom bent carefully - too far forward and it picks up wind noise.

**AV-technical lead** (`chapters/angel-voc-avtech.tex`) is the operators' direct, first-line support in the room: confirms the speaker's laptop is connected, owns the speaker's headset microphone, and is the first contact for any technical issue. The lead is also the communication gateway to the stage manager and to the external crew, working four-hour shifts.

**General crew** (`chapters/angel-voc-crew.tex`) is second-to-nth-line support above the AV-technical lead, reachable by phone or DECT, expected to know all the equipment in use and fix nearly anything the on-site lead cannot.

A separate **external crew** (`chapters/angel-external.tex`), typically the venue's own vendor rather than a C3VOC angel, runs house audio mixing and lighting fixtures; the guidance is to route requests through the AV technician rather than approach them directly.

Escalation and day-to-day coordination run over a dedicated intercom, not general chat (`chapters/communication-cch.tex`): a genuine emergency goes through the red VOC button on the room phone, then a call naming the lecture hall. The mixer position holds a party-line intercom to each camera, pressing the CAM button to talk and a red knob to set per-channel volume; each camera station talks back by holding a single button, with a red light on a channel meaning it is inactive.

## The two-tier training ladder

The source names two training concepts and picks between them by context, which is a genuine promotion condition rather than a preference.

**Full introduction** - a complete deck, used "for events without 'experienced' A/V angels." Run this when the host community has no standing AV volunteer base: a first edition, a new team, a venue nobody has worked in, or a crew recruited from general volunteers.

**Brief update plus hands-on training for newcomers** - a shorter deck plus dedicated per-topic self-training (basics, camera, video mixer, and talk timeline for one- and two-camera rooms), used at "usual" recurring events with an experienced returning pool. Run this when the crew has done it before and only the newcomers need depth.

**Why the ladder matters beyond training.** The second tier only exists because a crew came back. That makes crew training one of the clearest compounding investments a recurring event makes: the first edition pays full onboarding cost, and every later edition pays a fraction of it while getting a better result.

That is the same logic this collection applies to any asset that survives an edition, arrived at independently by an organizer community that has run the same event for years. It is also the concrete reason the interview asks whether the event is one-off or recurring before ranking the staffing menu.

## One camera or two

The same source maintains a separate "general talk timeline" for one camera and for two - confirming that camera count per session is a deliberate, named tier in that team's practice rather than an incidental resourcing outcome.

What the second camera buys is sourced concretely from the two-camera timeline: camera one holds a tight shot on the speaker for the whole talk, and camera two holds a wider, medium shot that resolves gestures and, before the talk starts, the full stage - only cutting live once the herald begins the introduction (`chapters/timeline-1cam.tex`, `chapters/timeline-2cam.tex`). What it costs is a second operator _and_ a vision mixer - two people, not one - plus the mixing position itself.

Choose one camera when the talk is the speaker and the slides are legible in a wide shot. Choose two when any of these hold:

- Slide detail is the content (code, diagrams, dense data).
- The room is wide enough that one position cannot cover both lectern and screen.
- The session is a panel or an interview, where a single fixed frame reads as a security camera.

## Rehearsal

Rehearsal is required for any livestream. The seven-step walkthrough below is built backwards from sourced failure modes and tests the signal path end to end before the audience is in the room.

Run it in the actual room, with the actual equipment, before the audience is in the building:

1. **Walk the signal end to end.** Microphone to mixing position to each of the three destinations. Confirm the room hears it, the encoder receives it, and the crew's monitor shows it.
2. **Record sixty seconds and play it back.** In full, listening. A level meter that moves is not evidence of a file that plays.
3. **Check the clock on every recording device** against one shared reference, and confirm the file naming convention produces the names you expect.
4. **Break something on purpose.** Unplug the primary microphone and time how long the swap to the backup takes, with the person who will actually do it. That number is the honest measure of the redundancy, and it is usually longer than anyone guessed.
5. **Run one real transition** at the changeover speed the grid actually allows - laptop swap, mic handover, camera reset - rather than at a relaxed pace.
6. **If streaming, go live to a private destination** and watch it on a device outside the venue network. A stream that works inside the building has proved nothing about the uplink.
7. **Confirm who is on which position for the first block**, by name, out loud.

Anything that fails here fails cheaply. The purpose of the rehearsal is not confidence; it is to convert unknown failures into known ones while there is still time to buy a cable.
