# Fixing event lead conversion: follow-up plan for an observability platform

## Verdict on the CEO's plan

**Don't send the 5-email/30-day sequence to everyone within 24 hours.** Send a personal note to the people you actually talked with, within two working days. Send everyone else at most one message.

- **The 80% statistic can't back the plan.** I found no published study behind "80% of trade show leads are never followed up", and industry write-ups report CEIR disowning it. Don't put it in a deck.
- **The speed research doesn't apply either.** The "respond within the hour" studies measured inbound web leads. None sampled booth contacts.
- **Speed still matters for one reason.** Memory fades, so the A-grade notes (defined below) should go out fast. That is the argument to give the CEO.
- **The blast is a risk.** A scan records presence, not intent. Developers name "people who scanned my badge at a conference" as a spam source. Every complaint lands on your sending domain, and the domain pays for all 9 events next year.
- **A sequence is probably not why last year failed.** Event leads usually fail to convert because the capture had no notes or grades, nothing was routed to an owner, and nobody measured the cohort. More emails don't fix that. I haven't seen your records, so this is a hypothesis. Step 1 tests it.

## Assumptions

I couldn't interview you, so these are my defaults. Correct any that are wrong and the plan re-ranks.

| # | Assumption | What moves if wrong |
|---|---|---|
| 1 | Mostly booth scans at 9 conferences, with unknown or thin notes | If a graded log exists, copy its grades |
| 2 | Purpose line unknown, so treated as "none stated" | A scanner screen saying "updates" reopens the nurture track for those records |
| 3 | Contacts include EU/Germany, so prior-consent is the default | A US-only list opens opt-out marketing (CAN-SPAM) |
| 4 | Developers with a card are your main buyers, with a sales team for enterprise | If buyers rarely touch the product, promote the sales handoff for A records with a stated buying need |
| 5 | Activation is the first successful data ingest (first agent or SDK sending telemetry), and you can tag an event cohort | If you can't tag a cohort, ship the promised-item message instead of an activation path |
| 6 | You run a series, not a one-off | Series promotes the public recap and community invitation |
| 7 | Staffers give under 1 hour each | Staffers write only the A messages. DevRel drafts the rest for their review |

## 1. Record inventory (do this first)

1. Pull every source per event: scanner exports, raffle entries, sign-up sheets, staff notes, any organizer-handed list.
2. Dedupe on email, then match against the CRM. Existing customers go to the account owner. Open deals go to the deal owner. An earlier unsubscribe or objection wins over anything the event produced.
3. Grade A/B/C:
   - **A:** has the problem now, builds or influences the decision, agreed a named next step.
   - **B:** has the problem but no next step.
   - **C:** curious, learning, or there for the swag.
4. Grade notes without grades yourself, and grade a doubtful one B. Raffle-only, scan-only and sign-up-sheet records are C unless a note proves more. A scan with no note stays C, because nothing in it can be personalized.
5. Count last year's 9 events by source and grade. If most records are scan-only with no notes, you have found the real cause.

**Last year's lists.** They are stale, so don't blast them. Do run this retro check once: match last year's scan emails against product signups, activation and CRM opportunities. That gives you your own baseline and tells you which events produced anything.

## 2. Gate table

Fill one row per source, copying the purpose line verbatim. This is a framework for your privacy owner, not legal advice.

| Source | Purpose line heard | Jurisdiction | Requested reply | Marketing |
|---|---|---|---|---|
| Staff conversation (A/B) | Their own promise, e.g. "I'll send the config" | Any | Yes | Only if "updates" was said aloud, with an objection link on every message |
| Scanner export | Paste the scanner screen text | Germany/EU | Yes, if an item was promised | No, without a consent you can show |
| Scanner export | Same | US | Yes | Only within what the screen said. CAN-SPAM opt-out and postal address required |
| Raffle entries | "Entry only puts you in the draw" | Any | No request made | No. Never reuse a draw entry |
| Organizer list | Paste the organizer's notice | EU/UK | Nothing requested | No, unless the consent named your company ("sponsors" wording isn't valid) |
| Organizer list | Same | US | Nothing requested | Within the notice only |

Rules that decide the table:

- **Marketing needs two yeses:** the jurisdiction allows it, and what staff said covers it. A scan taken for "the config" gets the config and no nurture, even in the US. There the law allows it but the promise doesn't.
- **A requested reply is owed at every grade.** If the scanner promised "we'll email you the dashboard template", every scan gets it.
- **Unlisted jurisdictions** are treated as prior-consent until your privacy owner names the rule. Germany needs double opt-in. France allows business prospecting on legitimate interest under conditions.
- **Gate the A rows first.** It takes minutes and must not delay them.

## 3. Routing (A records)

Hand a record to sales only when the buying signal is in the attendee's own words. Company size is not a signal.

| Signal in the note | Destination | Owner |
|---|---|---|
| Asked about pricing, procurement, SSO or a buyer conversation | Sales | Named account owner |
| Building with the product, blocked, or evaluating | Product path | The staffer who met them |
| Bug or missing integration | Engineering | Triage owner, with the note linked |
| Wants to contribute, speak or host | Community | Community lead |
| Integration or reseller interest | Partnerships | Partner manager |
| Existing customer or open deal | Account or deal owner | That owner |
| Student or job seeker | Community, never sales | Community lead |
| C with no note | Public recap, plus anything the capture promised | DevRel |

