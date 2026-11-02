# Post-re:Invent follow-up plan: don't send to everyone tomorrow

**Do now (about 30 minutes):**
1. Get the organizer's sharing notice for the 3,000-person list. Everything on that list is on hold until you've read it.
2. Split the 520 scans by country using the scanner export's country field, or the email domain if there isn't one.
3. Tell marketing that tomorrow's send goes only to the segments marked "send" below. Sending one blast to all ~3,500 contacts is what puts your main domain's reputation at risk.

I read `developer-event-followup` and both its references. Its interview needs your answers to Q1–Q4 (event dates, record sources, purpose lines, jurisdictions). I have only partial answers, so the assumptions are marked below. I haven't treated any of this as legal advice. Your privacy owner signs off on the gate rows.

## 1. Record inventory

| Source | Count | Grade | Notes |
|---|---|---|---|
| Badge scans | 520 | All C unless booth notes exist | A scan with no note stays C and can't be personalized. |
| – Germany | ~156 (30%) | C | |
| – Brazil, Japan | unknown | C | Not in the skill's jurisdiction table. |
| – US | unknown | C | |
| – UK | unknown | C | Many on gmail. |
| Organizer list | 3,000 | None | Basis unknown until I see the notice. |

Assumption: no graded booth log exists. **If staff took notes or agreed next steps with anyone, those are A or B records.** Send those people personal notes within two working days of the event closing, before any of this cleanup.

Before any send:
- Dedupe on email across scans and the organizer list.
- Match both against the CRM. Customers go to the account owner, open deals go to the deal owner, and earlier unsubscribes or objections win over anything the event produced.

## 2. Gate table

The scanner screen said "Scan to get product updates from Acme." That purpose covers product updates, so a launch announcement fits it. It does not by itself give every jurisdiction a valid basis. Marketing needs two yeses: the law allows it and the promise covers it.

| Source | Heard | Jurisdiction | Requested reply | Marketing |
|---|---|---|---|---|
| Scans | "get product updates from Acme" | US | Nothing requested | **Yes.** One product-update email within the purpose. CAN-SPAM needs accurate headers, a postal address, and an opt-out honored within 10 business days. |
| Scans | same | UK, corporate address (limited company) | Nothing requested | **Yes.** PECR doesn't apply to corporate subscribers. Add a privacy notice and an objection link. |
| Scans | same | UK, gmail or other personal address | Nothing requested | **Not tomorrow.** Treat as an individual subscriber, who needs consent or soft opt-in. A scan is not a sale, so soft opt-in doesn't apply. Your privacy owner decides whether the screen counts as logged, specific consent. If not, use the double opt-in below. |
| Scans | same | UK, unclear whether corporate | Nothing requested | Same as UK personal. When you can't tell, treat it as an individual. |
| Scans | same | Germany | Nothing requested | **No marketing without a consent you can show.** The scan counts as a request for updates, so it qualifies for a double opt-in. Only those who click get the launch email. |
| Scans | same | Brazil, Japan | Nothing requested | **Hold.** Not in the skill's table, so treat as prior-consent until the privacy owner names the local rule. Use double opt-in if they approve it. |
| Organizer list | Unknown | Mixed | Nothing requested | **No send.** See section 2a. |

If a scan also entered a draw, the entry adds no marketing basis. Only a separately ticked opt-in would.

Unfilled gate rows, which block the plan:
1. The exact scanner screen text (you gave it; keep a screenshot on file).
2. The organizer's sharing notice.
3. The country count per segment.

### 2a. The 3,000-person organizer list

"Opt-in" is not enough to send. The list is usable only within what the organizer's notice told attendees about sharing with sponsors. Find out opt-in to what.

| If the notice says | Then |
|---|---|
| No sharing notice, or you can't find one | **Don't import.** Return or delete the list and tell the organizer. |
| "Shared with sponsors for product updates" | US contacts: a launch announcement is within it, with CAN-SPAM compliance. EU and UK contacts: **no**, unless the consent named Acme. Wording like "sponsors" or "partners" is not valid consent. |
| Names Acme specifically | Usable for what it describes, in any jurisdiction. |

Also:
- The organizer's registration consent covers the organizer sharing data with you. It does not cover every message you send.
- For EU contacts you owe your own privacy notice no later than the first email, and within a month in any case.
- A launch email sent to the whole list tomorrow, without reading the notice, would be the sort of spam source developers name publicly.
- Load these records into the CRM as non-marketing contacts. Include source, purpose line, and capture date. Don't enroll them in a marketing flow, because a bulk enrollment is how the nurture reaches people the gate excluded.

## 3. Routing

- **A records with a named next step:** send a personal note from the staffer who met them. Name an owner and a date.
- **Existing customers and open deals:** account or deal owner.
- **Students and job seekers:** community, never sales.
- **Everyone else:** public recap, plus the single launch email only where the gate says yes.

