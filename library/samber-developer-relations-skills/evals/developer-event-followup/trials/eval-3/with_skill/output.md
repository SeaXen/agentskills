**No. Send the slides, but don't add everyone to the newsletter.** The sign-up form said "get the workshop materials". Sending them is owed to all 45 people. The newsletter is a second purpose nobody agreed to, and it is the one thing in your plan that could cost you trust or deliverability.

Slides alone also end the journey at the slides. A workshop cohort already started building, so the stronger play is to finish the exercise with them and measure it. That is also what you can show your boss.

This is a draft built on assumptions. I did not have attendee jurisdictions, your activation event, or hours available. The questions at the end change some rows. This is not legal advice, so confirm the gate with your privacy owner.

## Do this week (about 2 hours total)

1. Tag the cohort: `evt-pycon-2026-rag` on the roster, credit codes and signups. About 15 min.
2. Dedupe the roster on email and match it against the CRM. About 20 min.
   - Existing customers go to the account owner.
   - Open deals go to the deal owner.
   - Earlier unsubscribes win over anything this event produced.
3. Grade from your notes. About 30 min.
   - Anyone you talked to who had a live retrieval problem and a named next step is A.
   - Anyone with a problem but no next step is B.
   - Everyone else is C. A roster row with no note stays C, because nothing in it can be personalized.
4. Send the A notes within 2 working days of the event closing. If you are past that, send anyway and say plainly when you met.
5. Send the workshop-continuation email below to all 45 within the week. About 30 min.
6. Publish a public recap (slides, repo, recording, top questions) with the newsletter opt-in on that page. About 1 hour.

## 1. Record inventory

| Source | Count | Grade |
|---|---|---|
| Workshop roster | 45 | C by default |
| Your own notes or conversations | unknown | upgrade to A/B only where a note proves it |

You have no scanner export, raffle or organizer list, so there is nothing else to gate.

## 2. Gate table

| Source | What they read | Jurisdiction | Requested reply | Marketing |
|---|---|---|---|---|
| Roster (sign-up form) | "get the workshop materials" | unknown, treat as prior-consent | yes, to all 45 | **no** |

PyCon US draws an international crowd. Any jurisdiction not confirmed defaults to prior consent.

- **Germany and the rest of the EU/EEA:** unsolicited marketing email needs consent. A sign-up for materials is not consent for a newsletter.
- **UK corporate addresses:** the email rule is looser, but the promise was still narrower than a newsletter. That means no.
- **US:** the law (CAN-SPAM) would allow it. Your sign-up line did not promise it, so this is a trust rule, not a legal one.
- **Personal addresses:** these are the riskiest for the UK and Canada.

Subscribing them all would be the "slides email that subscribes the reader" mistake. The opt-in link goes on the public recap page, not in the email. An email asking for consent can itself count as advertising under prior-consent rules.

## 3. Routing (A records only)

| Signal | Destination | Owner | Date |
|---|---|---|---|
| Building or evaluating a retrieval pipeline | Product path | you | within 2 working days |
| Stated buying need, budget or procurement question | Sales, in the same thread | named account owner | same time |
| Bug or missing feature | Engineering | triage owner | same time |
| Wants to contribute or speak | Community | community lead | within the week |
| Student or job seeker | Community only, never sales | community lead | within the week |

Hand a record to sales only when the person's own words asked for pricing, procurement or a buyer conversation.

## 4. Tracks per segment

- **A:** personal note, plus the activation path.
- **B and C:** activation path (the workshop-continuation email), plus the public recap.
- **Community invitation and nurture:** deleted until a basis exists.
- Ranking line: personal note > activation path > promised-item message > public recap.
- What moved it: Q3 (a purpose line of "materials") deleted nurture. An unknown Q4 deleted marketing for everyone. The workshop event type promoted the activation path.

## 5. Message drafts

**Personal note (A), from you, your own address:**

