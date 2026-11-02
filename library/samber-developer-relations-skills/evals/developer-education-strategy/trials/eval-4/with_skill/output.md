Following `developer-education-strategy`. One thing up front: I didn't write lesson breakdowns for the eight modules as drafted, because that list is the exact "feature-tour curriculum" failure mode this skill exists to catch — every module mirrors a nav item, not a job a learner does. Two of the eight ("Billing and plans," "Settings and preferences") aren't skills anyone practices; they're one-off admin lookups. Writing lesson content for those first would waste your writer's week on modules likely to get cut later.

I couldn't run the skill's real interview (this is a single-shot answer), so I made the calls explicit below as assumptions, not facts. Confirm or correct them before your writer starts — everything downstream depends on them.

**Assumptions standing in for the interview (confirm these):**
- Learner = a self-serve/bottom-up user of Perigee (data analyst, data engineer, or team admin), not an enterprise buyer's staff or a reselling partner. If it's actually enterprise or partner-driven, the tier and credential recommendation below change.
- No evidence yet cited for a competence gap (no support-ticket clusters, no blocked deals, no "same question keeps coming up" pattern) — the module list came from the product nav, not from users failing at a task.
- No named external consumer (buyer, partner contract, hiring manager) is asking for a credential.
- Capacity: unknown. Treated as "whoever writes docs/content today," not a dedicated new hire, until told otherwise.

---

# Developer education charter — Perigee Academy (draft, pending confirmation)

## 1. Gate verdict
Fails as posed. The module list mirrors the product's left-nav, not a documented competence gap, and no evidence (tickets, blocked deals, telemetry, repeated questions) has been cited. Cheaper alternative rejected for the two admin-only items: docs information architecture and in-app tooltips, not curriculum — nobody needs a "lesson" on where the billing page is.

## 2. Audience and motion
Assumed: individual/bottom-up users of a self-serve data catalog (analysts, data engineers, team admins setting up Perigee for their team). **Unconfirmed — the single biggest variable.** If the real driver is enterprise deals stalling on "is our team trained" or partners implementing Perigee badly for clients, say so and the whole recommendation shifts toward rung 3+ with a badge.

