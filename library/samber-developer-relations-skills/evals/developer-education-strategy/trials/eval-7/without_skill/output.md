# Marrowfield Backend Engineering Academy

A 6-week, cohort-based onboarding program that replaces ad-hoc ramp-up with a structured curriculum, graded hands-on labs, and a certification gate before production access. Target: cut time-to-first-meaningful-ship from ~10 weeks to ≤6, without lowering the bar for who gets prod access — raise confidence in *when* they get it instead.

Every stack-specific reference below (`[LANG]`, `[QUEUE]`, `[ORCHESTRATOR]`, etc.) is a placeholder — fill from the customization checklist in §11 before running cohort 1.

## 1. Goals & how the academy is judged

| Metric | Baseline (today) | Target (academy) |
|---|---|---|
| Time to first PR merged | unmeasured | ≤ day 5 |
| Time to first meaningful ship | ~10 weeks | ≤ week 6 |
| Time to unsupervised prod access | ~10 weeks, informal | week 6, gated on cert |
| Certification pass rate (first attempt) | n/a | 70-85% target band |
| 90-day voluntary attrition, new hires | unmeasured | tracked, flagged if >10% |
| Manager satisfaction with cohort readiness | unmeasured | surveyed each cohort |

If pass rate is >90%, the bar is too low. If it's <60%, week 1-5 content is failing people, not the exam — fix curriculum before tightening the gate.

## 2. Design principles

- **Cohort-based, not solo self-paced.** Batch hires into monthly cohorts of 2-4; peer pressure and shared labs beat isolated video-watching.
- **70/20/10 split**: hands-on labs / pairing & code review / lecture. Lecture is the least effective part and gets the least time.
- **Real stack, sandboxed.** No toy Todo-app labs — every lab runs against a namespaced clone of the actual service mesh with synthetic data.
- **Weekly checkpoints, not one final exam.** Struggling hires get caught in week 2, not week 6.
- **Certification is a capability gate tied to week-7 reality**, not a trivia quiz. Every question maps to something they will actually face on-call.
- **Instructors are senior ICs on rotation**, not a permanent training team — keeps content from going stale, spreads the tax.

## 3. Operating model

- **Cadence**: monthly cohort start, batches of 2-4 (absorbs ~30/year without needing weekly cohorts).
- **Timeline per hire**: Week 0 (pre-boarding, async) → Weeks 1-6 (curriculum) → Week 7 (supervised on-call shadow, first solo prod deploy watched by mentor) → graduate.
- **Roles**:
  - *Academy Lead* — 0.5 FTE, rotates quarterly among senior engineers. Owns schedule, cert panel logistics, metrics.
  - *Module Owner* — one senior engineer per week's module, ~4h/week during their cohort's run. Owns lecture content + lab grader + keeps it current.
  - *Cohort Mentor* — 1 per 2 hires, buddy for daily unblocking and PR review, not a lecturer.
  - *Certification Panel* — 3 senior engineers + the hiring EM, convened week 6 only.

## 4. Curriculum, week by week

**Week 0 (pre-boarding, before day 1, async):** accounts/access provisioning, laptop + local dev environment setup, architecture overview doc, service map, read the on-call runbook index. Goal: day 1 starts with a working `[ORCHESTRATOR]` local stack, not a laptop-setup day.

**Week 1 — Systems map & the dev loop**
- Lecture: architecture walkthrough, request lifecycle end-to-end, where the money/data actually flows.
- Lab 1: bring up the full local stack (`[ORCHESTRATOR]`, `[DB]`, `[QUEUE]`), hit one endpoint through every layer, all tests green.
- Lab 2: seeded-bug hunt — a real, redacted historical bug planted in a sandbox branch; find it, fix it, open a PR.
- Checkpoint: environment verified, first PR merged (trivial fix counts).

**Week 2 — Contribution workflow**
- Lecture: coding standards, gates/linters (see coding-gates equivalent for Marrowfield), branch/PR conventions, review culture, what a "good" PR looks like here.
- Lab: pick a pre-tagged `good-first-issue` from the real backlog, ship it end to end (branch → code → tests → PR → address review → merge), paired with mentor.
- Checkpoint: first real backlog PR merged to main.

**Week 3 — Data & APIs**
- Lecture: schema ownership model, migration process, API contract/versioning policy, backward-compatibility rules.
- Lab A: add a field requiring a real migration + API change, with a backward-compatibility test that fails on breaking changes.
- Lab B: given a deliberately slow query, use `EXPLAIN`, add an index, benchmark before/after, document the delta.
- Checkpoint: migration lab passes CI grader; benchmark improvement documented.

**Week 4 — Distributed systems & resilience**
- Lecture: service-to-service comms, `[QUEUE]` event patterns, retries/idempotency/timeouts, common failure modes.
- Lab A: chaos lab — a dependency is killed in the sandbox; observe the blast radius, add retry/backoff/circuit-breaker, re-run the chaos suite until it passes.
- Lab B: build a small async consumer end to end, including dead-letter handling.
- Checkpoint: resilience lab passes the automated chaos test suite.

