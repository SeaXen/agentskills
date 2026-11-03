#!/usr/bin/env python3
"""Extract callout box snapshots from a textbook PDF.

Strategy:
  1. Detect filled header bars (strict color match).
  2. Find the enclosing stroke-only border rectangle (same x-range, top at header top).
  3. Extract callout number/title from text spans in the header (handle multi-span headings).
  4. Crop each callout as a clipped pixmap and assemble one PDF per chapter.

Input:
  - Source PDF path
  - A pre-built _chapters_index.json from pdf-textbook-chapter-splitter
  - Output directory (one subdir per chapter)

Adjust the BOX_HEADER_COLORS list to match your target textbook's accent color.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf as fitz


# Adjust these to match your textbook's box-header colors.
# Davidson 25e uses these two shades of teal-blue:
BOX_HEADER_COLORS = [
    (0.17059586942195892, 0.46643778681755066, 0.6412756443023682),  # #2B77A4 dark
    (0.2077668458223343, 0.5990539193153381, 0.7661402225494385),    # #3599C3 medium
]
COLOR_TOLERANCE = 0.05
DPI = 200
PAD = 2  # padding around crop so the border is fully visible


def is_box_header_color(rgb, targets=BOX_HEADER_COLORS, tol=COLOR_TOLERANCE):
    return any(all(abs(a - b) < tol for a, b in zip(rgb, t)) for t in targets)


def chapter_title_case(s):
    small = {"and", "in", "of", "the", "to", "for", "with", "on"}
    out = []
    for i, w in enumerate(s.split()):
        wl = w.lower()
        out.append(wl if i != 0 and wl in small else w.capitalize())
    return " ".join(out)


def find_callouts_on_page(page, chapter_n):
    """Find all boxed callouts on a page that belong to a given chapter.

    Returns: list of dicts with keys num, title, page_idx, rect (x0,y0,x1,y1).
    """
    drawings = page.get_drawings()

    # Step 1: filled header bars (strict color match, wide-and-short)
    header_rects = []
    for d in drawings:
        fill = d.get("fill")
        rect = d.get("rect")
        if not fill or not rect:
            continue
        if not is_box_header_color(fill):
            continue
        w = rect.x1 - rect.x0
        h = rect.y1 - rect.y0
        if w > 100 and 8 < h < 35:
            header_rects.append(rect)
    if not header_rects:
        return []

    # Step 2: enclosing border rectangle per header
    callouts = []
    for header in header_rects:
        hx0, hy0, hx1, hy1 = header
        border = None
        for d in drawings:
            stroke = d.get("color")
            fill = d.get("fill")
            rect = d.get("rect")
            if not rect or not stroke or fill:
                continue
            rx0, ry0, rx1, ry1 = rect
            if abs(rx0 - hx0) < 4 and abs(rx1 - hx1) < 4:
                if ry0 <= hy0 + 2 and ry1 > hy1:
                    w = rx1 - rx0
                    h = ry1 - ry0
                    if w > 100 and h > 30 and abs(ry0 - hy0) <= 5:
                        # Pick the tallest border that aligns with the header top
                        # (outer box frame, not inner table grid lines)
                        if border is None or (ry1 - ry0) > (border.y1 - border.y0):
                            border = rect
        if not border:
            continue

        # Step 3: extract number/title from text spans in the header bar.
        # Headings are often split across spans ("1.2" | " Title text") — join by y then x.
        bx0, by0, bx1, by1 = header
        blocks = page.get_text("dict")["blocks"]
        spans_in_header = []
        for b in blocks:
            if b.get("type") != 0:
                continue
            for line in b.get("lines", []):
                for span in line.get("spans", []):
                    sx0, sy0, sx1, sy1 = span["bbox"]
                    if sy0 >= by0 - 2 and sy1 <= by1 + 2 and sx0 >= bx0 - 5 and sx1 <= bx1 + 5:
                        text = span["text"].strip()
                        if text:
                            spans_in_header.append((sy0, sx0, text))
        # round(y * 2) / 2 puts spans within 0.5pt on the same sort key
        spans_in_header.sort(key=lambda x: (round(x[0] * 2) / 2, x[1]))
        full_text = " ".join(t for _, _, t in spans_in_header)

        m = re.search(r"(\d+)\.(\d+)\s+(.+)", full_text)
        if not m:
            continue
        ch_n = int(m.group(1))
        num = int(m.group(2))
        title = m.group(3).strip()
        if ch_n != chapter_n:
            continue

        callouts.append({
            "num": num,
            "title": title,
            "page_idx": page.number,
            "rect": (border.x0, border.y0, border.x1, border.y1),
        })
    return callouts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Source textbook PDF")
    ap.add_argument("--index", required=True, help="Path to _chapters_index.json from pdf-textbook-chapter-splitter")
    ap.add_argument("--out", required=True, help="Output directory (chapter subdirs)")
    ap.add_argument("--dpi", type=int, default=DPI)
    args = ap.parse_args()

    src = Path(args.src)
    out_root = Path(args.out)
    with open(args.index) as f:
        idx = json.load(f)

    doc = fitz.open(src)
    mat = fitz.Matrix(args.dpi / 72.0, args.dpi / 72.0)

    # Detect callouts per chapter
    chapter_callouts = {}
    for ch in idx["chapters"]:
        cn = ch["n"]
        all_callouts = []
        for p in range(ch["start"] - 1, ch["end"]):
            page = doc[p]
            all_callouts.extend(find_callouts_on_page(page, cn))

        # Deduplicate by (page_idx, num)
        seen = set()
        unique = []
        for c in all_callouts:
            key = (c["page_idx"], c["num"])
            if key in seen:
                continue
            seen.add(key)
            unique.append(c)
        all_callouts = unique
        all_callouts.sort(key=lambda c: (c["page_idx"], c["num"]))
        chapter_callouts[cn] = all_callouts

    # Build one chapter PDF per chapter
    summary = []
    total_pages = 0
    for ch in idx["chapters"]:
        cn = ch["n"]
        callouts = chapter_callouts.get(cn, [])
        if not callouts:
            continue
        title_ch = chapter_title_case(ch["title"])
        folder = out_root / f"{cn:02d} - {title_ch}"
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / f"{cn:02d} - All Boxes.pdf"

        pdf = fitz.open()
        by_page = defaultdict(list)
        for c in callouts:
            by_page[c["page_idx"]].append(c)

        for p_idx in sorted(by_page.keys()):
            page = doc[p_idx]
            for c in by_page[p_idx]:
                rx0, ry0, rx1, ry1 = c["rect"]
                clip = fitz.Rect(max(0, rx0 - PAD), max(0, ry0 - PAD),
                                 rx1 + PAD, ry1 + PAD)
                pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
                w_pt = (rx1 + PAD) - (rx0 - PAD)
                h_pt = (ry1 + PAD) - (ry0 - PAD)
                new_page = pdf.new_page(width=w_pt, height=h_pt)
                # NOTE: Page.insert_image() does NOT accept a clip kwarg in pymupdf.
                # The pixmap is already clipped via get_pixmap(clip=...) above.
                new_page.insert_image(new_page.rect, pixmap=pix)

        pdf.save(out_path, garbage=4, deflate=True)
        pdf.close()
        check = fitz.open(out_path)
        summary.append((cn, len(callouts), check.page_count, str(out_path)))
        total_pages += check.page_count
        check.close()

    # Report
    print(f"Created {len(summary)} chapter box PDFs", file=sys.stderr)
    print(f"Total callouts: {sum(c for _, c, _, _ in summary)}", file=sys.stderr)
    print(f"Total PDF pages: {total_pages}", file=sys.stderr)
    for cn, count, pages, path in summary:
        print(f"Ch {cn:02d}: {count:>3} callouts, {pages:>3} pages -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
