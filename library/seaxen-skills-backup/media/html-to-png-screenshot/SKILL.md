---
name: html-to-png-screenshot
description: Use when AI image generation is unavailable or unsuitable (designed infographics, document mockups, structured visuals where text must stay crisp) and you need to render HTML/CSS to a high-resolution PNG. Covers headless Chromium screenshot with proper window-size, full-page detection, and cropping.
version: 1.0.0
license: MIT
metadata:
  hermes:
    tags: [image, html, chromium, screenshot, png, infographic]
    related_skills: [weasyprint-pdf-creation, design-systems, impeccable]
---

# HTML → PNG via Headless Chromium

Render designed HTML/CSS to a sharp PNG when AI image generation (FAL / OpenAI) is offline, the user wants exact text fidelity, or the layout is structured enough that an AI generator would mangle it (infographics, study notes, document mockups, dashboards-as-image).

This is **not** a substitute for AI image generation when the user wants creative / photorealistic output. Reach for it when the visual is **designed** — a layout you can describe in HTML/CSS more precisely than in a prompt.

## When to use

- AI image generation is unavailable (`Missing requirements: FAL_KEY ...`) and you need a designed image.
- The visual has dense text, tables, comparison columns, or numbered sections where AI generators consistently misspell.
- The user asks for a "PNG of this" / "image like this reference" and the reference is clearly a designed document (infographic, study note, brochure, chart).
- You need pixel-exact control over layout, colors, typography, and density.

## When NOT to use

- Photorealistic scenes, illustrations of people/objects, mood imagery — use AI image gen.
- The output needs to be interactive (use HTML directly or a dashboard).
- The output is a PDF (use `weasyprint-pdf-creation`).
- A simple screenshot of an existing web page is enough — use the browser tool.

## Core pattern (one command + crop)

```bash
# 1. Set the viewport. 794x1123 = A4 portrait at 96dpi (crisp at 1x, fine at 2x).
#    Width must match the .page CSS width. Height should be generous — we'll
#    crop down to actual content.
chromium --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=794,1400 \
  --virtual-time-budget=5000 \
  --screenshot=/tmp/out.png \
  "file:///abs/path/to/your.html" 2>&1 | tail -1
```

Then crop to the actual content extent with PIL:

```python
from PIL import Image
img = Image.open('/tmp/out.png')
w, h = img.size
px = img.load()

# Find the page boundary by looking for the paper color (NOT the body background).
# Body bg #efe6d3 = (239,230,211) is darker; paper bg #fdf8ee = (253,248,238) is
# lighter. A naive is_white() check picks up the body bg as "content" and returns
# the full window — wrong.
def is_paper(rgb):
    r, g, b = rgb
    return r > 250 and g > 245 and b > 230

last_paper = 0
for y in range(h):
    if is_paper(px[10, y]):
        last_paper = y
print(f"Page extends to y={last_paper}")

# Crop to page bounds
page = img.crop((0, 0, w, last_paper + 12))
page.save('final.png', optimize=True)
```

## The page CSS that makes this work

The HTML needs a fixed-size page container with `overflow: hidden`, otherwise content spills past the page and the screenshot captures the body background instead:

```css
.page {
  width: 794px;          /* = window-size width */
  height: 1123px;        /* A4 portrait at 96dpi, or any fixed target */
  background: var(--paper);
  margin: 0 auto;
  padding: 16px 22px;
  overflow: hidden;      /* critical — without this content grows the page */
  position: relative;
}
```

`min-height` does NOT work — it lets content extend the page beyond the target. Use `height` (fixed) with `overflow: hidden` if you need to clip, or sized `padding` if you want content to fit naturally.

## Window-size: pick height larger than the page

If `--window-size=794,1123` exactly and content overflows, Chromium captures only the visible viewport — you get a clipped image. Two fixes:

1. **Set window height to ~1.5–2x the page height** (e.g. `794,2000` for a 1123px page). Chromium will render the whole document but only the visible window is captured. Then crop down to the page extent.
2. **Use `--screenshot` with `--virtual-time-budget`** to give layout time to settle before capture (default is fast but sometimes misses late-loading webfonts).

The crop step is required either way — Chromium's window includes the body background extending past the page.

## Full-page detection — the subtle bug

A naive "find last non-white row" check will return the full window because the body background (`<body style="background: #efe6d3">`) sits below the page and is **not** white. Solutions:

- Look for the **page** background color (the lighter one), not just "non-white".
- Or render the body background the same color as the page (cleaner, but limits you).
- Or scan only inside the page's left/right margins where the body bg can't bleed.

```python
# Wrong:
def is_white(rgb): return all(c > 250 for c in rgb)
# Right:
def is_paper(rgb): return r > 250 and g > 245 and b > 230
```

## Content density: budget for 10px per section

If you have N sections, target ~`(page_height - 100) / N` pixels per section. Tighten the section padding, font size, and margins before adding more content. The most common layout-bust is a 10-section page at default body padding — it overflows by 3-4x.

A 794×1123 A4 page comfortably fits **10 sections** at:
- 8-9px body font
- 1.2-1.3 line-height
- 3-4px section padding (top/bottom)
- 4-5px section margins

If you need more content, use a 2-page layout (render twice with different content) or compress the prose.

## Verify

After rendering, verify the image programmatically:

```python
# 1. Dimensions match target
assert img.size == (794, 1123)

# 2. Content is present (OCR or color band detection)
# The PNG renders text crisply at the chosen size, so OCR works well.
import subprocess
text = subprocess.run(['tesseract', 'final.png', '-', '-l', 'eng'],
                      capture_output=True, text=True).stdout
assert 'Section 1' in text  # adjust to expected content

# 3. No overflow: last_content_row should be within page bounds
#    (this is what the crop step enforces)
```

## Reference recipe (worked example)

The session that produced this skill rendered a 10-section medical infographic in Sea Knowledge style (rose/cream/sage palette, hand-drawn feel, comparison tables, exam pearls). Recipe:

1. Build `/root/sea-knowledge-infographics/topic.html` with:
   - `.page` at 794x1123, paper bg, fixed height, overflow hidden
   - 10 sections, each ~80-95px tall: header bar + 8-9px body text + bullets
   - 2-column grids for side-by-side content (stable vs ACS, classic vs atypical)
   - Inline SVG for tiny illustrations (3 artery cross-sections for atherosclerosis stages)
   - Comparison table with 6 rows (differential diagnosis) and 3 rows (reperfusion strategy)
2. Render with `chromium --window-size=794,2000 --screenshot=out.png`
3. Crop to the 1123px page extent
4. Result: 282KB PNG, fits A4, all 10 sections visible

The HTML source is reusable as a template — the only thing that changes per topic is the content and the SVG illustrations.

## What this skill is not

- Not a substitute for `weasyprint-pdf-creation` when the deliverable is a PDF. WeasyPrint gives better pagination and PDF-specific features (page numbers, headers/footers per page). Use Chromium→PNG when you need an *image* specifically.
- Not a way to fake AI image generation. If the user wants an illustration of a heart, use AI gen. This is for *designed* visuals with structured content.
- Not a screenshot tool for live web pages. Use the browser tool for that.

## Bundled assets

- **`templates/sea-knowledge-infographic.html`** — content-free Sea Knowledge style shell. Drop in your topic content, render, ship. 5 section layouts (chips, flow+figures, 2-col grid, table, pearls+callout) cover 95% of medical / study infographic needs.
- **`scripts/render.py`** — turnkey renderer. `python scripts/render.py input.html [output.png]` handles the chromium command, full-page detection, and cropping. Use it instead of hand-typing the chromium flags.

Working example invocation:

```bash
python scripts/render.py templates/sea-knowledge-infographic.html out.png
# -> Captured: 794x1796
# -> Cropped to: (794, 1123)
# -> Saved: out.png (282,725 bytes)
```
