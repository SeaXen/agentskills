# Hermes desktop starmap → AceRoute porting notes

## What upstream commit `931e235` actually does

The commit titled `feat(desktop): /journey opens the memory graph overlay instead of printing` does **not** add the graph renderer itself.

It only reroutes desktop slash commands:
- `/journey`
- `/learning`
- `/memory-graph`

to the existing desktop overlay action:
- `openMemoryGraph()` / `openStarmap()`

So if a user points at that commit and asks to "add the Hermes journey graph", do **not** cherry-pick the commit mentally and assume it contains the visual implementation. Inspect the actual starmap module.

## Actual upstream implementation location

In Hermes desktop, the real starmap implementation lives under:
- `apps/desktop/src/app/starmap/index.tsx`
- `apps/desktop/src/app/starmap/star-map.tsx`
- `apps/desktop/src/app/starmap/simulation.ts`
- `apps/desktop/src/app/starmap/render.ts`
- `apps/desktop/src/app/starmap/constants.ts`
- `apps/desktop/src/app/starmap/types.ts`

## Portable concepts worth copying

For a browser dashboard like AceRoute, the useful transferable ideas are:
- radial time model: **older near center, newer outside**
- bucketed time rings instead of one flat ring per type
- ring labels derived from time buckets
- category-colored node/group relationships
- highlighted "important" nodes (high use, pinned, active)
- click-to-inspect drawer instead of cluttering the graph with too much text

## What not to port literally

Do not try to port the desktop code 1:1 into a simple dashboard page.

Reasons:
- desktop code is React + canvas + d3-force oriented
- AceRoute is currently static HTML + JS and simpler DOM rendering
- Hermes desktop starmap is desktop-first and interaction-heavy
- the exact overlay model is not suitable for a narrow browser page without adaptation

## Practical AceRoute adaptation that worked

A good web-native approximation was:
1. keep the existing Journey page and drawer
2. replace the naive 2-ring graph with a **starmap-style radial layout**
3. group nodes into time buckets (`1d`, `2d`, `7d`, `14d`, `30d`, `90d` chosen from overall span)
4. render bucket rings as tilted ellipses
5. place nodes on each ring with slight deterministic angular jitter
6. connect nodes by shared category using SVG lines behind the buttons
7. surface light metadata chips (`nodes`, `rings`, `bucket width`)
8. on mobile, reduce node count and label count instead of trying to keep full desktop density

## Verification pattern

After the port, verify live in browser, not just by reading HTML:
- Journey page opens
- graph node count is non-zero
- ring count and ring labels exist
- SVG edges render
- clicking a graph node opens the journey drawer
- mutation buttons remain correctly disabled if backend capabilities report read-only
- browser console shows no JS errors

## Durable lesson

When upstream Hermes introduces a new visual surface via a small routing commit, check whether the commit is merely **exposing** an already-existing subsystem. For dashboard parity work, port the subsystem's interaction model, not the small trigger commit.