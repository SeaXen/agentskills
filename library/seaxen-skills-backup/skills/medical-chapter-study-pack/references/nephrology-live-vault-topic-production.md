# Nephrology Live Vault Topic Production Workflow

Use this when the user wants a nephrology topic produced both in chat and as a real Obsidian note in the medicine vault.

## Proven session pattern
- Root vault: `/mnt/tb/Medicine`
- Chapter folder: `/mnt/tb/Medicine/Nephrology/`
- Existing topic-note convention may already use short clean filenames such as `AKI.md`, `CKD.md`.
- Existing navigation note: `Nephrology MOC.md`
- Repo may be a live Git repository with `origin` configured.

## Recommended steps
1. Inspect the chapter folder for existing `.md` files.
2. If the user provided a nephrology session-resume note, read it first and reconcile its queue against the live `Nephrology MOC.md` before choosing the next topic.
3. Inspect the target topic file first before writing, to avoid creating duplicates.
4. Inspect the chapter MOC/index before editing.
5. If a starter note exists, upgrade it in place.
6. Use Obsidian-friendly frontmatter plus wikilinks to related nephrology notes.
7. After writing the topic file, update `Nephrology MOC.md` so the topic is visible from the chapter index.
8. If the topic also appears in a nephrology topic-group hub or the chapter hierarchy note, mark completion there too so navigation reflects the upgrade at every layer.
9. If a nephrology session-resume note is in use, update it after the batch to mark completion and refresh the recommended safe next command.
10. If requested — or if the nephrology channel rules make git push mandatory after each completed batch — run path-scoped Git workflow from the vault root using only the nephrology files changed in that batch (plus the nephrology resume note if edited):
   - `git -C /mnt/tb/Medicine add ...`
   - `git -C /mnt/tb/Medicine commit -m "docs(nephrology): ..."`
   - `git -C /mnt/tb/Medicine push origin main`
11. After push, verify `git status --short -- Nephrology 00_Index/'Nephrology Channel Session Resume <date>.md'` is clean.

## Pitfalls
- Do not create a second file with a different title if `AKI.md` or another established topic filename already exists.
- Do not only answer in chat when the user asked for real note production.
- Do not skip MOC maintenance when the chapter index is part of the workflow.
- Do not assume Git push unless the user requested it; but if requested, verify repo state and remote first.
