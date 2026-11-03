# AceRoute Journey/Search performance + layout follow-up

Session learnings:

## 1. Do not keep Skills/Journey in the global heavy refresh loop
If Search is the landing page, `refreshHeavy()` should not always call `renderSkills()` and `renderJourney()`.

Better pattern:
- heavy analytics refresh runs globally
- Skills/Journey render only when their tab is active
- opening the tab lazy-loads its data if state is empty

This reduces:
- unnecessary large JSON fetches
- browser parse cost
- chart/table re-render churn
- background CPU during idle dashboard refreshes

## 2. Cold Skills load: proper background cache is worth it
`/api/hermes/skills` had multi-second cold hits even though warm hits were fast.

Working fix:
- refactor heavy builder into `_compute_hermes_skills()`
- wrap it with a daemon singleton `SkillsInventoryCache`
- warm it on app startup
- refresh every ~300s
- serve cached payload immediately from `collect_hermes_skills()`

Measured effect in this session:
- before cold-ish samples: ~5-6s
- after cache warmup: ~0.046-0.084s

## 3. Journey drawer latency: prefetch top raw buffers
Main latency source was `hermes journey edit <node>` subprocess cost for raw content.

Working fix:
- add daemon singleton `JourneyItemCache`
- prefetch raw buffers for top-used + recent nodes
- seed the normal TTL cache from that prefetch
- warm on startup beside Skills cache

Measured effect in this session:
- before: ~1.7-2.9s
- after prefetch: ~0.005-0.039s for the tested node

## 4. Optimistic drawer header matters
Even before raw content lands, set drawer title/subtitle from already-loaded page data.
This removes the visible `Loading…` pause and makes the app feel much faster.

## 5. Search/Journey layout packing that worked
### Search top stats
- use a 6-column overview grid for compact one-line stats
- reduce gaps/padding before shrinking typography further

### Journey analytics ordering
Preferred arrangement:
- row 1: `Journey Growth` + `Orphan Heatmap`
- row 2: `Journey Mix` + `Category Health`

This used space better than putting `Journey Mix` beside growth and pushing the heatmap lower.

## 6. Sparse-data dashboards still need honest interpretation
After spacing fixes, remaining empty-looking space was driven mostly by sparse datasets / no-data panels, not broken layout. Distinguish true layout waste from valid empty-state charts during QA.
