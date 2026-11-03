---
name: fabric-writing-policy
description: "Strict low-noise Fabric policy for Hermes: save only high-signal, reusable, verified entries."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, fabric, memory, policy, training, review]
---

# Fabric Writing Policy

Use this skill when deciding whether to write to Fabric and how to structure the entry.

## Goal

Keep Fabric small, sharp, and reusable.

Fabric is **not** a dumping ground for session chatter.
Fabric should contain only entries that improve future recall, review quality, or training quality.

## Save to Fabric only if at least one is true

1. A real bug was found and fixed.
2. An important decision was made and the reason matters.
3. A prior answer or implementation was reviewed or corrected.
4. A resolution was verified with evidence.
5. Research ended in a concrete conclusion worth reusing.

If none of those are true, do **not** write to Fabric.

## Do not save

- generic session summaries
- temporary progress updates
- vague notes like "worked on this"
- raw logs without conclusion
- unfinished thoughts
- temporary identifiers that will go stale
- chatter that does not teach a future agent anything

## Preferred entry types

Use mainly:
- `resolution`
- `decision`
- `review`
- `research` only when it ends with a concrete conclusion

Use fewer:
- `session`

## Required structure

A good entry should contain most of these fields in plain language:

1. **Problem** — what was wrong or needed deciding
2. **Cause** — why it happened, if known
3. **Fix / decision** — what was changed or chosen
4. **Verification** — how it was checked
5. **Outcome** — final result

## Good example

Problem: dashboard model list was stale.
Cause: backend used the wrong provider list path.
Fix: switched to the picker-aware provider function.
Verification: API output now matches the CLI picker.
Outcome: dashboard and CLI show the same model inventory.

## Bad example

Worked on dashboard. Changed some files. Looks better.

## Training value rules

Set `high` only for:
- verified fixes
- strong decisions with outcomes
- useful review chains
- reusable resolutions

Set `normal` for:
- useful but non-critical notes
- research with moderate reuse value

Set `low` for:
- generic summaries
- weak notes
- anything you would not want training a future model

## Verification rules

Prefer `verified=true` only when there is real evidence, such as:
- tests passed
- endpoint returned expected status
- page rendered correctly
- output matched expected result
- user confirmed the fix

If verification is missing, say so plainly.

## Review-chain rule

When prior work was wrong or incomplete:
1. write a `review`
2. write the corrected entry with `revises`
3. add verification if available

This creates better before/after learning data.

## Strong-default workflow

Use this default sequence for high-value cases:

1. Solve the task.
2. Verify the result with concrete evidence.
3. Decide the correct destination:
   - stable fact → Memory
   - repeatable procedure → Skill
   - solved case / important decision / review → Fabric
4. If the result corrected prior work, create a review chain:
   - `review`
   - corrected entry with `revises`
5. Mark training value honestly:
   - `high` for verified reusable outcomes
   - `normal` for useful but less important notes
   - `low` for weak summaries
6. If there is no reusable lesson, write nothing.

## Entry-type defaults

Use these defaults unless there is a clear reason not to:

- `resolution` — default for bugs, incidents, fixes, troubleshooting, and concrete solved problems
- `decision` — default for architecture, config, workflow, or provider choices where the reason matters
- `review` — default when judging earlier work as wrong, incomplete, or notably good/bad
- `research` — only when the conclusion is concrete and likely reusable
- `session` — only for rare cases where a concise session-level summary is genuinely worth future recall

## Anti-noise rules

Before writing to Fabric, reject the entry if any of these are true:

- it is mostly progress/status with no conclusion
- it contains raw logs but no interpretation
- it repeats facts already stored elsewhere
- it is just a paraphrase of the chat
- it would not help solve a similar future case

If two or more are true, do not write it.

## Short pre-write checklist

Before every Fabric write, ask:

1. What is the reusable lesson?
2. Why is Fabric the right place instead of Memory or Skill?
3. What evidence verifies it?
4. Would I want this exact entry used as training data later?

If any answer is weak, do not write yet.

## Decision tree

Ask in order:

1. Is this a stable user or environment fact?
   - Save to Memory, not Fabric.
2. Is this a repeatable procedure?
   - Save as a Skill, not Fabric.
3. Is this a meaningful solved case, decision, review, or verified conclusion?
   - Save to Fabric.
4. Is this temporary chatter or progress?
   - Save nothing.

## Core rule

If the note would not help a future agent solve a similar problem faster or more correctly, do not put it in Fabric.
