# AceRoute Journey ↔ Hermes Desktop Starmap Parity

Use when the user wants AceRoute's Journey graph to feel like Hermes desktop's starmap rather than a generic radial widget.

## What the upstream desktop graph actually is

- The `/journey` desktop routing commit only changes command routing; it does **not** add the graph renderer itself.
- The real renderer lives under `apps/desktop/src/app/starmap/`.
- Desktop pulls its data from the Hermes learning graph payload (`/api/learning/graph`), which contains:
  - `nodes`
  - `edges`
  - `clusters`
  - `memory`
  - `stats`

## Non-negotiable parity rule

If you want Hermes-like behavior, use the **real Hermes graph edges**.

Do **not**:
- invent a second synthetic edge layer from categories
- overlay decorative radial structure on top of unrelated connections
- keep two competing visual logics in one graph

Users read that immediately as:
- duplicate graph
- haphazard layout
- overlap/noise
- "this is not the Hermes graph"

## Practical fallback hierarchy

1. **Best:** use the real Hermes graph payload and render a browser-native simplified starmap.
2. **If exact parity is too heavy:** preserve the real nodes + edges, but simplify visuals.
3. **If the simplified port still looks messy:** revert to the previous cleaner graph rather than shipping a confusing pseudo-starmap.

## Visual lessons from the session

The user explicitly rejected a graph that had:
- two visual structures at once
- oversized labeled nodes
- noisy always-on metadata chips
- decorative lines/rings that fought the actual graph
- no useful hover behavior

The cleaner direction that worked better:
- one centered radial graph
- small nodes
- thin muted links
- minimal ring labels
- no always-on node labels on dense views
- hover tooltip with real metadata
- hover neighbor highlighting
- click opens drawer

## Concrete rendering rules

- Prefer **tiny nodes first**, then scale modestly for key/high-use nodes.
- For dense graphs, remove always-on labels before reducing node count.
- Skills can be circles; memories can be diamonds/squares, but keep them subtle.
- Use muted edge opacity by default; brighten only on hover/focus.
- Keep the center label simple; do not stack badges/chips around the graph unless they add real value.
- If the graph is dense, hover must reveal:
  - label
  - type
  - category
  - date
  - use count/state
- Hover should also visually separate the local neighborhood from the rest of the graph.

## UX preference captured here

For this user, a visually confusing approximation is worse than a simpler but coherent graph. When parity is imperfect, choose **clean and restrained** over flashy and approximate.
