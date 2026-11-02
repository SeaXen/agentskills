**Do first: run `samber/developer-relations-skills@oss-contributor-onboarding` on Copperline.** No `CONTRIBUTING.md` in repo tree, 2200 stars, only 3 outside PRs merged this year. That gap is your biggest leak.

## Detection (no interview run — single-shot ask, so defaults assumed, flagged below)

- No `devrel-context.md` → cold start.
- Repo has: `.github/`, `docs/`, `src/`, `README.md`, `LICENSE`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `mkdocs.yml`, `AGENTS.md`.
- Missing: `CONTRIBUTING.md`, `GOVERNANCE.md`. Missing file is itself a routing signal.
- Git log: 7 commits in 6 months, last commit 2026-06-30 (~2.5 months stale as of today). Stall pattern.
- Apache-2.0, non-commercial library, no buyer mentioned → assumed Q3=(d).
- No team, no formal program mentioned → assumed Q5=(a) "nothing formal yet."

Assumed answers delete some skills outright: Q3d drops `devtools-pricing-strategy`, `devtools-business-model`, `developer-first-gtm`. Q5a drops `devrel-team-structure`, `devrel-budget-allocation`, `developer-community-health`. License already decided (Apache-2.0) → `oss-license-strategy` off list too. Stall in git log promotes diagnosis over build, per kickoff's own detection rule.

## Route

`samber/developer-relations-skills@oss-contributor-onboarding` — stranger-to-first-merge path. Missing CONTRIBUTING file plus 2200 stars vs 3 merged PRs/year = funnel broken at entry, not at awareness.

## Short-list (value per effort, highest first)

1. **`oss-contributor-onboarding`** — fixes contributor entry funnel (CONTRIBUTING doc, good-first-issue labels, cold-runnable dev setup). Costs one editing session + one PR. Biggest ratio: stars already prove demand, contribution side is what's broken.
2. **`developer-journey-map`** — confirms where the leak actually sits (discover/try fine given stars; contribute stage suspect) before you sink more work in. Costs one session over existing signals, no engineering time.
3. **`oss-issue-triage`** — only 3 PRs merged/year signals slow or absent triage. Costs a system + labels + response-time targets; standing job after setup, not one-off.
4. **`oss-governance`** — 7 commits in 6 months on a 2200-star repo = bus-factor risk. Covers succession, maintainer roles, who holds repo/trademark. Costs sign-off from whoever else has commit rights, if anyone.
5. **`readme-optimization`** — quick pass on first-impression funnel, cheap, complements #1. Costs one editing session.

## Chain

`developer-journey-map` → `oss-contributor-onboarding` → `oss-issue-triage` → `oss-governance`

Diagnosis confirms where the leak is → onboarding fix removes friction at that leak → triage system keeps new PRs moving once contributors show up → governance protects against the bus-factor risk the stall already flagged.

## Not now

- **`devrel-metrics` / `devrel-analytics`** — once you decide whether you even have analytics access on this repo (unasked question).
- **`changelog-writing` / `version-migration-guide`** — once release cadence resumes; 7 commits in 6 months means no release train to hook yet.
- **`developer-champions` / `developer-community-launch`** — once contributor pipeline is actually healthy; premature with a 3-PR/year throughput.
- **`build-in-public`** — could help perception of the stall, but only after #1–#3 give you something real to narrate.

## Gap

Collection has no skill for maintainer burnout as its own subject — relevant here since low throughput + high star count often means one overloaded maintainer. `oss-governance` only covers the succession/bus-factor angle, not burnout itself.

## `devrel-context.md` — save this at repo root yourself (no filesystem access to Copperline's repo from here)

```markdown
# DevRel Context — Copperline

## Product and audience
Python library, schema migrations, Apache-2.0, ~2200 GitHub stars.
Individual developers, self-serve, no commercial buyer identified.

## Program
Funded driver: none formal — assumed contributor-community by default (unconfirmed).
Stage: nothing formal yet, maintainer-hours only (assumed).
Team: unknown headcount, low commit velocity (7 commits / 6 months).

## Surfaces owned
README.md, LICENSE, CHANGELOG.md, CODE_OF_CONDUCT.md, docs/ (mkdocs), AGENTS.md.
Missing: CONTRIBUTING.md, GOVERNANCE.md.

## Measurement
None known. Analytics access unconfirmed.

## State
In flight: none.
Decided: license = Apache-2.0.
Open: funded driver, program stage, effort ceiling, sign-off owner — none confirmed, ask on next session.
Constraint: git history shows stall — last commit 2026-06-30.

## Stakeholders
Unconfirmed — ask who holds merge rights and repo ownership.

## Session log
- 2026-09-19: Cold-start kickoff run without interactive interview (single-shot request). Routed to oss-contributor-onboarding based on missing CONTRIBUTING.md + stall signal. Assumptions made on Q3/Q5 — confirm on next session.
```

Next: confirm the assumed answers (funded driver, effort ceiling, who has merge rights) so the next kickoff run is warm, not another guess.