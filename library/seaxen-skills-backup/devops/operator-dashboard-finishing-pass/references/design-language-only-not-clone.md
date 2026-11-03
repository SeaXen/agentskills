# Design language only, not clone

Use this note when the user points at another dashboard/app and says things like:
- "take the idea only"
- "do not make same to same"
- "use that design style"
- "combine features, not the product"

## Durable lesson
A visual inspiration request is often about:
- density
- dark/light palette direction
- chart/table rhythm
- header/sidebar hierarchy
- spacing discipline
- compact professional feel

It is **not** permission to clone:
- the source product's feature set
- the source product's domain widgets
- a sibling internal dashboard's structure one-for-one

## Anti-clone checklist
Before building:
1. Name the **real product** you are improving.
2. Name the **real data/actions** that product must expose.
3. List only the **visual traits** being borrowed from the inspiration.
4. Delete any panel whose only justification is "it looks like the inspiration app".

## Operator-dashboard rule
If the surface is actually a Hermes/operator console:
- no fake trading widgets
- no fake equity line
- no fake buy/sell flow
- no fake order book
- no fake market rails unless they map to real operator metrics

Replace them with real panels such as:
- sessions
- providers/models
- cron health
- system/gateway state
- cost/tokens/activity
- alert/watchlist rails backed by real payloads

## Merge-two-dashboards rule
When asked to combine two internal dashboards into one home surface:
- do not visually reskin one source and call it done
- do not expose both dashboards as a loose pile of panels
- build one dense homepage that remaps the strongest signals from both sources into a single operator flow

## Performance pattern that fit this class well
When a unified homepage was becoming slow because it made many frontend API calls, the good pattern was:
- move the homepage to **one batched backend endpoint**
- fan out server-side
- add a short cache
- optionally pre-warm on startup if cold fan-out is expensive

That keeps the page visually dense without making it network-chatty.

## Removal counterpart
1. source/dist/nav references
2. runtime plumbing (systemd unit, static deploy dir, helper scripts, bound port)

Do not stop after removing route labels if the standalone service is still listening on its old port.
