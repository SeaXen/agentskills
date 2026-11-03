# Obsidian graph dashboard — cleanest pass: type-ahead search, fit-to-view, clickable cluster labels, cohesion force

Use this when the user says the graph is "almost there" and wants the
**single most-premium upgrade** without switching to a different
visualization. Pairs with `references/graph-dashboard-advanced-polish.md`
(presets, focus mode, search pulse) and `references/graph-dashboard-force-layout.md`
(base force/minimap/saved-layout). Built and tested 2026-06-17.

## Target
- `/mnt/tb/hermes/obsidian_dashboard.py`
- real path may resolve to `/root/.hermes/obsidian_dashboard.py` (verify with `stat -c '%i'`)

## Five patterns, each one is small but compounding

### 1. Type-ahead search input inside the graph area

**Why:** the existing note search is in the Notes page header. A user
on the Graph page wants to type and immediately see golden-highlighted
matches without leaving the graph.

**HTML — add inside both `#graphArea` (Notes page) and `#graphArea2` (Graph page):**
```html
<div class="graph-floating-tools">
  <input id="graphSearch" class="graph-search" type="search"
         placeholder="Search notes…"
         oninput="onGraphSearchInput(this.value)"
         autocomplete="off" spellcheck="false" />
  <button class="graph-icon-btn" id="graphFitBtn" onclick="fitGraphToView()" title="Fit to view">⤢</button>
</div>
```
(Use `id="graphSearch2"` on the Graph page input; the JS syncs both.)

**CSS — glassmorphism floating panel pinned top-right of the canvas:**
```css
.graph-floating-tools{position:absolute;top:10px;right:10px;display:flex;gap:6px;align-items:center;z-index:5;background:rgba(7,13,26,.72);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:10px;padding:4px}
.graph-search{width:200px;background:transparent;border:0;outline:none;color:var(--text);font:13px system-ui;padding:6px 8px}
.graph-search::placeholder{color:#6b7a92}
.graph-search:focus{outline:none}
.graph-icon-btn{width:28px;height:28px;border:0;background:transparent;color:var(--muted);border-radius:7px;cursor:pointer;font:15px system-ui;display:inline-flex;align-items:center;justify-content:center;transition:background .12s,color .12s}
.graph-icon-btn:hover{background:rgba(88,166,255,.14);color:#a8c5ee}
.graph-icon-btn.active{background:rgba(88,166,255,.22);color:#dbeafe}
```

**JS — single source of truth, two inputs synced, reuses existing `state.query` so the existing pulse/render path lights up for free:**
```js
function onGraphSearchInput(value){
  const v=(value||'').trim().toLowerCase();
  state.query=v;
  state.graphSearch=v;
  const els=[document.getElementById('graphSearch'), document.getElementById('graphSearch2')];
  els.forEach(el=>{ if(el && el.value!==value) el.value=value; });
  if(v) reheatSimulation(0.2);  // wake the pulse animation
  drawGraph();
}
```

### 2. Fit-to-view button

**Why:** users zoom/pan freely and lose the graph. One click should
re-zoom to show every node in the canvas.

```js
function fitGraphToView(){
  const c=document.getElementById('graph');
  if(!c || !Object.keys(positions).length){ showToast('Graph not ready'); return; }
  const arr=Object.values(positions);
  let minX=Infinity, maxX=-Infinity, minY=Infinity, maxY=-Infinity;
  arr.forEach(p=>{
    const x=p.x, y=p.y, r=(p.r||8) * 0.012;
    if(x-r<minX) minX=x-r; if(x+r>maxX) maxX=x+r;
    if(y-r<minY) minY=y-r; if(y+r>maxY) maxY=y+r;
  });
  const padX=(maxX-minX)*0.08 || 0.05;
  const padY=(maxY-minY)*0.08 || 0.05;
  minX-=padX; maxX+=padX; minY-=padY; maxY+=padY;
  const rangeX=Math.max(maxX-minX, 0.1);
  const rangeY=Math.max(maxY-minY, 0.1);
  const zoomX=1/rangeX, zoomY=(c.height/c.width)/rangeY;
  const zoom=clamp(Math.min(zoomX,zoomY)*0.92, 0.55, 3.2);
  const cx=(minX+maxX)/2, cy=(minY+maxY)/2;
  graphView.zoom=zoom;
  graphView.panX=0.5-cx;
  graphView.panY=0.5-cy;
  saveViewState();
  renderGraphStats();
  drawGraph();
  showToast(`Fit · ${Math.round(zoom*100)}%`);
}
```

