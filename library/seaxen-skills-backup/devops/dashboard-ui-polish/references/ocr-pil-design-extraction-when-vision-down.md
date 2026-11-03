# Design extraction via OCR + PIL color analysis (when vision tools are down)

When `vision_analyze` or `browser_vision` returns `Unknown Model` / 404 (the auxiliary vision model is misconfigured or missing), and the user has shared a **screenshot they want you to replicate**, do not stop and ask them to describe it. You can still recover most of the layout, text content, and color palette by combining three local tools that ship with most Python environments:

1. **PIL** (`pip install Pillow`) for pixel-level color sampling.
2. **tesseract** + **pytesseract** for OCR with bounding boxes.
3. A local HTTP server (`python3 -m http.server`) if you want to use `browser_navigate` to load the image.

This is a **complement** to the existing DOM-probe fallback (which verifies *your own* UI). This technique is for **understanding a reference screenshot you cannot see**.

## When to use

- The user pasted an image and said "make it like this" / "match this dashboard".
- `vision_analyze` returned `{"success": false, "error": "...model 'X' not found"}` or similar.
- `browser_vision` (after serving the image locally) returned the same model error.

Skip if any vision tool worked — descriptions from vision are faster and more accurate than the OCR pipeline.

## Step 1 — Confirm the image exists and grab its dimensions

```bash
ls -la /path/to/screenshot.png
python3 -c "from PIL import Image; im=Image.open('/path/to/screenshot.png'); print(im.size, im.mode)"
```

If the path was given as a relative `MEDIA:` reference or a Discord attachment, check `~/.hermes/image_cache/` — Hermes often caches them there as `img_<hash>.png`.

## Step 2 — Get the color palette with PIL (cheap, no OCR needed)

Sample pixel averages on an N×M grid to map out rough color regions — sidebar vs main, header vs body, accent zones:

```python
from PIL import Image
import collections
img = Image.open('/path/to/screenshot.png')
w, h = img.size
gx, gy = 6, 4  # grid resolution
regions = collections.defaultdict(list)
for ry in range(gy):
    for rx in range(gx):
        x = int((rx + 0.5) * w / gx)
        y = int((ry + 0.5) * h / gy)
        # Average a small window to ignore text pixels
        rs, gs, bs, n = 0, 0, 0, 0
        for dx in range(-15, 16, 5):
            for dy in range(-15, 16, 5):
                px = min(max(x+dx, 0), w-1)
                py = min(max(y+dy, 0), h-1)
                p = img.getpixel((px, py))
                rs += p[0]; gs += p[1]; bs += p[2]; n += 1
        regions[(rx, ry)] = (rs//n, gs//n, bs//n)

for ry in range(gy):
    line = ""
    for rx in range(gx):
        r, g, b = regions[(rx, ry)]
        line += f"#{r:02x}{g:02x}{b:02x} "
    print(f"Row {ry}: {line}")
```

This tells you, at a glance:

- **Is it dark mode?** Top-left color near `#191919`/`#1a1a1a` = dark. Top-left near `#ffffff` = light.
- **Where is the sidebar?** A vertical strip of `#1a1a1a` on the left while the rest is `#191919` = sidebar.
- **Are there accent colors?** Look for green tints (`#38-55, #47` hue range = gains) or red (`#58, #42, #45` = losses) in any cell.
- **Is there a header band?** Row 0 significantly different from row 1 = header strip.

## Step 3 — Get text + bounding boxes with tesseract

```bash
pip install pytesseract Pillow  # if not already
which tesseract  # /usr/bin/tesseract
```

**Python interpreter pitfall:** if your active session's `python3` is a venv (e.g. `/usr/local/lib/hermes-agent/venv/bin/python3`) that doesn't have `pytesseract` or `Pillow` installed, the import will fail with `ModuleNotFoundError`. Try the system Python first:

```bash
which python3
python3 -c "import pytesseract" 2>&1 | head -1
# If that errors, try the system interpreter:
/usr/bin/python3 -c "import pytesseract; print('ok')"
/usr/bin/python3 << 'PYEOF'
import pytesseract
from PIL import Image
...
PYEOF
```

`/usr/bin/python3` (Debian/Ubuntu) typically has `pytesseract` + `Pillow` pre-installed for agent tooling. If both fail, `apt install python3-pil python3-pytesseract tesseract-ocr` (Debian) or `pip install pytesseract Pillow` into a venv that has internet. Don't waste time trying to bootstrap pip in a venv that doesn't have pip; switch interpreters.

When the OCR script needs to be inline (e.g. one-shot via `terminal()`), use a heredoc with the system interpreter:
```bash
/usr/bin/python3 << 'PYEOF'
import pytesseract
from PIL import Image, ImageEnhance, ImageOps
img = Image.open('/path/to/screenshot.png')
img_big = img.resize((img.width*2, img.height*2), Image.LANCZOS)
gray = ImageOps.grayscale(img_big)
gray = ImageEnhance.Contrast(gray).enhance(1.6)
print(pytesseract.image_to_string(gray))
PYEOF
```

