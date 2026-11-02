# CloudCamp Austin: venue change and livestream outage plan

Using the `event-comms-channels` skill and its three references. The skill normally interviews one question at a time. Here I've stated assumptions instead, so correct me if any are wrong.

**Assumptions:**
- One edition, no next edition guaranteed.
- A handful of organizers write to attendees.
- The livestream is the one thing attendees can't see for themselves (the skill's Q9 answer).
- You already have an email list from registration.
- Your register (the event's voice) is already set by `event-cultural-identity`. I write no copy here.
- Everything labelled "self-set" is my own construction or a number you must fix yourself, not a benchmark.

## 1. Venue change: yes, a Discord post is not enough

**The gap.** A venue change is a Disruption, the highest message class. The skill's matrix says it never rides "chat only", because the people it concerns are not in the building. It also changes where people travel, which makes it Tier 3: use the widest push you have.

**The numbers.** About a third of 600 is roughly 200 people on Discord, and "active" doesn't mean they read #announcements. Up to about 400 registrants may not know the address changed. Each of them will drive to the flooded venue.

### Do now (today, order matters)

1. **Email all 600 registrants today.** The list is the only channel that reaches every registrant by construction.
   - Open with the new fact, with "Read this before you travel" as the first line.
   - Use the skill's Venue change template (message-bank template 3): `[Event] on [date] is now at [address], not [old address]. [Transport note.] Doors from [time]. Full details and updates: [status page URL].`
   - Put the old address in the message so people recognize what changed.
   - Copy, subject line and consent rules belong to `event-attendee-email-sequences`. Hand the template fields to that skill.
2. **Stand up one canonical page for the address.**
   - Requirements: stable URL, editable from a phone in under a minute, not hosted on the venue's systems.
   - Put the address, transport, parking, doors time and "last updated [timestamp]" on it.
   - Every other channel points at it instead of restating it. This stops two volunteers publishing two different addresses.
3. **Fix the Discord post and make it point at the page.**
   - Edit or replace last night's post with the template.
   - Pin it. If the platform supports post-only for organizers, use it for #announcements.
   - Keep the post short, with the link as the payload.
4. **Say "this goes out publicly" to whoever owns social.** `event-social-media` owns platform and copy. You only flag that the change must be public.
5. **Update the other places the old address lives.** Your marketing-plan owner (`event-marketing-plan`) publishes the comms hub page, so ask them to update the site, the ticketing page, and any confirmation templates and calendar invites carrying the old address.
6. **Tell speakers and sponsors directly.** Speaker comms belong to `event-speaker-experience`. Sponsor traffic is its own class, so batch it into one message and keep it off the broadcast channel.

### Repeat on a fixed clock (self-set, as the venue-change class needs more than one pass)

- **T-7:** a know-before-you-go email with the new address, parking and transit.
- **T-3:** a Discord reminder plus a public post.
- **T-1:** an email and a Discord post: "Tomorrow, here, not there."
- **Morning of:** a pre-scheduled Discord post and status-page timestamp. Write this day's messages against literal timestamps now, so nobody has to remember at 07:30 while running the event.

### On the day

- **Put a person or sign at the old venue.** Some attendees will still go there. This is dynamic on-site announcement, which sits with this skill. Static wayfinding signs at the new venue belong to `event-attendee-experience`.
- **Give the page one owner** who can edit it, and tell the rest of the team to point at it instead of retyping the address.

### Measure it (thresholds self-set, fixed before the event)

- **Repeat rate:** the share of messages you had to re-send on a second channel because the first missed.
- **Unrouted questions:** "wait, where is it?" arriving by DM or social reply. Count them and note where they landed. Each one shows a missing channel or a missing line in the directory.
- Save both counts to your debrief (`event-debrief`).

## 2. Livestream policy: keep the intent, change the mechanism

**The conflict.** The skill is explicit that silence during an outage reads as abandonment. Tier 2 says to repeat on the status page with a timestamp at a fixed interval, "even when there is nothing new". "Stay quiet until fixed" fails remote viewers, who can't see the room and have nothing else to go on.

**Your concern is valid.** The skill agrees you shouldn't spam people with partial updates. The way to satisfy both is to separate where updates live from where people get pushed.

### Replacement policy

1. **One push, one canonical page.**
   - When the stream drops, send exactly one push to the broadcast channel (Discord #announcements, not the open chat).
   - Use the Livestream interrupted template (message-bank template 5): `The livestream for [track] is down as of [time]. We are working on it and will post here again by [time] whether or not it is fixed. Recordings will still be published.`
   - It points to the status page.
2. **All later updates go on the status page only.** Add timestamped lines at the fixed interval, including "still working on it, no change", with no further pushes while the outage continues. Remote viewers who check get fresh information, and nobody's phone buzzes every 10 minutes.
3. **Set the interval now, before the event.** Example: every 30 minutes (self-set). An interval chosen mid-outage is chosen badly.
4. **One more push when it's fixed.** Post one resolution message in the broadcast channel: when it ended, what happened, and that recordings will be published.
5. **Don't use email for this.** Email is an hours-scale channel and this is a minutes-scale message.
6. **Name an owner and a backup** for the stream status. Do this before the event. The skill's staffing failure (MLH's hybrid-event failure list) is exactly this: the team gets busy with the in-person crowd and remote attendees get nothing. If you have a stream-viewer page or stream chat, link the status page there too, since that is where those viewers already are.
7. **The page must not depend on the failing system.** Don't host it on the stream platform or venue wifi.

**What changed:** Your "don't spam" goal is kept (one push in, one push out). The "stay quiet" part is dropped for the page, and only for the page. Say so in your runbook, so a volunteer in the moment doesn't fall back on silence.

## 3. Roster and ownership for this edition

| Channel | Job | Owner (name before launch) | Opens | Closes |
|---|---|---|---|---|
| Email list | Venue change, pre-event practical, wind-down | Email owner | Existing | After wrap-up notice |
| Discord broadcast (#announcements, post-only if possible) | Pushes: live changes, disruption pointers | Comms owner | Existing | Wind-down date |
| Discord open channel | Attendees talk to each other and organizers | Moderator on duty | Existing | Wind-down date |
| Status page | Address now, stream status on the day | Named editor + backup | Today | Wind-down date |
| Public social | Public broadcast only | `event-social-media` owner | Existing | n/a |

- **Each channel needs one job and one owner.** An ownerless channel is how a message gets lost.
- **Staff coordination stays off all of these.** That is `event-run-of-show`'s separate organizer-only channel.
- **Code of conduct on Discord.** State it at the join point and keep a responder on duty. The reporting path belongs to `event-code-of-conduct`, so confirm with them that it covers Discord. Any incident statement goes through that skill's single authorized publisher, with no local exception.

## 4. Decide wind-down now, with a date

I'd default to an export plus scheduled deletion if this is a one-off, or a read-only archive if you're unsure. A hand-off to a community space needs a named person to run it. Whichever you choose, announce the date on the channels now, and do not close them silently. Retention questions (how long you may keep a member list, whether you need to ask again) go to your own counsel. I'm naming no jurisdiction or period.

## Open questions

Answer these and I'll tighten the plan:
1. How many people write to attendees on the day, and have any not written for this event before?
2. Is there a next edition planned? This decides the wind-down.
3. Do stream viewers have a page or chat of their own, and how many remote viewers do you expect?
4. Does a sponsor deliverable or venue contract force any channel on you?