Each A record gets a named owner and a send date within two working days of the show closing. If you're already past that window, send anyway and say plainly when you met.

## 4. Tracks per segment

Ranking line: **public recap > promised-item message > personal note > community invitation > activation path > sales handoff > nurture sequence**. This is the efficiency order. Value order puts the personal note first.

| Segment | Track | What moved it |
|---|---|---|
| A | Personal note from the staffer who met them. Sales handoff in the same thread only if they asked for buying help | Assumption 4 and the stated-need rule |
| B | One promised-item message, no second email unless they reply or click | Default for B |
| C | Public recap, plus any promised item | Default for C, and assumption 6 (series) |
| Product-path people (A or B) | Activation path: a "finish your first ingest" page with an event credit. Needs a cohort tag | Promoted only because assumption 5 says activation is measurable |
| Anyone whose basis covers it | Community invitation, sent once | Assumption 6 (series) |
| Nurture sequence | **Deleted** for raffle-only, scan-only with a narrower purpose, and EU/Germany without consent | Gate. Only records whose capture said "updates" or whose consent you can show qualify |

What the CEO gets from this is a short 1-2 email sequence on the records where it is allowed, not 5 emails to everyone. The 5-email/30-day sequence stays only for records that pass the gate (the updates-purpose and shown-consent group above).

## 5. Message drafts

Run each through your humanizer skill before sending. Send from the person's own address, never a marketing alias.

**Personal note (A):**
```
Subject: alert noise from your Kubernetes metrics

Hi Ana,

We talked at <event> about the alert noise on your EKS clusters,
and how on-call can't tell real incidents from flapping pods.
As promised: the alert-routing config we sketched, plus a 30-day event credit.
I'll check in Thursday to see if it ran.

Priya
```

**Promised-item message (B):**
```
Subject: The dashboard template from <event>

Hi Sam,

Here's the dashboard template you asked for at <event>: <link>.
This is the only email you'll get from me about it.

Priya
```
Add an opt-in line only where the gate's marketing column says yes. Elsewhere, put the opt-in on the public recap page. An email asking for consent can itself count as advertising.

**Sales handoff (A with a stated buying need, same thread):**
```
Hi Ana, you asked about SSO and procurement at <event>.
I'm adding Marcus, who handles that, so you don't have to repeat yourself.
I'll stay on the thread for the technical side.
```

**Community invitation (marketing, so it needs a basis):**
```
Subject: Where people tuning alert noise compare notes

Hi Ana, you mentioned alert fatigue at <event>. <N> people building the same
thing talk in <community>: <link>. Next office hours: <date>.

<sender identification + postal address + unsubscribe link>
```

**Public recap (no contact data needed):** one post with slides, the repo or config, the recording, and answers to the 5 questions the booth heard most. Publish it where developers already read. Send the link to nobody.

## 6. Stop rules and suppression

- **One message per B and C record,** unless they reply or click the opt-in.
- **Stop the batch on the second spam complaint.** Also stop if unsubscribes or "who are you, remove me" replies run above what the last event produced. This is the skill's own threshold, not a published one. Company-domain mailboxes rarely report complaints back, so count every visible negative.
- **Load records into the CRM as non-marketing contacts** carrying source, grade, purpose line and capture date. Enrolling in a marketing flow requires the gate's yes. Importing is not sending.
- **Never import a bought or scraped list,** and never reuse a raffle entry alone for marketing.
- **Organizer lists:** use them only within their notice. A list with no sharing notice gets returned or deleted. In the EU, send your own privacy notice by your first email at the latest.
- **Honour unsubscribes at once** and add them to a permanent suppression list. Name one suppression owner.
- **Retention:** raffle data goes once the prize ships. Agree the period for unanswered scan-only records with your privacy owner.

## 7. Measurement sheet

Fix this before the first send:

| Field | Value |
|---|---|
| Cohort tag | `evt-<name>-<year>` on signup links and credit codes |
| Activation event | First successful telemetry ingest (assumption 5) |
| Counts by grade | A / B / C per event |
| Messages sent per track | Personal, promised item, recap |
| Replies to A notes | X of Y, plus next steps completed per owner |
| Activated by day 30 / 60 / 90 | Per grade, beside a non-event baseline (same-month organic signups) |
| Complaint rate, unsubscribes, days to suppression | Guardrails, not goals |
| Opportunities sourced / influenced | Report both. Events mostly influence, and a CFO will test any "sourced" claim |
| Threshold | Self-set from last year's retro, or your blended acquisition cost. Label it self-set, since no published benchmark exists for event follow-up |

Send the 30-day readings to the sponsorship review in `developer-event-sponsorship`, and roll the program view into `devrel-metrics`. After the retro check, use that data to decide which of the 9 events deserve a renewal.

## What to tell the CEO

- "The 80% figure has no published source, so I won't build on it."
- "I'm following up fast, within two working days, with the people who told us they have the problem. That's where conversion comes from."
- "Everyone else gets what we promised them, once, plus a public recap. A blast to scan-only contacts, especially in the EU, risks complaints that hurt every email we send next year."
- "We'll measure activation and influenced pipeline per event at 30, 60 and 90 days. By the next sponsorship review we'll know which shows to keep."

## Questions that would change the plan

1. What did staff say when they scanned? Paste the scanner screen text.
2. What fraction of last year's scans have a note?
3. Which countries are the contacts in?
4. Can you tag an event cohort in product data?
5. How many hours can each staffer give this week, and who owns follow-up after that?