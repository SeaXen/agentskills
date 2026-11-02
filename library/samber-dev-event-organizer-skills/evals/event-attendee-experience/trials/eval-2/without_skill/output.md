# Recommendation: ship the UUID badge, with changes to the post-event spreadsheet

The designer's plan has a hard flaw. The organizer's plan is the right base, but the spreadsheet step needs fixing.

## Why not name, email and company in the QR

- **The QR is on the front of a single-clip lanyard.** Single clips flip, but anyone nearby can still scan or photograph a front-facing code. That includes other sponsors, strangers, and anyone with a photo of the hall or a LinkedIn post. You would be printing every attendee's email where it can be read by any scanner app, with no control.
- **It is irreversible.** Once printed, you can't revoke it, and you can't honor a withdrawn consent.
- **It breaks GDPR in Lisbon.** The event is in the EU, so GDPR applies. You'd be handing all 1,200 attendees' data to every scanner, whether or not they agreed to share it with the sponsor. Data minimization and purpose limitation fail here.
- **The "offline" benefit is weak.** Scanning a UUID offline works just as well, because the app only has to log the scan. It doesn't need the contact data.

## What to ship

1. **Print a random UUID (v4) per attendee.** It must not be sequential or derived from their data. Print nothing else in the QR.
2. **Add a consent checkbox at registration.** Something like "Share my name, email and company with sponsors whose staff scan my badge." Use only those fields. Don't share phone, address or job history.
3. **Update the privacy notice.** Name the sponsor, the purpose and the retention period. The sponsor becomes a recipient and probably a separate controller. Sign a short data-sharing agreement with them before the event.
4. **Handle attendees already registered.** If the current notice doesn't cover sponsor sharing, re-ask them. Treat anyone who doesn't answer as "no".
5. **Have the sponsor scan with any app that keeps an exportable scan log** (UUID plus timestamp). Test this before the event with their actual app. If it can't export a log, give them a free QR scanner PWA that does.
6. **Return contact details only for consented UUIDs.** Join the scan log against the registration table, drop non-consenting rows, and deliver the result.

## Where I'd change the organizer's plan

"Email a spreadsheet after the event" is the weakest part, for three reasons.

- **It may breach the contract.** "Lead capture" usually implies leads in hand while the conversation is fresh. Reread the clause. If it promises same-day or on-site contact details, a post-event file won't satisfy it.
- **It is slow and manual.** A spreadsheet sent by email also sits in inboxes indefinitely. That is a data-handling risk of its own.
- **Neither of you can verify consent at the moment of the scan.**

Better options, in order of preference:

- **A small lead-retrieval page** that your team builds or buys. The sponsor logs in, scans the QR (offline-capable, syncing when connected), and the app shows contact details only for consented UUIDs. The build is small, and the sponsor gets leads on the day. Commercial lead-retrieval tools do exactly this. Check your registration platform first, since it may already include one.
- **A daily export.** If you can't build it, send the sponsor a consented-only spreadsheet each evening of the event, not once afterward.
- **Spreadsheet after the event only as a last resort.** If you must, send it within a few days by an expiring secure link rather than email.

## Decisions for you

- Does the sponsor contract specify when and how leads are delivered? That decides spreadsheet versus live retrieval.
- Does your registration platform already offer lead retrieval? If so, the cost is near zero.
- Can your DPO or legal contact review the notice wording and the sponsor agreement? I can't give legal advice. This is the standard shape for a lawful design, but they should sign off.

**If you do one thing:** drop the plaintext QR, print opaque UUIDs, and add the consent checkbox now. Registration is already open, and the checkbox is the only item that gets harder to add later.