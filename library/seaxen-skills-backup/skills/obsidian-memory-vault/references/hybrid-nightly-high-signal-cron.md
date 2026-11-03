# Hybrid nightly high-signal cron for Obsidian

Use this pattern when a nightly Obsidian distillation cron is useful but full-AI runs are too quota-expensive or fail with provider `429 usage limit reached`.

## When to use
- The goal is a **high-signal nightly log**, not a raw activity dump.
- A pure `no_agent=True` script is too dumb.
- A full agent run over broad `session_search` + many reads is too expensive or brittle.

## Recommended shape
Split the job into two layers inside one cron job:

1. **Collector script first** (`script=...`, default `no_agent=False`)
   - scan the last 24h of vault changes
   - rank likely high-signal files by folder + content heuristics
   - emit a compact structured summary
   - include only short excerpts / headings / bullets, not full files
   - optionally include recent session titles only, not full transcript retrieval

2. **Short AI distiller second**
   - read only `AGENT.md`, `System/Assistant/context.md`, and today's daily note if present
   - treat collector output as the main candidate list
   - bias strongly toward **no write over weak write**
   - append at most a few bullets to the daily note
   - update `Memory/decisions.md` only for true decisions
   - update `System/Assistant/issues-fixes-log.md` only for true technical fixes

## Why this works
It preserves the useful part of AI — deciding what is actually durable — while shrinking token use enough to avoid many quota failures.

## Practical settings
- Prefer a cheaper/more-available provider/model for the cron than the user's main interactive model.
- Keep enabled toolsets minimal; for the nightly write path, `file` may be enough.
- Keep the final response terse so the scheduled delivery is scannable.

## Prompt guidance
Useful instruction shape:
- "Use the collector context as the primary candidate list."
- "Read only minimal canonical files first."
- "No transcript dumping."
- "No speculative synthesis beyond provided evidence."
- "Prefer no write over weak write."

## Anti-pattern to avoid
Do **not** make the nightly job start by searching many recent sessions and then browsing widely across the vault. That recreates the high-cost failure mode the hybrid pattern is meant to avoid.
