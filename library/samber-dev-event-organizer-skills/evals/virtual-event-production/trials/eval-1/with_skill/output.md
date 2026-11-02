# Northwind DevCon virtual delivery plan

**Recommendation:** don't sign the $9,000 quote. Run a one-way public video feed plus your existing Discord. Add no new platform, which means nothing to sign and nothing to lose by waiting.

I read the skill and its three reference files. The skill asks for a one-question-at-a-time interview, but you asked for the full answer in one go. So I filled in what you already told me, marked what I assumed, and listed the open questions at the end. Each one could change a rung.

## 1. Interaction posture

> An event people are inside, but small: one track, one session at a time, with conversation happening in the Discord you already have.

I assume this because your 2,400-member Discord is active weekly. If you want a broadcast with comments closed, see the fallback rung below.

## 2. Platform posture: one-way feed plus existing chat space

**What you told me:**
- Single track, so one session at a time.
- Free event.
- No sponsor deliverable names the stream.
- No platform has been imposed on you.
- A chat space already exists with an audience in it.

**Why the $9,000 platform fails the test:** the managed virtual-venue rung is promoted only by one of three conditions. You meet none of them.

| Promotion condition | Your situation |
|---|---|
| Several sessions at once, with attendees moving between them | One track. Nothing to move between. |
| A sponsor deliverable naming a virtual booth, or a directory sold as a ticket benefit | No sponsors, free ticket. |
| A procurement or sponsor constraint with no alternative | None. |

The quote buys three things:
- **Breakout rooms.** Nothing to break out from on a single track. They also put attendee faces on camera, which your speakers' consent forms don't cover. You can't collect that consent afterwards.
- **An expo area.** You have no sponsors to fill it.
- **An attendee directory.** It triggers a data-handling review before you sign, and the skill treats a list a sponsor has exported as impossible to recall.

The skill's warning on this ("buying interaction nobody uses") fits your case. These features cost procurement time, setup hours and a compliance review whether or not anyone opens them.

**Reversibility:** the feed plus Discord can be abandoned the week before the event at the cost of an announcement. The managed platform usually can't be, and "sign this week" is a long way from the event. Signing early buys nothing you can't get by waiting.

**Drop to a single one-way feed with comments closed if** nobody on your crew can watch Discord during sessions. An open space in the event's name with no responder is a code-of-conduct obligation with no one to answer it. The skill treats that as worse than having no chat.

**Check the Discord against four things:**
1. Is voice free?
2. Do attendees already have accounts? Your ~600 registrants may not all be members.
3. Does the free tier keep history?
4. Can you export the member list before you close the space?

**Network:** budget the uplink for your single room. The FOSDEM figure is 10 Mbit/s outgoing per room, and 2 Mbit/s is a floor that sacrifices resilience.

**If you still talk to any vendor, get answers in writing first** (from `platform-selection-and-vendor-questions.md`):
- **Delivery:** poor-connection behaviour, whether a viewer needs an account, the concurrent-viewer ceiling and what happens at it, and whether a restart changes the stream address.
- **Speakers:** screen-share, second-screen and system-audio limits.
- **Moderation:** can a moderator delete, remove and lock mid-session?
- **Accessibility:** what captions exist, and can an external captioner feed in?
- **Data (questions 13–16):** where attendee data is stored, what a booth or directory exports to sponsors, how long chat is retained, and whether any room records attendees on camera. Take these to your own counsel.

## 3. Remote-speaker readiness

- **Default:** send the written home-setup note with the join link, the same day you confirm each speaker. The note covers wired connection, wired headset, closing background sync, camera at eye level, a single shared window, and no background music.
- **Move up to an individual tech check plus a local backup recording** for any speaker who has never presented on your streaming tool, has an unknown connection, has a live demo, or has an unrepeatable slot. That is likely several of your 8, and I can't tell which from here.
- **Consent:** get any local backup recording covered by the speaker consent record before the file exists.
- **Run the tech check on the real streaming tool.** A check on another tool is deleted from the menu because it tests nothing that matters.
- **Time zones:** put each speaker's own local time in the first line of the note. A slot in someone's middle of the night is either moved or pre-recorded with the speaker live in chat.
- **Live demos:** ask for a recorded fallback and say so up front.

