# Northbeam SDK samples: status and plan

I worked only from your numbers. I didn't open the repo, so none of this is verified against CI.

## Where we stand

Four committed languages times six scenarios gives 24 cells.

| Language | Tested in CI | Missing or untested | Status |
|---|---|---|---|
| Python | 6/6 | 0 | Reference, complete |
| TypeScript | 5/6 | 1 | Nearly done |
| Go | 4/6 | 2 | Tested, but quality is poor |
| Java | 2/6 | 4 | Worst on coverage and quality |
| **Committed total** | **17/24 (71%)** | **7** | |
| Ruby (not committed) | 1/6 | n/a | Unowned, community-contributed |

- **Coverage gap:** 7 cells are not tested. Each one is either an untested sample or a missing one, and those need different work. Only an inventory can tell them apart.
- **Docs risk:** untested samples in the docs can rot silently. A documented scenario with no CI is a claim we can't back.
- **Rewrite risk:** the rewrite targets Go and Java, which are the languages with the weakest coverage. Only 6 tested Go/Java cells (4 Go, 2 Java) protect it.
- **Ruby:** one sample runs in CI with no owner. Every SDK change can break it, and nobody is accountable for fixing it.

## Concerns with "line-for-line equivalents"

I'd change one thing before starting.

1. **A diff can't show "only syntax differences" across languages.** Nothing mechanical checks the claim. Parity then depends on review discipline and erodes after the first edit.
2. **Literal translation produces unidiomatic code.**
   - Go has `(val, err)` returns, `context.Context` and no exceptions.
   - Java has checked exceptions, builders and `try-with-resources`.
   - Python-shaped helpers in those languages read as foreign code to the Go and Java developers who copy these samples.
   - Samples are a first impression of the SDK, so this is a real DX cost.
3. **TypeScript is not in the plan.** It is a committed language and 5/6 done. The parity rule needs to say whether TS follows Python too.

**Recommendation:** keep your goal, but define parity structurally instead of line by line.
- Same scenario names and the same numbered steps, in the same order.
- Same helper names, adapted to each language's casing (`load_features` / `loadFeatures` / `LoadFeatures`).
- Same variable meanings.
- Idiomatic syntax and error handling.

Then enforce it with a check instead of eyeballing a diff. Tag each step with a marker comment such as `# step: create-client`, and have CI verify that every language has the same markers in the same order per scenario. That gives you the side-by-side comparison you want, and it keeps working after future edits.

If you still want true line-for-line, that is your call. In that case Go and Java reviewers should read the result as a deliberate trade-off.

## Plan

Order matters. The tests are the safety net, so refactor under green tests first, and only then add scenarios.

1. **Inventory (small).** Build one 24-cell matrix: the file exists, runs in CI, or is absent. Record the exact scenario IDs per language. The "four in Go, two in Java" counts don't say which scenarios those are. If Go's four differ from Java's two, the order below changes.
2. **Freeze Python as the reference.**
   - Declare each scenario's step list and helper names, taken from the Python samples.
   - Add a rule that any Python sample change updates the parity manifest.
   - Add the structural parity check from the recommendation above.
3. **Go: refactor its 4 tested scenarios.** Do one scenario per PR, with CI green before and after. Check that the pre-rewrite and post-rewrite test output match.
4. **Java: refactor its 2 tested scenarios**, same method. Do Go first because it has the larger safety net.
5. **Close the 7 gaps, written to the parity manifest from the start.** Don't rewrite then add.
   - TS: 1 scenario. Do it first because it is the cheapest win.
   - Go: 2 scenarios.
   - Java: 4 scenarios.
   - For each cell that is untested but exists, put it under CI or remove it from the docs. Don't leave docs that claim support we don't verify.
6. **Decide Ruby.** The options:
   - **Keep as community-maintained.** Label it that way in the docs. Keep its one CI job as non-blocking, with a stated "may break, unsupported" policy.
   - **Drop it.** Remove the sample and the CI job.
   - **Promote it to a committed language.** That means five more scenarios and an owner.

   I recommend the first option. It costs nothing new and states the support level honestly.
7. **Done means:**
   - 24/24 committed cells run in CI.
   - The parity check is green.
   - The docs list only tested samples.
   - Ruby's status is stated.

## Questions

1. Is TypeScript meant to follow the Python structure too? It is not in your plan.
2. Do you accept structural parity with a CI check instead of literal line-for-line?
3. For the 7 gaps, do you know which samples exist untested and which are missing? If not, step 1 answers it.
4. What is your Ruby decision: keep as community-maintained, drop, or promote?
5. Should we freeze Python while the rewrite runs? Changes to Python mid-rewrite mean the Go and Java work has to follow them.