### 3. Clickable cluster labels with folder focus mode

**Why:** the existing `drawClusters()` already renders folder labels.
Making them clickable turns them into a primary navigation affordance.

**Add a folder-focus mode to `getFocusSet()` (before the existing `state.focusMode` branch):**
```js
function getFocusSet(){
  if(state.focusFolder){
    const set=new Set();
    Object.entries(positions).forEach(([name,p])=>{
      if(p.folder===state.focusFolder) set.add(name);
    });
    // include cross-folder links for context
    set.forEach(name=>{
      const links=adjacency[name];
      if(links) links.forEach(n=>set.add(n));
    });
    return set;
  }
  if(!state.focusMode) return null;
  const focus=getFocusRoot();
  if(!focus) return null;
  return new Set([focus, ...(adjacency[focus] ? Array.from(adjacency[focus]) : [])]);
}
```

**Add a `focusOnFolder(folder)` function:**
```js
function focusOnFolder(folder){
  if(!folder) return;
  state.focusFolder = (state.focusFolder===folder) ? null : folder;
  state.focusMode = !!state.focusFolder;
  state.selectedNode='';
  renderGraphStats();
  renderGraphMetaBar();
  drawGraph();
  showToast(state.focusFolder ? `Folder focus: ${shortFolder(folder)}` : 'Folder focus cleared');
}
```

**Track label rects in `drawClusters` (top of function):**
```js
if(!simulation.clusterLabelBoxes) simulation.clusterLabelBoxes=[];
simulation.clusterLabelBoxes=[];
```

**For each cluster label rendered, push the clickable rect:**
```js
// inside the Object.entries(clusterCenters).forEach loop, after computing labelX/labelY/boxW/boxH:
simulation.clusterLabelBoxes.push({
  folder, x:labelX-7*devicePixelRatio, y:labelY-boxH+2*devicePixelRatio, w:boxW, h:boxH
});
// draw the clickable pill (rounded rect with folder color tint)
ctx.fillStyle=rgbaFromHex(meta.color,isFocused?0.22:0.10);
roundRect(ctx,labelX-7*devicePixelRatio,labelY-boxH+2*devicePixelRatio,boxW,boxH,5*devicePixelRatio);
ctx.fill();
ctx.strokeStyle=rgbaFromHex(meta.color,isFocused?0.7:0.30);
ctx.lineWidth=1*devicePixelRatio; ctx.stroke();
```

**Add a hit-test helper:**
```js
function hitClusterLabel(pointer){
  const boxes=simulation.clusterLabelBoxes || [];
  for(const b of boxes){
    if(pointer.x>=b.x && pointer.x<=b.x+b.w && pointer.y>=b.y && pointer.y<=b.y+b.h) return b.folder;
  }
  return null;
}
```

**Wire it into `onGraphClick` (after the node-click branch):**
```js
function onGraphClick(e){
  const c=e.currentTarget;
  const pointer=getPointer(e,c);
  const node=pickNodeAt(pointer,c,8);
  if(graphView.dragged){ graphView.dragged=false; return; }
  if(node){ state.selectedNode=node; renderGraphStats(); if(noteMap[node]) openNoteByTitle(node); else drawGraph(); return; }
  const folder=hitClusterLabel(pointer);
  if(folder){ focusOnFolder(folder); return; }
}
```

**Render the focused cluster with an extra outer ring (inside the cluster loop):**
```js
const isFocused = state.focusFolder===folder;
if(isFocused){
  ctx.beginPath(); ctx.arc(s.x,s.y,radius+6*devicePixelRatio,0,Math.PI*2);
  ctx.fillStyle=rgbaFromHex(meta.color,0.14); ctx.fill();
  ctx.strokeStyle=rgbaFromHex(meta.color,0.55); ctx.lineWidth=1.4*devicePixelRatio; ctx.stroke();
}
```

