**Next action:** answer the 4 questions at the bottom. Your rewrite plan conflicts with the skill's rules, so I need your call before the plan is final.

I ran no scripts and saw no corpus. Every figure below comes from your numbers, and I know nothing about the samples themselves. They all count as unverified until a census runs.

## Where you stand

**Parity matrix, tier 1 only (Python, TypeScript, Go, Java):**

| Language | Tested (T) of 6 | Missing T cells |
|---|---|---|
| Python | 6 | 0 |
| TypeScript | 5 | 1 |
| Go | 4 | 2 |
| Java | 2 | 4 |
| Ruby (community) | 1 | not counted |

- **Parity coverage:** 17 ÷ (6 scenarios × 4 languages) = 17/24 = **70.8%**. The baseline gate is ≥90%, so you fail it. This is a skill baseline, not an industry standard.
- **Cells to close:** 7 `T` cells are missing. Reaching ≥90% needs 22/24, which is 5 more cells.
- **Column shape:** Java is a sparse column. The skill says to fund it or demote it. At 2 of 6 and "worse" quality, Java is tiered above what you staff today.
- **Ruby:** it sits outside the denominator. It is community, unowned and labelled untested. Its one CI-run sample has no owner, so its red build lands in nobody's queue.
- **Unknown cells:** the 7 missing cells split between `P` (present, untested) and `M` (missing). That split decides the effort, so the matrix is not fillable yet.
- **Unknown gates:**
  - Zero P0 findings: no secret scan has run.
  - Adoption-path samples (quickstart, auth, first call) at 100% Run and green: I don't know which scenarios they are.
  - Deprecated-API rate below 43%, the only gate with a measured comparator (Zhou and Walker, FSE 2016): not measured.

## Conflict with your plan

Your plan makes Go and Java line-for-line equivalents of Python: same variable names, same order, same helpers, diff shows only syntax. The skill disagrees on three points.

1. **Idiomaticity outranks consistency.** Google Cloud's ranking is clarity, idiomaticity, consistency, simplicity, portability, maintainability, and the higher principle wins. A transliteration fails idiomaticity even when the diff is clean.
2. **Parity is narrower than you plan.** Per the skill, what stays identical across languages is the sample identifier, the scenario and step order, and the testing approach. Variable names and helper structure are free to differ.
3. **You can't get a pure syntax diff.** Go error returns, `context.Context`, Java builders and exceptions, and camelCase versus snake_case all force structural differences.

A literal port of Python makes Go and Java correct-looking but non-idiomatic. Go and Java readers will notice and distrust them.

**What to keep from your plan:** the part that matches the skill's drift list is **structural drift**, where the same identifier shows a different step order. Enforce these across languages:

- the same scenario identifier
- the same step order
- the same outcome per scenario
- the same auth method
- one failure path wherever the API fails in normal use

**What to drop:** same variable names and helper structure.

**Python as the reference:** use it for scenario identifiers and step order only. Check that Python is also the language readers arrive with. Many corpora over-serve the maintainer's language.

## Plan

Order matters. Rewriting Go and Java in Markdown, without tests, rebuilds the same drift. The skill puts moving samples into compilable source ahead of ownership.

1. **Census and secret scan (about 1 day).** Run `scripts/sample-audit.py <docs-dir> --format summary`. Fix any credential leak first, because P0 outranks everything.
2. **Fill the real matrix.** Mark each non-`T` cell as `P` or `M` (and `S` if stale). Pick the scenario identifiers from the Python set, snake_case, shared by all languages.
3. **Tier each sample.** Choose Run, Compile-only or Illustrative.
   - Run is the default for anything untiered.
   - Billing or destructive samples can't be Run.
   - Compile-only costs a couple of days to stand up, then almost nothing per sample.
   - If you have no CI hours, this step is blocked (see Q2 below).
4. **Move Go and Java into compilable projects, region-tagged, published by transclusion.** The tag is the same scenario identifier in every language. The tested file is complete and the published view is a region, so setup stays hidden but present. Rewrite for idiom here, not as a port. Estimate (an assumption, not measured): 2 to 4 hours per Go sample and 4 to 8 per Java sample, if a test harness already exists.
5. **Close cells in this order**, which follows the effort ratio and sends the adoption-path scenarios to the front:
   - TypeScript 1 and Go 2: 20/24 = **83.3%**.
   - Java 2 of its 4 gaps: 22/24 = **91.7%**, which clears the gate.
   - The last 2 Java cells give 24/24.
   - The ratio starves Java, since it needs the most work per cell. Promote any Java cell on the adoption path by hand.
6. **CI shape.**
   - Install the published SDK artefact, not the working tree.
   - Run hermetic tests per pull request and integration tests nightly against the real service.
   - Make the check blocking.
   - Report per sample.
   - Use dedicated test accounts, teardown plus a sweeper, and secrets from the CI store.
7. **Ownership.**
   - Put code owners on the Go and Java sample paths.
   - Set a fix SLA, with bug fixes outranking new samples.
   - Label Ruby community, untested and unowned on the page. That means either dropping its one CI job or naming a maintainer for it.
8. **Re-run the census after each batch.** Don't declare victory from the fix list. Track tested share and parity coverage per release.

The deliverable of this stage is the filled matrix and the tier list. The Go and Java rewrites come after those two exist.

## Questions (answer 1 first)

1. Do you keep "same variable names and helpers" across languages, or switch to the narrower parity rule (identifier, step order, outcome, auth, failure path, tested approach)?
2. Which exist today for the samples: CI to extend, and engineering hours to build a harness? Without both, Run and Compile-only are off the menu.
3. Which of the 6 scenarios are quickstart, auth or first call?
4. Is Java usage large enough to stay tier 1, or should it drop to tier 2 (entry path plus top scenarios) until you staff it?