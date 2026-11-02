# Should Cobalt Conf mirror its stream to a second platform the whole time?

**Recommendation: no, don't mirror continuously.** Put the effort into what the Notion runbook probably lacks: a published fallback line, a rehearsed handoff, and someone watching the real output. If you want a second destination, keep it warm and silent, and only when one of the conditions below applies.

I couldn't open the Notion runbook, so I haven't judged its contents. I also don't know your answers to the interview in the virtual-event-production skill (the one the task pointed me to), so this answer states its assumptions and shows which answers would change it.

## Assumed posture

- **Interaction posture:** a feed people watch, with a chat space open only if someone can staff it.
- **Concurrent sessions:** one. This assumption matters because one moderator covering the whole event is enough for a single track.
- **Format and ticket:** the format is settled as fully virtual, and the ticket is free.

## 1. Why a permanent mirror is the wrong rung

The skill deletes this option from the menu instead of ranking it lower. It argues that a second live platform carrying the same sessions in parallel does two things:

- **It splits the audience.** Viewers, chat and questions end up on two platforms. Each speaker's Q&A reaches only half the room, and nobody sees the half that got no answer.
- **It doubles moderation.** A second chat means a second place to hold the code of conduct, and with one moderator you can't cover both.

A mirror also misses the failures most likely to hit you:

- **Speaker drops, speaker no-show, dead audio:** the mirror copies all three. The skill notes the production path hears the source, not the output, so a mirror carries dead audio just as faithfully.
- **Platform outage:** a mirror only helps if viewers know to switch and where. That is the fallback line, and the line works with or without the mirror.

## 2. What to do instead

In priority order:

1. **Publish a fallback line before the day.** One sentence, outside the stream platform, on the schedule page and in the chat space. It says where to look when the feed dies (for example "schedule page and email, updates within 5 minutes"). It costs a sentence and removes the worst minute of an outage, the one where everyone debugs their own connection.
2. **Rehearse one scenario, aloud.** The likeliest failure is a speaker's connection dropping mid-talk. Run it once with the moderator, a speaker and the host. Agree the moderator's exact first sentence, and have them say it.
3. **Read the Notion runbook aloud once.** The skill deletes "a contingency document nobody has read aloud," because when it's needed nobody can find it or knows their line. The runbook isn't worthless, but it only counts once the people named in it have run it.
   - Ask whether anyone besides you has read it.
   - Cut each role down to a one-page cue card of their own lines.
   - Keep a copy outside Notion in case the outage is wider than the stream.
4. **Name a technical watcher if any session can't be re-run.** This person watches the stream like an audience member, on a second device, and does nothing else.
5. **Rehearse on the platform the event actually runs on.** A tech check on any other tool is deleted from the skill's menu, because it tests nothing that matters.
6. **Cover the speaker cases.** Each speaker needs a home-setup note, and speakers with a live demo, an unknown connection or an unrepeatable session need an individual check plus an instructed local backup recording. Get consent for that file recorded with whoever owns your speaker agreements before it exists.

## 3. When a second destination is justified

The skill has a middle rung: a second stream target already live and silent, with the fallback line pointing at it. It is not a public mirror, so it doesn't split the audience. It is the first rung that puts a session back on air instead of explaining its absence.

Add it only if one of these is true:

- **A sponsor deliverable names the stream.** Which sponsors, if any, have this?
- **A session truly can't be rescheduled.** For example, a keynote with a guest on a fixed slot.
- **A previous edition's feed died and this edition is recurring.** Did Cobalt Conf's feed die before?

A refund-risk condition also exists in the skill, but a free ticket removes it.

If you add it, budget the uplink. A second target from one machine means double upload, and FOSDEM's published figure is 10 Mbit/s per stream, above a 2 Mbit/s floor that sacrifices resilience (my inference for your setup).

## 4. Questions that would change this answer

Normally I'd ask these one at a time. I'm giving all of them here, ordered by how much they move the answer:

1. **Is there a chat or Q&A surface, or is it a feed people watch?** If it's open, you need a named moderator for every session.
2. **Does any sponsor deliverable name the stream?** If so, the warm standby is justified.
3. **Has Cobalt Conf's feed died before, and will there be another edition?** Together these also justify the warm standby.
4. **Which sessions have a live demo, a speaker with an unknown connection, or no re-run option?** These get individual checks and local backups.
5. **How many people can do only production during a session?** If the answer is zero, drop the chat space and run a single one-way feed.

## 5. Checks and metrics

Gates to meet before the first session:

- Every speaker has joined the real platform at least once.
- A named person owns moderation, or chat is closed.
- The fallback line is published, and the person who will say it knows the sentence.

Metrics to record beforehand, all self-set rather than industry standards:

- **Time from feed drop to audience told.** This is the number the drill moves.
- **Sessions delivered with no audience-visible failure.** A session with no audio counts as a failure.

For each metric, write down what change it would trigger.

## 6. Budget note

The feed survives every budget tier. The chat space and its moderation are the first things a lean budget drops. A warm second destination, if you add it, costs organizer hours and uplink, not a contract.

Next, answer questions 1 to 3. I'd build the plan section by section from there: platform, speakers, moderation, drill, rehearsal date.