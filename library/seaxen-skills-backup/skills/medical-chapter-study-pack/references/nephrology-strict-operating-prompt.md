# Nephrology strict operating prompt

Use this reference when the user posts a channel constitution or pinned rule set for nephrology topic production.

## Scope
- Davidson **Chapter 18: Nephrology and urology** only.
- Write or update real files only under `/mnt/tb/Medicine/Nephrology/` unless the user explicitly names the continuation note under `00_Index/`.
- Keep output **FCPS/MRCP-oriented** and **Obsidian-friendly**.

## Continuation baseline
- If the user names `/mnt/tb/Medicine/00_Index/Nephrology Channel Session Resume <date>.md`, use it as the continuation setup.
- Reconcile the resume with the live `Nephrology MOC.md` before choosing the next target when the task is a continuation batch.

## Minimal-read working set
Default strict working set:
1. `Nephrology MOC.md`
2. the exact target topic note
3. **maximum one** directly relevant hub

Rules:
- Do **not** read the whole chapter tree.
- Do **not** scan many extra files just because they exist.
- If this working set is not enough to choose or complete the topic safely, **stop and ask** before widening scope.
- If the user asks for an exact `next N` but the current visible one-hub sequence exposes fewer than `N` unfinished topics, report the exact visible remainder and ask whether to do the smaller same-hub batch or allow wider scope for that turn.
- After the user explicitly widens scope, use the nephrology session-resume note plus the live MOC/hierarchy to select the exact next batch in sequence, then keep navigation edits limited to the MOC and the directly touched hubs/navigation files needed for that widened batch.

## In-place upgrade rule
- Reuse the existing note if present.
- Do **not** create duplicate parallel notes for the same nephrology topic.
- Upgrade only the requested topic in place.

## Navigation update rule
After writing, update only what is directly justified by the touched topic:
- `Nephrology MOC.md`
- the same one relevant hub you already read, if it exposes that topic
- the continuation note, only when the user is actively using it as the restart checkpoint

Do not widen into extra hubs or broad hierarchy maintenance unless the user allowed broader scope.

## Content emphasis
For nephrology notes, prioritize when relevant:
- urinalysis
- urine indices: urine sodium, FeNa, FeUrea
- creatinine / eGFR trend logic
- electrolytes
- acid-base interpretation
- AKI vs CKD
- nephritic vs nephrotic differentiation
- dialysis indication logic
- glomerular vs tubular vs post-renal differentiation

## Output standard
Prefer this section set for upgraded nephrology topics:
- Definition
- Anatomy
- Physiology
- Classification
- Etiology / risk factors
- Pathophysiology
- Clinical features
- Investigations
- Interpretation frameworks where relevant
- Diagnosis
- Differential diagnosis
- Management
- Complications
- Red flags / emergencies
- Important cut-offs / tables / algorithms
- One-page summary
- Revision prompts
- 10 MCQs
- 10 SBAs
- Flashcards when possible

## Git rule
If the nephrology channel rules say git after each completed change or batch:
- stage only nephrology-path files changed in that batch
- include the nephrology continuation note only if it was intentionally updated
- commit with a nephrology-specific message
- push
- verify the nephrology scope is clean after push

## Pitfalls
- Over-reading beyond `MOC + target + max 1 hub`
- Creating a new note when a starter file already exists
- Updating multiple hubs or hierarchy files without explicit need
- Mixing unrelated repo changes into the nephrology commit
- Reporting progress from stale counts instead of the live `Nephrology MOC.md`
