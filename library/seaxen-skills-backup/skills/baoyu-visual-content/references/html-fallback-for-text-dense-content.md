# HTML + Headless-Chromium Fallback for Text-Dense Infographics

## When to use this path
Use this when the source material is a **branded, text-dense educational infographic** (medical study notes, study cheat sheets, branded one-pagers) and either:

- `image_generate` is unavailable (FAL/OpenAI keys missing, no paid credits, backend down)
- AI image generation is available but reliably mangles text, tables, or section structure
- The deliverable must be pixel-faithful to a reference style (rose/cream palette, numbered sections, comparison tables, exam pearls)
- The user wants editable source (HTML) for later tweaks

For free-form illustrations, concept art, or anything that benefits from AI's creative variation, stick with `image_generate`.

## Why HTML beats AI gen for this class
- AI gen is great at mood, color, and rough layout — bad at **legible small text**, **tables**, and **precise section counts**
- HTML/CSS gives byte-perfect control over typography, spacing, and section structure
- The HTML file is **editable** — the user can adjust text, palette, or layout later
- Headless Chromium produces crisp 96-DPI PNG suitable for printing, sharing, or embedding

## Workflow
1. **Reverse-engineer the reference style** without vision tools if needed:
   - `tesseract <ref>.png /tmp/ref -l eng` → extract text structure
   - `PIL.Image` color analysis (resize to 100×100, `Counter(pixels).most_common(20)`) → palette
   - Note the dominant rose/cream/sage/coral tones and the section count
2. **Author the HTML** with a single fixed-size `.page` (e.g. A4 portrait 794×1123px), inline CSS, and the same palette as the reference
3. **Render to PNG**:
   ```bash
   chromium --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
     --window-size=794,1400 \
     --virtual-time-budget=5000 \
     --screenshot=out.png \
     "file:///abs/path/to/infographic.html"
   ```
   Use a window height ≥ target page height. Final image is cropped to the `.page` rect.
4. **Verify**:
   - `python -c "from PIL import Image; print(Image.open('out.png').size)"` → confirm dimensions
   - OCR the rendered PNG to confirm all sections survived
   - Scan for the brand-color pixels to confirm headers/sections rendered

## Hard-won pitfalls

### Page fit
- ❌ `min-height: 1123px` — content overflows the page; window-size then captures everything including the body background, so `is_white()` checks lie
- ✅ `height: 1123px; overflow: hidden;` — the page is exactly the size you want, content is clipped if it doesn't fit
- First render will likely be 2-4× too tall. **Compact aggressively**: section margins 4-6px, body padding 3-4px, font-size 7.5-9.5px, line-height 1.25-1.3

### Content-extent detection in the rendered PNG
- ❌ `is_white(rgb)` over the full image — the body background (`#efe6d3`) is **not** white, so a naive scan reports it as "content" and you think the page is 4500px tall when it's actually 1123px
- ✅ Look for the **paper color** specifically (`#fdf8ee` / `is_paper(rgb)`), or look for the body-background color to find the page boundary
- Cheap diagnostic: `print(px[10, 1115], px[10, 1125])` — if the first is paper and the second is body bg, the page ends at ~1123

### Section count verification without vision
- Sample horizontal bands for the brand color (e.g. `is_rose_deep(rgb)` for `#996677`)
- 10 sections → expect 10-16 rose-deep text bands (1 header title + 10 section titles + 5 misc chips)
- A4 portrait 794×1123 should fit 10 dense sections if each section is ~95px tall

### Window-size for headless Chromium
- `--window-size=W,H` is the **viewport**; for full-page content beyond H, content is clipped
- Use a window height ≥ the longest expected page, then crop to the page rect
- For A4 portrait with overflow risk, render at `--window-size=794,1400` then crop to `(0, 0, 794, 1123)`

### Inline SVG over external assets
- Reference style often has hand-drawn anatomical icons. **Inline SVG** keeps everything self-contained and renders crisp at any size
- Avoid `<img src=...>` — paths break if the file moves, and the user can't easily edit them

## When NOT to use this path
- The deliverable is a free-form illustration, character art, or concept image
- The reference style is photographic or 3D
- The user explicitly wants AI-generated art
- Text density is low (1-2 short paragraphs) — AI gen handles that fine

## Editable deliverable shape
Always save both:
- `out.png` — the rendered image
- `source.html` — the editable HTML (so the user can adjust content, palette, or layout)

Save them in a stable project directory like `~/sea-knowledge-infographics/<topic>.{html,png}` rather than `/tmp` so the user can find and re-render them.
