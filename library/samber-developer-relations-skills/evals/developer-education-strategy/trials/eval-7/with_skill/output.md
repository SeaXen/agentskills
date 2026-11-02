**Scope note, per the skill's own routing rule:** `developer-education-strategy` explicitly declines this exact request. Its scope check says: *"Internal employee onboarding and engineering ramp-up belong to people/L&D — that audience is captive, there is no adoption funnel to protect and no external consumer for a credential, so every trade-off in this skill points the wrong way for it. Say so and stop if that is the request."* Backend engineers ramping up at Marrowfield are a captive internal audience, not external users/customers/partners/students — so I'm not applying the skill's rungs (badge/certification sized for procurement currency, partner contracts, public credential compliance) here.

What carries over usefully regardless of audience: prove the problem before designing content, build backward from a job task analysis instead of a feature tour, name one owner, tie refresh to release cadence, and set a kill rule before launch. I used that method below, stripped of the external-facing apparatus (no partner delivery, no public badge, no procurement pricing).

---

# Marrowfield Backend Engineering Academy — Program Design

## 1. Problem and evidence

Current state: new backend hires take ~10 weeks to ship anything meaningful. At 30 hires/year, that's roughly 300 person-weeks/year of reduced output plus the mentor time currently burned re-explaining the same things ad hoc. Before building six weeks of curriculum, validate the 10-week number isn't actually two different problems wearing one number:

- Pull the last 6–12 months of new-hire 1:1 notes, onboarding survey comments, and the #eng-onboarding (or equivalent) Slack channel for recurring questions.
- Check whether the delay clusters around a repeatable, learnable sequence (architecture, data layer, deploy pipeline, on-call) — the case education fixes — or around access provisioning, unclear ownership, or missing docs for a specific service — cases a checklist or an IT ticket fixes cheaper than a curriculum ever will.
- If it's a genuine mix, keep the academy scoped to the competence gap only and fix the access/process delays separately; folding them into "curriculum" hides a ticket-queue problem behind a training problem.

Assume validation confirms a real competence gap (stated architecture, unfamiliar stack, and production-safety practices dominate the delay) — that's the case this design addresses. If validation instead shows most of the ten weeks is waiting on laptop provisioning or repo access, fix that first; it's cheaper and faster than anything below.

## 2. Program shape

Structured curriculum with hands-on labs on your own stack, gated by an internal competency check before production access. Not a public certification: nobody outside Marrowfield consumes this credential, so skip identity verification, expiry, appeals, and recertification — those exist to protect a claim strangers rely on. What you keep from that heavier tier, because it fits a production-access gate specifically, is a defensible pass/fail bar set by a real panel, not a number picked by feel.

Rejected alternatives:
- **Ad-hoc content / better docs alone** — doesn't fix a 10-week ramp when the delay is a repeatable sequence people must learn in order, not a lookup problem.
- **Curated reading path with no labs** — cheapest, but buys "where do I start," not the practice-under-observation that actually shortens time-to-first-ship. Worth doing as week 0 pre-reading, not as the whole program.
- **External-style badge/certification with public verification** — wrong tool; nobody outside Marrowfield acts on this, so the compliance cost (identity checks, appeals path) buys nothing here.

Escalation trigger: if Marrowfield starts requiring certified staff for a partner/SI integration program or a customer-facing credential, that's a *different* audience and reopens the developer-education-strategy skill properly — don't retrofit this internal program for it.

## 3. Competency map (job task analysis)

Derive the real list from interviews with 5–8 recent hires plus support/incident data before finalizing — the list below is a reasonable backend-engineering starting structure, not a substitute for that step. Each competency needs at least one lab or artifact as evidence; cut anything that doesn't trace to a real task.

