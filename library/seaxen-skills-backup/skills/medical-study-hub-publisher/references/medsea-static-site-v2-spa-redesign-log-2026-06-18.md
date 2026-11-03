# MedSea Static Site v2 Redesign — 2026-06-18

## Context
Phase 7 v1 (see `medsea-static-site-build-log-2026-06-18.md`) shipped a 3-tier static site (landing → chapter → topic) with a hero text and per-topic HTML pages. The user came back with specific corrections and a feature request that drove a v2 redesign of the build script (`scripts/site/build_site.py`).

## User feedback (verbatim)
> *"remove those hero text and move those stat to header and chapter name move below header with good arrangement below chapters, also make a dropdown option in header and like chapter > topic > left or right side show sub topic"*

The user also handed over the **full Davidson 25th Edition chapter list (32 chapters)** so the dropdown could show every chapter with a "coming soon" badge for the 27 not yet built. Translation for the build:

| User request | Implementation |
|---|---|
| Remove hero text | Drop the `<h1>MedSea</h1>` + subtitle + `.hero` stats block from `index.html` |
| Move stats to header | Stats pills inline in the sticky header; per-page counts override on chapter pages |
| Chapter names below header | Chapter grid becomes the main content of `index.html` |
| Dropdown in header | Full 32-chapter dropdown (5 LIVE + 27 SOON) with accent-color "Live" badge |
| Chapter > Topic > sub-topic | Per-chapter SPA: left sidebar (searchable topic list grouped by hub) \| right pane (selected topic content) |

## New architecture (v2)

### Landing (`index.html`)
- Sticky header: logo + stats pills + chapter dropdown + GitHub link
- No hero
- Single `<div class="chapters-grid">` of chapter cards
- Stats pills show: `5 Chapters · 52 Hubs · 762 Topics · 760 PNGs · 32 Total (25th)`

### Chapter SPA (`<chapter-slug>/index.html`)
- Same header (with per-chapter stat pills)
- Two-column layout:
  - **Left sidebar** (320px, sticky): search input + topic list grouped by hub
  - **Main pane**: chapter header + `<div id="topicContainer">` that the JS populates
- One `<script>` block at the bottom that:
  1. `fetch()`es `<chapter-slug>/topics.json` on load
  2. Reads `?topic=<local_prefix>` from URL
  3. Calls `showTopic(local_prefix)` to populate the right pane
  4. Sidebar search filters topics + empty hub groups in real time
  5. `navigateTopic(±1)` for prev/next buttons

### topics.json manifest (the key innovation)
Instead of N pre-rendered per-topic HTML files, the build generates **one JSON per chapter** with all topic HTML pre-rendered into a `topics[]` array. The SPA fetches it once on load (~50-300 KB per chapter depending on topic count), then topic switching is instant — no per-topic page request needed.

```json
{
  "chapter": "16-cardiology",
  "chapter_name": "Cardiology",
  "notion_url": "https://app.notion.com/p/SeaHub/...",
  "accent_color": "#ef4444",
  "topics": [
    {
      "local_prefix": "16.1.25",
      "hub_num": "16.1",
      "hub_name": "Acute Coronary Syndromes",
      "slug": "atherosclerosis-pathogenesis",
      "title": "Atherosclerosis Pathogenesis",
      "png": "diseases/16.1.25-atherosclerosis-pathogenesis/topic.png",
      "md": "diseases/16.1.25-atherosclerosis-pathogenesis/topic.md",
      "html": "<h2>1. Introduction</h2>..."
    },
    ...
  ]
}
```

Generated in `write_chapter_spa()` inside `build_site.py` by looping over `info["by_hub"]`, pre-rendering each topic's MD via `render_md_to_html()`, and dumping the whole list via `json.dumps()`.

### 32-chapter dropdown
Inline Python list in `build_site.py` — `DAVIDSON_25TH` — with `(dav_num, name, built_slug_or_None)` tuples. Live chapters (5 of them) render as clickable items with accent-color "Live" badge; the other 27 render as greyed-out "Soon" items with an `onclick` that shows an alert and `event.preventDefault()` to suppress navigation. Built chapters list (`BUILT_CHAPTERS`) maps `built_slug → (name, notion_url, desc, accent_color)`.

The mapping handles MedSea's number-vs-Davidson numbering mismatch (MedSea stores Nephrology at `15-nephrology-urology` even though Davidson has it at 18; Endo at 18 even though Davidson has it at 20; Gastro at 21 even though Davidson has it at 22). The dropdown shows the **MedSea** number for live chapters (matches the actual URL), and the **Davidson** number for "coming soon" items.

## Pitfalls encountered in v2

### Pitfall 65 — Don't put the build script inside `site/` if `site/` gets `shutil.rmtree()`'d
The Phase 7 v1 build script lived at `scripts/site/build_site.py`. But the build does `if SITE.exists(): shutil.rmtree(SITE)` at the start, which **deletes the entire `site/` tree including any nested `scripts/`**. The build then can't re-run because its own source is gone.

Fix: keep `scripts/site/` as a sibling of `site/`, not a child. Both live directly under `/mnt/tb/Sea-knowledge/#MedSea/`. Verify with `ls -la scripts/site/build_site.py site/index.html` — they must be in different top-level dirs from `site/`.

### Pitfall 66 — Don't accidentally delete `site/README.md` in `rmtree(SITE)`
The README documents how to build + deploy the site. It's tracked in git and committed to the repo. But `shutil.rmtree(SITE)` deletes it along with everything else.

