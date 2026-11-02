# DataDays Porto: comms review and incident definitions

I followed `event-comms-channels` and its three reference files. Questions I couldn't ask are marked as assumptions below. Please confirm them before anyone opens a channel.

## Verdict on your plan

| Plan item | Verdict | Why |
|---|---|---|
| Status page | ✅ Keep | You have things attendees can't see for themselves: the livestream, the shuttle and the entrance. |
| Operational / degraded / major outage levels | ❌ Replace | The skill says to use message classes instead (see below). |
| Subscribe-for-updates form | ❌ Drop | Nobody subscribes to a two-day conference's status feed. The page is a destination that a push points at. |
| Public post-mortem | ❌ Make it internal | At events the cause is often a person or a supplier. |
| Daily logistics on the page | ❌ Move to chat | It isn't an incident, and it trains people to ignore the page. |
| Same server as registration | ❌ Move | A status page hosted on the failing infrastructure fails with it. |

### 1. Severity levels → message classes
- **Why the levels don't fit:** The skill says tiers describe a system with measurable availability. Event disruptions are discrete and human-scale. Tiers also add a classification step in the minutes you have least of.
- **What the classes are:** Section A below classifies by two things only: how fast the message must land, and who it concerns.
- **Optional status badges:** If you still want a status badge, use two states per component: **Running** or **Disrupted**. The components are Livestream, Shuttle and Venue entrance. The two-state badge is my adaptation of your idea, not part of the skill. The timestamped note carries all the detail.

### 2. Subscribe form → push to channels attendees already have
- Every registrant is already on your announcement list. Point at the page from there.
- Add the page link and a QR code to the know-before-you-go email, the badge or lanyard, the on-site screens and the shuttle signs.
- A new subscriber list would create a second consent and copy problem. `event-attendee-email-sequences` owns that problem, so don't build one.

### 3. Public post-mortem → written resolution plus internal debrief
- **Public:** Post a short resolution note on the status page. It gives when it ended and what happened, and it names no person or supplier.
- **Internal:** Write the full review as a note for `event-debrief`.

### 4. Daily logistics → chat broadcast channel
- Lunch opening, badge desk hours and the last shuttle are "Day logistics" messages. Their first channel is the chat broadcast channel, with on-site screens as a second.
- The skill's matrix lists the status page under "Never" for this class.
- If the page is active every day, a real disruption looks like noise. A page that reports "everything is fine" trains people not to look.

### 5. Hosting → separate from the registration server
- **Why the shared server is a risk:** Registration traffic spikes before the event. The shared server is also the most likely thing to break on day one. A shared server fails together with the page.
- **What to use instead:** Any page with a stable URL, on different infrastructure and ideally a different DNS or CDN path. It must be editable from a phone in under a minute. It must not sit on the venue wifi or inside an app.
- **Cost:** It doesn't have to cost money. It just can't be the registration server.

## A. Message classes (replaces the severity definitions)

These are the skill's own construction. The deadlines are targets for you to set before the event.

| Class | Deadline | Concerns | DataDays examples |
|---|---|---|---|
| **Disruption** | Minutes | Everyone affected, including people not yet on site | Venue or entrance change, livestream down, shuttle suspended, session cancelled |
| **Live change** | Minutes to an hour | One room, or everyone on site | Talk starts 20 min late, track swaps rooms |
| **Day logistics** | Hours | Everyone on site | Lunch open, badge desk closes at 17:00, last shuttle |
| **Pre-event practical** | Days | Every registrant | Know-before-you-go, directions, what to bring |
| **Programme news** | Days to weeks | Registrants and often the public | Schedule published, speaker added |
| **Social / community** | None | Opted-in attendees | Introductions, dinner plans |
| **Sponsor and partner** | Days | Registrants | Sponsor workshop, partner discount |
| **Incident statement** | Set by the authority | Case by case | A public statement after an incident |
| **Wind-down** | Days | Everyone on closing channels | Recordings are up, channel closes on the 14th |

**What belongs on the status page:** Only the **Disruption** class goes on the status page. It covers the livestream, the shuttle and the venue entrance, which are the things attendees can't see for themselves.

**The load-bearing rule:** A minutes-scale message never rides an hours-scale channel. An hours-scale message never rides the disruption path.

**Escalation tiers (self-set intervals):**
- **Tier 0:** The message goes on its first channel. Nothing escalates.
- **Tier 1:** A Live change or Disruption that affects a session in progress goes at once to on-site screens or the PA. There is no wait.
- **Tier 2:** An unresolved Disruption is repeated on the status page with a timestamp at a fixed interval, even if nothing changed ("still working on it, next update by 11:30"). Proposed starting intervals, to be fixed before the event:
  - **Livestream:** 30 min.
  - **Shuttle:** 15 min, because people are standing at a stop.
