# Local document ingestion staging pattern

Use this when the user wants a low-risk local Obsidian/RAG ingestion path without MCP.

## Goal
Convert local office/docs files into markdown notes inside the vault while keeping Hermes hot memory and main runtime clean.

## Recommended shape
- dedicated venv for converter tooling
- wrapper shell script for easy repeated use
- Python importer script that:
  - accepts files/folders
  - supports recursive import
  - filters to supported extensions
  - converts one source file at a time
  - writes one vault note per source file
  - emits explicit `OK source -> target` lines for verification
- staging destination: `Inbox/Imports/`
- companion note: `[[Imports]]`

## Frontmatter fields worth keeping
- `title`
- `source_path`
- `source_filename`
- `source_extension`
- `imported_at`
- `converter`
- `tags`

## Naming rule
Use `stem + extension` in output filenames, not stem alone.

Example:
- `lecture.pdf` -> `lecture-pdf.md`
- `lecture.docx` -> `lecture-docx.md`

Reason: different source formats often share the same base name.

## Review/promotion rule
- raw imports stay in staging
- distilled notes move later into `Knowledge/` or `Work/`
- do not dump imports directly into polished folders by default

## Path-alias verification rule
If imports appear under a different absolute path than expected, verify whether the display path and resolved path are the samefile before treating it as a bug.

Example class:
- display path: `/mnt/tb/hermes/obsedianvault`
- resolved path: `/root/.hermes/obsedianvault`
- if `samefile == true`, imports landed correctly in the same live vault

## Minimal verification checklist
- importer script compiles
- wrapper script is executable
- `--help` works
- converter version prints
- one sample import lands in `Inbox/Imports/`
- resulting note contains frontmatter + converted body
