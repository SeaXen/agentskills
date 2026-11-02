**Mode:** draft mode. I can't interview you in this one-shot, so everything only your team knows is a `[FILL: …]` slot. I invented no numbers, config keys, or behaviours.

**Pattern:** Non-markety Product Perspectives. Your material is a shipped system, a design shift, and no benchmark data I know of, so Benchmarks and Rewrote It in X are struck. Re-rank to How We Built It if you have design-decision notes. Its credibility section is "what the redesign costs and where it doesn't apply".

**Title:** keep "Introducing Riverbend Autoscaling 2.0" as the product name and announcement tag, but lead with the engineering claim. Suggested:

> **Why we scale on queue depth, not CPU: Riverbend Autoscaling 2.0**

An "Introducing…" title passes none of the topic filters (counter-intuitive, counter-narrative, surprising capability, elegant articulation, recognition). The CPU-vs-queue argument is the recognition and counter-narrative hook.

---

## Claim ledger

| # | Claim | Class | Status |
|---|---|---|---|
| 1 | CPU is an indirect signal for queue consumers (I/O-bound workers idle at low CPU while backlog grows) | Opinion, argued from first principles | Reviewer to confirm it matches your workloads |
| 2 | Required workers ≈ arrival rate × processing time (Little's law) | Sourced (link a standard reference) | Add link |
| 3 | 2.0 reacts to queue depth | Shown | Needs config and log excerpt |
| 4 | Scale-up and scale-down behaviour, thresholds, cooldowns | Shown | `[FILL]` |
| 5 | Any latency, cost, or "faster scaling" figure | Measured | **None exist yet. Cut or measure.** |
| 6 | Limitations (below) | Opinion / Shown | Engineers to correct |

---

## Draft

# Why we scale on queue depth, not CPU: Riverbend Autoscaling 2.0

*By [FILL: engineer names]. Published 2026-[FILL]. Riverbend Cloud is our product; this post describes how its autoscaler works.*

**Autoscaling 2.0 adds workers when work is waiting, not when processors are busy.** That one change fixes the failure we saw most often with the CPU-based autoscaler: a backlog growing while every worker looked healthy.

### The failure: a backlog that CPU can't see

Here is a pattern we kept seeing in [FILL: support threads / internal data / your own incident]:

1. A worker pulls a job from a queue.
2. The job spends most of its time waiting on a database, an API, or a model call.
3. CPU stays low. The autoscaler does nothing.
4. The queue keeps growing.

CPU measures how hard your workers are working. Your users care how long work waits. When jobs are I/O-bound, those two numbers decouple.

```text
[FILL: real graph or log excerpt from a 1.x deployment showing queue depth rising
while CPU stays flat. Include date, workload type, and axis units.]
```

### What 2.0 does instead

You need enough workers to match how fast work arrives and how long each job takes. Little's law gives the shape: workers needed ≈ arrival rate × average processing time [FILL: link]. Queue depth is the observable symptom of that equation being violated. It is direct, it needs no per-workload tuning of a CPU target, and it is what a user feels.

How 2.0 works:

- **Signal:** `[FILL: depth only? depth per worker? age of oldest message?]`
- **Scale-up rule:** `[FILL: thresholds, step size, max rate]`
- **Scale-down rule:** `[FILL: cooldown, drain behaviour, in-flight jobs]`
- **Supported queues:** `[FILL: list, with versions]`

```yaml
# Riverbend Autoscaling 2.0, tested against [FILL: version/date]
# [FILL: minimal real config, under 20 lines, with expected output]
```

### Decisions and trade-offs

[FILL: 2–3 design decisions, each as a trade-off. Candidates to confirm with the engineers:]

- **Depth vs. age of the oldest job.** A depth of 10,000 is fine if workers drain it in seconds and bad if jobs take an hour. Say which one you chose and why.
- **Flapping.** Depth signals can oscillate during bursts. Say what prevents scale-up/down thrash.
- **Scale-down safety.** What happens to in-flight jobs when a worker is removed?

### Where this is the wrong tool

State these plainly. I've drafted the likely ones; keep, correct, or replace them:

- **CPU-bound services with no queue** (for example, request/response APIs). Queue depth has nothing to measure. `[FILL: is CPU scaling still available?]`
- **Queues you can't read depth from.** `[FILL: unsupported or approximate sources]`
- **Cost.** More workers sooner means more spend during bursts. `[FILL: how users cap it]`
- **Not measured.** We have not published a benchmark comparing 1.x and 2.0, so this post makes no speed or cost claim. `[Replace if you run one, with methodology before results.]`

### Try it

Autoscaling 2.0 is available on `[FILL: all plans / which plans]` today. Sign up with a card, `[FILL: free tier or trial terms]`, and enable it with `[FILL: command or dashboard path]`. Docs: `[FILL link]`. Existing deployments: `[FILL: opt-in or automatic; link migration notes]`.

If it misbehaves, tell us at `[FILL: public issue tracker / community / support channel]`. We'll read it.

---

## Gate report

| Check | Result |
|---|---|
| 1. Claims classified | ✅ Ledger complete. Rows 3–5 are blocked until you fill in evidence. |
| 2. No unsourced numbers | ✅ The draft contains none. |
| 3. Benchmark disclosure | ✅ Not applicable, because the post has no comparative numbers. |
| 4. One honest limitation | ✅ Four stated, each needing engineer confirmation. |
| 5. No unsupported superlatives | ✅ None. |
| 6. Snippets pinned and dated | ❌ Placeholders. Pin the version and date when you fill them in. |

I did not run `scan-draft.sh` or the humanizer pass. Both belong after the placeholders are real. Run them on the final text, and preserve code, versions, and the title exactly.

## Handoff: what a human must do

1. **Get evidence for the opening graph.** If no 1.x queue-depth vs. CPU trace exists, the "failure" section has no proof. Reproduce one.
2. **Decide whether to measure.** A before/after on scaling lag or cost would be the strongest section. Without it, keep the "not measured" line.
3. **Fill every `[FILL]`.** Have an engineer who built it review for accuracy. Have someone outside the team read it for insider vocabulary.
4. **Named authors.** Sign it with the engineers who built it, not "The Riverbend Team".
5. **Product-led framing.** I wrote the closing as try-it-now, because developers sign up with a card and there is no sales team. Check that the pricing and plan details match your billing page and don't promise anything unannounced.
6. **Confidentiality read.** Remove customer names and internal service names, and confirm no unannounced roadmap leaked in.
7. **Metadata after preview.** Set the title tag, description, slug, and alt text once it renders in the CMS.

**Questions that would sharpen the post:**
- Do you have any measurement of 1.x vs 2.0?
- Does 2.0 scale on depth, age, or both?
- Is CPU scaling still available as an option?