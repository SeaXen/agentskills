# ShipIt Conf comms channels: what I'd change

I followed `event-comms-channels` and its three references. The skill wants one interview question at a time. Since you asked for the full answer, I've stated assumptions and listed the open questions at the end, with what each would change.

**Assumed scale:** one room, one day, 300 people, two writers. At this scale, a routing rule and a short list come before more channels. Every ranking in the skill is a default, not a measurement, and I've marked the self-set parts.

## 1. Roster: cut the hackathon template down

The template comes from Major League Hacking's guide. It was written for an overnight student event, and the skill says not to port it to a conference unchanged.

| Template channel | Verdict | Why |
|---|---|---|
| #team-formation | ❌ Cut | Conference attendees have no teams to form. |
| #ask-mentors | ❌ Cut | There is no mentor population. Speaker comms belong to `event-speaker-experience`. |
| #mentors-internal | ❌ Cut | Same reason. Any speaker or staff backchannel goes to the organizer channel. |
| #carpool-search | ⚠️ Fold in | The skill finds no conference analogue. If rides matter, make them a pinned thread in #hallway. |
| #introductions + #random | ⚠️ Merge into #hallway | Two writers can't seed and watch two social channels. |
| #ask-organizers | ✅ Keep | This is the one staffed question lane. |
| #admin | ⚠️ Keep, but hand off | `event-run-of-show` owns it. Keep it private, off the attendee directory, and ideally outside the attendee-facing server or at least invisible to attendees. |
| *(missing)* #announcements | ✅ Add | The template has no post-only broadcast channel, which is the main gap. |

**Proposed attendee-facing roster (3 channels):**

- **#announcements** is post-only for organizers. It carries live changes and day logistics. Owner: writer A.
  - If the platform has a post-only mode, use it. That costs no extra channel.
- **#ask-organizers** is where attendees ask questions, watched during event hours. Owner: writer B.
- **#hallway** is open talk: introductions, random, rides. Owner: writer B. It has no organizer-post expectation.

The skill says a channel with no stated job and no named owner doesn't get created. Each channel above has both.

**Announcement list (email):** keep it as the floor. It reaches every registrant, but in hours. Never use it for a message about today.

**Event app:** no. The skill lists 3+ concurrent rooms, a signed obligation, or an app you already own as the conditions for one. None applies.

**Status page:** conditional. Add one only if Q9 below names something attendees can't see for themselves (livestream, shuttle, single entrance, venue-change risk). If nothing qualifies, skip it. A page that always says "all fine" trains people not to look. If you build one, it needs a push pointing at it, because nobody checks it unprompted.

**Chat opening date (self-set):** I suggest opening it a week before the event, not at ticket sales. That avoids weeks of moderation for a channel with nothing to say. Invite people by email.

## 2. Routing: two-channel split, no matrix

The skill's "conditional delete" removes the matrix and per-segment rungs when it's one room, one day and one or two writers. Nothing concerns "part of the room".

