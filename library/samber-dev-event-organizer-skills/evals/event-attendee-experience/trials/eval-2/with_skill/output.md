# CloudTide Summit badge decision: ship neither proposal

I followed the `event-attendee-experience` skill and its `checkin-badges-and-swag.md` reference. Neither option should ship as proposed. The platinum contract settles one point: you need a scannable badge. It doesn't settle how, and both proposals fail on that.

## Verdict

| Option | Verdict | Why |
|---|---|---|
| Name, email and company in the QR | ❌ Do not ship | The skill deletes this option outright. Every scanner in the building can read it, not just the sponsor's. Anyone walking past can read the QR, because it is on the front of the badge. |
| UUID in the QR, then email the sponsor a spreadsheet | ⚠️ Right payload, wrong release step | An opaque ID is the better payload. But the spreadsheet of scanned UUIDs mapped to contact details re-identifies everyone in the scan log. It is also a file you can't recall once sent. |
| **Ship this instead** | ✅ | A QR on the badge's **back**, with all four mitigations together. The QR carries an opaque ID, not attendee data. |

The skill says attendee contact lists are never given or sold to sponsors. Your signed contract is the case where it tells you to promote the "QR on the back with consent, opt-out and sponsor terms" option. The skill treats its mitigations as a set, not a menu.

## What to ship

1. **Consent at registration, before the badge is printed.** Add an explicit, separate opt-in to share contact details with sponsors who scan you. Keep a consent record for every badge that carries a code.
2. **Physical opt-out sticker.** Every badge gets a sticker that covers the code. An opt-out an attendee can't enforce at the moment of scanning isn't an opt-out.
3. **Written sponsor terms.** The sponsor is told in writing that scanning without consent is not permitted. Send this before the event.
4. **QR printed on the back, with two-point lanyard attachment.** A single-clip lanyard spins, so the code can face outward by accident. You'd have to change this part of your current plan.

Your planned front-printed QR on a single-clip lanyard fails mitigation 4 directly. Print the name large on the front, which is the badge's icebreaker job. Put the QR on the back and switch to two-point lanyards.

**The speed concern is smaller than it looks.** Flipping a badge takes about a second. It also acts as the attendee's physical consent gesture at the booth.

## Offline scanning still works

- The QR holds an opaque ID. It scans offline, so the sponsor's app needs no network.
- Only your organizer system can resolve that ID to a person. That is the control the badge designer's version gives up.
- **Do not put names or emails in the QR**, even encoded or encrypted. If the app can read them offline, any other scanner can too.

## The post-event release (my inference, not from the skill)

The skill doesn't prescribe the delivery mechanism, so this part is my reading of its rules. Check it with whoever owns privacy for you. Lisbon means EU law applies, so GDPR is likely relevant.

- Release rows **only for attendees who opted in** and whom that sponsor scanned. Nobody else's data goes in the file.
- Never send the full attendee list or a bulk UUID-to-contact map.
- Say in the consent text exactly what the sponsor receives (for example name, email, company) and for what purpose.
- Make delivery something you do per consenting scan, not an open spreadsheet. A tight, auditable export is safer than a broad one.

## Things to check this week

- **Read the contract wording.** Does "badge scanning for lead capture" say anything about the payload, the placement, or delivery of contact details? If it doesn't, the design above is compliant. If it promises a specific data format or a bulk export, bring it to Sales and legal now.
- **Confirm the badge print deadline.** Moving the QR to the back and switching lanyards both have to land before print. If the date is close, make this decision first.
- **Check whether the sponsor's scanner app can use an opaque ID.** If it only parses structured contact data, raise it with the sponsor early. Don't fix it by putting data in the QR.

## Gate before doors open

Consent-record completeness is one of the skill's three hard gates. If any badge has a machine-readable code, every scan-capable badge needs a recorded consent and a working opt-out sticker. Check this before print, not on the day.

## Open questions for you

1. Does the contract say anything about delivery format or timing of the leads?
2. What is the last date badge artwork and lanyards can change?
3. Can the sponsor's app work from an opaque ID?

I didn't run the skill's one-question-at-a-time interview. I used your answer to its Q6 (a signed sponsorship already promises lead capture), which fixed the ranking. The other answers are unknown, and my release suggestion depends on the contract.