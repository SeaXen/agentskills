---
name: mermaid-static-html
description: Render mermaid mindmap/flowchart/graph syntax into clean self-contained HTML for static sites — no mermaid.js dependency. Use when building static knowledge bases, offline documentation, or any site that needs visual diagrams without runtime JS libraries.
---

# Mermaid → Static HTML Renderer

Render mermaid `mindmap`, `flowchart`, and `graph` blocks into styled HTML at build time. The output is self-contained — no mermaid.js, no client-side JS, no SVG/Canvas dependencies. Works in any browser, prints cleanly, and indexes well.

## When to use

- Building a static-site knowledge base from markdown (medical notes, study cards, documentation)
- Need diagram visuals but cannot or do not want to ship mermaid.js / katex / external CDN
- Want print/PDF-friendly output
- Want the rendered HTML to be tiny (a few KB per diagram) and load instantly

## When NOT to use

- Real-time diagram editing — use mermaid.js live editor instead
- Highly complex mermaid syntax (sequenceDiagram with notes, classDiagram with generics, gantt charts with excludes) — limit support to the common cases below
- Output needs to be editable as mermaid source — provide the original code block alongside

## Supported mermaid syntax

| Type | Example | Render style |
|------|---------|--------------|
| mindmap | `mindmap\n  root((Topic))\n    Branch\n      Leaf` | Root pill + branch cards + leaf nodes, hierarchy via indentation |
| flowchart TD/LR | `flowchart TD\n  A[Start] --> B{Decision?}\n  B -->|Yes| C[OK]` | Vertical or horizontal flow with rounded/decision/node shapes |
| graph TD/LR | `graph TD\n  A --> B` | Same as flowchart |
| sequenceDiagram | partial — only first 2 actors | Simplified |

## Critical: shape-aware label extraction

Mermaid uses bracket pairs around node labels. The number of brackets determines the shape:

| Shape | Brackets | Strip |
|-------|----------|-------|
| Default | `text` | 0 chars |
| Rounded rect | `[text]` | 1 each end |
| Circle | `(text)` | 1 each end |
| Cloud | `)text(` | 1 each end |
| Hexagon | `{{text}}` | **2 each end** (double-brace) |
| Bang / asymmetric | `))text((` | **2 each end** |
| Trapezoid | `[/text/]` | 2 each end |
| Parallelogram | `[/text/]` or `[\text\]` | 2 each end |

**Gotcha**: a naive `lbl[1:-1]` strips 1 char regardless of shape — this corrupts hexagons (`{{Amyloid}}` becomes `{Amyloid}` instead of `Amyloid`). Always match the bracket count on both ends.

**Gotcha #2**: malformed hexagons like `{{Amyloid} Sarcoidosis}` (missing one closing brace) need a regex-based fallback that finds the LAST matching closing pair.

## Critical: multi-line edge labels

Mermaid allows:

```
A -->|Multi-line
edge label
that spans lines| B
```

You must **join consecutive lines** until the bracket pair (`|...|`) balances. Use a state machine:

```python
buf = []
in_label = False
for line in lines:
    if "|" in line and not in_label:
        in_label = True
        # start collecting
    if in_label:
        buf.append(line)
        if line.count("|") >= 2 and line.rstrip().endswith("|"):
            # label complete
            label = " ".join(buf).strip("|")
            in_label = False
            buf = []
```

## Critical: malformed input handling

Real-world mermaid content often has:
- Unclosed brackets (`A[Start --> B`)
- Empty node IDs (`--> text`)
- Mixed indentation (tabs vs spaces)
- Comments inside labels
- Unicode arrows (`→`, `↓`) that look like `-->`

Pre-process with a permissive regex pattern that captures whatever it can:

```python
# node_m pattern: matches `id<whitespace>delimiters<text>delimiters`
node_pattern = re.compile(
    r'(\w*)\s*'              # optional node ID
    r'([\(\[\{]{1,2})\s*'     # 1 or 2 opening brackets
    r'([^()\[\]{}\n]*?)'      # label text (no nested brackets)
    r'\s*([\)\]\}]{1,2})'     # 1 or 2 closing brackets
)
```

If the regex fails, fall back to:
- Use the entire line as the label
- Use the node ID as the label
- Skip the node entirely (better than garbage)

## Build integration pattern

Most static-site generators can call a Python function during build:

```python
def render_md_with_visuals(md_text):
    """Process markdown, replacing ```mermaid blocks with rendered HTML."""
    parts = []
    i = 0
    while i < len(md_text):
        fence_start = md_text.find("```mermaid", i)
        if fence_start < 0:
            fence_start = md_text.find("```mindmap", i)
        if fence_start < 0:
            fence_start = md_text.find("```flowchart", i)
        if fence_start < 0:
            parts.append(md_text[i:])
            break
        parts.append(md_text[i:fence_start])
        fence_end = md_text.find("```", fence_start + 3)
        if fence_end < 0:
            parts.append(md_text[i:])
            break
        mermaid_text = md_text[fence_start:fence_end+3]
        kind = detect_kind(mermaid_text)
        if kind == "mindmap":
            html = render_mindmap(mermaid_text)
        elif kind in ("flowchart", "graph"):
            html = render_flowchart(mermaid_text)
        else:
            html = f'<pre class="codeblock">{mermaid_text}</pre>'
        parts.append(html)
        i = fence_end + 3
    return "".join(parts)
```

## Auto-synthesis fallback (NEW PATTERN)

When source markdown has NO mermaid blocks, synthesize a mindmap from heading structure. This guarantees every topic page has a visual even if the author never wrote mermaid syntax.

```python
def synthesize_mindmap_from_headings(md_text):
    headings = []
    for line in md_text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = clean_heading(m.group(2))
            headings.append((level, text))

    if len(headings) < 2:
        return ""

    # First H1 = root, H2/H3 = branches
    root = ""
    items = []
    for lvl, txt in headings[:40]:
        if lvl == 1 and not root:
            root = txt
            continue
        if lvl in (2, 3):
            items.append((lvl, txt))

    if not root and items:
        root = items.pop(0)[1]
    if not root:
        return ""

    # Build mermaid text and run through normal renderer
    lines = ["mindmap", f"  root(({root}))"]
    for lvl, txt in items[:30]:
        indent = "    " if lvl == 2 else "      "
        lines.append(f"{indent}{txt}")
    return render_mindmap("\n".join(lines))
```

This pattern is critical for content-heavy sites (medical notes, documentation, study guides) where most authors don't write mermaid blocks but every topic benefits from a visual.

## CSS styling

A consistent visual style for the rendered diagrams:

```css
.mindmap {
  background: linear-gradient(135deg, #fff8e7 0%, #fdf3e0 100%);
  border: 1px solid var(--cream-deep);
  border-radius: 8px;
  padding: 16px;
  text-align: center;
}
.mm-root {
  display: inline-block;
  background: #2c3e50;
  color: #fff;
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 700;
  margin-bottom: 12px;
}
.mm-branches {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}
.mm-branch {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 10px;
  min-width: 120px;
}
.mm-node.mm-l1 { color: var(--accent); font-weight: 600; }
.mm-node.mm-l2 { color: var(--text-dim); font-size: 0.9em; padding-left: 8px; }

.flowchart {
  background: linear-gradient(135deg, #f5f0e2 0%, #ece1c8 100%);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
}
.fc-title {
  text-align: center;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--accent);
}
.fc-level {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 8px;
}
.fc-node {
  background: #fff;
  border: 2px solid var(--node-color, var(--accent));
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 0.9em;
}
.fc-arrows {
  text-align: center;
  color: var(--text-dim);
  margin: 4px 0;
}
```

## Verification

Always render a known fixture with each of these edge cases and assert:
- Hexagon label: `{{Hexagon Topic}}` → renders as "Hexagon Topic"
- Multi-line edge: `A -->|Two word\nlabel| B` → edge label is "Two word label"
- Multi-line node: `A[Line 1\nLine 2]` → node label is "Line 1 Line 2"
- Malformed hex: `{{Missing` → falls back to "Missing" (no garbage chars)
- Empty ID: `A[Node] --> B` → renders node "A" and "B" both with labels
- Synthesized from headings → root = first H1, branches = H2/H3

See `scripts/extract_label.py` for a working `_extract_label()` helper that handles all these cases. Run with `--test` to verify all 12 fixtures pass.

## Support files

- `scripts/extract_label.py` — `_extract_label()`, `normalize_node_id()`, `parse_node_decl()` functions with 12 verification fixtures. Drop into any Python project.
- `references/edge-cases.md` — concrete failure modes from the MedSea site build (hexagon strip counts, multi-line edge buffering, malformed hexagons), auto-synthesis coverage data (1,346 → 2,604 mindmaps), universal search scoring pattern, Docker port-mapping pitfall, DOM-based verification when vision is offline.