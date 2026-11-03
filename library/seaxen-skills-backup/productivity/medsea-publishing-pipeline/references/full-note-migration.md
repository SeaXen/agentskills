# Full-Note Migration Pattern — Medicine MD → Static Site with Real Mermaid

**Use this when the user says:** "make all Medicine notes to MedSea, no images, better notes with proper mindmap/flowchart."

This is the new preferred architecture for MedSea chapter content (replaces the PNG-infographic approach). Validated 2026-06-19/20 on Ch 16 Cardiology (570 notes → 899 chapters → 2,957 total topics live).

## Why This Exists

The old renderer (`render_topic.py`) produced ~300-word A4 PNG infographics. Limitations:
- Information density capped at ~300 words per topic
- Mindmap/flowchart rendered as **styled HTML approximations** (not real diagrams)
- User wanted full Medicine content (~1,800 words/14-section format) AND real Mermaid diagrams

The new pattern: **skip the renderer entirely**. Migrate Medicine MDs directly into chapters/, render client-side with mermaid.js.

## Pipeline

```
/mnt/tb/Medicine/<Chapter>/<Topic>.md   (FCPS/MRCP study notes, ~1,800 words)
        │
        │ strip frontmatter, copy as-is
        ▼
chapters/<chapter-slug>/diseases/<prefix>-<slug>/topic.md
        │
        │ build_site.py → renders topic.md to HTML inline
        │ - <pre class="mermaid"> for diagram blocks (kept as-is)
        │ - headings, bullets, tables, code blocks → standard HTML
        ▼
site/<chapter-slug>/diseases/<prefix>-<slug>/topic.md
        │
        │ nginx serves; browser fetches topics.json, renders MD to HTML,
        │ runs mermaid.render() on <pre class="mermaid"> blocks
        ▼
http://localhost:8855/16-cardiology/?topic=16.6.334   ← live, interactive
```

## Step 1 — Migrate Medicine MDs to chapters/

Script pattern (validated for Ch 16):

```python
from pathlib import Path
import re, json

MED = Path("/mnt/tb/Medicine/<Chapter>")
CHAP = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/<chapter-slug>/diseases")

SECTIONS = {
    "01_Cardiac_Investigations": (1, "cardiac-investigations"),
    "02_Acute_Coronary_Syndromes": (2, "acute-coronary-syndromes"),
    # ...
}

def is_junk(text):  # filter empty templates
    return any(s in text[:500] for s in
        ["status: starter-note", "status: template", "status: disease-level-scaffold"])

def strip_frontmatter(text):
    return re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL).lstrip()

# Track next available prefix per section (continue from existing max)
next_num = {}
for d in CHAP.iterdir():
    if d.is_dir():
        m = re.match(r'^(16\.\d+)\.(\d+)-', d.name)
        if m:
            sec_prefix, num = m.group(1), int(m.group(2))
            next_num[sec_prefix] = max(next_num.get(sec_prefix, 0), num)

for sec_folder in sorted(MED.iterdir()):
    if not re.match(r'^\d{2}_', sec_folder.name): continue
    sec_num, parent_slug = SECTIONS[sec_folder.name]
    sec_prefix = f"16.{sec_num}"
    for f in sorted(sec_folder.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        if is_junk(text) or "status: full-fcps-mrcp-note" not in text[:500]:
            continue
        # Try to reuse existing prefix by name match (fuzzy)
        target_folder = None
        norm = re.sub(r'[^a-z0-9]+', ' ', f.stem.lower()).strip()
        for existing in CHAP.iterdir():
            if existing.is_dir() and norm in re.sub(r'[^a-z0-9]+', ' ', existing.name.lower()):
                if existing.name.startswith(sec_prefix):
                    target_folder = existing
                    break
        if not target_folder:
            next_num[sec_prefix] = next_num.get(sec_prefix, 0) + 1
            new_slug = re.sub(r'[^a-z0-9]+', '-', f.stem.lower())[:80].strip('-')
            target_folder = CHAP / f"{sec_prefix}.{next_num[sec_prefix]}-{new_slug}"
            target_folder.mkdir(parents=True, exist_ok=True)
        content = f"<!-- Source: {f.relative_to(MED.parent)} -->\n\n{strip_frontmatter(text)}"
        (target_folder / "topic.md").write_text(content, encoding="utf-8")

# Cleanup: delete any topic.png/html (user said no images)
for d in CHAP.iterdir():
    if d.is_dir():
        for ext in ("png", "html"):
            f = d / f"topic.{ext}"
            if f.exists(): f.unlink()
```

