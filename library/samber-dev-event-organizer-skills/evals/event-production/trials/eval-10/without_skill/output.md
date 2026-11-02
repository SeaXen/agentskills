# 45-minute AV test plan for the keynote stream

**Premise:** 45 minutes is enough to *verify* a system, not to debug one. Anything not already proven the day before (network, encoder, stream key) is at risk.

## Gaps to close before the morning

- **Encoder:** your list has a vision mixer but no streaming encoder. If the mixer has a built-in one (ATEM Mini Pro, for example), fine. Otherwise you need a hardware encoder or a laptop running OBS or vMix. Say which, and name who owns it.
- **Audio to the stream:** the stream needs its own feed from the house desk, such as an aux or matrix send. A remote viewer should never get the room mix.
- **Wired drop:** ask the venue for the following.
  - A dedicated or non-shared line.
  - No captive portal.
  - Outbound ports open for your platform (RTMP 1935, or SRT).
  - Its upload speed. Aim for sustained upload of at least 2x your stream bitrate. A 1080p stream runs about 6 Mbps, so you want 12 Mbps or more.
- **Backup path:** a bonded cellular unit, or at least a phone hotspot, plus a second encoder output if you can.

## Roles (assign before the clock starts)

| Role | Owns |
|---|---|
| **Network/stream lead** | Wired drop, encoder, platform, off-site check |
| **Audio lead** | RF, house desk, stream feed |
| **Video lead** | Cameras, vision mixer, slides |
| **Producer** | Clock, checklist, run of show, sign-off |

Network and audio run in parallel from minute 0. Don't run the checklist one person at a time.

## Timeline

### 0:00–0:05, Power-up and baseline
1. Power everything on and confirm all signal paths are connected.
2. Network lead plugs into the wired drop **now**.
3. Producer confirms the speaker, or a stand-in, is available at 0:32.

### 0:05–0:12, Network and encoder (starts the soak test)
1. Run a speed test on the wired drop, upload especially. Compare it to the venue's promise.
2. Confirm the ports and platform are reachable.
3. Start a **private or unlisted test stream** and leave it running until 0:40. This soak test catches drops and throttling that a 30-second test won't.
4. Check that the encoder holds the target bitrate with no dropped frames.
5. Watch the test stream on a **phone on cellular, not on venue Wi-Fi**. That proves what viewers see.

### 0:05–0:22, Audio (in parallel with the above)
1. **RF:** scan for clean frequencies and set the handheld and headset on them. Walk the whole stage and the room with both. Look for dropouts near the stage edges, and check what your 400 attendees' phones and the venue's own wireless might add. Fit fresh batteries in both.
2. **Pick the primary mic.** The headset is usually primary for a walking speaker. Keep the handheld hot as the backup, and confirm the speaker knows how to swap.
3. **PA:** ring out the speaker mic and set gain before feedback. A full room absorbs sound, so leave headroom.
4. **Stream feed:** send the speaker mic, plus any playback audio, to the encoder and check the level (peaks around -12 dBFS, no clipping). Listen to the *stream's* audio on headphones, separate from the room.
5. **Lip-sync:** the stream needs an audio delay that matches video latency. Clap on camera and check the stream output.
6. **Playback audio:** test any video with sound. Confirm it reaches both the PA and the stream.

### 0:15–0:30, Video
1. **Cameras:**
   - Set white balance and exposure under the *show* lighting, not work lights.
   - Check focus, framing, and zoom range on the speaker's real positions.
   - Check tally and intercom between operators.
2. **Mixer:**
   - Run every input and every transition.
   - Confirm the output resolution and frame rate (1080p, 25/30/50/60) match the encoder, with no scaling surprises.
3. **Slides:**
   - Plug in the presenter's own laptop (or its backup) via the real cable and adapter.
   - Check the resolution on the main screen and in the stream.
   - Confirm slide advance and notes work.
4. **Graphics:** check lower thirds, title cards, and the starting and ending slates.
5. **Recording:** confirm a local program recording is running as a backup.

### 0:30–0:40, Walk-through with the speaker (or a stand-in)
Run it as a **cue-to-cue**, not a full talk.
1. The speaker walks on, picks up the mic, gives 30 seconds of speech, and advances slides.
2. Play a video clip if the talk has one.
3. Cut between cameras, as in the show.
4. Producer calls the cues out loud.
5. Check the stream monitor: the speaker should sound and look right there, not only in the room.
6. If the speaker isn't there, a stand-in speaking at normal volume is the only way to test gain.

### 0:40–0:45, Final checks and reset
1. **Failure drill (60 seconds):**
   - Pull the wired drop and confirm the backup takes over.
   - Everyone says who calls it and how.
2. **Stream readiness:**
   - Stop the test stream.
   - Confirm the real stream key and event page are armed, and that the stream is not live yet.
   - Confirm the doors-open and go-live times.
3. **Reset:**
   - Return faders and mutes to the show state.
   - Re-slate the cameras.
   - Put fresh batteries in if any are below 50%.
4. **Producer signs off** by confirming each lead's checklist verbally.

## Hard rules for the 45 minutes

- **Don't fix anything big:** if a fix will take more than 5 minutes, switch to the backup and note it.
- **Don't change settings after sign-off:** that's how a working system breaks at 9:55.
- **Test with the real gear and cables:** adapters and laptops count.
- **Write down the failures** you find, even the ones you fixed.

## If you only have time for five things

1. Soak-tested stream, viewed off-site.
2. Stream audio feed, checked on headphones.
3. RF walk of the stage and room.
4. Slides from the speaker's actual laptop.
5. Failover drill.

If you tell me the encoder, the streaming platform, and the mixer model, I can turn this into a per-role checklist with the exact settings to check.