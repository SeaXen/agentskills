# Gastroenterology MOC patching pitfalls

## When to use this note
Use this when updating `Gastroenterology/Gastroenterology MOC.md` after a batch of topic-note upgrades, especially when the batch spans more than one hub.

## Proven failure mode
A patch can insert newly completed topics twice when the anchor block is too broad and already contains repeated nearby entries from the same hub or section.

Observed session pattern:
- Mixed-hub gastro batch completed normally.
- MOC summary counts were patched correctly.
- Completed-topic insertions for the IBD section matched a broad anchor that also contained existing adjacent IBD completions.
- Result: the new completed lines were duplicated in the `Suggested First Full-Note Conversion Queue` area.

## Safer patch pattern
1. Re-read the exact MOC slice around the intended insertion point before patching.
2. Anchor on the last already-completed topic from the same hub block, or another uniquely identifying local run of lines.
3. Avoid anchoring on a short block that could also match a repeated cluster elsewhere in the completed lists.
4. After patching, re-read the affected slice and check for immediate duplicates before git work.

## Recovery pattern if duplication happened
1. Re-read the affected MOC region.
2. Remove only the duplicate inserted lines.
3. Re-check the hub note(s) to ensure the checkmarks still match the intended batch.
4. Recompute progress from real file statuses:
   - `^status:\s*full-fcps-mrcp-topic-note$`
   - `^status:\s*scaffold$`
5. Only then proceed to git add/commit/push.

## Important rule
Navigation lists in the MOC are helpful for visibility but are not the authoritative progress denominator. Real topic-file frontmatter statuses remain the source of truth for completed-versus-remaining counts.
