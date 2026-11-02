# Second opinion: leaderboard + 90%-in-7-days SLA

Both ideas measure *activity*, not *outcome*, and publish the number externally. That combination is exactly what triggers Goodhart's Law — the metric gets gamed the moment it's a target instead of an observation. Details below.

## 1. Top-10 forum leaderboard by raw answer count

**Verdict: redesign before shipping.** Raw count rewards volume, not help.

Failure modes:
- Farming: fast, low-effort, or duplicate answers to rack up count; racing to answer first instead of answering well.
- Wrong answers left unfixed — count doesn't check correctness or whether the asker was actually helped.
- Rich-get-richer: same 10 names every month discourages new contributors from trying, since the gap is unbridgeable.
- External incentive crowds out intrinsic motivation (over-justification effect) — people start answering *for the badge*, not to help.
- Public handles + public ranking = privacy/consent question, and an SEO/marketing target for agencies wanting exposure via your forum.

Fix:
- Score on **accepted answers + net upvotes**, not raw count. If you don't have an accept/upvote mechanism yet, build that before the leaderboard — a leaderboard is worthless without a quality signal underneath it.
- Reset monthly (you're already doing this) and consider excluding last month's #1 from re-entering the top spot immediately, or run a separate "Hall of Fame" vs. "This Month" so fresh names stay visible.
- Add a "Most Helpful Newcomer" category — protects against the top-10 becoming a closed club.
- Get opt-in consent before publishing a handle publicly; let people decline the badge without losing the recognition internally.
- Decide what the badge *unlocks* (swag, contributor-program invite, priority support) — cosmetic-only badges fade fast as motivation.

## 2. 90% of issues + PRs closed within 7 days, reported monthly

**Verdict: don't ship this metric externally as written.** This is the riskier of the two.

Failure modes:
- "Closed" ≠ "resolved." The metric is satisfied identically by a real fix, a drive-by "works for me" close, or a stale-bot auto-close. Nothing in the number tells you which happened.
- Issues and PRs are conflated. A closed PR could mean merged (good) or rejected (neutral/bad); a closed issue could mean fixed or dismissed. One ratio can't carry both meanings.
- Direct conflict with review quality: a hard 7-day close pressure on PRs pushes maintainers toward rushing review to hit the number — the opposite of what mandatory review/coding-gate discipline is for. A gnarly correctness bug shouldn't get merged faster because the SLA clock is running.
- Complex bugs genuinely take longer than 7 days to diagnose properly. The target then rewards premature "needs more info" / "can't reproduce" closes over real diagnosis.
- Publishing this externally as a health signal is a credibility risk, not just an internal one: enterprise buyers evaluating a feature-flag vendor's OSS maturity will notice if issues are being auto-closed to hit a number, and that reads worse than a lower, honest number would.
- If "maintainer team" includes unpaid external contributors, an enforced SLA on top of volunteer time is a burnout/attrition risk.

Fix — split the one dangerous metric into several safe ones:
- **Time-to-first-response** (triage SLA): safe to target hard, because responding fast ("thanks, looking into it," a label, a question back) is real user-facing value and doesn't pressure a premature close. This is the number worth putting a 90%/7-day target on.
- **Time-to-resolution / backlog age distribution**: report as an *observed* trend in the health report (median, p90, "issues open >90 days"), not as a target. Trends catch drift without creating close-for-the-number pressure.
- **PR review turnaround** (time to first substantive review comment), separate from merge decision — target the response, not the outcome.
- Segment by type/severity before setting any SLA: security issues get an instant-response commitment; ordinary bugs get a response-time target; feature requests and "good first issue" go in an unlimited backlog with no clock.
- If a stale-bot auto-close is part of the flow, exclude those from any "resolved" count and report them as their own line ("N closed for inactivity, reopen if still relevant") — don't let them silently inflate the 90%.

## Bottom line

Same root problem both times: a volume/throughput number, made public, without a quality gate underneath it. Add the quality signal (accepted/upvoted answers; first-response time instead of close time) before either one goes live, or you'll be reporting a number that looks great and means less every month it runs.