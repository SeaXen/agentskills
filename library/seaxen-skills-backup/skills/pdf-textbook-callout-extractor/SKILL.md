---
name: pdf-textbook-callout-extractor
description: Extract numbered callout boxes (e.g. "1.1 Title", "10.6 Reason for X") from a textbook PDF and produce one PDF per chapter containing visual snapshots of every box. Use when the user says "extract all boxes", "per chapter box PDFs", "callouts", "highlighted boxes", or asks for visual crops of sidebar/key-point panels from a medical/scientific textbook PDF. The skill detects the heading pattern (number.title, NOT the "Box N.N" prefix that only appears in inline cross-references), determines each box's extent by column-flow, crops the page at high DPI, and assembles a chapter PDF. Built around Davidson 25e but generalizes to any textbook with `N.N Title` style callouts.
---

# pdf-textbook-callout-extractor

## When to use

- User wants to extract numbered callout boxes / key-point panels / sidebars from a textbook PDF.
- The callouts are labeled like `1.1 Title`, `10.6 Reason for X` — the number is `chapter.box`, NO "Box" prefix in the actual heading.
- User wants **visual snapshots** (crops of the original page) — not text recreations.
- User wants the output organized as **one PDF per chapter containing all that chapter's boxes**.

## When NOT to use

- User wants per-box individual files (`.md` or single-PDF) — confirm before producing; user often corrects this to per-chapter.
- User only wants the text content of boxes (no visual preservation) → use `ocr-and-documents` / pymupdf text extraction; no cropping needed.
- PDF has no chapter structure / no detectable callouts → escalate, don't fabricate.
- "Box" actually appears as a literal prefix in the heading (rare textbook style) → the heading regex needs to match `^Box\s+\d+\.\d+` instead.

## Setup

```bash
# pymupdf is in the hermes-agent venv at /usr/local/lib/hermes-agent/venv/bin/python
/usr/local/lib/hermes-agent/venv/bin/python -m pip install pymupdf
```

## Workflow

### 1. Confirm output format with the user BEFORE running

User commonly asks for "boxes per chapter as one PDF" but receives per-box files by mistake. Clarify:

- ✅ "one PDF per chapter containing all that chapter's boxes, each box as a cropped image snapshot" — this skill's default.
- ❌ per-box individual `.md` / `.pdf` files — only if user explicitly asks.

If unsure, ask. If user shows an image of the original textbook page with a highlighted box, they almost certainly want **visual snapshots**.

### 2. Load chapter ranges

The skill assumes you have a `_chapters_index.json` from `pdf-textbook-chapter-splitter` (or build the ranges manually). Each chapter needs `{n, title, start, end}` in PDF-page coordinates.

### 3. Detect box headings

The actual heading inside a box is `N.N Title text` — NOT `Box N.N Title`. The "Box" prefix only appears as an inline cross-reference in body text (e.g. "see Box 10.6"). Match this pattern per span, but the heading is typically split across multiple adjacent spans on the same line (e.g. span 1: `"1.1 "`, span 2: `"Root causes of diagnostic error"`). Concatenate:

```python
import re
import pymupdf as fitz

def find_box_headings(page, chapter_n):
    blocks = page.get_text("dict")["blocks"]
    candidates = []
    for b in blocks:
        if b.get("type") != 0:
            continue
        for line in b.get("lines", []):
            spans = sorted(line.get("spans", []), key=lambda s: s["bbox"][0])
            for i, span in enumerate(spans):
                text = span["text"].strip()
                m = re.match(r"^(\d+)\.(\d+)$", text)
                if not m:
                    continue
                ch_n, num = int(m.group(1)), int(m.group(2))
                if ch_n != chapter_n:
                    continue
                bx0, by0, bx1, by1 = span["bbox"]
                title_parts, last_x1 = [], bx1
                for j in range(i + 1, len(spans)):
                    ns = spans[j]
                    if abs(ns["bbox"][1] - by0) > 5:  # different line
                        break
                    if ns["bbox"][0] < bx1 - 5:  # left of N.N label
                        continue
                    title_parts.append(ns["text"].strip())
                    last_x1 = ns["bbox"][2]
                title = " ".join(p for p in title_parts if p).strip()
                # Real headings: title is > 3 chars and not sentence-ending
                if title and len(title) > 3 and not title.endswith("."):
                    candidates.append({
                        "ch": ch_n, "num": num, "title": title,
                        "bbox": (bx0, by0, last_x1, by1),
                    })
    return candidates
```

Filter to `(ch_n, num)` pairs within the chapter being processed — the same `1.1` pattern appears as inline references in body text on other chapters' pages, so without the chapter filter you'd pick up false positives.

### 4. Determine each box's vertical extent

Boxes are NOT bounded by vector borders in the PDF — they're just blocks of text. Extent comes from the next box in the same column:

```python
def column_of(x):
    return 0 if x < 300 else 1  # two-column layout; tune threshold per textbook

def determine_extent(page, bbox, next_box_bbox=None):
    x0, y0, x1, y1 = bbox
    col = column_of(x0)
    page_h = page.rect.height
    if next_box_bbox and column_of(next_box_bbox[0]) == col:
        return next_box_bbox[1] - 4  # stop 4pt above next box header
    # Otherwise: last text element in this column
    blocks = page.get_text("dict")["blocks"]
    last_y = y1 + 8
    for b in blocks:
        if b.get("type") != 0:
            continue
        for line in b.get("lines", []):
            for span in line.get("spans", []):
                sx0, sy0, sx1, sy1 = span["bbox"]
                if sy0 >= y0 and column_of(sx0) == col and sy1 < page_h - 25:
                    last_y = max(last_y, sy1)
    return min(last_y + 6, page_h - 20)
```

