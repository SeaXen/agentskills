**Mode:** draft mode.
**Pattern:** Rewrote It in X.

**Status: this is a skeleton, not a publishable post.** Your material has the headline numbers and nothing else. The skill says to refuse to proceed on this pattern until the "what went wrong" material exists. I haven't invented any. Every bracket below is something only your team can supply. The post can't ship until they're filled.

## Pattern ranking

- **Rewrote It in X** matches the material: before/after numbers from a migration.
- **Bug Hunt, Lessons Learned and Benchmarks** are struck. There's no incident, no set of incidents and no methodology.
- **How We Built It** is struck for now. It needs decision-by-decision trade-offs, which I don't have.
- **Fallback:** if the went-wrong section stays empty, publish a short How We Built It built around the two or three decisions that mattered. A rewrite post with no friction reads as a press release.

## Claim ledger

| Claim | Class | Action |
|---|---|---|
| Billing reconciliation service moved from Ruby to Go | Shown | Link the repo or PR if public. Otherwise state "internal". |
| Migration took about four months | Measured | Give start and end dates. Say whether it was one engineer or several. |
| p99 went from 840ms to 95ms | Measured | **Needs methodology.** See the blanks below. |
| EC2 cost for the service dropped roughly 60% | Measured | **Needs methodology.** Give the instance counts and types, and the time window. |
| "The migration went smoothly, nothing really broke" | Opinion | Keep only as first-person judgement, backed by how you verified correctness. |
| "The team knew what they were doing" | Opinion | Cut. It praises the team and tells the reader nothing. |
| Go caused the gains | Unsupported | Downgrade, or measure. See the confound below. |

## Draft

> # We moved billing reconciliation from Ruby to Go: p99 from 840ms to 95ms
>
> *[Byline: named engineers. Publication date. Ruby and Go versions.]*
>
> We rewrote our billing reconciliation service from Ruby to Go over about four months. p99 latency went from 840ms to 95ms, and the service's EC2 bill dropped roughly 60%. This post covers what forced the move, how we ran it, what it cost, and when we wouldn't do it again.
>
> *Disclosure: [Do you sell anything Go-related? If not, say "We have no commercial interest in Go."]*
>
> ## The pain
>
> *[What made 840ms p99 a problem for this service? Name who or what felt it: batch-window overruns, timeouts, reconciliation lag, on-call pages. Without that, 840ms is only a number.]*
>
> ## Why Go
>
> *[Which alternatives did you consider, and why did they lose? Examples: optimising the Ruby, a different Ruby runtime, Java, Rust. If you didn't consider any, say so.]*
>
> ## How we migrated
>
> *[Fill in each of these:*
> - *Big bang or incremental?*
> - *Was there a dual-run period, where both services processed the same input?*
> - *How did you prove the Go service produced the same ledgers as the Ruby one? For billing this is the hard part, and readers will look for it.*
> - *What was the rollback plan?*
> - *How many people worked on it, and for how many weeks each?]*
>
> ## What went wrong
>
> *[Required section. You said nothing broke, so push on that. Candidate questions:*
> - *Did the four months match the estimate?*
> - *Which behaviours of the Ruby code did nobody remember until the Go version disagreed?*
> - *Did any numeric, rounding, time-zone or serialization behaviour differ?*
> - *What did you give up: libraries, dynamic tooling, hiring pool, build times, memory profile?*
> - *What is still ugly?*
>
> *If the honest answer is "very little", write that, but show it. Say what you checked and how many discrepancies the dual-run found, even if the number is small. A bare "it went smoothly" fails the credibility gate.]*
>
> ## Results
>
> | | Ruby | Go |
> |---|---|---|
> | p99 latency | 840ms | 95ms |
> | EC2 cost | [baseline, absolute $ or instance-hours] | roughly 60% lower |
>
> *[Disclosure block, placed before or beside this table:*
> - *Instance types and counts, before and after.*
> - *Window and load: the same traffic mix on both sides? Peak or average? How many days?*
> - *What p99 measures: per request, per reconciliation run, or per batch?*
> - *How it was measured: APM, load test or production traces, and the same tool on both sides.*
> - *Whether anything else changed in the four months: schema, queries, caching, DB indexes, instance generation.*
> - *p50 and p95 alongside p99.*
> - *At least one chart.]*
>
> *Attribution: say how much of the gain came from Go and how much from rewriting the code a second time, with the old behaviour now understood. If you didn't isolate the two, say that. It's the most common objection to a rewrite post.*
>
> ## Where this doesn't apply
>
> *[At least one specific, checkable limit, for example:*
> - *The service is CPU-bound or latency-bound. If yours waits on the database, the win will be smaller.*
> - *We didn't test above [X load].*
> - *Cost savings assume [instance family, reservation pricing].]*
>
> ## Would we do it again?
>
> *[Under what conditions, and under what conditions not. This is first-person opinion, so label it as such.]*

## Gate report

| Check | Result |
|---|---|
| 1. Claims classified | Fail. The ledger has one unsupported claim: Go caused the gains. |
| 2. No unsourced numbers | Fail. 840ms, 95ms and 60% need their runs described. |
| 3. Benchmark disclosure | Fail. Nothing is disclosed yet. |
| 4. One honest limitation | Fail. There's no limitation yet. |
| 5. No unsupported superlatives | Pass. I wrote none, and "smoothly" is not in the draft. |
| 6. Snippets pinned and dated | N/A. There are no snippets yet. |

I couldn't run `scan-draft.sh`. It errored in this environment with "Parser skipped input between top-level statements". The draft has only your three figures, so the numeric check would have flagged just those.

## What I need from you

Answer these and I'll write the full post:

1. **Why was 840ms a problem?** What was it blocking, and for whom?
2. **How did you verify correctness?** Billing readers will ask. Was there a dual-run, and how many discrepancies did it find?
3. **How were the numbers measured?** Cover the cost window, load, instances before and after, and what p99 is over.
4. **Did anything else change** during the four months?
5. **What did the four months actually go on?** Was any of it more than planned?
6. **What's worse, or still ugly, after the move?**
7. **Is there a commercial interest** to disclose?
8. **Who reviews technical accuracy**, and who are the named authors?
9. **Anything that must stay unpublished**, such as customer names or internal figures?

## Handoff

- Fill every bracket.
- Get a technical review from an engineer who worked on the migration.
- Get a second read from someone outside the team.
- Make the chart.
- Check the CMS preview before publishing.
- Run the credibility gate again once the post is complete.