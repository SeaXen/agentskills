# Stonecourse Certification Policy — Validity, Renewal & Re-alignment (draft v0.1)

Two corrections before the policy text, because both change what "mirror the competitor" should mean here:

**"Industry standard" isn't real.** CKA and HashiCorp chose 2 years with a paid retake; AWS chose 3 years with a discount voucher; Microsoft chose 1 year, renewed free via an unproctored open-book check. Four shipped programs, four different answers — that's a spread of deliberate business choices, not a convergence on a norm. Below I keep your 2-year/paid-retake instinct, but I name it as matching CKA/HashiCorp specifically, and what that choice trades away (a larger free-renewal installed base, which is what AWS and Microsoft optimize for instead). If that trade isn't the one you want, say so and the validity section changes.

**The re-alignment window doesn't transfer — the math breaks it.** CKA's "4 to 8 weeks" is sized against Kubernetes' own cadence: three minors a year, roughly one every 15 weeks. An 8-week realignment still lands with margin before the next minor ships. Stonecourse ships a minor every 3 weeks. Applying CKA's window literally means realignment (4-8 weeks) takes 1.3x to 2.7x longer than the gap between releases that triggered it — the item bank can never catch up, and by the time one realignment finishes, one or two more releases have already shipped behind it. That's the exact failure this skill's reference names: *"A program shipping faster than it can re-align its exam certifies a version nobody runs."* Section 3 below is not a mirror of CKA's number — it's a different mechanism sized to your cadence.

One thing to confirm before this policy is load-bearing rather than draft: certification is only the right rung if (a) a named buyer or partner contract will actually count certified heads, (b) the year-2 recertification cycle is funded, not hoped for, and (c) one person owns the item bank indefinitely. If any of those three isn't true yet, this policy is still fine to write, but the program itself should be scoped as a skill badge until they are.

---

## 1. Validity

**Stonecourse Certified Practitioner is valid for 24 months from the pass date.**

- Matches CKA and HashiCorp's Associate/Professional tiers (both 2 years) — the closest published comparators for a performance/lab-weighted devtool exam, not an industry baseline. *(Sourced: CKA and HashiCorp certification pages, per this program's reference material — re-verify both live before quoting the window to a buyer or partner; not re-checked this session.)*
- Explicitly rejected: AWS's 3-year window (optimizes for a larger, less-current certified base) and Microsoft's 1-year window with free renewal (optimizes for installed-base size over per-credential revenue). Pick 24 months only if per-credential revenue and a leaner, more-current certified population matter more to Stonecourse than certified-headcount volume — that's the actual trade-off being bought, not the 2 years by itself.
- Expiry date is fixed at pass date + 24 months, not re-based on partial credit or exam-version changes mid-cycle.

## 2. Renewal

**Renewal is a full-price retake of the current exam version. No free or discounted maintenance-activity path at launch.**

- Renewal window opens 6 months before expiry (matching HashiCorp's pattern) so a holder can retake early without losing time on an already-valid credential. *(Self-set: the 6-month window itself is this policy's own baseline, borrowed only as a mechanic, not a claimed standard.)*
- A retake always tests the **current** exam version, not the version the candidate originally passed. Given §3's re-alignment cadence, a candidate who waits until month 24 to renew is retested against content that has absorbed roughly 8 quarterly baselines' worth of drift since their original pass — that's disclosed to candidates up front, not a surprise at renewal time.
- No score banking, no partial-credit renewal. If Stonecourse later wants an activity-based or reduced-friction renewal path (AWS- or Microsoft-style) to grow the certified base rather than maximize per-credential revenue, that's a distinct policy change to negotiate explicitly — don't default into it by relaxing this one over time.
- *(Flag: paid-retake-only only pays for itself if enough people value the credential enough to pay twice. If the first cohort's retake rate comes in low, that's the signal to revisit toward a free/activity-based renewal — write that threshold into the kill-rule section of the wider charter, not into this document.)*

## 3. Re-alignment

This is where mirroring the competitor breaks, so the mechanism differs from CKA's on purpose.

**3.1 Not every minor triggers a re-alignment.** Each Stonecourse minor is triaged against the certification's competency map (the job-task-derived list, not the changelog) within one week of release. Only a minor that changes, adds, or removes an **assessed** competency counts as a re-alignment trigger. Most 3-week minors will touch surface area the exam doesn't test and trigger nothing.

**3.2 Exam content is versioned against a quarterly baseline, not against every minor.** The item bank, lab images, and any accompanying courseware are pinned to a named baseline release (e.g., "Stonecourse Certification Baseline 2026.Q4") refreshed on a ~13-week cycle — roughly one baseline per 4 shipped minors. This decouples "what the exam tests" from "what shipped last Tuesday," which is the only way a 3-week ship cadence and a defensible, stable exam can coexist. *(Self-set: the quarterly cadence and the 13-week/4-minor batching are this policy's own baseline, sized to your release cadence — not copied from any vendor.)*

**3.3 Competency-impacting changes get a bounded emergency SLA, separate from the baseline.** If a triaged minor changes an assessed competency in a way that makes a graded exam task wrong, unsafe, or no longer representative (a breaking change to a certified workflow, not a cosmetic one), re-align that specific item within **6 weeks** of the triggering release — roughly two Stonecourse release cycles. That's deliberately shorter than CKA's 4-8 weeks in absolute terms, because your release cadence is roughly 5x faster; stated as release cycles rather than calendar weeks, it's a comparable buffer, not a laxer one. It still means a candidate could sit an exam in weeks 1-6 after a breaking minor and be tested against a task that no longer reflects the shipped product — disclose that window explicitly rather than implying zero drift.
- Owner: the named item-bank owner (per the operating model) runs the weekly triage in 3.1 and is accountable for the 6-week SLA in 3.3; this is a standing weekly task, not a per-incident scramble.
- Courseware and lab images follow the same trigger and the same 6-week SLA as the exam items they back — CKA's competitor language bundles "courseware" and exam alignment together, and that's the one part worth keeping, since they go stale for the same underlying reason and should not be tracked separately.

**3.4 Escalation trigger.** If competency-impacting minors are landing faster than one per 6-week SLA window on a sustained basis (i.e., the emergency path itself can't keep up), that's the observable signal to either slow the assessed surface area (certify a narrower, more stable competency set) or fund a second item-bank maintainer — not to quietly let the SLA slip.

---

### Where each number came from

| Item | Status | Source |
|---|---|---|
| 24-month validity | Comparator, not standard | CKA, HashiCorp certification pages (per skill reference; re-verify live before quoting) |
| Paid full-price retake | Strategy choice | Matches CKA/HashiCorp; explicitly rejects AWS discount-voucher and Microsoft free-renewal models |
| 6-month renewal window | Self-set baseline | Borrowed as a mechanic from HashiCorp, not claimed as standard |
| Weekly minor triage | Self-set baseline | Sized to your 3-week ship cadence |
| Quarterly (~13-week) baseline cycle | Self-set baseline | Sized to batch ~4 Stonecourse minors per exam version |
| 6-week emergency re-alignment SLA | Self-set baseline, deliberately not copied from CKA's 4-8 weeks | Reasoned from your 3-week cadence being ~5x Kubernetes' ~15-week cadence |
| Kubernetes' ~15-week/3-per-year minor cadence | Background knowledge, not independently re-verified this session | Confirm against Kubernetes' current release cadence page before this figure appears in anything shown to a buyer |