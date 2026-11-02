# Kestrel Software virtual user conference: delivery plan

This follows the `virtual-event-production` skill. You gave me the context but I couldn't run the interview, so I list my assumptions and the open questions at the end. Each section is a decision point for you to validate before anything else is signed.

## 1. Interaction posture

⚠️ **Posture: an event people are inside, not a feed they watch.** Booths, a sold attendee list and camera-on breakouts all depend on an interaction surface.

Staffing depends on concurrency, which you haven't told me. I give both cases below.
- **One session at a time:** one moderator covers the whole event.
- **Parallel tracks:** staff one moderator per track. That is a staffing problem before it is a technical one.

## 2. Platform posture

✅ **The managed virtual-venue platform is settled.** Procurement signed it and the contract runs to next year, so this is a deleted rung, not a demoted one. Don't spend decision energy re-arguing it.

**Do not run a second live platform carrying the same sessions in parallel.** It halves the audience of every speaker Q&A and doubles moderation. The loss shows up only as people who never got an answer.

The remaining work is to find out what the contract and the admin console let you do. Put these questions to procurement and the vendor **in writing** before you design anything on top of the platform:

| Area | Ask |
|---|---|
| Ceiling | What is the concurrent-viewer limit on our plan? What happens at it: a queue, a refusal, or an upgrade invoice? |
| Delivery | Does the player degrade or stall on a poor connection? Is there an audio-only fallback? Does a mid-session restart keep the audience's place? |
| Speakers | Can a speaker share a screen, a second screen and system audio? Which of those needs a desktop app? |
| Moderation | Can a moderator delete a message, remove a person and lock a space during a live session without leaving it? Is there a moderator view of the question queue? |
| Breakouts | **Are breakout and networking rooms recorded? Can that be switched off? Is it separable from talk recordings?** |
| Sponsor data | **What exactly is exported to a sponsor when someone enters a booth or the directory? Does the attendee see that at the moment it happens?** |
| Data | Where is attendee data stored, and under which jurisdiction? How long is chat history kept, and can it be deleted on request? |
| Accessibility | What captioning exists, in which languages, and can an external captioner feed in? Is the player keyboard- and screen-reader-friendly? |
| Recordings | Can sessions be recorded on the platform? Who owns them and can delete them? |
| Reversibility | What can still be changed in the existing contract, and until when? |

Also run a bandwidth sanity check on your own side if you originate any streams yourselves.

Send the accessibility answers to `event-accessibility-inclusion`. That skill sets the captions bar, not you.

## 3. The sold attendee list (highest-risk item)

🔴 **Do not export the raw list to the sponsor until the data-handling review is done.** A list a sponsor has already exported cannot be recalled.

**What to check first (you or counsel; this skill names no jurisdiction):**
1. What did registration tell attendees? If it didn't say their details could go to sponsors, you probably can't hand over the list as it stands.
2. What does the sponsor's contract promise: a raw list or leads?
3. What does the platform's own terms and data flow already do with the directory?

**My recommendation:**
- Renegotiate the deliverable from "the list" to **opt-in leads**. Attendees choose to share when they enter the booth, scan, or book a demo. That is the platform's booth lead-capture flow, and the attendee sees it at the moment it happens.
- Offer the sponsor something that actually helps them, such as a guaranteed number of booth-visit slots or a sponsored session slot, in place of the list.
- If the list has to go out, send it only for attendees who consented at registration. Tell the other two sponsors the same terms are available, so you don't create a side deal.

The decision is yours and counsel's. I'm flagging it as the one item that can't be undone.

## 4. Camera-on networking breakouts

**Recommendation:** run them, but treat them as an open space with attendees on camera.

**Consent and privacy**
- Attendee consent for being on camera **cannot be collected after the fact**. Disclose in registration and in the join flow that breakouts are camera-on and **not recorded**.
- Confirm in writing that the platform does not record breakouts (Q16 above). If it can't be turned off, say so to attendees or drop the camera-on requirement.
- Recordings made by participants are outside any consent you hold. Say so in the breakout rules.
- Make camera-on the **default and the invitation, not a hard gate**. Offer an audio-only or profile-photo fallback. Whether that's required is `event-accessibility-inclusion`'s call. A safety or accessibility reason to keep a camera off shouldn't cost someone the whole networking block.

**Conduct**
- A digital space raises harassment risk. Name a responder for breakouts, with a visible way to report an incident and a way to remove someone fast. The reporting path belongs to `event-code-of-conduct`.
- Staff breakout hosts by name. They roam, welcome people, and handle conduct. They are not the session moderators.

**Design**
- Use small structured rooms with a prompt, such as "what are you building with Kestrel?" or topic and role rooms. Random matching works as an option, but open rooms with no prompt produce silence.
- Make the gaps between sessions long enough to join, talk and leave. Q2 (shortest gap) tells me whether you have room.

⚠️ **Buying interaction nobody uses:** breakouts and booths cost a review and ops whether or not anyone opens them. Plan capacity from your own signals, not from an assumed turnout. 3,000 registrants does not mean 3,000 attendees, and attendance can move either way. Track breakout usage live so you can fold rooms and avoid empty ones.

## 5. Sponsor booths

