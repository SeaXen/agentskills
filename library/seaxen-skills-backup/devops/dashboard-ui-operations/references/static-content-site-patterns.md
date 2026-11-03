# Static-content-site patterns for self-hosted web UIs

Reference for knowledge-base, study-tool, or markdown-driven static sites deployed behind nginx in Docker. Captures reusable UI patterns proven on MedSea (32 chapters, 2,957 topics from Davidson's).

## 1. Auto-synthesize diagrams from heading structure

When generating visualizations (mindmaps, flowcharts, concept maps) for a content site, do **not** rely on every source MD containing an explicit `mermaid`/`mindmap` code block. Coverage will be patchy and users will say *"only 1 chapter, I told you make all chapters"*.

**Pattern:** if the rendered HTML for a topic has no diagram block, synthesize one from H1 + H2 + H3 headings and append it at the end of the topic body.

```python
def _synthesize_mindmap_from_headings(md_text: str) -> str:
    headings = []
    for line in md_text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            headings.append((len(m.group(1)), m.group(2).strip()))
    if len(headings) < 2:
        return ""
    root = next((t for l, t in headings if l == 1), headings[0][1])
    branches = [(l, t) for l, t in headings if l in (2, 3)][:30]
    mm = ["mindmap", f"  root(({root}))"]
    for lvl, txt in branches:
        indent = "    " if lvl == 2 else "      "
        mm.append(f"{indent}{txt}")
    return render_mindmap_md("\n".join(mm))
```

Track `found_mermaid` while parsing code fences; only synthesize if `not found_mermaid`.

**Verification:** count rendered diagrams per chapter after each rebuild. If a chapter drops to zero, the synthesis path broke — fix the heading regex, not by hand-editing source MDs.

## 2. Universal search with pre-built index (no runtime crawl)

For a static site with thousands of topics, generate a single `search_index.json` at the site root during build. The header search input fetches it lazily on first keystroke and filters client-side.

**Index shape (compact, ~700 bytes/topic):**
```json
[
  {
    "chapter_num": "19",
    "chapter_name": "Clinical Biochemistry & Metabolic Medicine",
    "chapter_slug": "19-clinical-biochemistry-and-metabolic-medi",
    "hub_num": "19.1",
    "hub_name": "Metabolic Medicine",
    "topic": "19.1.1",
    "title": "Amyloidosis",
    "url": "/19-clinical-biochemistry-and-metabolic-medi/"
  }
]
```

**Scoring** (client-side, ~instant for 3k items):
- title exact match = 100
- title startsWith = 80
- topic prefix = 70
- title includes = 60
- hub_name includes = 40
- chapter_name includes = 20

Sort by score desc, then alphabetically. Top 20 in dropdown. Show `+N more` if hits > 20.

**Keyboard:** ↑/↓ to navigate, Enter to open, Esc to clear, click-outside to close. Highlight matched substring with `<mark>`.

**Pitfall:** do not load the index on every keystroke. Use a 120ms debounce, cache the loaded promise, and only show results when query length ≥ 2.

## 3. 3-column grid for a truly centered search header

A flex row with `search-box { flex: 1 1 auto }` between a wide logo+stats block and a narrow dropdown+github block puts the search off-center (search center shifts toward the wider side).

**Fix:** use CSS Grid with explicit equal columns:

```css
header.site .header-inner {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
  max-width: 1600px;
  width: 100%;
  margin: 0 auto;
}
header.site .header-left  { justify-self: start; }
header.site .search-box  { justify-self: center; }
header.site .header-right { justify-self: end; }
```

The `1fr auto 1fr` forces left and right columns to share remaining width equally; the middle `auto` (search input) takes only its content width, then `justify-self: center` locks it to the column center. Result: search center ≈ viewport center even when left and right widths differ.

**Verification (browser console):**
```js
Math.round(searchBox.getBoundingClientRect().left + searchBox.getBoundingClientRect().width/2)
// Should equal viewport.innerWidth / 2 within ±10px
```

## 4. Docker port alignment gotcha

When deploying a static site via nginx-in-Docker, three port numbers must agree:

1. **`EXPOSE`** in `Dockerfile` — documentation only, no effect.
2. **`listen`** in `nginx.conf` — port nginx actually binds inside container.
3. **`docker run -p HOST:CONTAINER`** — outer-to-inner port mapping.

**Easy mistake:** set `listen 8855` then `docker run -p 8855:80`. Requests to host:8855 land on container:80, where nothing listens → `Recv failure: Connection reset by peer` from curl, but the container appears healthy because nginx IS running on 8855 inside.

**Fix:** always set nginx to `listen 80` and `EXPOSE 80` so the `-p HOST:80` mapping just works. If you really need a non-80 inner port for any reason, also set `HEALTHCHECK` to use that inner port:

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1
```

If nginx serves on port 8855, change to `http://localhost:8855/`.

**Diagnosis triad:**
- `docker exec medsea wget -q -O- http://127.0.0.1:80/` — does nginx respond inside?
- `curl -sI http://HOST_IP:8855/` — does the host→container pipe work?
- `docker logs medsea | tail -20` — any `Connection refused` / `bind()` errors?

If all three are silent but curl returns "Empty reply" or "Connection reset", suspect the listen-port vs publish-port mismatch.

## 5. Missing template tag after header refactor

When refactoring a page template's header section (e.g. adding a search bar), the open tag for a sibling structural element (e.g. `<main>`) often gets deleted from `page_header()` while the matching close tag stays in `page_footer()`. The page renders fine in browser but `document.querySelector('main')` returns `null` and CSS rules scoped to `main` silently fail.

**Symptom:** "I added `main { padding: 32px; }` but the layout didn't change."

**Check immediately after any header/footer refactor:**
```bash
grep -c '<main' site/index.html site/<chapter>/index.html
grep -c '</main' site/index.html site/<chapter>/index.html
# Both counts should be > 0 and equal.
```

**Fix:** add the open `<main>` tag at the very end of `page_header()` (after the closing `</header>` and any pre-main script tags). The close `</main>` already lives at the start of `page_footer()`.

## 6. Layout balance: visible edge gap + close inner items

For dense card grids, the user wants a small but visible gap from the screen edges (~24px) AND a small gap between cards (~12px). Do not push either to one extreme.

**Bad:** edge-to-edge grid (`main { padding: 8px }`) — feels cramped against monitor bezel.
**Bad:** huge padding + huge card gap — wastes space on a wide screen.

**Good defaults:**
```css
main { padding: 28px 24px 64px; max-width: 1640px; margin: 0 auto; }
.chapters-grid { gap: 12px; }   /* close together, but not touching */
```

This gives a small breathing strip on the sides (~24px) while keeping chapter cards visibly close to each other.

## 7. User-frustration signal: "only N items, I told you make all"

When the user reports something works on N items but they wanted it everywhere, treat it as a coverage bug, not a sample-size complaint. Do **not** hand-craft fixes for the failing items. Fix the underlying generator so the change applies to every item by default.

**Pattern:**
1. Count outputs across all chapters/topics (e.g. `for d in */; do grep -l "diagram-class" $d/topics.json | wc -l`).
2. Find chapters with zero → identify why their source MD lacks the trigger (e.g. no `mermaid` block).
3. Add a fallback synthesis in the renderer for the missing cases.
4. Rebuild and recount — every chapter should now have the diagram.

This is faster and more durable than manual content edits.