Fix: re-create the README at the top of `main()` after the rmtree. Store the README content as a Python constant (`_README_MD = """..."""`) inside `build_site.py` so the build is self-contained and doesn't depend on any pre-existing files. Same pattern works for any other small "framework" files in `site/` (favicons, robots.txt, manifest.json for PWA, etc.).

### Pitfall 67 — Inline event-handler strings inside f-strings need `{{`/`}}` doubling for literal braces
The build script generates a `<script>` block inside a Python f-string. JS code has `{` and `}` for blocks/objects. To produce literal `{` in the output, you must double them in the f-string source: `{{` → `{`, `}}` → `}`.

```python
# WRONG — f-string treats { as expression delimiter
html += f"""
<script>
function showTopic(localPrefix) {{
  const el = document.querySelector(`[data-topic="${{localPrefix}}"]`);
}}
</script>
"""
```

`{{` (open brace), `}}` (close brace) — the doubling is only needed inside the f-string. When the f-string evaluates, you get the literal single braces.

**Pitfall-within-pitfall:** if you forget to double ONE brace (e.g. the closing one), Python raises `SyntaxError: f-string: invalid syntax` at compile time. The error is unhelpful — it points at the line of the f-string but doesn't tell you which brace you missed.

### Pitfall 68 — Don't compose complex JS expressions as inline `onclick="..."`
My first pass at prev/next buttons had:
```html
<button onclick="location.href='/${{MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix && MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix}}?topic=' + (MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix)">← Prev</button>
```
— unmaintainable, full of bugs, and the `&&` short-circuit produces `undefined` when at index 0.

Fix: extract to a named function in the same `<script>` block:
```js
function navigateTopic(dir) {
  if (!MANIFEST || !CURRENT_TOPIC) return;
  const i = MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix);
  const ni = i + dir;
  if (ni < 0 || ni >= MANIFEST.topics.length) return;
  showTopic(MANIFEST.topics[ni].local_prefix);
}
```
Then buttons just call `navigateTopic(-1)` / `navigateTopic(1)`.

**Rule:** any JS that needs more than ~10 chars of logic goes in a named function. Don't inline complex logic in `onclick="..."`.

### Pitfall 69 — `?topic=<local_prefix>` URL param must match the exact key in `topics.json`
My first test was `?topic=16.1.25` for Cardiology, but the actual `local_prefix` is `16.1.25` (cardiology) vs `17.1.01` (respiratory uses leading zero). The topic won't load if the prefix doesn't match exactly.

**Solution options:**
1. Make `local_prefix` URL-safe and stable (always zero-pad to 2 digits: `16.1.25` not `16.1.025` — but the existing convention varies per chapter)
2. Or: search the manifest for the closest matching prefix on load (fuzzy)
3. Or: accept that the URL uses the canonical `local_prefix` as-is — document the convention

Currently: option 3. Sidebar clicks always use the right prefix because they read `data-topic` from the rendered link, so direct URL entry is the only risk.

### Pitfall 70 — Browser snapshot / vision tools were down during v2 verification
The vision model returned `Error code: 400 - Unknown Model` repeatedly, and the user's reference image couldn't be auto-described. Worked around by:
- Using `browser_console(expression='document.querySelector(".topic-detail h1")?.textContent')` to verify topic content loaded
- Using `curl -s http://localhost:8855/...` + grep for class counts
- Capturing screenshots anyway (`browser_vision` returned them even when vision analysis failed) and sharing via `MEDIA:` paths

**Rule for "vision is down" sessions:** the user's previous request style is clear enough that text interpretation is usually fine. Don't block on vision; proceed with browser-console DOM probes and trust the user's text feedback. Note the limitation in the final response so the user knows to send more specific feedback if needed.

## What changed in `build_site.py` (v1 → v2 diff at high level)
- Added `DAVIDSON_25TH` and `BUILT_CHAPTERS` module constants
- Replaced `page_header()` to include chapter dropdown + per-page stats + GitHub link
- Replaced `write_chapter_page()` with `write_chapter_spa()` — generates topics.json + SPA HTML
- Removed hero block from `write_index()`; stats now go in header only
- Added `chapter_dropdown_html()` helper for the 32-chapter list
- Added `_README_MD` constant; `main()` re-creates `site/README.md` after `rmtree`
- Added `navigateTopic()` JS helper; simplified inline prev/next onclick
- Total file size: ~700 → ~1046 lines

## Verification
- `curl http://localhost:8855/` → 200, stats in header, no hero, dropdown has 32 items
- `curl http://localhost:8855/16-cardiology/topics.json | jq '.topics | length'` → 330
- Browser: drop chapter in dropdown → chapter SPA loads → sidebar lists 330 topics → click topic → right pane renders PNG + MD
- GitHub: commits `f594e63` (v2 redesign) + `a6d42b9` (README preservation) pushed to `SeaXen/MedSea` main

## When to use this doc vs. v1 reference
- **`medsea-static-site-build-log-2026-06-18.md`** (v1): Docker + nginx + Vercel + .gitignore for PNG binaries. Still relevant — all of that infra is unchanged.
- **This doc (v2)**: design decisions about layout (header stats, sidebar+main SPA, dropdown), the topics.json pattern, and pitfalls 65-70 specific to v2.

Future iterations should add a v3 doc with their own pitfalls numbered 71+ to keep the chain readable.