## 3. Chosen tier
**Curated learning path (rung 1).** Rejected: structured curriculum with labs — no evidence yet that reading a sequenced path is insufficient (that's the escalation trigger, not a starting assumption); badge/certification — no named external consumer. Escalation trigger to rung 2: learners finish the path and still can't complete the task unassisted (e.g., webhook-setup tickets don't drop after launch).

## 4. Competency map
Job tasks were not analyzed from interviews/tickets/telemetry — they're inferred from what the product lets someone do. Treat this as a starting hypothesis for your first real job-task pass, not a finished analysis.

Reframed from 8 nav items → 6 task-based modules + 2 items moved out of curriculum entirely:

**Module 1 — Find and trust a dataset**
*(absorbs "Dashboard overview" as the entry point, not its own topic)*
- Objective: search and filter the catalog by owner, domain, tags.
- Objective: read a dataset's lineage to trace its upstream source.
- Objective: interpret freshness/quality signals before relying on a dataset.
- Evidence: given a dataset page, decide "safe to use for X or not," and justify why.

**Module 2 — Set up a workspace for your team**
*(was "Projects and workspaces")*
- Objective: create a project/workspace and structure ownership.
- Objective: assign roles and decide what's shared vs. private.
- Evidence: stand up a workspace with two roles correctly scoped.

**Module 3 — Connect Perigee to your stack**
*(was "Integrations directory," plus the inbound half of "Webhooks")*
- Objective: pick the right connector for a common source.
- Objective: configure and verify a sync; diagnose a failed connection.
- Evidence: connect one sandbox source end-to-end.

**Module 4 — Automate on catalog events**
*(was "Webhooks," outbound half only)*
- Objective: register a webhook against a trigger (schema change, new PII tag, dataset deprecated).
- Objective: verify delivery and handle a failed delivery.
- Evidence: wire one working recipe (e.g., Slack alert on schema drift).

**Module 5 — Manage programmatic access safely**
*(was "API keys")*
- Objective: create a scoped key following least privilege.
- Objective: rotate and revoke a key.
- Evidence: scenario check — a key leaked in a public repo, what do you do and in what order.

**Module 6 — Investigate and prove governance**
*(was "Audit logs")*
- Objective: use the audit log to answer "who changed/deleted this."
- Objective: export a log slice for a compliance review.
- Evidence: given a mock incident, find the responsible change.

**Moved out of curriculum — not modules:**
- "Billing and plans" → help-center article + in-app tooltip. Pull back into curriculum only if you get evidence of a real competence gap (e.g., admins mismanaging seats causing invoice disputes) — that's the one thing that would justify a module here.
- "Settings and preferences" → same treatment. No repeatable task to practice, just a reference lookup.

Pass check: every module above now traces to a task a learner does repeatedly, not a screen they visit once. Confirm this against real interviews/tickets before your writer locks the outline — right now it's my inference, not sourced evidence.

## 5. Credential decision
None. No named external consumer (buyer, partner, hiring manager) has asked for one. Revisit if that changes.

## 6. Operating model
- **Owner**: not yet named — needs one person accountable for curriculum truth, not a team label.
- **Staffing**: PROPOSED, unconfirmed — curation/authoring ~6–8h/week for six short modules, technical review from product ~1–2h/week, learner support folded into existing support queue at this tier (no lab platform needed).
- **Platform**: docs-native learning path (sequenced pages on your existing docs site), not a new LMS — matches rung 1's minimal footprint.
- **Refresh trigger**: re-check each module within 4 weeks of any release that changes the flow it documents (nav changes, new connector types, key-scoping changes).
- **Pricing**: free, ungated — this tier is reach, not revenue.
- **Localization**: defer until one locale shows demand.
- **Partner delivery**: none at this tier.

## 7. Budget shape
Year one: ~40–50 person-hours to write and sequence six modules (PROPOSED estimate, not measured — validate against your writer's actual pace on module 1 before committing to the rest). Year two recurring: light, dominated by per-release re-checks, no lab maintenance at this tier.

## 8. Measurement plan
- Reaction: path completion rate.
- Learning: single end-of-module scenario check (as listed per module above), pass/fail.
- Behavior: feature adoption among path-finishers vs. matched non-finishers — e.g., % who create a webhook or scoped API key within 30 days of finishing the relevant module.
- Results: time-to-first-production-use (days from signup to first published workspace/dataset).
- Identity join: learner account ID → product usage events. Confirm this plumbing exists before launch — it can't be added retroactively for cohort one.
- Not measured this year: revenue/renewal attribution — no counterfactual at this scale yet.

## 9. Kill rule
If path completion stays under [PROPOSED: 20%] for two consecutive quarters, or the behavior metric shows no difference between finishers and matched non-finishers after two cohorts, retire the path, keep the six pages as reference docs, and reopen the gate with real evidence before trying again.

## 10. First 90 days
- Week 1: confirm the assumptions flagged above (audience, evidence, capacity) with whoever asked for this.
- Weeks 1–2: light job-task check — pull 20–30 real support tickets or onboarding-call notes to test the 6-module hypothesis above; adjust before writing starts.
- Weeks 2–3: writer drafts Module 1 and 2 only; ship and watch completion/drop-off before committing to the rest.
- Weeks 4–8: writer drafts Modules 3–6 using the same objective/evidence pattern.
- Week 9: baseline metrics captured for cohort one; billing/settings docs handed to whoever owns help-center content, off this curriculum.

## 11. Where each number came from
- 6-module reframing, module cuts, tier choice: this charter's own reasoning — not sourced, needs validation against real job-task evidence.
- 40–50h build estimate, 20% completion kill threshold, staffing hours: this skill's own baseline pattern, values invented for this draft — treat as placeholders to replace with your first real numbers, not targets.
- Four-level measurement framework (reaction/learning/behavior/results): Kirkpatrick, sourced from the skill's own reference material.
- Everything under "Assumptions" at the top: unconfirmed, supplied by me in absence of interview answers.

---

**Self-review against the skill's scorecard**: passes on gate verdict, tier ordering with rejected rungs, competency traceability, and kill rule. Fails, honestly, on items tied to real evidence — job-task analysis (built from inference, not interviews/tickets), named owner with hours (placeholder), and sourced numbers (mostly self-set placeholders). Those gaps are exactly what week-1 above is for.

Once you confirm the assumptions and the reframed module list, the actual lesson-by-lesson copy for your writer is a separate step (`developer-tutorial` skill, one invocation per module) — this charter is the input to that, not a substitute for it.