### 4. Cluster cohesion force in the simulation

**Why:** the existing simulation has repulsion + springs but no
folder-level force. Without this, related notes drift apart and
cluster hulls feel arbitrary.

**Add inside `tickSimulation()`, after the link-spring loop, before the per-node seed-pull loop:**
```js
Object.entries(clusterCenters).forEach(([folder, meta])=>{
  Object.entries(positions).forEach(([name,p])=>{
    if(p.folder!==folder || p.pinned) return;
    const pull=0.0011 * alpha;
    p.x += (meta.x - p.x) * pull;
    p.y += (meta.y - p.y) * pull;
  });
});
```

### 5. Faster alpha decay + settle

**Why:** the existing 0.995 decay makes the layout wobble for ~10s after
load. Drop to 0.985 for ~3s settle time without making the simulation
feel jerky.

**In `tickSimulation()`, last line:**
```js
simulation.alpha*=0.985; return simulation.alpha>0.002;  // was 0.995
```

## Verification checklist

1. `python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py`
2. Extract inline JS and run `node --check` (or just `node --check` on the page-load JS via a temp file)
3. `systemctl --user restart obsidian-vault-dashboard`
4. `sleep 2 && curl -s -o /dev/null -w "%{http_code} size=%{size_download}\n" http://127.0.0.1:6065/` (HTTP 200, larger than 138KB baseline = new code loaded)
5. Browser verification (vision may be down — use `browser_console` JSON probes):
   - `JSON.stringify({ hasSearch2: !!document.getElementById('graphSearch2'), btnCount: document.querySelectorAll('.graph-icon-btn').length, positions: Object.keys(positions).length })` — expect 2 buttons, 61 positions
   - `fitGraphToView(); graphView.zoom` — expect ~0.55x for a 61-node graph
   - `onGraphSearchInput('dash'); getSearchMatches().length` — expect > 0 matches, second input syncs
   - `focusOnFolder('Daily'); getFocusSet().size` — expect ~60 (folder + cross-folder links)
6. Visual sanity (vision up): top-right has a glassmorphism panel with search + ⤢ button; cluster labels are tinted pills with folder colors; clicking a label dims other folders.

## Pitfalls

- **Do not call `positions[name].x` inside the cohesion loop** without checking `p.pinned` — pinned notes will be dragged to the cluster center, breaking user-placed pins. The `if(p.folder!==folder || p.pinned) return;` guard is mandatory.
- **Do not use a strong cohesion force (>0.005)** — the simulation will collapse the entire graph into one big blob. 0.0011 is the sweet spot.
- **Do not put the search input outside `.graphArea`** — the position:absolute top-right anchor only works when the parent is the canvas container. Putting it in the toolbar will cause it to scroll with the page.
- **Do not forget to clear `state.focusFolder` when the user clicks a node** — keeping both selectedNode and focusFolder active creates a "frozen focus" that the user can't easily escape. The `focusOnFolder()` function clears `state.selectedNode=''` on purpose.
- **Do not trust the `folder` from a folder label click without round-tripping through `simulation.clusterLabelBoxes`** — the label is drawn in device-pixel coordinates, but the click event also produces device-pixel pointer coordinates (via `getPointer()` which multiplies by `devicePixelRatio`). Keeping the label box in the same coordinate space as the pointer is what makes hit-testing work.

## When NOT to use this

- If the user wants a **different visualization** (sunburst, treemap, radial, sankey), the force-directed graph is the wrong starting point. Acknowledge the fundamental shift, then offer to replace the canvas — not to bolt on more controls.
- If the user has < 20 notes, the cohesion force over-groups and the graph feels stiff. Disable the cohesion loop or raise the cluster radius floor.
- If the user wants the search to be aware of folder/tag/path (not just title), change `getSearchMatches()` first — the new input reuses that function for free.
