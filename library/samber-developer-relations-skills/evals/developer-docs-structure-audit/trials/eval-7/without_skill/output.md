# Pinerock Docs Quality Scorecard — Methodology & Rubric

## Why the 4s don't survive board scrutiny

"The writing is decent" scores *prose quality*, not *documentation quality*. A beautifully written page about a deprecated retry parameter is a 0, not a 4 — it actively costs someone a broken pipeline. Prose is one input among six, and it's the one least connected to what a board actually cares about: onboarding cost, support load, and trust in a workflow engine's correctness. Separate them, or the number stays a vibe with a decimal point.

## The six dimensions

Score each 0–5 against the anchors below. Anchors are tied to a measured value, not judgment — anyone re-running the measurement should land within ±0.5 of your score.

### 1. Accuracy (weight 25%)
Do the code/DSL examples actually run against the current engine version? This is the highest-weight dimension because Pinerock is an *engine* — a wrong example doesn't just confuse, it breaks a pipeline in production.

- **Measure**: extract every fenced code block from all 120 pages, tag by language/DSL, execute or syntax-validate each against current Pinerock. Pass rate = accuracy score input.
- **Anchors**: 5 = 98%+ pass · 4 = 90–97% · 3 = 75–89% · 2 = 50–74% · 1 = under 50% · 0 = examples untested, unknown pass rate.
- **Cost**: one script, one afternoon. Fully automatable for all 120 pages — no sampling needed.

### 2. Completeness / API coverage (weight 20%)
Is every public surface documented — every exported function, CLI command, config key, trigger type, connector?

- **Measure**: generate a symbol list (exported API, CLI flags, config schema keys) and grep docs for each. Undocumented-symbol count / total symbols = gap rate.
- **Anchors**: 5 = under 2% gap · 4 = 2–10% · 3 = 10–25% · 2 = 25–50% · 1 = over 50% · 0 = no symbol inventory exists to check against.
- **Cost**: half a day if the engine already exposes its API surface programmatically (most do via reflection/CLI --help/schema export).

### 3. Freshness / doc-to-code drift (weight 15%)
Pages that read fine but describe behavior the code no longer has.

- **Measure**: for each doc page, get last-modified date. For each feature/module it covers, get last *substantive* code change date (exclude formatting-only commits). Flag pages where code changed materially more than N days (suggest 30) after the doc's last touch.
- **Anchors**: 5 = 0 stale pages · 4 = under 5% of pages stale · 3 = 5–15% · 2 = 15–30% · 1 = over 30% · 0 = no correlation run.
- **Cost**: one script against `git log`, all 120 pages, no sampling needed.

### 4. Findability (weight 15%)
Correct content that nobody can locate is functionally absent.

- **Measure**: pull site search logs if you have them (zero-result query rate, top queries with no good landing page) and docs-to-issue-tracker 404/redirect data. No analytics yet → that gap is itself a finding, score conservatively and flag "instrumentation missing" as a named limitation.
- **Anchors**: 5 = zero-result rate under 5%, clear IA · 4 = 5–15% · 3 = 15–30% · 2 = 30–50% · 1 = over 50% or no search exists · 0 = no way to measure at all.
- **Cost**: near-zero if analytics already wired (check Posthog/GA per your existing setup); otherwise this dimension is your cheapest lever to improve next quarter — instrumenting it is a two-hour task, not a docs-writing task.

### 5. Task success (weight 15%)
Can a stranger go from zero to a running workflow using only the docs?

- **Measure**: sit 3–5 people who've never touched Pinerock in front of the quickstart, cold, timed. Note every stall point. This is the one dimension that can't be scripted — but n=5 is enough to be defensible; you're not publishing a study, you're catching the top 2–3 blockers.
- **Anchors**: 5 = all succeed under target time, no unscripted help · 4 = all succeed, 1 needed a hint · 3 = most succeed with friction · 2 = under half succeed unaided · 1 = most fail · 0 = never tested.
- **Cost**: half a day, one-time setup, worth repeating quarterly with fresh participants (reuse burns the signal — they'll remember the fixes).

### 6. Support-burden proxy (weight 10%)
The line item the board actually feels: how much of two maintainers' time goes to answering questions the docs should have already answered.

- **Measure**: sample the last 100 GitHub issues/Discord questions tagged "question" or "help." Manually triage each as "answerable from current docs" vs. "genuinely needed a human." Ratio is your proxy.
- **Anchors**: 5 = under 10% docs-preventable · 4 = 10–20% · 3 = 20–35% · 2 = 35–50% · 1 = over 50% · 0 = no triage done.
- **Cost**: half a day for 100 issues. This is the number to lead with in the board deck — it converts directly to maintainer-hours.

## What's explicitly out of the score

Prose quality (grammar, tone, style-guide adherence) is real but secondary — track it as a **modifier**, not a dimension: ±0.25 to the composite, capped, so good writing can't mask a broken example and bad writing can't sink an otherwise-correct, findable page. If you want it numeric, run examples through Vale or similar and report separately, never blended into the headline number.

## Composite formula

```
Score = 25(Accuracy) + 20(Completeness) + 15(Freshness)
      + 15(Findability) + 15(Task success) + 10(Support-burden)
```
Each dimension score (0–5) × its weight, summed, ×4 to land on a 0–100 scale (5×20=100 per dimension max, weights already sum to 100 so no extra scaling needed — just multiply each 0–5 score by its weight/5).

Concretely: `Composite = Σ (dimension_score/5 × weight)`, giving 0–100.

## Execution plan sized for two maintainers, no writer

- **Full population (all 120 pages), scriptable, ~2 days total**: Accuracy, Completeness, Freshness. These three are pure automation — write once, rerun every quarter for free trend data.
- **Sampled, ~1.5 days total**: Task success (n=5 people), Support-burden (n=100 issues). Sampling here is defensible — you're not claiming precision, you're claiming direction.
- **Findability**: zero cost if analytics exist; otherwise a one-time instrumentation task, then free going forward.
- Total first-pass cost: roughly 4 days across two people. Quarterly re-score after that: under a day, since three of six dimensions are scripted.

## How to present it to the board

Lead with the composite number, then the evidence table, then trend, then cost-to-close:

```
Docs Quality: 58/100

  Accuracy            72/100  (91% of code examples pass — 11 broken across 120 pages)
  Completeness        45/100  (34% of CLI flags undocumented)
  Freshness           50/100  (18% of pages stale >30d past a breaking code change)
  Findability          —      (not instrumented — recommend adding this quarter)
  Task success         60/100  (3/5 new users completed quickstart unaided, avg 14 min)
  Support-burden       55/100  (41% of last 100 questions were docs-preventable)
```

- Never present the composite without the breakdown — the number's defensibility comes from being able to point at which dimension is dragging it down and what fixing it costs.
- Report trend, not just the snapshot, starting next quarter — a board weighs "58, up from 51" very differently than "58" cold.
- Attach a remediation estimate per dimension (e.g., "closing the CLI-flag gap is ~3 days, one maintainer") so the score converts into a decision, not just a grade.