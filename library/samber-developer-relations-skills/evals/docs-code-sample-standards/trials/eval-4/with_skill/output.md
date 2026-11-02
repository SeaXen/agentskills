# Hollowmere Robotics: sample audit fix queue

Method: the skill's severity anchors (P0 harms the reader, P1 doesn't work as written, P2 works but breaks policy). The queue is strictly severity-first, as you asked. Where two findings share a severity, the tie-break is readers affected ÷ fix effort.

## Work order

| # | Finding | Severity | Readers/mo | Effort | Why here |
|---|---------|----------|-----------|--------|----------|
| 1 | **F3**: auth setup page embeds a live-format API key | P0 | 9,000 | 20 min + key rotation | Harms the reader who copies it. P0 goes first whatever the other numbers say. |
| 2 | **F2**: batch-ingest sample calls a method renamed two releases ago | P1 | 18,000 | 30 min | Tie-break within P1: 18,000 readers for 30 minutes, against 700 readers for three weeks. |
| 3 | **F4**: C++ first-call quickstart sample never compiled | P1 | 700 | ~3 engineer-weeks | Same severity as F2, far worse ratio, so it comes second in the P1 band. |
| 4 | **F1**: 61 samples have no language identifier on the fence | P2 | 40,000 | ~2 h scripted pass | Tie-break within P2: about 20,000 readers per hour of effort. |
| 5 | **F5**: 210 samples have no documented expected output | P2 | 120,000 combined | ~6 engineer-days | Same severity as F1, about 2,500 readers per hour of effort, so it comes last. |

## Per-item notes

**1. F3 (P0).**
- Rotate the key before editing the page. Revoking it is what removes the harm, and a page edit alone doesn't.
- Replace the value with `<YOUR_API_KEY>` and explain the placeholder.
- Treat the flag as a candidate until confirmed, but rotate anyway. The skill says a key-shaped string can be legitimate on a credential-rotation page, and this is an auth setup page, so a real key is plausible.
- Check the page history, caches and any copies of the page for the same string.
- After the fix, run `scripts/sample-audit.py docs/ --format json` and filter for `credential-shaped-literal` to find other leaks.

**2. F2 (P1).**
- Update the call to the current method name and pin the install block to the current major version.
- Run the sample once before merging. The skill counts a sample that CI doesn't run as unverified, not passing.
- The rename went in two releases ago, so check whether other samples use the old name. A grep for the old symbol across the corpus is cheap.

**3. F4 (P1).**
- This is an unverified sample, not a confirmed defect. Compile it by hand first. That tells you whether it is a live break or only a missing guarantee.
- The sample is on the adoption path (first call), so the skill's pass threshold wants it at tier Run and green in CI.
- With no C++ build in CI, every C++ sample in the corpus is unverified until a pipeline exists. The skill makes building it the first queue item for that language.
- Before committing three weeks, check whether a compile-only job covering just this sample is a much smaller first slice. That is my suggestion, not a measured estimate.
- Label the sample unverified on the page until the job exists.

**4. F1 (P2).**
- One scripted pass can add the identifiers. Review a sample of the 61 afterwards, since a script can guess a language wrong.
- Add the language-identifier check to the mechanical lint so it can't recur.

**5. F5 (P2).**
- Add expected output to each sample, starting with the highest-traffic pages.
- Where a sample can't be run, say so with an Illustrative or Compile-only label instead of leaving the output out.

## Where strict severity departs from the skill's default

The skill ranks everything below P0 by (readers × severity) ÷ effort. That ratio would put the queue in a different order:

| Order | Skill default (ratio) | Your order (strict severity) |
|-------|----------------------|------------------------------|
| 1 | F3 | F3 |
| 2 | F2 | F2 |
| 3 | F1 | F4 |
| 4 | F5 | F1 |
| 5 | F4 | F5 |

- Strict severity moves F4 from last to third. It puts three engineer-weeks ahead of two cheap fixes that reach 40,000 and 120,000 readers a month.
- The skill warns that its own ratio starves a low-traffic sample that needs a whole harness, and says to promote such a sample by hand when it sits on the adoption path. F4 is on the adoption path, so the strict order is defensible here.
- The cost is in the calendar. F1 is a 2-hour fix, so it can run alongside F4's long build without blocking it. I'd do that.
- This report is a severity list, not the skill's ratio queue.
- The severity labels (P0, P1, P2) are the audit's own. I haven't re-scored them against the corpus.
- The reader counts and effort figures are the ones you gave me, not measured by me.