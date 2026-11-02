# Verdict: don't sign off on the "imports omitted" note

The note and the `...` don't fix the bug. They label it.

## Why the proposal fails

- **`...` is not code.** A reader who pastes the block gets a syntax error in Python, Go, Java and TypeScript alike. The issues move from "missing import" to "syntax error."
- **The note adds noise.** Readers called the import block noise. One extra line under every sample repeats that noise on every page.
- **It leaves the cause alone.** The extractor now decides what to cut by position ("first line after imports"), not by what the reader needs. Anything above the first line that isn't an import is also gone. That includes client construction, config, and env vars, which is the setup the proposal wants to replace with `...`.
- **It can't be tested.** Nothing checks that the shown code plus the hidden code still runs.

## Better proposal: keep the full program, show the part that matters

1. **Revert the extractor to the old behavior now.** Do this before the new design ships. It stops new "doesn't run" issues today. It restores the noise, but nobody files bugs about noise.
2. **Make the full file the source of truth.** CI compiles or runs every sample as a complete file. The snippet on the page is a view of that file.
3. **Replace the position heuristic with explicit markers.** The author marks the published region, for example `// docs:start` and `// docs:end`. Setup that readers need goes inside the region. Boilerplate goes outside it. A new sample without markers fails CI, so nobody relies on a default.
4. **Collapse the imports and setup, don't delete them.**
   - The block shows the marked region.
   - A "Show imports and setup" toggle above it expands the full file.
   - The **copy button always copies the full runnable file**, never the trimmed view. This one change fixes most of the issues. Readers who scan get a clean view, and readers who paste get working code.
   - No-JS fallback: render the full file in a `<details>` element, so the page still works if the toggle script fails.
5. **Make fragments an explicit type.** A reference page may show a true fragment, such as a single method call. Mark it as a fragment in the source and style it differently. Quickstarts and tutorials may not use fragments. They must show a complete program, with imports expanded on the first block of each page.
6. **Add a CI gate.** For each sample, check that the marked region is a contiguous subset of a file that builds and runs. Fail the build if it isn't. This is what the original extractor change lacked.

## Rollout

| Step | Owner | Done when |
|---|---|---|
| Revert extractor change | Docs tooling | Published samples include imports again |
| Add markers and full-file CI | Docs tooling | Every sample builds from its full file |
| Ship collapse toggle and full-file copy | Docs tooling and frontend | Copy output compiles in a spot check of ~20 samples across languages |
| Re-enable trimmed view | Docs team | Trimmed view is on only for samples that pass the gate |

## How to know it worked

- The count of "sample doesn't run" issues drops after step 1. Compare against the weeks before the extractor change.
- Copy-button events per page stay flat or rise after step 4.
- No sample ships without markers (enforced by CI).

## Two things I assumed

- Your extractor cuts at the first non-import line in each file. If it also strips code that sits between imports, the revert in step 1 matters even more.
- Your samples are real files in a repo. If they are written inline in the docs source instead, step 2 means moving them into files first.

If the docs team wants a stopgap while step 3 is built, the least harmful one is to show imports on the first block of each page and trim them on later blocks. That halves the noise and keeps one runnable path per page.