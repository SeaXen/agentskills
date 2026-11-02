Verdict first: leaderboard, don't ship as specified. 90%-in-7-days target, don't ship as specified. Both fixable, both have quieter versions that get you the same goal without the failure mode this skill is built to catch (a metric that becomes a target).

## 1. Public top-10 answerer leaderboard

**Don't ship this as-is.**

Findings:

1. Person-level public leaderboard — this skill's own privacy gate says "avoid public per-member leaderboards without consent," and its negative-example report calls out this exact pattern ("public per-member message leaderboard rewards volume and creates privacy exposure"). Confidence: high, direct rule match, not judgment call.
2. Answer count is a volume metric, not a quality metric. Failure mode this skill names explicitly: "rewarding message counts produces chatter... watch for the behaviour the metric encourages, pair any incentivised metric with a quality counter-metric." A public count-based badge invites fast, low-effort, first-to-reply answers over correct ones — worse for a feature-flag product where a wrong answer (e.g. bad rollout-percentage advice) has real blast radius. Confidence: high.
3. Consent and removal. A public ranking ties a real identity to a number nobody agreed to have published, and there's no clean way to "unpublish" once indexed/screenshotted. GDPR-relevant if any answerers are EU-based — worth a legal check before launch, not after.

Fix, keeps the recognition goal:

- Badge yes, ranking no. Award a badge to top answerers (or anyone crossing a quality-reviewed threshold) without a public numeric leaderboard ranking one person against another.
- If a leaderboard ships anyway, make it opt-in (answerer consents to appear) and rank on a quality-adjusted score, not raw count — e.g. accepted-answer rate, or answers with no follow-up correction, alongside volume.
- Report the underlying metric ("non-maintainer share of answers", "active answerers per period") internally in the monthly health report instead — that's exactly what this skill's own worked example does, and it drives the same "community is answering itself" story without publishing anyone's name and number.

## 2. 90% of issues+PRs closed within 7 days, reported monthly

**Don't ship the number as specified.**

Findings:

1. No published source sets "90%" or "7 days" for closure. The one numeric guideline that exists anywhere in the field (VMware, quoted inside CHAOSS) is about *first response* within two business days — not closure. What you're proposing is folklore dressed as a standard: label it that way if you keep it, or better, don't keep it. Confidence: high.
2. Closure ≠ response. The metric this skill tracks is "change request closure ratio" (closed ÷ opened in the same window), read as a trend against your own baseline — not a fixed % target. A hard 90%/7-day target on *closure* creates direct pressure to close fast: premature "wontfix" on real bugs, rushed merges on a service that gates production rollouts, or maintainers racing the clock instead of reviewing properly. This is the skill's named failure mode verbatim: "rewarding closed issues produces premature closes."
3. Issues and PRs are different animals lumped into one number. A security-relevant issue closed fast to hit quota is a worse outcome than one triaged carefully outside 7 days. Bundling both pillars into one % hides which one is actually the problem when the number moves.
4. No baseline yet (as far as you've said). This skill's own rule: with no history, mark the metric "baselining" and read raw numbers for 3+ periods before setting any threshold — a threshold picked before that is arbitrary by construction, whether it's 90% or any other number.

Fix, keeps the accountability goal:

- Split the metric: time-to-first-human-response (target: fast, days not weeks, bot-excluded) vs. change-request closure ratio (target: trending toward 1, read over time, not a fixed %).
- Pull 3 months of trailing history first, set the threshold from that trailing median — not an imported number — before publishing any target externally.
- Pair the closure metric with a quality counter-metric so "fast" can't silently mean "sloppy": reopened-issue rate, or post-merge revert rate on PRs. Report both together or the closure number alone is gameable.
- Exclude bot-driven auto-close (stale-bot closures) from the count — otherwise the number measures the bot, not the team.

## Next action

Send both fixes back to whoever owns the rollout before next month's cadence lands — the leaderboard's consent question and the metric split are both easy to change now, expensive to unwind once public.