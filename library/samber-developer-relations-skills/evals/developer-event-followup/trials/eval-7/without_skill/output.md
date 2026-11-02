**Do not send to all 3,520 tomorrow from the main domain.** First action, about 20 minutes: pull the scanner vendor's consent export (per-lead timestamp, country, exact screen text). Then split the list by source and country.

Tomorrow is Sunday, so even the safe segments should go Tuesday or Wednesday at local send time.

## Why one blast is wrong

- **The two lists differ.** The scan list has Acme-specific consent. The organizer list has consent to the organizer, which does not transfer to Acme.
- **Consent is judged per country.** About 30% of scans are German, with some Brazilian and Japanese. All three need stricter handling than the US.
- **One spam wave hurts the main domain.** It would also hit your customer and transactional mail.

## Segment A: 520 scans

The screen said "Scan to get product updates from Acme". A launch announcement is a product update, so the wording fits.

1. **US (opt-out regime, CAN-SPAM).** Send. Include a physical address, a working unsubscribe link and honest sender identity.
2. **UK corporate addresses.** Send. The scan consent covers them.
3. **UK gmail and other personal addresses.** These count as individuals (UK PECR), so consent is required. The scan consent counts only if the vendor logged it. If the log is missing, do not send to these.
4. **Germany (about 156 people).** German law (UWG §7) expects double opt-in, and a scan screen is single opt-in. Send one plain confirmation email: "You asked for Acme product updates at re:Invent. Confirm here." Put no launch content in it. Send the launch only to people who click. Unconfirmed addresses get nothing.
5. **Brazil (LGPD).** The scan consent is specific and purpose-bound, so send. Give an easy opt-out and write in Portuguese if the leads suggest it.
6. **Japan.** Prior opt-in is required and you must keep records. Send only if the vendor log proves the consent. Include sender name, address and an opt-out in the email.

**Before any scan segment:**
- Dedupe the list.
- Suppress existing unsubscribes and current customers.
- Verify addresses, because badge scans have typos.
- Store consent in your CRM as source, timestamp, screen text and country.

## Segment B: 3,000 organizer list

Do not send the launch announcement to this list, from any domain.

1. **Read the sponsor terms first.** Most allow one-time use for stated purposes. Look for these items:
   - the exact wording of the opt-in the attendees saw;
   - whether sponsors may email them;
   - whether the use is one-time;
   - whether importing the list into your CRM is allowed.
2. **Drop all EU, UK-individual, Brazil and Japan contacts** unless the terms and local law clearly allow Acme to email them. For Germany, assume no.
3. **For the remaining US contacts, if the terms permit,** send one short, relevant message, not the full launch blast. For example: "You opted in to hear from re:Invent sponsors. Here is what we launched. Unsubscribe here." Name the event as the reason they are hearing from you.
4. **Keep the list out of your main marketing database.** Use it once, then delete it or keep it only as the terms allow. Move anyone who replies or clicks onto the consent track.
5. **Alternative:** ask the organizer to send on your behalf. This is the safest route for the EU contacts.

## Sending hygiene

Do this by tomorrow even for the safe segments.

1. **Use a subdomain, not the main domain.** For example `news.acme.com`, separate from your customer and transactional mail. Set up SPF, DKIM and DMARC, plus one-click unsubscribe (Gmail and Yahoo bulk-sender rules).
2. **Warm up.** If this subdomain is new, send 100 to 300 a day first, not 3,000 at once.
3. **Watch complaints.** Keep the spam-complaint rate under 0.1%. Google's hard limit is 0.3%. Pause the send if you cross 0.1%.
4. **Tier by conversation.** People you actually spoke to get a personal note, not the blast. Scans with no conversation get one light touch. This follows the event follow-up rules.

## Estimated effort

- Consent export and segmentation: about 1 to 2 hours.
- Reading the organizer terms: about 30 minutes.
- Subdomain DNS and warm-up setup: about 1 hour, plus the warm-up days.
- German double opt-in email: about 1 hour to write and send.

I am not a lawyer. Have counsel confirm the German, Japanese and Brazilian handling and the organizer terms before the send. That is a 30-minute review.

**Next:** ask the scanner vendor for the consent export and the organizer for the sponsor list terms, then paste the terms here and I will draft the segment plan and the German confirmation email.