Per-page processing: sort boxes by `(column, y)`, then for each box look ahead to the next box in the same column.

### 5. Crop and render — use FULL COLUMN WIDTH, not heading-text width

**Critical pitfall (caught by user on Davidson 25e):** the box heading text starts at one x-position, but the table / box body often extends further left (the first column of a 2-column table starts at the left margin, NOT at where the heading text begins). If you crop to the heading-text bbox width, the box body and tables get clipped on the left edge.

Use the **full column width** for the box's horizontal extent:

```python
COL_BOUNDS = {
    0: (44, 300),   # left column x-range for Davidson 25e — tune per textbook
    1: (305, 562),  # right column x-range
}

col = column_of(bbox[0])
col_min, col_max = COL_BOUNDS[col]
rect = (col_min, bbox[1] - 8, col_max, bottom)
```

Measure `COL_BOUNDS` once per textbook by sampling a few pages and looking at where the body-text column actually lives (not where the heading sits). Davidson 25e uses roughly `(44, 300)` and `(305, 562)`; adjust for other textbooks.

**Pitfall:** `Page.insert_image()` does NOT accept a `clip` keyword. You must use `page.get_pixmap(clip=...)` first to render only the box region, then `insert_image` the resulting pixmap:

```python
DPI = 200
ZOOM = DPI / 72.0
mat = fitz.Matrix(ZOOM, ZOOM)

for b in boxes_for_this_page:
    rx0, ry0, rx1, ry1 = b["rect"]
    clip = fitz.Rect(rx0, ry0, rx1, ry1)
    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
    w_pt = rx1 - rx0
    h_pt = ry1 - ry0
    new_page = pdf.new_page(width=w_pt, height=h_pt)
    new_page.insert_image(new_page.rect, pixmap=pix)
```

Top padding (~8pt above heading) is fine — the heading starts at `y0`.

### 6. Assemble chapter PDFs

One PDF per chapter, file named `NN - All Boxes.pdf` placed inside the chapter folder. Boxes within a chapter are sorted by `(chapter, num)`.

## Pitfalls

- **Heading split across spans.** `get_text("dict")` returns each PDF text run as a separate span. The label `1.1` and the title text are separate spans on the same line. Naive regex `^N.N .+` on `span["text"]` misses every box. Always concatenate adjacent spans to the right.
- **`Box N.N` is the inline reference, not the heading.** In Davidson-style textbooks, the word "Box" appears only in body-text cross-references (e.g. "see Box 10.6"). Matching `Box \d+\.\d+` finds thousands of false positives. Match `^\d+\.\d+$` (no prefix) and concatenate the title from following spans.
- **Filter to chapter.** Without scoping to chapter range, the heading regex hits numbered items from other chapters and from body-text enumerations. Each chapter scan must filter candidates by `ch_n == cn`.
- **`insert_image` has no `clip`.** It will raise `TypeError`. Always render the cropped region first via `page.get_pixmap(matrix=mat, clip=clip)`.
- **Two-column flow.** Boxes run in two columns on each page. Without column detection, the extent algorithm crosses the gutter and grabs the wrong column's content. Use `column_of(x) = 0 if x < 300 else 1` (or measure from a sample page).
- **Last box on a page.** When a box has no next-box-in-column anchor, extend to the last text element in the column (not the page bottom — that grabs page footer/running header).
- **User wants snapshots, not text.** If the user shows an image of the textbook page or says "same as original" / "actual box snap" / "same to same", default to cropped image PDF. If they say "text content of boxes" / "extract the writing", do text extraction instead. Confirm when ambiguous.
- **Output format.** Default to **one PDF per chapter** containing all that chapter's boxes as image pages (1 page per box). Users frequently reject per-box `.md` files — they wanted chapter-grouped PDFs. Users ALSO reject text-rendered PDFs (boxes look nothing like the original). If the user shows an image of the textbook page, they want visual snapshots — not recreated styled text.
- **Crop to full column width, not heading-text width.** The box's left edge is the column's left margin (e.g. x=44 for Davidson 25e left column), NOT where the heading text begins. Tables in 2-column boxes start at the column margin; the heading text is often indented inside that. Cropping to the heading bbox clips the table's left column. Define `COL_BOUNDS` once per textbook from a few sample pages.
- **DPI.** 200 DPI gives crisp text without huge file size. 300 DPI for archival. 150 DPI for quick preview.

## Files in this skill

- `scripts/extract_callouts_snapshots.py` — full extractor: detect headings, determine extents, crop, assemble chapter PDFs.
- `references/davidson-25e-callouts.md` — verified count per chapter (1,285 boxes across 33 chapters) and detection quirks specific to Davidson 25e.
- `references/pymupdf-crop-recipes.md` — copy-paste snippets for cropping pages, inserting pixmaps, and avoiding the `clip`/`insert_image` gotcha.
