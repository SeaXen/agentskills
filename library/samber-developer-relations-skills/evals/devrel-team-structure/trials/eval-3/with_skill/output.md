Three things to confirm with your team before this goes on a board slide — I've flagged each inline, and drafted around sensible defaults so the structure itself is ready now:

1. **Funded driver** (question the skill insists on first) — I assumed *developer adoption*, since that's what justifies mirroring "big API companies." If it's actually product input or sales enablement, the reporting-line section below changes.
2. **Real work inventory** — I couldn't fill the surface-by-surface table with your actual owners/hours (I don't have that data), so it's a skeleton. Fill it in before you finalize; it's what stops the new chart from erasing work someone's doing invisibly today.
3. **The headcount math doesn't cleanly fit "hub of 2 + spoke per line."** I found a real gap and designed around it rather than around it — see Shape, below. This is the most important thing in this brief.

---

# DevRel org design brief — Riverbend Analytics, 2026-09-23

## Situation

Board review in five weeks (~2026-10-28) is the trigger. You want to present a move from your current structure to hub-and-spoke, modeled on how large API companies run DevRel.

**Funded driver: assumed developer adoption** — developers evaluate and pull in Riverbend's tooling, and that's the standard driver behind a product-line-mirrored hub-and-spoke shape. *Confirm this; if the real driver is product input or sales enablement, re-run Step 2 below with the correct leader.*

Current reporting line, current functional coverage, and who sponsors the budget were not stated — flagged as open in Reporting line and Budget below.

## Work inventory

Not populated with your real surfaces and owners — I don't have that data, and the skill this brief follows is explicit that proposing a shape without it re-assigns work someone is already doing invisibly, and that person stops doing it the day the chart changes. Before you present, fill this in:

| Surface (docs, quickstarts, blog, community venue, events, SDKs per product line, changelog, support presence, sample apps…) | Owner today | Their manager | Hours/week | What breaks if it stops |
| --- | --- | --- | --- | --- |
| … | … | … | … | … |

Do this per product line — with four lines, you likely have at least 4× SDK/sample-app rows and at least one shared row (community, blog) that doesn't cleanly belong to one line. Those shared rows are exactly what the hub is for.

## Reporting line

**Framework, pending confirmation of the funded driver:**

> DevRel reports to `<function>`, because the funded driver is `<driver>` and `<leader>` owns it. This line will starve `<pillar>`. `<named person/team>` covers that gap, reviewed at `<date>`.

- If adoption (assumed): reports to **Marketing** — optimizes reach and launch alignment, starves the product feedback loop over time. Counter-move: a standing roadmap slot for the hub lead, and a rule that no DevRel surface carries a lead-gen gate.
- If product input: reports to **Product** — optimizes the feedback loop and enablement depth, starves distribution muscle. Counter-move: a named marketing partner with an agreed share of the channel calendar.

Given the shape below organizes spokes *around* your four product lines, whichever line you pick, put the standing product-feedback interlock in writing regardless — the hub-and-spoke shape only pays for itself if the product proximity it buys is actually used. *(Source: reporting-line spread — marketing 33.1%, product 21.7%, CEO 20.3%, engineering 19.9%, sales 3.2% — State of Developer Relations 2024, DevRel.Agency, 310 respondents. No line holds a majority; this is a trade-off, not a lookup.)*

## Shape

**Headcount reality first, because it's the whole ballgame here.** You have 7 people, 5 full-time on DevRel, 2 split their week with support. For capacity math I'm treating the 2 split people as ~0.5 FTE-equivalent each on DevRel — **flag this ratio, confirm the real split** — giving **6.0 FTE-equivalent capacity across 7 named heads.**

Three candidates, in the order the underlying skill ranks shapes by efficiency:

**Candidate 1 — Centralized.** One team, one manager, everyone serves all four product lines. Cheapest, most reversible, buys one voice. Rejected: with four product lines already competing for attention, this is exactly the setup that produces a request queue no single manager can prioritize — and it doesn't buy the per-product roadmap proximity you're presenting hub-and-spoke to get.

