**Recommendation:** don't run a public mirror the whole time. Run a silent, unlisted backup stream and share its link only if the primary fails. It costs you very little and splits nobody's audience.

**Why not a full public mirror**
- **It doesn't cover your likely failures.** Platform-wide outages are rare and usually short. A dead encoder, a home-internet drop, a lost mic or a speaker problem is more likely. If the mirror comes from the same encoder or uplink, it dies with the primary.
- **It splits the room.** With 400 people on one track, two public streams mean two chats, two Q&A queues and two sets of stats. Moderation doubles and attendees wonder which one is "real".
- **Switching depends on telling people.** If the primary dies, attendees won't see a banner on it. A mirror helps only if you can reach them somewhere else, like email, your Discord or Slack, or social.
- **It adds load.** Sending to two platforms from one machine doubles your upload bandwidth and CPU, unless you use a relay service, which is its own extra dependency.

**What I'd do instead**
1. **Make your own URL the single entry point.** Send everyone to a link you control, such as `cobalt.conf/live`, and have it redirect to the stream. On failure you repoint the link, and nobody has to find a new URL. This is the highest-value fix.
2. **Run a silent mirror.** Stream continuously to a second platform as unlisted or private, from a second encoder or a relay if you can. When the primary dies, you repoint the link and send one announcement.
3. **Pick a different platform for the backup.** A backup on the same provider fails with the primary.
4. **Set a trigger and an owner.** Write a rule like "primary down for more than 2 minutes means the stream lead repoints the link". Also name one person who sends the announcement through email and chat.
5. **Rehearse it once.** Do a full failover during your tech check, with a timer. Aim for under 3 minutes from decision to viewers on the backup.

**When a public mirror is justified**
- A sponsor contract promises uptime.
- Your primary platform has a bad track record for you.
- Ticket revenue depends on the stream.

None of these seems to apply to a free event, and a free event also forgives a 5 to 10 minute gap, especially with recordings available afterward.

**About the runbook**
I can't open the Notion page, so I haven't read it. A 14-page runbook is only as good as its decision thresholds, owners and rehearsal. Check that it names who declares an incident, how attendees get told when the stream is down, and that someone has run through it. If you paste the failure sections here, I'll review them against this plan.

**Questions that would change my answer**
- Which platform is the primary, and how does the encoder reach it?
- Do you already have an email list or chat channel for attendees?
- Is there a second person who can run the backup, or is it just you?