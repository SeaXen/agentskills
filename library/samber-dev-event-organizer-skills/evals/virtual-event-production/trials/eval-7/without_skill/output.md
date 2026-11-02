**Next action (2 min):** send me the event date and whether the 1,400 is registrants or expected live peak. Below I assume 1,400 registrants, 60% live peak (~840), and I size for 1,400 concurrent anyway.

Four decisions come first. The production plan follows.

## Decisions

### 1. Hybrid: no. Fully remote, with the auditorium as a studio

- Hybrid is two events: a room audience and a stream audience. Each needs its own AV, staff and attention.
- "Empty auditorium" is not free. Hybrid adds cameras, a switcher, house audio, a room crew, security, catering, insurance and local-attendee logistics.
- Remote attendees become second-class when the room gets the energy and the stream gets the leftovers. Two tracks make this worse, because the room can only watch one.
- The empty auditorium is useful as a production base:
  - **Keynote origination:** controlled acoustics, a fixed camera position and wired internet.
  - **Green room and speaker tech check** for local speakers.
  - **Staff war room** for producer, tech director and support.
- Optional: a staff-only watch party, capped, with no extra AV and no speakers on site. It must not touch the budget.
- Revisit hybrid next year only if all three hold:
  1. At least 30% of attendees are within one hour of the venue.
  2. Sponsors or revenue pay for the on-site cost.
  3. This year's remote run is stable.

Tell your co-organizer: "We use the room, we don't host in it."

### 2. Captioning: WCAG 2.2 Level AA, with human live captions

- Commit publicly: "All live sessions have human-written real-time captions (CART). All recordings have edited captions and a transcript."
- Live (WCAG 1.2.4): human CART on both tracks, one captioner per track, plus one standby.
  - Target 98% or better accuracy, and publish the target.
  - Auto-captions are the fallback only if a captioner drops.
- Pre-recorded sessions (WCAG 1.2.2): the speaker uploads the recording and the script, and we make human-edited captions before air. This is better than live CART for most talks.
- After the event: corrected captions and transcripts on all replays within 48 hours. Deliver WebVTT and SRT.
- Caption language is English. Add translated subtitles only if the registration data shows a clear need.
- Platform must-haves: closed captions, adjustable size and contrast, a separate transcript pane, and a CART text feed (API or StreamText-style embed).
- Also in scope: keyboard-navigable player and chat, no flashing content, slides at 4.5:1 contrast, and audio description for any pure-visual segment.
- Legal check, because I don't know your location or audience: the EU Accessibility Act (in force since June 2025) and US ADA expectations both point to AA. Confirm with counsel before you promise anything beyond this.
- Registration form gets an "accommodations needed" field. Someone owns it and replies within 2 business days.

### 3. Attendee communication: build five channels, one source of truth

| Channel | Role | Owner |
|---|---|---|
| **Email** (event platform plus ESP) | Primary. Registration, agenda, reminders, replays. Source of truth. | Comms lead |
| **Event platform chat and Q&A** | Live conversation, per-session chat, upvoted questions. | Moderators |
| **Banner and status page** | Incidents and schedule changes. One URL, linked in every email. | Producer |
| **Social, one hashtag** | Reach and proof. Not for support. | Comms lead |
| **Staff and speaker backchannel** (private Slack channel plus a backstage video room) | Run-of-show calls. Never shown to attendees. | Producer |

- No Discord or Slack for attendees this year. A new account is a signup barrier for 1,400 people, and you have no community to seed it.
- Collect an opt-in at registration for a post-event community. Decide next year from that number.
- Email cadence (T = event day):
  1. T-6 weeks: speakers and agenda announced.
  2. T-3 weeks: "Build your schedule".
  3. T-1 week: tech check link, accessibility info, time-zone converter.
  4. T-1 day: join link, "what to expect".
  5. T-1 hour: "starts soon".
  6. T+1 day: replays and survey.
  7. T+7 days: captioned replays, resources, next-year interest.
- Support: a help desk inbox plus an in-platform "Need help?" link, with a 5-minute response target during the event.
- Moderation: publish a code of conduct, with a named person and a report address.

### 4. Keynote audio: the mic and room matter more than the board

- Pick the setup by where the keynote speaker sits:
  - **Speaker in the auditorium (recommended): RØDECaster Pro II.**
    - Roughly $600–700 (check current price).
    - Handles 1–2 XLR mics, a USB return and a clean mix-minus for remote guests.
    - Built-in processing (compression, de-ess, noise gate) gives a polished sound without a sound engineer.
    - Pair it with a dynamic broadcast mic such as Shure SM7dB or Electro-Voice RE20, on a boom arm, plus a lav as backup.
  - **Panel with 3–6 mics:** Allen & Heath CQ-12T (or similar digital mixer), plus an engineer. Only if the keynote is a panel.
  - **Speaker remote at home:** no board. Ship a USB dynamic mic (Samson Q2U or Shure MV7+), a pop filter and a headphone requirement. Run a rehearsal on the actual platform.
