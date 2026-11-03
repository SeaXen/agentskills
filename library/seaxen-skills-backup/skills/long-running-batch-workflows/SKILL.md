---
name: long-running-batch-workflows
description: Use when executing multi-step batch work that would run >3 minutes continuously (WebP/image conversion, data processing, large migrations, bulk file operations, ML training data prep). The user wants step-by-step execution with cool-downs between batches to manage laptop heat and SSD throttling. Trigger on phrases like "step by step", "give gap", "laptop heat", "long process", "don't run too long", or when work involves many similar items each requiring >100ms of CPU/IO.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [workflow, batch, performance, thermal, kanban, planning]
    related_skills: [plan, writing-plans, simplify-code, subagent-driven-development]
---

# Long-Running Batch Workflows

When the user asks for batch work that will run many minutes (image conversion, data processing, bulk file ops, large migrations), do NOT run it as one continuous Python/Node loop. Break it into small steps with cool-downs between batches, track each step with the `todo` tool, and commit progress after each phase.

## The Pattern

```
STEP 1: Survey (1-2 min)        → count items, measure total size
STEP 2: Test on smallest (1-2 min) → validate approach on 1 file/chapter
STEP 3: Decide strategy (1 min)  → batch size, cool-down length, output format
STEP 4: COOL DOWN (30s)         → let laptop/SSD recover
STEP 5: Batch 1 (2-5 min)       → process 5-10 items
STEP 6: Verify (1 min)          → spot-check 1-2 outputs
STEP 7: COOL DOWN (30s)         → between batches
STEP 8: Batch 2 (2-5 min)       → next chunk
... repeat ...
FINAL: Commit + push + docker commit (if applicable)
```

## When to Use This Pattern

Apply when ANY of these is true:

- **Total time would exceed 3 minutes continuous** of CPU/IO work
- **Work involves >50 similar items** (images, files, chapters, records, rows)
- **Each item takes >100ms** of CPU time (Python/Node startup dominates)
- **User signals thermal/operational concern**: "laptop heat", "step by step", "give gap", "don't run too long", "take breaks"
- **Laptop work** (vs. server) — fan noise, thermal throttling, battery drain
- **IO-heavy work** — SSD writes can throttle after sustained writes
- **Process is unrecoverable if interrupted** — must commit progress between batches

Skip this pattern when:
- Work fits in a single short operation (<2 min)
- The user is on a server / cloud machine (no thermal concern)
- The work is naturally idempotent and resumable (can just rerun)

## Tooling

### `todo` tool (PRIMARY tracking)