**Week 5 — Observability, security, incident response**
- Lecture: logging/metrics/tracing stack, dashboards, alerting, on-call runbooks, authn/authz basics, secrets management, common OWASP-class mistakes, incident process.
- Lab A: instrument the week-4 service with logs/metrics/traces, build a dashboard, wire one alert.
- Lab B: mock incident — broken staging deploy + runbook, diagnose and resolve inside a time box, write a postmortem.
- Checkpoint: dashboard live, postmortem submitted.

**Week 6 — Capstone & certification**
- Capstone: ship one real, moderately-scoped backlog ticket solo, start to finish — design note, code, tests, review, merge, deploy to staging, watch it for 24h.
- Certification (§5).
- Pass → production access granted at end of week 6.
- Partial fail → targeted 2-week remediation on the failed component only, not a full repeat.

**Week 7 (post-cert):** first on-call shadow shift, first solo prod deploy with mentor watching live, then graduate from the academy.

## 5. Certification — four independent gates, all must pass

Blending everything into one score lets one strong area mask one critical gap. Each is pass/fail on its own rubric.

1. **Capstone ship** — code quality, test coverage, review responsiveness, whether it actually reached staging cleanly.
2. **Practical exam** (timed, sandboxed) — fix a production-like bug from a report; design a migration from a schema; optimize a slow query. No trivia; every task is a compressed version of a real week 1-4 lab.
3. **Incident/postmortem defense** — walk the panel through the week-5 incident: what broke, what they'd do differently, whether they know the escalation path.
4. **Production Readiness Review** — live panel Q&A: "this pages you at 2am, what do you do," "how do you know it's safe to ship on a Friday," "walk me through rolling this back."

Rubrics scored independently by 2+ panelists, then reconciled — reduces single-grader bias. Fail one component → re-sit only that component after remediation; pass three of four does not average to a pass.

## 6. Lab design principles

- Sandboxed clone of the prod stack, namespace-isolated, synthetic data only, cost-capped — never touches real customer data.
- Every lab has a written spec, a starter branch, and an automated CI grader giving pass/fail plus rubric feedback — not "ask a mentor and hope."
- Seeded-bug labs are rotated from real, redacted historical incidents, so the curriculum reuses institutional knowledge and stays current by construction.
- Labs live in a versioned repo, owned like production code; module owners update the lab set each cohort based on where people actually fail.

## 7. Staffing & cost

| Role | Time / cohort | Headcount needed | Note |
|---|---|---|---|
| Academy Lead | ~10h/wk × 6wk | 1, rotates quarterly | Logistics, metrics, panel scheduling |
| Module Owner ×6 | ~4h/wk during their week | 6 (can repeat across cohorts) | Keeps content honest — they own real code too |
| Cohort Mentor | ~3-5h/wk | 1 per 2 hires | Daily unblocking, PR review |
| Cert Panel | ~4h, week 6 only | 3 seniors + EM | One-time per cohort |

At 30 hires/year in cohorts of 3, that's ~10 cohorts/year — roughly 1.5-2 senior engineers' worth of time annualized. Budget it explicitly against a hiring manager's headcount plan; it's cheaper than 10 weeks of unstructured ramp-up repeated 30 times.

## 8. Feedback loop

- Track per-module pass rate and per-lab completion time — a module with consistently low pass rate is a content problem, not a hiring-bar problem.
- Post-cohort survey from graduates and their managers.
- 90-day retention and manager satisfaction, tied back to which cohort/module owners were active.
- Quarterly retro with module owners: drop or rewrite stale labs; repeat cert failures on the same component are a signal to fix the docs/lab, not to lecture harder.

## 9. Rollout plan

- Weeks -6 to -1: module owners draft content and lab graders in parallel; Academy Lead assembles cert rubrics and panel logistics.
- Pilot cohort of 2 (not 4) — treat it as a dry run, expect to rewrite 30-40% of labs after it.
- Scale to standard cohort size only after pilot retro.

## 10. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Senior engineer burnout from teaching tax | Rotate module ownership quarterly; cap at one module per person per cohort |
| Sandbox stack drifts from real prod | Module owner re-validates their lab against current prod config every cohort |
| Cert becomes gatekeeping theater | Every question must map to a real week 1-5 task; review rubric quarterly against actual on-call incidents |
| Hiring is lumpy, cohorts aren't full | Allow solo "cohort of 1" runs with async peer group from the prior cohort rather than delaying start |
| 6 weeks is too tight for some hires | Remediation extends the failed component only, never treated as a strike |

## 11. Customization checklist before cohort 1

Fill these in and thread them through every lecture and lab above:

- Primary language/framework (`[LANG]`)
- Database engine + migration tool (`[DB]`)
- Queue/broker (`[QUEUE]`: Kafka/SQS/RabbitMQ/etc.)
- Orchestration platform (`[ORCHESTRATOR]`: Kubernetes/ECS/etc.)
- Observability stack (logs/metrics/tracing tool names)
- On-call/paging tool and escalation policy doc
- Feature flag system, if any
- The actual tag/label used for `good-first-issue` in the backlog tracker
- Repo hosting the sandbox stack and where lab graders will live in CI