Don't hand any scan to sales. A scan alone isn't a buying signal.

## 4. Tracks per segment

Ranking line (efficiency): public recap > promised-item message > personal note > community invitation > activation path > sales handoff > nurture sequence.

What moved it:
- **Scanner purpose "updates" (Q3).** This keeps the nurture track open for US and corporate-UK scans. Nothing was promised beyond updates, so I limited it to one launch announcement, not a sequence.
- **Germany plus unlisted jurisdictions (Q4).** This forces the double opt-in path and deletes the nurture track for anyone who doesn't click.
- **Organizer list (Q3 for that source).** This deletes the track until the notice is read.

| Segment | Track |
|---|---|
| US scans, corporate UK scans | One launch announcement (this is the one message they get), plus the public recap. |
| Personal-address UK scans | Double opt-in confirmation, or hold pending the privacy owner's decision. |
| Germany, Brazil, Japan scans | Double opt-in confirmation, enrolled only on click. |
| Organizer list | Nothing until the notice is read. |
| All C | Public recap. No separate promised-item email, since nothing was promised. |

## 5. Message drafts

I kept these plain-text and short. Run them through your humanizer skill before sending.

**Public recap** (publish on your blog or docs; send the link to nobody)

> What we showed at re:Invent: slides, repo, the questions we heard most, and [launch]. Want updates? Opt in here: [link]

The opt-in link lives on the page, not in an email.

**Double opt-in confirmation** (no promotion, sender identified, no product pitch)

```
Subject: Confirm you want product updates from Acme

Hi <first name>,

You scanned your badge at the Acme booth at AWS re:Invent. The scanner said
"Scan to get product updates from Acme."

Please confirm you want those updates: <confirm link>

If you don't click, we won't email you again.

<sender name, Acme, postal address>
```

Log the click with a timestamp. That log is your proof of consent.

**Launch announcement** (US and corporate-UK scans, plus anyone who confirmed)

```
Subject: <what launched, plainly>

Hi <first name>,

You scanned your badge at the Acme booth at re:Invent for product updates.
Here is the one we shipped: <two sentences, one link>.

<sender name, Acme, postal address>
<unsubscribe or objection link>
```

Add UK GDPR transparency text for UK recipients.

## 6. Stop rules and suppression

- **At most one message per B or C record**, unless they reply or click. The launch announcement is that message.
- **Send in waves, safest segment first** (US, then corporate UK, then confirmed double opt-ins). Review before each next wave.
- **Stop the batch on the second spam complaint.** Also stop if unsubscribes or "who are you, remove me" replies run above your last event's level. This is the skill's own threshold, not a published one. Company-domain mailboxes rarely report complaints, so count every observable negative.
- **Google's 0.10% target and 0.30% ceiling** apply to your domain's daily Gmail rate in Postmaster Tools. A few hundred emails rarely show there, so protect the rate yourself and don't wait for it to react.
- **Suppression owner:** name one person before the first send. Honor unsubscribes and objections at once, on a permanent suppression list. The US floor is 10 business days and Yahoo expects bulk senders within 2 days. The right to object in the EU and UK is absolute.
- **Retention:** agree with the privacy owner how long unconfirmed Germany, Brazil and Japan scan records are kept. Delete them after that.
- **Never import a bought, scraped or rented list.** Never reuse a raffle entry alone for marketing.

Objection to "leadership wants the whole list in the nurture": every complaint lands on the sending domain's reputation, and the domain pays for every event after this one.

## 7. Measurement sheet

| Field | Value |
|---|---|
| Event, date closed | AWS re:Invent, <date> |
| Cohort tag | `evt-reinvent-2026` on UTM links and any signup or credit codes |
| Activation event | **Needs your answer (Q6)**: API key, first successful call, or first deploy |
| Counts by grade | A <n>, B <n>, C 520 |
| Messages per track | launch announcement <n>, double opt-in <n>, confirmed <n>, recap published |
| Activated at day 30 / 60 / 90 | per grade, beside a non-event baseline for the same window |
| Guardrails | complaint rate, unsubscribes, max days to suppression |
| Opportunities sourced / influenced | report both; events mostly influence |
| Threshold | Self-set from your last event or blended acquisition cost. No published benchmark exists for event follow-up. |

Read the 30-day numbers into the sponsorship review for the Diamond tier.

## What I need from you

1. The organizer's sharing notice for the list (blocks the list).
2. Per-country counts for the scans (UK gmail count and Brazil/Japan counts especially).
3. Any booth notes or graded log (they make A records and change the routing).
4. Your activation event and whether you can tag a cohort.
5. Your privacy owner's call on whether the scanner screen counts as consent for UK personal addresses.