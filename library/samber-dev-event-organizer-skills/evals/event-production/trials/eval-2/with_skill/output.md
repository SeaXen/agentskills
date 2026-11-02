# Can we say yes to the sponsor's keynote livestream?

**Answer: yes, but only conditionally. Don't sign "we will livestream" on the current plan.**

"Laptop pointed at the camcorder's HDMI" is the sourced failure mode *streaming with no rehearsal and no dedicated operator*. The skill says to delete that option rather than treat it as a cheap rung. It isn't free, and it has three technical gaps:

- **No capture path.** Laptop HDMI ports are outputs, so a camcorder cable alone won't work. You need a capture device and an encoder.
- **Bad audio.** A camcorder at the back of the room records room audio. The skill requires audio taken from the mixing board.
- **Unmeasured uplink.** Nobody has asked the venue for a guaranteed upstream connection.

**Next action today:** send the venue the Part 1 questions below, and tell the sponsor "yes, conditional on a go/no-go on 2026-10-19."

## 1. Capture posture and tier

- **Posture:** keynote room only, streamed live, with recording as the floor. Every other session stays recorded-for-later.
- **Current plan:** this is the smartphone-floor rung (camcorder mic to SD card). It is the minimum and not enough for a sponsor commitment.
- **Needed:** a fixed or operated camera on the board audio feed, with a stream layer on top. The skill's sponsor-commitment condition is what promotes streaming.
- **Judgment call (mine, not the skill's):** the sourced top rung is a stream on two cameras with a vision mixer. In 19 days, with all volunteers, I'd ship one camera and make the second camera and mixer a stretch goal.
- **Slides:** a wide shot can't read slides. If the keynote is slide-heavy, ask whether the venue can give you the projector feed.

## 2. Signal path and redundancy

**Signal path:** use the three-destination split off the board.

1. Room projector and PA, with minimal delay.
2. Encoder: camera video plus board audio into a capture device, then the laptop, then the platform.
3. A crew monitor on the encoder output. Someone looks at it at the start of the session, so you never discover a black stream 40 minutes in.

**Redundancy:** the keynote can't be repeated, so move up one rung from "spare mic and cable".

- **Spare gear:** a second mic live at the lectern on a separate channel, spare batteries, and a spare cable and adapter per connector.
- **Independent audio recorder:** a recorder outside the live mix, taking the same board feed. This protects the archive if the encoder dies.
- **Camcorder SD card:** keep it recording as a local backup.
- **Labelled files:** name the files (e.g. `keynote-YYYYMMDD-HHMM`) and set the clocks the same morning. Play back one test file before the event. An unopened backup doesn't count.

## 3. Crew and training

The skill says this needs more than one named production owner. Name people, and none of them may also be speaking, MCing, or running registration.

- **Stream operator:** their only job is the stream.
- **Audio operator.**
- **Camera operator.**
- **Production owner:** one of these, or a fourth person.

Training is the full introduction, because it is a first-time crew. Scope: the keynote block, plus the recording for the rest of the day.

## 4. Venue questions and supplier brief

**Ask the venue in writing.** Don't state a bandwidth number yourself.

- What upstream bandwidth is guaranteed to our room, and is a dedicated connection available?
- Is there a wired port at the production position?
- Is there a second, independent path to the internet?
- Who administers the network on the day, and are ports or destinations blocked by default?
- Where is the room's audio available as a feed, and in what form?
- Is there a production position and power at it?
- Is there a house technician, and what are they responsible for?
- Are there restrictions on streaming or recording, or on bringing our own gear?

**Supplier brief:** only needed if you hire or borrow gear. If you do, state the capture posture per room, require board-sourced audio, name the stream destination, and list acceptance criteria. Hand it to whoever handles supplier selection.

## 5. Budget, consent, and pipeline

**Budget:** it is not free. Give the Media line to the budget owner split three ways: recording, captioning, and streaming. Captioning stays pending until accessibility decides.

Streaming costs these things, none of which I've priced:

- A capture device.
- The audio recorder.
- A wired or cellular uplink fallback.
- Cables and spares.
- Rehearsal time.
- The operator's time.

**Consent:** you need the keynote speaker's written consent for a live stream, because a stream can't be edited afterwards. Warn them off background music in any demo, since that can get the stream taken down. Check sponsor-supplied content too.

**Post-event pipeline:** name the owner and the publication date now. Verify every file plays before the crew leaves, then edit, check against the consent record, publish, and send the speaker their link.

## Rehearsal and go/no-go gates

The event is 2026-11-02.

| Date | Gate | If it fails |
|---|---|---|
| **2026-10-19** | Venue confirms in writing a guaranteed upstream figure, a wired port, and a board feed. Speaker consent is in. Four people are named and gear is ordered. | Fall back to recording-only. |
| **2026-10-26** | Off-site dry run with the exact gear, streamed to a private destination and watched on a device outside the venue network. | Same fallback. |
| **Event eve or morning** | In-room rehearsal: walk the signal, record and play back 60 seconds, unplug the mic and time the swap, run a real changeover. | Same fallback. |

Ask the venue now whether you can have in-room rehearsal access.

## What to tell the sponsor

- **Offer:** "Keynote livestream on [platform], plus a recorded keynote video published within [N] days."
- **Don't offer:** an uptime guarantee or a penalty clause.
- **Why:** a live stream can fail even when well prepared. If the 2026-10-19 gate fails, you tell them early and deliver the recording.
- **Fallback is your choice:** if they will only sign for a guaranteed live stream, that is their call. Don't accept a guarantee you can't engineer.

## Metrics (self-set, not benchmarks)

- Keynote capture completeness: a usable file, counted as failed if unusable.
- Failures caught by a redundancy versus failures that reached the audience.
- Time from event end to published video.

## Open questions I couldn't ask

- Does the camcorder have a clean HDMI output (no on-screen overlay)? Does it have an audio input, and can it run for the whole keynote without auto power-off?
- Is there a mixing board at the venue, or is it only a PA?
- Does the sponsor contract name "livestream" explicitly, and on which platform?
- Has accessibility decided on captions or a hearing loop?
- Is this a recurring event? If so, the trained crew and written brief pay off next edition.