# DevSummit Oslo attendee comms: recommended setup

This follows the `event-comms-channels` skill and its references. I couldn't run the interview, so I state my assumptions. Nothing below is created until you approve it section by section.

## Verdict

1. **Keep one voice.** Retune the Discord and email styles to the written guide. Don't keep a personality per channel.
2. **Limit head-of-comms sign-off.** Use it only for slow, high-stakes messages, and have them approve a message bank once, before the event. Don't route live-day messages through them.
3. **Script the three repeat messages in advance.** Write them against literal clock times, and nobody has to remember to send them.

## Assumptions

- I treat last year's brand voice guide as the fixed register. The skill executes a register and never sets one. If the guide doesn't cover how the event sounds in short operational messages, run `event-cultural-identity` first and label this plan provisional.
- **Scale:** several rooms or days, five writers, two of them new. At that scale the skill says you need a routing rule before you need more channels.
- **Existing channels:** Discord and an email list, as you described them.
- **Not given:** whether the event is livestreamed, recorded or press-covered, whether a sponsor fixes wording, whether it's a one-off or a series, and who is on duty after the event.

## 1. Voice: why per-channel personality is the cause

The skill is explicit on this point. A register invented by whoever writes a channel is a "delete, never demote" item, because it is what makes an event sound like four different events. Your attendees' joke is that symptom.

Your instinct has a valid half. Identity is fixed, and only expression modulates. Discord can be shorter and warmer than email, but both must stay inside the same guide. The jokey Discord style and the lawyerly email style are each a private register, so both get retuned.

Actions:

- **Quick-reference page.** Condense the voice guide into do/don't lines with worked examples. Rewrite the same message once as Discord and once as email, so the allowed range of modulation is visible. Both new volunteers read this first.
- **Named owner per channel.** Your Discord person and your email person keep their channels and become accountable for them. They keep their skills and lose their private register.
- **No new voice.** Nobody on the team invents wording rules. The guide is the authority.

## 2. Approval: why not every message

Sign-off on everything is the skill's "starved rung". It gives the most consistency and the most effort, and it is the slowest, which hurts most on event days. The skill promotes it only when one of these holds:

- The edition is recorded, livestreamed or press-covered.
- A sponsor contract fixes verbatim wording.
- Most writers have never seen the register.

On your facts none clearly holds, because two of five new writers is not most. Check the first two. If either is true, use sign-off for the slow classes below.

Recommended split:

| Message type | Approval |
| --- | --- |
| Pre-event practical, programme news, sponsor messages (days-scale) | Head of comms signs off. There is time. |
| Live change, day logistics, disruption (minutes to hours) | **No sign-off.** Use pre-approved bank templates. |
| Incident statement | Not yours. One authority publishes it under `event-code-of-conduct`, and nobody else posts about it on any channel. |

Head of comms approves the bank once, before the event. After that, a message in the bank is already approved, so a live message never waits for them. The two new volunteers can send only bank templates until they've shipped a few. That is my suggestion, not the skill's.

## 3. Your three repeat messages

The skill singles out exactly these: a venue-closing warning, a meal-ready ping and a "starting in N minutes" call. Go one step beyond a template on standby. Write the whole day's script against literal timestamps before the event.

