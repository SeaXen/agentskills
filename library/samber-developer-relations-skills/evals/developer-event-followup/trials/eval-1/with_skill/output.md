# KubeCon EU Amsterdam follow-up plan

**Answer for the CMO:** don't enrol the 412 scans in the nurture. Do these by Monday:
- Email the demo config to all 412 scans.
- Send personal notes to the ~30 real conversations.
- Import everyone into HubSpot as non-marketing contacts.

The nurture then runs only for people who opt in.

This plan is not legal advice. Have your privacy owner confirm the gate table before the first send.

## Why "B2B legitimate interest covers it" fails

- **Wrong law.** Marketing email to individuals falls under ePrivacy art. 13, which requires prior consent. GDPR legitimate interest is not the basis for it. The EDPB's legitimate-interest guidelines (1/2024, consultation draft, para 114) say so. Confirm the current text.
- **Germany (about 40% of your contacts).** UWG s.7 requires prior express consent, business recipients included. A scanned badge is not consent. Only a double opt-in counts as proof.
- **Rest of the EU (about 30%).** Treat as prior-consent until the privacy owner names the local rule. France allows some business prospecting under conditions, but only if people were informed at collection.
- **The promise is the second blocker.** The scanner said "Scan to get the demo config emailed to you." That is the purpose. A six-email nurture is a new purpose nobody heard.
- **The UK and US (about 30%).** The law may allow it: PECR doesn't cover corporate subscribers, and CAN-SPAM is opt-out. The promise doesn't allow it, so those contacts get no nurture either.
- **Result:** 0 of the 412 scans qualify for the nurture on scan alone.
- **Deliverability.** Every complaint lands on your sending domain and affects every later campaign. Company-domain mailboxes rarely report complaints, so you would see the damage late.

## 1. Record inventory

| Source | Count | Grade |
|---|---|---|
| Scanner export | 412 | C unless a note proves more |
| Engineers' Google Sheet | about 30 | not graded yet |

**Do first:**
1. Dedupe the scans on email.
2. Match them against HubSpot. An existing customer goes to the account owner, an open deal to the deal owner, and an earlier unsubscribe wins over anything from the event.
3. Grade the ~30 notes. A means they have the problem now, build or influence the decision, and agreed a named next step. B means they have the problem but no next step. C means curious or here for swag. Grade doubtful ones B.
4. Any scan with no note stays C.

## 2. Gate table

