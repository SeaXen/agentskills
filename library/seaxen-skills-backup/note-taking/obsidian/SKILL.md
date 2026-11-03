---
name: obsidian
description: Read, search, create, and edit notes in the Obsidian vault.
platforms: [linux, macos, windows]
---

# Obsidian Vault

Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks.

## Vault path

Use a known or resolved vault path before calling file tools.

The documented vault-path convention is the `OBSIDIAN_VAULT_PATH` environment variable, for example from `~/.hermes/.env`. If it is unset, use `~/Documents/Obsidian Vault`.

File tools do not expand shell variables. Do not pass paths containing `$OBSIDIAN_VAULT_PATH` to `read_file`, `write_file`, `patch`, or `search_files`; resolve the vault path first and pass a concrete absolute path. Vault paths may contain spaces, which is another reason to prefer file tools over shell commands.

If the vault path is unknown, `terminal` is acceptable for resolving `OBSIDIAN_VAULT_PATH` or checking whether the fallback path exists. Once the path is known, switch back to file tools.

## Read a note

Use `read_file` with the resolved absolute path to the note. Prefer this over `cat` because it provides line numbers and pagination.

## List notes

Use `search_files` with `target: "files"` and the resolved vault path. Prefer this over `find` or `ls`.

- To list all markdown notes, use `pattern: "*.md"` under the vault path.
- To list a subfolder, search under that subfolder's absolute path.

## Search

Use `search_files` for both filename and content searches. Prefer this over `grep`, `find`, or `ls`.

- For filenames, use `search_files` with `target: "files"` and a filename `pattern`.
- For note contents, use `search_files` with `target: "content"`, the content regex as `pattern`, and `file_glob: "*.md"` when you want to restrict matches to markdown notes.

## Create a note

Use `write_file` with the resolved absolute path and the full markdown content. Prefer this over shell heredocs or `echo` because it avoids shell quoting issues and returns structured results.

## Append to a note

Prefer a native file-tool workflow when it is not awkward:

- Read the target note with `read_file`.
- Use `patch` for an anchored append when there is stable context, such as adding a section after an existing heading or appending before a known trailing block.
- Use `write_file` when rewriting the whole note is clearer than constructing a fragile patch.

For an anchored append with `patch`, replace the anchor with the anchor plus the new content.

For a simple append with no stable context, `terminal` is acceptable if it is the clearest safe option.

## Targeted edits

Use `patch` for focused note changes when the current content gives you stable context. Prefer this over shell text rewriting.

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## Hermes memory-vault workflow

When the user asks to connect Hermes memory to Obsidian, prefer a low-noise three-tier setup: hot Hermes memory stays small, Obsidian stores warm/cold long-form context, and daily notes/logs capture only important decisions, fixes, conclusions, and project state changes. Do not auto-dump every chat unless explicitly requested.

Use `AGENT.md` as the vault entry point, add a human dashboard (`Dashboard.md`), keep core context under `System/Assistant/`, durable decisions under `Memory/decisions.md`, reusable guides under `Knowledge/`, active projects under `Work/`, and append-only important events under `Daily/YYYY-MM-DD.md`.

For a live dashboard, install/enable the Obsidian Dataview community plugin in the vault and add Dataview query blocks. See `references/hermes-memory-vault-pattern.md` for the full structure, dashboard blocks, Dataview install commands, and vault-move checklist.

## Hermes memory vault pattern

When the user asks whether Obsidian can help Hermes memory, continuity, token use, path finding, or graph/dashboard views, use the low-noise three-tier pattern in `references/hermes-memory-vault-pattern.md`.

Key rules:

- Keep Hermes built-in `USER.md` / `MEMORY.md` as lean hot memory.
- Use Obsidian as warm/cold memory: project context, decisions, fixes, research, daily important logs.
- Do not imply file-level Obsidian access is automatic live sync or auto-injected context.
- Prefer manual structured capture first; add cron/distillation only after useful notes accumulate.
- Recommend dashboard/index notes and optional Dataview blocks for human graph/dashboard views.
