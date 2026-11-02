Using developer-education-strategy to evaluate Vantahold's academy request against the evidence you gave me.

**Quick answer, in the order the skill requires:**

1. **Gate verdict: No.** None of your four signals is a competence gap — the thing a developer academy is built to fix.
2. **Tier recommendation: ad-hoc content only** (one workshop + recording for the customer that asked). Curated path, curriculum with labs, badge, and certification are all rejected below.
3. **Operating model:** near-zero — one named person runs the single workshop; the real fixes belong to docs, engineering, and growth, not to an education program.

Full charter follows. Unanswered interview items (capacity, release cadence, timeline pressure, one-off-vs-compounding appetite, effort ceiling) only matter for *re-ranking tiers once the gate is open* — it isn't, so they're skipped rather than guessed at.

---

# Developer education charter — Vantahold Settlement Reconciliation API, 2026 H2

## Gate verdict

Education is not the right fix. Run each of the four inputs against the evidence gate:

| Signal | What it looks like | What it actually is |
|---|---|---|
| Biggest ticket cluster: "which endpoint returns settlement batches" | Sounds like a knowledge gap | The answer already exists, on page 4 of the API reference. This is "users cannot find an answer that exists" — **docs information architecture**, not education. |
| Second biggest cluster: expired token → generic 400 → ticket | Sounds like users not understanding auth | The API can distinguish this failure and doesn't. This is "users misuse an API that could refuse misuse" — **product and error-message design**, not education. |
| 62% of signups never complete a first successful call | Sounds like onboarding needs a course | This is "users fail at first success" — **quickstart and activation**, not a curriculum. |
| One customer's platform team asked for training, once | Sounds like the first academy customer | This is "one team asked once" — **a live workshop and a recording**, not a program. |

None of these is "the same conceptual misunderstanding dominating support," "deals blocked on trained staff," or "a repeatable sequence people must learn in order" — the actual triggers for a structured program. Rejected cheaper alternatives were not rejected; they weren't even tried yet, which is itself the finding: the VP's ask jumped past three near-zero-cost fixes straight to the most expensive rung on the ladder.

One more thing to check before trusting the headline number at all: **"support volume up 3x in six months" is not yet normalized.** If active API consumers also grew ~3x in that window, this is flat per-developer support load, not a regression. Pull ticket volume per active integration before using 3x as evidence of anything. This charter proceeds on the assumption it's at least partly a real per-user increase, but flags it as unverified.

## Audience and motion

Primary: bottom-up individual developers integrating the API — this is where three of your four signals sit (ticket clusters, signup funnel). Secondary: one enterprise-style customer's platform team, single ad-hoc ask, not a contract requirement or a repeated pattern. No partner/SI motion is evidenced. No hiring-market signal. No one asked for a credential — the VP proposed the *format* (academy); the ticket data doesn't support the *need* for one.

## Chosen tier, with rejected alternatives

**Chosen: ad-hoc content — one workshop, recorded.** Nothing above it.

Deleted, not parked:

- **Curated learning path** — deleted. Sequencing existing content into a reading order doesn't fix a *findability* problem (the answer is already written, just buried), doesn't fix a *first-call* problem (friction is in the actual call, not in reading order), and doesn't fix a *wrong error code* (no amount of reading order fixes a 400 that should be a 401 with `token_expired`).
- **Structured curriculum with labs** — deleted. No repeatable multi-step task requires practice under observation here; nothing in the evidence needs a lab.
- **Completion or skill badge** — deleted. No named external consumer: no buyer, no partner contract, no hiring manager counting credentialed staff. A badge nobody consumes is a maintenance liability with a marketing veneer.
- **Proctored certification** — deleted hardest. None of the three promotion conditions hold: no named buyer/partner counting certified heads, no funded recertification cycle, no owner for an item bank.

**Escalation trigger to the next rung (curated path):** reopen this gate only if, after the docs/error-message/quickstart fixes below have shipped for one full quarter, *either* (a) the two ticket clusters haven't dropped materially, *or* (b) two or more additional, distinct customers or partners request training in a single quarter (versus the one logged to date). Short of that, adding a program on top of unfixed docs/error/onboarding problems just gives the same confusion a syllabus.

## Competency map

Not applicable — no curriculum is being built. The one workshop's content is scoped and owned by whoever runs it, not authored here; this skill doesn't write lesson content.

## Credential decision

No credential. No external consumer exists to act on one — not a buyer, not a partner contract, not a hiring manager. If the escalation trigger above ever fires and a curated path gets built, revisit; a credential decision at that point still needs its own named consumer, not just a program that exists.

## Operating model

