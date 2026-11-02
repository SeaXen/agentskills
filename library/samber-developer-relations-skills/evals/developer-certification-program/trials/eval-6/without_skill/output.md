# Orvalon Certified Integrator: Partner Model

## Verdict on the proposal

I'd keep the partnership and change four of its five mechanisms. Each of the four lets one party grade or leak its own exam.

| Proposed | Problem | Replace with |
|---|---|---|
| Pay 40% of exam fee **per pass** | Partner earns only when students pass, so it is rewarded for lenient proctoring, coaching during the exam, or answer sharing. | Pay per **sitting delivered**, regardless of result. |
| Partner runs sittings on own premises for own students | The seller of the course also controls the exam room. | Remote proctoring run by Orvalon or a third party. Premises are optional, and only as audited test centers. |
| Tomasz, lead item writer, writes the prep course | He knows the live items. Course content will drift toward them, knowingly or not. | Firewall: item writers never write training. Someone else writes the course from the public exam blueprint. |
| Exam moves into the MOOC quiz engine | A course quiz engine has no secure delivery, no item-exposure control, no proctoring and no psychometrics. Course and exam share one trust boundary. | Keep a separate secure exam delivery. Link it to the course by single sign-on and an automatic booking button. |
| Share the item bank with partners | Three outside companies would hold every live item. The credential is then worthless, and the bank would need a full rewrite. | **Never share live items.** Share the blueprint, objectives, and a practice exam built from retired items. |

The goal behind the proposal (finish the course and get certified in one flow) is achievable without those risks. Section 4 shows how.

## 1. Roles

- **Orvalon (certification owner):** owns the credential, the blueprint, the item bank, exam delivery, scoring, appeals, revocation and the trademark.
- **Authorized Training Partner (ATP):** sells and teaches the prep course. It gets no access to live items and no role in scoring.
- **Proctoring provider:** Orvalon-contracted, independent of every ATP. It checks identity and watches the sitting.
- **Item writing team (Tomasz and others):** writes and maintains the exam only. It has no contact with course authoring.
- **Course author:** a different person, or an outside author, who writes from the blueprint and the public objectives.

## 2. Partner revenue

The partner's main income is the **course fee**, which it keeps in full. The exam adds a small, outcome-neutral fee.

- **Course fee:** partner sets the price and keeps 100%. Orvalon charges a license fee for the official course materials (or none, if you want to drive adoption).
- **Exam sitting:** Orvalon bills the candidate the exam fee.
- **Partner exam commission:** a fixed share of the exam fee for each sitting taken by a candidate the partner referred. It is paid on the sitting, not on the pass.
- **Retakes:** the same commission applies. Retakes never pay more than first attempts.
- **Illustration only:** at an exam fee of $F, a 20% sitting commission is $0.20F. That is below your proposed $0.40F per pass whenever the pass rate is above 50%. Set the percentage from your real fee and margin.

Why this works: the partner earns from teaching well and filling seats, not from the result. Teaching well still raises its pass rate, which helps its reputation and sales.

## 3. Integrity controls

1. **Impartiality separation.** Keep training and certification staff, budgets and files apart. Record it in a written policy. Credentialing standards such as ISO/IEC 17024 expect this, and it is easier to design in now than to retrofit.
2. **Item secrecy.** Live items are never given to partners. Partners get the blueprint, learning objectives, weighting, and a practice exam made of retired items.
3. **Item bank health.** Check the bank's size before launch. Three partners and more candidates will expose items faster. Plan alternate forms and a rotation or retirement schedule, and write new items before launch.
4. **Independent proctoring.** Orvalon or its provider verifies ID and records the sitting. Partners may host a room, but never proctor their own candidates.
5. **Test-center option.** If a physical room is required, certify it. Require an Orvalon-appointed proctor, locked-down devices and unannounced audits.
6. **Statistical monitoring per partner.** Track pass rate, completion time, answer-pattern similarity, and retake rate. Flag outliers such as a pass rate far above the others, very short sitting times, or identical wrong answers.
7. **Sanctions.** The contract allows suspension, candidate invalidation, and credential revocation for proven irregularities. Partners cannot negotiate these away.
8. **No pass guarantees.** Partners may not advertise "guaranteed pass" or "exam questions included".
9. **Conflicts register.** Anyone who writes items declares any training relationship. Item writers are barred from teaching the course.

## 4. Candidate flow ("finish and certify in one place")

1. The candidate buys the course from the partner.
2. The course runs on your MOOC platform, covering objectives only.
3. At the end, a button opens exam booking via single sign-on. The candidate does not create a second account.
4. The exam runs in the secure delivery system with remote proctoring.
5. The result and a verifiable credential come back automatically. The course page shows the status.

The candidate sees one flow, but the exam stays outside the course platform.

## 5. Regional points to check with counsel

- **Poland (EU):** GDPR for candidate data and proctoring recordings. Set a retention period and a legal basis.
- **Brazil:** LGPD, plus local tax treatment of cross-border commission payments.
- **India:** the DPDP Act, withholding tax and foreign-remittance rules on payments.
- **All three:** the trademark license, governing law, and whether partners are agents or independent resellers.
- **Language:** if you translate the exam, treat each translation as a separate form needing equivalence checks. Otherwise keep it English-only at launch.

## 6. Rollout

1. **Pre-launch, weeks 0–6:** move Tomasz fully to item work. Appoint another course author. Publish the blueprint and a retired-item practice exam. Select the proctoring provider. Write the partner contract.
2. **Pilot, one partner, one cohort:** run the full flow and the monitoring. Sign off against the pass-rate and irregularity thresholds you set beforehand.
3. **Expansion:** add the other two partners one at a time, only if the pilot metrics are clean.
4. **Review at 6 months:** inspect the bank's exposure, partner statistics, and complaint volume, then adjust fees or controls.

## 7. Open questions for you

- What is the current exam fee, and the size of the item bank?
- How many forms exist, and how often does the bank rotate?
- Do you want physical test centers, or is remote proctoring enough?
- Who is the replacement course author, and does Tomasz's role change formally?
- Are you willing to forgo the per-pass payment? If not, tell me the reason, and I'll design a capped alternative with extra audits.

I did not read the repo to write this, as instructed. Everything above comes from your description.