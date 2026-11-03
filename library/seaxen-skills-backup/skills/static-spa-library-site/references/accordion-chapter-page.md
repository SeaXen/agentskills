# Accordion chapter page (hub + topic tree) reference

Companion to `static-spa-library-site` SKILL.md "Accordion chapter page" section. Replaces the old sidebar+main SPA with a full-width native `<details>` accordion tree that scales to 300+ topics per chapter without scrolling through a giant list.

## Why the accordion tree replaced sidebar+main

User feedback pattern across multiple sessions:

| Layout | Outcome | Problem |
|---|---|---|
| Sticky sidebar + main pane | Worked, but 300+ topics = huge scroll | User on mobile said "there are so many in mobile" — sidebar overwhelming |
| Collapsed groups in sidebar | Better, but still requires JS state | Hub state lost on reload, no deep-linkable URL |
| **Native `<details>` tree with inline content** | Clean on mobile + desktop, no JS state, deep-linkable | Slightly larger HTML (content embedded inline) |

The accordion tree is the right answer for content libraries where topics are self-contained pages of notes — the user wants to scan hubs, open one, scan topics, open one, read inline. No cross-topic navigation needed (universal header search handles "jump to topic X in chapter Y").

## Architecture

```
chapter-page (full width, single column)
├── chapter-header (title + meta + Notion link)
├── chapter-toolbar (sticky)
│   ├── search input (filters topics, auto-expands matching)
│   ├── Expand all button
│   └── Collapse all button
└── hub-accordion (vertical stack of <details>)
    └── hub-acc (one per hub)
        ├── summary (arrow + hub-num + hub-name + topic-count)
        └── hub-body
            └── topic-acc (one per topic in hub) [<details>]
                ├── summary (arrow + topic-num + topic-title)
                └── topic-body
                    ├── topic-content (rendered HTML from MD — embedded inline)
                    └── topic-image-toggle (collapsible PNG infographic)
```

**No JSON fetch. No JS state for navigation. All content is in the HTML.**

## Why embed content inline (vs. JSON fetch like the old SPA)

The old SPA fetched `topics.json` (700KB for cardiology) and rendered the selected topic into the main pane via JS. Trade-offs:

| | Old (JSON fetch) | New (inline `<details>`) |
|---|---|---|
| HTML size per chapter | ~50KB shell + 700KB JSON | ~2-5MB (all topic HTML embedded) |
| Time to first topic | 200-500ms (fetch + render) | **0ms** (content in DOM, browser just unhides) |
| Works with JS disabled? | No (no topics load) | Yes (browser-native `<details>`) |
| SEO? | Single SPA URL per topic | All topics indexed, deep links work |
| Memory? | Lower (only rendered topic) | Higher (all rendered, but hidden) |
| Build script complexity | Higher (JSON serialization, client-side renderer) | Lower (string concat) |

**For a study site where the user wants instant navigation and is willing to ship a 2-5MB chapter HTML, the inline approach wins.** The disk cost is fine — MedSea cardiology is 5.7MB HTML + 220MB PNGs = 226MB per chapter, all gitignored PNGs.

If a chapter ever grew to 1000+ topics, revisit and switch to a JSON manifest + lazy hydration. The 30-300 topic range is the sweet spot for inline.

## Template (Python f-string in `write_chapter_spa`)

