# Moderation roles and failure drills

Contents: what each moderation role does minute to minute · the question-relay mechanic · the failure-drill runbook · the scenarios worth rehearsing · a negative and a positive outage response.

The channel architecture and the standing cost of keeping a space open belong to `samber/dev-event-organizer-skills@event-comms-channels`; the incident-reporting path belongs to `samber/dev-event-organizer-skills@event-code-of-conduct`. Neither is redesigned here. This file covers only the live, in-session layer.

## What each role does minute to minute

**The session moderator.** One named person per stream that is live at the same time.

- **Before the session:** confirms the speaker joined, posts the session's opening message, states where questions go.
- **During:** reads chat continuously, selects and relays questions, watches for conduct problems and acts on them, and posts the one line that tells people what is happening whenever anything is not normal.
- **After:** closes the question surface, posts where the recording will appear if one exists. Where recordings publish asynchronously rather than live, this includes a code-of-conduct review pass on each one before release, not only on the live space - the Python Software Foundation staffed exactly this when PyCon US converted to virtual in 2020, reviewing every recorded talk and tutorial before it went up.

The moderator is the person answerable for conduct inside the space. That duty is not delegable to the speaker and does not pause because a talk is interesting. The Major League Hacking organizer guide is explicit that a digital space raises the risk rather than lowering it: "Digital spaces can increase harassment as people are hidden behind a computer, so it is key to make sure your attendees know you still take this seriously".

**The technical watcher.** A second person per session whose only job is whether the output is up, audible and in sync - watching it the way an audience member does, from outside the production path, on a second device. Not a producer, not a moderator, not also doing something else.

The pattern behind the role is a physical event's livestream needing "at least one person to run it during the event" (DevOpsDays organizing guide). What does not carry across is the equipment, since there is no board to run and nothing to mix. What transfers is the single-point-of-ownership discipline.

The watcher's one non-obvious value is diagnostic: without somebody watching the actual output, nobody finds out the audio has been dead since the second slide, because everyone inside the production path hears the source rather than the stream.

**The host on the feed.** A person who speaks, on air, between and during sessions: introduces the speaker, fills a gap, and - the reason the role exists - says out loud what has happened when something breaks. Every rung below leaves the audience to infer a failure from silence.

## The question-relay mechanic

Decide per speaker, at the tech check, not per event:

- **Speaker reads their own questions.** Works only for a presenter who can read and talk at once, and only when a moderator is still holding conduct in the same space. Never make this the moderation plan; it is a preference about who reads, not a staffing rung.
- **Moderator reads questions aloud at agreed points.** The default. The moderator batches, drops duplicates, rewrites a hostile question into a real one or drops it, and holds the queue to the time the speaker agreed.
- **Moderator posts selected questions into a private channel the speaker watches.** Useful when a talk has natural pauses and the speaker prefers reading to being interrupted.

Whichever is chosen, agree the ending: who says "we're out of time", and where unanswered questions go. Questions that vanish unanswered are a routine complaint, and free to fix.

A fourth shape sits at the event level rather than the per-speaker level. It trades against the concurrent programme rather than against the speaker's own time.

ICFP 2020, an ACM conference, streamed every talk pre-recorded on schedule and opened a separate live video room for that talk's Q&A immediately after, running in parallel with whatever streamed next. Its own post-conference survey measured the trade rather than assuming it: 37% of respondents were very happy with the arrangement, 24% found it acceptable, and 10% would have preferred something else. The most common complaint on record was being forced to choose between the next talk and staying for questions.

A parallel Q&A room buys depth of discussion, and spends a piece of whatever the audience would otherwise watch next. Decide that trade on purpose rather than discovering it live.

## Failure-drill runbook

A drill is a rehearsal with words agreed in advance, not a document. The delete-don't-demote rule in Menu 4 exists for exactly the artifact this section is at risk of becoming: a contingency file nobody has read aloud.

Run one dry run of the single likeliest failure - the speaker's connection dropping mid-talk - with the moderator, the speaker, and whoever else will be live. It takes one short session and it is the highest-value preparation on the menu.

The sequence to rehearse:

1. **Notice.** Who declares it. If a technical watcher exists, they do; otherwise the moderator does, and the drill is about the moderator noticing while also reading chat.
2. **Say it, immediately.** The moderator posts the agreed opening line in the space, and the host says it on the feed if a host exists. Speed matters more than accuracy here: every attendee's first hypothesis is that the problem is on their end, and the only thing that removes that is somebody else saying it is not.
3. **Point somewhere.** The fallback line published before the day names where the audience should look. Repeat it now rather than assuming they remember it.
4. **Recover or reschedule.** The speaker rejoins by the same link. If the connection is gone rather than dropped, say what happens to the session - moved later in the day, replaced, or cancelled - and say it as a decision rather than as a hope.
5. **Close the loop.** When it is fixed, say that too. A stream that quietly resumes leaves the people who left not knowing they can come back.

## Scenarios worth rehearsing, in order

Rehearse the first. Write down the rest and read them aloud once with the people who would act on them.

- The speaker's connection drops mid-talk. The most likely by a distance, and the one the drill exists for.
- The speaker never appears. ACM's governing-board minutes record no-shows for remote presentations at conferences - this is not a hypothetical. Agree in advance what fills the slot.
- The stream is up and the audio is dead. Sounds unlikely and happens constantly, because the production path hears the source and not the output.
- The platform itself has an incident. Nothing you rehearse fixes it; what you rehearse is where you tell people to go, which is why the fallback line lives outside the platform.
- A conduct incident in chat during a live session. The moderator acts under `samber/dev-event-organizer-skills@event-code-of-conduct`'s path; what needs rehearsing here is only that the session does not stop while it happens, and that the moderator is not also the speaker.
- A stream taken down by the platform for incidental background music in a demo. A named risk in the DevOpsDays organizing guide. The fix is upstream, in the speaker briefing, because there is no fix downstream that lands in time.

## A negative and a positive outage response

**Negative.** The keynote's feed dies. The chat fills with people asking whether it is just them. An organizer sees it long afterwards and posts "sorry, technical issues, we're looking into it!"

Nothing else is said for the rest of the session. The talk is quietly rescheduled to a slot announced only in the chat, which the people who left are no longer reading.

What went wrong is not the outage:

- the audience spent minutes debugging their own equipment
- the message named no destination and no time
- the recovery was announced in the one place the departed audience could not see

**Positive.** The feed dies. The technical watcher says so in the organizer channel within seconds. The moderator posts the agreed line - "the stream has dropped on our side, not yours; we're on it, and updates will appear here and on the schedule page" - and the host says the same sentence on whatever is still live.

The published fallback line already pointed at the schedule page, so the people who left know where to look. The speaker rejoins by the same link. The moderator posts that the session is resuming, and posts once more when it has, and the schedule page carries the same two updates for anyone arriving late.

The difference is entirely in the first minute, and it costs one rehearsed sentence and one destination decided before the day.
