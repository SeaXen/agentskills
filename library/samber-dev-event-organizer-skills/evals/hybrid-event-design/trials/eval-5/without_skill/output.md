# Larkspur Dev Day: Stream Rundown

**Scope:** one streamed room, 09:00–17:30. Times are local venue time.

⚠️ **Assumptions to check.** I didn't open your run of show, so I haven't synced anything to it. I wrote the session blocks as a generic day shape. Replace the `[bracketed]` fields with your real slot times, speakers, room name and room lead. The stream's clock must match the in-room clock to the minute, so check every row against the run of show. Roles, thresholds and contact fields are my proposals.

---

## 1. Roles

| Role | Does | Where |
|---|---|---|
| **Stream Director (SD)** | Calls every cue. Owns go/no-go and the escalation decision. | Control desk |
| **Technical Engineer (TE)** | Encoder, switcher, audio mix, ingest health, backup path. | Control desk |
| **Online Host** | Speaks to the stream audience in links, breaks and Q&A. | On camera or voice-over |
| **Chat Moderator (CM)** | Runs chat, filters questions, enforces the code of conduct, feeds Q&A to the Host. | Remote or desk |
| **Graphics and Captions Op (GCO)** | Lower-thirds, slates, sponsor cards, live captions. | Control desk |
| **Room Lead (RL)** | In-room liaison: speaker readiness, mic swaps, room-side problems. | Streamed room |
| **In-room MC** | Existing MC lines from the run of show. The stream follows them and doesn't replace them. | Stage |

Names: `[SD] [TE] [Host] [CM] [GCO] [RL]`. Name a deputy for each role. Breaks must never leave the SD or TE seat empty.

## 2. Comms

- **Talkback channel (voice):** SD, TE, GCO, RL. Cue calls only, no chatter.
- **Text channel:** all roles, plus the venue lead and the organizer on-call. Use it for non-urgent notes.
- **Cue vocabulary:**
  - *Standby [X]* means 30 seconds out.
  - *Go [X]* means execute now.
  - *Hold* means stop and wait.
  - *Clear* means resolved.

## 3. Pre-show

| Time | Action | Owner |
|---|---|---|
| T-3 days | Test the full path (encoder → ingest → public player) with the backup path. Confirm captions vendor, slates and the sponsor card list. | TE, GCO |
| T-1 day | Load rundown, slates and speaker lower-thirds. Confirm the pre-recorded fallback loop plays. | GCO, TE |
| 06:30 | Crew call. Power up. Check network and uplink speed (target at least 2× the stream bitrate, up and down). | TE |
| 07:15 | Camera, mic and audio-return checks in the room. | TE, RL |
| 07:45 | Full dry run: slate → live feed → slide capture → lower-third → slate. | SD |
| 08:15 | Start the **private** test stream. Confirm captions, recording and the backup encoder are all alive. | TE |
| 08:30 | **Go/no-go call.** Each role says "go" or names a blocker. | SD |
| 08:45 | **Public stream live on the pre-roll slate** with countdown and music bed. | SD, GCO |
| 08:55 | Host welcome to chat. CM opens chat with house rules. RL confirms the stage is clear. | Host, CM, RL |

## 4. Show rundown

All rows are in the streamed room.

| Time | Dur | Segment | Stream action | Cue / line | Owner |
|---|---|---|---|---|---|
| 08:45–09:00 | 15 | Pre-roll | Countdown slate, music bed, schedule card, Wi-Fi/chat-rules card. | Host live-reads the schedule at 08:55. | GCO, Host |
| **09:00** | 10 | Opening | Cut to room camera on the in-room MC's first line. Lower-third: MC name. | *Standby room, Go room.* Host hands off: "Welcome to Larkspur Dev Day. Over to the room." | SD |
| 09:10 | 40 | Keynote `[speaker]` | Switch to slides+camera layout. Lower-third at 30 s in, again at 10 min. | CM posts the Q&A link in chat at start. | SD, GCO |
| 09:50 | 10 | Keynote Q&A | Camera on the speaker and the mic runner. Host reads out chat questions. | CM passes the top 3 to the Host by 09:45. | Host, CM |
| 10:00 | 15 | **Break 1** | Break slate with countdown. Host does a chat recap and a sponsor read. | *Standby slate, Go slate.* Run the sponsor card. | SD, GCO |
| 10:15 | 30 | Talk 1 `[title/speaker]` | Standard talk layout. | Host intro line: `[one sentence]`. | SD |
| 10:45 | 5 | Changeover | Hold the slate or the stage wide shot. Do not show a speaker walk-on with live audio. | RL confirms the next speaker's mic and laptop. | RL, TE |
| 10:50 | 30 | Talk 2 `[title/speaker]` | Same. | | SD |
| 11:20 | 10 | **Break 2** | Break slate and chat recap. | | SD, Host |
| 11:30 | 30 | Talk 3 `[title/speaker]` | Same. | | SD |
| 12:00 | 30 | Talk 4 `[title/speaker]` | Same. | | SD |
| 12:30 | 60 | **Lunch** | Lunch slate, afternoon agenda card and sponsor loop. Host posts a midday recap and polls chat. | Public player stays up. The TE does a full path check and a recording-integrity check. | SD, TE |
| 13:30 | 30 | Talk 5 `[title/speaker]` | Resume with a short Host link. | *Go room* only after the TE confirms mic level. | SD |
| 14:00 | 30 | Talk 6 `[title/speaker]` | Standard. | | SD |
| 14:30 | 15 | **Break 3** | Break slate. | | SD |
| 14:45 | 30 | Talk 7 `[title/speaker]` | Standard. | | SD |
| 15:15 | 30 | Panel `[panelists]` | Wide + two-shot layout. All mics are live. Lower-third per speaker, 10 s each at the first answer. | The Host feeds chat questions to the moderator in the room. | SD, GCO |
| 15:45 | 15 | **Break 4** | Break slate. | | SD |
| 16:00 | 30 | Talk 8 `[title/speaker]` | Standard. | | SD |
| 16:30 | 30 | Closing Talk / Fireside `[speaker]` | Standard. | | SD |
| 17:00 | 20 | Closing + thanks | Sponsor/credit slate. Room camera on the MC's closing lines. | Host line: "Thanks for watching. The recording will be at `[URL]` by `[date]`." | SD, Host |
| 17:20 | 10 | Post-roll | End slate with recording link. Chat stays open until 17:25. | CM posts the feedback survey link. | CM |
| **17:30** | – | **Stream off** | End on slate. Stop encoder last, after the recording is confirmed closed. | *Clear stream.* | TE |

