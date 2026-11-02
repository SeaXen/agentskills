**Short answer: there isn't a credible industry-standard ratio you can put in front of a CFO. Don't lead with one — it's the weakest part of the case, not the strongest.**

## Why the ratio doesn't exist as a defensible number

- No survey body (DevRel Collective, SlashData, Orbit/Common Room) publishes an audited "advocates per registered developer" ratio. What circulates in talks and blog posts is self-reported, single-company anecdote, not benchmarked data.
- "Registered developers" is a bad denominator anywhere it's used — it's a cumulative signup counter, not a population. It never shrinks, it includes dead trials, bot signups, and abandoned accounts. Two companies with identical real usage can report registered counts 10x apart depending on how long they've existed and how aggressively they gate signup.
- The informal heuristics that do get quoted in the field span roughly 1 advocate per 1,000–5,000 *active* developers (high-touch, hands-on support model) to 1 per 10,000–50,000 *active* developers (self-serve, content/community-led model). That's a 10-50x spread — wide enough that picking a number from it to justify a fixed headcount ask is picking whichever end flatters your conclusion, and a competent CFO will smell that.

## What that spread implies for Sedgeline, both ways

Applying the same heuristic range to your two denominators shows exactly why the choice of denominator matters more than the ratio itself:

| Denominator | 1:50,000 (lean) | 1:10,000 | 1:5,000 | 1:1,000 (high-touch) |
|---|---|---|---|---|
| 12,000 MAU | 0.2 heads | 1.2 heads | 2.4 heads | 12 heads |
| 84,000 registered | 1.7 heads | 8.4 heads | 16.8 heads | 84 heads |

You're currently at 2. Depending only on which cell you pick, that reads as "overstaffed" or "understaffed by 80." A ratio that swings that hard isn't a benchmark, it's a rounding error dressed up as data. If you present "the industry ratio is X" and the CFO asks "active or registered, and what's your source," the ask loses credibility on the spot.

## What actually justifies headcount to a CFO

Ratio arguments get punctured; capacity and outcome arguments don't. Build the January ask on:

1. **Workload gap, named specifically** — what's not happening today with 2 people: response SLA misses, no weekend/international community coverage, content backlog, no conference coverage, no onboarding cohort programs. Quantify the backlog (tickets unanswered, events declined, content cadence missed vs. target).
2. **Revenue/retention link** — tie DevRel output to the metric finance actually cares about: activation rate (your 12K/84K = 14% MAU/registered is itself a more useful number than any ratio benchmark — it's your funnel, not an industry comparison), time-to-first-API-call, paid conversion from active developers, support-ticket deflection from community answers.
3. **Phase the ask, don't front-load it** — request 1-2 heads now against the named capacity gap, with the remaining heads gated on hitting defined KPIs (e.g., activation rate improvement, response-time SLA) in the following half. This is a much easier "yes" than 4 heads justified by a number nobody can source, and it matches how finance actually evaluates team-scaling requests — against a plan with checkpoints, not a static ratio.

## Target headcount recommendation

Given 12,000 MAU and no data yet on what specific coverage is failing: **ask for 2 more now (total 4), framed against a named capacity gap and one activation/retention metric, with a second tranche of 2 gated on hitting that metric next cycle.** That's defensible without an external ratio, and it survives the CFO asking "where did this number come from" — because the answer is "our own funnel and backlog," not a borrowed statistic.

If you still want an external number for the deck, get it from a primary source rather than a blog-post ratio: DevRel Collective's annual State of Developer Relations survey publishes team-size-vs-company-stage data you can cite by name — I wasn't able to pull the current edition's figures for you in this session (web search wasn't available), so verify the current numbers there before quoting anything as "industry benchmark" to your CFO.