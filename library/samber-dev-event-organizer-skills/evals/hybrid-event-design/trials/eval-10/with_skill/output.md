**Don't build the separate remote agenda page.** Start with one question: what was the remote audience promised, and to whom? Everything else is ranked against that answer.

## Step 1: Answer Q1 before touching the site

Pick one:

- A. A paid virtual ticket.
- B. A sponsor deliverable that names the stream.
- C. An access commitment to people who can't travel.
- D. Nothing written down. Marketing just said "hybrid".

Then write the answer as one sentence. Every later choice is measured against it, not against what's technically possible. I can't answer this for you, and it decides most of the plan below.

I treated the format decision as closed because Marketing made it. I won't re-argue hybrid. If it's still open, that goes to `event-format-selection` first.

## Step 2: Why the separate page is the wrong move

- A separate remote agenda is a second document with a second update path. The update that gets missed is always on the document fewer people open.
- That is the documented failure shape: a session slips in the room and the remote side is never told.
- Instead, add a remote column to the grid you already published. For each session it holds:
  - **eligible / not eligible**,
  - **the return path**, if it differs from the event default,
  - **the named person on the remote side**, or an explicit **"closed"**.
- "Closed" matters. It separates "deliberately no remote path" from "nobody has looked at this row".
- If the cleanliness of the public page is the real worry, render the column as a badge or filter on the same grid page. Don't hand-maintain a second page. That rendering suggestion is my extension, not the skill's. A view generated from the same data is fine. A page someone edits by hand is not.

## Step 3: Your two facts, handled

**The two speakers who don't want to be streamed.**
- Mark those sessions **not eligible** and log the declines.
- This kills the "every session in every room" option.
- Check with whoever holds the consent record (`event-speaker-experience`). Does every other eligible speaker's consent cover a *live* feed, or only a recording? Those are different permissions.
- A speaker's opt-out has to be honoured in the room, not fixed in an edit. A published stream can't be recalled.

**The Thursday hands-on workshop block.**
- Live Q&A was never their shape, so don't build live parity for them.
- The fit is the **asynchronous written return path**. It must state who answers, by when, and where the answer appears. Without those three, it's just an unread question channel.
- If nobody can be named for a session, drop to **feed only** with one published line saying questions aren't taken live.
- Never leave an open question channel that nobody reads. It invites a question and drops it in front of the person who asked.
- Also ask whether these rooms should be streamed at all. Hands-on sessions put the in-room audience on camera.
- Tell remote attendees out loud *and* in text when a workshop overruns. That is the documented failure.

## Step 4: Defaults to start from (change them after Q1)

I'm assuming the Q2 answer, how many rooms can carry a feed, is more than one. Q2 is one of your open questions.

| Menu | Default | Moves up when |
|---|---|---|
| Eligibility | **One designated streamed room**. A room-booking question the grid already answered. | Q1 is A or B (paid or promised specific content): **curated remote programme** |
| Eligibility (minimum) | **Plenary only** | Q1 is D: this is the honest choice |
| Parity | **Live relay by a named person** | Q1 says the ticket was sold on participation: remote participants appear in the room |
| Staffing | **One named advocate per streamed session** | More than one room streams at once: add a watcher off the floor |

- **Per-session opt-in** is strictly dominated by a curated programme. Skip it unless your consent record already hands it to you.
- **Staffing:** the room lead cannot double as the remote advocate. Both jobs come due at the same moment, so one gets dropped.
- **Unstaffed sessions:** if a session has no named person, give it feed only.
- I've invented no ratios or thresholds. None exist.

## Step 5: Do this before Marketing announces anything

- Removing a session from the remote programme after it's public is a retraction, not a decision.
- Your grid is public but has no remote promise on it yet, so you're still free to decide. Settle Q1, eligibility and consent first. Only then publish the column and the "hybrid" announcement.
- Tell Marketing not to imply "all sessions streamed".

## Order of work

1. **Q1:** state what was promised, in one sentence.
2. **Menu 1:** pick the eligibility rung and mark the column. The two declines and the workshop block are the first entries.
3. **Consent:** confirm live-feed coverage with the consent record's holder.
4. **Menu 2:** set parity depth per rung. Workshops get the async path or feed only.
5. **Handoff:** give `event-production` the list of eligible sessions and the return path, not equipment.
6. **Staffing:** assign names per streamed session.
7. **Cue track:** hand `event-run-of-show` a stream column on its existing rows. Give every break a holding card, and flag every row where the room is told something out loud.
8. **Disruption order:** write down who decides when a remote failure and an in-room one compete. Also decide whether a moved session keeps its remote slot. Neither has an inherited answer.
9. **Budget:** report the staffing cost to `event-budget`. A lean tier cuts the return path and the people watching it first.

## Questions to answer next

Answer these one at a time:

1. **Q1** (above): what was promised?
2. **Q2:** how many rooms run at once, and how many can physically carry a feed?
3. **Q7:** what is the last date a session can join or leave the remote programme?
4. **Q9:** how many people can work the remote side alone during a session?

Start with Q1.