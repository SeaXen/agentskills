# KubeCon EU badge scans: what to do before Monday

## Short answer

Don't load all 412 scans into the 6-email nurture. Send the one email the scanner promised, with a clear opt-in to the series. Then handle the roughly 30 real conversations as human follow-ups.

This isn't legal advice. Have your DPO or counsel confirm the Germany and UK points before Monday.

## Why the CMO's reasoning doesn't hold ❌

1. **Legitimate interest is only half the test.** It is a GDPR basis for processing. Marketing email is also governed by the ePrivacy rules, which each country implements in its own law. Those rules override a general legitimate-interest argument.
2. **Germany (about 165 contacts) is the strictest case.** UWG §7 requires prior express consent for marketing email, and it makes no B2B exception. The soft opt-in exception covers only addresses collected during a sale of your own similar products. A badge scan is not a sale. Competitors and consumer associations can also send cease-and-desist letters (Abmahnung), which is a cheap and common enforcement route.
3. **Rest of EU (about 124 contacts) varies by country.** Austria, Italy and Spain lean toward consent, and some countries allow B2B email with an opt-out. Treat all of them as consent-required unless counsel clears a specific country.
4. **A work address is still personal data.** `firstname@company.com` identifies a natural person.
5. **The scanner's promise undercuts the balancing test.** The scan said "Scan to get the demo config emailed to you." That sets the expectation of one email. Six sales-nurture emails are a different purpose, which hurts both purpose limitation and the "reasonable expectations" part of a legitimate-interest assessment.
6. **The right to object to direct marketing is absolute.** If someone objects, you must stop immediately.

## Plan

### 1. Check these before Monday (about 1 hour)

- What did the scanner screen or the organizer's attendee terms say about sharing data with sponsors? Does it cover marketing, or only the item requested?
- Was the demo config email already sent? If not, send it first.
- Which of the roughly 30 conversations include "asked us to follow up"? Add a column to the Sheet.

### 2. Clean the list (about 1 hour)

- Dedupe against existing HubSpot contacts and customers. Existing customers may already have a lawful basis.
- Remove competitors, recruiters, students and personal addresses.
- Tag each contact by country and by company type. In the UK, a sole trader or partnership counts as an individual under PECR.

### 3. Segment

| Segment | Size (est.) | Action Monday |
|---|---|---|
| Real conversations that asked for follow-up | ≤30 | A personal email from the engineer who spoke with them. Enroll in the nurture only if they said yes, and log that. |
| Other real conversations | remainder | One personal email, no sequence. |
| Scan-only, all countries | about 380 | The promised demo config email with an opt-in to the series (step 4). |

**If the CMO insists on enrolling some contacts Monday**, the lowest-risk fallback is:
- **US (about 62):** CAN-SPAM only requires an unsubscribe, a physical address and honest headers. The legal risk is low, but you'd still be breaking the scanner's promise.
- **UK (about 62):** corporate subscribers at limited companies can be emailed under PECR. You need a documented legitimate-interest assessment, a privacy notice in the first email, and a one-click unsubscribe.
- **Germany and the rest of the EU:** never without consent.

I recommend against the fallback. A single rule is easier to run, and it keeps your promise to every contact.

### 4. The Monday email (all scan-only contacts)

- Deliver the demo config, as promised.
- Include a short privacy notice: who you are, why you hold their data, how long you keep it, and how to object or delete. GDPR Art. 14 requires this within one month of obtaining the data. If that month is already over, send it now and say so to your DPO.
- Add one unticked opt-in: "Want a 6-part series on cutting Kubernetes cloud costs? Yes, subscribe." Use double opt-in, with a confirmation click, for DE and EU contacts.
- Link to the free tier signup. This is the best conversion path for a product-led SaaS. Give signups a consent checkbox for marketing emails. Onboarding emails needed to use the product are fine without it.
- Don't add sales pitches to this email.

### 5. HubSpot setup

- Import with the source "KubeCon EU 2026 badge scan".
- Set the legal basis and consent status per contact. Use "not opted in" for the scan-only group.
- Import them as non-marketing contacts until they opt in. This also avoids paying for marketing-contact slots you can't email.
- Enroll in the 6-email workflow only on confirmed opt-in.
- Set a retention rule. For example, delete scan-only contacts who haven't engaged after 6 months.

### 6. Why this is also better marketing

- Your audience is Kubernetes engineers, who punish spam.
- Spam complaints from a cold list can hurt the sending domain's reputation. That can drag down your product's transactional email too.
- Opted-in contacts convert better. I have no baseline for your opt-in rate, so measure it on Monday's send.

## Message to the CMO

> We'll load all 412 into HubSpot Monday and send everyone the demo config we promised, with a one-click opt-in to the series. German and EU email marketing needs consent even B2B, and the scanner promised only one email. Opt-ins go straight into the nurture. The ~30 real conversations get personal follow-ups from the engineers. This protects our sending domain and avoids a German cease-and-desist.

## Next time

Add a marketing consent line at the booth: a checkbox on the scanner or a QR form with "Also send me Kubernetes cost-saving tips (unsubscribe anytime)." Record the consent text and timestamp.