- Rules for all setups:
  - Speakers wear wired headphones, never speakers, to avoid echo.
  - Keep the room carpeted or draped. Hard walls sound amateur.
  - Set the level in rehearsal to peak around -12 dBFS, and use a limiter.
  - Run a separate monitor feed to the producer, plus a backup recording on the mixer or on a laptop.
- Prices are from memory, not checked. Confirm before you buy.

## Production plan

### Format

- Assumed: one or two days, two parallel tracks, with the keynote as a single-stage opener.
- Run in 4-hour blocks that favor your main time zones, and keep replays on demand. Fully remote with global registrants means no single hour suits everyone.
- Session length is 25–30 minutes, plus 5 minutes of live Q&A and a 10-minute break between sessions. The keynote is 30–40 minutes.
- **Pre-record most track talks and run live Q&A** (decision): this removes most speaker-side failures. The keynote runs live, with a pre-recorded fallback ready.

### Platform (pick by criteria, not brand)

- Must have:
  - Capacity of 2,000 or more concurrent.
  - Two or more tracks with a sessions-switch UX.
  - Live Q&A, chat, polls, and CART integration.
  - Speaker backstage and green room.
  - On-demand replay and exportable engagement data.
  - SSO or a magic-link join (no password fatigue).
- Shortlist and run a demo for each: Zoom Events, Airmeet, Swapcard, Hubilo, Cvent Attendee Hub, Vimeo Events.
- Run a 1,400-viewer load test with the vendor in writing. Get the SLA and support contact for event day.
- Decide by T-10 weeks.

### Team (roles, not people)

| Role | Count |
|---|---|
| Producer (final call) | 1 |
| Tech director (platform and streams) | 1 |
| Track director and stage manager | 1 per track |
| Moderator and host | 1 per track, plus 1 for keynote |
| CART captioner | 1 per track, plus 1 standby |
| Chat moderators | 4, plus a lead (~1 per 300 concurrent attendees) |
| Support desk | 2 |
| Speaker wrangler | 1 |
| Comms lead | 1 |
| Accessibility lead | 1 |

That is about 16 people in total, with some roles merged. Never merge the producer with the tech director.

### Timeline (T = event day)

| When | Milestone |
|---|---|
| T-14 wks | Scope, budget, date, platform shortlist, accessibility commitment |
| T-12 wks | CFP closed, speakers confirmed. Book CART vendor and captioners |
| T-10 wks | Platform contract signed. Registration live. Accommodations form live |
| T-8 wks | Agenda draft. Speaker kit sent (mic, lighting guide, template, recording spec) |
| T-6 wks | Email 1. Speaker briefing call. Slide template with accessibility rules |
| T-4 wks | Pre-recorded talks due. Captioning of recordings starts |
| T-3 wks | Load test. Rehearsal 1 (platform and backstage) for all speakers |
| T-2 wks | Final agenda lock. Staff runbook frozen. Rehearsal 2 for keynote and live-Q&A speakers |
| T-1 wk | Tech check link out. Fallback drill (kill a stream, switch to backup) |
| T-1 day | Full dress rehearsal with captioners. Go/no-go meeting |
| T day | Run of show. Producer checks in every 2 hours |
| T+1 day | Replays up, survey out |
| T+2 days | Edited captions and transcripts done |
| T+2 wks | Post-mortem. Report to stakeholders |

### Run-of-show rules

- Open each room 15 minutes early with looping slides and music. Mute, no echo.
- A countdown to every session. The stage manager calls cues on the private channel.
- Hard stops: sessions never overrun. The moderator cuts at the time, and Q&A continues in chat.
- The producer holds a pre-written holding slide, a pre-recorded fallback for each live session, and a script for "we have a technical issue".
- Moderators triage Q&A. Questions go to the speaker in priority order, and a few are answered in writing afterward.

### Risk register

| Risk | Plan |
|---|---|
| Platform outage | Backup stream (YouTube unlisted) and a template email, tested at T-1 week |
| Speaker connection failure | Pre-recorded fallback for every live talk |
| Captioner no-show | Standby captioner, plus auto-caption fallback |
| Audio echo or noise | Headphone rule and rehearsal 1 |
| Attendee overload (more than 1,400) | Plan for 2,000, with a waiting-room message |
| Harassment in chat | Code of conduct, 4 moderators, ban rights, a named lead |
| Time-zone confusion | Auto-converted times in every email and the agenda |

### Measurement (pipeline and quality, not applause)

- Real metrics:
  1. Live attendance rate (target 50–60% of registrants).
  2. Median session watch time.
  3. Replay views in the 14 days after.
  4. Caption-feature usage.
  5. Survey score and net promoter score.
  6. Qualified opt-ins for follow-up.
- Vanity metrics (registrations, peak concurrency): track, don't report as success.
- Judge on the two or three events after this one, not just this one.

## Open questions (defaults in brackets)

1. Date and number of days? [two days]
2. Is 1,400 registrants or live peak? [registrants]
3. Free or paid? Sponsors? [free, no sponsors]
4. Main time zones of attendees? [Europe plus US East]
5. Where is the keynote speaker? [in the auditorium]
6. Budget ceiling?

**Next:** send me answers to 1 and 2, and I'll turn the timeline into dated milestones.