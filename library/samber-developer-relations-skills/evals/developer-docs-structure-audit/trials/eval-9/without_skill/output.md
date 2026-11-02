Note one assumption up front: you didn't list what's across the top, so I'm using the industry-standard developer-docs matrix — Diataxis's four modes (Tutorial, How-to Guide, Reference, Explanation). If your matrix uses different modes, the ranking method below still holds; just re-map the 14 cells to it.

## Reconstructed matrix (6 surfaces × 4 modes = 24 cells, 14 empty)

| Surface | Tutorial | How-to | Reference | Explanation |
|---|---|---|---|---|
| Python SDK | ✅ | ✅ | ✅ | ⬜ |
| C++ SDK | ⬜ | ⬜ | ✅ | ⬜ |
| ROS 2 bridge | ⬜ | ⬜ | ✅ | ⬜ |
| Fleet API | ✅ | ⬜ | ✅ | ⬜ |
| On-prem deployment | ⬜ | ✅ | ⬜ | ⬜ |
| Grafana integration | ⬜ | ✅ | ✅ | ⬜ |

`/api/fleet/overview` is the Fleet API **Reference** landing page — it exists, which is why it's not one of the 14. Its 78% exit rate is the signal that tells you which of Fleet API's *empty* cells to fill first: people land on an endpoint index with no task-oriented path forward and no conceptual grounding, then leave.

## Ranking method

Three factors, in priority order:

1. **Proven pain beats inferred pain.** The exit-rate number is hard data — weight it above anything read from Algolia or GitHub issues alone.
2. **Mode dependency.** Reference and Tutorial are foundational; How-to guides deflect support tickets (map these against GitHub issue volume per surface); Explanation resolves confusion but rarely drives a ticket or a search query by itself — lowest urgency.
3. **Existing scaffolding.** A surface with zero docs needs a Tutorial before a How-to guide is useful. A surface that already has Tutorial + Reference (Fleet API) can jump straight to How-to.

## Backlog, in write order

1. **Fleet API — How-to Guide.** Directly targets the 78%-exit page; visitors need a task path out of the reference index.
2. **Fleet API — Explanation.** Closes the "why" gap right under the highest-traffic, highest-friction surface.
3. **Python SDK — Explanation.** Only gap on your most mature, highest-reach surface — cheap to write, high aggregate payoff.
4. **C++ SDK — Tutorial.** Second SDK, zero foundation — must exist before its How-to is useful.
5. **C++ SDK — How-to Guide.**
6. **ROS 2 bridge — Tutorial.** Robotics-specific but sits on the critical hardware-integration path.
7. **ROS 2 bridge — How-to Guide.**
8. **C++ SDK — Explanation.**
9. **ROS 2 bridge — Explanation.**
10. **On-prem deployment — Reference (specs).** Ops teams file tickets over missing requirements/ports/versions more than missing narrative.
11. **On-prem deployment — Explanation (architecture).** High-stakes, low-frequency action — readers want to understand before they act.
12. **Grafana integration — Explanation.** Helps interpret dashboards; narrowest audience of the six surfaces.
13. **On-prem deployment — Tutorial.** Largely redundant with the How-to that already exists — lowest urgency in that surface.
14. **Grafana integration — Tutorial.** Same redundancy argument, smallest audience — last.

## Schedule (writing starts Monday, ~1 page/day)

- **Week 1 (Mon–Fri):** items 1–5
- **Week 2 (Mon–Fri):** items 6–10
- **Week 3 (Mon–Thu):** items 11–14

## Re-rank before you commit to it

⚠️ Items 1–3 are grounded in the exit-rate number you gave me; items 4–14 are ordered on reach/dependency logic, not your actual Algolia or GitHub data. Before Monday, pull two numbers that can reshuffle tiers 2–5:

- Algolia: top zero-result queries and top queries-then-bounce, filtered by surface name. If C++ SDK or ROS 2 bridge dominates over Fleet API, promote items 4–9 ahead of item 3.
- GitHub issues: issue count by surface label. If on-prem deployment or Grafana carries more open issues than C++/ROS, pull items 10–12 forward.
- Analytics: exit rate on the C++/ROS/on-prem/Grafana landing pages. Anything rivaling 78% jumps to tier 1 alongside Fleet API.