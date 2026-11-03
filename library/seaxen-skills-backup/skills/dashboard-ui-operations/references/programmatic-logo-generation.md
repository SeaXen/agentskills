# Programmatic Logo Generation with PIL

Use when AI image generation is unavailable (no FAL_KEY, no credits) and you need a clean app logo/favicon set.

## Pattern

Create logos programmatically with Python PIL/Pillow — works offline, deterministic, no API needed.

```python
from PIL import Image, ImageDraw
import math, os

def create_logo(size=512):
    hr = size * 4  # 4x for anti-aliasing, then downscale
    img = Image.new('RGBA', (hr, hr), (0, 0, 0, 0))  # transparent
    draw = ImageDraw.Draw(img)
    
    # Background: rounded rectangle with gradient
    margin = int(hr * 0.02)
    corner_r = int(hr * 0.16)
    # Draw gradient pixel-by-pixel (slow but works)
    for y in range(margin, hr - margin):
        ratio = (y - margin) / (hr - 2 * margin)
        r = int(top_color[0] + ratio * (bottom_color[0] - top_color[0]))
        g = int(top_color[1] + ratio * (bottom_color[1] - top_color[1]))
        b = int(top_color[2] + ratio * (bottom_color[2] - top_color[2]))
        for x in range(margin, hr - margin):
            if in_rounded_rect(x, y, margin, hr-margin, corner_r):
                draw.point((x, y), fill=(r, g, b, 255))
    
    # Downscale for anti-aliasing
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(img)
    
    # Draw letter mark / icon on top
    # ... polygon, line, ellipse operations
    
    return img

# Generate all sizes
for size, name in [(512,'logo-512'), (192,'favicon-192'), (64,'logo-64'),
                    (48,'favicon-48'), (32,'favicon-32'), (16,'favicon-16')]:
    create_logo(size).save(f'static/icons/{name}.png')

# Multi-size ICO
img16 = create_logo(16)
img16.save('static/favicon.ico', format='ICO', sizes=[(16,16),(32,32),(48,48)])
```

## Size guide

| Size | Use |
|------|-----|
| 512 | Full logo, social share, splash |
| 192 | PWA icon, Apple touch icon |
| 64 | Dashboard header |
| 48 | Fallback favicon |
| 32 | Standard favicon |
| 16 | Tab icon |

## Serving in FastAPI

```python
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico", media_type="image/x-icon")
```

HTML head:
```html
<link rel="icon" type="image/png" href="/static/icons/favicon-32.png">
<link rel="shortcut icon" href="/static/favicon.ico">
<link rel="apple-touch-icon" href="/static/icons/favicon-192.png">
```

## Anti-aliasing trick

Draw at 4x resolution, then `Image.Resampling.LANCZOS` downscale. This gives smooth edges without needing anti-aliased drawing primitives (which PIL lacks for polygons).

## Pitfalls

1. **PIL polygon fill doesn't support transparency well.** For cutting holes (like the triangle inside an "A"), draw the outer shape in the accent color, then draw the inner cutout with `(0,0,0,0)`. This only works on RGBA images.

2. **favicon.ico must be saved from a PIL Image**, not just renamed PNG. Use `img.save('favicon.ico', format='ICO', sizes=[...])`.

3. **Large sizes with pixel-by-pixel gradients are slow** (512px = 2M pixels × 4x = 32M iterations). Acceptable for one-time generation but not for runtime.

4. **Test at actual favicon size (16px).** Complex logos become unreadable blobs at 16px. Keep the design to 2-3 geometric shapes max.
