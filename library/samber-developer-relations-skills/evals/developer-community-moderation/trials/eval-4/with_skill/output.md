# Fix the plan before you build it

Your three heuristics split into one that works and two that will hurt you. Handle them differently, and don't let "score above threshold" be the thing that closes a report *and* bans an account — those need different evidence bars.

**Drop perplexity and boilerplate-phrase scoring as a close/ban trigger.** OpenSSF's own working group on this exact problem concluded there is no reliable technical indicator for AI-generated text — detection runs on maintainer intuition, not a metric (`wg-vulnerability-disclosures#178`). Practically: perplexity bands overlap heavily with terse writers and non-native English speakers, and boilerplate phrasing is trivial for a submitter to vary once they learn what's being filtered — it's an adversarial, non-stationary target, not a stable signal. Worse, for a *security* inbox the failure mode is asymmetric: a false positive here means an auto-closed real vulnerability, not just an annoyed spam sender. Don't build a system whose job is "guess whether a human wrote this" — score whether the report is *actionable*, which is checkable, not whether it's *authored by AI*, which isn't.

**Keep and strengthen "do the referenced symbols exist."** This is the one heuristic in your list that's objective, mechanically checkable, and hard to fake without actually engaging the real code — which is exactly the point where an attacker's cost approaches a legitimate reporter's cost. Build the full pipeline around this idea, not around a composite AI-ness score.

# Replace the scorer with a three-gate pipeline

Curl hit this same problem in the same domain — a security inbox, not a general issue tracker — and published real numbers: ~20% of 2025 bug-bounty submissions were AI slop, each one still cost the 7-person team 30 minutes to 3 hours and pulled in 3-4 people, and the confirmed-valid rate fell from >15% to <5% before they shut the bounty down entirely (Stenberg, "Death by a thousand slops," 2025-07; bounty closed 2026-01-31). Node.js's fix was a reputation floor (HackerOne Signal ≥ 1.0), which pulled a 30+/month spike back to its usual 6-7. Neither project tried to detect authorship. Both gated on structure and reputation instead.

For Tarnish, structure the pipeline as three gates, each with a different consequence — never one score with one auto-close threshold:

**Gate 1 — structural completeness (binary, automatable today).** Require a template: exact crate version/commit, the specific symbol path (function/struct/module) the report claims is affected, and a reproduction command or code block. Missing any field → auto-bounce with the template, not a close. This alone kills a large share of copy-paste slop, since generic filler doesn't survive a "which exact version and symbol" prompt, and it costs you nothing per report to enforce.

**Gate 2 — symbol/version resolution (mechanical, near-zero false-positive rate).** Pull `rustdoc` JSON (or a ctags/rust-analyzer index) for the exact tag/commit the report cites, and check whether every symbol it names actually resolves there. This is stronger than a generic "AI detector" because it's checking a fact, not a style. Resolution rate:
- 100% resolved → passes to Gate 3.
- <100% → auto-reply asking for correction (wrong version pinned is a real, non-malicious failure mode too), start a 7-day clock, close as **needs-info** — not spam, not banned — if no response. This is the correct place for your "invented function names" observation to actually bite, without risking a false accusation.

**Gate 3 — automated repro attempt (the load-bearing gate for a *security* inbox specifically).** Sandbox-compile and run the submitted PoC against the cited commit. Pass (it actually triggers the claimed panic/crash/misparse) → fast-track to human review as likely-real, skip the queue. Fail → route to a **time-boxed** human triage (cap it — 10-15 minutes, matching roughly what curl was already spending per report even mid-flood), close as "could not reproduce" if the cap is hit with nothing found. A failed repro is not proof of bad faith; plenty of legitimate reporters submit incomplete PoCs. This is also why you never auto-close on a score alone in this domain — the cost of missing a real CVE dwarfs the cost of one more human skim.

None of this needs an "is this AI" judgment anywhere in it. It needs "does this claim resolve against the real crate," which you can check with `cargo` and a doc index, not a classifier.

# On banning accounts

Keep it, but treat it as the lowest-leverage tool in the stack, not the enforcement backbone. The skill's own ranking of volume countermeasures explains why: individual bans remove one identity, and a scripted or LLM-driven submitter returns under a new email/account for near-zero cost — you'd be paying per-instance forever against an attacker whose marginal cost is ~0. The leverage is upstream, in gates 1-3, which cut inflow regardless of which identity is submitting.

If you do ban: log a minimal case record (identifier, date, count of invalid/needs-info closures, what template response was sent) so a later false-positive dispute has a paper trail, and never let the same event that closes one report also trigger the ban — require a pattern (e.g., N needs-info or failed-repro closures) before it's an account-level decision rather than a report-level one.

# When to escalate past the gates

Track two numbers weekly regardless of what else you do: **submissions/week** and **valid share** (reports that pass Gate 3 or get confirmed by a human). That's the only thing that tells you whether any of this is working — curl and Node.js both instrumented this before picking a fix.

If gates 1-3 don't bring valid share back up:
- **Move to a reputation-gated channel** — GitHub's Private Vulnerability Reporting plus an account-age/contribution-history floor is a zero-cost version of what Node.js did with HackerOne Signal; a paid HackerOne/Bugcrowd program with a Signal-score floor is the fuller version if Tarnish's volume justifies it.
- **If there's a monetary bounty attached**, know that's the actual incentive being farmed — curl's own sequence was measure → template → signal-gate → withdraw the bounty entirely once valid share kept falling. Removing or capping a reward is the highest-value, highest-political-cost move; don't reach for it first, but don't rule it out if 40/month keeps climbing.

# Two things to confirm before you build this

- Does Tarnish's security inbox currently pay a bounty, or is it a plain disclosure channel? Changes whether "raise the submission cost" ever needs to include withdrawing a reward.
- Is intake a private email alias or something with existing identity signal (GitHub Security Advisories, a HackerOne program)? Changes how cheap Gate 2's "reputation" tier is to add — free on GitHub, a platform relationship on HackerOne.