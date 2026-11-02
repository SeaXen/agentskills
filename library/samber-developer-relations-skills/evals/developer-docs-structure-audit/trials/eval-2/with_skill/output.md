# Docs structure audit — Northwind Telemetry, 2026-09-18

## Inputs (read this before the rest)

No repository, ditamap, live site, or analytics were available for this pass — this is a desk audit built from what you described: ~1,400 DITA topics in Oxygen, typed `concept`/`task`/`reference` and typed *rigorously* (confirmed fact, not inferred), plus one demand signal (support tickets — new customers dropped into task topics with no starting point). Everything below that rests on that signal is marked **confirmed**. Everything about your actual surface catalog, audience split, and per-topic mode purity is marked **inferred** or **needs inventory** — I'm not going to hand you invented numbers dressed up as an audit. Section 7 gives you the exact next step to turn this into a page-by-page pass.

Two assumptions I made to write this at all, flag if wrong: (1) audience is mixed self-serve + enterprise evaluators, typical for an observability/telemetry product — **inferred**, not asked; (2) the DITA project is version-controlled and Oxygen-published via DITA-OT or a similar toolchain — **inferred** from "DITA setup in Oxygen."

## Verdict

Northwind Telemetry's docs are typed correctly and consistently against DITA's three base types across ~1,400 topics — that rigor is a real asset, not the problem. Diátaxis needs four quadrants and DITA's type system only ever asked for three; the missing one, tutorial, has no DITA equivalent by design, so it is a genuine structural gap, not a mapping artefact. The support pattern is the direct, mechanical symptom of that gap — a `task` topic assumes competence and branches on real-world variables, so a new customer routed straight into one is being handed a how-to when what they need is a managed, linear, guaranteed-success first win. Closing it does not require re-typing 1,400 topics: it requires a small set of net-new tutorial topics per primary audience, a reclassification pass on `concept` topics (some are explanation, some are secretly reference), and a publish-time layer that projects the existing DITA typing into a four-quadrant nav — not a rewrite of the authoring schema underneath it.

**Push back on "everything migrated," specifically.** A full re-type of 1,400 XML topics against a 4th generic type is the retyping cost Paligo documents teams losing months to before abandoning it for "basic topic types with writing guidelines" — and it is the "rewrite the docs site" move Diátaxis itself calls an abdication, not a recommendation. What the VP actually wants (readers landing in the right mode) is achievable this year without that project. What follows is the version that ships.

## DITA → Diátaxis crosswalk ("what moves where")

This is the core deliverable — the rule set a writer applies per topic, not a one-time label swap.

| DITA type | Default Diátaxis mode | When it's actually something else | Tie-breaker |
|---|---|---|---|
| `concept` | **Explanation** | If its dominant content mirrors product shape (a `<simpletable>`/`<table>` of parameters, one section per setting) and is referenced from a task's `<postreq>` or `<related-links>` as a lookup → **reference** instead. This is a common DITA drift: parameter tables accrete inside "concept" because there was nowhere typed for them to go. | Would a reader open this *while working* (reference) or *away from the keyboard* (explanation)? |
| `task` | **How-to** | Almost never a tutorial as-is, and that's correct — don't force it. A task only qualifies as tutorial-shaped if it has one linear path (no `<choicetable>`, no conditional branching), assumes nothing beyond "has an account," and ends at one working artefact. Existing tasks were written to branch on real-world variables — that's the how-to acceptance criterion working as intended. | Does the page promise *learning* or a *finished task* for someone already competent? |
| `reference` | **Reference** | Near 1:1 — the closest mapping of the three, since DITA `reference` ("mirrors the shape of the product," "one section per command/parameter") already satisfies Diátaxis reference's acceptance criteria almost exactly. Watch only for reference topics that grew a narrative preamble; cut it to one sentence and link the concept/explanation topic. | — |
| *(none)* | **Tutorial** | DITA has no base type for this. It is the one quadrant nothing in your set could have been correctly typed into, no matter how rigorous the writer was. | — |

