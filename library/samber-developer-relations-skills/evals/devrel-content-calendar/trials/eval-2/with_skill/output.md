**Verdict: no — 18 pieces do not fit. Dan is the constraint, not the writer. Review demand ≈ 47 h of Dan; he dependably has ~18-21 h; committed ceiling ≈ 16 h. Plan is ~3× over.**

## Capacity model (step 4: passes, not drafting hours)

**Writer — passes, roughly:**

- 390 h/quarter. 80% committed ceiling = 312 h, rest is slack.
- Your 18 pieces: 6 tutorials × ~30 h + 4 benchmarks × ~20 h + 5 docs × ~10 h + 3 changelogs × ~2.5 h ≈ **317 h**.
- Marginal fail even before counting Dan. Cuts below fix both, but Dan forces them.

**Dan — the binding constraint:**

- Nominal: 13 × 3 = 39 h.
- On call every other week = 6-7 of 13 weeks. Plan those weeks at **zero committed review** — incidents eat them.
- Dependable: 6-7 non-on-call weeks × 3 h = **18-21 h**.
- 80/20 applied to reviewer, adjusted downward (reviewer tighter than writer): **~16 h committable**.
- Skill's own calibration: a 4 h/week reviewer sustains ~2 review-heavy pieces/month. Dan at 3 h/week plus on call = **2-3 review-heavy pieces per quarter. You slotted 10** (6 tutorials + 4 benchmarks are all review-heavy).

## Review demand per format

| Format | Dan h/piece | Count | Total | Why |
| --- | --- | --- | --- | --- |
| Benchmark vs 2 named alternatives | ~5 | 4 | 20 | Reproducible measurements, honest limitations, competitor claims only Dan can defend. Fails late: killed methodology in W10 wastes the slot. |
| Tutorial, runnable code | ~3 | 6 | 18 | Checkpoint verification at every step, plus environment. |
| Docs page | ~1.5 | 5 | 7.5 | Correctness review only. |
| Changelog | ~0.5 | 3 | 1.5 | Invert ownership: Dan owns substance at release, writer edits — near-zero incremental cost. |
| **Total** | | **18** | **47** | vs ~16 committable. |

Verdict is estimate-proof: halve every number above, still 23.5 h > 16.

## What to drop, in order

1. **All 4 benchmark posts.** Biggest Dan cost (20 h = 43% of demand), highest claim-verification burden, fails late. The skill's worked example cuts exactly this format first when reviewer-constrained. Zero this quarter.
2. **Tutorials 6 → 3.** −9 h. Tutorials stay the adoption engine for open core — protect a core three, don't spread six thin.
3. **Docs 5 → 4.** −1.5 h. Keep the four with strongest demand evidence (tickets, search-returning-nothing).

**Result: 3 tutorials + 4 docs + 3 changelogs = 10 pieces, ≈ 16.5 h Dan, ≈ 137.5 h writer.** Fits budget with writer slack for reply load, refresh slots, and reactive work — writer slack is not a reason to re-add Dan-dependent pieces.

Swap variant: 2 tutorials + 5 docs + 3 changelogs = 15 h, if the docs backlog is the demand-heavy one. Pick by evidence, not preference.

## Rules that make it hold

1. Dan-dependent publishes only in non-on-call weeks.
2. Each piece gets a named Dan review slot ~2 weeks before publish, batched into one block per week — never "when he has a minute."
3. Mid-quarter review: if on-call turns out mild, buy back the 5th docs page (1.5 h) first, a 4th tutorial (3 h) second.

## If benchmarks are strategic anyway

One benchmark costs 5 h of Dan ≈ 1.7 tutorials ≈ 3 docs pages. Keeping one means 2 tutorials + 1 benchmark + 4 docs + 3 changelogs = 18.5 h — runs at the dependable ceiling with **zero slack**. Only affordable shape: one reusable harness, one methodology sign-off (~4 h Dan), all future benchmark posts share it. Still recommend zero this quarter; revisit at the mid-quarter checkpoint, not now.

## Real fix is organizational

"A team with no technical reviewer available cannot run any shape at the cost stated here." Until a second verifier exists (train one engineer to verify docs + tutorial claims, Dan keeps benchmarks/architecture), this team's cap is ~10-11 pieces per quarter of this mix, regardless of writer hours.

Assumption: 13 weeks anchor-light, no launch freeze given. Changelog entries are release-tied whenever releases ship — they cost little either way. Re-run with real anchors to place dates.