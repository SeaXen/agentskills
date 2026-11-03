---
name: pdf-textbook-chapter-splitter
description: Split a large printed-textbook PDF into per-chapter PDFs when the source has no embedded PDF TOC (doc.get_toc() == 0). Use when the user wants a textbook divided into chapter PDFs, e.g. "divide this book into individual chapter PDFs". Works by parsing the printed contents pages, locating each chapter's listing page in the PDF body, computing ranges, and writing one PDF per chapter + a front-matter PDF + an index JSON. Includes a reusable splitter script and a reference mapping for Davidson's 25th edition.
---

# pdf-textbook-chapter-splitter

## When to use

- User asks to split / divide / extract chapters from a textbook PDF.
- `pymupdf` `doc.get_toc()` returns 0 (no embedded bookmarks) — most scanned or typeset medical textbooks behave this way.
- The book has a printed contents page (chapter list with title + starting printed page number).
- You need one PDF per chapter, not just text extraction.

## When NOT to use

- PDF already has a usable embedded TOC → just walk `doc.get_toc()` and `insert_pdf` directly, no detection needed.
- User only wants text per chapter (not separate PDFs) → use `ocr-and-documents` / `pymupdf` text extraction directly.
- User wants OCR on a scanned book → different problem.

## Setup

```bash
# pymupdf is in the hermes-agent venv at /usr/local/lib/hermes-agent/venv/bin/python
/usr/local/lib/hermes-agent/venv/bin/python -m pip install pymupdf
```

System pip is PEP 668 locked (Debian) — always use the venv python.

## Workflow

1. **Open the PDF and verify no embedded TOC**
   ```python
   import pymupdf as fitz
   doc = fitz.open(SRC)
   assert doc.get_toc() == 0, "PDF has embedded TOC — use it instead of this skill"
   ```

2. **Extract the printed TOC text** — usually PDF pages 5–7 for medical textbooks (after cover, copyright, contents header). Read the contents pages manually to get:
   - chapter number, exact title, printed starting page
   - part/section headers if they exist (Part 1, Part 2 …)

3. **Build chapter list** as `(n, title, printed_start_page)`.

4. **Locate each chapter's listing page in the PDF** (the page where the chapter title appears as a heading, typically listing the chapter's sections).
   - **Normalize whitespace**: chapter titles often wrap across 2 lines on the listing page (e.g. `"Acute medicine and / critical illness"`). Use `re.sub(r"\s+", " ", s).strip().lower()` and check containment, not exact match.
   - **Search only the first ~30 lines** of each page — listing content is at the top of the chapter-opening page, and the title also appears in cross-references and running headers later.
   - **Skip the first ~12–14 pages** (front matter: cover, copyright, contents, contributors, preface) — start scanning from page index 13.
   - Take the **first match per chapter**.

5. **Verify with running headers** — every body page has a header like `12  • POISONING` or `POISONING  •  12`. Parse with regex and build a printed→PDF page offset map. The header offset should grow slowly from front to back (~14 at front, ~48 at end for a 1400-page medical textbook). If the offset between adjacent chapters changes drastically, the listing-page detection is wrong.

6. **Compute ranges**: chapter N ends at `(chapter N+1 start) - 1`; last chapter ends at `doc.page_count`.

7. **Write output**:
   - `00_Front_Matter.pdf` — cover through last preface page (`start_page = 1`, `end_page = chapter1_start - 1`)
   - `01_Ch01_<safe_title>.pdf` … `NN_ChNN_<safe_title>.pdf` — one per chapter
   - `_chapters_index.json` — chapter→range mapping for future reference

   Use `fitz.open().insert_pdf(doc, from_page=start-1, to_page=end-1)` for zero-loss extraction (no rasterization).

## Pitfalls

- **Printed page ≠ PDF page.** Always probe with known anchors first (e.g. for Davidson 25e, the chapter 1 printed page "2" is at PDF page 16, offset = 14).
- **Title matching by exact line fails** when titles wrap. Normalize whitespace and search the first 30 lines of each page as one big string.
- **First-match wins** — running headers contain the chapter title on every page, so `doc[p].get_text().find(title)` will hit hundreds of false positives. Restrict to the first 30 lines of pages from index 13 onward.
- **Front matter pages contain titles** in the printed TOC — start scanning AFTER the front matter (page index 13+ is a safe default for medical textbooks).
- **Some chapters wrap titles awkwardly** on the listing page (verified in Davidson 25e for Ch 2, 6, 9, 10, 12, 24). Whitespace normalization handles all of these.
- **Book has subsections like Part 1 / Part 2** — preserve them as separate "section divider" PDFs only if the user wants; default is one PDF per numbered chapter.
- **File names** — sanitize: `re.sub(r"[^\w\s\-]", "", name).replace(" ", "_")`.

## Files in this skill

- `scripts/split_textbook_by_chapters.py` — generic splitter template (fill in the chapter list, run).
- `references/davidson-25e-chapter-mapping.md` — verified chapter→PDF page map for Davidson's Principles and Practice of Medicine 25th edition (1,409 pages, 33 chapters). Pre-built if anyone needs to regenerate.
