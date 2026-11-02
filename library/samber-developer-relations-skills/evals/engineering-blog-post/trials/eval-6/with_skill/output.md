I couldn't run `scripts/scan-draft.sh` because the sandbox denied writing the draft to `/tmp`. I checked the draft by hand for superlatives, absolutes, adoption claims and numbers instead. The draft below is a skeleton with `[FILL]` slots, not a finished post, because I have no raw material about how the autoscaler works.

## 1. Mode and pattern

**Mode:** draft mode, with nothing yet to build on beyond the one-line brief.

**Pattern:** How We Built It, with a plain disclosure that Riverbend sells the product.

Ranking, and the strikes the skill requires me to say out loud:
- **Struck: Benchmarks and Rewrote It in X.** There are no before/after numbers or methodology in the brief. If a load test exists, Rewrote It in X comes back.
- **Struck: Bug Hunt, Lessons Learned, Thoughts on Trends.** There's no incident, no set of incidents, and no opinion piece.
- **Survivors:** How We Built It (decisions framed as trade-offs) and Non-markety Product Perspectives. How We Built It ranks higher on efficiency, and it also makes the post a read for an engineer. Its credibility section is "each decision as a trade-off" plus "what went wrong", so someone has to supply real material for both.

**The suggested title is an announcement.** "Introducing Riverbend Autoscaling 2.0" is the failing outline from the skill's worked example 6. Delete the product name and nothing remains, and the title implies a performance claim you haven't measured. I recommend leading with the problem: *"Why we stopped scaling on CPU: how Riverbend Autoscaling 2.0 reacts to queue depth"*. The product name still appears once, for search and for marketing. Keep the original as the title of the changelog or product page.

**Audience:** you're product-led, so the reader is a developer who signs up with a card and may later champion Riverbend at work. The call to action is "try it now": config, quickstart, and the cost of scaling up. There's no "contact sales".

## 2. Claim ledger

| Claim | Class | Action |
|---|---|---|
| CPU is a poor signal for I/O-bound queue workers | Opinion | Keep, first person. Add a sourced reference if one exists. |
| New autoscaler scales on queue depth | Shown | Needs the real config and rule. |
| Exact signal (raw depth vs drain-time estimate) | Unknown | Get it from the design doc. |
| Replica start time | Measured | Needs a number and how it was measured, or cut. |
| "Faster / better / more efficient than 1.x" | **Unsupported** | Cut unless a same-method before/after run exists. |
| Cost impact on customers | Unknown | Confirm. State plainly that more replicas means a higher bill. |
| "10,000 queued jobs" example | Illustrative | Label it hypothetical, as in the draft. |

## 3. Outline (confirm before the body is final)

1. Hook: a real graph where CPU is flat and the queue grows.
2. The problem with CPU for queue workers.
3. What the new autoscaler watches.
4. Decisions and what each one cost.
5. What went wrong.
6. Results, only if measured.
7. Where this does not apply.
8. Try it.

## 4. The draft

