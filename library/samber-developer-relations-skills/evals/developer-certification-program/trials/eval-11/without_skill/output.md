# Verification

Anyone can confirm a Quorrin Identity Platform credential in seconds, without contacting us. The public record shows one status per credential and nothing else.

## What the holder receives

1. Quorrin emails a PDF certificate on issue.
2. The PDF carries the holder's name, credential level, issue date, expiry date, and a unique certificate number.
3. The PDF also carries the verification URL and a QR code that opens the matching record.
4. Certificate numbers are random and non-sequential, so no one can guess a valid one.
5. The PDF alone is not proof. Only the public record is.

## How a third party verifies

1. Open the verification page and enter the certificate number, or scan the QR code.
2. The page returns the holder's name, credential, issue date, expiry date, and current status.
3. Name search is a secondary route. It returns only holders who opted into the public directory (see below). Results show the credential and status so that same-name holders can be told apart.
4. If the lookup fails, email certifications@quorrin.example. We reply within two business days. This is the fallback, not the main path.

## Public directory

- Listing is opt-in. Candidates choose it at registration and can withdraw at any time.
- A holder who opts out stays verifiable by certificate number. They do not appear in name search.
- The directory shows only name, credential, issue date, expiry date, and status. It never shows email, employer, or exam scores.
- Rate-limit name search and block bulk export, so the directory cannot be scraped into a mailing list.
- Document the legal basis for publishing names under GDPR and tell candidates before they sit the exam.

## Status values

| Status | Meaning | Shown publicly |
|---|---|---|
| Valid | Credential is current | Name, credential, dates, "Valid" |
| Expired | Past the expiry date | Same fields, "Expired" |
| Revoked | Quorrin withdrew the credential | Same fields, "Revoked" |
| Not found | No such number | "No record found" |

## Revocation

1. Revoke only after a written finding by a reviewer who was not the original investigator.
2. Notify the holder in writing with the reason and a 14-day window to appeal.
3. Keep the holder's record page and change its status to "Revoked", with the revocation date. Do not delete the page: a deleted page looks the same as a forged number.
4. Do not publish the reason. The public page says "Revoked" and nothing about misconduct. Publishing an accusation invites defamation claims and GDPR complaints.
5. Keep the full case file privately.
6. If an appeal succeeds, restore the status and the original issue date.

## Partner fee lapse

The partner fee pays for a listing. It does not pay for the credential, so the two stay separate.

1. Send two written notices before acting: one at 30 days overdue and a final one at 7 days before removal.
2. After the final notice, remove the holder from the name-search directory only.
3. The certificate number still resolves to "Valid" or "Expired" by date. A lapsed payment never changes the credential's status.
4. Never use "Revoked" for non-payment. Verifiers would read it as a competence or conduct problem.
5. Relisting on payment is immediate and automatic.

## Changes from the original plan

- **Instant lookup added.** The original plan had only email verification with a two-business-day wait. Clients hiring now need an answer now. Email stays as a fallback.
- **Listing is opt-in.** A full public list of every holder, searchable by name, needs a documented legal basis and invites scraping. Opt-in is the safer default.
- **No "revoked for misconduct" page.** Deleting the page makes real holders look forged, and the label is a public accusation. Use a neutral "Revoked" status with a private case file and an appeal.
- **No silent removal for non-payment.** Removal without notice breaks the contract and leaves clients with a false signal. Use notices and a separate directory listing.

## Open decisions for you

- Who is the independent reviewer for revocations, and what is the appeal body?
- What is the credential's expiry period?
- What is the legal basis for the directory, and does counsel sign off?
- Does the partner agreement already allow removal on non-payment, and with what notice?