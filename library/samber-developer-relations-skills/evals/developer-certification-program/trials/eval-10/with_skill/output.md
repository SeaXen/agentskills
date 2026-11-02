**Answer to your Canada question: no. Don't call them "Certified Engineers".** Two reasons:

- **"Certified" is the wrong tier.** What you describe is a skill badge, and the skill says never present a badge as a certification. "Certified" returns when a buyer contract counts certified people.
- **"Engineer" is a regulated title.** The skill's logistics checklist flags it as regulated in Canadian provinces. Your candidates are in Ontario and Quebec, so ask counsel before using it. I did not check the statutes, and this is not legal advice.

Rename it now. Suggested: **Sindral Feature Flags Implementer** badge. Alternative: "Sindral Badge: Implementer". Reword any agency agreement that says "certified engineers" to name the badge.

**Next action (30 min):** email 5 customers who hired agencies. Ask: "Would a Sindral badge change which agency you shortlist?" That answer decides the gate below.

I read the SKILL.md and its three references (`charter-example.md`, `assessment-integrity.md`, `exam-build-and-operations.md`). The interview was skipped because you asked for the full deliverable in one pass. Unanswered questions are marked ⚠️ and gathered at the end. Every number is **self-set** unless it says sourced.

## Verdict on your draft

| Draft item | Verdict | Why |
|---|---|---|
| 8 features × 12.5% | ❌ Change | A blueprint comes from a job task analysis, not the feature list. Equal weights mean no task analysis was done. |
| 3 variants per feature | ❌ Change | 24 tasks cost about 170h to build, more than your 120h (math in section 4). |
| 75% of checks passed | ❌ Change | No standard-setting behind it. A pass mark you can't defend to a failed candidate or a buyer is a guess. |
| Skip pilot | ❌ Change | Eleven devs is the right size for a pilot. The charter example pilots with ten. |
| 120h, no reviewers | ⚠️ Blocker | No reviewers means no second-expert check and no panel. Also no named successor. |
| Accommodations in candidate record | ❌ Change | Treat them as health data. Reviewer-only store. |
| "Certified Engineer" | ❌ Change | See above. |

## Charter

### 1. Gate verdict

- **Consumer:** customers who hire the agencies. They are outside Sindral.
- **Action to confirm:** shortlisting agencies by badge, or browsing a directory of badge holders.
- **Evidence now:** agencies ask for it. That is holder-side demand. No customer has been named.
- **Ceiling:** skill badge. Role certification needs a buyer contract or tender that counts certified people.
- **Rejected alternative:** completion badge only. It proves attendance, so a client can't rely on it.
- **If the 5-customer check returns zero interest:** the gate falls to "only holders want it". Ship a free badge with no fee and no directory push.
- **Certification trigger (observable):** a customer contract or tender naming certified people, plus two years of funded re-alignment.

### 2. Tier, format, proctoring, levels

- **One level.** "Implementer", skill-badge tier. Deleted: an Expert exam, role certification now, any multiple-choice exam.
- **Format:** auto-graded hands-on tasks in a disposable Sindral tenant. Checkers verify the end state.
- **AI policy: allowed.** Agency devs use assistants on the job, so the claim reads "works competently with their own tools". Banning is unenforceable without live proctoring.
- **Human-attributable step:** a 15-minute live call on 1 pass in 10. The holder explains and changes their own solution. A refused or failed call suspends the badge pending a supervised retest, with appeal. Announce this in the candidate agreement.
- **Proxy sitting is the named threat.** Agencies will badge staff in bulk, so one strong dev could sit for colleagues. The sampled call is the counter.
- **Identity:** account login. No face matching, so no biometric review is needed.
- **Later Expert level:** a client project plus live defence, never an exam. Trigger: a customer asks for the distinction, and the first level has lived through one major version or 12 months.

### 3. Competency blueprint

Weights come from the job task analysis. I can't invent them without your data.

