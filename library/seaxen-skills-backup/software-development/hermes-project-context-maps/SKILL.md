---
name: hermes-project-context-maps
description: Create and maintain Hermes-friendly project context maps, including folder-by-folder INDEX.md navigation files and instruction-only AGENTS.md files.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  tags: [hermes, context-files, index, agents-md, repository-navigation, documentation]
---

# Hermes Project Context Maps

Use this skill when a user wants a repo or workspace made easier for Hermes to navigate, especially when they ask for:
- an `INDEX.md` file
- a folder-by-folder file map
- a Hermes-friendly project tree
- the difference between `INDEX.md` and `AGENTS.md`
- a documentation layout that helps agents find files faster

## Core principle

Split the problem into two separate artifacts:

1. **`INDEX.md`** — navigation only
   - folder map
   - file map
   - where to start
   - what lives where
   - deprecated / ignore areas

2. **`AGENTS.md` / `.hermes.md` / `CLAUDE.md`** — instructions only
   - architecture
   - conventions
   - build/test commands
   - special repo rules
   - agent behavior hints

Do not mix the two unless the user explicitly wants a hybrid document.

## Decision rules

- If the user asks “where are the files?”, create or update `INDEX.md`.
- If the user asks “how should Hermes work here?”, create or update `AGENTS.md`.
- If the user asks for both, keep them separate by default.
- If the root path is a symlink, canonicalize it before writing and mention the real path.
- Default shape for large trees: **one strong root `INDEX.md` plus a few nested indexes only for major subtrees**. Do **not** spray `INDEX.md` into every directory unless the user explicitly insists after you warn about the clutter.
- If the workspace is huge, prefer a summarized root map over a literal full recursive dump. A single mega-index across tens of thousands of directories becomes too large to help Hermes.
- Before doing recursive per-directory index generation, quantify the tree size first and explain the tradeoff: one root map vs selected nested maps vs full recursion.

## How Hermes uses `INDEX.md`

- `INDEX.md` is **not** auto-loaded into memory and **not** a built-in Hermes feature.
- It helps only when the agent **reads** it during a task.
- Prefer **curated, short** maps over exhaustive dumps.

## Dr. Sagar / DietPi defaults (2026-07)

- **Do not edit `AGENTS.md`** for navigation-only index work unless explicitly asked.
- Keep `/mnt/tb/INDEX.md` (curated disk map), `/root/.hermes/INDEX.md`, and nested `skills/`, `plugins/`, `repos/` indexes — not per-folder indexes under all of `/mnt/tb`.
- Weekly `no_agent` cron: `refresh_mnt_tb_index.py`, `refresh_hermes_indexes.py` — see `references/curated-index-cron-and-layout.md`.

## Recommended `INDEX.md` structure

Prefer a **folder-by-folder** layout over a flat list when the tree is non-trivial.

Suggested sections:
- `# <Project> INDEX`
- `Root: /absolute/path`
- brief note explaining the file is for navigation only
- `## Root files`
- one `## <folder>/` section per top-level directory
- nested bullet lists for subfolders and files
- `README`, `AGENTS.md`, `INDEX.md`, and entry-point files near the top of each section
- a short `Start here` / `Common tasks` note when useful
- when the tree is large, split `skills/`, `plugins/`, and `repos/` into their own nested `INDEX.md` files and have the root index point to them

Keep the document readable. If the tree is huge, prefer a shallow map with the most relevant levels rather than an unreadable dump.

See `references/folder-by-folder-layout.md` for the compact pattern used in this session.
See `references/large-tree-index-scaling.md` for the large-workspace decision rule: root map vs selected nested maps vs full recursion.

## Recommended `AGENTS.md` structure

Use `AGENTS.md` for agent instructions, not file inventory.

Typical sections:
- project purpose
- architecture
- conventions
- build / test / run commands
- important paths
- gotchas / ignored directories
- any repo-specific invariants

## Workflow

1. Inspect the live filesystem.
2. Canonicalize the target root.
3. Decide whether the user wants navigation (`INDEX.md`) or instructions (`AGENTS.md`).
4. Generate the file in the requested style.
5. Verify the file was written and read back correctly.
6. If a symlink path exists, note both the canonical path and the alias path if relevant.

## Verification

Always verify with a real readback after writing:
- confirm the file path
- confirm the top of the file looks right
- confirm the sectioning matches the requested style

## Pitfalls

- Don’t treat `INDEX.md` as a special Hermes config file; it is a convention.
- Don’t edit `AGENTS.md` when the task is navigation-only.
- Don’t bury instructions inside a giant file map.
- Don’t use a flat tree when the user specifically asked for folder-by-folder.
- Don’t assume the visible path is the canonical path.
- Don’t claim the file is ready until it has been read back from disk.
- Don’t default to writing `INDEX.md` into every folder. For most repos/workspaces that is clutter, not signal.
- Don’t mistake “I want one index that maps everything” for “generate one file in every directory.” Clarify that distinction and recommend the minimal useful set: root index + a few major subtree indexes.

## References

- `references/index-vs-agents.md` — concise distinction between navigation maps and instruction files.
- `references/folder-by-folder-layout.md` — example layout pattern for large trees.
- `references/verifying-canonical-paths.md` — path canonicalization and symlink handling notes.
- `references/curated-index-cron-and-layout.md` — minimal INDEX set, weekly scripts/cron, `/mnt/tb` exclusions on this host.