| Source | What they heard | Jurisdiction | Requested reply (config) | Marketing |
|---|---|---|---|---|
| Scanner, all 412 | "Scan to get the demo config emailed to you" | Germany, ~165 | Yes | No |
| | | Other EU, ~124 | Yes | No (prior-consent default) |
| | | UK, ~62 | Yes | No (the promise is narrower than PECR) |
| | | US, ~61 | Yes | No (law allows, promise doesn't) |
| Engineers' ~30 conversations | Unknown, must be asked | All | Yes | Only what the engineer actually said aloud, and never in Germany or the EU without consent |
| Organizer-supplied list | Unknown | All | n/a | Only if the organizer's notice allowed sharing with sponsors |

**Rules for filling it:**
- If nobody can say what was said at the booth, mark the purpose "none stated" and open no marketing track.
- If the scans came through the organizer's lead-retrieval app, get the organizer's sharing notice. With no sharing notice, return or delete the list and tell the organizer.
- The config is owed to every scan, C included. It is a reply to their request, so it carries no promotion.
- Do not send a "confirm your subscription" email to Germans. Your scanner text said config only, so that email would itself be a cold consent request and count as advertising.
- Put the opt-in on a public recap page instead.

## 3. Routing (A records)

| Signal in their words | Destination | Owner |
|---|---|---|
| Asked about pricing, procurement or a buyer conversation | Sales | named account owner |
| Building or evaluating, blocked | Product path | the engineer who met them |
| Bug or missing feature | Engineering | triage owner, link the note |
| Wants to contribute, speak or host | Community | community lead |
| Integration or reseller interest | Partnerships | partner manager |
| Existing customer or open deal | Account or deal owner | that owner |
| Student or job seeker | Community, never sales | community lead |

- Company size or cluster count alone is not a buying signal.
- Name an owner and a date per A record. Fill in the column once the sheet is graded.

## 4. Tracks per segment

| Segment | Tracks | Moved by |
|---|---|---|
| A (~30 max) | Personal note from the engineer. Sales handoff in the same thread, only if they asked for it. | Their own words |
| B | Promised-item message: the config, plus a cohort-tagged link to run it. | The scanner promise |
| C (~380) | Promised-item message (the config) and a public recap. | The scanner promise |
| Nurture (6 emails) | Opt-ins only (see below). | The gate table |

**Where the free tier helps:**
- The recap page offers the free-tier signup and a newsletter opt-in checkbox.
- A free-tier signup tied to a paid offering may open the EU soft opt-in. The CJEU said this in C-654/23, Inteligo Media, 13 Nov 2025, and read the exception narrowly.
- The privacy owner must confirm this before you rely on it. It needs an opt-out at collection and in every message.
- Anyone who ticks the box or signs up after opt-in feeds the nurture. The nurture stays; the cohort is just smaller than 412.

**Ranking line:** the usual order puts the nurture last, because it has the highest compliance cost and is hardest to undo. Q3 (the scanner text is narrower than marketing) deleted that track for scans.

## 5. Message drafts

Run each one through your humanizer skill before sending. Send from the person's own address, not marketing@.

**Personal note (A), from the engineer who met them:**

```
Subject: <their problem, in their words>

Hi <first name>,

We talked at KubeCon about <problem as they said it> on <their stack>.
As promised: <the config / item, attached or one link>.
<Agreed next step, e.g. "I'll ping you Thursday to see if it ran.">

<engineer name>
```

**Sales handoff, same thread, only where they asked:**

```
Hi <first name>, you asked about <pricing / procurement> at KubeCon.
I'm adding <account owner>, who handles that, so you don't have to repeat yourself.
I'll stay on the thread for the technical side.
```

**Promised-item message (B and C):**

```
Subject: The demo config from KubeCon

Hi <first name>,

Here's the demo config you asked for at KubeCon: <link>.
This is the only email you'll get from us about it.

<name, DevRel>
<one-line privacy notice link>
```

- It has no newsletter link, no demo-booking call to action and no "latest features."
- The privacy-notice link is there because EU people met this way are owed one no later than the first email.
- Drop "This is the only email" from C messages if you plan the recap to reach them elsewhere.

**Public recap:** publish a page with the config, repo, slides, and answers to the questions the booth heard most.
- Add the free-tier signup and an unticked newsletter checkbox.
- Do not email the link to the 412.

## 6. Stop rules and suppression

- **One message per B and C record,** unless they reply or click.
- **Stop the batch** on the second spam complaint. Also stop if unsubscribes or "who are you, remove me" replies run above what your last event produced. That threshold is this skill's rule, not a published one.
- **Import into HubSpot as non-marketing contacts.** Carry source, grade, purpose line, capture date and country. Enrolling in any marketing flow needs the gate's yes. Importing is not sending, but bulk enrolment is how the nurture reaches people the gate excluded.
- **Suppression owner:** name one person. Honour unsubscribes and objections at once and keep a permanent suppression list. The EU/UK right to object is absolute.
- **Retention:** agree with the privacy owner how long unanswered scan-only records stay.
- **Late A notes:** the target is two working days after the event closed. If you're past it, send anyway and say plainly when you met. Never skip the note.

## 7. Measurement sheet

| Field | Value |
|---|---|
| Event, date closed | KubeCon EU Amsterdam, `<closing date>` |
| Cohort tag | `evt-kubeconeu-2026` on signup and links (suggested name) |
| Activation event | Proposed: first cluster connected with cost data flowing. Confirm in Q6. |
| Counts by grade | A `<n>`, B `<n>`, C `<n>` |
| Reply rate to A notes | per owner |
| Activated by day 30 / 60 / 90 | per grade A, B, C |
| Non-event baseline | free-tier signups over the same window, other channels |
| Opportunities sourced / influenced | report both. Events mostly influence. |
| Guardrails | complaint rate, unsubscribes, max days to suppression |
| Threshold | set from your previous event or blended acquisition cost, labelled self-set |

- Read the 30-day numbers into the sponsorship review.
- Track activation separately for A, B and C.
- Don't cite the "respond within the hour" studies as evidence. They measured inbound web leads, not event contacts. Send A notes fast because memory fades, and say that.

## By Monday

Rough staff effort, my estimates:

1. **Today or tomorrow (about 1 hour):** dedupe and match against HubSpot. Grade the ~30 notes.
2. **With the privacy owner (about 1 hour):** confirm the gate table. Get the organizer's sharing notice. Ask each engineer what they said aloud.
3. **A notes (about 10 minutes each, so up to 5 hours across the engineers):** write and send. Do this before the rest of the log is clean.
4. **Config email (about 30 minutes):** send to all deduped scans.
5. **Recap page (2 to 3 hours):** publish with the opt-in.
6. **HubSpot:** import as non-marketing contacts. Build the opt-in-only enrolment.

## Tell the CMO

"All 412 get the demo config. That is what the scanner promised, so it's owed to everyone and costs nothing in risk. The ~30 conversations get personal notes. The 6-email nurture runs for anyone who opts in through the recap page, because a scan only covers the config. Enrolling everyone would put the sending domain at risk for every later campaign, and in Germany it is simply not allowed."

## Questions I need to finish the plan

1. What did each engineer say aloud when they took details? Did anyone say "I'll add you to updates" or similar?
2. Did the scans come through the organizer's app? Can you share the organizer's notice?
3. Was there a raffle or draw? If so, bring the form text.
4. What is your activation event, and can you tag an event cohort in product data?
5. By what date must a result show (a sponsorship review, a quarter close)? Is this a one-off or a series?
6. How many hours can the engineers give this week, and who owns follow-up after that?

My assumptions until you answer: the scans are all C with no purpose beyond the config, and the engineers promised only the items in their notes.