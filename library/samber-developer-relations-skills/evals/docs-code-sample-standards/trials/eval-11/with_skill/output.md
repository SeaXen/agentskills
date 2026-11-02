# Thalberg Labs: verdict on the "imports omitted for brevity" proposal

**Verdict: do not sign off.** The note and the `...` placeholder treat a symptom. The extractor change is the defect, and the proposal would add two more policy violations on top of it.

I haven't seen your corpus, CI or extractor, and I ran nothing. Every claim below comes from the change you described and from the skill's policy.

## Why the proposal fails

1. **The samples are still not runnable.** The note tells readers the code is incomplete. It doesn't make it complete. Readers still have to reconstruct the imports and setup themselves, and the issues you're getting are exactly that cost.
2. **`...` breaks the safety rule.** Policy says omissions are marked with a comment in the language's own syntax, never `...` or `…`, and never inside a click-to-copy block. A pasted `...` is a syntax error in most languages. It would turn "does not run" (P1) into "does not run, and we told you to paste it" (P1 plus P2 on every block).
3. **It deletes setup that anatomy requires.** Every sample must carry all imports and explicit client setup. The published artefact is not allowed to have elided setup. The fix is to hide setup, not delete it.
4. **Clarity outranks simplicity.** Google Cloud's ordering of sample principles is clarity, idiomaticity, consistency, simplicity, portability, maintainability, and the higher one wins. The reader complaint ("imports are noise") is a simplicity complaint. The new complaint ("does not run") is a clarity and correctness one. The first loses.
5. **Nothing would catch this again.** Your CI almost certainly runs the full source file, so it stays green while the published region can't run. That is the "samples pass CI but fail for readers" failure mode.

## What I propose instead

**1. Fix the extractor: publish the whole region, hide the setup, never delete it.**

- Wrap the maximum useful code, imports and client setup included. A region that starts after the imports publishes a sample the reader cannot run.
- Render the import block collapsed by default, with a "Show imports" toggle. This answers the original "noise" feedback.
- The copy button must copy the full text, hidden lines included. Rustdoc's `#`-prefixed lines have this property: they compile but don't render.
- Don't ship a hide mechanism whose copy button copies only the visible lines. That recreates the bug.
- Keep the region identifier unchanged and identical across languages.

**2. Gate the published artefact, not the source file.**

- Add a CI step that takes the extracted region exactly as published, hidden lines included, and compiles it in a fresh file against the released package, not the working tree.
- Fail the docs build on it. An advisory job goes red and stays red.
- Add one negative control: a region with its imports stripped must fail the job. Otherwise you can't tell a green job from a job that can't see.

**3. Triage the damage already shipped.**

- Quote-search your issues for samples that fail with missing-symbol or import errors. These are P1 (does not work as written).
- Count them per page and per language, and treat the count as a baseline.
- Rank the fix queue by (readers affected × severity) ÷ effort. Say in the report that it is a ratio, not a severity list.
- Promote the quickstart, auth and first-call samples by hand, even if the ratio ranks them low. They should be tier Run and green in CI.

**4. Ship in two steps.**

- **Days:** revert the extractor to the previous region boundaries for the adoption-path samples, or pull the import-less regions. This stops the bleeding with no new tooling.
- **Sprint:** ship the collapsed-imports rendering, the copy-includes-hidden behaviour and the CI gate.

**5. Check the reader feedback.**

- The "imports are noise" feedback likely came from import-heavy languages. For short samples, a collapsed block may not be worth the UI.
- Decide per language, not globally. Idiomatic beats uniform.

## Policy lines to record

- Anatomy: all imports and setup are present in the published artefact; display may collapse them.
- Safety: omissions are marked with a comment in the language's syntax, never `...`.
- Verification: CI runs the extracted, as-published region against the released package.
- Ownership: name who gets the red build when the extractor changes. The docs team owns the extractor, so its output must be inside their gate.

## Open questions

These change the plan:

- Do you have CI for samples today, and how many engineering hours can go to the gate?
- Which languages are tier 1?
- Can you share the issue count, and the copy-button metrics if your docs platform exposes them?

If the answer to the first question is "no CI", the gate becomes the first queue item. Until a pipeline exists, every sample is unverified, not passing.