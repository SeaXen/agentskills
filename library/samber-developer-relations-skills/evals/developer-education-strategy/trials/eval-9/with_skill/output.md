## Direct answer

Reject both asks as framed. Neither is an education problem — they're demand-gen and credibility tactics wearing an education costume, and that mismatch is exactly what feels off.

- **Evidence gate fails.** Nothing in your situation matches what justifies structured education: no time-to-competence data, no deals blocked on trained staff (no sales team to block), no dominant misconception in support/community, no hiring-market demand for "Fernlow skills." The actual asks — capture emails, get a LinkedIn-shareable badge — aren't on that list. They're growth and social-proof goals routed through the education team because docs are the only asset marketing can point at.
- **The signup wall breaks the thing that's working.** Your entire adoption motion is 40,000 monthly organic docs visitors finding answers and adopting bottom-up. There's no sales team to hand captured emails to, so the wall trades a working top-of-funnel for a list nobody will work. This is the skill's own named failure mode: *"gating what used to be open docs collapses top-of-funnel reach."*
- **The certification has no consumer.** A credential is only worth building when someone outside your team acts on it — a buyer, a partner contract, a hiring manager screening for it. You have none: no enterprise buyer counting certified heads, no partner/SI contract requiring badged staff, and no evidence any hiring manager screens for "Fernlow Certified." Build it anyway and you own a permanent liability (cut-score defense, disputes queue, recertification) for a badge that changes nobody's behavior. That's certification theater.

What's actually justified, on the evidence you gave: a **curated learning path** — sequence the tutorials/docs you already have into an ordered "where do I start" path, still fully public, no login. That's the one rung that returns value without any of the obligations marketing's version would create.

I don't have real data behind most of the numbers below (no interviews, no support-ticket export, no analytics pull) — I've built the charter to the shape the evidence gate requires and flagged every number as an invented baseline you replace once you pull real numbers. Treat this as a first pass to react to, not a final plan.

---

# Developer education charter — Fernlow, 2026 H2

## 1. Gate verdict
Education is **not justified** for the stated problems. Capturing emails and shipping a certification are demand-generation and credibility asks, not evidence of a competence gap — there's no cited time-to-competence problem, no blocked deal, no recurring conceptual misunderstanding in support or community channels, and no hiring-market demand for a Fernlow-specific skill. Rejected cheaper/correct alternatives: a signup wall is a distribution decision, not an education one — it belongs nowhere on this ladder — and a certification with no external consumer is not "cheaper," it's simply unjustified at any price. The one thing evidence *does* support — you have enough existing tutorials that a first-time user has no obvious "start here" — justifies the lowest rung only.

## 2. Audience and motion
Individual developers adopting bottom-up. No enterprise motion, no partner/SI motion, no student motion mentioned. This matters because the audience rule for bottom-up adoption is the opposite of what marketing proposed: *"free, public, shareable and low-friction beats rigorous... a login wall suppresses the exact funnel this motion lives on."*

## 3. Chosen tier
**Rung 1 — curated learning path.** Sequence existing docs/tutorials into one ordered path (e.g., first migration → rollback → schema drift → CI integration → multi-database), still open, no signup.

Rejected:
- **Ad-hoc content (current state)** — you're already here; nothing accumulates, and it's why "no obvious start" is the actual pain, not the trigger for anything bigger.
- **Curriculum with labs** — no job-task analysis, no named capacity for a standing lab-maintenance role, no evidence reading-then-doing is the gap (vs. simply not knowing where to start).
- **Badge** — no named external consumer.
- **Certification** — no named external consumer, no funded standard-setting study, no funded recertification cycle. All three refusal conditions from the certification reference are unmet simultaneously, which is a clean reject, not a close call.

Escalation trigger to rung 2 (curriculum with labs): learners finish the curated path and still can't complete a real migration unassisted — i.e., reading the sequence isn't producing competence. Escalation trigger to badge/certification: Fernlow signs its first enterprise or partner/SI contract, **and** that contract or an RFP explicitly asks for named trained or certified staff, twice within one quarter. Until both trigger conditions exist, badge and certification stay off the list entirely rather than parked as "later."