```python
def write_chapter_spa(ch_slug, ch_name, ch_url, ch_color, info):
    ch_display_num = ch_slug.split("-")[0]
    html = page_header(f"{ch_name} · MedSea", current_ch_slug=ch_slug,
                       stats=[(info["n_hubs"], "Hubs"),
                              (info["n_topics"], "Topics"),
                              (info["n_pngs"], "PNGs")])

    # First pass: collect topics per hub + render content
    topics_for_manifest = []
    rendered_topics = {}  # local_prefix -> (md_html, png_rel, title)

    for hub_num in sorted(info["by_hub"].keys()):
        hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
        for t in hub_topics:
            title = t["slug"].replace("-", " ").title()
            if t["folder"]:
                png_rel = f"diseases/{t['folder']}/topic.png"
                md_rel = f"diseases/{t['folder']}/topic.md"
            else:
                png_rel = f"diseases/{t['local_prefix']}-{t['slug']}.png"
                md_rel = f"diseases/{t['local_prefix']}-{t['slug']}.md"
            png_path = SITE / ch_slug / png_rel
            md_path = SITE / ch_slug / md_rel
            md_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
            md_html = (render_md_to_html(md_text) if md_text
                       else "<p><em>No text content available for this topic.</em></p>")
            rendered_topics[t["local_prefix"]] = (md_html,
                                                  png_rel if png_path.exists() else None,
                                                  title)
            topics_for_manifest.append({...})  # also write to topics.json for backward compat

    # Second pass: build accordion HTML
    accordion_html = ""
    for hub_num in sorted(info["by_hub"].keys()):
        hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
        hub_name = info["hub_names"].get(hub_num, hub_num)
        n_topics = len(hub_topics)
        accordion_html += f'<details class="hub-acc" data-hub="{hub_num}">\n'
        accordion_html += f'  <summary class="hub-summary">\n'
        accordion_html += f'    <span class="hub-arrow">▸</span>\n'
        accordion_html += f'    <span class="hub-label"><span class="hub-num">{hub_num}</span> {hub_name}</span>\n'
        accordion_html += f'    <span class="hub-count">{n_topics}</span>\n'
        accordion_html += f'  </summary>\n'
        accordion_html += f'  <div class="hub-body">\n'
        for t in hub_topics:
            title = rendered_topics[t["local_prefix"]][2]
            md_html, png_rel, _ = rendered_topics[t["local_prefix"]]
            img_html = ""
            if png_rel:
                img_html = f'''
    <div class="topic-image-toggle collapsed" onclick="toggleTopicImage(this)">
      <span><span class="toggle-icon">▼</span> &nbsp;Show infographic image</span>
      <span style="font-size:11px;color:var(--text-dim)">click to expand</span>
    </div>
    <div class="topic-image-wrap collapsed">
      <div class="topic-image"><img src="/{ch_slug}/{png_rel}" alt="{title}" loading="lazy"></div>
    </div>'''
            accordion_html += f'    <details class="topic-acc" data-topic="{t["local_prefix"]}" data-hub="{hub_num}">\n'
            accordion_html += f'      <summary class="topic-summary">\n'
            accordion_html += f'        <span class="topic-arrow">▸</span>\n'
            accordion_html += f'        <span class="topic-num">{t["local_prefix"]}</span>\n'
            accordion_html += f'        <span class="topic-title">{title}</span>\n'
            accordion_html += f'      </summary>\n'
            accordion_html += f'      <div class="topic-body">\n'
            accordion_html += f'        <div class="topic-content">{md_html}</div>\n'
            accordion_html += f'        {img_html}\n'
            accordion_html += f'      </div>\n'
            accordion_html += f'    </details>\n'
        accordion_html += f'  </div>\n'
        accordion_html += f'</details>\n'

    # Page shell
    html += f"""
<div class="chapter-page" style="--accent-color: {ch_color}">
  <header class="chapter-header">
    <h1>{ch_name}</h1>
    <div class="meta">Davidson Ch {ch_display_num} · {info['n_hubs']} hubs · {info['n_topics']} topics · <a href="{ch_url}" target="_blank">Notion ↗</a></div>
  </header>
  <div class="chapter-toolbar">
    <input type="text" class="search" id="topicSearch" placeholder="🔍 Search topics…">
    <div class="toolbar-actions">
      <button class="btn-acc" onclick="expandAll()">Expand all</button>
      <button class="btn-acc" onclick="collapseAll()">Collapse all</button>
    </div>
    <div class="no-results" id="noResults">No matching topics</div>
  </div>
  <div class="hub-accordion" id="hubAccordion">
    {accordion_html}
  </div>
</div>
<script>
const CHAPTER_SLUG = "{ch_slug}";

function toggleTopicImage(btn) {{
  btn.classList.toggle("collapsed");
  const wrap = btn.nextElementSibling;
  if (wrap) {{
    wrap.classList.toggle("collapsed");
    btn.querySelector("span:last-child").textContent = wrap.classList.contains("collapsed") ? "click to expand" : "click to collapse";
  }}
}}

function expandAll() {{
  document.querySelectorAll("#hubAccordion details").forEach(d => d.open = true);
  const p = new URL(location.href);
  if (p.searchParams.get("expand") !== "all") {{
    p.searchParams.set("expand", "all");
    history.replaceState(null, "", p);
  }}
}}

function collapseAll() {{
  document.querySelectorAll("#hubAccordion details").forEach(d => d.open = false);
  const p = new URL(location.href);
  p.searchParams.delete("topic");
  p.searchParams.delete("expand");
  history.replaceState(null, "", p);
}}

// Search filter — auto-expands matching items
document.getElementById("topicSearch").addEventListener("input", function(e) {{
  const q = e.target.value.trim().toLowerCase();
  let visible = 0;
  document.querySelectorAll(".topic-acc").forEach(el => {{
    const text = el.textContent.toLowerCase();
    const show = !q || text.includes(q);
    el.style.display = show ? "" : "none";
    if (show) {{
      visible++;
      if (q) {{
        el.open = true;  // auto-expand matching topics
        const hub = el.closest(".hub-acc");
        if (hub) hub.open = true;  // and their parent hubs
      }}
    }}
  }});
  document.querySelectorAll(".hub-acc").forEach(g => {{
    const anyVisible = Array.from(g.querySelectorAll(".topic-acc")).some(el => el.style.display !== "none");
    g.style.display = anyVisible ? "" : "none";
    if (!q) g.open = false;  // collapse all when search cleared
  }});
  document.getElementById("noResults").classList.toggle("show", visible === 0);
}});

// Deep-link: ?topic=X auto-opens + scrolls; ?expand=all opens everything
(function() {{
  const params = new URLSearchParams(location.search);
  const t = params.get("topic");
  if (t) {{
    const el = document.querySelector(`.topic-acc[data-topic="${{t}}"]`);
    if (el) {{
      el.open = true;
      const hub = el.closest(".hub-acc");
      if (hub) hub.open = true;
      setTimeout(() => el.scrollIntoView({{ block: "start", behavior: "smooth" }}), 100);
    }}
  }} else if (params.get("expand") === "all") {{
    document.querySelectorAll("#hubAccordion details").forEach(d => d.open = true);
  }}
}})();
</script>
"""
    html += page_footer()
    (SITE / ch_slug / "index.html").write_text(html)
```

