#!/usr/bin/env python3
"""
split_textbook_by_chapters.py — generic textbook splitter.

For a printed textbook PDF with NO embedded TOC, this script:
  1) Reads the configured (chapter_number, title, listing_page) list
  2) Writes one PDF per chapter + a front-matter PDF + an index JSON

Usage:
  1. Open the source PDF, find each chapter's listing page (1-indexed).
  2. Fill in CHAPTERS below.
  3. Run: /usr/local/lib/hermes-agent/venv/bin/python split_textbook_by_chapters.py
"""

import pymupdf as fitz
import os
import re
import json

# === CONFIG — fill these in for your book ===
SRC = "/path/to/book.pdf"
DST = "/path/to/output_dir"
CHAPTERS = [
    # (n, title, listing_pdf_page_1indexed)
    (1,  "Chapter one title",                15),
    (2,  "Chapter two title",                27),
    # ...
]
FRONT_MATTER_END = CHAPTERS[0][2] - 1   # last front-matter PDF page (1-indexed, inclusive)
# ============================================


def safe(name: str) -> str:
    return re.sub(r"[^\w\s\-]", "", name).strip().replace(" ", "_")


def main():
    os.makedirs(DST, exist_ok=True)
    doc = fitz.open(SRC)
    total = doc.page_count

    if doc.get_toc():
        print("WARNING: PDF has an embedded TOC. This script is for books without one.")
        print("You can usually just walk doc.get_toc() and insert_pdf per entry instead.")

    # Build ranges
    items = []
    for i, (n, title, start) in enumerate(CHAPTERS):
        end = CHAPTERS[i + 1][2] - 1 if i + 1 < len(CHAPTERS) else total
        items.append((n, title, start, end))

    # Front matter
    print(f"Writing front matter (PDF p1–p{FRONT_MATTER_END})...")
    front = fitz.open()
    front.insert_pdf(doc, from_page=0, to_page=FRONT_MATTER_END - 1)
    front.save(os.path.join(DST, "00_Front_Matter.pdf"))
    front.close()

    # Chapters
    for n, title, start, end in items:
        fname = f"{n:02d}_Ch{n:02d}_{safe(title)}.pdf"
        fpath = os.path.join(DST, fname)
        print(f"Ch {n:>2}  PDF p{start}–p{end}  ({end - start + 1} pages)  -> {fname}")
        out = fitz.open()
        out.insert_pdf(doc, from_page=start - 1, to_page=end - 1)
        out.save(fpath)
        out.close()

    # Index
    with open(os.path.join(DST, "_chapters_index.json"), "w") as f:
        json.dump({
            "source": SRC,
            "total_pdf_pages": total,
            "front_matter": {"start": 1, "end": FRONT_MATTER_END, "pages": FRONT_MATTER_END},
            "chapters": [
                {"n": n, "title": t, "start": s, "end": e, "pages": e - s + 1}
                for n, t, s, e in items
            ],
        }, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {len(items) + 1} files in {DST}")


if __name__ == "__main__":
    main()
