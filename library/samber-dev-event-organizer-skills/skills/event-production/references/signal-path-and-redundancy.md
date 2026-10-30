# Signal path and redundancy

Two published sources carry this file: FOSDEM's open-hardware capture design, and C3VOC's post-mortem of a recording setup that failed at scale.

## The three-destination split

Source: `fosdem/video-hardware`, `README.md`. FOSDEM's next-generation open-hardware recording box, built because the existing video boxes were "relatively bulky and expensive," aiming at "a cheap, compact and lightweight device" that could "enable a shared platform with other conferences and projects."

The design takes 720p60 HDMI audio and video as input - chosen as "the most widely supported resolution/refresh rate combination," a deliberate trade of quality against processing complexity - and splits it three ways:

1. **To the projector, with minimal delay.** What the room sees. Latency is a hard constraint here and nowhere else.
2. **To the H.264 encoder.** What becomes the recorded or streamed output, and eventually the archive.
3. **To a monitor for live playback.** What the crew watches to know the other two are working.

### Why this is a redundancy property and not just wiring

These are three destinations off one signal, not three copies of one pipeline. A failure in the encode path does not have to take down what the room sees, and a failure in either does not have to take down the crew's ability to see that it happened. The split buys separation of concerns before any duplicate hardware is bought - which is why it sits mid-ladder on effort and high on the room-continuity axis.

The third destination is the one organizers skip, and it is the one that catches silent failures. A recording that has been black since 10:40 costs nothing extra to discover at 10:41 and costs the entire session to discover in the edit.

### What to cite from it

It is a hardware-design document rather than a runbook. Cite the architecture pattern and the "shared platform across conferences" ambition - real evidence that conference AV needs are broadly generic - never a procedure, a vendor or a cost.

## What redundancy is actually protecting against

Source: `voc/aes67-recorder`, `README.md`. C3VOC runs AV production for the Chaos Communication Congress and publishes its infrastructure openly. This README documents why its backup audio recorder was rebuilt.

At 34C3, a hardware SSD recorder captured all 128 audio tracks from every sub-group mixer. It worked, in the sense that recordings existed. Five named failure modes:

- **Unlabelled tracks.** 128 tracks captured with no naming, so finding the one that mattered afterwards was hard.
- **No clock sync.** No NTP on the recorder, so its timestamps did not reliably line up with anything else.
- **A manual physical relay with a single point of failure.** "Someone had to unload the SSDs when they were full, carry them to an unloading-station, unload them and carry them back."
- **A network-load spike designed into the process.** Because drives filled in batches, "120GB+ had [to] be copied at-once every hours ... spiking the network load" - the backup process became a predictable operational risk of its own.
- **Files too large to work with.** "The backup files were hours-long of multi-GB .wav-files, so seeking in them (via network) was quite a challenge." The recording existed and was operationally useless.

The 35C3 redesign - the recorder this README documents - captures audio over AES67 directly into a media pipeline, writing "chunked, nicely named .wav-files, constantly syncing them to a storage-server" - continuous incremental sync replacing the batch physical relay entirely. The README states this as the plan for 35C3, so cite it as the designed answer to the five failure modes rather than as a measured outcome.

### The principle that carries over

**A backup system has its own failure modes, separate from the failure it exists to protect against.** A redundant recording path that is unlabelled, unsynced in time, dependent on one person's manual relay, or that produces files nobody can practically open is not meaningfully redundant, even though a recording nominally exists.

That is the whole argument for the labelling convention and the one test playback demanded in the skill's redundancy menu. It is also why "unusable" counts as a failure in the capture-completeness metric rather than as a partial success.

### Boundary

This is one team's specific tooling history at a very large event. Cite the failure-mode list and the principle.

Do not cite the specific software stack, the audio-over-IP transport, or the track count as a requirement for anyone else's setup. A two-room conference has no 128-track mixer and needs none of that machinery to hit the same principle with a labelled file and a synced clock.

## A redundancy plan, done twice

**Negative - a plan that reads complete and protects nothing:**

> Backup: we have a second camera and a spare mic in the AV cupboard, and we'll copy everything to the NAS at the end of each day.

Nothing here has an owner:

- The spare mic is in a cupboard rather than beside the lectern.
- The second camera duplicates the layer least likely to fail silently.
- The end-of-day bulk copy is exactly the network-spike pattern above.
- Nobody has opened a file.

Every element is a real technique; none of them is engineered.

**Positive - the same budget, arranged against named failures:**

> **Room A (plenary), recorded, not streamed.**
>
> - Live-session continuity: a second handheld microphone live on the lectern at all times, on a different channel; spare batteries with the room lead; a spare cable per run, labelled and taped down. Owner: room audio operator.
> - Archive continuity: a standalone audio recorder taking a feed from the mixing board but sitting outside the live mix, recording continuously through the whole block, files named `roomA-YYYYMMDD-HHMM`. Clock set against the same time source as the video recorder that morning. Owner: production owner.
> - Silent-failure detection: the encode output is mirrored to a monitor at the production desk. Somebody looks at it at the start of every session. Owner: production owner.
> - Test: one 60-second recording made at 08:30, played back in full before the first session. Not a level check - playback.
> - Collection: files copied off between sessions, not in one pass at 18:00.

The difference is not equipment. It is that each line names a failure, an owner and a moment at which it is verified.
