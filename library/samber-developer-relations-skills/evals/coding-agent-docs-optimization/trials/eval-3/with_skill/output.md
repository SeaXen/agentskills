# Corvid Data — OKR target + traffic-stat check

No docs URL or repo given, so no cold run happened. Both answers below are calibration/sanity-check against published data, not a scored audit of your actual corpus. Section 1 (task baseline) is empty for that reason — run it before you lock the OKR number.

## 1. The 95% number: drop it

Put a lower number in, split by category, not one blended figure. Reasons:

- Only open, vendor-published benchmark of this exact shape: Stripe's agentic-integration evals (`github.com/stripe/ai`, 2026-02-26). Best-of-3 per task, not first-attempt. Results: backend-only 73-85%, full-stack 77-92%, feature-depth ("Gym") 61-73%.
- That's the ceiling for a mature, already-optimized doc corpus, scored best-of-3. Skill's own read: "80% first-attempt, unattended, is a stretch goal, not a floor."
- Your set: 3 CRUD tasks (breadth-like, ~backend-only category) + 6 deep tasks (streaming replay, custom partitioner, schema-registry failover — squarely feature-depth/"Gym"). 6 of 9 tasks sit in the category that scores 15-25 points below breadth for every model tested.
- "First try" is stricter than the benchmark's best-of-3. "Unattended" removes the correction turns that produced those scores.
- Corvid's docs have never been cold-run tested. First baseline on an unaudited corpus lands well under these figures — that's expected, not a failure.

Recommendation for the OKR doc:

1. This quarter: run the baseline (9 frozen tasks, fresh agent per task, docs-only access, log every corrective turn). ~half a day of setup, one afternoon to run 9 tasks in parallel.
2. Write the OKR as two numbers, not one: e.g. "≥75% first-attempt on core CRUD tasks, ≥50% first-attempt on deep-integration tasks (replay, partitioner, failover) by Q1." Blending them into one 95% hides that the deep tasks are the hard, revenue-relevant ones — exactly what the VP needs visible, not averaged away.
3. If a single number is contractually required for the OKR template, use the baseline score plus a stated improvement delta ("baseline + 20pts"), not an absolute ceiling picked before any measurement exists.

## 2. The 66% traffic stat: doesn't hold up as an industry fact

That number is Mintlify's own platform telemetry — 66% of measured traffic across docs it powers is agents, up from 15.2% early 2026, self-reported, one vendor, sampled only from sites that already invested in agent-facing docs surfaces. This skill's own reference file lists "quoting a vendor's own traffic statistic as an industry fact" as a named failure mode.

For a budget slide:

- Don't state it as "AI agents are now 66% of documentation web traffic" — that phrasing claims a population-wide fact it isn't.
- If you want to use it: attribute it correctly ("Mintlify reports 66% of traffic on docs it hosts is now agents, up 4x since January") and frame it as a directional trend, not Corvid's own number.
- Stronger for headcount ask: pull Corvid's own docs server/CDN logs, filter by agent user-agent strings (Claude, GPT, Perplexity bots, etc.), and report your own agent-traffic share. If you don't log that yet, that gap is itself a finding worth a slide — "we don't know our own agent traffic share" argues for headcount too.

Next: decide who runs the baseline cold-run this week — that number replaces the placeholder in both the OKR and, if you go that route, the budget slide.