## CSS for the accordion

```css
/* Page shell */
.chapter-page { display: block; padding: 20px 24px; max-width: 1400px; margin: 0 auto; }
.chapter-page > .chapter-header { padding: 12px 0 16px; border-bottom: 1px solid var(--border);
                                   margin-bottom: 16px; border-left: 3px solid var(--accent-color, var(--accent));
                                   padding-left: 14px; }
.chapter-page > .chapter-header h1 { font-size: 26px; font-weight: 800; margin: 0 0 6px; }
.chapter-page > .chapter-header .meta { color: var(--text-dim); font-size: 12px;
                                         font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; }

/* Sticky toolbar */
.chapter-toolbar { display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
                    margin-bottom: 16px; padding: 10px 12px; background: var(--bg-2);
                    border: 1px solid var(--border); border-radius: 10px;
                    position: sticky; top: 64px; z-index: 50; backdrop-filter: blur(10px); }
.chapter-toolbar .search { flex: 1; min-width: 200px; background: var(--bg-3);
                            border: 1px solid var(--border); color: var(--text);
                            padding: 9px 12px; border-radius: 7px; font-size: 13px; outline: none; }
.chapter-toolbar .search:focus { border-color: var(--accent); box-shadow: 0 0 0 2px rgba(56,189,248,0.18); }
.chapter-toolbar .btn-acc { background: var(--bg-3); border: 1px solid var(--border);
                             color: var(--text); padding: 7px 12px; border-radius: 7px;
                             font-size: 12px; cursor: pointer; white-space: nowrap; }
.chapter-toolbar .btn-acc:hover { background: var(--bg-4); color: var(--accent); border-color: var(--accent); }
.chapter-toolbar .no-results { flex-basis: 100%; color: var(--text-dim); font-size: 12px;
                               text-align: center; padding: 6px; display: none; }
.chapter-toolbar .no-results.show { display: block; }

/* Hub accordion (outer) */
.hub-accordion { display: flex; flex-direction: column; gap: 8px; }
.hub-acc { background: var(--bg-2); border: 1px solid var(--border); border-radius: 10px;
           overflow: hidden; transition: border-color 0.15s; }
.hub-acc[open] { border-color: var(--accent-color, var(--accent));
                  box-shadow: 0 2px 12px rgba(0,0,0,0.2); }
.hub-summary { list-style: none; cursor: pointer; padding: 14px 16px;
                display: flex; align-items: center; gap: 12px; user-select: none;
                background: var(--bg-2); transition: background 0.15s; }
.hub-summary:hover { background: var(--bg-3); }
.hub-summary::-webkit-details-marker { display: none; }   /* hide default triangle */
.hub-arrow { color: var(--accent); font-size: 14px; transition: transform 0.2s;
              display: inline-block; width: 14px; }
.hub-acc[open] > .hub-summary .hub-arrow { transform: rotate(90deg); }
.hub-num { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--accent);
            background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.25);
            padding: 2px 6px; border-radius: 4px; font-weight: 600; margin-right: 8px; }
.hub-label { flex: 1; font-size: 14px; font-weight: 600; color: var(--text); }
.hub-count { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-dim);
              background: var(--bg-3); padding: 3px 8px; border-radius: 10px; font-weight: 600; }
.hub-body { padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 4px;
             background: var(--bg); border-top: 1px solid var(--border); }

/* Topic accordion (nested) */
.topic-acc { background: var(--bg-2); border: 1px solid transparent; border-radius: 8px;
              margin-left: 14px; transition: all 0.15s; position: relative; }
.topic-acc::before { content: ''; position: absolute; left: -10px; top: 24px;   /* tree-line */
                       width: 8px; height: 1px; background: var(--border); }
.topic-acc:hover { background: var(--bg-3); border-color: var(--border); }
.topic-acc[open] { background: var(--bg-3); border-color: var(--accent-color, var(--accent));
                    box-shadow: 0 1px 8px rgba(0,0,0,0.15); }
.topic-summary { list-style: none; cursor: pointer; padding: 10px 14px;
                  display: flex; align-items: center; gap: 10px; user-select: none; border-radius: 8px; }
.topic-summary::-webkit-details-marker { display: none; }
.topic-arrow { color: var(--text-dim); font-size: 12px; transition: transform 0.2s;
                display: inline-block; width: 12px; }
.topic-acc[open] > .topic-summary .topic-arrow { transform: rotate(90deg); color: var(--accent); }
.topic-num { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--text-dim);
              background: var(--bg-3); border: 1px solid var(--border); padding: 2px 6px;
              border-radius: 4px; font-weight: 600; flex-shrink: 0; min-width: 48px; text-align: center; }
.topic-acc[open] > .topic-summary .topic-num { color: var(--accent); border-color: var(--accent);
                                                 background: rgba(56,189,248,0.08); }
.topic-title { flex: 1; font-size: 13px; font-weight: 500; color: var(--text); line-height: 1.35; }

.topic-body { padding: 12px 16px 18px; border-top: 1px solid var(--border);
               background: var(--bg); margin-top: 6px; border-radius: 0 0 8px 8px; }
.topic-content { font-size: 14px; line-height: 1.65; color: var(--text); }
.topic-content h1 { font-size: 22px; margin: 16px 0 10px; color: var(--accent); }
.topic-content h2 { font-size: 18px; margin: 16px 0 8px; color: var(--accent);
                     border-left: 3px solid var(--accent); padding-left: 10px; }
.topic-content h3 { font-size: 15px; margin: 14px 0 6px; color: var(--text); }
.topic-content pre { background: var(--bg-3); border: 1px solid var(--border);
                       padding: 10px 12px; border-radius: 6px; overflow-x: auto; font-size: 12px; }
.topic-content table { border-collapse: collapse; margin: 10px 0; font-size: 13px; width: 100%; }
.topic-content th, .topic-content td { border: 1px solid var(--border); padding: 6px 10px; }
.topic-content th { background: var(--bg-3); font-weight: 600; }
.topic-content blockquote { border-left: 3px solid var(--accent); padding: 8px 14px;
                             margin: 10px 0; background: var(--bg-2); border-radius: 0 6px 6px 0; }

/* Collapsible PNG image */
.topic-image-toggle { margin-top: 12px; padding: 10px 12px; background: var(--bg-2);
                       border: 1px solid var(--border); border-radius: 8px; cursor: pointer;
                       display: flex; justify-content: space-between; align-items: center;
                       font-size: 13px; color: var(--accent); }
.topic-image-toggle:hover { background: var(--bg-3); }
.topic-image-toggle .toggle-icon { display: inline-block; transition: transform 0.2s; }
.topic-image-toggle:not(.collapsed) .toggle-icon { transform: rotate(180deg); }
.topic-image-wrap { margin-top: 8px; overflow: hidden; max-height: 5000px; transition: max-height 0.4s ease; }
.topic-image-wrap.collapsed { max-height: 0; margin-top: 0; }
.topic-image { background: var(--bg-2); border: 1px solid var(--border); border-radius: 8px; padding: 8px; }
.topic-image img { width: 100%; height: auto; display: block; border-radius: 4px; }

/* Mobile: tighter spacing, smaller fonts */
@media (max-width: 900px) {
  .chapter-page { padding: 12px 12px 60px; }
  .hub-summary { padding: 12px 14px; }
  .hub-label { font-size: 13px; }
  .topic-acc { margin-left: 8px; }
  .topic-summary { padding: 9px 12px; }
  .topic-title { font-size: 12px; }
  .topic-num { font-size: 9px; min-width: 42px; }
  .topic-body { padding: 10px 12px 14px; }
  .topic-content { font-size: 13px; line-height: 1.55; }
  .topic-content h1 { font-size: 18px; }
  .topic-content h2 { font-size: 16px; }
  .topic-content h3 { font-size: 14px; }
  .topic-content pre { font-size: 11px; padding: 8px 10px; }
  .chapter-toolbar { position: static; }  /* don't double-sticky on mobile */
  .chapter-toolbar .search { font-size: 12px; padding: 8px 10px; }
  .chapter-toolbar .btn-acc { font-size: 11px; padding: 6px 10px; }
}
```