- **Tier 3:** A disruption that changes whether or where someone should travel goes to the widest-reach push you have, whatever the noise. This is the only tier allowed to wake people up.

## B. Proposed roster (assumes: 700 attendees, 2 days, livestreamed main track)

Each channel gets one job and one named owner. Owner names and dates are placeholders for you to fill in.

| Channel | Job | Owner | What it's not for |
|---|---|---|---|
| Announcement list (exists) | Pre-event practical, programme news, sponsor batches, wind-down | [name] | Anything about today |
| Chat, broadcast channel (post-only) | Live change, day logistics, push pointing at the status page | [name] | Conversation |
| Chat, open channel | Social and community | [name] | Official announcements |
| Status page | Disruption only: Livestream, Shuttle, Venue entrance | [name] | Daily logistics, anything non-incident |
| On-site screens and PA | Tier 1 escalation | [name] | Static wayfinding (`event-attendee-experience` owns that) |

Notes on the roster:
- **Chat space:** I recommend it because the event is multi-day, remote viewers watch the stream, and day logistics need something faster than email. Confirm this. If you decide against chat, day logistics fall back to email plus screens, and that is slower.
- **Public broadcast:** Say "this goes out publicly" for Disruption and Programme news. `event-social-media` picks the platform.
- **Organizer-only coordination:** That channel belongs to `event-run-of-show`. Keep it separate from all of the above.
- **Channel directory:** Hand this roster to `event-marketing-plan`'s comms-hub page. List each channel's job, who answers, the hours it's watched and what it's not for. Don't publish a second directory.
- **Message bank:** If you have several writers, use the bank templates below and write the day's timed messages against literal timestamps in advance.

## C. Message-bank fields to draft before the event

These are field sets, not finished copy. Rewrite them in your event's register, which `event-cultural-identity` sets. State the new fact before any apology, and always give a next-update time.

- **Livestream interrupted:** "The livestream for [track] is down as of [time]. We are working on it and will post here again by [time] whether or not it is fixed. Recordings will still be published."
- **Shuttle disrupted (adapted from the venue-change template):** "[Shuttle] from [metro stop] is [suspended/delayed] as of [time]. Alternative: [route/transport note]. Next update by [time]. Details: [status page URL]."
- **Venue or entrance change:** "Read this before you travel. [Event] on [date] is now at [address], not [old address]. [Transport note.] Doors from [time]. Full details and updates: [status page URL]."
- **Resolution (status page):** "Resolved at [time]. [What happened, in one line, naming no person or supplier.] [What is back to normal.]"
- **Last call, closing and delay:** Use the skill's generic templates.

## D. Code-of-conduct check
- The code of conduct is stated at the join point of each chat channel, not only on the website.
- Someone is on duty in the chat during opening hours.
- **I did not design the reporting path.** `event-code-of-conduct` owns it. Confirm with them that it covers every channel opened here.
- A public statement after an incident has exactly one authorized publisher. The matrix carries an Incident statement row with that person named, and nobody else posts about it on any channel.

## E. Wind-down (decide now, publish the date on the channels)

Dates are placeholders. Q7 (one-off or recurring series?) changes the choice for the chat.

| Channel | Default wind-down | Notes |
|---|---|---|
| Status page | Read-only archive | Freeze it after the event. Post a final note saying where updates go next. |
| Chat | One-off edition: export plus scheduled deletion. Recurring series: hand-off to a community space, only if a named person commits to running it. | Announce the date at least a week ahead on the channel. Take the retention decision to your own counsel. I name no jurisdiction or retention period. |
| Announcement list | Handled by `event-attendee-email-sequences` | |

Whichever you choose, wind-down is complete only when every channel has a closed state and a date.

## F. Measurement (self-set, fix before the event)
- **Repeat rate:** Messages re-sent on a second channel because the first didn't reach. Set a ceiling in advance.
- **Unrouted questions:** Questions that landed with no owner (DMs, social replies, speaker inboxes). Note where they landed.
- **Channel silence:** Any channel with no organizer post for a period fixed in advance is a deletion candidate for next edition.
- **Wind-down completion:** Pass or fail on the scheduled day.

## What I need from you
1. Is this a one-off edition or a series with a next edition?
2. How many rooms and how many people will write to attendees?
3. Does a register exist from `event-cultural-identity`? If not, run that skill first and treat this as provisional.
4. Who is on duty the week after the event?
5. Is any channel already fixed by a sponsor or venue contract?

I haven't created anything. Approve the roster, routing, consistency process and wind-down section by section before anyone opens a channel.