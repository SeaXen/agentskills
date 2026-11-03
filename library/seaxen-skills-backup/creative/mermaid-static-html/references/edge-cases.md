# Mermaid Rendering Edge Cases — Real Failures From MedSea

Concrete examples extracted from building the MedSea static knowledge site
(`/mnt/tb/Sea-knowledge/#MedSea/`). All fixed in `scripts/extract_label.py`.

## Hexagon shapes — strip count matters

Mermaid's hexagon syntax uses **double braces**:

```
H{{Amyloidosis}}
```

A naive `label[1:-1]` (strip 1 char each end) produces:
- `H{{Amyloidosis}}` → `{Amyloidosis}`  ❌ extra braces remain

Correct fix — strip 2 chars each end when shape is `{{...}}`:
- `H{{Amyloidosis}}` → `Amyloidosis`  ✅

The same applies to:
- Double-circle / bang: `((text))` → strip 2 each end
- Cylindrical: `[(text)]` → strip 2 each end
- Subroutine: `[[text]]` → strip 2 each end
- Parallelogram: `[/text/]` → strip 2 each end (different chars!)

**Detection rule**: count the opening brackets and strip the same number on the close side.

## Multi-line edge labels

Mermaid allows continuation lines on edge labels:

```
A -->|Most common 90% Maculopapular,
Symmetrical, Spares face
initially, resolves in 1-2 weeks| B
```

Without joining, the renderer sees only the first line and the rest becomes orphan content. The fix is to buffer until the second `|` (or end of statement) is found.

## Malformed hexagons

Real-world content often has unbalanced brackets, e.g.:

```
F{{Drug Rash}
```

The opening `{{` is doubled but only one `}` exists. The robust pattern handles this by finding the LAST `}` after the opening `{{` instead of requiring exact match.

The pre-fix output was:
- `F{{Drug Rash}` → renders `F` as label, `{Drug Rash}` as second node (two cards instead of one)

Post-fix:
- `F{{Drug Rash}` → renders `F` with label `Drug Rash` (single node)

## Multi-line node labels

Some Davidson topic content had:

```
A[Line 1
Line 2
Line 3]
```

The label spans 3 lines. Joining with space gives: `Line 1 Line 2 Line 3`.

The pre-fix renderer would render only `Line 1` because the bracket-balance check fired on the first `]`.

## Detection pattern that handles all of these

```python
_NODE_DECL_RE = re.compile(
    r"""^(
        (?P<id>[A-Za-z_][A-Za-z0-9_]*)?     # optional node ID
        \s*
        (?P<open>[\(\[\{]{1,2})             # 1 or 2 opening brackets
        \s*
        (?P<label>[^()\[\]{}\n]+?)          # label (no nested brackets, no newlines)
        \s*
        (?P<close>[\)\]\}]{1,2})            # 1 or 2 closing brackets
    )$""",
    re.VERBOSE,
)
```

The `{1,2}` quantifier on `[\(\[\{]` and `[\)\]\}]` is the key — it matches both single and double brackets.

The label character class `[^()\[\]{}\n]+?` excludes nested brackets (no N² complexity blowup) and newlines (multi-line handled separately).

## Auto-synthesis from headings — why it matters

The MedSea project had 32 chapters × ~92 topics = ~2,957 topic pages. Of these:

- Ch 19 (Biochemistry): 28 topics, all with explicit mermaid blocks → mindmap coverage 28/28
- Ch 26 (Dermatology): 348 topics, only 4 had mermaid → mindmap coverage 4/348
- Ch 29-32 (Psychiatry, Maternal, Adolescence, Older Adult): 278 topics, **0 had mermaid** → mindmap coverage 0/278

The renderer only fired on explicit mermaid blocks. Without a fallback, 90%+ of topic pages had no visual summary.

The fix: add `_synthesize_mindmap_from_headings(md_text)` that runs at the end of markdown-to-HTML conversion. When `found_mermaid` is False AND at least 2 headings exist, build a mindmap from the H1/H2/H3 structure.

