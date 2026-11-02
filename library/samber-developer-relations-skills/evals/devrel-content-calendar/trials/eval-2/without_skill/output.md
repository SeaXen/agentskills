**No — 18 pieces doesn't fit. The writer isn't your constraint; Dan is.**

## The math

**Writer capacity:** 30 h/wk × 13 wk = **390 h**. Requested slate needs ~370–400 h (tutorials 25–30 h each with runnable code, benchmarks 30–40 h each, docs ~10 h, changelogs ~3 h). Zero slack — one benchmark re-run or broken-code debug cycle and you're over. Marginal fail.

**Dan capacity:** 3 h/wk × 13 wk = 39 h nominal. He's on call every other week — ~6–7 of 13 weeks. Plan those as near-zero: incidents eat discretionary time first. Realistic supply: **~18–26 h**, and he's a single point of failure (one vacation or bad incident month and it shrinks further).

**Dan demand for the requested slate** (everything makes claims about the product, everything needs him):

| Piece | Est. Dan-hours each | Count | Total |
|---|---|---|---|
| Tutorial w/ runnable code | 2.5–3 (run it, verify claims) | 6 | ~15 |
| Benchmark post | 4–6 (methodology, re-runs, fairness) | 4 | ~20 |
| Docs page | 1–1.5 | 5 | ~7.5 |
| Changelog entry | 0.5 | 3 | ~1.5 |
| **Total** | | | **~44 h** |

44 h demand vs ~20 h usable supply. **~2× over.**

## What to drop

1. **Drop 3 of the 4 benchmark posts.** Worst ratio of Dan-cost to risk. A benchmark vs. named alternatives with a broken methodology becomes someone else's Hacker News post, and you have no verifier-hours to defend it. Keep one — the single most defensible head-to-head — scheduled on an off-call week with a dedicated 2 h methodology block plus run verification (~6 h total). If you need to cut deeper, cut it to zero.
2. **Don't cut tutorials — change their verification model.** Weeks 1–2: put all tutorial code in one repo, CI runs every sample on every PR and weekly against new releases. Dan verifies the harness once (~3 h); each tutorial then costs ~1 h of claims-review instead of ~3. If you skip the harness, cut tutorials to 4.
3. **Keep all 5 docs pages and all 3 changelogs.** Cheapest to verify, evergreen, and changelogs mostly draft themselves from merged PRs.

## Fitted slate: 15 pieces, ~23 Dan-hours

6 tutorials (CI-verified) + 1 benchmark + 5 docs + 3 changelogs ≈ 6 + 3 (one-time harness) + 5–6 + 7.5 + 1.5 ≈ **23 h** — fits the realistic band with slack for one bad on-call month. Writer side: ~280 h of 390 (~72% utilization), leaving room for revision cycles. Don't plan a lone writer above ~80%.

Sequencing: batch Dan's reviews into single 90-min blocks on **off-call weeks only** — fragmented async review of technical claims costs more than the block. Front-load changelogs and docs; build the harness weeks 1–2; benchmark mid-quarter. ⚠️ If Dan's on-call weeks turn out to be *total* losses (~18 h supply), drop the benchmark entirely and push it to Q4.