## Key design decisions

1. **Native `<details>` not custom div+JS state** — browser handles open/close, persists state across page reloads (well, mostly — depends on whether the user-agent persists accordion state, which is implementation-specific). Deep links via `?topic=X` work regardless of accordion state.
2. **Tree-line `::before` on `.topic-acc`** — small horizontal line connecting topic to its hub gives a visual hierarchy without extra DOM.
3. **Hub count badge** — `30` next to hub name tells user how many topics before they click. Critical for 30+ topic hubs.
4. **Topic number uses monospace + min-width** — keeps all topic-number badges aligned in a column even when prefixes have varying length (`16.1.25` vs `16.10.262`).
5. **Sticky toolbar with `position: sticky; top: 64px`** — search + Expand/Collapse stays visible as user scrolls through expanded topics. On mobile, `position: static` to avoid stacking with the sticky mobile bar.
6. **Loading="lazy" on topic images** — defers PNG fetches until the topic is opened. Saves 200MB of bandwidth on chapters where user only opens 2-3 topics.
7. **Search auto-expands matching** — better UX than "filter and show only matches" because user sees the full context (which hub the match is in).
8. **Expand all sets `?expand=all` in URL** — shareable "show me everything" link.

## Verification probes (DOM, no vision needed)

```javascript
// On a chapter page at default 1280px viewport:
const hubs = document.querySelectorAll('.hub-acc');          // expect n_hubs
const topics = document.querySelectorAll('.topic-acc');      // expect n_topics
const toolbar = document.querySelector('.chapter-toolbar');
const accordion = document.querySelector('.hub-accordion');
const tb = toolbar.getBoundingClientRect();
const acc = accordion.getBoundingClientRect();
const firstHubText = hubs[0].querySelector('.hub-label').textContent.replace(/\s+/g,' ');
// expect "16.1 Acute Coronary Syndromes"
const firstCount = hubs[0].querySelector('.hub-count').textContent;
// expect "30" for ACS hub

// Test expand-all works
expandAll();
Array.from(document.querySelectorAll('.hub-acc')).filter(h => h.open).length;   // expect 17
document.body.scrollHeight;                                                      // expect ~500KB worth

// Test search
collapseAll();
document.getElementById('topicSearch').value = 'amyloid';
document.getElementById('topicSearch').dispatchEvent(new Event('input'));
Array.from(document.querySelectorAll('.topic-acc')).filter(t => t.style.display !== 'none').length;
// expect ~5-50 matches depending on chapter
Array.from(document.querySelectorAll('.hub-acc')).filter(h => h.open).length;
// expect ≥1 (the auto-expanded hubs)

// Test deep link
window.history.replaceState(null, '', '?topic=16.1.25');
location.reload();
// expect topic "16.1.25" auto-opened, scrolled into view
```

