# Obsidian dashboard redesign — phased workflow

Use this when the vault dashboard is visually noisy, cramped, or structurally weak but already functional.

## Goal
Redesign without destabilizing the dashboard service or degrading graph/recall behavior.

## Working pattern
1. Audit the live dashboard first.
   - Inspect browser snapshot/vision, not just source.
   - Identify noise by class: layout waste, control density, graph clutter, reader weakness, editorial/tool-language.
2. Back up `obsidian_dashboard.py` before each phase.
   - Keep one backup per phase, not one giant rolling overwrite.
3. Implement in narrow phases.
   - Phase 1: structure/layout cleanup.
   - Phase 2: graph control-density reduction.
   - Phase 3: declutter + make reader/content more prominent.
   - Phase 4: premium visual polish only; no backend behavior changes.
   - Phase 5: editorial cleanup and quieter control wording.
4. Verify after every phase.
   - Python syntax check.
   - Extract inline JS and run `node --check`.
   - Restart service.
   - Recheck root HTTP and core APIs.
   - Re-open in browser and confirm the change is visibly live.
5. Treat immediate post-restart HTTP `000` as a startup-race possibility, not automatic failure.
   - Recheck service state and retry root/API probes before concluding breakage.

## Durable UI lessons
- Make the graph the focal area, but move support chrome out of the canvas when possible.
- Hide help overlays by default.
- Reduce label density aggressively; only important labels should surface easily.
- Keep sidebar rows compact by default; expand emphasis only for the active note.
- Reader panel should show excerpt/body flow clearly, not act like an afterthought.
- Prefer calmer product-language labels over admin-tool jargon.
  - Examples from a successful cleanup: `Latest`, `Home`, `Focus`, `Groups`, `Fixes`, `Tidy`.
- Reduce status-chip noise; visual state should carry more weight than explanatory suffix text.

## Verification checklist
- Service active after restart.
- Root URL returns HTTP 200.
- Graph API works.
- Health/recall endpoints still work.
- Broken links count did not regress.
- Browser QA confirms the new layout is actually applied, not just syntactically valid.

## Common pitfall
Do not attempt one giant regex rewrite of the dashboard source. Safer pattern: inspect exact source segments, patch targeted blocks, then validate and refresh live UI.
