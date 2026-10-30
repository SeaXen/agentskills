# Wind-down and the status page

Contents: per-rung wind-down checklists · the review list to hand to counsel · the status-page pattern and what does not transfer.

## Per-rung wind-down checklists

Do all of it on a date chosen before the event, published on the channels themselves. The four checklists below are this skill's own construction, not observed practice. Treat any documented wind-down practice you meet as grounds to revise them for the next edition.

**Leave everything open** - only legitimate where someone is genuinely still on duty.

1. Name the person on duty and the end date of their duty, in writing.
2. Post that name and date on every channel, so attendees know who they are talking to.
3. Confirm the code-of-conduct reporting path still reaches a responder - the obligation did not end with the event.
4. Put a review date in a calendar. Without one this rung becomes permanent by default rather than by decision.

**Read-only archive**

1. Announce the freeze date at least a week ahead, on the channel itself.
2. Post a final message that says where to go next and who to contact - an archive with no forwarding address strands anyone who arrives late.
3. Set the space to post-only-by-organizers or fully read-only, whichever the platform supports.
4. Check the platform's free-tier history retention. A tier that hides messages past a certain age has already deleted the archive you think you kept.
5. Remove any bot, integration or webhook that would keep writing into a frozen space.

**Export plus scheduled deletion**

1. Decide the retention window and its reason before exporting anything, and take that decision to counsel (see the review list below).
2. Announce the deletion date on the channel, ahead of time, and say what will be exported and what will not.
3. Export: the member list only if you have a basis to keep it, plus anything the event genuinely needs - decisions taken, unanswered questions, the post-event content links.
4. Store the export where it is covered by the same basis as the original, and record who can reach it.
5. Delete on the announced date, including invites, integrations and any mirror.
6. Confirm the deletion actually happened. A scheduled deletion nobody checked is leave-open with paperwork.

**Hand-off to a persistent community space**

1. Confirm both halves of the promotion condition: the series is compounding, and a named person has committed to running the receiving space.
2. Agree with that person what changes at handover - the space's purpose, its rules, its moderation roster.
3. Invite rather than migrate. Moving people into a new space without asking is a new purpose applied to old consent.
4. Wind the old channels down on one of the rungs above. A hand-off is not an alternative to closing them.
5. Hand over the open questions, not just the members. The first week of a community space is decided by whether the questions people left behind get answered.

## The review list to hand to counsel

Name no jurisdiction, quote no retention period, and state no rule. Data protection, platform terms and moderation duty differ by country, by platform and by year. Take this list to the organizer's own counsel:

- What lawful basis covered collecting the member list, and does it cover keeping it after the edition ends?
- How long may the list be kept, and what has to happen at the end of that period?
- Does moving people to a different space require asking them again?
- What do the platform's terms say about exporting a member list, and about what happens to the data if the space is deleted or the account lapses?
- Who holds the moderation duty for a space still carrying the event's name after the event, and for how long?
- Does anything change if attendees included minors?

## The status-page pattern

The event status page adapts a practice from software incident communication: a public page stating current service status, with timestamped updates through an incident and a written resolution afterwards. Software's status-page practice is mature and widely documented. The adaptation to events is this skill's own construction, and the two lists below are the whole of it.

What transfers:

- **One canonical surface.** During a disruption, contradiction is worse than silence. A single page that is authoritative by agreement lets every other channel point at it instead of restating it, which is what stops two volunteers publishing two room numbers.
- **Timestamped updates on a fixed interval, including "no change".** Silence during an outage reads as abandonment. This is the single most transferable habit software has here.
- **A written resolution.** Saying when it ended, and what actually happened, closes the loop for people who only saw the problem.
- **Independence from the thing that broke.** A status page hosted on the failing infrastructure fails with it. At an event this means: not on the venue's wifi, not inside the app, editable from a phone.

What does **not** transfer:

- **The audience habit.** Software users are trained to check a status page. Event attendees are not, and will not learn it during a one-day event.
  - The page is therefore never a push channel - it is the destination a push points at. A page with no push in front of it reaches nobody.
- **The severity taxonomy.** Degraded/partial/major outage tiers describe a system with measurable availability. An event's disruptions are discrete and human-scale.
  - Forcing them into tiers adds a classification step during the minutes you have least of. Use the message classes instead.
- **The subscribe-for-updates model.** It assumes a long relationship with the service. Nobody subscribes to a two-day conference's status feed.
- **The post-incident review.** A public written post-mortem is a norm in software and a liability at an event, where the cause is frequently a person or a supplier. The event equivalent is an internal note that goes to `samber/dev-event-organizer-skills@event-debrief`, not a published page.