The important nuance for the VP: **strict DITA typing does not guarantee Diátaxis mode purity.** A topic can be a perfectly rigorous, unmixed DITA `concept` and still be internally mixing explanation and reference, because DITA's rigor was enforced against DITA's own three-way schema, never against a four-way reader-need split. "The typing was strict" and "the mode is pure" are different claims — this audit's mode-purity finding (below) tests the second one.

## The tutorial gap — how to close it without a schema rewrite

1. **Don't specialize a new DTD-level `tutorial` topic type.** This is the exact trap Paligo documents: a team spent months debating a new topic type for troubleshooting content, dropped it, and got the same result from plain topics plus writing guidelines. A tutorial is structurally still step-shaped — keep it as `<task>` at the schema level.
2. **Flag mode in metadata instead.** Add `<prolog><metadata><othermeta name="diataxis-mode" value="tutorial"/>` (or reuse `audience`/`otherprops`, both already conditional-processing idioms in DITA) to every topic that is tutorial-mode. This is the DITA-native equivalent of Microsoft Learn's `ms.topic` front-matter declaration — machine-checkable, not tribal knowledge.
3. **Enforce the shape at authoring time.** Write an Oxygen Schematron rule that rejects `<choicetable>`, branching `<steps-unordered>`, or more than one `<steps>` block inside any topic flagged `diataxis-mode="tutorial"`. This is your CI-equivalent governance layer, native to the DITA-OT/Oxygen toolchain — don't reach for Vale or markdownlint, wrong stack.
4. **Assemble tutorial topics into their own ditamap(s)**, one per primary audience, published as its own top-level nav entry distinct from the existing task/how-to collection. One tutorial per primary audience is usually enough — not one per feature; resist the urge to write a tutorial per surface.
5. **Write the tutorial content net-new.** Don't strip branches out of an existing task topic to force it into tutorial shape — that breaks the how-to for the competent readers who currently rely on it.

## Findings

**[must fix] Onboarding — no tutorial-mode entry point exists**
- Now: 1,400 topics span `concept`/`task`/`reference`; none is typed or shaped as a contrived, single-path, guaranteed-success walkthrough. New customers are routed to `task` topics, which by design assume competence and branch on real-world variables.
- Reader impact: someone with zero context hits a page that forks on options they can't yet evaluate, and gets no promised, linear first win. This is a repeat support pattern, not a one-off complaint.
- Next action: write one tutorial (per primary audience, pending confirmation of audience split) to first success, assembled in its own ditamap, wired into the top-level nav as a distinct entry point from "Guides."
- Evidence: support ticket pattern (confirmed, as reported).

**[should fix — hypothesis, unverified] `concept` topics likely mixing explanation and reference**
- Now: DITA `concept` has no separate home for parameter/settings tables, so they commonly accrete inside concept topics rather than being split out. Not yet confirmed against your actual topics.
- Reader impact, if confirmed: an evaluator reading for architecture understanding wades through a settings table; someone mid-configuration scrolls past narrative to find the one field they need.
- Next action: run the inventory pass below on `concept`-typed topics specifically, filtering for topics containing `<simpletable>`/`<table>` elements — that's your candidate list, not a confirmed finding yet.
- Evidence: structural inference from DITA's type system, not yet inventoried. Label as inference until checked.

**[worth noting — credit where due]** `reference` topics are the one bucket expected to need the least rework — DITA's `reference` type already matches Diátaxis reference almost exactly. Don't spend queue budget re-auditing this bucket first; it's the cleanest one by construction.

## Remediation queue

Ordered by reader need fixed per hour, per the skill's own ranking (split > merge > move > write-missing-page > rename on efficiency) — with the tutorial gap promoted above its normal rank because it sits on the adoption path and the same complaint recurs in support.