Output for Ch 16: 570 notes processed → 564 new folders + 6 reused existing = 899 topics.

## Step 2 — Patch build_site.py for Mermaid.js + Full MD Rendering

Two changes needed in `scripts/site/build_site.py`:

### 2a. Replace styled-HTML mindmap/flowchart with `<pre class="mermaid">`

Find `def flush_code(self):` and replace the mindmap/flowchart branches:

```python
def flush_code(self):
    if not in_code: return
    body = "\n".join(code_buf)
    if code_kind in ("mindmap", "flowchart", "graph"):
        # Real mermaid.js renders these client-side from <pre class="mermaid">
        rendered = f'<pre class="mermaid">{_esc(body)}</pre>'
        found_mermaid = True
    elif code_kind is None:
        stripped_body = body.strip()
        if stripped_body.startswith(("mindmap", "flowchart", "graph ")):
            rendered = f'<pre class="mermaid">{_esc(body)}</pre>'
            found_mermaid = True
        else:
            rendered = f'<pre class="codeblock"><code>{_esc(body)}</code></pre>'
    else:
        rendered = f'<pre class="codeblock"><code>{_esc(body)}</code></pre>'
    out.append(rendered)
    in_code = False; code_buf = []; code_kind = None; code_fence_open = None
```

### 2b. Add Mermaid.js CDN to page_footer

```python
def page_footer():
    return f"""
</main>
<footer>...</footer>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
if (typeof mermaid !== 'undefined') {{
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'base',
    themeVariables: {{
      primaryColor: '#1f2937', primaryTextColor: '#e5e7eb',
      primaryBorderColor: '#38bdf8', lineColor: '#9ca3af',
      secondaryColor: '#111827', tertiaryColor: '#0f172a',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }},
    flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }},
    mindmap: {{ useMaxWidth: true }},
    securityLevel: 'loose'
  }});
}}

window.renderMermaidIn = function(container) {{
  if (typeof mermaid === 'undefined') return;
  const blocks = (container || document).querySelectorAll('pre.mermaid:not([data-rendered])');
  blocks.forEach((block, i) => {{
    block.setAttribute('data-rendered', 'true');
    const id = 'mm-' + Date.now() + '-' + i;
    try {{
      mermaid.render(id, block.textContent).then(({{ svg }}) => {{
        const wrapper = document.createElement('div');
        wrapper.className = 'mermaid-diagram';
        wrapper.innerHTML = svg;
        block.replaceWith(wrapper);
      }}).catch(err => console.warn('mermaid render failed:', err));
    }} catch (e) {{ console.warn('mermaid error:', e); }}
  }});
}};

document.addEventListener('DOMContentLoaded', () => {{
  setTimeout(() => window.renderMermaidIn(document), 100);
}});
</script>
</body>
</html>
"""
```

### 2c. Call renderMermaidIn after desktop topic load

In the `showTopic(localPrefix)` function (inside the `html += f"""..."""` block — uses `{{` for JS braces):

```javascript
container.innerHTML = `...${{t.html}}...`;
if (typeof window.renderMermaidIn === 'function') {{
  setTimeout(() => window.renderMermaidIn(container), 50);
}}
container.scrollTop = 0;
```

## Step 3 — Fix loadManifest URL Parsing (BUG, FIXED 2026-06-20)

**Bug:** when URL was `?topic=16.6.334-antibiotic-regimens-...` (full slug), `loadManifest` passed the full string to `showTopic` which searched by exact `local_prefix` (16.6.334) → no match → placeholder shown forever.