| Competency | Evidence |
|---|---|
| Codebase & architecture orientation | Guided first PR merged to a real repo |
| Local dev environment & CI | Green CI run on a branch, unassisted |
| Service-to-service communication (API contracts, queues) | Lab: add an endpoint/consumer against a sandbox |
| Data layer (schema, migrations, caching) | Lab: write and run a safe migration |
| Testing standards | Lab: add unit + integration tests that pass CI |
| Observability (logs, metrics, traces, alerts) | Lab: diagnose a seeded bug using real dashboards |
| Security & access model (secrets, least privilege) | Quiz + walk the access-request process live |
| Deployment pipeline & rollback | Lab: supervised deploy to staging, execute a rollback |
| Incident response basics | Timed scenario: staging service throwing errors, fix and document |
| Production-change judgment | Capstone: ship one real, scoped change end-to-end |

If more than 20% of the modules you actually draft don't trace to a task on this list, the curriculum drifted into a feature tour of your service catalog — restart from the interviews, not from the tech radar.

## 4. Six-week curriculum

Each week: one new concept area, one lab in a real (sandboxed) environment, one short mentor check-in. No week introduces two unrelated concepts.

- **Week 1 — Orientation.** System map, git/PR/code-review norms, environment setup. Lab: first guided PR merged.
- **Week 2 — Services & data.** How core services talk, primary datastore, caching. Lab: build a small endpoint against sandbox data.
- **Week 3 — Testing & CI/CD.** Test conventions, pipeline stages, feature flags. Lab: add tests to a real repo, pass CI unassisted.
- **Week 4 — Observability & reliability.** Logging/metrics/tracing/alerting. Lab: diagnose a seeded staging bug using dashboards only.
- **Week 5 — Security & deployment.** Secrets, access model, deploy pipeline, rollback. Lab: supervised staging deploy + rollback walkthrough.
- **Week 6 — Capstone.** Ship one real, scoped production change (design → review → test → deploy → monitor), paired with a mentor. This week doubles as the assessment.

Pre-work (week 0, optional, unlabbed): curated reading list of existing docs/architecture decision records — the cheap rung folded in as prep, not a separate program.

## 5. Certification gate (internal, not public)

Three components, all required for production access:

1. **Knowledge check** (low weight): architecture, access policy, incident runbook basics. Pass bar: 90%, unlimited retakes, no cooldown — this component screens for "read the material," not competence.
2. **Practical exam**: a timed, scenario-based lab (e.g., a staging service is failing — diagnose and fix within a time box), graded by two reviewers against a shared rubric. This is the real gate.
3. **Capstone sign-off**: the week-6 shipped change, reviewed through your normal code-review process plus explicit mentor sign-off that the hire operated with appropriate judgment, not just correct code.

**Cut score**: set by a panel of 3–5 senior engineers running a short calibration session on 8–10 anonymized past new-hire code samples/incidents before cohort 1 — this replaces a felt-sense pass mark with something you can defend if someone disputes a fail. Revisit the rubric quarterly, and any time the stack changes enough to make the calibration samples stale.

**On fail**: one week of paired remediation with the mentor, then retake the practical exam. No production access until pass — never grant conditional/probationary access as a workaround, or the gate stops meaning anything.

**Do not gate the content itself.** Anyone at Marrowfield can read the curriculum or watch the labs; only the production-access decision is gated on passing. Locking the material itself just slows down the people you most need ramped.

## 6. Operating model

- **Owner**: one named senior/staff engineer, accountable for curriculum accuracy and cut-score integrity. Not a committee, not "the platform team."
- **Staffing** (self-set estimate — validate against real Marrowfield hours):
  - Owner: ~10–12 hrs/week (curriculum truth, cohort scheduling, panel coordination).
  - Module SMEs (rotating senior engineers, one per competency area): ~2–4 hrs/week during refresh windows only.
  - Lab-environment maintainer: ~4 hrs/week — this is the line item that breaks every time the stack changes; budget it as standing cost, not a one-time build.
  - Mentors (drawn from the existing senior eng org, one per hire): ~2–3 hrs/week for that hire's six weeks.
  - Cut-score panel (3–5 senior engineers): one-time calibration session, then ~4 hrs/quarter each.
  - Rough total: ~1,250–1,300 engineer-hours/year spread across many people — closer to 0.6–0.7 FTE-equivalent than a dedicated headcount, at 30 hires/year.