If the room's real schedule has a different number of slots, keep the structure: every break and the lunch get a slate, and every session gets a Host intro line.

## 5. Per-segment checklist (SD runs it for each session)

1. T-2 min: *Standby slides.* The TE confirms speaker mic level, slide capture and return.
2. T-30 s: *Standby lower-third.* The GCO has the right name and title loaded.
3. T-0: *Go room.* Cut to room feed.
4. T+30 s: Lower-third on, 8 s.
5. End: *Standby slate.* Cut to slate only once the speaker finishes, never mid-sentence.
6. The CM confirms Q&A questions are sorted before any Q&A block.

## 6. Contingency and escalation

### Severity levels

| Level | What it looks like | Response time |
|---|---|---|
| **S1: stream down** | Public player is dead, or is frozen for more than 30 s. | Act immediately. |
| **S2: degraded** | No audio, wrong source, major A/V desync, captions dead. | Fix within 2 min. |
| **S3: minor** | Wrong lower-third, typo on slate, chat spam. | Fix within the segment. |

### Playbooks

| Failure | First action (≤30 s) | If not fixed |
|---|---|---|
| **Audio lost** | TE switches to the backup audio feed. SD cuts to the slate "We'll be right back" if over 10 s. | Hold slate. RL swaps mic. |
| **Video lost** | Switch camera. SD cuts to slides-only layout. | Hold slate. |
| **Encoder / uplink fail** | TE fails over to the **backup encoder** on the **backup uplink**. | SD posts a "technical difficulties" notice in chat. Go to S1. |
| **Slides won't show** | RL gets the speaker to re-share. SD stays on camera. | Move to the next item and return later. |
| **Speaker late / no-show** | RL calls. SD holds the slate with the Host filling live. | After 5 min, the Host announces a schedule shift and the in-room MC extends the slot. |
| **Session overrun** | SD tells the RL at T-5. The in-room MC gives the cut-off. | The stream follows the room. The Host absorbs the delay at the next break. |
| **Chat abuse** | CM removes and bans per the code of conduct. | Slow mode, then followers-only. |
| **Captions down** | GCO restarts. | Tell chat. Fix by the next break. |

### Escalation path

1. The role owner tries the fix for up to **60 s**.
2. The SD is informed and makes the call: hold, fail over or cut.
3. S1 or an unresolved S2 at 2 min: **notify the Organizer on-call** `[name/phone]`.
4. S1 at 5 min: **notify the Venue/AV contact** `[name/phone]` and the **Streaming provider support** `[phone/ticket URL]`. The Organizer decides whether to announce a delay.
5. S1 at 10 min or more: the Organizer authorizes switching to the **pre-recorded fallback loop** and posts to the social account. Publish a recording-later notice.

Contact sheet to fill: SD `[ ]`, TE `[ ]`, Organizer on-call `[ ]`, Venue AV `[ ]`, ISP/uplink NOC `[ ]`, Platform support `[ ]`, Captions vendor `[ ]`.

## 7. Post-show

| Time | Action | Owner |
|---|---|---|
| 17:30 | Confirm the recording file is closed and its size looks plausible. Copy to two locations. | TE |
| 17:45 | Strike the control desk. Log incidents (time, severity, fix). | TE, SD |
| 18:00 | 10-minute crew debrief: what broke, what worked. | SD |
| +1 day | Publish the full recording (or per-session cuts) and the final chat export. | TE, CM |
| +3 days | Send viewer numbers and incident log to the Organizer. | SD |

## 8. Open items for you

- ❌ **Session grid:** replace every `[bracket]` with the real slots, speakers and room name from the run of show.
- ❌ **Lunch and break lengths:** I assumed 10–15 min breaks and a 60 min lunch. Match yours.
- ℹ️ **Contact sheet:** nothing is filled in, and I left in no phone numbers.
- ℹ️ **Pre-recorded fallback loop:** if you don't have one, make a 10-minute loop with the schedule and sponsor cards.

If you paste the in-room grid (without anything private), I can sync times and MC hand-offs row by row.