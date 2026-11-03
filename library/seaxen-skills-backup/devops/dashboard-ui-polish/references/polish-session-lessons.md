# Polish-session lessons from Systor / self-hosted dashboard work

Concrete pitfalls and techniques that turned up during real polish passes. Add to `SKILL.md` via a one-line pointer, or reference inline.

## "Full" / "100%" / "wide" / "big" = 100% of parent

When the user says **"full width"**, **"100%"**, **"3/3"**, **"wide big"**, they mean **100% of the immediate parent container** — not "wider than the previous version" and not "taller in the other axis".

Concrete failure pattern observed: a hero was set to `grid-template-columns: 1.15fr .85fr` (left=1.15, right=0.85) to make the GO card "wider." The user replied "make go 3/3, 100% full width f that box, don't you understand meaning of full?" That means the GO card must occupy the **full top hero width** with no sibling panel, not just be the wider of two columns.

Verification rule: after applying, probe live `getBoundingClientRect()` and assert the target element's `width` equals the parent's `width` (within ~2px tolerance). Do not stop at "it's bigger than before."

## Duplicate CSS rules accumulate silently across many polish passes

When a dashboard is polished in many rounds (v3, v6, v8, v12, v17, v19...), the same selector can end up redefined multiple times in `style.css` with conflicting values. The cascade picks whichever rule wins, often the **most recent**, but the dead rules stay around and bloat the file.

Symptoms:
- A fix lands but the page doesn't change visually
- `style.css` is 80+ KB and most of it is stale

Detection:
```bash
grep -nE '\.speed-simple-toolbar' style.css
```
If the same selector appears more than 2–3 times, consolidate.

Quick consolidation pattern (Python regex, applies to the LAST remaining definition):
```python
import re
for sel in ['.speed-simple-toolbar', '.speed-current-card']:
    pat = re.compile(rf'(?:^|\n)[^{{}}]*?{re.escape(sel)}[^{{}}]*?\{{[^{{}}]*?\}}\s*', re.M)
    matches = list(pat.finditer(css))
    if len(matches) < 2: continue
    new_css = css
    for m in reversed(matches[:-1]):
        new_css = new_css[:m.start()] + new_css[m.end():]
```

After consolidation, the CSS file should drop ~10–15% without any visual change.

## Duplicate DOM ids across templates

A common layout mistake: when the same `id="..."` appears in two templates (e.g. `id="alerts-body"` in both `dashboard.html` and `alerts.html`), `document.getElementById()` returns only the first match in document order, breaking the second page's binding silently.

Detection:
```bash
grep -RIn 'id="' templates/*.html | awk -F'id="' '{print $2}' | awk -F'"' '{print $1}' | sort | uniq -c | sort -rn | awk '$1>1'
```

Fix: rename the colliding id (e.g. `dash-alerts-body`) and update the JS reference in both the template that owns the id AND any JS that calls `getElementById()` for it.

## Mobile toolbar 2-column stack pattern

On narrow viewports (`max-width: 700px`), dashboard toolbars must collapse from horizontal to vertical, and controls must go into a 2-column grid where buttons span full width.

Working pattern:
```css
@media (max-width:700px){
  .speed-simple-toolbar{
    height:auto !important; min-height:0 !important;
    padding:8px !important; gap:6px !important;
    display:flex !important; flex-direction:column !important;
    align-items:stretch !important;
  }
  .speed-simple-controls{
    display:grid !important;
    grid-template-columns:1fr 1fr !important;
    gap:6px !important;
  }
  .speed-inline-field{display:flex !important; align-items:stretch !important; width:100% !important}
  .speed-inline-field .control-select{height:36px !important; width:100% !important}
  #speed-run-btn, #speed-refresh-btn{height:36px !important; width:100% !important; grid-column:span 2 !important}
}
```

Remove label wrappers entirely from the toolbar HTML (move them to `aria-label` on the controls) so the label-row doesn't re-introduce vertical stack on mobile.

## Flask static-asset Cache-Control

Flask's default static handler returns `Cache-Control: no-cache`. For a self-hosted dashboard, that's wrong — CSS/JS/logo rarely change between deploys, so use:

```python
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 300  # 5 min
```

Plus a defensive `after_request` for any non-`/static/` paths that also serve assets:
```python
@app.after_request
def _static_cache_headers(response):
    path = request.path or ""
    if path.startswith("/static/") or path.endswith((".css",".js",".png",".svg",".ico",".webp",".woff2")):
        response.headers["Cache-Control"] = "public, max-age=300"
    return response
```

Verify with `curl -fsSI http://host/static/css/style.css | grep -i cache-control` — must print `public, max-age=300`.

## Logo file size is real first-paint cost

A header logo used at 26×26 px but served from a 1024×1536 PNG at **2.08 MB** is wasteful. Resize once with PIL to the actual rendered size + a small margin (96×96 is fine for retina):

```python
from PIL import Image
im = Image.open(src).convert("RGBA")
im.thumbnail((96, 96))
im.save(out, optimize=True)
```

After: **6.9 KB** instead of 2 MB. Same visual result.

## "Look at the screenshot" workflow for this user

When the user sends screenshots and says "still not fix":
1. Look at the screenshot first (`vision_analyze` or native vision).
2. Identify the **literal** visual complaint — not a nearby improvement.
3. Apply a hard structural change (not a font/padding tweak).
4. Verify live in browser with `getBoundingClientRect()`.
5. Report concrete numbers, not adjectives ("GO width = 775px" beats "GO is bigger").

If the same complaint appears twice in a row, the previous interpretation was wrong. Restart from the literal screenshot.
