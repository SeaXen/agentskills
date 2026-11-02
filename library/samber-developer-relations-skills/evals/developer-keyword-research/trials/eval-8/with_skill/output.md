# Keyword map: Glasswing Deploy — candidate cluster triage

## Scope

- **Product:** Glasswing Deploy, CI/CD runner.
- **Axes observed from the evidence itself:** Python is a runtime users run *inside* jobs; on-prem is a supported deployment mode (quote-only pricing); caching and secrets are core runner features. Full language/framework/version axes weren't supplied — not needed for this pass, since all 5 candidates are pre-generated, not a fresh matrix expansion.
- **Adoption mode:** mixed. Exit code 137, venv, and cache-key are individual-adoption (developer mid-job). Pricing and secrets rotation are company-adoption (champion/evaluator).
- **Sources:** all 5 figures are **user-provided**, not pulled by me — no export dates or source system named. Before anyone treats this map as auditable, get the pull dates for each number (docs-search export window, ticket-system date range, telemetry window). Until then, treat every count below as directionally right, not citation-ready.
- **Gap:** the interview's capacity question (pages/quarter the team can ship and keep current) wasn't answered. I'm not cutting anything to a backlog on that basis — all 4 "write" clusters below are cheap enough (an hour to a half-hour each) that capacity is unlikely to be the constraint. Confirm before treating this as a committed quarter plan.

## Ranked clusters

Sorted by outcome per page-hour (evidence tier × business proximity × winnability ÷ cost to write and keep current), highest first. No migration or comparison candidates were in this batch, so the ratio didn't demote anything this round.

| Cluster | Primary query | Family | Evidence | Incumbent | Target surface | Existing URL or new | Priority |
|---|---|---|---|---|---|---|---|
| Job OOM-killed, exit 137 | glasswing exit code 137 | Error string | 4,100 error events (tier 4, User-provided); 61 tickets/quarter (tier 3, User-provided) | Nothing Glasswing-specific — only generic Docker/Kubernetes OOMKilled explanations, none of which reference our config | Error entry | new | P1 |
| Cache key not restored | glasswing cache key not restored | Error string | 900 docs searches (tier 2, User-provided) | 2023 forum thread describing a version we no longer ship — stale, the strongest free winnability signal there is | Error entry | new | P1 |
| Secrets rotation | glasswing secrets rotation | Evaluation | 140 docs searches (tier 2, User-provided) | Our own README, ~half the topic | Trust/limits page | update README | P1 |
| Python venv not found inside a job | python venv activate not found (Glasswing-runner-specific slice only) | Error string | 1,200 impressions (tier 1, User-provided) | Generic Python/venv content — doesn't know our runner exists | Error entry | new | P2 — gated on root-cause confirmation, see brief |

## Company-adoption set

| Cluster | Primary query | Family | Evidence | Incumbent | Target surface | Priority |
|---|---|---|---|---|---|---|
| Secrets rotation | glasswing secrets rotation | Evaluation | 140 docs searches (tier 2, User-provided) | Own README, ~half | Trust/limits page | P1 |

Target for this cycle is "at least one company-adoption entry" — met. This set is thin (1 of 5 candidates); it wasn't buried by the ratio, there just wasn't more evaluation/comparison/migration evidence in this batch. Pull sales and solution-engineer question lists next round — that's the tier this family actually lives in, and it wasn't part of this pull.

## Fix first

- **Secrets rotation** — the README already ranks and already answers half the query. Extend it; don't create a second doc page. Two pages splitting this query is a cannibalization risk you'd be creating, not fixing.

## Do not target

- **glasswing on-prem pricing calculator** (82 docs searches/90d) — no calculator exists and on-prem pricing is quote-only. Building one would mean publishing numbers we can't stand behind. This is the textbook "cannot honestly answer" refusal. If the underlying evaluator need (self-serve pricing signal) matters enough to solve, that's a different, honestly-answerable cluster — a pricing-factors/quote-CTA page — but it has no evidence pull of its own here, so it doesn't enter this map on the back of this number.
- **python venv activate not found, generic form** — owned by Python's own documentation; we cannot out-rank the canonical explainer on "how venv activation works." Only the Glasswing-runner-specific failure mode is targeted (above), not the general concept.

## Writer briefs

**Exit code 137 (P1, new error entry)**
- Open with the exact strings people will paste/search: "exit code 137" and "job failed" (today's actual unhelpful message), so both match.
- State the cause as fact, not hedge: this is always an OOM kill (SIGKILL, 128+9) in the cases behind these tickets. Pull 5–10 real ticket resolutions from support instead of guessing the fix — they already contain it.
- Give a fix that works *today*: how to find the currently configured memory limit (get the actual config path/command from engineering), how to raise it, and how to cut a job's memory footprint (streaming vs. loading fully, fewer parallel workers).
- Do not write as if the product already prints the memory limit — that's 5.1 only. Phrase it conditionally ("From version 5.1, the log also shows the configured limit") and stamp a review date against the 5.1 ship. When it ships, cut the "how to find your limit" workaround section — the log will do it.

**Cache key not restored (P1, new error entry)**
- State the current version up front and stamp a review date — caching internals are exactly the kind of thing that silently rots a keyword.
- Reproduce the current cache-key syntax and log text verbatim.
- Cover the real causes: key computed differently between save and restore steps (e.g., a hash input path changed), branch/scope restrictions, expiry, glob/path mismatch.
- We can't edit the 2023 forum thread, so winning here is about our page actually ranking and being the more complete, current answer — not about displacing the old thread directly.

**Secrets rotation (P1, README update, not new)**
- Before writing: diff the README against real support/sales questions to find the actual missing half — it isn't itemized yet, don't guess at structure.
- Likely gaps worth checking: rotation cadence/automation, whether an in-flight job sees the old or new secret during rotation, audit logging of rotation events, CLI/API vs. UI-only rotation, consistency across environments.
- Write for a compliance reviewer skimming for a checklist match, not just an engineer executing a task: lead with capability bullets, then the how-to steps.

**Python venv not found (P2, new error entry — gated)**
- Do not start writing until engineering/support confirms the actual mechanism: shell-per-step isolation (activation doesn't persist to the next step), a missing venv/virtualenv package in the base image, or a PATH reset between steps. Guessing here fails the "failure conditions covered" bar.
- If the confirmed cause is "venv is missing from our base image," that's a product fix, not a page — route it back to engineering instead of writing a workaround, same call made on exit 137's messaging.
- If it's a runner-mechanics issue, scope the page narrowly to that — "using a Python virtualenv across Glasswing job steps" — not a generic venv tutorial. Include the literal shell error text. Cross-link Python's own docs for the general concept instead of re-explaining it.