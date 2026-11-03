# Renderer Pitfalls — Full Failure Modes

Renderer: `/root/sea-knowledge-infographics/render_topic.py`
Signature: `--slug <slug> --title <title> --markdown-file <path> --out-dir <path> --tag <tag>`

## Output Path Quirk (MOST IMPORTANT)

The renderer creates a **subdirectory named after the slug** inside the output dir. Output is nested one level deeper than expected:

```
--out-dir /path/to/topic_dir
  → /path/to/topic_dir/<slug>/<slug>.html
  → /path/to/topic_dir/<slug>/<slug>.md
  → /path/to/topic_dir/<slug>/<slug>.png
```

NOT:
```
/path/to/topic_dir/<slug>.png  (what you might expect)
```

**Fix options**:
- (A) Pass `--out-dir <parent_of_topic_dir>`, then look for output in `<parent>/<slug>/`
- (B) Pass `--out-dir <topic_dir>`, then **move files up** with `scripts/flatten_renderer_output.py`
- (C) Pass `--out-dir <topic_dir>` and expect `topic_dir/<slug>/<slug>.png` everywhere

**Most builds use option (B)** — create the topic_dir, run renderer with `--out-dir topic_dir`, then flatten.

## Unnumbered `##` Headers → Infinite Loop

The renderer's `parse_markdown_to_html` function expects `##` headers to have a **numeric prefix**:

```
## 1. Section Title        ✅ works
## 2. Another Section      ✅ works
## Section Without Number  ❌ infinite loop
```

**Symptom**: Renderer hangs indefinitely, no output, 60s timeout triggers.

**Root cause**: A `## 24-Hour Recall Prompts` section header in the source MD (from the "Spaced Repetition Trackers" template) doesn't match the regex `^## \d+\.`, so the parser falls into a default branch that increments a counter forever.

**Fix history**:
- 2026-06-19: Renderer patched to tolerate non-numeric headers (skip them as `### ` subheadings)

**Pre-processing workaround** (if you can't update the renderer):

```python
def auto_number_headers(text):
    counter = [0]
    def replacer(m):
        counter[0] += 1
        return f"## {counter[0]}. {m.group(1).strip()}"
    return re.sub(r"^##\s+(?![\d.])(.+)$", replacer, text, flags=re.MULTILINE)
```

This converts `## Bare Header` → `## N. Bare Header` before rendering.

## Mermaid mindmap/flowchart Not Rendered

Before 2026-06-19, the renderer showed mermaid code blocks as raw text:

````
```mindmap
  root((Topic))
    Subtopic A
    Subtopic B
```
````

**Fix**: Added `render_mindmap()` and `render_flowchart()` functions that parse mermaid syntax and produce visual HTML:

```html
<ul class="mindmap">
  <li class="mm-root">Topic</li>
  <li class="mm-branch">Subtopic A</li>
  <li class="mm-branch">Subtopic B</li>
</ul>
```

```html
<div class="flowchart">
  <div class="fc-node">Start</div>
  <div class="fc-arrow"></div>
  <div class="fc-node">Decision</div>
  ...
</div>
```

CSS for `.mindmap`, `.mm-root`, `.mm-branch`, `.flowchart`, `.fc-node`, `.fc-arrow` was added to the HTML template.

**Affected templates**: source MDs that include mindmap/flowchart code blocks. The Davidson 25th Ed Ch 1-9 sources had several; after the fix, they render as nested visual trees.

## Large MDs Hang (>400 lines)

**Symptom**: Renderer hits 60s timeout, no PNG output, no error.

**Root cause**: The HTML→PNG conversion (headless Chromium) hangs on long content.

**Fix**: Truncation retry pattern:

```python
def render_with_retry(text, slug, title, out_path, tag, max_lines=200):
    """Try full, then retry with truncation."""
    try:
        render_topic(text, slug, title, out_path, tag)
    except TimeoutError:
        # Truncate and retry
        truncated = "\n".join(text.split("\n")[:max_lines])
        truncated += f"\n\n*...truncated to {max_lines} lines for renderer*"
        render_topic(truncated, slug, title, out_path, tag)
```

**Tradeoff**: Truncated content is incomplete in the PNG. The MD file still has the full content; only the PNG visualization is partial.

**Validated working**: Ch 11 Poisoning (37 topics), Ch 13.1.05 (Environmental Chemical Hazards, 330 lines), Ch 14.1.42 (Sepsis, 578 lines).

## YAML Frontmatter Must Be Stripped

The Davidson source MDs include YAML frontmatter that the renderer doesn't understand:

```yaml
---
title: Acute Coronary Syndrome
tags: [cardiology, emergency]
status: full-fcps-mrcp-note
---
```

**Pre-process before render**:

```python
text = md_path.read_text(encoding="utf-8", errors="replace")
if text.startswith("---"):
    end = text.find("\n---", 3)
    if end != -1:
        text = text[end + 4:].lstrip()
# Also remove H1 (we add it via --title)
text = re.sub(r"^#\s+.+?\n", "", text, count=1).strip()
```

## Renderer Returns OK But No PNG

Sometimes the renderer exits 0 but only writes the HTML and MD, not the PNG. Causes:
- Chromium not available
- Out of memory
- Headless browser crash on malformed HTML

**Workaround**: Re-render with truncation (forces smaller output that succeeds).

## Batch Renderer Behavior

When running in batch (subprocess per topic), each topic:
- 1-3 seconds typical
- 60s timeout for large files
- HTML+MD written to `<out>/<slug>/<slug>.{html,md}` first
- PNG rendered from HTML last

If multiple topics in a chapter fail, check the renderer version and source MD for the specific failure mode.

## Verifying Renderer Output

After running build_chapter.py for a chapter, verify:

```bash
# Every topic should have all 3 files
for topic_dir in chapters/<slug>/diseases/*/; do
  slug=$(basename "$topic_dir")
  for ext in md html png; do
    if [ ! -f "$topic_dir/${slug}.${ext}" ] && [ ! -f "$topic_dir/topic.${ext}" ]; then
      echo "MISSING: $topic_dir/${slug}.${ext} (or topic.${ext})"
    fi
  done
done
```

## Common Renderer Bug: Nested output After Re-render

When re-rendering a topic that already has files in `topic_dir/`, the renderer writes NEW files to `topic_dir/<slug>/` but the OLD files at `topic_dir/topic.png` remain. This creates duplicates.

**Fix**: Always start with a clean `topic_dir` for each render, OR check both `topic.png` and `<slug>/<slug>.png` locations.

The build script uses **option (B) — flatten after render** which is robust:

```python
# 1. mkdir -p topic_dir
# 2. Run renderer with --out-dir topic_dir
# 3. Move files from topic_dir/<slug>/ to topic_dir/
# 4. rmdir topic_dir/<slug>/
```
