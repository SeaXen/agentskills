# Cardiology strict operating prompt — proven Chapter 16 workflow

Use this when the user turns a live cardiology channel into a strict production lane.

## Scope
- Work only within **Davidson Chapter 16: Cardiology**.
- Write/update real files only under `/mnt/tb/Medicine/Cardiology/`.
- Keep output **FCPS/MRCP-oriented** and **Obsidian-friendly**.

## Source split
- **Anatomy:** Gray's + Davidson
- **Physiology:** Guyton & Hall + Ganong + Davidson
- **Clinical discussion:** Davidson + PasTest + personal notes

## Cardiology emphasis to preserve in full notes
- ECG interpretation
- ACS / ischemia / troponin logic
- Heart-failure and hemodynamic profiling
- Murmur / valve clues
- Syncope and shock differentiation
- Red flags and exam traps

## Minimal-read operating rule
Read only:
1. `Cardiology MOC.md`
2. the exact target note(s)
3. **maximum 1 directly relevant hub**

Do **not** read all files.

If more context is genuinely needed, stop and ask before widening scope.

## In-place upgrade rule
- Reuse the existing note if present.
- Do **not** create duplicate parallel notes.
- Upgrade only the requested cardiology topic in place.

## Allowed post-write updates
After completing the topic:
- update `Cardiology MOC.md` if needed
- update only the **same one directly relevant hub** if needed
- do not touch extra hubs unless the user explicitly widens scope

## Expected section set for upgraded cardiology topics
- Definition
- Anatomy
- Physiology
- Classification
- Etiology / risk factors
- Pathophysiology
- Clinical features
- Investigations
- Interpretation frameworks where relevant:
  - ECG
  - ACS / troponin logic
  - hemodynamic profiles
  - murmur / valve clues
- Diagnosis
- Differential diagnosis
- Management
- Complications
- Red flags / emergencies
- One-page summary
- Revision prompts
- 10 MCQs
- 10 SBAs
- Flashcards when possible

## Git hygiene
- Do cardiology-only path-scoped `git add` / `git commit` / `git push`.
- Stage only cardiology files changed in that batch.
- Do **not** include unrelated repo changes.
- After push, verify cardiology scope is clean.

## Selection rule for bare prompts like `next 2`, `next 5`, `next 10`
- Treat the number as an **exact batch size**.
- Use the live `Cardiology MOC.md` plus the current one relevant hub to identify the next visible consecutive pending topics.
- If the current hub exposes fewer remaining topics than requested, ask whether to continue with the smaller same-hub batch or allow one extra directly relevant hub for that turn.
- If the user grants the extra hub, finish the visible current-hub sequence first, then take only the remaining count needed from the next directly relevant hub in order.

## Reporting rule
When summarizing the batch, report:
- exact completed topic names
- touched MOC/hub files
- cardiology-only commit hashes/messages when relevant
- clean-scope verification result
- refreshed done/left counts when asked or useful
