Skipped the interview — you asked for the deliverable directly. Substituted these for interview answers: product = embedded SDK (company adoption exists), funded driver = revenue (per-seat pricing), evidence = your two numbers, both first-party. Flagging that assumption up front since it drives the whole ranking.

# Developer segment map — Byrnewood Analytics charting SDK, H2 2026

## Cut

Dimensions: **buying mode** (purchase exists vs not, who signs) × **licence channel** (direct self-serve vs institutionally-mediated enrollment).

Rejected:
- Seniority — a junior and a staff product engineer integrating the same chart component need the same SDK docs.
- Technographic (framework/language) — likely relevant for a charting SDK (React vs Python vs mobile bindings usually mean separate docs tracks), but no framework-level data exists yet. Parked, not rejected: instrument this next, it may outrank the current cut once you have it.
- **Raw population size as a ranking axis.** This is the one marketing is implicitly using. 40,000 vs 900 is a symptom of the buying-mode split, not an independent dimension — scoring segments by headcount alone is what this map corrects.

Company shape: developer-first (B2D) — the evaluator is usually inside the buying group for small accounts.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| Paying product teams | Teams licensing the SDK per seat to embed charts in a commercial product | 900 seats, exact — internal billing records, as of 2026-09-19; seats-per-account distribution unknown | Developer evaluates; eng/product lead approves and signs for small accounts; whether larger accounts trigger procurement is unmeasured | Production-grade docs, framework-specific samples, renewal/licence management | Existing sales pipeline, product-eng communities | 900 billing records — measured |
| Individual students & bootcamp learners | Individuals self-serving the free educational licence while enrolled in a program | ~40,000, exact — internal free-tier activation records, as of 2026-09-19 | Individual adoption, no purchase — learner self-activates | Quickstart, learning-oriented samples — already built | Course/bootcamp assignments, student dev communities | 40,000 activations — measured |
| Bootcamp & university program leads (hypothesis) | Instructors/curriculum directors who place the SDK on a syllabus, driving cohort-wide signups | ~150–1,300 distinct programs, inferred — 40,000 ÷ assumed 30–300 learners/cohort, wide range, unverified | No purchase; champion role deciding curriculum placement, not a buyer | Curriculum kit, instructor portal, bulk enrollment — none built yet | CS/data-viz course networks, bootcamp partner programs | 0 data points — hypothesis, below evidence floor |
| Non-qualifying "educational" licence users (anti-segment) | Free-tier accounts showing production/commercial usage instead of coursework — avoiding the $1,200/seat fee | Unknown share of the 40,000 — no audit run | Same self-serve channel as students, indistinguishable without audit | None — this is leakage to close, not a segment to serve | Same signup flow as students | 0 — unaudited, flagged risk |

## Primary

Paying product teams. Score (driver = revenue): size 2, reachability 3, fit 3, value 3, effort 1, competitive position 2, compounding 2. Effort near-zero (sales motion, SDK, billing already built) against 100% of current ARR (~$1.08M at 900×$1,200). Wins on value per effort, not on headcount.

## Secondary

Individual students & bootcamp learners. Served only by artefacts the primary already funds — existing free-tier quickstart and docs, nothing new built. Justified solely as a future-buyer and talent-brand pipeline, not as revenue. Capped: no dedicated headline campaign, no roadmap commitment this horizon.

## Anti-segment

Non-qualifying "educational" licence users. Reachable through the same flow as legitimate students, but not to be served — it's paying-segment revenue hiding inside the free tier. This is likely part of why 40,000 "looks great": headline it before auditing and you may be publicizing your own fee leakage.

## Hypotheses

Bootcamp & university program leads: 0 data points, below floor.
- Test 1: cluster the 40,000 free-tier records by email/institution domain — sizes the real program count.
- Test 2: interview 5 program leads on why they did or didn't put the SDK in a course.
- Drop if activations turn out mostly independent, not cohort-driven — concentration is the whole case for this segment.

## Implications

- **Build:** nothing new for primary or secondary this horizon — both run on existing infrastructure.
- **Test:** audit a sample of free-tier accounts for production-traffic signals, non-institutional domains, licence age vs. typical course length (anti-segment sizing).
- **Test:** domain-cluster the 40,000 before funding any curriculum kit or partnership outreach (hypothesis segment).
- **Stop:** do not headline "40,000 students" as an equal-billing segment, or commit marketing/roadmap spend to it, until the audit lands.

## Review

Re-read 2026-12-19. Early re-read if: the free-tier audit finds material leakage, domain-clustering shows real program concentration, seat-concentration analysis on the 900 finds a procurement threshold, or licensing terms change.

## Quality gate

- 4 segments (3–5 target) ✓
- Each differs from siblings on artefact/channel/proof ✓
- Sizes carry method + date + confidence. Deviation: primary and secondary use exact counts, not ranges — stronger than an estimate since both are direct database counts, not modelled ✓
- Decision unit named or "no purchase" stated for all four ✓
- Funded segments (primary, secondary) both measured, both clear the evidence floor ✓
- Anti-segment named, non-empty, is the exact population marketing wanted headlined ✓
- Review date named ✓

Next: run the free-tier audit — that number gates whether the student segment should even stay at secondary.