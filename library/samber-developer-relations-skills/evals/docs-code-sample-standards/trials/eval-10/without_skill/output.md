**Next action (10 min):** run the census. `scripts/sample-audit.py <docs-dir> --format json --ext .md,.mdx > inventory.json` (from the docs-code-sample-standards skill). Every number below is an assumption until that file exists.

# Plan: test 1,400 code samples

## 1. Fix the metric first

80% of 1,400 = **1,120 samples**.

The 700 one-liners plus 120 auth copies are 820 samples, or 59% of the corpus. They are also the cheapest to test. If you test only those, you reach about 59%. Then 300 of the other 580 samples get you to 80%. You can hit the number while the quickstarts and multi-step scenarios stay untested, and those are the samples where a wrong example costs a reader the most.

Do two things before work starts:

1. **Write the definition of "tested" down and get it agreed.**
   - A sample counts as tested only if CI compiles or runs it on every release.
   - It must run against the **published** SDK, not the working tree.
   - A failure must block the docs build.
   - A sample that was once checked by hand does not count.
2. **Add companion gates, so the 80% can't be met with trivial samples alone:**
   - 100% of the adoption path (quickstart, auth, first call) is tier Run and green.
   - Every non-trivial scenario sample is covered by the 80%, not only the one-liners.
   - Report two numbers: *placements* (1,400) and *distinct tested sources* (fewer, after dedupe).

⚠️ Leadership approved "80% tested" without a definition. If you don't settle it now, someone will settle it later, probably in a way that undercounts your work.

## 2. Tier every sample

Every sample gets exactly one tier:

| Tier | Applies to | CI does |
|---|---|---|
| Run | Auth, quickstart, first call, high-copy samples | Executes against a sandbox or mock and asserts the output |
| Compile-only | Most of the 700 one-liners, billing and destructive calls | Type-checks against the published SDK |
| Illustrative | Pseudocode, fragments | Excluded, and visibly labelled on the page |

- Untiered samples default to Run, so an unclassified sample fails loudly instead of being ignored.
- Cut dead samples. Removing one that references a removed API costs a reader nothing. That is ROT triage (redundant, outdated, trivial).

## 3. Handle each bucket

**A. 700 one-liners (reference pages)**
- These are one per endpoint, so generate the harness from the OpenAPI spec and the sample files. Don't write 700 tests.
- Per sample:
  1. Extract it.
  2. Wrap it in a stub that supplies client setup and imports.
  3. Compile it against the published SDK.
  4. Optionally run it against a mock server built from the OpenAPI spec (Prism or similar). The mock gives you free Run coverage.
- ⚠️ A mock proves signatures and request shape. It does not prove real behavior. Label this tier "compile + mock", not "verified against the service".
- Expect the first run to fail a lot. Samples hand-written years ago will reference renamed methods and removed endpoints. Triage the failures into fix, delete, or relabel.
- This bucket is low risk per sample. Their value is mostly correct signatures, which the compile check covers.

**B. About 120 auth copies**
- Reduce them to **1 canonical snippet per language and auth method**. For example, API key and OAuth, times languages.
- Test each canonical snippet at tier Run against a sandbox, with a dedicated test credential held in the CI secret store.
- Replace each copy with an include from the tested source. Where the variations are real (scopes, regions), make them parameters of the include, not separate hand-edited copies.
- Result: about 120 placements count as tested, backed by a handful of tests, and drift is gone for good.
- Per the standards skill: "keep auth setup in one place that other samples link to."

**C. The other ~580 (scenarios, tutorials, guides, README)**
- These carry the most reader risk. Test them all, or cut them.
- Order of work:
  1. Pages by traffic and copy-button clicks, if your docs platform exposes them.
  2. Quickstart and tutorials.
  3. The long tail.
- Move each sample into a real compilable file, and publish a marked region of that file into the page. Hide setup in the page, never delete it. This is the single-sourcing pattern.
- Anything that bills, destroys data, or calls a third party is compile-only, never Run.

## 4. CI shape

- **Per PR:** a hermetic job covering compile-only and mock-backed samples. Keep it fast and make it blocking.
- **Nightly or per SDK release:** a Run job against a sandbox, with fixtures that clean up after themselves.
- **Install from the published SDK**, not the working tree. Otherwise CI passes while readers fail.
- **Fail the docs build on a red sample.** If it stays green with red samples, nobody reads the red.
- **Separate flaky from broken.** Split the per-PR job from the sandbox job so a flaky sandbox never gets the whole suite disabled.
- **Freshness:** flag any sample whose last *successful* run is older than a window you set (suggest 30 days).

## 5. Ownership

Answer this in writing: *when a sample goes red on a Friday, whose queue is it in?*

- Suggested default is the SDK owners for reference and auth samples, and docs for tutorials.
- Encode it as CODEOWNERS rules plus a blocking check, not a wiki paragraph.
- You own the program. You do not have to own every fix.

## 6. Phases and effort

These are my rough estimates. Calibrate them after step 0.

| Phase | Work | Rough effort |
|---|---|---|
| 0 | Census, tiering, written definition of "tested", leadership sign-off on it | 2–3 days |
| 1 | Harness for one-liners: extract, stub, compile, mock run. First failure triage. | 1–2 weeks |
| 2 | Auth dedupe, canonical tested snippets, includes | 3–5 days |
| 3 | Scenario samples moved into tested source, in traffic order | 3–6 weeks, parallelizable |
| 4 | Ownership, blocking gates, freshness window, dashboard | 3–5 days |

Expected coverage progression: roughly 59% after phases 1–2 (if all pass), then to 80%+ through phase 3. Phase 3 is the schedule risk.

## 7. Report the program

Track per release, not per audit:

- Tested share (placements) and distinct tested sources.
- Adoption-path samples green: target 100%.
- Pass rate: target ≥90%. Below it, stop authoring and run a remediation sprint.
- Mean time from a red sample to a merged fix.
- Samples over the freshness window.

Label the 80% and 90% figures as targets set by the program, not industry benchmarks. No vendor publishes either.

## 8. Risks

- ⚠️ **Gaming the metric:** covered by the definition and companion gates in section 1.
- ⚠️ **First-run failure rate is unknown.** Old hand-written samples may fail at a high rate. Budget phase 1 triage time for that.
- ⚠️ **Mocks overstate confidence.** Keep the label honest.
- ⚠️ **Credentials in CI:** use a sandbox account with a scoped test key. Run a secret scan on the samples too, since stale hand-written ones may embed real-looking keys. Any hit is P0.

## Questions that change this plan (answer in any order)

1. Which languages are published, and how many samples per language?
2. Is there an SDK and an OpenAPI spec, and are samples published from the SDK's current version?
3. Does CI exist for the docs repo today?
4. Is there a sandbox environment with test credentials?
5. What is the deadline for the 80%, and how many engineer-days do you have?

**Next:** run the census command above and paste the summary line (count by language and by page type). I'll then turn the estimates into a dated schedule.