```markdown
# Why we stopped scaling on CPU: how Riverbend Autoscaling 2.0 reacts to queue depth

*[Author name(s)], [role], Riverbend Cloud. Published [DATE]. Written against Riverbend [VERSION].*

Disclosure: we build and sell Riverbend Cloud, and this post describes how
one of its features works. Where we measured something, we say how. Where we
did not, we say that too.

[HOOK: one real incident or graph from the old autoscaler where CPU stayed
flat while the queue grew. Needs the workload type, queue depth and CPU over
the same window, and the user-visible delay.]

## The problem: CPU is an indirect signal for queue workers

Riverbend 1.x scaled replicas on CPU utilisation. For a worker that pulls
jobs from a queue, CPU shows how busy workers are, not how much work is
waiting. In my experience two cases break it (opinion):

- I/O-bound workers. A worker blocked on a database or an API call can sit
  at low CPU while the backlog grows.
- Late reaction. By the time CPU on existing replicas saturates, the backlog
  is already built, and new replicas still need [measured: median start
  time] to become ready.

[SHOW: the old 1.x scaling rule, version pinned.]

## What the new autoscaler watches

[FILL from the design doc, in this order: the exact signal (raw depth, depth
per replica, or estimated time to drain); how often it is read; the scale-up
formula; the scale-down rule.]

Raw queue depth alone does not say how fast the queue drains. 10,000 queued
jobs that workers clear in seconds need no action; the same depth at a lower
drain rate does. [CONFIRM which one Riverbend uses. If raw depth, say so
under limitations.]

    # Riverbend autoscaling rule, Riverbend [VERSION], checked [DATE]
    # [REPLACE with the real, runnable config and its expected behaviour]

## Decisions and what each one cost

[One block per decision: options considered, choice, cost. Candidates to
confirm with the team; delete any that did not happen.]

1. Signal: queue depth vs. drain-time estimate, and whether CPU stays as a
   fallback. [Options, choice, cost.]
2. Scale-down behaviour: cooldown or stabilisation window, and whether
   flapping showed up. [Detail.]
3. Supported queues. [List. Anything unsupported goes under limitations.]
4. Bill guard: what stops a stuck queue from scaling replicas, and the bill,
   without bound? [Max replicas default, alerting.]

## What went wrong

[REQUIRED: at least one real dead end, bug or surprise from building this,
with the error text or graph. If nothing went wrong, this is not a
how-we-built-it post.]

## Results

[ONLY if measured: same workload and method, old vs. new; instance size, run
count, variance, absolute values, script link. If this section stays empty,
delete it and make no performance claim anywhere in the post.]

## Where this does not apply

- Services with no queue: [what happens; does CPU scaling still apply?]
- Queue backends not yet supported: [list]
- Scale-up latency floor: [measured replica start time; bursts shorter than
  this are not helped]
- Not tested: [e.g. very deep queues, multi-queue workers, regions]

## Try it

Turn it on from [exact dashboard path or CLI command] [CONFIRM plan limits].
More replicas means a higher bill; the max-replicas setting is how you cap
it. Quickstart: [link]. Config reference: [link]. If it misbehaves on your
workload, report it at [issue tracker or community channel].

Full config and the scripts behind any numbers above: [repo link, commit hash].
```

## 5. Credibility gate report

The draft cannot pass the gate yet, because the evidence is missing and I didn't invent it.

| Check | Status |
|---|---|
| 1. Claims classified | ⚠️ Classified, but several are Unknown until you supply evidence. |
| 2. No unsourced numbers | ✅ The only figure is the labelled hypothetical 10,000. |
| 3. Benchmark disclosure | ✅ Not applicable, because the draft makes no comparative claim. It becomes ❌ if a "faster" claim is added without the disclosure block. |
| 4. One honest limitation | ❌ Slots only. Needs real answers. |
| 5. Zero unsupported superlatives | ✅ By hand. |
| 6. Snippets pinned and dated | ❌ The config block is a placeholder. |

## 6. Handoff: what a human must supply

1. **Raw material.** The design doc, the PR, or an engineer's notes on the signal, formula and cooldown.
2. **A real graph** for the hook, showing CPU flat while the queue grows.
3. **A real "what went wrong".** Without it, this is a press release.
4. **The actual config snippet**, runnable, with the version pinned.
5. **Any measurements, if you want a Results section.** Same workload and method for old and new, with the run count and a script link. Otherwise the post makes no performance claim.
6. **Cost facts for card-paying users.** Max-replicas default, plan limits, and how a stuck queue is capped.
7. **Reviewers.** One engineer on the autoscaler for accuracy, and one person outside the team for readability. Brief them on what to check.
8. **Named authors**, not an unsigned corporate post.
9. **A pass through your preferred humanizer skill** once the slots are filled, then a final `scan-draft.sh` run. I couldn't run the script here.
10. **Preview in your CMS** before publishing, then check the title tag, slug and meta description.

## Questions that would move this forward

- **Hard date?** A launch date would promote a faster pattern.
- **Is there a before/after run?** If yes, I'll draft the Results section and may switch to Rewrote It in X.
- **Can marketing accept the problem-first title**, with "Autoscaling 2.0" as the product-page and changelog title?