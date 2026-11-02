## How long to budget per slateform PR

Short answer: don't set one number. The skill's PR gate order (Step 6) splits review into cheap, mandatory gates that run on all 230 first, and an expensive gate that should only run on what survives them. Applying "review properly" as a blanket policy to every PR is the failure mode the skill calls out directly — it treats triage as the work, when triage's job is to schedule the work.

### The gate order, with a time budget per gate

1. **Sign-off + CI status — 0 maintainer-minutes.** Automated precondition, not a menu item. If slateform requires DCO/CLA and CI-green, filter on that first (`gh pr list --json ...` for mergeable state, checks status, sign-off). Anything failing here needs zero review time until the author fixes it. Worth confirming this exists on the repo before anyone opens a diff — if it doesn't, that's the first gap to close, not a review-time problem.

2. **Direction check — ~1–2 minutes, run on all 230, in any order.** Title, description, linked issue, diff shape at a glance: does this belong in slateform at all. This is where most of your problem actually resolves. The MSR 2026 Mining Challenge (353 manually inspected rejected agentic PRs) found **35.7% clear agentic failures + 31.2% workflow-constraint rejections ≈ two-thirds never needed the code read at all** — resolved by description/CI/scope alone. Given your recent PRs "look like they came out of coding agents," expect a chunk of this queue to fall out here, not in a code review. For the oldest PRs (14 months), the equivalent cheap check is "does this still apply" — merge conflicts, target code since rewritten, already fixed a different way. That's the same one-minute class of decision, just a different question.

3. **Size-based risk label — 0 incremental minutes.** Computed from the diff automatically. It's a sort key for step 4, not a review.

4. **Code-correctness review — time-box it, don't open-end it.** Only for PRs that clear step 2. Check out the branch, run the tests, verify the claim in the description against the actual diff (per the response playbook — that's the "properly reviewed" standard, and it's the right one for agent-authored code specifically, since agents are good at plausible descriptions). For a form library, budget **30–45 minutes** as the box for a typical PR (new validation rule, field type, bugfix). If it's not resolved in the box, that's a signal to flag it for a scheduled deeper session with two people, not to keep going — "a session spent debugging one item" is a named failure mode, not diligence.

### The arithmetic (plug in your real numbers)

```
weekly capacity (items) = 4 maintainers × sessions/week × minutes/session ÷ minutes/item
```

I don't have sessions/week or minutes/session per maintainer — that's the one input that would let me turn this into a real week-count. Rough shape with the gates above, unassumed hours aside:

- Step 2 on all 230: 230 × ~1.5 min ≈ **5.75 hours total**, one-time, ≈1.5 hours per maintainer split four ways.
- Say roughly a third to two-thirds clear step 2 as worth a real look (MSR figure as the anchor, not a promise — your actual split needs the pilot below). Call it ~100–150 PRs left, as a planning range.
- At 30–45 min each: **50–110 hours total** of real review, split four ways ≈ **13–28 hours per maintainer**, one-time.

That's a multi-week effort on top of normal work, and it doesn't account for new PRs still arriving while you clear it. Don't treat the time budget as the whole fix — Step 2's lever ranking (cut intake > shorten the promise > add triagers, by effort) says a backlog this size with a rising agent-generated share needs an intake lever too, or the 230 becomes 260 by the time you've cleared the first 100.

### On "oldest-first, review every one properly"

Oldest-first for the *real* review pool is actually well-supported here, not just a fairness call — the response playbook flags stale-PR cost as asymmetric (someone already spent real hours writing these, unlike an abandoned issue), so protecting the oldest sunk-cost PRs first is the right instinct. Keep that ordering for step 4.

But run step 2 (the direction check) across the whole queue first, in bulk, regardless of age. It's cheap enough that doing it out of order costs nothing, and it stops you from spending oldest-first review-grade time working strictly in sequence before you know which of the old ones are even live candidates.

### What would sharpen this number

- Each maintainer's actual available hours/week for this (the missing input above).
- Whether DCO/CI gating already exists on slateform — if not, that's free capacity you're not using yet.
- A timed pilot on 15–20 PRs (Step 9) — that replaces every "3 minutes" and "30–45 minutes" placeholder above with slateform's own measured number, which is what the skill says to trust instead of any of these figures.