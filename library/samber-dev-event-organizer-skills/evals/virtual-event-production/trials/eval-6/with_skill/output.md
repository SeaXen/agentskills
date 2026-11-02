# OpenKernel Days: virtual production plan

## Verdict on the 25 Mbit/s uplink

❌ **Not as planned.** Two separate problems:

- **Capacity.** The only published yardstick I have is FOSDEM's video team. They ask for 10 Mbit/s of outgoing bandwidth per room, and they call 2 Mbit/s a floor that gives up resilience.
  - Five rooms at 10 Mbit/s is 50 Mbit/s, twice your line.
  - Five rooms at the 2 Mbit/s floor is 10 Mbit/s, which fits but has no resilience.
  - My own rule of thumb (unsourced): plan on 60–70% of the uplink you measure under sustained load. On 25 Mbit/s that is about 15–17 Mbit/s, or roughly 3 Mbit/s per room. That is workable for slides plus a talking head, tight for terminal-heavy demos.
  - FOSDEM's 10 Mbit/s is a calibration point, not your requirement. Budget per room, and above the floor.
- **Blast radius.** One home line carrying all five rooms is one point of failure. One ISP hiccup, one family member's video call, or one cloud backup blanks every room at once. That is the silent-failure mode the skill warns about.

Fixes, best first:

1. **Push each room's feed from where its OBS runs.** The room lead's connection carries their own room, so a failure takes out one room. Then the coordinator's line carries nothing but their own work.
2. **If everything must leave from the coordinator's home,** cap each room at about 3 Mbit/s. Wire it with Ethernet, not Wi-Fi. Keep everyone else off the line during sessions.
3. **Send each feed once, to a public video platform.** Never serve viewers from the home line. At 3 Mbit/s per viewer, 25 Mbit/s is about eight viewers. Never send the same session to two platforms in parallel, because the skill deletes that option. It also doubles each OBS's upload.

**Test before trusting any number.** Run all five encoders at once at full bitrate for at least 30 minutes, at the hour of the event, while the household is normally active. A short speed-test burst proves nothing. Watch for dropped frames in OBS and for latency climbing on the line (bufferbloat). Do this on the real platform, on the rehearsal date below.

## Assumption to correct

I could not run the interview one question at a time, so I assumed an answer to Q1. If it is wrong, step 5 changes.

**Interaction posture:** an event people are inside. Five devrooms plus your chat server means open chat in every room.

## Delivery plan

Validate each section before you sign up for anything.

### 1. Platform posture

Your plan is an assembled stack: OBS, a self-run chat server, and a hand-edited static schedule page.

- **Fits:** it is free and reversible until the week before, which suits zero budget.
- **Cost:** your hours and the seams between the parts. The schedule must be edited by hand when a slot moves. Questions land where the speaker isn't looking. Attendees hold two logins if the chat needs an account.
- **Cheaper option:** because you already run a chat server, "one-way feed plus the existing chat space" is the default rung. The assembled stack only adds your own schedule page on top. Don't add anything further.
- **Host the schedule page off the coordinator's home line.** It is the fallback destination (see section 5). It must survive the line failing.
- **Questions to put in writing to the video platform before committing:**
  - May one account run five simultaneous live streams?
  - Is there a lead time or verification step to enable live streaming?
  - Is there a viewer ceiling?
  - Does restarting a stream change its address?
  - What does the player do on a weak connection?
  - What are the music takedown rules?
  - Who can record and delete a recording afterwards?
- **Chat server questions for you:**
  - Can moderators delete a message, remove a person and lock a room mid-session?
  - Where is the history kept, and can you delete it on request?
  - Can you export a member list before closing?
  - Can it handle the concurrent load you expect? Where does it run? If on the coordinator's line, it competes with the feeds.
- **Compliance:** the chat holds attendee identity. Take data-location and retention questions to your own counsel.

### 2. Remote-speaker readiness

- **Default:** send a written home-setup note with the join link, the day acceptances go out.
  - Wired connection.
  - Wired headset.
  - Close background syncing.
  - Single window share.
  - Recorded fallback of any demo.
  - No background music.
- **Promote to an individual tech check plus an instructed local backup recording** for any speaker who has:
  - an unrepeatable session,
  - a live demo, or
  - an unknown or poor connection.
- **Run all checks on the real platform,** through the same route an attendee or speaker uses. A check on any other tool is deleted from the menu.
- **Time zones:** ask where each speaker is before the grid is fixed. A slot in someone's middle of the night is a pre-record candidate (recorded talk, speaker live in chat). An online community spread across time zones makes this likely.
- **Consent:** any local backup creates a file. Get it covered by the speaker consent record before it exists. Hand the results to the speaker-experience skill.

### 3. Moderation staffing

Five parallel rooms with open chat is a staffing problem before it is a technical one.

