# Expedition brief: Streamhaven CI, Denver platform engineering meetup

## Bottom line

❌ **Don't plan a visit day.** ✅ Invite your friend to speak or sit in a fireside Q&A in a room you already control.

Three of your answers decide this:

- **Nothing physical needs to be seen.** You said it's a normal office and the value is in how they work. That removes the main reason to travel.
- **Your question is specific.** Merge queue and flaky-test quarantine is a question your members can push a named engineer on. The skill says to recommend the in-room session and stop in this case, not to design travel around a conversation that fits in a session.
- **Your friend can't commit his teammates.** That deletes the negotiated-agenda visit. What's left is a host-led tour of an ordinary office, which is the weakest option for you.

I've answered the interview from what you wrote. The "Flip conditions" section lists the answers that would change this.

## 1. Routing: what belongs to other skills

| Item | Owner |
|---|---|
| Whether this is the right format at all, and who to invite | `event-learning-expedition-design`'s scope rules send it to `business-event-formats` |
| Your room, AV, and capacity for 120 | `event-venue-sourcing` |
| Code of conduct clause (your room only, since there's no coach or host floor) | `event-code-of-conduct` |
| Food and drink | `event-hospitality`, then `event-vendor-sourcing` |
| Recording the talk and publishing it | `event-production`, then `event-content-repurposing` |
| Goals and measurement | `corporate-event-strategy` |

## 2. Host-dependency posture

Chosen: **host representative in your own room**.

| Rung | Status | Why |
|---|---|---|
| Host rep in your own room | ✅ Recommended | Q3 is a specific technical question, and this rung has the best fit per unit effort. Q2 names no physical thing, so the rung survives. |
| One host site, host-led | ⚠️ Fallback only | It needs a yes from someone who speaks for Streamhaven, and you have none. The audience would see an ordinary office and hear a generic tour. |
| One host site, negotiated agenda | ❌ Deleted | Q4: your friend speaks only for himself, so no counterpart can commit colleagues' time. Without one, it's the host-led rung plus meetings, the worst cell on the menu. |
| Multi-host circuit | ❌ Not considered | It needs standing relationships with several hosts (Q9) and runway to survive a withdrawal (Q8). You have one personal relationship. |

A note on the 120 attendees: a group that size in a working office is the host's call. Don't pitch it until Streamhaven states what it can host.

## 3. Access and repeatability posture

Chosen: **named ground rules, no instrument**. This is the default, and no instrument is needed for a talk.

- **Restriction list so far: empty, and unverified.** Nobody who speaks for Streamhaven has stated a restriction (Q5). Don't assume one, and don't assume there is none. Silence is not permission.
- **Ask your friend to get these answered**, from his manager or the company's comms or legal people:
  1. May he present this publicly at all, as himself?
  2. Which parts of the merge queue and quarantine setup are already public, such as engineering blog posts and conference talks, and which are internal?
  3. May the session be recorded and published?
  4. May attendees attribute statements to him or to Streamhaven?
- **Draft rules, to publish to attendees before the day (not at the door):**
  - No slides or screens are photographed unless the speaker says so.
  - Nothing is attributed to Streamhaven, only to "an engineer who has run this."
  - Recording and publishing are decided by the speaker and his employer, not by you.
- **Rung deletions:**
  - *Open on the record* is cut only if Q5 yields a restriction from someone who speaks for Streamhaven. Keep it if he sticks to material Streamhaven has already published.
  - *Per-attendee written undertaking* is not needed for a talk. It only matters if Streamhaven asks for it as a condition (Q1) and your attendee list is bounded before the day (Q6).
  - *Host-controlled, organizer-relayed clearance* is deleted until you name a person who will run that queue (Q7).

## 4. What to ask your friend to show

You can't ask to *see* things in the office. Ask him to *show and tell* things that fit on a screen. These are asks, not promises. He decides what he can share.

**Merge queue**
- How a change moves from approval to merge: batching, speculative builds, and what happens when a batch fails.
- The failure that taught them the most, told as a story rather than a configuration dump.
- What they tried and abandoned.
- A redacted dashboard or diagram if he's allowed one.

**Flaky-test quarantine**
- How a test gets flagged, quarantined, and released, and who owns each step.
- What stops quarantine from becoming a graveyard of ignored tests.
- How they handle the trade-off between blocking developers and hiding real failures.
- A redacted example of a quarantine decision, if permitted.

**Both**
- What he'd do differently starting over.
- Which parts are tied to Streamhaven's scale and which a team of ten could copy.

**Format:** a moderated conversation rather than slides, so your members can push him. Collect questions from members beforehand and have a moderator who knows the topic.

If he can bring a colleague *voluntarily*, great, but treat it as a bonus and don't put it on the flyer.

## 5. Host brief (draft to send your friend)

> **What the audience is coming to understand:** how a large organization keeps a merge queue fast and trustworthy, and how it keeps flaky tests from eroding trust in CI.
>
> **What we're asking of you:** speak for yourself, in our room in Denver, about the above. We're not asking you to represent Streamhaven or commit anyone else.
>
> **What we've told attendees they may repeat:** only what you say you're comfortable with being repeated, plus anything already public. We will not record or publish without your explicit, written okay and your employer's.
>
> **Before we announce anything:** please check with your manager or comms/legal contact whether you may do this, and tell us what restrictions apply. We'll go with whatever they decide.

Send this before he starts any internal approval, and send it as a draft he can edit.

## 6. Handoffs

- `event-venue-sourcing`: your room and its requirements sheet.
- `event-code-of-conduct`: a scope clause covering your room and any online stream. No vehicle, so no transport clause.
- `event-hospitality` and `event-vendor-sourcing`: only if you serve food.
- `event-production`: recording, only after the speaker and his employer say yes in writing.
- `corporate-event-strategy`: goals and measurement.

## 7. Flip conditions

| Choice | Flips if... |
|---|---|
| In-room session instead of a visit | Streamhaven itself, through someone who speaks for the company, invites your group in writing (Q1) and a colleague can commit time (Q4). Then reconsider the negotiated-agenda rung. |
| Same | Your members need to see something physical, such as a build-farm room or hardware (Q2). That keeps the visit rung alive. |
| Ground rules, not a bare open record | Your friend confirms in writing that everything he'll cover is already public. Then open on the record is fine. |
| Ground rules, not an undertaking | Streamhaven requires signatures (Q1) and you have a bounded list (Q6). |
| No clearance queue | You name a person who will still be doing it when requests arrive (Q7). |
| Single host, not a circuit | You gain standing relationships at other companies (Q9) and enough runway (Q8). |

## 8. Pass threshold: not yet met

Before you tell anyone where they're going, these four must exist in writing, with no blanks:

| Item | Status |
|---|---|
| The host's yes, and any condition | ❌ Blank. Your friend's enthusiasm is not Streamhaven's yes. |
| Named counterpart inside the host | ⚠️ Your friend, but only for himself. |
| Access posture with restriction list | ⚠️ Posture drafted, restriction list empty. |
| Person who handles publishing requests afterwards | ❌ Blank. Name one. |

These gates are self-set, not external benchmarks.

## 9. Next steps

1. Send your friend the brief in section 5.
2. Name the person who handles publishing requests.
3. Get his answers to the four restriction questions.
4. Pick a date and room only after he reports back.
5. Record afterwards whether Streamhaven would receive you again. That relationship is the only thing that carries over to the next event.

Nothing here should be promised to your members until sections 5 and 8 are validated.