## 4. Competency map
No job task analysis has been run. Provisional task sequence, ordered by what a migration tool user actually does in order (replace with real interview/support data before treating this as final):
1. Write and run a first migration.
2. Roll back a migration safely.
3. Resolve a schema-drift conflict.
4. Wire migrations into CI.
5. Run migrations across multiple environments/databases.

Each existing tutorial/doc page maps to one of these; anything that doesn't map either gets cut from the path (stays as reference docs, just not in the sequence) or flags a real content gap to fill. No labs, no assessment — the path is navigation, not a curriculum.

## 5. Credential decision
**No credential.** No named external consumer: no buyer, no partner contract, no hiring manager confirmed to screen for it, no community request cited. If marketing wants a shareable, LinkedIn-able artifact, that want is legitimate but this isn't how to fund it cheaply — revisit only when the escalation trigger in section 3 fires.

## 6. Operating model
- **Owner**: whoever already owns the docs site today, named individually, not "the DevRel team."
- **Staffing**: ~1 week one-time to curate and sequence; ~1–2 hours/week ongoing to re-order after releases. No new hire, no standing lab role — there's no lab.
- **Platform**: docs-native. No LMS, no hosted lab platform, no new vendor.
- **Refresh trigger**: re-order within one release cycle of any change to the CLI's migration workflow (new subcommand, changed flag, changed default behavior).
- **Pricing**: free, public, no login — non-negotiable given the audience.
- **Localization**: defer until one locale shows demand.
- **Partner delivery**: none — no partners today.

## 7. Budget shape
Year one: docs-owner time only (~1 week build), zero new tooling spend. Year two recurring: ~1–2 hours/week. If this can't be staffed even at that size, don't start it — but it's small enough that it should clear easily.

## 8. Measurement plan
- **Reaction**: drop-off point in the sequence (page analytics, anonymous — no login needed). Own baseline target: no single step loses more than 25% of path viewers; adjust after cohort one.
- **Learning**: not measured this year — no assessment exists at this rung, and building one would be curriculum-rung scope, not curated-path scope.
- **Behavior**: proxy only, since there's no login to join identity to usage — track whether "how do I get started" / "where do I begin" questions in support or community channels drop after launch. Name this explicitly as a proxy, not a real identity-joined behavior metric.
- **Results**: not measured this year. No sales motion exists to move, and claiming any without a sales motion would be inventing an outcome. Revisit if/when an enterprise or partner motion exists.

## 9. Kill rule
If "where do I start" questions in support/community show no measurable drop two releases after launch, retire the path as a distinct artifact, keep the underlying doc pages as they are, and don't re-propose without new evidence.

## 10. First 90 days
- Weeks 1–2: inventory existing tutorials/docs, map each to the provisional task list in section 4.
- Weeks 3–4: sequence into one ordered, public path; no new content authored, only re-ordering and "next step" links.
- Weeks 5–6: ship it on the docs site.
- Weeks 7–12: watch drop-off, re-order the weakest step, recheck support-channel "where do I start" volume.

## 11. Where each number came from
- 40,000 monthly docs visitors — you provided this; treat as sourced from your own analytics, dated 2026-09-20.
- 25% single-step drop-off target, "1–2 hours/week" maintenance, "one release cycle" refresh window, the two-release kill-rule window — all this charter's own invented baselines, not benchmarks; replace with your own numbers after cohort one.
- Everything under "certification" and "badge" that's absent from this charter (cut-score method, recertification funding, Open Badges format) is absent on purpose: there's no credential being built, so none of that machinery is being spun up.

---

Two things worth doing separately, outside this charter, if the underlying wants are real:
- If marketing wants emails, propose a narrow opt-in (e.g., release-notes subscription) that never blocks the existing free docs — and ask marketing directly who works those emails, since "capture" with no one to action them is a vanity metric.
- If marketing wants a shareable "I use Fernlow" artifact, a public show-and-tell / case-study wall costs nothing recurring and doesn't require defending a cut score to anyone.