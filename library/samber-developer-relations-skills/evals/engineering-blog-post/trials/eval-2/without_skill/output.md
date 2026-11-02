**Mode:** draft. **Pattern:** Rewrote It in X.

Two gaps in the material:

- The pattern's credibility section is "what went wrong", and you said nothing broke. I didn't invent a failure. The post says plainly that nothing broke and puts the weight on what the move cost and where the numbers stop applying.
- You gave no methodology for the latency and cost figures, and I didn't make any up. Every `[FILL: …]` below is a fact only your team has. Readers will dismiss unsupported numbers, so fill these before publishing.

---

# We moved our billing reconciliation service from Ruby to Go. p99 dropped from 840ms to 95ms.

*By [FILL: author name(s)], Halcyon Systems. Published [FILL: date].*

Over about four months, we rewrote our billing reconciliation service from Ruby to Go. After the cutover, p99 latency fell from 840ms to 95ms. The EC2 bill for that service dropped roughly 60%.

The migration was uneventful. We had no rollback and no incident, and nothing in the cutover surprised us. This post covers why we think it went that way, what the numbers do and don't show, and when we wouldn't repeat the move.

If you're a backend engineer weighing Go for an existing service, this is one data point from one service. Read it that way.

## The service and why we touched it

Billing reconciliation matches [FILL: what it matches against what, e.g. ledger entries against processor settlements]. It runs [FILL: batch/streaming/request-driven] at roughly [FILL: volume per day or per second]. It's on the path of [FILL: what depends on its latency].

We moved it because [FILL: the actual trigger: latency complaints, the infrastructure bill, a scaling ceiling]. We did not move it because of anything wrong with Ruby in general. [FILL: one sentence on what the Ruby version did well. If nothing, delete this.]

## Results

| | Ruby (before) | Go (after) |
|---|---|---|
| p99 latency | 840ms | 95ms |
| EC2 cost for this service | baseline | roughly 60% lower |

The two figures above are from our production monitoring. This is what we can say about them:

- **Measurement window:** [FILL: dates and duration for each side, and whether they cover month-end or other peak load].
- **Percentile source:** [FILL: APM, load balancer logs, or app-side timers. Where is latency measured from and to?].
- **Hardware:** [FILL: instance types and counts before and after].
- **Workload:** [FILL: same production traffic, or a replay? Same data volume on both sides?].
- **Cost figure:** [FILL: what "roughly 60%" is computed from, such as on-demand vs. reserved pricing and the billing period. Say whether it includes the migration period's double-running].
- **Variance:** [FILL: whether the 840ms and 95ms hold week over week, or are single readings].

The ratio is about 8.8x on p99. In absolute terms, requests that used to take most of a second now finish in under a tenth of one. [FILL: what that change meant to downstream callers, if you can say.]

## What we think produced the gain

Say what you know and what you're guessing. We haven't isolated the cause, and a rewrite changes more than the language.

- [FILL: what you actually changed besides the language: data access patterns, batching, caching, concurrency model, schema. Even small things count.]
- [FILL: any profiling of the Ruby version showing where the 840ms went.]
- [FILL: any profiling of the Go version showing where the 95ms goes.]

Without a Ruby-to-Ruby control, we can't say how much came from Go's runtime and how much from redesign. If the code was restructured on the way over, some of the gain would have been available without leaving Ruby. [FILL: confirm or refute this for your case. This is the question the first sceptical commenter will ask.]

## Why the migration was uneventful

We don't have a war story, so here is what we did that we think mattered. All of it is for you to confirm.

- **Team familiarity.** The team knew what they were doing. [FILL: how much Go experience existed beforehand. If some engineers were new, how did they ramp?]
- **Cutover strategy.** [FILL: big-bang, shadow traffic, gradual percentage rollout? How did you verify the Go output matched Ruby's on reconciliation results?]
- **Correctness checking.** For a billing service the risk is wrong money, not slow money. [FILL: how you proved the new service reconciled identically. Diffing outputs, parallel runs, a period of comparison.]
- **Scope.** [FILL: whether you ported behavior one-for-one or changed behavior along the way.]

"Nothing broke" is a claim about four months and one service. [FILL: if there were minor frictions that never became incidents, such as tooling gaps, slower early velocity, missing libraries, or on-call unfamiliarity, list them here. They make the rest of the post believable.]

## What it cost

- **Four months of engineering time**, [FILL: for how many people, and what they weren't building meanwhile].
- **[FILL: ramp-up, review, hiring, or ownership implications of having a Go service in a Ruby-heavy shop, if applicable].**
- **[FILL: operational changes: deployment, observability, runbooks].**

## When we wouldn't do this

- **If the service isn't a bottleneck.** The benefit here came from a service where latency and compute cost were visible and large. For a service with neither, four months of rewrite buys little.
- **If your team has no Go experience.** Our result depended partly on a team that already knew what it was doing. We can't speak to a cold start.
- **If the cost is I/O-bound elsewhere.** If your latency is dominated by a database or a third-party call, a faster language moves less. [FILL: whether this was true for you, and what share of the Ruby latency was compute vs. waiting.]
- **If the service changes constantly.** [FILL: how stable the reconciliation logic was during the migration. A rewrite of fast-moving code is a different project.]

## What we haven't tested

- Whether the gain holds under [FILL: peak scenarios not yet seen].
- Whether maintenance cost over a year or two comes out lower, equal, or higher than the Ruby version's. Four months of post-migration data can't tell us.
- The cost of the migration against the cost of an optimized Ruby version. We didn't build that comparison.

## Takeaway

For this one service, rewriting from Ruby to Go cut p99 from 840ms to 95ms and the EC2 bill by about 60%, with no incidents. We attribute part of that to Go and part to [FILL: the redesign, if any]. Measure your own bottleneck first.

*[FILL: link to any benchmark scripts, dashboards, or anonymized graphs. Add one chart of p99 before and after, since readers will look for it.]*

---

## Gate report

| Check | Status |
|---|---|
| 1. Claims classified | ✅ Every figure is labelled as measured or has a `FILL` for its evidence. |
| 2. No unsourced numbers | ✅ Only your four figures (4 months, 840ms, 95ms, ~60%). The 8.8x ratio is derived from 840/95. |
| 3. Benchmark disclosure | ❌ Open. Needs window, hardware, workload, and variance from the Results section. |
| 4. One honest limitation | ✅ Rewrite-vs-language confound, plus the "when we wouldn't" section. |
| 5. No unsupported superlatives | ✅ |
| 6. Snippets pinned and dated | ➖ No code. Add the date, and the Go and Ruby versions. |

## Handoff: what a human must do before publishing

1. Fill every `FILL`. Do not publish with check 3 open.
2. Name a technical reviewer on the team, for accuracy of the cost and latency methodology.
3. Decide if "billing reconciliation," the volumes, and the cost figures are cleared for external release. I included only what you gave me.
4. Add the p99 chart.
5. Add at least one real friction, even a small one. A four-month rewrite with zero friction is the part readers are least likely to believe.