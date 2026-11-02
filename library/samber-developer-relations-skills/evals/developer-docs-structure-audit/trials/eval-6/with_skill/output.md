# Docs structure audit — Halyard Grid, 2026-09-18

## Scope and evidence

No repository or live site was provided for this pass — Interview gate Q1 resolves to "neither," which the skill treats as the weakest evidence tier available. What follows is a desk audit built from the five named sections and the stated complaint, not a page-by-page inventory. Every scorecard row that needs file-level data (mode purity, word counts, orphans, staleness, ROT rate) is marked **insufficient evidence** below rather than guessed, and the findings are graded on the argument's strength against the skill's own rubric, not on fabricated analytics. Running `docs-inventory.py` against the real tree, plus pulling search/ticket signals, would upgrade this from a desk audit to a scored one — recommended before anyone starts moving pages.

One fact from the brief does gate the whole verdict and is not in question: "sold to utilities — six-month procurement, security review, the works" is the **team/enterprise adoption** profile, not self-serve individual-developer adoption. There is an evaluator and a signer behind every user, and neither of them will ever run the quickstart.

## Verdict

The instruction to cut architecture, security model, limits, cost model, and migration content to a paragraph each and fold them into quickstarts is not supported by the audit — it reproduces this skill's own named failure mode, "audience blindness: enterprise evaluator content judged as tutorial bloat." All five targeted sections are exactly the content the audience-weighting model calls mandatory for a buyer with an evaluator and a signer behind them, and the proposed fix would also re-create a mixing defect (procedure and narrative sharing one page) rather than remove one. The real complaint underneath — "developers want to copy-paste, not read essays" — is legitimate but points at a different, narrower gap: whether a standalone, single-path quickstart for the telemetry API actually exists and is prominent, which is a page to *add*, not a reason to gut the five pages named.

## Section ratings (CNCF TechDocs scale, inferred — confirm before citing externally)

| Section                              | Information architecture | New user content | Content maintainability | Content creation processes |
| ------------------------------------- | ------------------------- | ------------------ | -------------------------- | ----------------------------- |
| Getting started / quickstarts        | 2 (unconfirmed — presence/prominence of a copy-paste path is unverified) | 2 | — insufficient evidence | — insufficient evidence |
| Architecture & security explanation  | 3 (correctly-moded content by description) | n/a — not this section's job | — insufficient evidence | — insufficient evidence |
| Reference: rate & retention limits   | 3, provisionally — "published" suggests it already behaves as reference | n/a | — insufficient evidence | — insufficient evidence |
| Cost model                            | 2–3, unconfirmed whether it's pure explanation or has a usable rate table | n/a | — insufficient evidence | — insufficient evidence |
| Migration-from-SCADA                  | 2, unconfirmed whether a runnable cutover procedure exists alongside the narrative | n/a | — insufficient evidence | — insufficient evidence |

1 = not present · 2 = needs improvement · 3 = meets standards · 4 = meets/exceeds · 5 = exemplary. Ratings above 3 are provisional pending a real read of the pages.

## Scorecard

| Measure | Now | Target | Threshold source | Status |
| --- | --- | --- | --- | --- |
| Mode purity | insufficient evidence | ≥ 90% | agreed baseline | untested |
| Surface coverage | partial — see coverage matrix | 100% of top surfaces | agreed baseline | untested |
| Entry points (1 tutorial/quickstart per primary audience) | **unclear — this is the actual open question, not the theory pages** | present for both self-serve and enterprise audiences | Diátaxis | needs confirmation |
| Demand coverage | insufficient evidence (no search/ticket data supplied) | ≥ 90% | agreed baseline | untested |
| ROT rate | insufficient evidence | report only | ROT heuristic | untested |

## Coverage matrix (surfaces inferred from the product description — confirm against the real surface list)