**Candidate 2 — Textbook hub-and-spoke (2 hub + 1 spoke × 4 lines), no reserved backup.** This is what "big API companies" actually run, and it's what you asked for literally. Staffing it eats all 5 full-timers (2 hub + 3 spokes) plus one of the two split people as the 4th spoke — leaving the second split person unassigned, and **every single seat at bus factor one.** First thing that breaks: any spoke owner takes PTO or gets sick during a launch week, and that product line goes dark with nobody covering it. This is close to a named failure mode in the underlying skill — copying a large company's shape when you can't staff the spokes it presupposes. **Not recommended as-is**, but it's the story a board slide modeled on Stripe or Twilio implicitly promises, so a board member who's used a competitor's docs will ask exactly this question. Better to walk in with the answer than get caught by it.

**Candidate 3 — Right-sized hub-and-spoke (recommended).**

| Seat | Headcount | Role |
| --- | --- | --- |
| Hub | 2 FT | Standards, tooling, cross-product consistency, shared calendar |
| Spoke — Product Line 1 | 1 FT | Full-time owner |
| Spoke — Product Line 2 | 1 FT | Full-time owner |
| Spoke — Product Line 3 | 1 FT | Full-time owner |
| Spoke — Product Line 4 | 1 split-with-support (~0.5 FTE) | Partial-capacity owner — see risk below |
| Floating / backup + Support liaison | 1 split-with-support (~0.5 FTE) | Named backup across all 4 spokes; owns the Support interlock |

This keeps the shape you want to present — a hub owning craft and standards, one spoke per product line — but makes the backup problem a **named seat** instead of a silent gap. Two honest costs to say out loud in the room, not discover in Q&A:

- **The floating seat is shared backup, not dedicated 1:1.** If two spokes need coverage in the same week, it can't cover both. This is the residual risk — name it as a re-org trigger below, not a solved problem.
- **Spoke 4 runs at roughly half capacity of the other three.** Put your smallest or lowest-complexity product line there, and treat "fund spoke 4 to full-time" as the natural headcount ask that pairs with this restructure at the board review.
- **Capacity check, shown not asserted:** Hub (2.0) + three full spokes (3.0) = 5.0 FTE already committed to named recurring surfaces, against 6.0 FTE-equivalent total. That's over 80% of capacity pre-committed, above this skill's own 70%-of-capacity planning baseline (baseline, not a benchmark — chosen to leave room for support spikes, launches, and travel). You are staffing this shape at the edge, not with headroom. Say that plainly to the board rather than let a good org chart imply spare capacity that doesn't exist.

**This sits below the field's own centralized-only rule of thumb (roughly ten full-time people is where shapes other than centralized become affordable without straining).** Proceeding at 7 is defensible only because of the floating-backup seat above; without it, the honest recommendation would be to stay centralized with informal craft leads until you're at 9–10.

## Coverage

Placeholder — confirm against your real inventory once built (Step 1 above). Based on the shape above:

| Function | State |
| --- | --- |
| Advocacy | Owned — primarily by spoke owners, per product line |
| Community management | **Recommend: owned by the hub, not split per spoke.** Four separate community venues fragment the audience and produce per-product content with no cross-product story — this is the exact imprint a team split by product line produces if community isn't held centrally. |
| Technical writing | Shared — hub sets standards, spokes write product-specific docs, unless engineering already owns this (confirm — it sits under another manager at roughly 6 in 10 DevRel teams, and is the single most common place work falls through a gap between two orgs) |
| Developer marketing | Shared with your marketing org — hub owns the editorial calendar, marketing distributes |
| Developer education | **Recommend: deliberately refused this year**, in writing. The capacity math above has no room for it, and an unstated refusal reads as a miss rather than a decision. |
| Developer-experience engineering | Unowned by this team — stays with core engineering, service interlock only |

## Roles

| Seat | Surfaces owned | Backup | Capacity assumption |
| --- | --- | --- | --- |
| Hub lead | Standards, tooling, calendar, reporting line management | Hub craft | 70% |
| Hub craft | Tooling, cross-spoke consistency | Hub lead | 70% |
| Spoke 1–3 owners | Full DevRel surface for their product line | Floating seat (shared) | 70% |
| Spoke 4 owner | Full DevRel surface, reduced hours | Floating seat (shared) | ~35–40% (split with support) |
| Floating/backup | Named backup for all spokes; Support interlock | Hub, in a pinch | ~35–40% (split with support) |

