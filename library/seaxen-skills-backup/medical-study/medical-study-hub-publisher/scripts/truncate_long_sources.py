#!/usr/bin/env python3
"""Truncate long source markdown for safe rendering.

The renderer's headless Chromium hangs on sources > ~30KB / ~400 lines because
the page height grows past several A4-pages-worth of pixels. Truncate to the
first ~100 lines (cut at the next `## ` header after the midpoint) and append a
`[Content truncated for rendering]` footnote. The full source is preserved
locally in `<hub>/<slug>/<slug>.md`.

Usage:
    from truncate_long_sources import make_truncated_md
    actual_md = make_truncated_md(Path('/root/resp-content/foo.md'))
    # pass actual_md to render_topic.py
"""
from pathlib import Path


def make_truncated_md(src_md, max_lines=100, threshold_bytes=30000):
    """Return a truncated copy of the markdown if it's too long, else the original.

    - max_lines=100 is empirically safe (one tall A4 page, no chromium hang).
    - threshold_bytes=30_000 is the rough cutoff; files below render fine
      without truncation, files above hang reliably.
    - The truncated file is written to /tmp/resp-trunc-<stem>.md so re-runs
      pick up the truncated version (no overwriting the canonical source).
    """
    if src_md.stat().st_size <= threshold_bytes:
        return src_md
    text = src_md.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if len(lines) <= max_lines:
        return src_md
    # Try to cut at the next `## ` section header after the midpoint, so we
    # don't slice in the middle of a section.
    cut = max_lines
    for i in range(max_lines, min(len(lines), max_lines + 50)):
        if lines[i].startswith("## ") and i > max_lines // 2:
            cut = i
            break
    truncated = (
        "".join(lines[:cut])
        + f"\n\n*[Content truncated for rendering - see {src_md.name} for full text]*\n"
    )
    out = Path(f"/tmp/resp-trunc-{src_md.stem}.md")
    out.write_text(truncated, encoding="utf-8")
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: truncate_long_sources.py <md_path> [max_lines]")
        sys.exit(1)
    src = Path(sys.argv[1])
    max_lines = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    out = make_truncated_md(src, max_lines=max_lines)
    print(f"input:  {src} ({src.stat().st_size} bytes)")
    print(f"output: {out} ({out.stat().st_size} bytes)")