1. Interview 8 agency devs (45 min each). Read 2 quarters of support tickets from agency-built integrations.
2. List the tasks agencies do with Sindral: rollout, targeting, SDK wiring, experiments, cleanup and the like.
3. Score each task: frequency (1–5) × cost of a mistake (1–5).
4. Group tasks into 4–5 domains. Weight = domain score ÷ total score.
5. Publish domains and weights.

Your eight features are an input to step 2, not the blueprint. Expect some features to merge and some to drop. Weight source: self-set from interviews and tickets.

### 4. Build plan (self-set, against 120h)

| Line | Hours |
|---|---|
| Job task analysis | 14 |
| 4 domains × 2 variants = 8 tasks, at 7h each (authoring, tenant seed, checker, reference solution) | 56 |
| Pilot with the 11 devs (recruit, run, analyse) | 12 |
| Standard-setting panel (prep and session) | 7 |
| Issuing service (buy) and verification page | 6 |
| Candidate agreement, accommodation process, privacy check | 6 |
| Free practice quiz plus published blueprint | 4 |
| Live-explanation protocol | 2 |
| Go/no-go, metrics, directory page | 6 |
| **Total** | **113** (7h buffer) |

- **Why not 24 tasks:** at 7h each that is 168h for tasks alone, which breaks the ceiling. Per the skill, cut variants, domains, or the tier. Never cut the pilot or the review.
- **Not in the 120h:** post-launch work. That means re-running checkers each release, the live calls, appeals, and the yearly fixed cost.
- **Prep course:** not at launch. The blueprint plus the practice quiz is enough. A course on a MOOC or edtech platform is the first scale step.
- **Issuing:** buy a service that exports Open Badges 3.0. Keep the master holder record in a system you own.

### 5. Integrity plan

- **Cut score.** Replace "75% of checks" with a panel method. The method is a modified Angoff adapted to end-state checks (sourced: Cizek and Bunch, *Standard Setting*, 2007, via `assessment-integrity.md`). The panel reviews pilot solutions and writes each task's minimum end-state checks. Each check is marked must-pass or scored. Pass = every must-pass check met in every task.
- **Panel size:** the skill says 5–15 experts is typical. Use 5, drawn from senior agency devs outside the pilot cohort. Compensate them. This is the "reviewers" gap in your plan.
- **Variants:** pilot solve times and pass rates must match across variants of one task. Retire a variant that drifts.
- **Item security:** two variants per task, rotated per sitting. Watch the pass rate per variant. A sudden rise signals a leak. Confidentiality clause in the candidate agreement, with revocation as the sanction.
- **Checkers:** run in CI against every Sindral release. A failing checker pulls its variant until fixed.
- **Reviewers needed (minimum 2):** one second-expert technical review per task, and checker failures at about 2h a month. If you can't get two, the skill's fallback is a completion badge at launch.
- **Accommodations:**
  - Catalogue: extra time, assistive technology, breaks, relief from environment rules.
  - Request before scheduling, with a stated processing time. Microsoft's is up to 20 days (sourced, from `assessment-integrity.md`). Yours is self-set at 10 business days.
  - Intake goes to one named reviewer, not support.
  - **Do not put requests or reasons in the candidate record.** Treat them as health data. Only the reviewer sees them, with a set retention (self-set: delete 12 months after the decision).
  - The sitting config holds only the granted adjustment, for example a time multiplier. Support sees "adjustment applied", never why.
  - Appeal path for denials.
  - Support can't see the history. That is the point.
- **Privacy:** run the review before launch. Canada is multi-jurisdiction, and Quebec has its own privacy regime. ⚠️ Check it, and check whether the exam and handbook need French for Quebec candidates.

### 6. Renewal, version binding, retirement

