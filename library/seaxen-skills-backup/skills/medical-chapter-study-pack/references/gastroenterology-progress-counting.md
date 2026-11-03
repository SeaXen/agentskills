# Gastroenterology progress counting and completion-state guardrails

## Why this reference exists
In the live Chapter 23 workflow, counting `✅` links directly from `Gastroenterology MOC.md` overstated completion because the same topic was listed in multiple sections.

## Proven pitfall
- `✅` markers in the MOC are useful for navigation.
- They are **not** a reliable unique-topic counter when topics are duplicated across sections such as:
  - suggested conversion queue
  - completed full topic notes
  - heading-specific completion blocks

## Recommended counting workflow
1. Get the chapter total from the live chapter summary or validated disease-level file total.
2. Count actual upgraded topic files across the chapter tree using frontmatter status markers, especially:
   - `status: full-fcps-mrcp-topic-note`
   - `status: scaffold`
3. Compute:
   - completed = number of full-topic-note files
   - left = number of scaffold files
4. Only report `completed / total` after checking these counts agree.

## Completion-state guardrail
Do **not** switch the chapter MOC to a completion state such as `first-pass-full-note-complete`, and do **not** write `111 / 111`-style summaries, unless the whole-tree scaffold search is zero.

## How to talk about the mismatch
If the user asked for counts and the MOC `✅` count differs from file-status counts, say so explicitly:
- MOC `✅` count = navigation markers, may include duplicates
- file-status count = real unique completed topic files

## Session-proven example
A Chapter 23 pass produced misleading MOC counts like `93 complete / 18 left`, then later `129` `✅` links, while the true file-based state was:
- total disease-level topic files: `111`
- completed full topic files: `71`
- remaining scaffold files: `40`

Use this pattern whenever MOC sections duplicate the same topic links.