- **Default: one named moderator per room. That is five people per session-hour, by name, not "the volunteers".**
- **Add a technical watcher** (second person, watching the stream as a viewer would) for any unrepeatable session or live demo. Also add one if a past edition lost a feed unnoticed.
- **If you cannot name five moderators for a slot, close that room's chat for that slot,** or drop to the single one-way feed. An open space with nobody on duty is a conduct obligation with no responder, and the skill ranks it the worst on compliance.
- **Never have the speaker moderate their own chat.** That option is deleted.
- **Publish the code-of-conduct warning and the incident path.** A digital space raises harassment risk. Keep one organizer-only coordination channel, separate from every attendee channel.
- **Question relay:** decide per speaker. The default is that the moderator reads questions aloud at agreed points. Agree who calls "out of time" and where unanswered questions go.

### 4. Captions and accessibility

- Ask the accessibility skill's owner what bar is required.
- Report back what your video platform and chat server can and cannot do. Don't set the bar yourself.

### 5. Failure drill and fallback line

- **Publish one sentence before the day,** on the schedule page and in the chat topic. It names where to look when a feed dies.
  - Example: "If a stream drops, it's on our side; updates will appear here and on the schedule page."
  - Name a destination and a time, never just "technical issues".
- **Rehearse one scenario with real words:** the speaker's connection drops mid-talk.
  1. The watcher or moderator notices.
  2. The moderator posts the agreed line immediately.
  3. Repeat where to look.
  4. The speaker rejoins by the same link, or you announce a decision on what happens to the session.
  5. Say when it's fixed.
- **Also read aloud once:**
  - the speaker never appears,
  - the audio is dead while the stream looks fine,
  - the platform itself has an incident,
  - a conduct incident during a live session,
  - a takedown for music in a demo.
- **A warm standby stream is probably unaffordable** on this uplink. A silent stream still needs an encoder and ingest bandwidth (my inference, not sourced). Skip it unless a feed has died before (Q10).
- **Delete the contingency document nobody has read aloud.**

### 6. Rehearsal

Rehearse once, on the real platform, with all five rooms live at the same time and every moderator in place. This is the step that gets cut. It is also the one that tests your uplink claim.

### 7. Cost split for the budget (no cash, so hours)

- **Survives every tier:** the feeds.
- **Goes first when lean:** the interaction surface and its staffing. That is the tier-order the skill gives, and for you it means closing chat in rooms you can't staff.

## What else you are probably underestimating

1. **Moderator hours.** Five rooms times the number of session-hours, for two days. That is the biggest hidden cost, and it is volunteer fatigue as much as headcount. Ask Q9: how many people can do only production during a session, and who is free the week after?
2. **The hand-edited schedule.** One person editing a static page while slots shift across five rooms is a seam. If it is also the fallback destination and the coordinator is busy firefighting, it goes stale exactly when needed.
3. **Where the OBS machines run.** Five OBS instances encoding on one computer is a CPU problem too. If room leads run their own, check each lead's connection, not only the coordinator's.
4. **Your chat server's load and location.** It was fine for a community; five rooms of live conversation is a different load. If it sits behind the same home line, the chat suffers when the feeds eat the uplink.
5. **Music takedowns.** A demo with incidental music can get a stream pulled mid-session. Warn speakers before the day.
6. **Consent surprises.** Local backups, and any attendee on camera in a Q&A, sit outside what a talk's consent covered unless collected that way.
7. **Attendance guesswork.** Published conference data goes both directions when moving online (PyCon US fell about 22%, KubeCon NA nearly doubled). Plan from your own signals, not from either default.

## Questions I couldn't ask

Each of these flips something above:

1. Is chat open, or is this a feed people watch? (Decides whether section 3 exists.)
2. How long is the shortest gap between sessions?
3. Where are speakers and audience? Does anyone present in their night?
4. Did you promise anything to sponsors or ticket buyers?
5. What is the consent posture per session, and where is the record held?
6. Does anything constrain the platform or data location?
7. What is the last date the platform choice can still be reversed?
8. One edition, or recurring? Recurring promotes rehearsed crew and reusable notes.
9. How many people can do only production during a session?
10. Did a past edition lose a feed?
11. Which sessions cannot be re-run, carry a live demo, or have a speaker with an unknown connection?

## Gates before the first session

- Every concurrent session has a named moderator, or its interaction surface is closed.
- Every speaker joined the real platform at least once.
- The fallback line is published, and whoever says it aloud knows the sentence.

## Metrics to set (self-set, not industry standards)

Pick two or three and record them before the event:

- Time from a feed dropping to the audience being told.
- Sessions delivered without an audible or visible failure, over sessions scheduled.
- Speakers who joined a check before the day, over speakers scheduled.

## After the event

Hand captured sessions to content repurposing. Hand the recording consent check back to speaker experience.

*Source note:* the 10 Mbit/s and 2 Mbit/s figures come from FOSDEM's published video-team requirement via the skill's reference. The 60–70% headroom and the warm-standby bandwidth point are my own general reasoning.