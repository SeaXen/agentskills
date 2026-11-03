#!/usr/bin/env python3
"""Extract numbered callout boxes from a textbook PDF as visual snapshots.

Output: one PDF per chapter containing cropped images of each box.

Usage:
    /usr/local/lib/hermes-agent/venv/bin/python extract_callouts_snapshots.py

Expects:
    - SRC PDF at the path configured below
    - _chapters_index.json from pdf-textbook-chapter-splitter next to output

Adjust COL_BOUNDS for the target textbook by sampling a few pages first.
"""
import pymupdf as fitz
import json
import re
from pathlib import Path
from collections import defaultdict

SRC = '/mnt/tb/#Sea/Book/Davidson_s Principles and Practice of Medicine 25e.pdf'
DST = Path('/mnt/tb/#Sea/Book/Davidson 25 Chapters')
INDEX_PATH = DST / '_chapters_index.json'

DPI = 200
ZOOM = DPI / 72.0

# Column bounds measured from Davidson 25e samples. Tune per textbook.
COL_BOUNDS = {
    0: (44, 300),    # left column
    1: (305, 562),   # right column
}


def chapter_title_case(s):
    small = {"and", "in", "of", "the", "to", "for", "with", "on"}
    out = []
    for i, w in enumerate(s.split()):
        wl = w.lower()
        out.append(wl if i != 0 and wl in small else w.capitalize())
    return " ".join(out)


def find_box_headings(page, chapter_n):
    """Find N.N Title heading bboxes by joining adjacent rightward spans on the same line."""
    blocks = page.get_text("dict")["blocks"]
    candidates = []
    for b in blocks:
        if b.get("type") != 0:
            continue
        for line in b.get("lines", []):
            spans_data = sorted(line.get("spans", []), key=lambda s: s["bbox"][0])
            for i, span in enumerate(spans_data):
                text = span["text"].strip()
                m = re.match(r"^(\d+)\.(\d+)$", text)
                if not m:
                    continue
                ch_n = int(m.group(1))
                num = int(m.group(2))
                if ch_n != chapter_n:
                    continue
                bx0, by0, bx1, by1 = span["bbox"]
                title_parts = []
                last_x1 = bx1
                for j in range(i + 1, len(spans_data)):
                    ns = spans_data[j]
                    if abs(ns["bbox"][1] - by0) > 5:
                        break
                    if ns["bbox"][0] < bx1 - 5:
                        continue
                    title_parts.append(ns["text"].strip())
                    last_x1 = ns["bbox"][2]
                title = " ".join(p for p in title_parts if p).strip()
                if title and len(title) > 3 and not title.endswith("."):
                    candidates.append({"ch": ch_n, "num": num, "title": title, "bbox": (bx0, by0, last_x1, by1)})
    return candidates


def column_of(x):
    return 0 if x < 300 else 1


def determine_extent(page, bbox, next_box_bbox=None):
    """Bottom y-coordinate of box content. Stops at next box in same column, else last text in column."""
    x0, y0, x1, y1 = bbox
    col = column_of(x0)
    page_h = page.rect.height
    if next_box_bbox and column_of(next_box_bbox[0]) == col:
        return next_box_bbox[1] - 4
    blocks = page.get_text("dict")["blocks"]
    last_y = y1 + 8
    col_min, col_max = COL_BOUNDS[col]
    for b in blocks:
        if b.get("type") != 0:
            continue
        for line in b.get("lines", []):
            for span in line.get("spans", []):
                sx0, sy0, sx1, sy1 = span["bbox"]
                if sy0 >= y0 and sx0 >= col_min - 10 and sx1 <= col_max + 10 and sy1 < page_h - 25:
                    last_y = max(last_y, sy1)
    return min(last_y + 6, page_h - 20)


def main():
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    doc = fitz.open(SRC)

    chapter_boxes = {}
    for ch in idx["chapters"]:
        cn = ch["n"]
        boxes = []
        for p in range(ch["start"] - 1, ch["end"]):
            page = doc[p]
            found = find_box_headings(page, cn)
            for b in found:
                b["page_idx"] = p
                boxes.append(b)

        # Dedupe
        seen = set()
        unique = []
        for b in boxes:
            key = (b["ch"], b["num"])
            if key in seen:
                continue
            seen.add(key)
            unique.append(b)
        boxes = unique

        by_page = defaultdict(list)
        for b in boxes:
            by_page[b["page_idx"]].append(b)

        final_boxes = []
        for p_idx, page_boxes in by_page.items():
            page = doc[p_idx]
            page_boxes.sort(key=lambda b: (column_of(b["bbox"][0]), b["bbox"][1]))
            for i, b in enumerate(page_boxes):
                next_box = None
                for j in range(i + 1, len(page_boxes)):
                    if column_of(page_boxes[j]["bbox"][0]) == column_of(b["bbox"][0]):
                        next_box = page_boxes[j]
                        break
                bottom = determine_extent(page, b["bbox"], next_box["bbox"] if next_box else None)
                x0, y0, x1, y1 = b["bbox"]
                col = column_of(x0)
                col_min, col_max = COL_BOUNDS[col]
                final_boxes.append({
                    "num": f"{b['ch']}.{b['num']}",
                    "title": b["title"],
                    "page_idx": p_idx,
                    "rect": (col_min, max(20, y0 - 8), col_max, bottom),
                })
        final_boxes.sort(key=lambda b: (int(b["num"].split(".")[0]), int(b["num"].split(".")[1])))
        chapter_boxes[cn] = final_boxes

    mat = fitz.Matrix(ZOOM, ZOOM)
    created = []
    total_pages = 0
    for ch in idx["chapters"]:
        cn = ch["n"]
        boxes = chapter_boxes.get(cn, [])
        if not boxes:
            continue
        title_ch = chapter_title_case(ch["title"])
        folder = DST / f"{cn:02d} - {title_ch}"
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / f"{cn:02d} - All Boxes.pdf"

        pdf = fitz.open()
        by_page = defaultdict(list)
        for b in boxes:
            by_page[b["page_idx"]].append(b)

        for p_idx in sorted(by_page.keys()):
            page = doc[p_idx]
            for b in by_page[p_idx]:
                rx0, ry0, rx1, ry1 = b["rect"]
                clip = fitz.Rect(rx0, ry0, rx1, ry1)
                pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
                w_pt = rx1 - rx0
                h_pt = ry1 - ry0
                new_page = pdf.new_page(width=w_pt, height=h_pt)
                new_page.insert_image(new_page.rect, pixmap=pix)

        pdf.save(out, garbage=4, deflate=True)
        pdf.close()
        check = fitz.open(out)
        pcount = check.page_count
        check.close()
        created.append((cn, len(boxes), pcount, str(out)))
        total_pages += pcount

    print(f"Created {len(created)} chapter box PDFs")
    print(f"Total boxes: {sum(c for _, c, _, _ in created)}")
    print(f"Total PDF pages: {total_pages}")
    for cn, count, pages, path in created:
        print(f"Ch {cn:02d}: {count:>3} boxes, {pages:>3} pages -> {path}")


if __name__ == "__main__":
    main()