```
Subject: <their problem, in their words>

Hi <first name>,

At the workshop you mentioned <problem as they said it> on <their stack>.
Here is <the item you promised: a config, a snippet, a link>.
<Agreed next step: "I'll ping you Thursday to see if the index build ran">

<your name>
```

**Workshop continuation (B and C, and also part of A), from you personally:**

```
Subject: The retrieval workshop materials, and the step where we stopped

Hi <first name>,

Here are the materials you signed up for at PyCon US:
- Slides: <link>
- Repo with the finished pipeline: <link>
- Finish-the-exercise page, which starts at the step where the session
  ended: <link>
<If provisioned:> A sandbox is already set up for you with the code <code>.

If you get stuck, reply to this email. I read every reply.
This is the only email you'll get from me about the workshop.

<your name>
```

Rules for this email:

- It carries no pitch and no newsletter link.
- The sandbox line stays only if the sandbox or credit is part of the workshop materials. Otherwise it is a new purpose, so cut it.
- No unsubscribe footer is needed, because it is a requested reply. Include one if your privacy owner prefers.

Before sending, run both drafts through your humanizer skill.

**Public recap page** (publish it, don't email it):

- Slides, repo, recording.
- The 5 questions people asked most.
- A "get monthly updates" opt-in the visitor chooses to click.

## 6. Stop rules and suppression

- Send each B and C record at most one message, unless they reply or click.
- Stop and review the gate on the second spam complaint. Also stop if unsubscribes or "who are you" replies run above your last event. Count every negative signal, not complaints alone.
- Load the 45 into the CRM as non-marketing contacts with source, grade, purpose line ("get the workshop materials") and capture date. Importing is not sending. Do not bulk-enroll them in any marketing flow.
- Honour unsubscribes and objections immediately. Add them to a permanent suppression list. Owner: you, unless you name someone else.
- Agree a retention period for the roster with your privacy owner.

## 7. Measurement sheet (for your boss at day 60)

| Field | Value |
|---|---|
| Event, date closed | PyCon US workshop, `<date>` |
| Cohort tag | `evt-pycon-2026-rag` |
| Activation event | `<your definition: first successful query against a created index, or similar>` |
| Counts by grade | A `?`, B `?`, C `?` (total 45) |
| Messages sent per track | personal `?`, continuation 45, recap published |
| Replies to A notes, next steps done | `?` of `?` |
| Activated by day 30 / 60 / 90, per grade | fill at each date |
| Non-event baseline, same window | organic signups for the same period |
| Guardrails | complaints, unsubscribes, days to suppression |
| Opportunities sourced / influenced | report both |
| Threshold | **self-set**, from your last event or your blended acquisition cost |

- No published benchmark exists for event follow-up reply or activation rates. Say that in the report, and label your threshold as self-set.
- Workshops mostly influence deals. Don't claim "sourced" for an influenced deal, because that is the claim a CFO will test.
- Where attendees stall at the same exercise step, the workshop or the docs are broken. That finding is worth showing your boss too.

## What your boss sees at day 60

1. A cohort of 45 with a tag and grades.
2. Activation at day 30 and 60 beside a non-event baseline.
3. Replies and completed next steps on the A notes.
4. Influenced and sourced pipeline.
5. Guardrails showing no complaint damage, plus where attendees stalled.

## Questions that change the plan

1. **Where are the 45 based?** Any confirmed UK corporate, US or France addresses open specific rows. Everything else stays at no marketing.
2. **What counts as activation** in your product (API key, first query, first index)? Without a cohort tag and a defined activation event, drop the activation path and send the materials only.
3. **How many hours do you have?** Under an hour means you write only the A notes, and DevRel drafts the rest for your review.
4. **Is this a one-off or a series?** A series promotes the public recap, which compounds into the next edition.
5. **Do you have notes on who you actually spoke to?** Without them, everyone is C, and the personal-note track is empty.

Next: answer question 1 (where the 45 are based), and I'll fill the gate table row by row.