Result: mindmap coverage went from 1,346/2,957 (45%) to 2,604/2,957 (88%).

**The 12% still missing are topics with fewer than 2 H1/H2/H3 headings** — these are short overview notes that don't have enough structure to synthesize from.

## Universal search pattern

For a static site with thousands of topics, server-side search is overkill. The pattern:

1. **Build phase**: pre-generate `search_index.json` at site root
   ```json
   [
     {"chapter_num": "19", "chapter_name": "Biochemistry", "topic": "19.1.1", "title": "Amyloidosis", "url": "/19-biochemistry/"},
     ...
   ]
   ```
   File size for 2,957 topics: ~700KB. Acceptable.

2. **Client phase**: lazy-load the JSON on first search keystroke
   ```javascript
   let idx = null;
   function search(q) {
     if (!idx) idx = await fetch('/search_index.json').then(r => r.json());
     // ... scoring
   }
   ```

3. **Scoring**: rank by field priority
   ```javascript
   if (title === query) score = 100;       // exact
   else if (title.startsWith(query)) score = 80;
   else if (topic.startsWith(query)) score = 70;  // "19.1" matches topic prefix
   else if (title.includes(query)) score = 60;
   else if (hub.includes(query)) score = 40;
   else if (chapter.includes(query)) score = 20;
   ```

4. **UX**: dropdown panel, keyboard nav (↑/↓/Enter/Esc), debounced input (120ms), click-outside to close

## Docker port mapping pitfall

When the static site is served by nginx in a Docker container:

```bash
docker run -p 8855:80 myimage
```

The `-p 8855:80` means: host port 8855 → container port 80. The nginx config MUST listen on 80, not 8855:

```nginx
server {
    listen 80;       # ← container port, not host port
    server_name _;
    root /usr/share/nginx/html;
}
```

If the config has `listen 8855`, the docker port mapping sends requests to container:80 where nothing is listening → `Connection reset by peer` / `Empty reply from server`.

The healthcheck also needs to use the container's localhost:80:
```dockerfile
HEALTHCHECK CMD wget -q --spider http://localhost/ || exit 1
# NOT http://localhost:8855/
```

## Verification strategy (no vision model needed)

When vision model is offline, verify rendering via DOM inspection in a browser:

```javascript
// Count rendered mindmaps
document.querySelectorAll('.mindmap').length

// Check root label
document.querySelector('.mm-root')?.textContent

// Verify no raw tokens leaked
Array.from(document.querySelectorAll('.mm-node'))
  .map(n => n.textContent)
  .filter(t => t.match(/[\[\{\(\|]/))   // any leftover brackets = bug
```

For Docker container health:
```bash
docker exec mycontainer wget -q -O- http://localhost:80/
```

If that returns content, nginx is working. The external curl test can give false negatives due to port mapping bugs even when internal is fine.

## Files in MedSea that implement these patterns

- `/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py`
  - `_extract_label()` — shape-aware label extraction (line ~950)
  - `render_mindmap_md()` — mindmap HTML renderer
  - `render_flowchart_md()` — flowchart HTML renderer (with multi-line edge buffering)
  - `_synthesize_mindmap_from_headings()` — auto-synthesis fallback
  - `write_search_index()` — pre-build search index
  - Search box HTML/JS in `page_header()` with scoring + keyboard nav

- `/root/sea-knowledge-infographics/render_topic.py`
  - PNG renderer (uses same parsing logic as `build_site.py`)
  - `_extract_label()` mirrored here for PNG output consistency

- `/mnt/tb/Sea-knowledge/#MedSea/docker/nginx.conf`
  - `listen 80` (matches docker `-p 8855:80` mapping)

- `/mnt/tb/Sea-knowledge/#MedSea/Dockerfile`
  - `HEALTHCHECK CMD wget -q --spider http://localhost/`

## Test fixtures

The `scripts/extract_label.py` in this skill has 12 fixtures covering every edge case above. Run with `--test` to verify.