**Rule (write it in the writers' pinned message, not a doc):**

| Message class | Goes to | Notes |
|---|---|---|
| Disruption, e.g. venue change or livestream down | Email, plus the public broadcast (a call for `event-social-media`), plus a status page if one exists | Never chat only. People who need it aren't in the building yet. |
| Live change, e.g. talk starts late | #announcements, plus **PA call** | Single track makes the PA the best live surface. |
| Day logistics | #announcements | Don't use the status page, or it stops meaning "incident". |
| Pre-event practical and programme news | Email | Link to the channel directory inside it. |
| Social | #hallway | Keep it off email and the broadcast. |
| Sponsor messages | Email, batched | Not one message per sponsor in #announcements. |
| Incident statement | Whatever `event-code-of-conduct` names | One publisher. Nobody else posts, with no local exception for being faster. |
| Wind-down | Every channel being closed, plus email | Not just one channel. |

A minutes-scale message never rides an hours-scale channel, and an hours-scale message never rides the disruption path. Don't use organizer DMs as a routing tier, because they leave no record for the next shift.

## 3. Consistency for two writers

- **Register:** it must come from `event-cultural-identity`. If ShipIt Conf doesn't have one yet, run that skill first and label everything here provisional. Don't carry over last year's hackathon voice, and don't let each channel develop its own.
- **Default:** a one-page quick-reference (do/don't lines, worked examples).
- **Add a pre-written message bank.** Time-critical messages shouldn't wait on a specific person. Draft these eight before the day: delay, room change, venue change, session cancelled, livestream interrupted, lost property, last call, closing and wind-down. They are field sets from the skill, not finished copy. Rewrite them in your register, keep every field, and give the next-update time whenever it's unresolved.
- **Script the predictable clock:** meal-ready, "starting in 3 minutes" and venue-closing messages get written against literal timestamps in advance. That way neither writer has to remember to compose one mid-event.
- **Named owner per channel** as in section 1. Skip editorial sign-off unless a sponsor contract fixes wording or the event is livestreamed or press-covered. Even then, time-critical classes are exempt.

## 4. The "channels" page: don't build it on the microsite

Your marketing lead already maintains a comms hub page. The skill says `event-marketing-plan` owns that page, so extend it and don't publish a second competing directory. Two directories drift apart, and attendees follow whichever they saw first.

- **Hand the marketing lead:** for each channel, the name, the one-line job, who answers, the hours it's watched, and what it is not for with a pointer to the right channel. Most directories omit that last line, and it stops awkward messages landing on whichever channel the attendee saw first.
- **If the microsite is forced** (see Q4 below), make it link to the hub page, not duplicate the content.

## 5. Code of conduct

- State the code of conduct at the join point (welcome screen, rules channel), not only on the website.
- Confirm with `event-code-of-conduct` that its reporting path covers every channel you open, and that someone is on duty for the whole time each channel is open, including after the event. Don't write the reporting path yourself.
- Digital spaces can increase harassment, so make that visible to attendees.
- **Check the cloned server before use.** Last year's attendees were students, possibly including minors. Verify the template carried over no members, roles, bots, webhooks or live invite links. Strip anything that would keep writing into it.

## 6. Wind-down: decide now, publish the date on the channels

The right rung depends on Q7 (one-off or series) and Q8 (who is on duty afterwards). Both are open, so here are the branches.

| Situation | Rung |
|---|---|
| One-off edition (default if unsure) | Export, then scheduled deletion after a stated window. A one-off's member list is a liability with no next edition to spend it on. |
| Series intended **and** a named person or standing space exists to receive people | Hand-off to a persistent community space. Invite rather than migrate. |
| Neither, or you want the lowest-effort safe option | Read-only archive: freeze posting, post where to go next. |
| Leave open | Only if someone is named on duty with an end date. With two people and nobody on duty the week after, this is a conditional delete. |

- **Retention window and lawful basis:** take them to your own counsel with the skill's review list. I'm not naming a jurisdiction or a period.
- **Announce the date a week ahead** on the channel itself.
- **Never wind down silently.** It destroys trust in the next edition's channel.
- **Confirm the deletion happened.** An unchecked scheduled deletion is leave-open with paperwork.

## 7. Measurement (all thresholds self-set, fixed before the event)

- **Repeat rate:** the share of messages re-sent on a second channel because the first didn't reach. Pick a ceiling in advance.
- **Unrouted questions:** count questions that landed somewhere with no owner (a DM, a social reply, a speaker's inbox). They show your missing channel or directory line.
- **Channel silence:** a period with no organizer post, fixed in advance. A silent channel is a deletion candidate next edition.
- **Wind-down completion:** every opened channel has a closed state and a date. This is the only clean pass/fail.

## Open questions

1. **Q5:** Does `event-cultural-identity` already give ShipIt Conf a register? If not, everything above is provisional.
2. **Q9:** What can break that attendees can't see for themselves (livestream, shuttle, single entrance, venue)? This decides whether you build a status page.
3. **Q7:** Is this a one-off or a series? If a series, who would run the persistent space?
4. **Q8:** Who is watching channels during the event, and who is on duty the week after?
5. **Q4:** Is anything forcing the microsite or the Discord (sponsor deliverable, venue, umbrella platform)? If not, drop the microsite page.
6. **Q10:** Is there an existing developer community chat your audience already uses? A hackathon-scale Discord may not suit 300 professionals, and an existing space would change the roster.

I haven't created, changed or sent anything. The roster, routing rule, consistency process and wind-down each need your approval before anyone creates a channel.