- **Platform**: keep curriculum and lab definitions as code in a repo you own, run labs against existing staging/sandbox infra rather than standing up new infrastructure or buying an LMS. Track pass/fail status wherever you already track onboarding and access requests.
- **Refresh trigger**: any change to core services, the deploy pipeline, or the access model triggers a module refresh within 2 weeks — tighter than a typical content refresh window, because incorrect production-access material is a safety issue, not an accuracy nice-to-have. Full curriculum review quarterly.
- **Pricing**: free — it's internal headcount ramp-up, not a revenue line.
- **Partner delivery / localization**: not applicable at this scope.

## 7. Measurement plan

Reaction and learning-rate numbers alone don't tell you if this worked — track through to behavior and results, and decide the data join (HR/onboarding system ↔ git/PR/deploy/incident data) before cohort 1, since it can't be reconstructed retroactively.

- **Reaction**: post-week-6 survey — module clarity, lab realism, mentor quality. Target ≥4/5, first-cohort number becomes your baseline.
- **Learning**: first-attempt pass rate on the practical exam. No industry baseline exists for this — report cohort 1's number as your own baseline, not a target borrowed from elsewhere.
- **Behavior**: time from production-access grant to first independent (unpaired) merged production change; on-call shadow readiness by week 8–10.
- **Results**: time-to-first-meaningful-ship vs. the current ~10-week baseline; 90-day retention; defect/incident rate on new-hire changes in their first 90 days vs. the pre-academy baseline.

## 8. Kill rule

Set at launch, not after: if, after 3 cohorts (~9 months), first-attempt practical-exam pass rate stays below 50% **and** time-to-first-meaningful-ship hasn't improved by at least 2 weeks vs. the pre-academy baseline, pause new cohorts and rebuild the curriculum from a fresh job-task analysis rather than patch modules one at a time. Review checkpoint: quarterly, first hard checkpoint at cohort 3.

## 9. First 90 days

- **Days 1–15**: run the job task analysis — interview 5–8 recent hires, pull onboarding-channel question clusters and incident data touching new-hire changes. Build the real competency map from this, not from the list in section 3.
- **Days 16–30**: draft the six-week curriculum and labs from that map, recruit module SMEs, stand up lab environment on existing staging infra.
- **Days 31–45**: recruit the 3–5-person cut-score panel, run the calibration session on the practical-exam rubric using anonymized past new-hire samples.
- **Days 46–60**: pilot cohort (2–4 hires from the current pipeline) runs the academy live; owner and mentors shadow closely, collect reaction/learning data in real time.
- **Days 61–90**: retro the pilot, fix the worst-scoring modules, lock curriculum v1, schedule cohort 2, and calendar the quarterly review plus the cohort-3 kill-rule checkpoint.

## 10. Failure modes to avoid

- **Feature-tour curriculum** — modules mirror your service catalog instead of what actually blocked past hires. Restart from the interviews if this happens.
- **Orphan academy** — launched this quarter, owned by nobody by month four. Don't launch without the named owner in section 6.
- **Lab drift** — sandbox diverges from the real stack after 2–3 releases and the gate stops meaning anything. This is why lab-maintainer hours are a standing line item, not a one-time build cost.
- **Cut score picked by feel** — no calibration panel, no documented rubric, indefensible when someone disputes a fail. Avoided by the days-31–45 calibration session.
- **Gating the material, not just the access** — locking curriculum content behind the assessment slows down the exact people it should be speeding up.

## 11. Where the numbers came from

- 10-week baseline, 30 hires/year: given in the request.
- Staffing hours, cost total, cut-score cohort size, kill-rule thresholds, pass-rate target: this design's own baselines — replace with your first cohort's real numbers as soon as you have them.
- Kirkpatrick four-level structure (reaction/learning/behavior/results) referenced in section 7: published framework (Kirkpatrick Partners), used here as a measurement structure, not as a source of target numbers.

---

If Marrowfield later needs an *external*-facing credential — a partner/SI certification, or something enterprise customers' staff can earn — that's a different audience and the right moment to bring the `developer-education-strategy` skill back in properly, since that's exactly the case it's built for.