- Stamp the badge with the Sindral major or API version tested. No expiry. ⚠️ Needs your release cadence and version-support length.
- On a new major version, a 30-minute delta task covering only what changed, with the same sampled live call. The older badge stays valid, labelled with its version, while that version is supported.
- Retake: 14-day wait, 3 attempts per 6 months, no repeat fee. Self-set.
- Exam-version retirement: announce in advance, keep holders valid, stamp the version, offer a path to the replacement.
- Program retirement: honour every badge, keep verification live 3 years after the last issue (self-set), honour sold vouchers.

### 7. Price, vouchers, verification

- **Price follows the consumer.** Until a customer-side action is evidenced, treat demand as holder-only: free for the first cohort. Set the fee at go/no-go once directory contacts exist.
- **Fee formula** (from `exam-build-and-operations.md`):
  - `break-even fee = (yearly fixed + yearly operating) / expected attempts per year + cost per attempt − amount absorbed by a contract or program`
  - Charge per attempt, never per holder.
  - Needs your hosting cost per sitting and expected volume.
- **Agency seats:** sell seat bundles to agencies, a fee one engagement repays.
- **Vouchers:** expiry, single use, no resale, tracked by campaign. Don't count voucher sittings as organic demand.
- **Verification:**
  - Open Badges 3.0 credential with a status entry. Revocation updates that status.
  - Verify by credential ID or holder link.
  - The directory is opt-in: name, agency, region, languages, contact. For agency devs it is the main return on the fee.
  - Shown fields: holder, credential, version, issue date, "no expiry", status. A revoked badge shows "not valid" with no reason.
- **Candidate agreement:** conduct, AI policy, sampled live call, item confidentiality, revocation grounds, appeal to a named decision-maker. ⚠️ Name that person.

### 8. Operating model

- **Owner:** you, 7h a week during the build. ⚠️ **Successor: unnamed.**
- **Reviewers:** none today. Required: 2 (see section 5).
- **Partners:** none at launch. Later: a course on a MOOC or edtech platform, or authorised training partners. Firewall for both: no one who sees live items writes the course, no trainer proctors their own students, and no revenue share on passes.
- **Budget line:** ⚠️ unset.

### 9. Measurement, go/no-go, kill rule

- **Outcome metrics (customer side):** customer RFPs or shortlists naming the badge, directory contact requests from customers, deals where an agency won citing it, escalations per project from badged versus other agency teams.
- **Health signals only:** pass rate per variant, checker failures per release, appeals, revocations, live-call failures.
- **Dates:** today is 2026-10-23, so the 4-month window ends about 2027-02-23.
  - **Go/no-go: 2027-02-01.** Requires pilot data, all checkers green, panel done.
  - **Fallback:** launch a completion badge, ship the assessed badge next quarter.
- **Kill rule (self-set):** no customer-side outcome within 18 months of launch, by 2028-08, or checkers missing their re-alignment window on two consecutive Sindral releases.

### 10. Where each number came from

- **Sourced:** the 5–15 panel range and the modified Angoff method (Cizek and Bunch 2007). The 20-day accommodation figure (Microsoft, as quoted in the skill's reference file; not re-read from Microsoft's site).
- **Self-set:** everything else. That covers all hours, the 8 interviews, 8 tasks, 2 variants, 1-in-10 live calls, 15-min and 30-min tasks, retake limits, retention periods, 3-year retirement tail and the kill threshold.

## Open questions

These are the ⚠️ items. The first three block the plan.

1. Who is your named successor and who are your 2 reviewers? Without a standing owner, the skill deletes every option above completion badge.
2. Do any customers act on the badge? Run the 5-customer email first.
3. By when must the first badge ship, and what forces that date?
4. How often does Sindral ship user-visible change, and how long is a major version supported?
5. Must the program pay for itself, or run as a cost centre?

Also confirm: do the 120 hours cover the build only, and what existing courses, sandbox tenants or badge service do you have?

Step 1 of 12 of the skill's workflow (interview and gate) is draft-complete. The next step is your answers to 1–3.