| # | Action | Scope | Mode outcome | Reader need fixed | Effort | Evidence |
|---|---|---|---|---|---|---|
| 1 | Write tutorial entry point(s), new ditamap, new nav entry | Onboarding path | tutorial | new customers get a promised first win instead of a how-to | ~1 week + refresh per release — **promoted above rank**, adoption-path + recurring support signal | confirmed support pattern |
| 2 | Add `diataxis-mode` prolog metadata + Schematron guard | All topics, incremental | n/a (governance) | mode stays machine-checkable, doesn't decay after this audit | 1–2 days, one-time | governance requirement, not optional |
| 3 | Inventory `concept` topics for embedded parameter tables | ~1,400 topics, filtered | concept → explanation + reference candidates | reclassification list to split from, once confirmed | half-day to run, ongoing to action | see Step 7 below |
| 4 | Split confirmed mixed `concept` topics | per confirmed hit from #3 | explanation + reference | evaluator and mid-task readers stop meeting each other's content | a day per topic, both halves rewritten | pending #3 |
| 5 | Full re-inventory once ditamap access is granted, re-score | whole set | — | converts every "needs inventory" cell above into a real number | half-day to run, ongoing to maintain | this audit's own gap |

**Deleted, not deferred:** a full re-type of all 1,400 topics to Diátaxis's four labels at the schema level. That's the teardown Diátaxis explicitly warns against, and the specialization-debate cost Paligo already watched a team lose months to for one new type. If the VP's mandate is genuinely "the XML types must say tutorial/how-to/reference/explanation," say so back to them as a scoping question — it changes #2 from a metadata flag to a schema migration, and changes effort by an order of magnitude.

## Scorecard

| Measure | Now | Target | Threshold source | Status |
|---|---|---|---|---|
| Entry points (tutorial per primary audience) | 0 | present | Diátaxis — missing quadrant strands a class of visitor | **fail — confirmed** |
| Mode purity | unknown | ≥ 90% | agreed baseline | needs inventory (run script against ditamap) |
| Surface coverage | unknown | 100% of top surfaces | agreed baseline | needs your real surface list |
| Orphans / dead nav / broken links | unknown | 0 each | agreed baseline | needs ditamap + build log |
| ROT rate | unknown | report, no target | standard content-audit heuristic | needs inventory |

## Section ratings (CNCF TechDocs, 1–5)

| Section | Information architecture | New user content | Content maintainability | Content creation processes |
|---|---|---|---|---|
| Whole set | 3 (DITA typing rigor is real IA) | **1 — confirmed** | not rated, insufficient evidence | not rated, insufficient evidence |

Rating everything else here would be exactly the "silent inference" failure mode this skill's own doc warns against — a rubric filled from vibes isn't a rubric.

## Coverage matrix (illustrative — confirm the surface list)

Rows below are inferred from "telemetry product," not your real catalog — replace before acting on it.

| Surface (inferred) | Tutorial | How-to | Reference | Explanation |
|---|---|---|---|---|
| Onboarding / first success | **missing — confirmed** | — | — | — |
| Agents / SDKs per language | ? | likely (task) | likely (reference) | ? |
| Dashboards & alerting | ? | likely (task) | likely (reference) | ? |
| Self-hosting / deployment | ? | ? | likely (reference) | ? |
| Query language / API | ? | ? | likely (reference) | ? |

## Not covered by this audit

- Per-topic mode classification of the actual 1,400 topics — needs the ditamap.
- Accuracy of any topic against current product behavior — separate concern, owner: engineering + writer.
- Prose quality, terminology consistency across topics — separate concern.
- Validation of the proposed structure against real users (card sort / tree test) — not run; every structural recommendation above is **proposed**, not validated. Recommend a tree test on "keep DITA typing, add Diátaxis metadata layer" before greenlighting the full nav change.

## Next step to finish this for real

1. Point me at the ditamap (or grant repo/Oxygen project access).
2. Confirm audience split (self-serve / enterprise / both) — reweights how much explanation content matters.
3. Confirm your real surface catalog (replaces the illustrative matrix above).
4. I run `docs-inventory.py`-equivalent logic against the actual topic set, filtering `concept` topics for embedded tables (finding #2) and scoring the full scorecard with real numbers.

That converts this from a structural diagnosis into the page-by-page queue — the diagnosis and the fix shape don't change; only the row count does.