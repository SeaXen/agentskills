I can't give you a post under the headline "3x faster ingest than Northlake". I read the skill and its references, and the setup you described fails the skill's credibility gate. Below is a draft you can publish next week that keeps the 3x figure but scopes it honestly.

I couldn't run `scan-draft.sh`. The first attempts errored, and the last needed an approval I couldn't get, so the grep pass on the draft below is not done. I also didn't save the draft to a file, because my earlier write to `/tmp/vantage-post/draft.md` never confirmed. It is inline here.

## Mode and pattern

- **Mode:** draft mode. You have raw results and no post yet.
- **Interview:** I couldn't ask the questions, so I assumed:
  - a company engineering blog,
  - a developer-evaluator audience,
  - a hard date next week,
  - an effort ceiling that excludes new benchmark runs,
  - the commercial interest disclosed in the post.
- **Classification:** benchmarketing, meaning your product against a named competitor. That is the highest-scrutiny class and carries a legal-read cost.
- **Ranking:** Benchmarks wins on value, but it takes weeks and needs re-runs and published scripts. A hard date plus no new evidence strikes it from the menu.
- **What survives:** you have no design decisions, no migration story and no incident. The only material is one result, so the honest form is a short, labelled-indicative measurement post.
- **Alternative:** if you can spend days on evidence before publishing, the full Benchmarks pattern comes back. That route is in the handoff.

## Why the headline fails

- **Tuned against untuned.** The skill calls this "the specific move that gets a post publicly dismantled". If you can't tune both sides, you must say which side is untuned and call the result indicative.
- **One run each.** There is no variance, so the 3x could be noise.
- **"Most people run defaults."** This is unsourced. Either source it or mark it as your belief.
- **A ratio with no absolute values.** "3x" hides whether the gap is 3 versus 1 points/s or 3M versus 1M.

## Claim ledger

| Claim | Class | Action |
| --- | --- | --- |
| "3x faster ingest than Northlake" | Unsupported | **Cut** as a headline. Downgrade to "about 3x in one run, tuned vs defaults". |
| Ours: [V_OURS] points/s, theirs: [V_THEIRS] points/s | Measured (n=1) | Needs the absolute values, a chart and the scripts. |
| Our config is the production profile | Shown | Commit the config and link it. |
| Northlake ran on install defaults | Shown | State the version and link the config. |
| "Most people run Northlake on defaults" | Unsupported | Mark as opinion ("we believe") or source it. |
| m6i.2xlarge, one run | Measured | Disclose it as is, including that variance is unknown. |
| "Vantage is faster than Northlake" in general | Unsupported | **Cut.** Ingest only, one workload. |

## Outline

This follows the Benchmarks pattern in compressed form:

1. Question and disclosure of who we are.
2. Methodology before results.
3. Results with one chart and absolute values.
4. What this does and doesn't show.
5. Where this doesn't apply.
6. Next steps, only if they are true.

## The draft post

Everything in `[BRACKETS]` is a number or fact I don't have. I did not invent any of them.

---

# Ingest, one run: Vantage Metrics (tuned) vs Northlake (defaults)

*[PUBLISH DATE]. Vantage Metrics [VERSION], Northlake TSDB [VERSION].*

We build Vantage Metrics, so read this as a vendor's measurement. In a single run on one m6i.2xlarge, our production tuning profile ingested [V_OURS] points/s. Northlake on its install defaults ingested [V_THEIRS] points/s, a ratio of about 3x. One run gives no variance. Treat the number as a lead, not a conclusion.

## How we measured

- **Hardware:** [N] × m6i.2xlarge (8 vCPU, 32 GB), [region/AZ], [storage type].
- **Versions:** Vantage Metrics [VERSION], Northlake TSDB [VERSION].
- **Workload:** [series count, points per batch, batch size, client count, duration, dataset shape].
- **Vantage Metrics config:** the profile we run in production, committed at [LINK].
- **Northlake config:** install defaults, unchanged. We chose defaults because we believe most installs never change them. That is our belief; we have no survey.
- **Runs:** 1. No warm-up discarded, no variance reported.
- **Reproduce:** [LINK TO SCRIPTS].

## Results

[CHART: ingest throughput, both systems, absolute points/s]

| System | Config | Points/s | CPU % | p99 write latency |
| --- | --- | --- | --- | --- |
| Vantage Metrics | production tuning | [V_OURS] | [..] | [..] |
| Northlake TSDB | install defaults | [V_THEIRS] | [..] | [..] |

## What this does and doesn't show

It shows that our tuned setup outran an untuned competitor on this workload, once. It doesn't show that the engines differ by 3x. The two sides had different tuning, so the gap mixes engine speed with configuration effort. We don't know how much of the 3x a Northlake tuned by its own guide would close.

## Where this doesn't apply

- One run on one instance type. We can't say how stable the ratio is.
- Ingest only. We measured no queries, no compaction behaviour and no recovery.
- Defaults versus tuning isn't an engine comparison. A Northlake operator who follows the vendor's tuning guide may see a smaller gap. We haven't run that.
- [What our profile costs: memory, durability setting, anything it trades away. FILL IN.]

## What we'll do next

[Only if true: we'll re-run with both sides tuned, 10 runs each, and publish the scripts and raw results by DATE.]

---

## Gate report

| # | Check | Result |
| --- | --- | --- |
| 1 | Claims classified | Pass, once the placeholders are filled |
| 2 | No unsourced numbers | **Open.** Needs `[V_OURS]`, `[V_THEIRS]` and the workload figures. |
| 3 | Benchmark disclosure complete | **Open.** Needs versions, workload, config links and scripts. Run count and tuning are disclosed. |
| 4 | One honest limitation | Pass, with four stated |
| 5 | No unsupported superlatives | Pass, since the "faster than Northlake" headline claim is cut |
| 6 | Snippets pinned and dated | Open. Add the date and versions, and link the configs. |

The post must not ship until checks 2, 3 and 6 are closed.

## Handoff: what still needs a human

1. **Fill the placeholders.** Pull absolute throughput, CPU, latency and workload details from the original run.
2. **Pick the headline route.**
   - Route A is the scoped title above, which ships next week and is honest about n=1.
   - Route B is to re-run with both sides tuned. Follow Northlake's tuning guide, do at least 5–10 runs, discard warm-up, and publish scripts and raw data. Then "N× faster ingest" becomes defensible and the post moves to the full Benchmarks pattern. Whether this fits next week depends on your effort ceiling.
3. **Run the chart.** Benchmark posts are read visually, so one chart is required.
4. **Get a technical reviewer** who didn't run the benchmark, and a legal read. A named-competitor comparison invites both.
5. **Invite the Northlake maintainers to review** the config before publishing. If you don't, say so in the post.
6. **Pass the humanizer pass and the `scan-draft.sh` grep.** Both are still undone.
7. **Preview in the CMS** and set the title tag, slug, meta description and alt text.

Two questions decide the route:

- Can you spend a few days on re-runs before next week?
- Is the "most people run defaults" belief backed by anything you can cite?