Bus-factor-one risk, flagged rather than hidden: **the floating seat itself.** It backs four spokes with roughly half a person. If it's out, every spoke reverts to bus factor one simultaneously.

## Interlocks

- Product (×4, one per line) — collaboration during launches, X-as-a-service otherwise — feedback in, roadmap/launch dates out — arbiter: each product line's lead.
- Engineering — facilitation — technical review in, writing/demo coaching out — arbiter: eng manager.
- Docs/technical writing — X-as-a-service, either direction — drafts, reviews, structure decisions — arbiter: hub craft.
- Support — X-as-a-service — recurring failure signals in, troubleshooting content out — arbiter: floating seat, since they already sit half in support.
- Developer marketing — collaboration on campaigns, X-as-a-service on distribution — content in, channels/audience data out — arbiter: hub lead.
- Sales — X-as-a-service, strictly — evaluation material out, objections in — arbiter: hub lead. *(Confirm this applies — not stated whether Riverbend's motion involves sales-assist.)*

## Ladder & titles

Not stated — confirm which ladder (engineering, marketing, or DevRel-specific) these seven roles sit on. If "hub lead" carries company-level accountability, it warrants a real manager or director title, not an ambiguous "Head of DevRel." Sanity check only, not DevRel-specific data: a hub lead managing 4 spoke owners + 1 hub peer + 1 floating seat sits inside the general 5–8 direct-report span-of-control convention — worth noting, not a finding.

## Budget

Not stated — confirm who owns headcount budget vs. program budget; they're different people in roughly 6 in 10 DevRel programs, and it changes who signs off on the spoke-4-to-full-time ask above.

## Re-org triggers

- The funded driver changes, or its sponsor leaves.
- The floating seat's backup load runs above capacity for 3 consecutive weeks — signal to fund a second backup seat.
- Spoke 4 stays at partial capacity for more than two quarters without a headcount decision either way.
- A 5th product line ships — the spoke math above changes.
- Either split-with-support seat gets pulled further toward support, eroding the ~0.5 FTE this design assumes.
- A second team starts doing DevRel-shaped work (e.g., marketing spinning up its own community channel) without a declared interlock.
- Headcount crosses ~9–10 — a dedicated second backup seat becomes affordable instead of shared.

## Transition

- **Week 1:** Publish this brief internally; name the hub and spoke owners; confirm the driver, reporting line, and budget owners flagged above.
- **Month 1:** Stand up the hub-spoke sync ritual (this is the "standing forum" the shape needs); if community is currently split per product, begin consolidating it under the hub.
- **Quarter 1:** Review actual floating-seat backup load against the capacity math above; use that data, not a guess, to decide whether spoke 4 needs to move to full-time before the next planning cycle.
- **Unchanged:** whatever reporting line you confirm, whatever coverage gets explicitly refused.

---

## Quality gate

- Work inventory with named owners — **not met**, template only; you must complete this before presenting.
- Reporting line names driver/leader/starved pillar/cover — **conditionally met**, pending driver confirmation.
- Shape justified by coordination bought, not by copying a larger company — **met**; Candidate 2 (the literal "big API company" copy) was explicitly rejected in favor of Candidate 3, with the staffing gap shown, not asserted.
- All six functions carry one of five coverage states — **met**.
- No surface at bus factor one without being flagged — **met**, with the floating seat itself named as the residual risk.
- One interaction mode + named arbiter per adjacent team — **met**.
- Planned work fits inside 70% of capacity — **not met, flagged**: Candidate 3 runs at ~83% of stated capacity. Said explicitly above rather than hidden.
- Every number labeled sourced/baseline/refused — **met**.
- No headcount ratio quoted as benchmark, no compensation band — **met**.
- Re-org triggers non-empty and observable — **met**.

Net: the structure is board-ready in shape; the work-inventory table, driver confirmation, and the over-70%-capacity flag are the three things to close before it's presentation-final.