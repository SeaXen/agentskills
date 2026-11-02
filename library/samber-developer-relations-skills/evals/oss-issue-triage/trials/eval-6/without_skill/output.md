Two-pass budget, not one flat number. A single "review properly" pass on all 230 wastes hours on PRs already dead.

## Pass 1 — Triage every PR, oldest-first (~8–10 min each)

For each PR, before reading a single line of logic:
- Check CI status — red build kills momentum, park it.
- Check for merge conflicts with current main.
- Check if the underlying issue is already fixed elsewhere (common after 14 months).
- Check if it duplicates another open PR.
- Check if it's still in scope (API may have moved on).
- Bucket it: **close** (stale/duplicate/out-of-scope), **fast-track** (typo/docs/one-liner), or **full review**.

Why: on a 14-month-old backlog, a large slice is already dead weight. Triage first so full-review time only goes to PRs that can actually merge.

Total triage cost: 230 × ~10 min ≈ 38 hours.

## Pass 2 — Full review, by size

- Docs / trivial config fix: 10–15 min.
- Small bug fix, one file, has a test: 20–30 min.
- Medium feature (new validator, new hook, new prop): 45–90 min — check API consistency, type correctness, null/empty/controlled-vs-uncontrolled edge cases, real test coverage.
- Large or architectural change (field-array rewrite, breaking change): 2–4 hours, expect multiple rounds.

## AI-agent-authored PRs: budget more, not less

A clean-looking diff from a coding agent is not a shortcut. Add 1.5–2x the size-based estimate, and check specifically for:
- Plausible-but-wrong semantics — code that reads idiomatic but doesn't match the library's actual behavior.
- Tautological tests — assertions that pass regardless of whether the fix works.
- Unrelated refactors bundled with the actual fix, hiding the real diff.
- New dependencies or unusual code paths (eval, dynamic imports, network calls) — unfamiliar contributor + agent-authored code is exactly the combination that warrants supply-chain scrutiny, not less of it.
- Whether it actually reproduces and fixes the linked issue locally — don't take "looks right" as verification.

## Throughput math

- Assume triage closes/fast-tracks ~35% of 230 → ~150 go to full review.
- Weighted average full review, given the AI-PR tax: ~45 min.
- 150 × 45 min ≈ 112 hours + 38 hours triage ≈ **150 hours total**.
- Split across 4 maintainers at ~4–5 focused review-hours/week each: **~7–9 weeks** to clear the current backlog, not counting new PRs arriving in parallel — add ~20% buffer for that.

## Bottom line

- 10 min triage, every PR, before any deep read.
- 30–60 min full review for typical PRs, 90+ min for non-trivial ones, 2x that for anything agent-flavored.
- Expect the full backlog gone in roughly two months at ~4–5 hours/week per maintainer — not "oldest-first forever," since triage removes the dead ones fast.