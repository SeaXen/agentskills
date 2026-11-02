# Will 25 Mbit/s hold for OpenKernel Days?

**Verdict:** 25 Mbit/s will not hold if the home line also serves viewers. It is tight if it only carries the ingest, and it is fine if the home line carries almost nothing.

## 1. The bandwidth math

I assumed typical OBS/x264 bitrates, so check them against your own settings.

| Per-room setting | Bitrate | 5 rooms | Share of 25 Mbit/s |
|---|---|---|---|
| 1080p30 | 4.5–6 Mbit/s | 22–30 Mbit/s | 90–120% ❌ |
| 720p30 | ~3 Mbit/s | ~15 Mbit/s | 60% ⚠️ |
| 1080p15 (slides/terminal) | ~2.5 Mbit/s | ~12.5 Mbit/s | 50% ✅ |

- **Plan on 70% of the advertised rate at most.** That is about 17 Mbit/s usable. Residential upstream sags in the evening, and protocol overhead adds 5–10%.
- **Add audio and overhead.** Audio is roughly 128–160 kbit/s per room.
- **Expect bufferbloat.** A saturated upstream makes every packet queue, including the coordinator's own admin session, chat moderation and calls. Enable SQM/QoS on the router or cap the OBS bitrates well below the line rate.
- **Devrooms are mostly slides and terminals.** Use 1080p at 15 fps instead of 720p30. Text stays legible and the bitrate stays low.

## 2. The bigger problem: who serves the viewers?

Your plan says "push all five feeds out" but does not say to what. Viewers have to pull the streams from somewhere.

- **If viewers connect to the home line, it dies almost immediately.** One viewer of one room at 3 Mbit/s uses 3 Mbit/s of upstream. Eight viewers saturate the line.
- **You need a fan-out point.** Options, best first:
  1. **A rented VPS or bare-metal box with good bandwidth.** OBS sends SRT or RTMP to it. MediaMTX or nginx-rtmp repackages the stream to HLS and serves it. The home line then carries only ingest. An hourly-billed server for a weekend should cost a few euros, but check the provider's traffic cap.
  2. **A self-hosted PeerTube or Owncast instance on that VPS.** The same fan-out applies, and you get a player, VOD and chat integration.
  3. **A restream to YouTube or Twitch as a mirror or fallback.** It costs nothing in egress and scales to any audience. It gives up the "fully self-hosted" goal, so decide that deliberately.
- **Estimate your egress.** One viewer-hour at 3 Mbit/s is about 1.35 GB. For example, 200 viewers averaging 4 hours across two days is about 2.2 TB. Check that against the provider's included traffic. Home upstream is irrelevant at that scale.
- **Where is OBS physically running?** If each room's host runs OBS from their own home, the coordinator's line is not involved at all, and the problem is much smaller. If all five run on or behind the coordinator's connection, everything above applies.

## 3. What else you're probably underestimating

**Encoding hardware**
- **Five simultaneous encodes on one machine is heavy.** Software x264 at 1080p needs several cores per stream. Hardware encoders (NVENC, QuickSync, VideoToolbox) are cheaper but have concurrent-session limits.
- **If speakers join by video call and you capture that into OBS,** the coordinator's downlink and CPU take that load as well.

**Failure handling**
- **The home line is a single point of failure.** One power cut or router reboot takes down all five rooms.
- **Prepare these ahead of time:**
  - a backup stream key or ingest;
  - a "we'll be right back" slate scene;
  - pre-recorded fallback talks;
  - a phone hotspot or second line for at least the main room.

**Rehearsal and monitoring**
- **Do a full dress rehearsal with all five rooms live at once.** Run it for at least an hour, at least a week before the event. Single-room tests tell you nothing about aggregate load.
- **Watch the right numbers during the event.** These are dropped frames, ingest bitrate per room, encoder CPU/GPU, and viewer counts per room.
- **Assign one person to watch the dashboard,** not just the rooms.

**Staffing**
- **Five rooms across two days is a lot for volunteers.** Plan for one host/producer per room per slot, plus a floater and a coordinator who is not also running a room.
- **Write a short runbook,** with an organizer backchannel and shift handovers.
- **Include breaks,** or volunteers will burn out by the afternoon of day one.

**Speakers**
- **Run a tech check for every speaker,** covering mic, screen share and fallback if their connection drops.
- **Ask them to join 10–15 minutes early** and collect their slides in advance as a backup.
- **Collect recording consent and a licence/release** before the event, not after.

**Chat**
- **The server load is probably fine. Moderation is the real cost.** Public online events attract spam and raids. Plan for:
  - a code of conduct;
  - named moderators per room;
  - rate limits and account requirements;
  - a quick way to lock a channel.
- **Handle stream latency in Q&A.** HLS runs 10–30 seconds behind real time, so questions asked in chat will lag the speaker. Tell hosts to wait before closing Q&A, or use low-latency HLS or WebRTC if you can support it.

**The hand-maintained schedule page**
- **A hand-edited static page for 5 rooms × 2 days will drift** the moment a talk moves.
- **Keep one source file (YAML or JSON) and generate the HTML and an .ics file with a small script.** The page stays static.
- **Show times in UTC plus a client-side local-time conversion.** An online event with the wrong timezone display loses attendees.
- **Put the per-room stream link on the page,** and decide who is allowed to edit it during the event.

**Recordings**
- **Record locally in OBS** at a higher bitrate as the master copy, and decide where the files go afterwards.
- **Plan for captions or at least transcripts** if accessibility is a goal.

**Security and privacy**
- **Treat stream keys as secrets.** Do not leave them in shared OBS profiles or screenshots.
- **Chat logs and server logs hold personal data.** Decide the retention period before the event.

## 4. Recommended setup

1. **Rent one VPS for the event.** Run MediaMTX or PeerTube there for ingest and HLS fan-out.
2. **Cap each room at 1080p15, about 2.5 Mbit/s.** Total ingest is about 12.5 Mbit/s, or 50% of the home line.
3. **Run SQM/QoS on the home router** so admin and chat traffic still gets through.
4. **Consider a YouTube/Twitch mirror** as the fallback for the main room, or for everything.
5. **Rehearse with all five rooms live** before the event.

## 5. Questions for you

1. **Where does each OBS instance run?** Is it at the coordinator's home or at each room host's home, and are speakers remote?
2. **How many concurrent viewers do you expect?**
3. **How strict is the self-hosting rule for video delivery?** Is a VPS acceptable, or a YouTube/Twitch mirror?
4. **Is the 25 Mbit/s figure measured?** Run `iperf3` to the intended VPS for 30 minutes, not a speed-test site.