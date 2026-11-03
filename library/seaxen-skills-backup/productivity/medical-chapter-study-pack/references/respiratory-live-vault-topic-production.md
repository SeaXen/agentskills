# Respiratory Live Vault Topic Production

Use this pattern when the user wants a **real respiratory topic note** created/updated under `/mnt/tb/Medicine/Respiratory/` and also asks for repo sync.

## Proven workflow
1. Inspect the existing topic file and `Respiratory MOC.md` first.
2. Reuse the established clean filename, e.g. `COPD.md`, `Bronchiectasis.md`.
3. Upgrade starter notes in place rather than creating duplicates.
4. Keep the note Obsidian-friendly with frontmatter, wikilinks, exam tags, and chapter metadata.
5. For this user's respiratory notes, default source split is:
   - Anatomy: Gray's Anatomy + Davidson
   - Physiology: Ganong + Guyton & Hall + Davidson
   - Clinical discussion: Davidson + PasTest + personal notes
6. In respiratory notes, reliably include high-yield interpretation and bedside sections when relevant:
   - spirometry patterns
   - ABG interpretation
   - oxygen therapy cautions
   - differential diagnosis with asthma/COPD/TB/bronchiectasis overlap where applicable
7. If a topic becomes a full exam-ready note, update `Respiratory MOC.md` in place and annotate the topic line clearly, e.g. `[[COPD]] — full FCPS/MRCP note updated`.
8. Before git work, run `git status --short`.
9. If unrelated repo changes exist, use **path-specific staging only** for the respiratory topic file and any directly related MOC/index files touched in that task.
10. If the user explicitly asked for git sync, run:
    - `git add -- <topic-file> <moc-file>`
    - `git commit -m "Add full FCPS/MRCP <topic> respiratory note"`
    - `git push origin HEAD`
11. Verify final repo state and report any unrelated modified/untracked files left untouched.

## Pitfalls
- Do not sweep unrelated repo changes into the respiratory topic commit.
- Do not leave the note as a starter template when the user asked for a full FCPS/MRCP note.
- Do not forget MOC visibility updates after promoting a starter note to a full note.
- Do not skip the git push when the user explicitly requested add/commit/push and authentication is already working.

## Good commit style
- `Add full FCPS/MRCP COPD respiratory note`
- `Add full FCPS/MRCP bronchiectasis respiratory note`

## Verification
- Topic file saved under `/mnt/tb/Medicine/Respiratory/`
- `status: full-note` in frontmatter when appropriate
- Respiratory MOC updated if note was promoted from starter to full
- Only task-related files staged
- Commit and push succeeded
- Final reply mentions any unrelated pending repo changes
