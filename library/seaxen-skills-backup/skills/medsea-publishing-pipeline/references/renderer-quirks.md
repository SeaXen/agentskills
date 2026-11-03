# Renderer Quirks — `/root/sea-knowledge-infographics/render_topic.py`

Validated quirks as of 2026-06-19. Read this before building a new chapter.

## Header Format: `## N. Title` Required

The renderer's `parse_markdown_to_html()` expects headers to be **numeric-prefixed**:
- ✅ `## 1. Definition`
- ✅ `## 2. Epidemiology`
- ❌ `## Definition` (unnumbered — caused infinite loop, see below)

**Pre-process all source MDs** before rendering: strip YAML frontmatter, strip H1, then auto-number any unnumbered `##` headers. Reference pre-processor is in `build_ch10_15.py`:
```python
counter = [0]
def replacer(m):
    counter[0] += 1
    return f"## {counter[0]}. {m.group(1).strip()}"
text = re.sub(r"^##\s+(?![\d.])(.+)$", replacer, text, flags=re.MULTILINE)
```

## Infinite Loop on Unnumbered `##` Headers (FIXED 2026-06-19)

`## 24-Hour Recall Prompts` and similar unnumbered H2 headers caused `parse_markdown_to_html` to hang indefinitely (no timeout — process ran forever). Root cause: the parser incremented a counter only on numeric-prefixed `##`, but the body-collection code expected a single section per iteration; when no numeric prefix matched, the counter never advanced and the loop never exited.

**Fix:** the parser now skips/tolerates non-numeric `##` headers. If you update the renderer, preserve this behavior.

## Output Path is `out_dir/slug/{slug}.{png,html,md}` — NOT `topic.{ext}`

The renderer's `--out-dir` flag is the PARENT directory. It creates a subdirectory named after the slug and writes 3 files inside:
```
out_dir/
└── <slug>/
    ├── <slug>.png
    ├── <slug>.html
    └── <slug>.md
```

**After rendering, you must FLATTEN** to `diseases/<prefix>-<slug>/topic.{md,html,png}` before `build_site.py` will find the PNGs. Reference flatten pattern:
```bash
mv "<out_dir>/<slug>/<slug>.png" "<diseases_dir>/<prefix>-<slug>/topic.png"
mv "<out_dir>/<slug>/<slug>.html" "<diseases_dir>/<prefix>-<slug>/topic.html"
mv "<out_dir>/<slug>/<slug>.md" "<diseases_dir>/<prefix>-<slug>/topic.md"
rmdir "<out_dir>/<slug>"
```

(`build_site.py`'s `find_files()` was updated to look for `topic.png` flat in topic dir; older versions expected `<slug>.png`.)

## Mermaid Code Blocks Need Explicit Handling (ADDED 2026-06-19)

The renderer doesn't auto-parse mermaid. The source MDs include ```mindmap``` and ```flowchart``` code blocks for visual diagrams. These need to be rendered as visual HTML (nested `<ul class="mindmap">`, styled `<div class="flowchart">` with boxes/arrows).

If you add a new diagram type, add a `render_<type>()` function in `render_topic.py` BEFORE `render_inline()`, then add a detection branch in `render_inline()`. Also add the corresponding CSS in the HTML template.

## Truncation Retry on Hang/Timeout

For source files > 200 lines, the renderer can hang or timeout. Pattern:
```python
def render_topic(md_text, slug, title, out_path, tag, truncate_to=None):
    if truncate_to:
        lines = md_text.split("\n")
        if len(lines) > truncate_to:
            md_text = "\n".join(lines[:truncate_to]) + f"\n\n*...truncated to {truncate_to} lines*"
    # ... subprocess.run with timeout=60
```

Validated for Ch 11 Poisoning (37/37) and Ch 12 Envenomation (13/13) using 120-line truncation. For Ch 13.1.05 (Environmental Medicine) and Ch 14.1.42 (Sepsis) — 200-line truncation worked.

## Renderer Signature (CLI)

```
python3 render_topic.py \
    --slug <slug> \
    --title "<title>" \
    --markdown-file <path> \
    --out-dir <parent_dir> \
    --tag <chapter_label>
```

Returns exit 0 on success, non-zero on failure. Use `subprocess.run` with `timeout=60-180s`.

## Common Failure Modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Process hangs forever | Unnumbered `##` header in source | Already fixed in renderer; if regressed, patch parser to skip non-numeric `##` |
| Process times out at 60s | Source file too long | Truncate to 100-200 lines and retry |
| Empty `topic.png` (< 50KB) | Renderer succeeded but template didn't fit content | Check renderer logs; re-render with different truncation |
| Mermaid blocks show as raw code | Renderer not handling mermaid | Add `render_mindmap()` / `render_flowchart()` functions |
| Output at `<out_dir>/<slug>/<slug>.{ext}` but `build_site.py` finds nothing | Renderer nested output not flattened | Run flatten step before site build |
