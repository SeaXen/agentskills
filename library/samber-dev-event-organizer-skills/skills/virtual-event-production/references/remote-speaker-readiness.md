# Remote speaker readiness

Contents: the home-setup note · the tech-check script · instructing a local backup recording · the time-zone rule · a negative and a positive speaker briefing.

The setup note, the tech-check script and both briefings are constructed guidance, not a record of any event's practice. Only the two sources named inline, the DevOpsDays music warning and ICFP 2020's walkthrough timing, describe what a real event did.

The speaker relationship itself - the acceptance, the deadline ladder, the single named point of contact, the recording consent record - belongs to `samber/dev-event-organizer-skills@event-speaker-experience`. Send the material below through that skill's existing contact rather than opening a second correspondence with the same person.

## The home-setup note

Send it with the join link, in the same message. It is the default rung on Menu 2 because it is asynchronous, reusable next edition, and costs the speaker minutes rather than a scheduled call. Keep it short enough that it gets read.

**Connection**

- Prefer a wired connection to the router over wireless. If wireless is the only option, sit in the same room as the router.
- Close anything syncing in the background - file sync, backups, updates, another device streaming video in the same household.
- If the connection is shared with other people, tell them the hour.
- Have a phone with a mobile connection nearby as a fallback path, not as the plan.

**Audio, which decides whether the talk is watchable**

- Wired headphones with a microphone beat a laptop's built-in microphone, and beat wireless earbuds that may drop or switch devices mid-sentence.
- Speak in the quietest room available, with the door shut. Soft furnishings help more than equipment does.
- Mute notifications at the operating-system level, not only in the application.

**Video**

- Put the camera at eye level. A laptop on a stack of books is the whole intervention.
- Put the light in front of the face, never behind it. A window behind you makes a silhouette.
- Check what is visible behind you, and whether you want it visible.

**Slides and demos**

- Share a single window or a single screen, decided in advance, not the whole desktop.
- Close every application not needed for the talk before joining, including chat clients that pop up messages.
- A live demo depending on a network call is the single most fragile thing in a remote talk. Have a recorded fallback of the demo, and say so up front rather than discovering it live.
- No background music in anything shared. This is a platform risk rather than a stylistic note: incidental music in a stream can get the stream taken down by the platform itself (DevOpsDays organizing guide).

## The tech-check script

Run the check on the platform the event actually runs on. A check on any other tool is deleted rather than demoted in Menu 2, because it tests nothing that matters.

In order, and confirm each out loud before moving on:

1. The speaker joins by the same link and the same route an attendee or a speaker will use on the day - no organizer shortcut, no pre-authorized session.
2. Audio in both directions. The moderator confirms what the speaker sounds like, in words, rather than watching a level meter.
3. Screen share, with the actual deck, including the transition into and out of a demo.
4. Whatever the talk does that is unusual: system audio, a second screen, a video clip, a hardware device, a terminal at a readable font size.
5. Where questions will appear, and whether the speaker will see them or a moderator will read them aloud. Decide this per speaker, not per event - some presenters cannot read and talk at once.
6. What the speaker does if they lose the connection: rejoin by the same link, and the moderator's agreed words while they are gone.
7. The local backup recording, below.

A group check runs the same script once with everyone present. Its saving is real: platform-wide problems surface once instead of per speaker. Its cost is that step 4 gets skipped for the quiet speaker who did not want to hold up the group. Ask each person by name.

A real precedent for the timing: ICFP 2020 ran its platform walkthroughs in the two weeks before the conference - for attendees and student volunteers rather than speakers specifically, but the reasoning transfers. Early enough that a platform problem is still fixable; not so early that what was learned is forgotten by the day.

## Instructing a local backup recording

The point of a local recording is that it does not travel over the connection that is failing. It is the difference between a dropped feed costing the live session and costing the talk.

- The speaker starts a local recording on their own machine before the session and stops it after. Give the exact steps for the platform in use, in the note, rather than telling them to figure it out.
- Local means local: a recording that uploads while the talk runs is competing for the same uplink and is not a backup.
- Tell the speaker where to send the file and by when, in the same sentence as the instruction. A backup nobody collected is not one.
- **It does not cover audience-facing failure.** A local recording produces a talk after the fact; it does nothing for the people watching in the minute the feed dies. That is Menu 4's job, and the two are not substitutes.
- **It creates a file, and a file changes the consent question.** Get the recording covered by `samber/dev-event-organizer-skills@event-speaker-experience`'s consent record before the file exists. A recording made as insurance is not automatically a recording anyone agreed to publish.

## The time-zone rule

Ask where each speaker is before the grid is fixed, and report an impossible slot upward rather than solving it locally.

- A speaker presenting in the middle of their own night is a no-show risk and a quality risk at once, and no amount of readiness preparation fixes either.
- The two real answers are moving the slot, which belongs to `samber/dev-event-organizer-skills@event-schedule-design`, or promoting that speaker to the pre-recorded rung with the speaker live in chat.
- The same question applies to the audience. A programme built where the organizers live silently excludes the half of a distributed community that is asleep.

## A negative and a positive briefing

**Negative, a constructed example.** "Hi! Here's your link for Thursday. We'll do a quick tech check beforehand - I'll send a separate invite. Any questions, let me know!"

Everything wrong with it is wrong in the same way: nothing is actionable before the call.

- The speaker arrives at the check having changed nothing, so the check becomes the setup session.
- The demo dependency is never surfaced.
- Nothing says what happens if the connection drops.
- The phrase "a quick tech check" names no tool, which is how a check ends up running on whatever the organizer had open.

**Positive, the same briefing rewritten.** "Your session is Thursday at 14:00 UTC - that's 09:00 for you in Boston; tell me now if that's wrong. Join link below; it's the same link on the day, and it's the platform we'll run the whole event on. Before Tuesday, please read the setup note attached - the three things that matter most are a wired connection, wired headphones rather than laptop audio, and closing anything syncing in the background. Tuesday's check is a short slot with me on this same link: we'll test your screen share with your actual deck, run the demo once, and agree what I say to the audience if you drop. I'll also walk you through starting a local recording on your own machine - it's insurance, so a dropped connection costs the live session and not your talk. If you'd rather not be recorded locally, say so and we'll skip it; your consent form covers the session recording only."

What the second version does:

- it makes the check testable rather than introductory
- it surfaces the demo before the day
- it names the failure plan in advance
- it ties the recording to a consent posture the speaker can refuse
- it puts the speaker's own local time in the first line

The speaker's own local time is the cheapest item on that list, and the easiest one to leave out.