Use the `todo` tool to track each step:
- `merge=false` at start to create the plan
- Mark each step `in_progress` when starting
- Mark each step `completed` IMMEDIATELY when done (don't batch completions)
- Add a new step if the work reveals an unplanned sub-task
- `merge=true` for small updates during execution

Each step should be **2-5 minutes of focused work**. If a step is larger, break it down. If smaller, group related micro-steps.

### Background terminal (escape hatch for very long ops)

Only use `terminal(background=true, notify_on_complete=true)` for operations that:
- Are a single command (not a Python loop)
- Run >5 minutes and would block other work
- You need the foreground free for the next step

The user wants you to TRACK via todo, not delegate everything to background.

### Time-bounded subprocesses

```bash
# Measure batch duration
START=$(date +%s)
process_batch_1
END=$(date +%s)
echo "Batch 1: $((END-START))s"
sleep 30  # cool down
```

## Cool-Down Triggers

Sleep 30-60s when:
- After every 2-5 minutes of continuous CPU/IO work
- Before switching batch tools (e.g. cwebp → docker cp)
- After 5+ parallel processes spawned
- When laptop fan ramps up (subjective but real)
- Between Docker commits (image write is heavy)

## Pitfalls

1. **One giant Python loop** — never `for x in 3000_items: process(x)`. Always batch.
2. **Skipping verification** — after batch N, spot-check 1-2 outputs before batch N+1.
3. **No cool-down** — 3+ minutes of cwebp/Pillow/similar without break can throttle SSD/CPU on laptops.
4. **Lost progress** — commit after each phase, not at the end. A long task that gets interrupted at 80% should leave the repo in a known-good state.
5. **No early termination signal** — if a batch shows 0% progress or 100% failure rate, stop and check before continuing.
6. **Quiet tools** — cwebp with `-quiet` shows nothing; use `time` or `date +%s` to track progress.
7. **No throughput measurement** — log "Batch N: 53 items in 81s (0.65/s)" so you can spot regressions.
8. **Trusting subagent self-reports** — measure yourself, don't accept "batch complete" without evidence (number of items changed, file sizes verified).
9. **Cool-down at the wrong time** — sleeping AFTER the final batch wastes time; sleeping BETWEEN batches is the goal.
10. **Forgetting to update the todo list** — leaving items `in_progress` after they're done defeats the tracking purpose.
11. **Claiming "all done" based on the last edit.** When the user follows up with "is it complete? anything still X?", re-run the actual measurement (e.g. `find ... | wc -l`), do not re-assert the prior claim. A 30-second probe buys credibility you cannot buy back from a wrong "yes, all done" — see `static-site-performance-optimization/references/web-perf-recipe.md` §"Anti-pattern: claiming 'all done' without re-verification" for the canonical example.

## Example: WebP Conversion (this session)

```python
# STEP 1: Survey
total_pngs = find . -name "*.png" | wc -l  # 3034
total_size = du -sh .  # 0.86 GB

# STEP 2: Test on smallest chapter
python3 webp_convert.py 1-clinical-decision-making  # 6 PNGs, 3.7 MB → 1.5 MB, 3s

# STEP 3: Decide batches (5-6 chapters per batch, ~2-5 min each)

# STEP 4: COOL DOWN 30s
sleep 30

# STEP 5: Batch 1 (6 chapters)
for ch in ch2 ch3 ch4 ch5 ch6 ch7; do python3 webp_convert.py $ch; done

# STEP 6: Verify
ls ch1/diseases/*.webp  # confirm output

# STEP 7: COOL DOWN 30s
sleep 30

# STEP 8: Batch 2 (next 6)
... continue ...

# FINAL: git commit + git push + docker commit
```

## Communication Style

When the user requests long batch work:

1. **Acknowledge the constraint**: "Got it — I'll do this in batches with 30s cool-downs to keep your laptop happy."
2. **Show the plan**: list steps via `todo` so they can see progress
3. **Report per-batch**: "Batch 1: 6 chapters, 117s, -75% size" (with concrete numbers)
4. **Don't over-explain** between batches — just the result, move on
5. **At the end**: total time, total savings, what's left to do

## Kanban Mode: `todo` as a visible board

When the user explicitly says "kanban", "plan", or "use kanban/plan", shape the `todo` list as a visible kanban board with explicit columns. The default `todo` workflow (1-line per step) hides structure; kanban mode shows lanes and unblocks the user from asking "what's next?".

**Shape**: name each `id` with a prefix that maps to a column. `merge=false` at the start to lay out the whole board, then `merge=true` as you move cards.

```python
todo(merge=false, todos=[
    # BACKLOG — known work, not started
    {"id": "backlog-1", "content": "Convert PNGs to WebP (3034 files)",      "status": "pending"},
    {"id": "backlog-2", "content": "Generate 480w/960w variants for >300KB",  "status": "pending"},
    {"id": "backlog-3", "content": "Update chapter.js to use srcset",         "status": "pending"},
    {"id": "backlog-4", "content": "Copy variants to container + chmod 644",  "status": "pending"},
    {"id": "backlog-5", "content": "Verify in browser + measure size",        "status": "pending"},
    {"id": "backlog-6", "content": "git commit + push",                        "status": "pending"},

    # IN_PROGRESS — work actively in flight (only one at a time)
    {"id": "wip-1",    "content": "Convert PNGs to WebP (3034 files)",       "status": "in_progress"},

    # DONE — completed and verified
    # (move here as you finish)
])
```

**Movement**:
```python
todo(merge=true, todos=[
    {"id": "backlog-1", "content": "Convert PNGs to WebP (3034 files)",      "status": "completed"},
    {"id": "wip-1",     "content": "Convert PNGs to WebP (3034 files)",      "status": "completed"},
    {"id": "wip-2",     "content": "Generate 480w/960w variants for >300KB",  "status": "in_progress"},
])
```

**Cool-down signal**: name one `id` like `cooldown-1` and mark it `in_progress` for the duration of the sleep so the user can see "I'm resting the laptop."

**Why this works for Dr. Sagar**: when he asks "kanban/plan" he wants to see the work, not just trust you're doing it. The 3 lanes (BACKLOG → IN_PROGRESS → DONE) make it scannable, and the per-step `in_progress` marker shows progress without him having to ask.

**Anti-pattern**: do not use kanban for work that has < 4 steps. A 2-step task with a kanban board is overkill; just narrate inline.

## Verification

After the entire workflow, you should be able to answer:
- How many items were processed?
- What's the total time elapsed (real, not estimated)?
- What's the cool-down time budget vs work time?
- Were all batches verified?
- Was progress committed at safe checkpoints?

If any answer is "I don't know", the workflow wasn't tracked well — restart with a todo list next time.

## Related

- `devops:static-site-performance-optimization` — **the right home for web perf recipes**. Has a `references/web-perf-recipe.md` with a worked example from a real session (MedSea 32-chapter site, 3,034 PNGs, 876 MB → 372 MB). Use that skill when the user asks "make my website fast" or "optimize images" — it has the copy-pasteable code and gotchas.
- `software-development:plan` — for the *planning* phase (write the plan); this skill is for the *execution* phase
- `software-development:writing-plans` — same, for the plan document itself
- `autonomous-ai-agents:kanban-codex-lane` — for delegating batch work to a sub-agent (different approach: parallel lanes vs sequential steps with cool-downs)