For dark-theme UIs (white text on dark background), the default OCR pass underperforms. Three tweaks:

1. **Upscale 2×** with `Image.LANCZOS` so small text is legible to tesseract.
2. **Grayscale + contrast enhance** (factor 1.5–2.0).
3. **Run twice** — once on the enhanced grayscale, once on the inverted version. The union of both usually gets all text; pick whichever has higher confidence per region.

```python
import pytesseract
from PIL import Image, ImageEnhance, ImageOps

img = Image.open('/path/to/screenshot.png')
img_big = img.resize((img.width*2, img.height*2), Image.LANCZOS)
gray = ImageOps.grayscale(img_big)
gray = ImageEnhance.Contrast(gray).enhance(1.6)
inv = ImageOps.invert(gray)

text_normal = pytesseract.image_to_string(gray)
text_inverted = pytesseract.image_to_string(inv)
print(text_normal + "\n--- inverted ---\n" + text_inverted)
```

For **bounding boxes** (essential to map which label belongs to which card/region):

```python
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
for i, txt in enumerate(data['text']):
    if not txt.strip():
        continue
    try:
        conf = int(data['conf'][i])
    except ValueError:
        continue
    if conf < 40:
        continue
    x = data['left'][i] // 2
    y = data['top'][i] // 2
    w = data['width'][i] // 2
    h = data['height'][i] // 2
    print(f"({x:4d},{y:4d}) {w:3d}x{h:2d} conf={conf:3d}: {txt!r}")
```

Scaled-back coords (divide by the upscale factor) match the original image's coordinate system, so you can map labels directly to layout regions.

## Step 4 — Cross-reference to figure out the structure

Combine the grid colors + bounding boxes + text content to deduce:

- **Header region**: y=0–80, often contains a hero title (large text) + a nav strip below.
- **Stat cards row**: usually y=200–350, multiple cards at the same y. If you see 4 stat-card-shaped labels at the same y (`Win Rate`, `Total P&L`, `Returns`, `Profit Factor`) with numeric values 30px below them — that's a 4-col stat row.
- **Sidebar**: vertical strip on left, x=0–260, with stacked link/button labels.
- **Main content**: right of sidebar, with mixed y regions for content cards.

Sort the bounding boxes by `y` then `x` to reconstruct reading order. Group labels by similar y to find rows.

## Step 5 — Optional: serve the image locally for `browser_navigate`

If you want to use `browser_vision` after all (e.g. another model is configured) or want the user to see the served image:

```bash
# terminal(background=true, notify_on_complete=false)
cd /path/to/image/dir && python3 -m http.server 9876
```

Then `browser_navigate(url="http://localhost:9876/img.png")`. If `browser_vision` still returns model errors, fall back to PIL + OCR — don't loop on browser_navigate.

## Pitfalls

- **Vision sometimes works after a retry** — try `vision_analyze` once with a different `image_url` form (file:// vs http:// vs absolute path) before falling back. Only commit to the OCR pipeline after vision has failed twice on the same image.
- **tesseract confidence < 40 means the text is probably wrong** — drop those rows. False-positive labels from noise on the page will misdirect your layout map. Keep `if conf < 40: continue`.
- **Tesseract on light-theme UIs (dark text on light bg) is excellent out of the box** — no enhancement needed. The grayscale+contrast+invert dance is for dark-theme UIs specifically. If the top-left pixel is brighter than #cccccc, skip enhancement.
- **OCR does not give you the design language** — it gives you text + positions. The "design" (typography, spacing, hover states, animations) must come from your own judgment based on the reference's domain (trading → dense numerics, content library → typography, etc.).
- **Do NOT save this OCR pipeline as a fallback rule that triggers every time vision is slow.** This is a recovery technique for when vision returns *model errors*. If vision returns valid text but is just slow, wait for it. The OCR pipeline is for tool-down situations only.
- **Don't claim you "saw" the image.** Tell the user explicitly that vision was unavailable and you used OCR + color analysis to read the screenshot. Cite the OCR-extracted text so they can verify you got it right.
- **Verify the recovered structure by browsing to your built app**, not by re-running OCR on your own UI. The OCR pipeline is for understanding inputs; the verification pipeline (browser DOM probes, screenshots, curl checks) is for confirming outputs.

## Example session output shape

When this technique fires, the response to the user should be brief and structured:

> Vision tools returned model errors for the reference screenshot, so I extracted the layout via PIL color sampling + tesseract OCR. Detected:
> - Dark theme (#191919 base, #1a1a1f cards, #22c55e green / #ef4444 red accents)
> - Header at y≈36: "FREE TRADING JOURNAL"
> - Tab row at y≈133: REVIEW, TRADES DB, MISSED TRADES DB, MILESTONES
> - 4 stat cards at y≈277: Win Rate 50.0%, Total P&L $1.8K, Returns 18.0%, Profit Factor 5.50
> - Calendar grid at y≈432 with day cells colored green/red by P&L
>
> Building the Next.js version at `/mnt/tb/1Apps/Tradingx` on port 8799 now.

The user can verify the OCR pass before you write a line of code.