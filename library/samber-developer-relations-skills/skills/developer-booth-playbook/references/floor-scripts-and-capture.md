# Floor scripts and capture

Contents: floor scripts → consent lines → record schema → graded examples → end-of-shift log → same-day debrief.

## Floor scripts

Adapt the words; keep the order.

**Opener** - about their work, never about the product:

- "What are you building at the moment?"
- "What's the most annoying part of [the problem space the booth is about] for your team right now?"

**Three qualifying questions** - each answers one field of the record:

1. "How do you handle that today?" → current stack and pain.
2. "Who else on your team deals with it?" → role and whether they champion or decide.
3. "Would it help to [concrete next step] next week?" → the next step, or a clear no.

**Hand-off** (DevRel to engineer, or to account executive):

- "Priya built the part you're asking about. Priya, they're running [stack] and hitting [problem]."

**Polite exit** - for a C, or once the next step is agreed:

- "I don't want to keep you from the sessions. Here's [ambient item]; the docs page for what we sketched is on the card."
- "Sounds like we're not the fit for this one. [Other approach] is worth a look."

## Purpose lines

Say what the details are for, matching the record's next step and route. Never promise "nothing else" and then route the record to sales or a nurture sequence: the promise is the purpose, and breaking it breaks trust and, at EU events, purpose limitation.

- Scanner: "Can I scan your badge? I'll send the config we sketched, and our solutions engineer will follow up about the trial. Privacy details are on this card."
- Draw: "The draw is separate. Entering only puts you in the draw, unless you tick the box for updates."
- Hand log at a no-scanner event: "Can I note your email to send that over, and check in after you've tried it? The card has how we handle it."

Hand every person whose details you take a card or link to your privacy notice. Agree the legal basis per event with your privacy owner before the show, and write it in the record.

## Record schema

| Field           | Example                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| grade           | A / B / C                                                                                                 |
| problem         | in the attendee's words                                                                                   |
| stack           | languages, platform, current tool                                                                         |
| role            | builds, champions, decides                                                                                |
| next step       | concrete, dated                                                                                           |
| owner           | the staffer who promised it                                                                               |
| route           | self-serve invite, sales, product, engineering, partnerships, recruiting, community                       |
| consent basis   | what the attendee agreed to, in their hearing, plus the legal basis your privacy owner set for this event |
| captured by, at | name, shift                                                                                               |

Grades: A = has the problem now, builds with or influences the decision, and agreed a named next step. B = has the problem, no next step yet. C = curious, learning, here for swag. Only A counts toward the threshold; B is reported beside it as warm interest.

## Graded examples

Constructed for illustration.

```
// ✓ A - problem, stack, decision role, dated next step, owner
grade A | "staging DB refresh takes a day, blocks every release" | Postgres 15, Terraform, EKS |
champions, platform lead signs | trial with event credit + 30-min call Tue 10:00 | Priya |
self-serve invite + engineering | scan purpose said aloud: config + trial follow-up

// ✓ C - logged honestly, no follow-up promised
grade C | student, learning Kubernetes | - | - | none | - | community | took sticker, no data

// ✗ - scan only, no note, cannot be graded or followed up
scan #0412 | "great chat!!"
```

## End-of-shift log

Five minutes before handing over, the outgoing shift:

1. Completes every record started on the shift.
2. Counts A, B and C for the shift.
3. Notes the questions the booth could not answer.
4. Passes open conversations to the incoming shift by name.

A shift that skipped its log reconstructs its A and B records that same evening, before memory fades; a record rebuilt next week is fiction.

End of day one, the captain reads the counts against the daily share of the minimum and changes day two:

- A count well under the daily share → move engineers onto peak blocks and rewrite the opener toward the problem.
- Visitors left a queue → fill the optional peak slot.
- C share dominates → move the ambient item off the front edge so the opener comes before the sticker, and keep the earned item behind the counter.
- Same unanswered question three times → write the answer on a card, send it to docs.

## Same-day debrief

Thirty minutes, the day the hall closes, everyone who worked a shift:

- A count against the minimum, pass or miss; B count beside it.
- Scan count, reported as activity beside it.
- Top three questions the booth could not answer → product and docs.
- What to change next edition: crew, grid, scripts, swag.
- Handover: the graded log, each A with its owner and date, goes to follow-up.
