# Neurology Live Vault Topic Production

Use this reference when the user is producing real Neurology notes inside the medicine vault.

## Scope rules

- Folder root: `/mnt/tb/Medicine/Neurology/`
- Chapter boundary: **Davidson Chapter 28: Neurology only**
- Exclude **Stroke** from Neurology work; it belongs to the separate Stroke Medicine chapter/folder.
- Core clinical source base: **Davidson + PasTest**
- Support references: **Gray's** for anatomy, **Guyton & Hall + Ganong** for physiology
- Style: elaborate, FCPS/MRCP-oriented, Obsidian-friendly Markdown

## Required topic features

When expanding a disease-level scaffold into a full note, include when relevant:
- localization
- neuroimaging interpretation
- CSF interpretation
- cut-offs / thresholds
- differential diagnosis
- management cautions
- red flags
- one-page revision summary
- recall prompts
- 10 MCQs
- 10 SBAs
- flashcards when possible

## Proven continuation workflow

1. Read the user's current setup note if they specify one, typically `00_Index/Neurology Channel Session Resume <date>.md`.
2. Read the current live `Neurology MOC.md` before choosing the next topics.
3. Reconcile the resume against the MOC because the resume may lag behind already-completed notes.
4. Select the next pending disease-level scaffold files already present in the validated Neurology hierarchy.
5. Upgrade those scaffold files **in place** rather than creating parallel duplicates.
6. After each batch, update `Neurology MOC.md`:
   - milestone/status line (for example `first-20-must-know-full-notes-completed`)
   - completed-note list
   - recently upgraded list
7. Also update the relevant heading hub notes by prefixing completed topic links with `✅`.
8. Verify the converted files contain the expected full-note status marker used by the vault.
9. Only run git add/commit/push if the user explicitly asks for repo update side effects.

## Navigation files commonly touched

- `Neurology MOC.md`
- `Davidson Chapter 28 - Neurology Hierarchy.md`
- heading hubs such as:
  - `Clinical Examination of the Nervous System.md`
  - `Epilepsy.md`
  - `Meningitis.md`
  - `Neuroimaging.md`
  - `Vestibular Disorders.md`

## Pitfalls

- Do not let generic neurology knowledge pull Stroke topics back into Neurology.
- Do not trust an old queue or resume note without checking the current MOC.
- Do not create duplicate filenames when a scaffold already exists.
- Do not report completion counts from a brittle regex if the MOC formatting has changed; count from the live completed entries or milestone block instead.
- Do not push git changes unless explicitly requested.