- Three sponsors have virtual booths. Run each sponsor through a **walkthrough on the real platform** before the day, and tell them the conduct rules apply to their booth staff too.
- Give sponsors a **single named contact** on your side during the event.
- Agree up front what a sponsor receives (opt-in leads, per section 3) and when.
- Check what each sponsor's contract promises. If one names the stream or a session, that raises your failure-drill rung (section 8).

## 6. Remote-speaker readiness

**Default rung:** send the written home-setup note with the join link on the day acceptances go out. It covers a wired connection, wired headphones, closing background sync, camera at eye level, and light on the face. It also covers sharing a single window, no background music (a platform can take a stream down for it), and a recorded fallback for any live demo.

**Move up for these (Q11):**
- **Any speaker who has never presented on this platform:** move up one rung to a **group tech-check window** on the real platform, run well before the day.
- **Keynote, unrepeatable sessions, live demos, unknown or poor connections:** **individual tech check plus an instructed local backup recording.**
- **Anyone presenting in the middle of their night:** a **pre-recorded talk** with the speaker live in chat.

**Hand-offs**
- **Get the local backup recording covered by the consent record in `event-speaker-experience` before the file exists.** Offer a way to decline.
- Put the speaker's own local time in the first line of the briefing.
- A tech check on any tool other than the event platform is deleted. It tests nothing that matters.

## 7. Moderation staffing

Assign people **by name**, not by function.

- **Default:** one named moderator per concurrent session. They read chat, select and relay questions, and hold conduct.
- **Add a technical watcher** who watches the output as an audience member does, on a second device. Use this for the keynote and any unrepeatable session. Use it for every session if last edition's feed died unnoticed.
- **Add a host on the feed** for the keynote and the opening and closing. The sponsor booth deliverables and any paid ticket (Q4) justify it, and it's the only role that tells the audience out loud when something breaks.
- **Breakout hosts** are in addition to all of the above.
- **Do not let speakers moderate their own chat.** That rung is deleted.
- Agree per speaker how questions are relayed (moderator reads aloud, or posts to a private channel the speaker watches), and who calls time.
- Keep one organizers-only coordination channel, separate from everything attendee-facing. It carries over unchanged from a physical event.

## 8. Failure drill

1. **Publish a fallback line before the day**, in a place outside the platform (email, status or schedule page, social). One sentence naming where to look. Example: "If the stream drops, it's our side, not yours. Updates are at [page]."
2. **Rehearse the single likeliest failure** (a speaker's connection dropping mid-talk), with the moderator's exact words agreed in advance.
3. **Consider a warm fallback stream target for the keynote and unrepeatable sessions,** if the platform can output one. Don't treat that as a parallel platform carrying all sessions.
4. **Read the other scenarios aloud once** with the people who would act on them: no-show, live stream with dead audio, platform incident, conduct incident, and a stream pulled for background music.
5. **Close the loop.** Say it out loud when it breaks, and say again when it's fixed.

## 9. Rehearsal

Rehearse **once, on the real platform**, with moderators, breakout hosts, the host and at least one sponsor booth. This is the step that gets cut. The date depends on your event date, so I need that from you.

## 10. Budget consequence (for `event-budget`)

- **Survives every tier:** the stream and fallback line.
- **Goes first on a lean budget:** the interaction surface and its staffing, meaning breakout hosts, extra moderators and the host.
- Counsel review of the list and consent is a real cost, not optional.

## 11. Measurement (self-set metrics, not industry standards)

**Gates to check before the first session:**
- Every concurrent session has a named moderator, or its interaction surface is closed.
- Every speaker has joined the real platform at least once before the day.
- The fallback line is published and the person who'll say it knows the sentence.

**Pick two or three metrics and record in advance what each would trigger:**
- Sessions delivered without an audience-visible failure.
- Time from a feed dropping to the audience being told.
- Questions relayed against questions asked.
- Breakout usage against sign-ups (this one guards against buying interaction nobody uses).

## Assumptions and open questions

| # | Open question | Assumed |
|---|---|---|
| 1 | Event date and rehearsal date | Unknown. Schedule backward from it |
| 2 | Concurrent sessions and shortest gap (Q2) | Unknown. Both staffing cases given above |
| 3 | Speaker and audience time zones (Q3) | Unknown. Affects the pre-record rung |
| 4 | What registration disclosed about sharing and camera-on (Q5) | **Unknown. Gates sections 3 and 4** |
| 5 | Paid tickets or stream-naming sponsor clauses (Q4) | Unknown. Raises host and drill rungs |
| 6 | Recurring or one-off (Q8) | Unknown. Recurring promotes reusable prep |
| 7 | People available for production only (Q9) | Unknown. Caps the staffing |
| 8 | Unrepeatable sessions, live demos, unknown speakers (Q11) | Unknown. Drives speaker rungs |
| 9 | Last edition's failures (Q10) | Unknown |

The first thing I'd resolve is item 4 together with the list question in section 3, because it can't be reversed once data is exported or people appear on camera without notice.

**Hand-offs:** channel roster to `event-comms-channels`, consent record to `event-speaker-experience`, captions bar to `event-accessibility-inclusion`, incident path to `event-code-of-conduct`, cue sheet to `event-run-of-show`, cost split to `event-budget`, and captured sessions to `event-content-repurposing` after the event.

I didn't use the Bash tool, which was denied. I read the skill file and its three reference files with Read, and didn't change any files.