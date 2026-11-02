# Charter section 7: Verification and revocation (Quorrin identity-platform credential)

**Draft for your validation.** I did not have the earlier sections, so I assumed two things. First, the credential is the skill-badge tier, version-stamped with no expiry. Second, clients of freelancers and services firms are the outside consumer. Correct me if either is wrong. Every number below is self-set.

## What changed from your plan, and why

| Your plan | Problem | Replacement |
|---|---|---|
| PDF with a unique number, verified by emailing certifications@ (answer within 2 business days) | The vendor has to be contacted, and a PDF alone can be edited. A client checking a shortlist will not wait two days. | Instant public check by credential ID, plus a signed portable credential. The PDF is a copy of it. |
| Public list of every holder, searchable by name | Holders did not opt in, and this is personal data. | Opt-in directory. The default check is by credential ID or a holder-shared link. |
| Delete the page and show "revoked for misconduct" | It publishes an accusation. A deleted page also looks like a 404, which a client can't tell from a typo. | The ID URL keeps resolving and shows "not valid", with no reason. The reason goes to the holder only. |
| Drop holders from the list without notice if they stop paying the partner fee | It mixes a commercial status with the competence claim. It also makes a valid credential look invalid. | The credential stays valid. Only the paid directory listing lapses, after notice. |

## Issuing

1. Issue each credential as an Open Badges 3.0 signed credential. It carries the holder name, credential, version stamped, issue date, "no expiry", and a status entry that verifiers check.
2. Give each credential a random, non-sequential ID. A sequential number lets anyone enumerate every holder.
3. Email the holder the PDF and the wallet-importable credential together. Print the ID, a verification URL and a QR code on the PDF. The URL is the trust anchor; the PDF is only a rendering.
4. Keep the master record of holders, versions and status in a system Quorrin owns, even if a credential-issuing service signs the badges.

## Verification

1. Public check by credential ID or a holder-shared link. No login, no contact with Quorrin.
2. The page shows exactly: holder name, credential, version, issue date, "no expiry", status (`valid` or `not valid`).
3. The page shows no email, employer, country, score or reason.
4. A wallet copy checks the signed status entry, so it stops verifying on its own after revocation.
5. Keep certifications@ as a fallback for lost IDs and disputes only. Reply within 2 business days there. The primary check never depends on it.
6. Tell buyers which tier this credential is. Never describe it as a "certification" if it is a skill badge.

## Expert directory (opt-in)

1. The holder opts in at issue or later, and can remove themselves at any time, effective within 1 business day (self-set).
2. Listing shows name, firm, credential, region, languages, contact. This is the main return on the exam fee for freelancers, because it brings client leads.
3. Search by name is allowed inside the directory only. It never lists holders who did not opt in.
4. Directory membership is separate from credential validity. A holder who is not listed still verifies as `valid` by ID.

## Revocation

1. **Grounds.** List them in the candidate agreement: cheating, proxy sitting, leaking items, a failed or refused live explanation on a sampled pass. Misconduct must be written there before it can be sanctioned.
2. **Decision.**
   - A human reviews all evidence before any sanction, including any automated flag.
   - Name the decision-maker in the agreement.
   - A failed or refused explanation suspends the credential pending a supervised retest.
3. **Notice.** Tell the holder privately, with the reason and the evidence, before the status changes. Emergency suspension for a live leak is the only exception.
4. **Appeal.** The holder has 30 days (self-set) to appeal to a named person who was not the original decider. The credential stays `not valid` during the appeal unless the holder is reinstated.
5. **Effect.**
   - Update the signed status entry within 1 business day of the decision (self-set).
   - The public page shows `not valid` and nothing else.
   - Remove the directory entry.
   - Keep the internal record.
6. **Reinstatement.** If an appeal succeeds, restore the status. The public page was never accusatory, so there is nothing to retract.

## Partner fee lapse

1. Misconduct revokes. A missed partner fee never does.
2. When a partner stops paying, send written notice. After 30 days (self-set) remove only the paid directory and partner-tier listings.
3. The credential still verifies as `valid` by ID.
4. If your partner agreement ties seat allocations to the fee, state that in the agreement. It limits new seats, not existing holders.
5. Reword any partner text that says "certified engineers" to name the badge held.

## Pass-threshold check

| Threshold | Status |
|---|---|
| A third party can verify without contacting the vendor | ✅ Public ID check, instant |
| Holders opt in to any directory | ✅ |
| Revocation has an appeals path | ✅ Named decision-maker and 30-day window |
| Revocation shows "not valid" with no reason | ✅ |
| Revocation reaches wallet copies | ✅ Via the signed status entry |

## Open points for you

1. Who is the named decision-maker for revocation, and who hears appeals? They must be two different people.
2. Is the partner fee tied to seat allocations or to directory placement? That decides what the 30-day notice removes.
3. Which countries do holders sit in? Any EU holders mean a privacy review of the public page and the directory.
4. Do you want the 30-day and 1-business-day windows kept, or changed? They are self-set.