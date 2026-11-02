**Next action:** move every tech check off Google Meet onto the licensed broadcast platform, and re-send the invites today.

I don't have answers to Q1 (is there a Q&A or chat surface at all?), Q2 (how many sessions run at once?), Q4, Q5, Q7 and Q10, so I assumed the following. Correct me on any of them.
- The event is people watching, with a question queue on the platform.
- Sessions run one at a time.
- Nothing about last edition is known.

## 1. Fix the tech-check tool (blocking)

- A check on Meet is a deleted rung in the skill, not a weak one. It tests nothing that matters on the day: the platform's screen-share path, its audio device handling, or what the speaker's browser does under it.
- "One less account" is a false saving. Every speaker must join the licensed platform on the day anyway. Joining it once before the day is the point of the check.
- Gate to pass before the day: every speaker has joined the real platform at least once, by the same link and route as on the day.
- Ask the platform vendor in writing, before the checks:
  1. Does a speaker need an account, or only the link?
  2. Which of screen share, second screen and system audio needs a desktop app rather than a browser?
  3. Can a speaker record locally, and how?
  4. Can a stream restart without changing its address?
  5. Is there a rehearsal room I can open before the day?
- Time: about 30 minutes to email the vendor and re-issue 14 invites.

## 2. Speaker readiness, by rung

| Speakers | Rung | Why |
|---|---|---|
| All 14 | Written home-setup note, sent now with the platform join link | Cheap and reusable. It catches the common failures before any call. |
| 2 live-demo speakers | Individual check plus an instructed local backup recording | Q11 promotes on a live demo. |
| Auckland speaker | See section 3 | Q3 |
| Any keynote, any unrepeatable session, any speaker with a bad or unknown connection | Individual check plus local backup | Q11. I need names from you. |
| Everyone else | Group window or short individual slot, on the platform | The slots already exist, so use them. Ask each person by name whether the demo or audio setup is unusual, because quiet speakers skip that. |

**The home-setup note** covers:
- a wired connection, or the same room as the router
- wired headphones with a microphone
- closing anything that syncs in the background
- a phone on a mobile connection nearby as a fallback
- the camera at eye level with light in front
- sharing one window, decided in advance
- no background music in anything shared. Incidental music can get a stream taken down by the platform itself, mid-session.

**Tech-check script**, in order, each step confirmed out loud:
1. Join by the attendee route.
2. Audio both ways. The moderator describes in words what the speaker sounds like.
3. Share the real deck, including the switch into and out of the demo.
4. Test anything unusual.
5. Decide how questions reach the speaker. Decide it per speaker.
6. Agree the dropped-connection plan: rejoin by the same link, plus the moderator's agreed words.
7. Start the local backup recording.

**Local backup recording** rules:
- It is local only. An upload competes for the same failing uplink.
- Give the exact steps for this platform.
- Name where to send the file and by when, in the same sentence.
- It creates a file, so cover it in the consent record held by `event-speaker-experience` before the file exists. Let speakers refuse it.
- It does not help the audience in the minute the feed dies. Section 5 covers that.

## 3. The two live demos against staging

- Have each demo speaker record a fallback of the demo and say so up front. A network-dependent demo is the most fragile thing in a remote talk.
- Check the demo once during the individual check, on the platform, with the real screen share.
- Add a technical watcher to those two sessions. Q11 ("anything live that cannot be re-run") promotes it. This person watches the output as an audience member does, on a second device. Name them.
- If either demo has already failed live once, promote that speaker to a pre-recorded talk with the speaker live in chat. That needs your Q10 answer.
- These next points come from my own reasoning, not the skill, so verify them:
  - Check that staging is reachable from each speaker's home network, with no VPN or IP allowlist surprises.
  - Check that credentials and test data survive the day.
  - Check that nobody deploys to staging during the sessions.
  - Check that rate limits hold when two demos and rehearsals overlap.

## 4. Auckland speaker

- **Do not run the check at 03:00.** A night-time slot is a no-show risk and a quality risk, and no preparation fixes either.
- Offer her a slot in her own evening or early morning. The cost is your time, so you take a late or early slot.
- Time conversion, to verify against actual dates:
  - New Zealand is UTC+13 now.
  - Her 03:00 is about 14:00 UTC the day before.
  - That is about 16:00 in Central Europe and 10:00 on the US East coast.
  - Europe leaves summer time on Oct 25 and the US on Nov 1, so next week's offsets may shift mid-week.
- Open question: when is her talk? If it is also in her night, report it to `event-schedule-design`. The two real answers are moving the slot, or a pre-recorded talk with her live in chat (Q3 promotes this).
- If no check slot works for her, ask the vendor whether she can join a self-serve rehearsal room. That still meets the gate that she joined the real platform once. It does not replace the check.
- Put her local time in the first line of her message.

Briefing draft:

> Your session is [day] at [UTC time], which is [her local time]. Tell me now if that is wrong. Join with the link below. It is the platform we run the whole event on. Read the attached setup note before [date]. The check is a short slot with me on this same link. We test your screen share with your real deck, run the demo once, and agree what I say if you drop. I will also walk you through a local recording on your own machine. It is insurance so a dropped connection costs the live session, not your talk. If you would rather not be recorded locally, say so and we skip it. Your consent form covers the session recording only.

## 5. Also for the speakers

1. **Moderator, by name.** Name one moderator for the session, since sessions run one at a time. If you close the question surface, you need no moderator. An open surface with nobody watching is a conduct duty with no responder, and the speaker cannot moderate their own chat.
2. **Failure drill.** Rehearse one scenario: the speaker's connection drops mid-talk. Agree the moderator's exact opening words.
3. **Fallback line.** Publish one sentence before the day, where the audience already looks. It says where to go when the feed dies.
4. **Rehearsal.** Run one full rehearsal on the real platform.
5. **Hand-offs.**
   - Send tech-check results and the consent status for the local recordings back to `event-speaker-experience`.
   - Ask the vendor what captioning the platform provides, then report the answer to `event-accessibility-inclusion`. They set the bar, not me.
   - Send the cost of the technical watcher and the extra check slots to `event-budget`.

## Open questions, in priority order

1. Q1: is there a question queue or chat, or is this a pure feed?
2. Q11: which sessions cannot be re-run? Which speakers have an unknown connection or have never used this platform? Has either demo failed live before (Q10)?
3. When is the Auckland talk, and which slot can you offer her?
4. Q4 and Q7: does a sponsor or a paid ticket name the stream, and what is the last date you could still change platform?

I'll present this section by section for validation if you want. Say "go" and I'll start with the interaction posture.