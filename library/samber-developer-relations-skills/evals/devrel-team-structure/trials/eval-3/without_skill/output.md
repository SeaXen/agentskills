# DevRel Hub-and-Spoke Restructure — Draft for Board Review

## The math that drives the design

7 people, but not 7 full FTEs of capacity: 5 full-time + 2 people at ~0.5 FTE (split with support) = **6.0 FTE-equivalent** of DevRel capacity.

Your target shape — hub of 2, one spoke per product line (4 lines) — is **6 seats**. That's not a coincidence you need to force; it's a clean fit if you treat the two 0.5-FTE people as jointly filling *one* seat rather than each owning a thin slice of everything.

**Recommended allocation:**

| Seat | Owner(s) | FTE |
|---|---|---|
| Hub — Standards & Editorial Lead | 1 full-time | 1.0 |
| Hub — Tooling & Platform Lead | 1 full-time | 1.0 |
| Spoke — Product Line A | 1 full-time | 1.0 |
| Spoke — Product Line B | 1 full-time | 1.0 |
| Spoke — Product Line C | 1 full-time | 1.0 |
| Spoke — Product Line D (paired) | 2 people at 0.5 | 1.0 |

Put the pair in a **spoke**, not the hub. The hub is the chokepoint everyone else depends on for standards and tooling — halving its availability creates coordination lag for all four spokes at once. A paired spoke only constrains one product line's coverage; the blast radius stays contained.

Pick *which* product line gets the paired spoke using two signals, not seniority: (1) which line already generates the most support-ticket overlap for those two people — that's a natural context bridge, not a tax; (2) which line is lowest-priority for the board this cycle, so reduced bandwidth there is the cheapest place to absorb it. If the two 0.5-FTE people have real editorial/tooling depth instead, swap one into the hub and push a full-timer into the paired spoke — role fit beats raw FTE math when the two conflict.

## Org chart

```
                    ┌─────────────────────────────┐
                    │   HUB (2, full-time)          │
                    │   • Standards & Editorial Lead│
                    │   • Tooling & Platform Lead   │
                    │   Owns: style guide, docs      │
                    │   platform, sample-app/SDK      │
                    │   tooling, metrics definitions, │
                    │   brand voice, review SLA       │
                    └───────────────┬────────────────┘
           ┌───────────┬────────────┼────────────┬───────────┐
           │            │            │             │
      Spoke: A      Spoke: B     Spoke: C     Spoke: D (paired)
      1 FT           1 FT         1 FT          2 × 0.5 FT
      Owns: content, community, talks, samples, changelog — for their line
```

## Who owns what (RACI, one line each)

- **Standards, style guide, brand voice** — Hub accountable, spokes responsible for adherence.
- **Docs platform, sample-repo templates, SDK/testing tooling, analytics instrumentation** — Hub accountable and responsible; spokes consulted on line-specific needs.
- **Product-line content calendar, community Q&A, conference talks, changelog comms** — Spoke accountable and responsible; hub consulted only on cross-cutting campaigns.
- **Cross-product campaigns and platform-wide programs (forum, Discord/Slack, central editorial calendar)** — Hub accountable; spokes consulted.
- **Metrics roll-up and board reporting** — Hub accountable for aggregation; spokes accountable for their own line's raw numbers.

## Cadence

- Weekly 30-min hub-spoke sync, all seats.
- 48-hour async review SLA for spoke content against hub standards — most spoke work should never need a live review.
- Quarterly OKRs: 2 hub-owned (platform/standards), 1 per spoke (product-line-specific).
- Monthly metrics roll-up into one dashboard, hub-owned.

## Why hub-and-spoke, for the board slide

Pure-centralized DevRel becomes a single bottleneck with no product depth. Pure-embedded DevRel (no hub) fragments brand voice and duplicates tooling four times over. Hub-and-spoke is the model the larger API-first companies converge on for exactly this trade-off: one team owns consistency and leverage (tooling, standards, reporting), while each product line gets a dedicated owner who can go deep on that audience without re-inventing infrastructure.

## Risks to flag to the board, not bury

- **Spoke D runs at reduced, variable bandwidth.** Its two owners lose devrel time during support-heavy weeks. Set lighter KPI targets for that line this quarter rather than holding it to the same bar as the solo-owned spokes.
- **Hub is a two-skillset role wearing one hat.** Standards/editorial and tooling/platform are different disciplines. If the two hub people don't naturally split that way, name it now as a hiring gap for the next cycle rather than discovering it in Q2.
- **Review SLA is the hub's real workload risk.** If every spoke publish waits on hub sign-off, the hub becomes the bottleneck the structure was meant to avoid. The 48-hour async SLA plus a published standards doc is the mitigation — track how often it's actually honored.

## 5-week rollout to board day

- **Week 1** — Finalize seat assignments and write a one-page charter per seat (owner, product line, standards they inherit from hub). Migrate in-flight work to new owners.
- **Week 2** — Hub ships its first deliverables: style guide v1, content-calendar template, metrics dashboard skeleton. Spokes can't be held accountable to standards that don't exist yet.
- **Week 3** — Run the structure live for one full sprint. Hub runs its first cross-spoke review. Collect friction points, especially from Spoke D.
- **Week 4** — Adjust based on Week 3 friction. Baseline each product line's KPIs. Build board slides.
- **Week 5** — Rehearse the board presentation. Present the structure as committed for at least one full quarter before the next iteration — a re-org proposed and revised in the same breath reads as unproven to a board.