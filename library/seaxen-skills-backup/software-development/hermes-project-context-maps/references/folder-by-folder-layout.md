# Folder-by-folder INDEX.md layout

Use this pattern when the user wants a Hermes-friendly navigation map for a large tree.

## Rules
- Treat `INDEX.md` as navigation only; keep instructions in `AGENTS.md`/`.hermes.md`/`CLAUDE.md`.
- Canonicalize the root path before writing. If the visible path is a symlink, write the real path in the file and mention the alias if useful.
- Prefer a shallow root map plus nested `INDEX.md` files in large or important subtrees.
- When the user asks for folder-by-folder, group by top-level folder and list the key files inside each folder.
- Include a short `Purpose:` line for each section.
- Keep lockfiles, caches, backups, and generated artifacts out unless they matter for debugging.
- Put `INDEX.md` near the top of each section so the agent sees the map before random files.

## Good split
- Root `INDEX.md`: top-level map and pointers to nested indexes.
- `skills/INDEX.md`: skills tree.
- `plugins/INDEX.md`: plugin tree.
- `repos/INDEX.md`: repository tree.

## Good section content
- `Root files`
- `## <folder>/`
- `- Purpose: ...`
- `- See: <nested INDEX.md>` when the folder has its own map.
- `- Key files:` with only the important files or entry points.

## Pitfalls
- Don’t dump every file in very large trees if the result becomes unreadable.
- Don’t mix repo instructions into the index.
- Don’t leave the root index pointing nowhere if nested indexes exist.
- Don’t assume `/mnt/tb/hermes` and `/root/.hermes` are different trees without checking the canonical path.