## 4. Moderation staffing (single track)

Because Discord is open, a named person has to watch it.

- **Floor:** one named moderator for the whole day. With one track this is also the "per concurrent session" default. The moderator reads chat, relays questions to the speaker and holds conduct. The speaker never moderates their own chat.
- **Add a technical watcher** (a second named person) if any session is unrepeatable, or if a previous edition lost a feed unnoticed. The watcher watches the output as an audience member does, on a second device, and does not read chat.
- **Add a host on the feed** only if you sell a paid ticket or have a sponsor deliverable naming the stream, if there are long gaps to fill, or if the audience has no other way to learn what is happening. At the moment none of these applies.

Everyone involved needs a name, not a function.

## 5. Failure drill and fallback line

- **Publish one fallback line before the day**, where the audience will already look. For example: "If the stream drops, it's on our side. Updates go on the schedule page and in #announcements." Point it somewhere outside the streaming platform.
- Since a moderator exists, **move up to a rehearsed handoff** for the likeliest failure, a speaker's connection dropping mid-talk. Agree the moderator's exact words and rehearse once, with the moderator, the speaker and whoever is on air.
- The sequence is notice, say it immediately, point somewhere, recover or reschedule, then say when it's fixed.
- A standing warm fallback stream or a full outage drill is not recommended for a free, one-day, single-track event. Revisit it if you promise refunds, a sponsor names the stream, or an earlier feed died.

## 6. Rehearsal

Hold one rehearsal on the actual streaming tool and the actual Discord, with every speaker joining at least once before the day. I don't know your event date, so schedule it once you confirm. Leave enough time before the event to fix what it finds. A rehearsal on any other tool tests nothing.

## 7. Cost consequence for the budget

Hand this split to `event-budget`:
- **The feed survives every tier.** It is a public video platform plus uplink.
- **Interaction and its staffing go first** in any lean tier.
- **Recurring cost:** the $9,000/year quote is a yearly commitment. The lean approach carries about zero platform spend. Your real cost is organiser hours and the moderator roster.
- **Don't copy outside numbers.** Published cost figures price a hybrid event's virtual layer, not a standalone virtual event. Plan capacity from your own signals. 600 registered is a signal, but attendance can move either way once an event goes virtual.

## 8. Measurement

All of these are self-set, not industry standards. Pick two or three and write down what change each would trigger.

- **Pre-event gates:**
  - every session has a named moderator;
  - every speaker joined the real platform once;
  - the fallback line is published and the person who'll say it knows the sentence.
- **Sessions delivered without an audience-visible failure**, out of 8. A session with no audio counts as a failure.
- **Time from a feed drop to the audience being told something.**
- **Questions relayed against questions asked.**
- **Speakers who joined a check before the day.**

## What to do this week

1. Reply to the vendor that you're not signing this week. Keep the quote only as a fallback if a sponsor or an organiser changes the answers below.
2. Confirm the posture and the Discord check above.
3. Name the moderator, and the technical watcher if the answers below call for one.
4. Send the speaker note and the fallback line text.

## Open questions

The recommendation holds under any of these answers except where noted.

1. **Is there a live interaction surface, or a feed people watch?** I assumed Discord. A "feed only" answer drops the moderation menu entirely.
2. **Where are the speakers and the audience?** A spread wide enough that someone presents in the middle of their night promotes pre-recording for that slot.
3. **What is the consent posture per session, and where is the record held?** This decides what you may record or publish.
4. **What is the last date a platform choice can be reversed?** I assumed your deadline is this week, with the event date later.
5. **Is this a one-off or a recurring event?** If it recurs, warm fallback paths and a rehearsed crew are worth more.
6. **How many people can do only production during a session, and who is free the week after?** If nobody can watch Discord live, drop to the comments-closed feed.
7. **Which sessions can't be re-run, which carry live demos, and which speakers have unknown connections?** This decides speaker readiness, the technical watcher, and whether any session is pre-recorded.
8. **Did a previous edition's feed die, or is a platform already paid for by someone?** This could promote a heavier drill.

One more point: nothing about this plan is a legal reading. Data duty, platform terms and retention differ by country, so take questions 13–16 above to your own counsel.