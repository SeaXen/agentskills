# Docs structure audit — Ferrite, 2026-09-25

## Evidence tier — read this before the ratings below

No repo, no tree, no SUMMARY.md pasted. Per skill's own evidence rule, that's below "titles only" — the weakest tier it defines. Everything below with **[predicted]** is pattern-matching on stated facts (mdBook, ~70 pages, contributor-written, no writer, 4k stars, CNCF sandbox in flight), not a page-by-page read. Findings with **[mechanical]** need zero new evidence — run them today. Treat **[predicted]** rows as hypotheses to confirm, not verdicts to act on blind.

One command unlocks the real audit:

```bash
python3 scripts/docs-inventory.py ./docs/src --nav docs/src/SUMMARY.md > inventory.tsv
```

(mdBook nav lives in `src/SUMMARY.md` — same slot GitBook uses, not in skill's platform table but same mechanism.) Paste `inventory.tsv` back and I turn this into real per-page findings instead of predictions.

## Say this out loud to the two part-timers first

Skill mandates flagging this for any no-writer project: **CNCF TechDocs assistance program and Google Season of Docs both give a free external docs analysis, implementation plan, and issues backlog.** With a sandbox application in flight and zero writer budget ever, apply to one of these before spending your own evening hours re-deriving what a paid reviewer would hand you free. Run this audit as the interim measure while you wait on that.

## Verdict

Real severity is unknown — no page-level evidence exists yet. What's knowable now: mdBook's default (flat `SUMMARY.md`, no content-type taxonomy, no CI validation) almost never survives 70 pages of contributor PRs without drift, and CNCF's own TUF calibration puts a no-writer project at mostly 1s and 2s on entry-point criteria as the realistic starting point, not an insult. Biggest predicted cost: a Rust developer evaluating an actor framework, or a CNCF reviewer skimming for maturity, hits no single confirmed entry path. Fix size, once confirmed, is likely mechanical (nav checks, CI lint, a few splits) — not a rewrite.

## Section ratings — CNCF TechDocs rubric

**[predicted, unvalidated]** — anchored to CNCF's 2024 TUF calibration, the sourced baseline for a serious no-writer project. Replace with real scores after inventory.

| Section | Info architecture | New user content | Content maintainability | Content creation processes |
|---|---|---|---|---|
| Project docs (end user) | 1–2 | 1–2 | 2–3 | 1 |
| Contributor docs | not scored this pass | — | — | — |

Scale: 1 not present, 2 needs improvement, 3 meets standards, 4 exceeds, 5 exemplary.

## Scorecard

Most measures need the tree. What's known now:

| Measure | Now | Target | Threshold source | Status |
|---|---|---|---|---|
| Mode purity | unknown | ≥90% | skill baseline | pending inventory |
| Surface coverage | unknown | 100% of top surfaces | skill baseline | pending inventory |
| Entry points (1 tutorial/quickstart per audience) | unknown | present | Diátaxis | **check this first** — single highest-leverage unknown |
| Orphans / dead nav entries | unknown | 0 | skill baseline | mdBook: run `mdbook build` in strict-link mode, or check `lychee` |
| Nav depth | unknown | ≤3 | skill baseline | mdBook `SUMMARY.md` — count indentation levels directly, 2 min job |
| Broken internal links | unknown | 0 | skill baseline | `lychee --include-fragments docs/` — one command, no repo access needed on your side |
| Thin sections (1-page nav groups) | unknown | 0 | skill baseline | visible in `SUMMARY.md` directly |
| CI content-type validation | **confirmed absent** | present | governance | mdBook has no native front-matter schema check — this is a real, confirmed gap, not a guess |

## Coverage matrix — inferred surfaces, confirm or correct

**[predicted]** surfaces for an actor framework. Rows you should replace with your real ones:

| Surface | Tutorial | How-to | Reference | Explanation |
|---|---|---|---|---|
| Actor model core (spawn, mailbox) | ? | ? | ? | ? |
| Supervision / fault tolerance | ? | ? | ? | ? |
| Async runtime integration | ? | ? | ? | ? |
| Testing actors | ? | ? | ? | ? |
| Distributed / clustering (if Ferrite has this) | ? | ? | ? | ? |
| Observability / tracing | ? | ? | ? | ? |
| Deployment / production | ? | ? | ? | ? |
| Migration between versions | ? | ? | ? | ? |
| API reference | usually not mdBook — check if you're pointing to docs.rs or duplicating it in-book | | | |

Empty **reference** cells on a surface users configure are the costliest gap — reviewer or new adopter falls back to reading source. Empty **tutorial** anywhere means no supported first path; you need exactly one per audience, not one per feature — don't let this table push you toward writing more than that.

## Findings

**[mechanical]** — do these today, zero page-content evidence needed:

```
[should fix] site-wide nav
- Now: unknown whether SUMMARY.md nav depth exceeds 3, or holds single-page sections.
- Reader impact: deep or thin nav makes a 70-page book feel bigger than it is; CNCF reviewers skim nav first.
- Next action: open docs/src/SUMMARY.md, count indent levels, count single-entry sections. 10 minutes.
```

```
[must fix] entry point unverified
- Now: unknown whether Ferrite has one confirmed tutorial/quickstart a brand-new Rust dev can run start to finish with no branching.
- Reader impact: no entry point strands every self-serve adopter and every CNCF reviewer's first 5 minutes.
- Next action: find the page that currently plays "getting started." Check it against tutorial acceptance criteria (one path, no config menu, ends at a working artifact). If it branches or teaches options mid-walkthrough, it's a how-to wearing a tutorial's title — flag for split.
```

```
[should fix] API reference duplication risk
- Now: unknown whether the 70 mdBook pages duplicate what cargo doc / docs.rs already generates.
- Reader impact: two sources of truth for the same API drift apart; readers hit whichever is stale.
- Next action: grep mdBook pages for anything that looks like a hand-maintained method/struct list. If found, replace with a link to docs.rs, keep mdBook for how-to and explanation only.
```

**[predicted]** — high base-rate pattern for this archetype, confirm before acting:

```
[should fix] concepts-page mixing (predicted)
- Now: actor-framework docs commonly hold a "Concepts" or "Actors" page that mixes the mental model (explanation) with a setup/spawn walkthrough (how-to).
- Reader impact: someone mid-task rotating through a supervision failure scrolls past architecture prose; someone learning the model hits procedure noise.
- Next action: open whichever page explains the actor model. If it ends in numbered steps, extract those into a separate how-to.
```

Severity tiers (skill's definitions, verbatim): **Must fix** — a reader with a common need cannot succeed. **Should fix** — need is met but expensively. **Worth noting** — hygiene (single-page nav sections, depth >3, stale pages, mismatched titles).

## Remediation queue — ranked for 2–3 people, evenings only, no writer ever

Given your resourcing, weight mechanical and governance work far above writing — it's one-time setup cost against permanent leverage, versus writing which recurs every release with no writer to carry it.

| # | Action | Effort | Payoff | Evidence needed |
|---|---|---|---|---|
| 1 | Run `lychee` link check, wire as GitHub Action on cron | ~1 evening | 0 broken links forever, not once | none |
| 2 | Add CODEOWNERS for `docs/` subtree | ~10 min | review no longer falls on whoever's online | none |
| 3 | Count SUMMARY.md nav depth + single-page sections | ~10 min | tells you if IA is already broken | none |
| 4 | Confirm one working tutorial/quickstart exists and is single-path | ~1 evening | closes the single highest-severity possible gap | none — direct read |
| 5 | Run `docs-inventory.py`, paste result back | ~15 min | unlocks real per-page audit, replaces every "predicted" row above | your tree |
| 6 (deferred) | Front-matter content-type + CI schema check | ~1 weekend, one-time | makes future drift a build failure instead of a 2-year-old audit finding | none, but do after #5 |
| 7 (deferred) | Splits / merges / missing pages | depends on #5 findings | — | inventory required — don't guess at this yet |

Deleted from queue: renames and moves involving URL changes — not listing redirect policy as answered, so I won't recommend anything that could break inbound links until you confirm you can ship redirects.

## Drift controls — this is the highest-leverage section for a team that will never hire a writer

- CI content-type check: mdBook has no native front-matter schema. Fake it with a small script asserting each page under `src/` declares a type comment or matches a naming convention, run in CI. One-time build, then free forever.
- `lychee` on a daily cron, opens an issue on failure — no human has to remember to check.
- CODEOWNERS per subtree — review load spreads instead of landing on one person.
- Redirect for every page you ever move.
- Re-audit quarterly, 90-day vs prior-90-day, so this doesn't depend on memory.

## Not covered by this audit

Prose accuracy, whether code samples still compile, SEO, contributor-docs rubric category (governance docs, "new contributor" content) — flag if you want those scored separately.

## Inputs

Repo: not provided. Live site: not provided. Tree: not provided. Everything above with **[predicted]** came from stated facts only (mdBook, ~70 pages, Rust actor framework, CNCF sandbox in flight, no writer) — this is the report's own honesty check, not a hedge.

**Next action:** run the `docs-inventory.py` command above against your `src/`, paste the TSV back. That converts every `?` and every **[predicted]** row into a real finding.