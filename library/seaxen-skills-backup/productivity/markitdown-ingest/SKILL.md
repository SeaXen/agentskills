---
name: markitdown-ingest
description: Use when converting local documents into Obsidian markdown notes through the MarkItDown bridge on this machine.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [markitdown, obsidian, ingestion, local-documents, rag]
    related_skills: [ocr-and-documents, powerpoint, obsidian, hermes-agent]
---

# MarkItDown Ingest

## Overview
This skill covers the small local bridge that turns local files into markdown notes inside the Obsidian vault.

It uses the already-installed MarkItDown runtime here:
- runtime binary: `/mnt/tb/hermes/venvs/markitdown/bin/markitdown`
- wrapper: `/mnt/tb/hermes/scripts/obsidian-ingest.sh`
- importer: `/mnt/tb/hermes/scripts/obsidian_ingest.py`
- default destination: `Knowledge/Imported`

This is for local files. For URLs and web pages, prefer Hermes web extraction tools instead of this workflow.

See `references/examples.md` for copy-paste command examples.

## When to Use
Use this skill when:
- the user wants to ingest a local PDF, DOCX, PPTX, XLSX, EPUB, TXT, HTML, CSV, JSON, or XML file into Obsidian
- the user wants batch import from a local folder
- the user wants raw markdown staging for later RAG or note cleanup

Do not use this skill when:
- the source is a web URL
- the user only wants quick text from a remote PDF or website
- a different specialized workflow is better, such as OCR-heavy PDF work or PowerPoint editing

## Current Bridge
Flow:
1. Hermes runs `/mnt/tb/hermes/scripts/obsidian-ingest.sh`
2. wrapper calls `/mnt/tb/hermes/scripts/obsidian_ingest.py`
3. importer calls the MarkItDown CLI
4. markdown note is written into the Obsidian vault

## Supported Inputs
- PDF
- DOCX
- PPTX
- XLSX / XLS
- CSV
- JSON
- XML
- HTML / HTM
- TXT
- EPUB

## Commands
### Single file
```bash
/mnt/tb/hermes/scripts/obsidian-ingest.sh /path/to/file.pdf
```

### Recursive folder ingest
```bash
/mnt/tb/hermes/scripts/obsidian-ingest.sh --recursive /path/to/folder
```

### Custom tag
```bash
/mnt/tb/hermes/scripts/obsidian-ingest.sh --tag lecture-notes /path/to/file.docx
```

### Custom destination folder
```bash
/mnt/tb/hermes/scripts/obsidian-ingest.sh --folder Knowledge/Imported /path/to/file.pdf
```

## Output Behavior
- default output folder: `Knowledge/Imported`
- one note per source file
- filenames use source stem plus extension, such as `lecture-pdf.md`
- collisions get `-2`, `-3`, and so on
- frontmatter includes source path, source filename, source extension, import time, converter, and tags

## Quick Checks
```bash
/mnt/tb/hermes/scripts/obsidian-ingest.sh --help
python3 -m py_compile /mnt/tb/hermes/scripts/obsidian_ingest.py
/mnt/tb/hermes/venvs/markitdown/bin/markitdown --version
```

## Common Pitfalls
1. Using this for URLs.
   - Use Hermes `web_extract` for remote PDFs and websites.

2. Confusing the tracker repo with the runtime install.
   - tracking-only repo: `/root/.hermes/repos/markitdown`
   - live runtime: `/mnt/tb/hermes/venvs/markitdown`

3. Expecting perfect cleanup.
   - This is conversion, not final polishing. Imported markdown may still need manual cleanup.

4. Forgetting vault path assumptions.
   - The wrapper defaults `OBSIDIAN_VAULT_PATH` to `/mnt/tb/hermes/obsedianvault`.

5. Google Drive exports are already plain text.
   - After `public-google-drive-ingest` mirrors `.txt` under `/mnt/tb/Medicine/External/...`, use those files directly for study/MedSea pipelines, or run MarkItDown ingest only when the user wants the same content in Obsidian `Knowledge/Imported`.

## Verification Checklist
- [ ] MarkItDown binary exists at `/mnt/tb/hermes/venvs/markitdown/bin/markitdown`
- [ ] wrapper exists at `/mnt/tb/hermes/scripts/obsidian-ingest.sh`
- [ ] importer exists at `/mnt/tb/hermes/scripts/obsidian_ingest.py`
- [ ] output lands in `Knowledge/Imported` unless overridden
- [ ] imported note contains frontmatter and extracted body
