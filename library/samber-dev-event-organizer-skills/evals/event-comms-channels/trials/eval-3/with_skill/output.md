# TechFest Krakow channel plan: sanity check

⚠️ **Verdict: don't build it as written.** Of the three ideas, two are patterns the skill says to delete outright, and the third is the weakest routing option at your size. Below are the problems, a replacement, and the questions I need answered before anything is created.

**Scale assumed:** 800 attendees, 2 days, 4 tracks, 4 volunteer writers. This is the "several rooms, several days, several writers" scale, where a routing rule matters more than the number of channels. Every ranking below is the skill's own construction, not a measured benchmark.

## 1. What's wrong with the plan

### ❌ Urgent messages by DM

The skill says to delete this, never demote it, as a routing tier. It has four problems:

- **No record for the next shift.** Nobody can see who was told what.
- **Can't escalate.** A DM has no next step if it isn't read.
- **The sender becomes the channel.** If that person is in a session or off duty, the message doesn't go out.
- **Misses the people who most need it.** A venue or room change affects people who aren't on Discord yet or aren't in the building. Eight hundred people can't be individually DMed in minutes.

Urgent messages (disruption and live-change classes) need an escalation path, described in section 3 below.

### ❌ Telegram mirror of all announcements

As described, this is a second chat platform doing the same job in parallel. The skill's rule: it doubles moderation and halves each announcement's audience. It also causes other problems:

