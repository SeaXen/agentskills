# INDEX.md regeneration — full reference

## When to regenerate

- After a large batch of new learnables (10+ added at once)
- After manifest reconciliation (so counts match)
- When the user asks "how many skills do I have?"

## Running

```bash
python3 ~/.hermes/skills/productivity/hermes-skills-library-maintenance/scripts/regenerate_index.py
```

## What it does

1. Lists every dir under `~/.hermes/skills/learnables/` (skip `_*`)
2. For each:
   - `has_card`: SKILL.md present at root
   - `leaf_count`: count of `skills/<name>/` subdirs
   - `size`: one-shot `du -sh */` aggregated to dict (fast — single shell call)
   - `category`: heuristic on the name
3. Groups by category, sorts groups by count desc
4. Emits one Markdown table per category
5. Appends a section noting the **other** skill locations under `~/.hermes/skills/<cat>/SKILL.md` outside learnables — users want both counts together

## Categorization edge cases

The heuristics in the script are tuned for ~90% accuracy. Notable cases:

- `ai-for-beginners-quiz-app` → "Other" (the heuristic doesn't know "ai-for-beginners" is its own thing)
- `mattpocock-engineering-flow` → "Other" (hasn't been added to the Skills & Meta-Skills list)
- `react-useanimations` → "Design & UI" (matches "useanimations")
- `coolify` → "Self-hosted Tools & Devops" (matches "coolify")

For items that don't fit any bucket, they fall through to "Other". This is
intentional — always show the "Other" group so nothing is silently dropped.

## After regenerating

```bash
# Spot-check
head -30 ~/.hermes/skills/learnables/INDEX.md
wc -l ~/.hermes/skills/learnables/INDEX.md
```

## What INDEX.md does NOT cover

- Verbatim file contents — those are in `skills/<repo>/skills/<leaf>/`
- Manifest drift detection — use `scripts/reconcile_manifest.py` instead
- Live skill metadata — Hermes scans the live tree on start

INDEX is a static, human-readable snapshot. For the canonical ledger, read `_verbatim-manifest.json`.
