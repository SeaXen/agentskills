Plan wrong. Fix: **barbell it inside the OSS line** — heavy cash+hours on the one crate you can't lose, thin spread on the rest. Coverage number is a vanity metric, not risk mitigation.

Entry point: single-line stress test (skill step 3/4 OSS-sponsorship model), not full devrel interview — you already gave envelope ($40K) and driver (supply-chain exposure on a critical dependency). No routing needed.

## Why $50/mo × 60 fails

- You ranked by **efficiency** (goodwill per dollar spent). Skill's own OSS axis: efficiency favors breadth, but **value favors depth** — depth buys a named maintainer relationship, breadth buys coverage and goodwill only.
- Rule: promote depth when a single project carries your product's critical path, or the driver is supply-chain exposure rather than goodwill. That's exactly your case — storage layer, one maintainer.
- $600/yr (Self-set: $50×12) to that maintainer changes nothing about bus factor. It's a tip, not insurance.
- DevRel's dominant input is staff time, not cash. A sponsorship check with zero engineer-hours behind it buys nothing the day the maintainer actually disappears.
- "Spreads goodwill widest per dollar" = ranking by cash-per-outcome. Named failure mode: whatever's easiest to count (deps sponsored) wins, and the thing actually carrying risk stays unfunded.

## Reallocated $40,000

All figures below: **Self-set** — no industry benchmark exists for sizing OSS sponsorship (the one available survey has no OSS row at all; it's folded invisibly into other categories).

| Line | Cash | Hours/yr | Owner | Buys | Threshold | Review | If it misses |
|---|---|---|---|---|---|---|---|
| Depth: the crate | $12,000 | ~180 (4h/wk) | *name an engineer* | Top sponsorship tier + real upstream work | Experiment (no baseline yet) — by Q2: direct maintainer contact established, fork/vendor feasibility documented, engineer lands ≥1 non-trivial upstream PR | Quarterly | Escalate hours first, not cash |
| Breadth: goodwill sponsorships | $22,000 | ~20 | OSS program owner | $50/mo × ~36 deps | Coverage count — labeled goodwill, not risk control | Quarterly | Trim dep count |
| Reserve | $6,000 | - | budget owner | Unallocated | - | Quarterly | - |

Starved on purpose: breadth count drops 60 → ~36. That's the trade: fewer logos, real coverage on the one dependency that can actually hurt you.

**Unfunded list:** other single-maintainer-critical deps you haven't audited yet. Check the rest of your dependency graph for more bus-factor-1 packages — this crate may not be the only one.

**Ruled out:** none — you named no constraint (no "cash only" rule, no travel ban, nothing).

## Cut list (if $40K shrinks)

- −20% ($8,000): breadth down to ~$14,000 (~23 deps). Depth line untouched.
- −40% ($16,000): breadth to zero. Depth line still untouched — foundational, cut last regardless of ranking.

**Clocks:** burn monthly · depth line verdict at Q2 kill-date, breadth quarterly · envelope annual.

**Reallocation triggers:** maintainer signals stepping back · engineer on depth line leaves/reassigned · depth threshold missed twice · you find a second bus-factor-1 dependency (redraw the split).

## Funder narrative (plain English — repeat this to your CFO as-is)

"We put real weight behind the one dependency our storage layer can't function without, instead of spreading everything evenly. Twelve thousand dollars and about four engineering hours a week go into building an actual relationship with that maintainer, including making sure we could take over maintenance ourselves if they left. The remaining twenty-two thousand keeps broad goodwill sponsorships across roughly three dozen other dependencies. If the budget shrinks, the broad sponsorships go first — the critical dependency stays funded to the end, because that's the one that could actually break us."

## Gaps before this locks

1. Crate name + which engineer owns the depth relationship?
2. Does the maintainer even offer a tier that high, or does this need a direct contract/grant instead of a sponsorship platform?
3. Is $40K the whole company's OSS budget, or does anything else (existing sponsorships mid-contract) already eat into it?

## Quality gate

- Hours priced, not cash-only: ✅ (depth owner still missing — your input)
- Owner per line: breadth ✅, depth ⚠️ pending
- Threshold traces to baseline or is labeled experiment: ✅
- Reserve ≥10% of discretionary: ✅ ($6,000 = 15%)
- No pillar ranked against another by cost-per-unit: ✅
- Starved item named: ✅ (breadth count)
- Cut list ordered and non-empty: ✅
- Every number tagged self-set/sourced/baseline: ✅ (all self-set, stated)

Next: name the engineer for the depth line — plan locks once that's filled in.