# Wrenmoor Certification Program — Program Design Doc

**Status:** Draft v0.1
**Owner:** Certification Program Lead (TBD)
**Date:** 2026-09-20

> Three items below carry real legal/credibility/PR risk that a design doc shouldn't paper over. They're called out inline (⚠️) with mitigations that don't require reversing anything already decided.

## 1. Program overview

Wrenmoor is launching a proctored, paid certification for its API gateway product: a 60-question multiple-choice exam, 90 minutes, validated against an official $1,200 prep course sold by the education team. The launch coincides with sunsetting a legacy 2024 completion-badge program (~300 holders).

| Item | Spec |
|---|---|
| Format | 60 MCQ, single/multi-select |
| Duration | 90 minutes (1.5 min/question — in line with comparable vendor certs) |
| Delivery | Proctored (mode TBD — see §4) |
| Prep material | Official $1,200 course, education team |
| Pass/fail line | Set by education team |
| Predecessor | 2024 completion badge (~300 holders, being sunset) |

## 2. Roles & governance

⚠️ **Conflict of interest.** The team that writes and sells the $1,200 prep course also sets the passing score. That's the one group with a direct financial incentive to make the bar match what their own course teaches — or to move it if pass rates affect renewal/sales. Left as-is, this is the single biggest threat to the certification's credibility: if a customer or competitor ever asks "who decided what a passing score means, and do they profit from it," there's no good answer today.

This doesn't require taking pass/fail authority away from education. It requires making the *process* defensible:

- Run cut-score setting as a documented standard-setting exercise (Modified Angoff or Bookmark method), with a **SME panel that includes engineers outside the education team** — education can still own the final sign-off, but the input isn't solely theirs.
- Publish the exam blueprint (domains + weightings) publicly. Opacity is what turns "we set our own bar" into a scandal; transparency turns it into a normal industry practice.
- Re-run the cut-score study any time the exam form changes materially, and log the rationale. A dated paper trail is the cheapest insurance against a "you moved the goalposts" complaint.

## 3. Exam design

- Blueprint: define 4–6 content domains (e.g., routing/config, auth policies, rate limiting, observability, troubleshooting, upgrades/migration) with weightings that map to real job tasks, not to the prep course's table of contents. Draft blueprint independently of the course outline, then compare — convergence should be a check, not the starting point.
- Item bank: build at minimum 2–3x the live item count (120–180 items) so forms can rotate. This matters more than usual given §5.
- Form assembly: randomize question order and answer-option order per candidate at minimum — free, and it kills the simplest kind of shared-answer-key cheating.

## 4. Proctoring & exam integrity

⚠️ **"Proctored" with zero anti-cheating budget is a contradiction worth resolving before launch, not after.** Calling an exam "proctored" implies some verification of who's taking it and how — if the actual answer is "nobody's watching and we hope for the best," that's a misrepresentation risk the moment a customer asks how the credential is protected, and it undercuts the $1,200 course's value proposition (why pay a premium for a credential nobody's securing?).

Zero/near-zero-cost options that still count as "proctored," roughly in order of rigor:

1. **Live human proctor over an existing video tool** (Zoom/Meet you already pay for) — ID check on camera, screen-share required, candidate declares a clear space. Costs staff time, not software.
2. **Recorded, unmonitored video** with a written honor code and an explicit clause: certification is revocable if a later review of the recording shows a violation. Cheaper than live, weaker deterrent, but still "proctored" in a literal sense.
3. At minimum: a signed integrity attestation plus a real, exercised right to revoke for cause. Do not skip this even if 1 or 2 aren't feasible — without it, "we'll deal with it if it happens" has no contractual teeth to deal with it *with*.

Pick one of these explicitly before the marketing copy says "proctored" — the choice changes what the word is allowed to mean on the sales page.

## 5. Exam security (no-budget version)

No line item needed for most of this — it's process, not tooling:

- Rotate forms per the item bank in §3; never issue the same 60-question set twice in a row to the same cohort.
- Retake cooldown (e.g., 14 days) with a different form on retake — cheap, and standard practice.
- Track score + completion-time outliers in a spreadsheet (e.g., <20 min completion with a passing score). This is a detection method, not prevention, but it's free and catches the obvious leak/collusion cases.
- Terms of use for the exam should state plainly that certification can be revoked post-hoc if cheating is later discovered — write this now, while it's abstract, not after the first incident when it looks retaliatory.

## 6. Prep course relationship

- Keep the exam blueprint and the course outline as separate documents with a mapping table between them, so a candidate (or auditor) can see the exam tests job-relevant skills, not "did you memorize this specific course."
- Publicly disclose that the course and the exam are produced by the same team. Disclosure doesn't remove the conflict, but non-disclosure turns a design tradeoff into a trust violation if discovered later.

## 7. Legacy badge program sunset (2024, ~300 holders)

⚠️ **"Pull the badge pages and revoke the badges" is a bigger action than the goal requires, and it lands hardest on people who did nothing wrong.** The actual goal is "avoid confusion between old and new programs" — that's a labeling problem, not a revocation problem. Revoking a credential someone earned and may have on their résumé or LinkedIn profile, with a dead verification link behind it, reads to that person (and to anyone checking their claim) as "the company decided their work no longer counts." For ~300 people, some of that will surface publicly, and it's disproportionate to the stated goal.

Recommended instead:

- **Retire, don't revoke.** Stop issuing new legacy badges immediately. Leave existing verification pages live but relabel them clearly: *"Legacy Wrenmoor Badge (2024 program, retired [date]) — succeeded by Wrenmoor Certified Engineer."* This solves the confusion problem without invalidating anyone's history.
- Reserve actual revocation for the narrow case it's meant for: fraud or policy violation, not "the program changed."
- Offer legacy holders a migration path — e.g., a discount or waiver toward the new exam — which turns a population that could feel devalued into your first cohort of paying customers for the new cert.
- Have someone check whether the original badge terms reserved a right to revoke at all; if they didn't, revoking isn't just a trust problem, it may be a contract one.

## 8. Launch sequencing

⚠️ **Don't retire the old badge the same week the new paid cert launches.** Doing both at once reads as "we devalued your free credential in the same breath as launching one we charge $1,200 to prep for" — even if that's not the intent, it's the obvious read, and it's the version of the story that spreads. Stagger by at least 3–4 weeks: announce the legacy retirement first with a grace period, let that land and settle, then launch the new certification separately.

Suggested timeline:

| Week | Action |
|---|---|
| T-4 | Announce legacy badge retirement + migration offer to the ~300 holders |
| T-4 → T-1 | Legacy pages relabeled as above; no launch messaging yet |
| T0 | New certification + prep course launch |
| T0 → T+4 | Monitor pass rates, score-outlier log (§5), candidate feedback |

## 9. Comms plan (legacy holders)

- Direct email to all ~300 holders before any public change, not after.
- Message: program is being succeeded, not invalidated; badge remains verifiable; here's the migration offer and deadline.
- Public FAQ entry addressing "what happened to the old badge" before anyone has to ask.

## 10. Success metrics

- Exam pass rate (flag if outside a healthy 60–85% band — too high suggests the bar is too low or leaked, too low suggests a validity problem)
- Score-outlier rate from §5's tracking
- Legacy-holder migration/discount redemption rate
- Complaint/support volume tied to the badge retirement in the 30 days post-announcement

## 11. Open decisions

- Which proctoring tier (§4, options 1–3) ships at launch — needs a decision before marketing copy is written.
- Who sits on the cut-score SME panel alongside education (§2).
- Whether legal reviews the original 2024 badge terms before any page relabeling goes out (§7).
- Exact migration incentive (discount %, deadline) for legacy holders.