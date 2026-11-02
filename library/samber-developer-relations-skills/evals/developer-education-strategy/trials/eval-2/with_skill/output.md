# Developer education charter — Quillstone SDK, board review cycle (next 8 weeks)

## Quick answer

1. **Gate verdict:** Justified, but only at the cheapest rung. The problem is a *sequencing* gap, not a competence gap — you have 53 artefacts and no one owns the order they go in. That's the textbook trigger for a curated learning path, not a curriculum, academy, or certification.
2. **Tier recommendation:** **Curated learning path.** Rejected: structured curriculum with labs (no standing capacity to run it — see below), skill badge and certification (no named external party would act on either), and "keep doing what we're doing" (that's the status quo generating the weekly emails).
3. **Operating model:** Your existing technical writer, inside their existing ~8h/week, builds and owns a single sequenced "Start Here" page on the docs site that orders the 41 tutorials and 12 videos you already have. No new hire, no LMS, no lab platform, no ongoing budget ask — ever, under this plan.

---

## 1. Gate verdict

Education is the right fix, at the curated-path rung only. Evidence: new users ask "where do I start" on a recurring, weekly basis, against a body of 41 tutorials and 12 videos published over three years with no sequence, prerequisite order, or stated starting point. That is the exact escalation condition this problem class is defined by — the same learner-facing question repeating "more than the team can answer individually" — and it's a symptom of nobody owning the order content should be consumed in, not of missing content or a hard product.

Rejected alternatives:
- **More ad-hoc tutorials/videos.** This is the status quo, and it's what produced the problem — every additional standalone piece makes the "where do I start" question harder to answer, not easier, because nothing accumulates into a path.
- **A general docs information-architecture overhaul.** IA fixes "I can't find the answer that exists." Your users aren't reporting that they can't find things — they're reporting they don't know what order to consume things in. Different failure, cheaper fix.
- **A structured curriculum with hands-on labs.** No evidence of a *competence* gap (no conceptual-misunderstanding clustering in support, no deals blocked on trained staff, nothing suggesting people who read the docs still can't do the job) — only a wayfinding gap. Building labs to fix wayfinding is the wrong tool and, separately, unaffordable (see §6).

**Assumption to confirm:** "basically every week" is currently anecdotal. Before you present to the board, have the technical writer spend 30 minutes tagging the last 2–3 months of inbound "where do I start"-type emails/tickets to turn that into a real number. Everything below treats it as real and recurring; if it turns out to be 2 emails total, the verdict changes to "do nothing, it's noise."

## 2. Audience and motion

Primary: individual developers evaluating or newly onboarding to the Quillstone SDK, largely bottom-up/self-serve, spread across your ~2,400 active orgs plus prospective new orgs. Not in scope: no enterprise procurement motion, partner/SI ecosystem, or student audience was named — if one of those exists and is driving this, that changes the credential answer in §5, so flag it if so. Consumer of the outcome: the new user (faster to first value) and your support/success function (fewer navigational emails to answer one at a time).

## 3. Chosen tier, with rejected alternatives

**Curated learning path** — sequence the 41 tutorials and 12 videos you already own into one ordered page, named stages, one net-new "start here" step if a true first-success quickstart doesn't already exist.

Rejected and deleted, not parked:
- **Structured curriculum with labs** — deleted. It requires standing weekly hours across authoring, technical review, lab-environment maintenance, and learner support (order of 20–30h/week in a comparable build) against a real capacity of one person at 8h/week with no headcount ever. Also unsupported by evidence — no signal yet that reading in the right order fails to produce competence.
- **Skill badge / certification** — deleted. Both require a named external party who will act on the credential — a buyer, a partner contract, a hiring manager. None was named. Both are also the first two rungs you can't quietly withdraw once issued; don't open that door on a wayfinding problem.

**Escalation trigger to the next rung, written as an observable condition:** if users who complete the curated path top-to-bottom are *still* failing at the job — still filing the same category of support ticket after finishing the sequence — that's evidence of a competence gap the path can't fix, and it's the point to revisit structured curriculum with labs, with budget, not before.

## 4. Competency map

Lightweight, not a full job-task analysis (that's the curriculum-with-labs tier). Derived from what a competent user of an observability SDK does, cross-checked against your existing content titles — have the writer confirm/adjust against the real 41+12 during the week-1 audit:

| Stage | Job task | Evidence it's done | Existing content (writer to map) |
|---|---|---|---|
| 1. First signal | Install SDK, emit first trace/metric, see it in the UI | User reports data visible within one sitting | Likely covered — becomes step 1; write net-new only if no single "first trace in 10 minutes" piece exists |
| 2. Instrument for real | Auto- vs manual instrumentation, context propagation across services | Traces span more than one service correctly | Map from existing tutorials |
| 3. Configure the pipeline | Exporters, sampling, collector config | Data volume/cost is intentional, not accidental | Map from existing tutorials |
| 4. Make it actionable | Dashboards, alerts, SLOs | User has at least one alert wired to a real threshold | Map from existing tutorials/videos |
| 5. Operate it | Debug missing/broken traces, manage cardinality, upgrade across SDK versions | User self-resolves without opening a ticket | Map from existing tutorials |

Every stage must trace to at least one existing artefact or get named as a gap. If more than ~20% of stages have no matching artefact today, that's real signal your 53 pieces skew toward one part of the journey — worth knowing before launch, not after.

## 5. Credential decision

No credential. No buyer, partner contract, or hiring manager was named as a consumer of one, and inventing that consumer to justify a badge is exactly the failure mode this process exists to prevent. Revisit only if a named enterprise or partner motion emerges that counts trained/certified staff.

## 6. Operating model

- **Owner:** the technical writer, named individually, accountable for the path's accuracy and order — not "docs team."
- **Staffing (inside the existing ~8h/week, no new hire, no ongoing ask):**
  - Audit + sequence the 53 existing artefacts, name gaps: ~16–20h, one-time.
  - Build the "Start Here" page + link-level tracking: ~8–12h, one-time.
  - Write the one likely gap piece (first-success quickstart, if missing): ~8h, one-time.
  - Steady state after launch: ~1–2h/week — reorder on release, fix broken links, retire dead content.
- **Platform:** docs-native. One page on the existing docs site, linking out to existing tutorials/videos in order. No LMS, no lab platform, no new vendor. Source lives in the same repo the docs already live in.
- **Refresh trigger:** re-check ordering within a stated window of any SDK release that changes instrumentation setup (confirm your actual release cadence with the writer — this charter assumes monthly-or-tighter and proposes reviewing every release plus a full pass quarterly; adjust to your real cadence).
- **Pricing:** free, same as current docs.
- **Localization:** deferred until one locale proves demand.
- **Partner delivery:** not applicable — no partner/SI motion identified.

This is the load-bearing point for your board conversation: **the fix fits entirely inside capacity you already have, permanently, with no future budget ask.**

## 7. Budget shape

- **Year one build:** ~32–40 person-hours, entirely inside the writer's existing 8h/week allocation — fits inside your 8-week window with room to spare.
- **Year two recurring:** ~1–2h/week, steady state. If this ever exceeds what the writer can absorb alongside their other work, that's the signal to stop adding content to the path, not to hire — hiring isn't on the table per your constraint, so the plan is designed to never need it.

## 8. Measurement plan

- **Reaction:** click-through rate from the "Start Here" page into step 2+. Baseline: capture at soft-launch, no prior number exists.
- **Learning:** proxy self-check at the end of stage 1 ("data visible in your dashboard? yes/no" — a simple in-page checkbox, not a graded lab).
- **Behavior:** depth of product usage 30 days after a user first lands on the path (which features/stages they reach), if your product analytics can tie a docs visit to an account — see identity join below.
- **Results (the number for the board):** volume of "where do I start"-type inbound emails/tickets per month. Baseline = the real count from the week-1 audit (§1). Target: a stated reduction (self-set — propose 50% within two quarters, replace with your own once you have a real baseline) by the review date below.
- **Identity join, decide before launch:** you likely have no existing link between "someone read the path" and "someone's account/usage." Cheapest fix: UTM-tag the path's outbound links and tag inbound support tickets as "onboarding-navigation" at intake — both are configuration, not engineering, and both need to exist before launch or the behavior/results numbers above can't be reconstructed later.
- **Not measured this year:** revenue/expansion attribution — no clean counterfactual at this scale without more instrumentation than this plan budgets for.

## 9. Kill rule

If onboarding-navigation ticket volume has not dropped materially (target: 50%, replace with your real target once baselined) by the review date **[set at ~2 quarters post-launch]**, and path click-through is flat, stop actively curating: fold the page into normal docs maintenance at whatever state it's in, and reopen this gate only with new evidence. Separately: if the writer role is reduced or reassigned and not backfilled within one release cycle, freeze the page rather than let it silently go stale.

## 10. First-90-days sequence (front-loaded to hit the 8-week board date)

- **Week 1:** Tag real inbound "where do I start" volume for the last 2–3 months → real baseline number for both the gate and the board deck. Inventory all 41 tutorials + 12 videos against the 5-stage map in §4; name gaps honestly.
- **Weeks 2–3:** Sequence content into stages; confirm with 2–3 recent new users or support whether the order matches how they'd actually expect to learn it.
- **Weeks 4–5:** Build the "Start Here" page; add link-level tracking and the stage-1 self-check; write the one likely gap piece if needed.
- **Week 6:** Soft-launch — link it from the welcome email or in-app onboarding if one exists, or from the docs homepage if not.
- **Week 7:** Let it run; collect first click-through and ticket-volume numbers.
- **Week 8 (board review):** Present the charter, the live artefact, and the first two weeks of real numbers against the baseline — a shipped thing plus a trend, not a proposal.
- **Weeks 9–13 (post-board, continuing toward day 90):** First full-release refresh pass; start tracking toward the kill-rule review date; prioritize any stage with the highest drop-off for a content fix.

## 11. Where each number came from

| Number | Source |
|---|---|
| 41 tutorials, 12 videos, 2,400 active orgs, 8h/week writer capacity, 8-week board deadline | Your own figures |
| "A week to curate" as the baseline effort for this tier | This skill's own stated baseline for the curated-path rung — not measured, a starting estimate |
| 5-stage competency map | My inference from typical observability-SDK adoption journeys, not sourced to Quillstone data — confirm/replace against your real content and support themes in week 1 |
| 20% gap-tolerance threshold | This process's own baseline threshold (borrowed here from the equivalent curriculum-trace rule), not a published standard — adjust freely |
| 50% ticket-reduction target, click-through targets | Self-set placeholders — replace with real numbers once you have a baseline from week 1; do not present these as researched |
| Kirkpatrick's four measurement levels (reaction/learning/behavior/results) | Kirkpatrick, popularized 1959/1994; his own publisher's emphasis on starting from Level 4 is a real, citable methodological point, used here to justify pairing the ticket-volume metric with the click-through metric rather than reporting engagement alone |
| Monthly/quarterly refresh cadence | Assumed, not confirmed — replace with your SDK's actual release cadence |

---

**Open items to confirm, not blockers:** the real weekly-email count (§1), your actual release cadence (§6), and whether any enterprise/partner motion exists that would change §5's "no credential" answer. Everything else in this charter is buildable as written, inside the capacity you already have, in time for the board review.