- **Two copies to keep in sync.** Edits and corrections drift, which is how two room numbers get published (the skill's negative example).
- **The code of conduct and a duty responder must cover both platforms.**
- **Both need a wind-down date and a deletion check.**

"About half live on Telegram" is the useful fact here, but it's unverified. It changes the question to *which one* platform, not *both*. Two ways to resolve it:

- **Option A:** poll registrants at check-in or by email, then pick the single platform most of them will join.
- **Option B:** use the announcement list as the guaranteed-reach floor, because it reaches all 800 by construction. Chat then only needs to serve the opted-in subset.

If Telegram has a post-only mode, that is the nearest acceptable form of a mirror. It still adds a second platform to staff and close, so I'd only allow it if your answer to Q4 or Q10 forces it.

### ⚠️ Six per-audience channels

Per-segment is the lowest-ranked routing option on efficiency. A writer has to decide segment membership on every message, and resolves it by cross-posting, which recreates the noise the segments were meant to remove. Examples of the overlap:

- A student who is remote and attending a workshop belongs to three of your six channels.
- `#talks-only` and `#workshop-folks` split by activity, but four tracks run concurrently, so a "Track C room change" concerns neither group as a whole.
- Four volunteers cannot staff six channels. Staffing, not existence, is what reaches people.

### ⚠️ Missing channels the plan assumes exist

- **No broadcast channel nobody replies in.** Without one, an announcement lands between conversations.
- **No open channel for attendees to talk or ask organizers.** That social/community traffic will end up in whichever channel exists, mostly `#talks-only`.
- **No pre-event or Day 1 floor.** Email is the right first channel for pre-event practical information and programme news, and the plan never mentions it.

### ⚠️ `#speakers` and `#sponsors` aren't attendee channels

- **`#speakers`:** speaker communication is owned by `event-speaker-experience`. Organizer-only coordination is owned by `event-run-of-show` and must stay off every attendee channel. Decide which of these `#speakers` actually is before building it.
- **`#sponsors`:** the skill treats sponsor traffic as its own message class. Default routing is batched email, with a named sponsor channel only where a signed deliverable (Q4) forces one. Don't broadcast one message per sponsor.

### ⚠️ `#remote` needs an on-duty owner

The skill's strongest evidence on staffing is the hybrid-event case where remote attendees were never told about a schedule change because the team was busy with in-person check-in. If `#remote` stays, it gets a named person who is on duty whenever sessions run. It also still receives the same live-change messages as on-site attendees.

## 2. Proposed roster (for approval)

| Channel | Job | Owner | Notes |
| --- | --- | --- | --- |
| Announcement list (floor) | Pre-event practical, programme news, batched sponsor notes, wind-down | TBD, one named writer | Copy and consent belong to `event-attendee-email-sequences`. Never carries a minutes-scale message. |
| Chat: broadcast channel (post-only) | Live change and day logistics | One named owner per shift | Prefix the track, e.g. `[Track C]`, instead of making four channels. |
| Chat: open channel | Social, questions to organizers | A volunteer who watches it | Gets the code of conduct stated at the join point. |
| `#remote`, kept only if livestream or remote attendance is real (Q2) | Remote attendees' live feed and questions | A named person on duty during sessions | The one segment that is plausibly disjoint and stable. |
| Status page, conditional on Q9 | One canonical page on whether the broken thing is still broken | Whoever is on duty | Hosted off venue wifi, editable from a phone. A push on another channel must point at it. |
| On-site screens and PA | Live change affecting a session in progress | Floor lead | Dynamic announcement is this skill's job. Printed signs belong to `event-attendee-experience`. |

Left out of this roster:

- **Speaker channel:** goes through `event-speaker-experience`.
- **Organizer coordination:** goes through `event-run-of-show`.
- **Incident reporting:** goes through `event-code-of-conduct`. Confirm its reporting path covers every channel opened here.

**One chat platform only,** chosen per section 1. The roster's directory of channels goes to `event-marketing-plan`'s comms-hub page rather than a second page. It lists each channel's job, who answers, the hours it is watched, and what it is *not* for.

## 3. Routing rule (matrix, since you're at the matrix scale)

| Class | First channel | Also | Never |
| --- | --- | --- | --- |
| Disruption (venue change, session cancelled, livestream down) | Status page plus a push pointing at it | Broadcast channel, email if the change affects travel, screens, PA | Chat only |
| Live change (late start, room swap) | Broadcast channel | Screens; PA if a session is in progress | Email |
| Day logistics | Broadcast channel | Screens | Status page |
| Pre-event practical | Email | Directory link | Chat only |
| Programme news | Email | Public broadcast (social, owned by `event-social-media`) | Chat only |
| Social / community | Open channel | None | Email, broadcast |
| Sponsor and partner | Email, batched | Named sponsor channel only if a contract forces it | Broadcast, one message per sponsor |
| Incident statement | The authority named by `event-code-of-conduct` | None | Anyone else, anywhere |
| Wind-down | Every channel being closed, plus email | None | One channel only |

**Escalation tiers** (the skill's own construction):

- **Tier 1:** a live change affecting a session in progress goes to screens or PA immediately.
- **Tier 2:** an unresolved disruption is re-posted on the status page at a fixed interval, even with "no change".
- **Tier 3:** a disruption that changes whether or where people travel goes to the widest-reach push you have (email plus broadcast).

All intervals are **self-set and must be fixed before the event.** For example, "no change" updates every 30 minutes is an illustration, not a benchmark.

## 4. Consistency across the 4 writers

- **Start with the shared quick-reference page.** It condenses the register into do/don't lines with worked examples.
- **Add a pre-written message bank for time-critical classes.** The skill supplies eight templates: delay, room change, venue change, session cancelled, livestream interrupted, lost property, last call, closing. They are field sets, not finished copy. Rewrite them in your register before the event.
- **Give each channel a named owner.**
- **Skip editorial sign-off.** It bottoms out on speed, which hurts at a live event. It would only be justified if the event is livestreamed, press-covered or fixed by a sponsor contract, and even then time-critical classes go to the bank.
- **Script the predictable nudges against literal timestamps.** Examples: "lunch is open", "badge desk closes", "starting in 3 minutes".
- **Confirm the register exists (Q5).** If `event-cultural-identity` hasn't been run, everything above is provisional. The skill executes a register and never invents one.

## 5. Wind-down (decide now, publish the date on the channels)

- Default for a one-off edition: **export plus scheduled deletion.** Announce the date on the channel first.
- If TechFest compounds into a series and someone has committed to running the next community space: **hand-off.**
- If nobody is on duty after the closing date, don't leave channels open. An unmoderated space in the event's name has a code-of-conduct duty with no responder.
- Read-only archive is the cheapest fallback that destroys nothing.
- Retention length, lawful basis and attendees-who-were-minors go to your own counsel. Take the skill's review list to them; I'm naming no jurisdiction or period.
- Every channel opened gets a closed state and a date. That is the one pass/fail check.

## 6. Questions that gate the build

One at a time is the skill's default. Here they are in priority order:

1. **Telegram:** is "half the audience" measured or a guess? Which single platform wins? (Q10, Q4)
2. **Q9:** what can break that attendees can't see for themselves (livestream, shuttle, single entrance, venue change, catering)? If nothing, the status page is dropped.
3. **Q2/Q1:** is there a livestream or remote programme, and do you need pre-event, on-site and wind-down all three?
4. **Q4:** does anything signed force a channel (sponsor deliverable, venue system)?
5. **Q5:** does a register from `event-cultural-identity` exist?
6. **Q3:** how many of the four writers have never written for this event?
7. **Q7/Q8:** one-off or series, and who is on duty the week after?
8. **Q6:** hard go-live date?

## 7. Measurement (all thresholds self-set, fixed before the event)

- **Repeat rate:** the share of messages re-sent on a second channel because the first didn't reach.
- **Unrouted questions:** questions that land somewhere with no owner (a DM, a social reply, a speaker's inbox).
- **Channel silence:** any channel with no organizer post for a period you fix in advance. Candidate for deletion next edition.
- **Wind-down completion:** binary.

## Recommended next step

Answer questions 1 and 2. I'd then finalize section 2 (roster) first, get your approval, and only then hand the directory to `event-marketing-plan` and draft the message bank. Nothing should be created on Discord or Telegram until the roster is approved.