# AceRoute Journey graph: hover + spacing cleanup

Context: AceRoute Journey graph used real Hermes data but still needed a cleanup pass after user complaints:
- graph looked overlapped / chaotic
- hover behavior was too weak
- stale `Loading graph…` text could remain visible

## Durable lessons

### 1. Use real graph edges for hover behavior
If the backend returns real `edges`, build hover state from those exact links.
Do not infer hover neighbors from category, ring, or sort order.

Good hover behavior:
- focused node: strongest emphasis
- direct neighbors: secondary emphasis
- direct connecting edges: brighter / thicker
- unrelated nodes: dim aggressively
- unrelated edges: fade hard

This reads much closer to Hermes desktop than broad cluster highlighting.

### 2. Dense radial graphs need ring-local spacing, not just smaller nodes
A useful lightweight fix before full force simulation:
1. bucket nodes into rings by time
2. assign initial angular positions
3. run a ring-local relaxation pass over sorted nodes
4. enforce minimum angular gap based on `(nodeA.size + nodeB.size + padding) / radius`
5. clamp final positions to stage bounds

This substantially reduces overlap while staying cheap in plain browser JS.

### 3. Prefer smaller nodes + wider ring gaps before adding labels
When the user says the graph is messy, reduce visual density first:
- shrink node diameter
- increase minimum ring gap
- remove always-on labels
- reduce decorative text

Label-heavy radial graphs degrade quickly.

### 4. Never hardcode `Loading graph…` in static markup
If the graph renders asynchronously, put a neutral placeholder like `—` in HTML and let JS write live legend/status text.
Otherwise a stale loading label can persist visually and users will assume the graph is broken even when nodes are present.

## Practical verification checks
After a hover/spacing pass, verify:
- graph legend shows live counts, not loading text
- DOM contains real node + edge counts
- hover adds direct-neighbor highlight class
- hover dims unrelated nodes
- tooltip includes enough detail to justify hover
- static markup no longer contains persistent `Loading graph…`

## Example behavior that verified well
- tooltip showing node label, kind/category, date, use count, state, and neighbor count
- direct neighbors get their own class (`hover-neighbor`)
- unrelated nodes use a stronger dim class (`edge-dim`)
- only directly connected edges brighten on hover
