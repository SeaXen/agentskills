**Next action:** answer the 8 open questions in section 9. The plan below rests on 5 stated assumptions. The plan is not yet approved, so sign nothing until you have checked each section.

I could not run the interview one question at a time, so I made assumptions instead. Each is flagged and each can overturn a rung.

**Assumptions**
- A1: open chat exists, so attendees are inside the event, not only watching.
- A2: two tracks run at once, with a shared keynote.
- A3: the keynote cannot be re-run.
- A4: no paid virtual ticket and no sponsor deliverable naming the stream.
- A5: no chat space or platform is already paid for.

## 1. Interaction posture

**Event people are inside.** Two concurrent tracks with open chat is a staffing problem before it is a technical one. If you close chat, Menu 3 disappears and the plan shrinks a lot. Tell me if A1 is wrong.

## 2. Hybrid: settled

**Stay fully virtual. I recommend against reopening the format.**
- Format choice belongs to `event-format-selection`. This production plan treats virtual as closed.
- That skill ranks hybrid last for conferences. It is the maximum-cost option: two simultaneous productions, roughly double the AV and logistics cost.
- Its promotion test is remote registrations above ~25–30% of paid attendance, covering their marginal cost, plus a budget sized for the extra production.
- Your event is 100% remote, so that test does not apply. The empty auditorium saves a room fee. It does not fund a second production, and no in-room audience evidence exists.
- Ask your co-organizer for numbers: how many people would attend in person, and would they pay?
- If they bring that evidence, reopen the decision in `event-format-selection`, not here.
- Cheap legitimate use of the room: a studio for the keynote speaker, hosts and moderators. That has no in-room audience, so it is not hybrid. It does add a physical stage, which makes section 7 `event-production`'s job.

## 3. Platform posture

**Recommend: one one-way feed per track on a public video platform, plus a chat space built from scratch (section 6).** This is the default rung.
- No second login for viewers.
- Most robust on a phone with a weak connection.
- Lowest compliance exposure.

Why not the managed virtual-venue platform? It earns promotion only on three conditions. None is confirmed:
- Attendees move between sessions (Q2): two tracks may qualify, so confirm.
- A sponsor booth or an attendee directory sold as a ticket benefit (Q4).
- Procurement forces it (Q6).

If Q4 or Q6 says yes, the managed platform is promoted and the ranking changes.

Do not run the same sessions live on two platforms. That rung is deleted.

**Put these vendor questions in writing before committing.** The full list is in `references/platform-selection-and-vendor-questions.md`. The most important:
1. Concurrent-viewer ceiling on your plan, and what happens at the ceiling. Size it for ~1,400 on the keynote, split across two tracks afterwards.
2. Can a viewer watch without an account? Is there an audio-only fallback?
3. Can the stream restart mid-session without changing its address?
4. Moderator powers: delete a message, remove a person and lock a space mid-session.
5. Captioning: what the platform provides, and can an external captioner feed it?
6. Where attendee data is stored, and does anything record attendees on camera?

Take the data and residency questions to your own counsel. I name no jurisdiction.

**Reversal date (Q7):** unknown. A public feed plus chat can be abandoned the week before, at the cost of an announcement. Rank every later choice against that date.

## 4. Speaker readiness

- **All speakers:**
  - Send the home-setup note (`references/remote-speaker-readiness.md`) with the join link.
  - Send it the same day the acceptance goes out. If acceptances are already out, send it today.
  - Put each speaker's own local time in the first line.
- **One shared group tech-check window**, on the real platform, for everyone.
  - Ask each speaker by name whether they have anything unusual to test.
- **Promoted to an individual check plus an instructed local backup recording:**
  - the keynote speaker (A3)
  - any speaker with a live demo
  - any speaker with an unknown or bad connection
  - anyone who has never presented on this platform
- **Pre-recorded, played on schedule, speaker live in chat:**
  - speakers whose slot lands in the middle of their night (Q3)
  - speakers who cannot hold a live slot
  - a demo that already failed once
  - Move the slot first, if the schedule allows (`event-schedule-design`).
