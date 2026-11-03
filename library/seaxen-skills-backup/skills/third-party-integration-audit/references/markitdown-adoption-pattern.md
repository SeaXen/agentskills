# MarkItDown adoption pattern for Hermes/Obsidian

Use when a user asks whether a GitHub repo like `microsoft/markitdown` is actually needed.

## Practical framing

Do not answer from README alone. First compare against what the user already has.

For Hermes-like stacks:
- existing web extraction may already cover URLs and many remote PDFs well
- the missing gap is often **local office-document to Markdown** ingestion
- the relevant decision is whether that local-ingestion gap happens often enough to justify another tool

## Recommendation pattern

Good fit when the user repeatedly needs:
- local `.docx` → Markdown
- local `.pptx` → Markdown
- local `.xlsx` / `.xls` → Markdown/text extraction
- local PDFs converted into note-friendly Markdown for Obsidian/RAG

Probably unnecessary when the user mostly needs:
- web pages
- direct URLs
- remote PDFs already handled by current extraction flow
- occasional one-off local docs where manual copy/paste is cheaper

## Install stance

Prefer:
- isolated venv
- package install only
- no repo clone

Clone the repo only if you need to:
- patch source
- inspect unreleased behavior not visible from hosted files
- run tests or local development workflows

## Local workflow pattern that worked

A durable low-risk setup:
- install `markitdown[...]` into a dedicated venv
- keep it outside the main Hermes runtime
- wrap it with a small importer script + shell entrypoint
- write converted notes into the live Obsidian vault with frontmatter for source path, extension, import time, converter, and tags
- choose a clean target folder such as `Knowledge/Imported` rather than an inbox-looking dump path if the user wants a tidier knowledge base

## User-facing verdict shape

Use plain language:
- "You do not need the repo itself."
- "You only need the package if local document ingestion is a recurring workflow."
- "If you mostly ingest web pages and remote PDFs, your current stack already covers most of that."
