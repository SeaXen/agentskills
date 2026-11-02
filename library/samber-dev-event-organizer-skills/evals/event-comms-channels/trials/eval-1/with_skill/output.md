# PyForge Day: comms channel plan (draft for committee approval)

## Decision

❌ **Do not buy the EventPulse app ($4,800).** ✅ Use the registration email list plus on-site announcements. Add a status page or a chat space only if the open questions in section 6 call for one.

Nothing has been created. Each section below needs your approval before anyone opens a channel.

## Assumptions

You answered only part of the skill's interview, so I filled the gaps. Say which are wrong, and I'll re-rank.

- ℹ️ **Scale:** 1 day, 2 rooms, about 500 people, in person, no livestream or recording. This sits between the skill's two reference scales: one room with one writer needs a list only, while three rooms with five writers needs a routing rule. I assume about 3 to 5 volunteer writers, some new to this event.
- ℹ️ **Existing channels:** only the registration email list. No contract forces an app (no sponsor deliverable, no venue system).
- ⚠️ **No register yet.** The skill executes a voice and never sets one. If PyForge Day has no tone-of-voice document, run `event-cultural-identity` first. Treat the wording below as provisional until then.
- ⚠️ **Unknown:** one-off or recurring event, what can break out of attendees' sight (Q9), and who is on duty the week after.

## 1. Why not the app

| Committee belief | What the analysis shows |
|---|---|
| "80% of attendees install it" | No adoption figure exists for community-run technical events, so don't accept the vendor's. Ask EventPulse for 3 named comparable events and the definition of "install": installed, opened, or opted in to push. Events where check-in or badges require the app would inflate the number. |
| "Push is perfect for announcements" | Push reaches only people who installed the app and allowed notifications. The email list reaches every registrant by construction. Even at 80%, 100 people still need the email, so you would staff two channels and send each message twice. |
| "We need a way to announce things" | Your schedule is locked a month out and basically never changes, so the main thing an app is good for barely applies. |
| "We can launch the app to attendees" | The only audience you own is the email list. Promoting the app means emailing everyone first, so the list is the channel the app depends on. |

**Where the app ranks.** The skill ranks the event app last on efficiency. It is worth promoting only if one of these is true:

- A signed commitment forces one.
- You have 3 or more concurrent rooms with a grid that changes more than once a day.
- You already own an app and have sunk content cost.

You have none of these. You have 2 rooms and a locked grid.

**Cost.** $4,800 is about $9.60 per registrant for a channel that adds standing work and reaches a subset of attendees.

**Where push would help.** Push beats email only for a same-day change that affects people who aren't in the building yet. Your fixed venue and locked schedule make that rare. If the committee fears it, the cheaper fix is a broadcast-only chat channel (see section 6), not an app.

**If the committee still wants an app,** judge it on three criteria:

- Who is forced to install it.
- Whether the schedule updates without an app-store release.
- Whether it works with no connectivity in the room.

Re-open the decision only if one of the three promotion conditions above becomes true.

## 2. Channel roster

Each channel has one job and one named owner. Names are placeholders for the committee to fill in.

| Channel | Job | Owner | Opens |
|---|---|---|---|
| **Announcement list** (existing) | Reach every registrant before the event, and on the day for anything that isn't urgent. | Name needed | Exists |
| **On-site surfaces:** PA call, plus a live schedule-change screen or sheet at each room door and the registration desk | Anything happening now, for people in the building. | Name needed (volunteer on duty) | Event morning |
| **Channel directory page** (owned by `event-marketing-plan`) | Say what each channel is and is not for. | Marketing-plan owner | When the schedule locks (D-30) |
| **Status page**, conditional | One canonical page for a disruption. | Name needed | Only if Q9 names a risk (see section 6) |
| **Chat space**, conditional | Two-way talk among attendees. | Name needed | Only if attendees need to reach each other (see section 6) |

- **Deleted:** a second chat platform running the same job in parallel.
- **Out of scope:** incident reporting belongs to `event-code-of-conduct`. Staff coordination belongs to `event-run-of-show` and never goes on an attendee channel.

**Hand-off to `event-marketing-plan`.** Give that skill's channel directory the roster above rather than a second page. Each channel gets these five lines:

- Name.
- One-line job.
- Who answers.
- Hours watched.
- What it is not for, plus the right channel.

**Reply address.** The list needs a monitored reply-to address named in the directory. Otherwise questions land in personal DMs.

## 3. Routing: which announcements go where

The writers can't ask anyone mid-event, so keep this table small. Put it where they work, for example pinned in the volunteers' coordination channel and printed at the registration desk.

| Class | First channel | Also | Never |
|---|---|---|---|
| **Pre-event practical** (directions, what to bring, doors) | Email | Directory link inside the email | Social only |
| **Programme news** (schedule published, speaker added) | Email | Public broadcast (owned by `event-social-media`) | n/a |
| **Day logistics** (lunch open, badge desk closes, last call) | Door screens or sheets and PA | n/a | Email, which is hours-scale for a minutes-scale message |
| **Live change** (talk 20 minutes late, room swap) | PA if the session is in progress, plus the screen at that room's door | Screens at the registration desk | Email only |
| **Disruption** (venue change, room closed) | Email, plus the status page if one exists | Public broadcast, PA, screens | Chat only, because affected people may not be in the building |
| **Sponsor and partner** | Email, batched | n/a | One message per sponsor on any urgent surface |
| **Incident statement** | Whoever `event-code-of-conduct` names as the single publisher | n/a | Anyone else, on any channel |
| **Wind-down** | Every channel being closed, plus email | n/a | One channel only |

There is no "social / community" row because you have no open channel. If you add chat in section 6, that class goes there.