- Get the local backup recordings covered by the consent record in `event-speaker-experience` before the files exist.
- Warn every speaker: no background music in anything shared. It can get the stream taken down by the platform.
- Do not run a check on any tool other than the event platform.

## 5. Moderation staffing

**Recommend: one moderator per concurrent track, plus a technical watcher per track.** The watcher promotion comes from A3 (unrepeatable keynote).
- The watcher watches the output as an audience member does, on a second device.
- The watcher does not read chat.
- One person cannot watch two streams' health at once.

| Role | Track A | Track B |
|---|---|---|
| Moderator (reads chat, relays questions, holds conduct) | `____` | `____` |
| Technical watcher | `____` | `____` |

- **Gate:** every slot needs a real name before the first session. If a slot stays empty, close that track's chat.
- **Host on the feed:** add one only if Q4 turns out to be a paid ticket or a sponsor deliverable, or if the programme has gaps to fill (Q2).
- The speaker never moderates their own chat. That rung is deleted.
- Question relay is decided per speaker at the tech check. The default is that the moderator reads questions aloud at agreed points.
- Add one organizer-only coordination channel, kept separate from every attendee channel (`event-run-of-show`).

## 6. Attendee communication channels

This comes from `event-comms-channels`. It is provisional until `event-cultural-identity` supplies a register. Check that it exists (Q5).

**Roster. Every channel has one job and one named owner.**

| Channel | Job | Owner |
|---|---|---|
| Announcement list | Routine messages to all registrants. Already exists from registration. | `____` |
| Chat space, read-only announcements channel | Live change-of-plan pushes | `____` |
| Chat space, open channel | Attendees talk to each other | `____` |
| Chat space, one live-question channel per track | In-session questions, staffed by that track's moderator | Track moderator |
| Status page, hosted outside the platform | Single source of truth when a feed breaks. Nobody checks it unprompted, so every disruption pushes a link on the announcement channel. | `____` |

- **Chat space:** pick it on four checks:
  - free voice
  - an account the audience already has
  - history retained on the free tier
  - an exportable member list
- **Event app:** no. Under 3 concurrent rooms and nothing forces one.
- **Incident reporting:** excluded. `event-code-of-conduct` owns it, including the rule that one authorized publisher issues any public incident statement. Confirm the CoC covers digital spaces.
- **Routing:** two-channel split, meaning broadcast channels that nobody replies in, plus open talk channels.
  - Add the matrix if three or more people write messages, or if missed messages are permanent for a recorded edition.
- **Consistency:** shared quick-reference page, plus a pre-written message bank.
  - Bank templates: stream drop, session delay, track switch, speaker no-show, recording link.
  - Schedule the post-event survey message in advance with its send time written down.
- **Directory:** hand the roster to `event-marketing-plan`'s channel page. Do not publish a second page.
- **Wind-down: decide before the event, publish the date on each channel.**
  - One-off edition: export, then scheduled deletion.
  - Recurring edition with a named owner of a community space: hand off.
  - Otherwise: read-only archive.
  - Never close silently. Retention is counsel's call.

## 7. Captioning and the keynote audio

**Captioning standard.** The bar belongs to `event-accessibility-inclusion`. What follows is that skill's logic applied provisionally, with three inputs still open:
- funding line (Q1)
- access needs already known from earlier editions (Q3)
- a named owner (Q5)

Recommendation, by what the funding answer turns out to be:
- **If a budget line exists:** commit to live human captioning on the keynote and both tracks. Cost and scope depend on Q1.
- **If no budget line exists:**
  - Publish live captioning on request, with a stated lead time.
  - Use an automatic feed only as a labelled fallback.
  - Correct captions on the recordings after the event.
- **Either way:**
  - State exactly which sessions are covered on the accessibility page. Never imply coverage you have not funded.
  - Brief the human captioner ahead with the programme, speaker names, decks and a glossary of product, library and acronym names.
  - Never announce an unvetted automatic feed as captioning coverage. That rung is deleted.
  - Apply WCAG 2.2 AA to the event's own surfaces: site, forms, schedule and player. From my own knowledge, WCAG 2.2 AA includes live captions for live media. Verify that against the sibling's digital-layer checklist.
  - Report to that skill what the platform can and cannot do (vendor question 5).
