# PortQuay Conf remote plan (14 March 2027, £6,000 AV line)

**Next action this week:** email the venue and ask the 6 questions in section 1. Every number below depends on the answers.

All prices are my planning estimates for UK freelance and hire rates, not quotes. Get 2-3 quotes before committing.

## Decision: what "remote" means

- ✅ **One-way livestream of both tracks, plus recordings, plus a chat and Q&A bridge.**
- ❌ **Not building:** remote speakers on stage, remote "hallway" networking, 360° or VR, a custom platform, human live captioning.
- Why: £6k covers two rooms captured well. It does not cover an interactive remote product. Remote viewers of a Go/Rust talk mostly need clear slides and code, clean audio, and a way to ask questions.

## 1. Venue questions (this week)

1. Is in-house AV included, and what does it charge per room?
2. Can we get a **line-level audio feed** from the venue mixing desk in each room?
3. Is there a dedicated wired upload line, and what speed? I recommend at least 20 Mbps up per stream, so 40 Mbps or more for two tracks.
4. When is load-in, and can we do a tech rehearsal on 13 March?
5. Are there any restrictions on camera positions or rigging?
6. Is mobile signal good in both rooms? This matters for the backup uplink.

## 2. Budget (£6,000)

| Line | £ | What it buys |
|---|---|---|
| Camera, switcher and capture hire, 2 rooms | 1,400 | 1 speaker camera per room, HDMI slide capture, a switcher per room |
| Crew: 2 room operators at £500, 1 stream producer at £600 | 1,600 | One operator per track, one person running the output and chat bridge |
| Load-in and rehearsal day (13 March) | 500 | Crew half-day plus kit hold |
| Network: wired uplink plus bonded or cellular backup | 500 | Failover so a line drop doesn't kill the stream |
| Audio feeds, cables, comms, spares | 300 | Desk-to-capture cabling, intercom, spares |
| Streaming software and platform | 300 | Multistream tool or licence, one month |
| Remote Q&A tool and moderator thank-you | 300 | Q&A tool, volunteer moderator gifts |
| Post-production and publishing | 600 | Trim and cut talks from the recordings, thumbnails, upload |
| Contingency | 500 | Roughly 8%. Don't spend it early |
| **Total** | **6,000** | |

If the venue's in-house AV covers cameras and a feed, move the saved money to a second camera per room or to human captioning on one track.

## 3. Technical design (per track)

- **Slides and code:** capture the presenter laptop's HDMI output directly. Never film the screen. This matters most for a Go/Rust audience.
- **Camera:** one fixed or operated camera on the speaker, with picture-in-picture or a layout switch.
- **Audio:** take the mix from the venue desk, not from a camera microphone. Add one room microphone at low level for applause.
- **Output:** each room's switcher sends its own stream. Send to YouTube Live, one stream per track. Unlisted if remote tickets are gated, public if they're free.
- **Record locally in every room as well.** Don't rely on the cloud recording.
- **Backup:** a second uplink, and a pre-loaded "technical difficulties" slate.
- **Speaker handling:** use a speaker release form that covers livestream and recording. Collect it in the CFP acceptance email.

## 4. Remote attendee experience

- **Ticket:** I recommend free registration, with an optional paid "supporter" remote ticket. Registration gives you a list for follow-up and a count. Your tickets and sponsors are your call.
- **Chat:** one channel per track in your existing community space (Discord or Slack, whichever you already run).
- **Q&A:** one Q&A tool with a shared link. Each track has one volunteer moderator who relays the top remote questions to the room host.
- **Schedule:** publish a time-zone-friendly schedule. Mark each talk's track and say clearly that the stream is view-only.
- **Recordings:** published on YouTube within 2 weeks. Tell remote attendees upfront, because it lowers their anxiety about missing a talk.

## 5. Timeline

| When | Action |
|---|---|
| By 30 Oct | Venue answers. Decide in-house AV vs external crew. |
| By 20 Nov | Get 3 quotes (crew and kit). Pick a supplier. |
| By 15 Dec | Contract signed. Speaker release form added to the speaker pack. |
| Jan | Remote registration opens. Platform and chat channels created. |
| Early Feb | Site visit. Confirm camera positions, feeds and uplink. |
| Late Feb | Full dry run with the crew, ideally remote, with a fake talk. |
| 13 Mar | Load-in and full rehearsal in both rooms. Failover test: pull the main line. |
| 14 Mar | Show day. Producer has a go/no-go call at doors open. |
| By 28 Mar | Recordings published. Remote attendee survey sent. |

## 6. Risks and failovers

1. **Uplink drops:** the bonded or cellular backup takes over, and local recording continues.
2. **Slides not captured:** keep a spare HDMI adapter set and a speaker laptop swap procedure. Have the speaker's slides emailed to the producer as a last resort.
3. **Audio feed unavailable from the desk:** fall back to a dedicated microphone for the recording.
4. **Operator illness:** keep one backup operator on a call-off arrangement. Don't pre-pay for them.
5. **A speaker declines recording:** list this on the schedule up front and use a "this talk is in-room only" card.

## 7. Success measures (set now)

- Remote registrations and peak concurrent viewers per track.
- Percent of talks published within 2 weeks.
- Number of remote questions answered.
- Stream interruptions longer than 60 seconds. Target: zero.

## 8. Open questions

- Is there any sponsor money that could pay for a stream tier or captioning? It's worth asking before the budget is committed.
- Do you want remote attendees to pay? That changes the platform (gated vs public).
- Are there any speakers who can't be recorded, or any remote speakers? If so, I'll add a call-in path.

Tell me the venue answers and I'll turn this into a quote-comparison sheet and a run-of-show for 13-14 March.