**Rule across the table.** A minutes-scale message never rides an hours-scale channel. An hours-scale message never rides the disruption path.

**Escalation tiers.** All intervals are self-set. The committee sets the numbers before the event.

- **Tier 0:** the message goes on its first channel.
- **Tier 1:** if a live change affects a session already in progress, go to PA and the door screen immediately, with no wait.
- **Tier 2:** if a disruption is unresolved after `[N]` minutes, repeat on the status page or email with a timestamp, even if there is no news ("next update by `[time]`").
- **Tier 3:** if a disruption changes whether or where people should travel, use the widest-reach channel you have, with no cost limit. For you that is email plus public broadcast, plus chat or the status page if they exist.

## 4. Consistency across volunteer writers

- **Take:** a pre-written message bank, plus a **timestamped day script**. The script covers the predictable nudges: "doors open", "lunch ready", "starting in 3 minutes", "last call". No one has to compose and send at a set hour while also running the event.
- **Skip:** editorial sign-off. It is too slow for a live day, and nothing here requires it because there is no recording, press coverage, or verbatim sponsor wording.
- **Name an owner per channel:** the list, and the on-site surfaces. The public social account belongs to `event-social-media`.
- **No channel-local voice.** One register, set by `event-cultural-identity`.

**Bank field sets.** These are field sets and not finished copy. Rewrite them in the event's voice, keep every field, and run a humanizer pass. Put the new fact before any apology, and always give a next-update time when the situation is unresolved.

1. **Delay:** "[Session] in [room] now starts at [time], about [n] minutes late. Nothing else on the schedule moves. Next update by [time] if that changes."
2. **Room change:** "[Session] has moved from [old room] to [new room], starting [time]. Signs are up at [old room]. If you are already seated in [old room], you have [n] minutes."
3. **Venue change:** "Read this before you travel. PyForge Day on [date] is now at [address], not [old address]. [Transport note.] Doors from [time]. Full details and updates: [URL]."
4. **Session cancelled:** "[Session] at [time] is cancelled. [One-line reason, without naming a person.] [Replacement, or 'the room is open for the hallway track'.]"
5. **Lost property:** "Found: [item, described without anything identifying]. Claim it at [location] until [time]. After that it goes to [venue lost property / an organizer's bag]."
6. **Last call:** "[Thing] closes in [n] minutes at [location]. After that, [what happens instead]."
7. **Closing and wind-down notice:** "That's a wrap on PyForge Day. [One line of thanks.] Recordings go up by [date]. This channel [stays open read-only / closes on date / moves to X]. See [link]."

I left out the livestream template because you have no livestream.

## 5. Digital-space code of conduct and wind-down

**Code of conduct.** It binds every channel, and a conditional chat space or status page is no exception.

- State the code of conduct at the join point of any chat space.
- Name someone on duty to act on reports from it.
- Confirm with `event-code-of-conduct` that its reporting path covers every channel in the roster. I have not written that path.

**Wind-down (decide now, publish the date on the channels).** The right rung depends on whether PyForge Day is a one-off or a series, and that is still unanswered.

| Channel | One-off | Recurring series |
|---|---|---|
| **Email list** | Owned by `event-attendee-email-sequences`, including consent and retention. | Same. |
| **On-site surfaces** | Nothing to close. | Same. |
| **Status page or chat** (if opened) | Export plus scheduled deletion on a published date, after you ask your own counsel about lawful basis and retention. | Read-only archive. Hand off to a community space only if a named person has committed to run it. |

- **Counsel questions.** The skill supplies a list for your counsel (lawful basis, retention, re-consent, platform export terms, post-event moderation duty, minors). I name no jurisdiction and no retention period.
- **Never wind down silently.** Announce the closing at least a week ahead, on the channel itself.
- **Confirm completion.** Check that every opened channel has a closed state and a date, and mark that gate pass or fail.

## 6. Open questions that would change this

I'd ask these one at a time, so reply with just the answers.

1. **Do attendees need to reach each other, or do you want a hallway-track space?** Yes means opening the chat space. Without chat there is nowhere for community messages to go.
2. **Is there anything attendees can't see for themselves?** Examples are a single entrance, shuttles, or a venue that could change. Yes means adding the status page, with a push (email or broadcast) pointing at it. An empty answer means deleting it, since a page that always says "all fine" trains people to ignore it.
3. **Is PyForge Day a one-off or a series?** This turns the wind-down choice in section 5.
4. **How many people write, how many are new to it, and who is on duty the week after?** This sets the owners, and whether chat is affordable at all.
5. **Does a tone-of-voice document exist?** If not, run `event-cultural-identity` first.
6. **Is there a hard date by which comms must be live?**

## 7. Measures (all thresholds self-set)

Fix these before the event.

- **Repeat rate:** the share of messages re-sent on a second channel because the first missed. Ceiling `[set a number]`.
- **Unrouted questions:** questions that arrived with no owner, such as a DM or a speaker's inbox. Count them and note where they landed. That shows a missing channel or directory line.
- **Channel silence:** any channel with no organizer post for a period you fix in advance becomes a deletion candidate next edition.
- **Wind-down completion** (pass or fail): every opened channel has a closed state and a date, on the day it was scheduled.
- **Learning for next edition:** record the roster and each channel's job and owner, which message classes were sent where, every message that had to be repeated, any channel that went quiet, and the wind-down decision with its date.

## Next steps

1. Approve or amend section 1, the no-app decision. ⏳ about 5 minutes.
2. Answer the six questions in section 6.
3. Tell EventPulse you are declining. If you want a record of the claim first, ask for named comparable events and their install definition.
4. Hand the roster in section 2 to whoever owns `event-marketing-plan`'s channel directory.
5. Write the message bank and the timestamped day script about two weeks before the event, once the register exists.