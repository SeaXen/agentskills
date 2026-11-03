# Obsidian dashboard redesign + auto-recall bridge

## When this reference matters
- Redesigning the Obsidian vault dashboard without breaking recall/search/reader features.
- Fixing clipped reader/recall panels after layout changes.
- Wiring Obsidian vault notes into Hermes chat as targeted warm/cold memory.

## Durable lessons

### 1) Dashboard redesign: preserve behavior first
Use a frontend-first pass before touching backend routes.

Preserve unless you are deliberately replacing them equivalently:
- existing route paths
- DOM ids/classes used by JS handlers
- reader/search/graph/recall button hooks
- API response shapes

Practical rule:
- change CSS/layout first
- validate Python compile + JS syntax + live APIs + browser interactions before claiming success

### 2) Reader clipping fix pattern
If the redesigned dashboard looks good but reader content is clipped or recall cards open below the fold:
- reduce graph dominance; give the reader more vertical share
- do not keep quick actions as sticky overlays inside the scroll region
- move reader action buttons above long tab content
- for async tab content (Recall, Memory Health, Review Queue), scroll after content render, not only on tab switch

Why:
- scrolling on `setReaderTab()` alone can happen before async content exists, so the panel still lands off-screen

### 3) Better Obsidian auto-recall architecture
For Hermes chat recall, prefer this order:
1. dashboard-backed hybrid recall (`/api/recall`)
2. lexical vault scan as fallback only

Why:
- the dashboard already maintains a stronger ranking path than naive file scanning
- fallback keeps recall available if dashboard recall is temporarily unavailable

### 4) Recall injection format
When injecting recalled note context into Hermes, use the native memory wrapper rather than raw plain text.

Reason:
- reduces leakage risk
- aligns with the rest of Hermes memory context handling

### 5) Trigger discipline
Do not trigger recall on overly broad generic words.
Prefer:
- explicit memory cues: `obsidian`, `vault`, `notes`, `memory`, `recall`, `previous`, `history`, `before`, `decision`
- intent-aware boosts for common query classes:
  - decision queries → decisions note(s)
  - fix/root-cause queries → issues/fixes log
  - setup/path/config queries → agent/setup/environment notes

### 6) Intent-aware gating beats blind top-1 retrieval
If semantic recall returns a weak but technically top-ranked result, do not blindly inject it.
Use intent-sensitive inclusion/gating so low-confidence results can be replaced or withheld.

Example pattern:
- decision query + generic daily note top hit -> prefer `decisions.md`
- fix query + generic daily note top hit -> prefer `issues-fixes-log.md`
- setup query + vague hit -> prefer setup/environment docs

### 7) Anti-noise safeguards
Keep these in the bridge:
- cap notes count and chars
- suppress near-duplicate overlaps
- redact obvious secrets in snippets
- stay silent on unrelated chat

## Verification checklist
For dashboard UI changes:
- Python compile passes
- extracted inline JS passes syntax check
- dashboard service is healthy
- `/api/graph`, `/api/memory-health`, `/api/recall-eval`, `/api/memory-candidates` respond
- browser console shows no JS errors
- search, folder filters, reader tabs, note selection, and recall panels still work

For recall bridge changes:
- plugin/module compiles
- direct hook test: targeted query injects recall
- direct hook test: normal chat injects nothing
- fresh Hermes chat session answers a recall-dependent question correctly
- fresh Hermes chat session still returns a trivial reply cleanly (e.g. `OK`)

## Session-specific implementation notes
- Reader visibility was improved by rebalancing layout share, moving quick actions above reader sections, and scrolling recall content after async render.
- Dashboard-backed recall was tuned with intent-aware gating because semantic top hits alone still sometimes preferred generic dashboard/daily notes over the real decisions/fixes note.
- Fresh CLI sessions picked up the new recall bridge immediately; long-running gateway/chat runtimes may need a clean reload to pick up plugin code changes.