- Whether captions are legally required depends on jurisdiction. That is a question for counsel.

**Mixing board.** There is no board for a fully remote keynote. A mixer sits inside a room. What makes a remote keynote sound professional:
- the speaker's wired headset or microphone
- a quiet room
- the individual tech check and local backup recording from section 4
- the technical watcher listening to the output

If the keynote speaker presents from the auditorium, the signal path becomes `event-production`'s job. I recommend no board model and no equipment list.
- Hand `event-production` this posture: streamed live; rehearsal plus a dedicated operator are required; a board feed to the recorder; a standalone audio recorder outside the live mix; a monitor on the encode output.
- The board's channel count and model go in the supplier brief, not in this plan.

## 8. Failure drill, rehearsal, budget

- **Fallback line:** publish before the day, on the status page and the schedule page, outside the platform. Draft: "If a stream drops, it is on our side, not yours. Updates appear at `____` and on the announcement channel." The person who will say it live must know it.
- **Rehearsed handoff:** the speaker's connection drops mid-talk, and the moderator's exact opening words are agreed in advance.
  - Also read the other scenarios aloud once: no-show, dead audio, platform incident, conduct incident in chat, takedown for music.
  - Moderators exist, so the published line alone is no longer enough.
- **Warm fallback destination for the keynote:** a second stream target, live and silent (A3).
  - Escalate to a full outage drill on a second platform if Q4 reveals a paid ticket or sponsor deliverable naming the stream.
  - Do not run the second platform with duplicate sessions in parallel.
- **Rehearsal:** the full run on the real platform, with moderators, watchers, host and speakers for the keynote, one week before.
- **Timeline (relative, because no event date was given):**
  1. T–8 weeks: vendor answers in writing, captioning decision, channel roster approved.
  2. T–5 weeks: platform reversal deadline (Q7). If the event is nearer than 5 weeks, compress and tell me.
  3. T–4 to T–3 weeks: group tech check, individual checks, captioner glossary sent.
  4. T–2 weeks: pre-recorded files due, fallback line and channels published.
  5. T–1 week: full rehearsal and handoff drill.
  6. T–1 day: status page live, message bank scheduled.
  7. After the event: recordings go to `event-content-repurposing`, and the consent check goes back to `event-speaker-experience`.
- **Budget split for `event-budget`:** the feed survives every tier. A lean tier drops the interaction surface and its staffing first.
  - The captioning line goes separately, and a sponsor can fund it as a named line. Budget it first.
  - The published cost evidence prices a hybrid's virtual layer, so it does not size this event.

**Gates before the first session**
- Every concurrent track has a named moderator, or its chat is closed.
- Every speaker has joined the real platform at least once.
- The fallback line is published, and the person who will say it live knows the sentence.

**Metrics (self-set; each is a number I'm proposing, not an industry standard).** Record before the event.
- Time from a feed dropping to the audience being told something. If it exceeds your ceiling, add a host.
- Sessions delivered without an audience-visible failure. A session with no audio counts as a failure.
- Speakers who joined a check before the day. If it is low a week out, escalate individual checks.

## 9. Open questions

Q4 and Q6 gate signature. Q7 sets every deadline.

1. Q4: Is there a paid virtual ticket or a sponsor deliverable naming the stream or a virtual booth?
2. Q6: Does procurement or a sponsor contract constrain the platform or where data sits?
3. Q7: What is the last date the platform choice can be reversed?
4. Q3: Where are the speakers and the audience? Does anyone present in the middle of their night?
5. Q11: Which sessions have a live demo or an unknown connection? Is the keynote really unrepeatable? Where will the keynote speaker present from?
6. Q9: How many people can do only production during a session?
7. Q8: One-off or recurring edition?
8. Captioning: is there a funding line, do you know access needs from earlier editions, and who owns accessibility?

Next: reply with answers to 1 and 2, and I'll lock the platform posture and re-rank any rung they change.