| Surface | Tutorial | How-to | Reference | Explanation |
| --- | --- | --- | --- | --- |
| Telemetry ingestion API/SDK | **?** — existence/prominence unconfirmed, this is the row the complaint is actually about | ? | ? | — |
| Site/device onboarding | ? | ? | ? | Architecture overview (claimed) |
| Data export & alerting | ? | ? | ? | — |
| Security & compliance | — (not this row's job) | ? | **gap candidate** — no control/cert/data-flow reference described, only narrative | Security-model section (claimed) |
| Pricing & procurement | — | — | **gap candidate** — no rate-card style reference described | Cost model page (claimed) |
| Migration from legacy SCADA | — | **gap candidate** — no cutover runbook described, only narrative | — | Migration explainer (claimed) |

Read as a heat map: the explanation column is populated exactly where the audience-weighting model says it should be for a procurement-and-security-review buyer. The **reference** cells under Security and Migration, and the **tutorial/how-to** cell under the API row, are where a real gap might actually live — and none of those are fixed by shrinking the explanation column.

## Findings

**[must fix] The growth head's directive, as stated**
- Now: proposes reducing architecture, security-model, limits, cost-model, and migration content to a paragraph each and folding them into quickstarts, on the stated grounds that they are "theory."
- Reader impact: the reader who needs this content is not the self-serve developer copy-pasting a snippet — it's the security reviewer and the procurement signer who never touch the quickstart and who gate the six-month sale. Per this skill's audience-weighting rule, that reader profile requires *adding* explanation early (architecture, security model, limits, cost model, migration path) "because someone who will never run the quickstart has to approve the choice," and reference completeness "carries procurement weight; missing limits and compliance detail become sales blockers." Cutting exactly this list to a paragraph removes the material that shortens, not lengthens, a security review.
- Next action: do not execute the directive as scoped. Re-scope it to the narrower, real complaint below.

**[must fix] Executing the directive would re-create a mixing defect the skill exists to remove**
- Now: "push everything into quickstarts" means splicing explanation-mode content (architecture rationale, threat model, pricing logic, legacy-mapping concepts) into action-mode pages.
- Reader impact: this is the mirror image of the documented mixing symptom "steps interrupted by paragraphs of rationale," whose prescribed fix is to *pull the rationale out* into its own explanation page and leave one linked sentence — not the reverse. A developer running the quickstart would now wade through cost-model and SCADA-migration paragraphs to get to their first API call; the evaluator would find that content is buried inside a task-oriented page they were never going to open.
- Next action: keep quickstarts single-path and single-mode; link out to the explanation/reference pages instead of inlining them.

**[should fix] Security-model section may be pure narrative with no reference component**
- Now (unconfirmed — flagged as an inference, not a measured fact): the section is described only as "a security-model section," with no mention of a control list, certifications, data-flow diagram, or subprocessor list a security reviewer could cite directly in a questionnaire.
- Reader impact: if true, a reviewer mid-audit has to extract facts from prose instead of consulting a reference table — the reference-vs-explanation split this skill flags under "API page with long narrative before the signature." This is a real, separate defect from the growth head's diagnosis, and points the opposite direction: add reference, don't shrink the page.
- Next action: confirm with the docs owner whether a discrete controls/certifications reference page exists; if not, extract one from the narrative (write-missing-page effort, not a cut).

**[should fix] Migration-from-legacy-SCADA may lack an actionable cutover procedure**
- Now (unconfirmed — inference): described as an "explainer," which by the hard-cases guidance is explanation; the guide most utilities actually need during a live cutover is a how-to.
- Reader impact: a utility team executing a SCADA migration needs a branching, real-world procedure, not just conceptual mapping — the concept page is the wrong mode for the moment they're most anxious about.
- Next action: confirm whether a step-by-step cutover how-to exists alongside the concept page; if not, split one out (this is exactly the kind of gap most likely to show up as a recurring sales-engineering or support question, and worth promoting up the queue if it does).

**[worth noting → possible must-fix, needs confirmation] The actual complaint may be a missing or buried quickstart**
- Now (unconfirmed): "developers want to copy-paste, not read essays" is a real and legitimate signal about entry points, but it names no specific missing page.
- Reader impact: if there is no short, single-path, copy-pasteable "first telemetry reading in under 15 minutes" quickstart prominently linked from the landing page, that is the actual must-fix — an empty tutorial/quickstart cell for the primary self-serve surface. It is independent of whether the five enterprise-facing pages exist.
- Next action: confirm the quickstart exists and is discoverable in ≤2 clicks from the docs home. If it doesn't exist, write it. If it exists but is buried under the theory sections in navigation, that's a nav-order fix, not a content cut.

## Remediation queue

| # | Action | Page(s) | Mode outcome | Reader need fixed | Effort | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Confirm/promote a single-path ingestion quickstart to the top of the nav | new or existing quickstart | tutorial | self-serve developer gets a copy-paste first success without wading through theory | 1d if missing, 1h if just buried | growth head's own complaint — promoted above rank, it's the only part of the complaint with a concrete reader need behind it |
| 2 | Extract a security controls/certifications reference table from the security-model narrative, if none exists | security-model section | explanation + reference | reviewer gets a citable answer instead of prose-mining | 1d | inferred gap, confirm before executing |
| 3 | Split a cutover how-to out of the SCADA migration explainer, if none exists | migration page | explanation + how-to | a utility mid-cutover gets a procedure, not just a concept | 1d | inferred gap, confirm before executing |
| — | Cut architecture, security-model, limits, and cost-model pages to a paragraph each | all five named pages | would merge explanation/reference into action pages | **none identified — deleted from the queue** | n/a | this action fails the audience-weighting check for this specific buyer profile; do not ship it |

Card sort / tree test (Step 7) should run before any of rows 1–3 touch navigation, with both a self-serve-developer panel and a security/procurement panel — a single panel would re-introduce the same audience-blindness error at the validation stage that the growth head's memo made at the diagnosis stage.

## Not covered by this audit

- Whether the five pages are individually too long or badly written *within* their correct mode — that's a prose/ROT pass over the actual text, which needs file access.
- Whether the published rate and retention limits are accurate — accuracy is explicitly out of scope for a structure audit.
- Whether procurement cycles have actually lengthened or shortened — that's a CRM/sales-cycle correlation question, not a docs-structure one, and would be the strongest possible rebuttal or confirmation of the growth head's claim if the data exists.
- Docs search/AI findability — route to `docs-seo` / `ai-seo` if that's the next question.

## Inputs

- Available: a prose description of five sections and one directive, no repository, no site, no analytics, no support-ticket data.
- Missing, and needed before locking this queue: the real page tree (`docs-inventory.py ./docs --nav <config>`), search/zero-result queries, support-ticket clusters mentioning security review or SCADA migration, and confirmation of whether a prominent quickstart already exists.
- Every "confirm" and "unconfirmed — inference" flag above is a specific, answerable follow-up question, not a hedge — resolve those before any page is actually cut, split, or moved.