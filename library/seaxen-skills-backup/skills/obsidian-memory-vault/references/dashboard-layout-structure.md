# Dashboard layout structure and CSS pitfalls

## Current layout (post-restructure)

The dashboard is a single Python file at `/mnt/tb/hermes/obsidian_dashboard.py` containing an inline HTML/CSS/JS string (`INDEX = r"""..."""`).

**Layout structure:**
```
body (overflow:hidden)
  header (72px, gradient underline)
  wrap (grid: 280px | 1fr, fills remaining height)
    notesPanel (left sidebar, always visible)
      panelHead ("Notes" title)
      sidebarTools (search, folder filter, mode filter, collapsible: tags + saved searches + orphan lane)
      list (scrollable note cards)
    rightContainer (grid: 55fr | 45fr, vertical split)
      main (graph panel, top ~55%)
        graphToolbar (summary, buttons, graph tools dropdown)
        graphArea (canvas, stats, toast, presets, minimap, legend)
      reader (reader panel, bottom ~45%)
        panelHead ("READER" title, status)
        readerMeta (overflow-y:auto, single scroll container for everything below)
          note info: title, path, tags, facts
          readerTabBar (Overview/Links/Recall/Important)
          readerSections (one active tab visible at a time)
            Overview: markdown content + cluster inspector + backlinks + related
            Links: backlinks tabbed (incoming/outgoing)
            Recall: hybrid recall results + broken link fixes
            Important: pinned notes + timeline
          readerActions (Dashboard, Decisions, Recall QA, Memory Health, etc.)
```

## Key CSS rules

| Selector | Purpose | Gotcha |
|---|---|---|
| `.wrap` | Main grid container | `height:calc(100vh - var(--header-h))` — must subtract exact header height |
| `.rightContainer` | Vertical split right area | `grid-template-rows: 55fr 45fr` — adjust ratio if graph/reader too small |
| `.readerMeta` | Scrollable reader | `overflow-y:auto; flex:1` — SINGLE scroll container for ALL reader content |
| `.readerSections` | Tab content wrapper | No overflow — scrolling is parent's job |
| `.readerSection` | Individual tab | `display:none` / `display:flex` toggled by JS |
| `.main` | Graph panel | `grid-template-rows:auto 1fr` — toolbar fixed, graph fills |

## CSS pitfalls discovered

### 1. overflow:hidden clips scrollable children
Setting `overflow:hidden` on any parent prevents children with `overflow-y:auto` from scrolling. Fix: make only the deepest common ancestor the scroll container. Do NOT stack overflow:hidden on multiple nested elements.

### 2. Multiple overflow layers
Do NOT set `overflow:hidden` on `.reader`, `.readerSections`, AND `.readerSection` simultaneously. Pick ONE scroll container.

### 3. Duplicate CSS rules / multiple :root blocks
If two `:root` blocks exist in `<style>`, the second silently overrides the first. This causes CSS variables to disappear. Always keep a single `:root`. After agy edits, check for this.

### 4. patch tool duplicate closing braces
When patching inside `{...}` blocks, the tool can leave the original `}` plus add a new one. Always count open/close braces after patching.

## Mandatory validation after ANY edit

```
python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py
node --check /tmp/check_dashboard.js   # extract JS first
systemctl --user restart obsidian-vault-dashboard.service
curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:6065/
```

## agy reliability note

`agy --print` frequently **claims success but does not actually modify the file**. After every agy run, `grep` the file for the expected change. If absent, use the `patch` tool instead. Do not trust agy for non-trivial layout surgery — it produces plans but execution silently fails.

## What was removed (do not re-add)

- **Workspace bar** (Workbench/Explore/Reader/Recall buttons) — caused confusion, took space
- **3-column layout** (notes + graph + reader side-by-side) — graph was too small
- **Notes collapse toggle** — user never wanted it, always caused "Loading vault…" confusion
- **Workspace modes** (`data-workspace` CSS/JS) — simplified to single workbench mode
