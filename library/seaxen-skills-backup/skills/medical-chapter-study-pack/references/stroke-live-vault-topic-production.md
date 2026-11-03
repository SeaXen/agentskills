# Stroke Live Vault Topic Production

Session-proven workflow for continuing Davidson **Chapter 29: Stroke medicine** inside `/mnt/tb/Medicine/Stroke Medicine/`.

## Scope guard
- Keep this channel strictly limited to **Davidson Chapter 29: Stroke medicine**.
- Do **not** mix Chapter 28 Neurology topics into the stroke workflow.
- Treat Stroke Medicine as a separate live chapter system with its own MOC, heading hubs, and disease-level files.

## Live files to read before choosing the next batch
1. `Stroke Medicine/Stroke Medicine MOC.md`
2. Relevant heading hub(s), especially the current unfinished heading
3. `Stroke Medicine/Davidson Chapter 29 - Stroke Medicine Hierarchy.md` when counts or structure need rechecking

## Exact `next N` continuation rule
For short continuation prompts like `next 1`, `next 2`, `next 3`, or `next 5`:
1. Re-read the live MOC first; do not rely on prior chat counts alone.
2. Inspect the relevant heading hub(s) to find the next uncompleted disease-level scaffold files.
3. Upgrade **exactly N** existing scaffold notes in place.
4. Update both navigation layers:
   - `Stroke Medicine MOC.md`
   - the relevant heading hub(s)
5. If a scaffold became a full note, mark it clearly as `✅ full-note` in the hub/MOC style already used in the vault.
6. Commit and push **only** the stroke-related files changed in that batch if the channel rules require git after each completed batch/session.

## Minimal-read override proven in session
If the user explicitly narrows the read scope (for example: `Read only Stroke Medicine MOC + target note + max 1 relevant hub`), treat that as a hard operational constraint, not a suggestion.

### Allowed working set for a single targeted stroke upgrade
- `Stroke Medicine/Stroke Medicine MOC.md`
- the target disease-level note
- at most **one** directly relevant heading hub or topic-group hub

If more context would actually be required to choose safely, **stop and ask** rather than silently reading extra files.

### If the user asks only for the next topic name/path
For prompts like `give me next 1 topic`, identify the next pending topic from the live MOC plus at most one relevant hub and reply with just:
- note title
- path

Do not widen into note-writing, navigation edits, or git work unless asked.

### If a constrained `next N` cannot be satisfied safely
If the user requests `next 2` or similar but the allowed MOC + hub scope exposes only one safe next pending topic, say so clearly and ask for permission to read one more relevant hub instead of guessing the second topic.

## Reporting rule
- Report the exact files upgraded in the batch.
- Recount the batch size before replying so the summary does not claim `next 5` when 6 topics were actually upgraded.
- Report progress from the live MOC/hub state rather than from stale remembered totals.
- Distinguish **topic-count** from **file-count** in the final summary: a `next 5` batch may legitimately produce more than 5 changed files because the 5 upgraded disease-level notes are accompanied by MOC and heading-hub updates.

## Practical verification note
- When counting completed entries from `Stroke Medicine MOC.md` via terminal snippets, prefer `python3` rather than `python` in this environment, or use a shell fallback such as `grep`/`awk`. Do not assume a bare `python` executable exists.

## Note-content standard for upgraded stroke notes
Each upgraded disease-level stroke note should include:
- exam-focused management
- red flags / emergencies
- one-page summary
- exactly 10 MCQs
- exactly 10 SBAs
- flashcards

## Preferred topic-order heuristic
- Continue within the same heading/topic-group when there is an obvious unfinished sequence.
- Use the live MOC and heading hubs as the source of truth for what remains.
- Good stroke-session sequences already proven in practice: Reperfusion Therapy cluster → Stroke Unit Care and Complications cluster → Secondary Prevention cluster.

## Git scope rule for stroke batches
- Stage only the stroke files changed in the batch, typically:
  - upgraded disease-level note files
  - `Stroke Medicine/Stroke Medicine MOC.md`
  - the relevant heading hub(s)
- Do not include unrelated repo changes.
- After push, verify the outcome with both:
  1. successful commit/push output
  2. `git status --short -- 'Stroke Medicine'` is clean

## Progress-count note
- This chapter tree was previously counted at **86 disease-level topics**.
- Use the live `Stroke Medicine MOC.md` completed markers as the primary source of truth for completed-vs-left reporting.
- If transcript history and file state disagree, trust the live MOC and heading hubs after verification.

## Pitfalls proven in session
- Overrunning the requested batch size because adjacent topics looked convenient.
- Reporting progress from chat memory instead of re-reading the MOC.
- Forgetting that stroke has its own chapter boundary and should not absorb Neurology topics.
- Staging a broad repo commit instead of a stroke-path-scoped commit.