## CSS gotcha: `replace_all: true` for inline CSS

When `PAGE_CSS` is a single Python string containing many `@media` blocks, the same block can exist in 2+ places from prior edits. `patch(replace)` fails with "Found N matches"; use `patch(replace_all=true)` to remove all duplicates in one shot. Always verify after:

```bash
grep -c '@media (max-width: 900px)' scripts/site/build_site.py
# expect 1, not 2 or 3
```

A duplicate 900px block is the #1 cause of "I changed the CSS but nothing happened" — the earlier block wins on shared properties.

## Backward compatibility

`topics.json` is still written at `SITE / ch_slug / "topics.json"` with the same shape as before, in case any external tool or future feature still needs the pre-rendered manifest. It's just not loaded by the SPA anymore.

## File sizes (real numbers, MedSea 16-cardiology)

| File | Size | Notes |
|---|---|---|
| `site/16-cardiology/index.html` | 5.7MB | 17 hubs × 330 topics, all content embedded |
| `site/16-cardiology/topics.json` | 4.8MB | Still written, same shape as before |
| `site/16-cardiology/diseases/*/topic.png` | 220MB | Lazy-loaded when topic opened |
| Build time for 1 chapter | ~3-5 sec | String concat is cheap |
| Build time for all 32 chapters | ~90 sec | Acceptable for the depth-first layout |

## When to switch back to JSON fetch

If a chapter ever exceeds ~1000 topics, consider:
- The HTML file becomes 15-20MB — slow to parse, hits browser memory limits
- Most users only view 1-5% of topics — wasting 95% of bandwidth
- Switch to a JSON manifest + lazy hydration: render topics on demand, keep collapsed topics as stubs

For 30-300 topics, inline wins. For 1000+ topics, JSON fetch wins.