| Message | Class | Template | Channels |
| --- | --- | --- | --- |
| "Venue closes at 22:00" | Day logistics | Last call (#7) | Chat broadcast channel and on-site screens |
| "Lunch is ready" | Day logistics | Last call or custom, same fields | Chat broadcast channel and on-site screens |
| "Next session in 5 min" | Day logistics | Last call (#7) | Chat broadcast channel, plus PA or screen in the room |

Rules:

- **Not email.** Email takes hours to land, and these messages are due in minutes.
- **Not the status page.** These aren't incidents, and using it for them trains people to ignore it.
- **Fill the clock times from the final programme.** Freeze the script when the programme freezes.
- **A slip is a different class.** If a session runs late, it becomes a Live change, which uses the Delay template (#1), and the scheduled "starts in 5" for that slot must not fire. Give one named person the job of pausing scheduled sends. This pause step is my addition.
- **State the new fact before the apology**, and give a next-update time whenever something is unresolved.

The skill's eight templates are Delay, Room change, Venue change, Session cancelled, Livestream interrupted, Lost property, Last call and Closing notice. They are field sets, not finished copy. Rewrite each into your register and keep every field.

## 4. Channel roster (assumed scale)

Each channel gets one job and one named owner, or it isn't created.

| Channel | Job | Notes |
| --- | --- | --- |
| Announcement list (email) | Pre-event practical, programme news, sponsor batches, wind-down notice | Copy and consent belong to `event-attendee-email-sequences`. Here it only carries hours-scale messages. |
| Chat space, broadcast channel | Live change and day logistics, posted by the event only | Use the platform's post-only mode if it has one. |
| Chat space, open channel | Social, community, attendee questions | The code of conduct is stated at the join point, and someone is on duty. |
| On-site screens and PA | Dynamic on-site announcements | `event-attendee-experience` owns static signs only. |
| Status page | Only if something can break that attendees can't see for themselves (livestream, shuttle, single entrance, venue change) | Skip it if nothing qualifies. It is never a push channel, so a push on another channel must point to it. |

Two exclusions:

- **Organizer coordination channel.** It belongs to `event-run-of-show`, and staff coordination never goes on an attendee channel.
- **Event app.** Only if a signed commitment forces one, or the grid changes more than once a day across three or more concurrent rooms, or you already own one.

If a second chat platform already runs the same job in parallel, delete one. Two platforms double the moderation and halve each announcement's audience.

Hand the roster to `event-marketing-plan` for its channel directory page, so there is no second page. Per channel, list its name, its job, who answers, the hours it is watched, and what it is not for with a pointer to the right channel.

## 5. Routing rule

At your scale the skill's default is a two-channel split: one place the event posts and one place attendees talk. Move to the full matrix if you have three or more rooms across two days, or the event is recorded or livestreamed.

The load-bearing rule: **a minutes-scale message never rides an hours-scale channel, and an hours-scale message never rides the disruption path.**

| Class | First channel | Never |
| --- | --- | --- |
| Disruption | Status page plus a push pointing to it | Chat only |
| Live change | Chat broadcast channel, plus screen or PA if a room is in session | Email |
| Day logistics | Chat broadcast channel plus screens | Status page |
| Pre-event practical and programme news | Email | Chat only |
| Social | Chat open channel | Email or broadcast |
| Sponsor | Email, batched | Broadcast, one message per sponsor |
| Incident statement | Whatever the authority names | Anyone else, anywhere |
| Wind-down | Every channel being closed, plus email | One channel only |

Put this table where the writers work, not in a document they open once. For disruptions, set the repeat intervals in advance (for example "still working on it, next update in 30 minutes"). Intervals chosen during an outage are chosen badly. The skill's four tiers are the self-set escalation rules to use here.

## 6. Wind-down: decide now

This depends on whether DevSummit Oslo is a one-off or a series. That is the one answer I most need from you.

- **One-off:** export plus scheduled deletion, with the deletion date published on the channel in advance.
- **Series, with a named person committed to run a community space:** hand-off, by invitation and not by migration.
- **Series with no committed owner, or nobody on duty after the event:** read-only archive. Leaving it open with nobody on duty leaves a code-of-conduct duty with no responder.

Publish the date on the channels, and never close one silently. The skill names no retention period and no jurisdiction, so take the retention questions to your own counsel.

## 7. Measures (all self-set; fix before the event)

- **Repeat rate:** the share of messages re-sent on a second channel because the first missed.
- **Unrouted questions:** questions that landed in a DM or a social reply with no owner.
- **Channel silence:** any channel with no organizer post for a period you set in advance.
- **Wind-down completion:** every opened channel has a closed state and a date, which passes or fails cleanly.

## Questions that could change this plan

1. Is the event livestreamed, recorded or press-covered, and does any sponsor fix wording? If yes to either, sign-off moves up for the slow classes.
2. Is it a one-off or a series?
3. How many rooms and days are there?
4. Does anything signed force a channel, and does the guide cover short operational messages?
5. Who is on duty after the event?
6. What can fail that attendees can't see?

## Approval order

Each section below needs your approval before anyone creates a channel:

1. Roster
2. Routing
3. Consistency (quick-reference, bank, and the sign-off split)
4. Wind-down