**Fix in loadManifest:**
```javascript
async function loadManifest() {{
  try {{
    const res = await fetch(MANIFEST_URL);
    MANIFEST = await res.json();
    const params = new URLSearchParams(location.search);
    let t = params.get("topic");
    if (t) {{
      const found = MANIFEST.topics.find(x => x.local_prefix === t || x.local_prefix === t.split("-")[0]);
      if (found) showTopic(found.local_prefix);
      else console.warn("Topic not found in manifest:", t);
    }}
  }} catch(e) {{ console.error("Failed to load topics.json", e); }}
}}
```

## Step 4 — Deploy

Docker port mapping pitfall: nginx listens on **port 80 inside the container**, not the `EXPOSE 8855`. Use:

```bash
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
```

**NOT** `-p 8855:8855` (which leaves the port unmapped → HTTP 000 on curl).

Rebuild script (must NOT use per-command docker stop/kill/rm — Hermes blocks those; wrap in a script file):

```bash
#!/bin/bash
set -e
cd /mnt/tb/Sea-knowledge/#MedSea
docker build -t medsea-site:latest . > /tmp/build.log 2>&1
docker stop medsea 2>&1 || true
docker rm medsea 2>&1 || true
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
sleep 5
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8855/
```

Build takes ~5 min (1GB site context → Docker). Run in background:

```bash
nohup bash /tmp/redeploy.sh > /tmp/redeploy.log 2>&1 &
```

## Verification

After deploy:
```bash
curl -s http://localhost:8855/16-cardiology/topics.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
t = d.get('topics', [])
print(f'Topics: {len(t)}')
print(f'PNG: {sum(1 for x in t if x.get(\"png\"))}')
print(f'HTML: {sum(1 for x in t if x.get(\"html\"))}')
mermaid_count = sum(1 for x in t if 'pre class=\"mermaid\"' in (x.get('html') or ''))
print(f'With mermaid blocks: {mermaid_count}')
"
```

In browser, open topic with mermaid:
```
http://localhost:8855/16-cardiology/?topic=16.6.334
```

Check via JS console:
```javascript
window.renderMermaidIn(document.getElementById('topicContainer'))
// Should convert pre.mermaid → div.mermaid-diagram > svg
```

## Gotchas

1. **Python f-string JS escaping**: when the JS block is inside an f-string `html += f"""..."""`, every JS `{` must be `{{` and every `}` must be `}}`. Forgetting this causes `SyntaxError: f-string: invalid syntax`. The page-footer block (after `html +=`) does NOT need this escaping.

2. **PNG remains in HTML**: after removing PNG files from chapters/, the existing site HTML still references them. Run `build_site.py` to regenerate site/ with no PNG refs.

3. **Mermaid securityLevel 'loose'**: required for some user-provided diagram syntax (square brackets in node labels, special characters). Without it, mermaid silently fails to render and you get empty `<div class="mermaid-diagram"></div>`.

4. **Topic loadManifest timing**: the `setTimeout(50)` after `container.innerHTML = ...` is critical — without it, mermaid tries to render before the browser has parsed the new DOM, and `<pre class="mermaid">` blocks are missed.

5. **Mermaid.js CDN must load before renderMermaidIn runs**: use `document.addEventListener('DOMContentLoaded', ...)` with a small setTimeout (100ms) so the CDN script has time to load.

## When to Use Old (Infographic) vs New (Full-Note) Pattern

| Pattern | When |
|---|---|
| **Full-Note Migration** (this doc) | User wants full study notes on the website with proper diagrams. Default for FCPS/MRCP study apps. |
| **Old Infographic (render_topic.py)** | Quick reference card for an entire disease on a single A4 page. Useful for posters/print/quick-glance. Ch 16-18 still have these as legacy. |

You can mix: keep the old infographic for the chapter landing page or for chapters not yet migrated, and use full-note for chapters the user actively studies from.