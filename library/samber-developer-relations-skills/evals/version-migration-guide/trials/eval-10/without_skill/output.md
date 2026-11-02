## The line for the top of the guide

Don't ship the engineer's gut estimate as a bare marketing claim — "about an hour" from the person who *wrote* the guide is the fastest possible case, not the typical one. Validate it first (see below), then use a range, not a single number:

> **Estimated upgrade time: 30–90 minutes for most apps** (less if you have few Tessel v3 APIs in use, more if you're on a large or heavily customized codebase). Run the [codemod](#) first — it handles most of the mechanical changes automatically.

If the validation below confirms ~1 hour is genuinely typical, tighten it to:

> **Most apps upgrade in about an hour**, largely automated by our codemod. Larger or heavily customized codebases may take longer.

Either way: state the codemod exists in that same line — it's the biggest lever on the actual time, and marketing's claim will look inflated if a reader doesn't know a codemod is available before they start reading 17 manual-looking entries.

## Validating the time claim

1. **Time 3–5 real upgrades**, not one. Pick a small app, a medium app, a large/monorepo app, one TS and one JS codebase. Have someone who *didn't* write the guide run them — the author is both faster (wrote it) and biased (wants it to look easy).
2. **Split the clock**: time spent running the codemod vs. time spent on the manual entries it can't cover. That tells you which of the 17 entries are actually the long pole, and whether "about an hour" holds up once codemod coverage is subtracted out.
3. Report a **range or median**, not the author's single anecdote, in the published line.

## Verifying the guide is actually correct

Treat the guide's code as a test suite, not prose — it's checkable, so check it mechanically before trusting a read-through.

1. **Executable doc-tests.** Extract the "before"/"after" snippet from each of the 17 entries and run each through the real v4 compiler/runtime: "before" should fail or warn exactly as the entry claims, "after" should build and run clean. Wire this into CI so a future v4 release that silently breaks an entry gets caught, not discovered by a user.
2. **Codemod fixture tests.** Standard jscodeshift practice: for each transform, add an `__testfixtures__/<case>.input.js` / `.output.js` pair and run via jscodeshift's `defineTest`/`testUtils`. If this doesn't already exist, it's the single highest-leverage check here — it directly proves the codemod produces what the guide claims.
3. **Codemod-vs-guide diff.** Run the codemod on each entry's "before" snippet and diff the result against the entry's hand-written "after" snippet. Mismatches mean either the codemod is wrong or the guide's manual example has drifted from what the tool actually does — both are bugs to fix before publishing.
4. **Idempotency check.** Run the codemod twice on the same fixture set; second run should be a no-op. A non-idempotent codemod corrupts code on re-runs (e.g. CI re-applying it, or a user running it twice by mistake).
5. **Run it against real apps, not just fixtures.** Point the codemod at a handful of actual internal/dogfood apps (ideally the same ones used for the timing test above), then run their existing test suites post-migration. Fixtures prove the transform works on the case you thought of; real apps catch the cases you didn't.
6. **Fresh-eyes walkthrough.** Someone who has never seen v4 follows the guide top to bottom on an app they didn't write, with no help from the author. This is the same session that validates the time estimate (item 1 above) — combine them, it's the same exercise. Note every place they got stuck, misread an instruction, or hit an error the guide didn't mention.
7. **Version-pin the guide.** State the exact v4 version (and codemod version) it was tested against at the top, next to the time estimate. Guides silently rot as the framework moves; a pinned version turns "is this still accurate" into a checkable fact instead of a guess.
8. **Soft-launch before the full push.** Publish as beta / link it in a Discord or community channel to a small group before marketing drives full traffic to it. Real-world stragglers (unusual bundler configs, older Node versions, monorepo setups) surface here cheaper than after a wide promotion.

Ship order: run 1–5 (all mechanical, catch outright wrong entries) → run 6 with real people (catches usability and timing) → fix what surfaces → soft-launch (8) → widen. Only put the time-estimate line live once step 6's numbers actually back it up.