- **Owner:** one named person already supporting that customer account (solutions engineer or DevRel) runs the single workshop — not a standing role, not a team label.
- **Staffing:** ~2–4h prep, ~1h delivery, ~1–2h to cut and publish the recording. One-time. If a second or third customer asks (the escalation trigger), revisit staffing then — don't pre-build capacity for a demand pattern that's happened once.
- **The three real fixes are not owned by education:**
  - Settlement-batch endpoint discoverability → docs/technical-writing team (route to `developer-docs-structure-audit`).
  - Expired-token 400 → API/platform engineering (out of DevRel scope entirely — this is error-contract design).
  - First-call activation (62% drop) → DevRel or growth/PM (route to `developer-quickstart-guide`).
- **Platform:** none needed. Recording goes wherever existing customer-facing video already lives; workshop notes stay in the docs repo, not a new LMS.
- **Refresh trigger:** none — it's one-off. If repeated, refresh whenever the settlement-batch endpoint or the auth/token flow changes.
- **Pricing:** free, absorbed into existing customer-success time.
- **Localization / partner delivery:** not applicable — no demand signal for either.

## Budget shape

Year one: single-digit hours for the workshop (self-set estimate: 6–8h total), zero new tooling spend. The docs, error-message, and quickstart fixes are normal roadmap work for teams that already exist — call this out explicitly to the VP, because the honest budget answer to "build an academy" is *near-zero incremental spend*, since the real fixes were already other teams' backlog items.

Year two recurring: $0 for an academy, because none is being built. If the escalation trigger fires, budget a curated-path build then — per the ladder, that's roughly a week of curation effort plus a per-release re-order, not the standing cost a curriculum or badge would carry.

## Measurement plan

No course exists, so measure the actual fixes on the same four levels instead of course metrics:

- **Reaction:** informal feedback from the one workshop's attendees only — not scaled into a program metric.
- **Learning:** not applicable — nothing to assess.
- **Behavior:** ticket volume in the two named clusters ("which endpoint for settlement batches," "expired token / 400"), tracked weekly after each fix ships. Target (self-set): both clusters down ≥50% within one quarter of shipping.
- **Results:** (a) total support ticket volume normalized per active API consumer, not raw count — this is what actually tells you whether the 3x is real; (b) signup-to-first-successful-call rate, current baseline 38% (100% − 62%), target to be set by whoever owns the quickstart fix once they've diagnosed exactly where in the funnel developers drop.
- **Identity join:** ticket category → endpoint/error type; signup ID → first-call timestamp in gateway logs. Both look like they already exist, since you can already report "62%" and "which endpoint" as clean numbers — confirm the plumbing before relying on it for the quarter-out review.

## Kill rule (stay-closed rule)

No program exists to kill, so the rule gates *re-opening* instead: do not start a curated path or anything above it unless, at the review date, either the two ticket clusters are still above the −50% target or two-plus new customers have separately asked for training in one quarter. Review date: 13 weeks after the docs/error-message/quickstart fixes ship (set the exact date once those ship dates are known).

## First 90 days

- **Weeks 1–2:** confirm the ticket-tagging and signup-funnel instrumentation actually support the joins above; normalize "3x in six months" per active API consumer before treating it as a competence signal.
- **Weeks 1–3:** docs team makes the settlement-batch endpoint independently findable — indexed in nav/search, cross-linked from related pages, not just page 4 of a linear reference.
- **Weeks 2–4:** platform engineering ships a distinguishable expired-token error (specific code, e.g. `token_expired`, with a link to the refresh flow) in place of the generic 400.
- **Weeks 3–6:** DevRel/growth rebuilds the first-call path (sandbox key, one-command first call) and instruments exactly where the 62% drop off — hand to `developer-quickstart-guide`.
- **Weeks 4–5:** deliver the one workshop for the customer that asked; publish the recording.
- **Week 13:** review date. Pull updated ticket-cluster volumes and activation rate; check both kill-rule conditions before considering anything further.

## Where each number came from

- "Support volume up 3x in six months" — given by Vantahold; **not yet normalized** against active-API-consumer growth, flagged above as needing verification before being read as a competence signal.
- "62% of new signups never complete a first successful API call" — given by Vantahold; used as-is as the activation baseline.
- "One customer's platform team asked... last month" — given by Vantahold; this count of 1 is what the "two or more" escalation-trigger threshold is compared against.
- "−50% ticket-cluster target," "two or more additional requests," "13-week review window," "6–8h workshop estimate" — this charter's own baselines, not sourced from any vendor or published benchmark. Adjust on your first quarter's real numbers.
- The evidence-gate categories used to route each ticket cluster ("users can't find an answer that exists," "users fail at first success," "users misuse an API that could refuse misuse," "one team asked once") — the `developer-education-strategy` skill's own framework, not a published industry standard.