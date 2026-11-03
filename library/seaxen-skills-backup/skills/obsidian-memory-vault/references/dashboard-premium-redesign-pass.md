# Dashboard premium redesign pass

Use this when redesigning `/mnt/tb/hermes/obsidian_dashboard.py` after the 2026-05 frontend pass.

## Durable pattern

For this dashboard class, prefer a **frontend-first, backend-safe** redesign:

1. Backup the Python script.
2. Capture baseline service/API counts.
3. Modify the inline `<style>` / safe HTML only first.
4. Preserve existing IDs and onclick handlers.
5. Avoid backend/API changes unless explicitly required.
6. Validate syntax, restart service, then do browser QA.

## Known-good preservation contract

Do not remove or rename these routes/features during visual redesign:

- GET `/`, `/api/graph`, `/api/layout`, `/api/note`, `/api/recall`, `/api/recall-feedback-summary`, `/api/recall-eval`, `/api/memory-health`, `/api/memory-candidates`
- POST `/api/layout`, `/api/recall-feedback`, `/api/memory-review`
- Notes: search `#q`, clear, open first, folder/tag filters, list modes, saved searches, orphan lane
- Graph: `#graph`, `#minimap`, force layout, zoom/pan, node drag, pinning, focus mode, hull clusters, graph presets, save/load layout, legend/help
- Reader: note open, markdown render, note facts, Overview/Links/Recall/Important tabs, backlinks, related notes
- Memory/recall: hybrid recall, feedback voting, Recall QA, Memory Health, Memory Review Queue, candidate approve/reject flow
- State: localStorage view state, saved searches, pinned node positions, active reader tab
- Keyboard: `/` search focus, Esc clear

## Visual direction that worked

- graph-first layout
- notes sidebar as navigation
- reader as inspector
- one disciplined violet/blue accent plus semantic status colors
- single coherent `:root` token block
- restrained borders/shadows, fewer decorative gradients
- active note card with a clear left accent marker
- command-palette-like search box
- sticky reader tabs/actions only inside `.readerMeta`

## Concrete improvements from the pass

- Consolidated duplicate `:root` blocks into one theme block.
- Rebuilt component styling around panels, buttons, note cards, graph overlays, reader tabs, markdown content.
- Shortened sidebar search placeholder to avoid clipping: `Search notes…`.
- Reduced graph label density by lowering label limits and raising degree/zoom thresholds.
- Kept `.readerMeta` as the only reader scroll container.

## Reader / Root clipping fix pattern

If the user reports the Root/Recall/Memory Health reader card is only visible as a small cut-off strip:

1. Inspect `.rightContainer` row split. The graph can dominate vertical space; increase the reader row share/min-height before adding nested scrolls.
2. Keep `.readerMeta` as the only scroll container. Do **not** add `overflow:hidden` to `.reader`, `.readerSections`, or `.readerSection`.
3. Do not use a sticky-bottom `.readerActions` overlay. Make action buttons normal static flow so they cannot cover reader content.
4. Place `.readerActions` **before** `.readerSections` in the reader HTML, so Dashboard/Decisions/Recall QA/Memory Health controls appear above the active tab body rather than after long content.
5. Add/keep a helper like `scrollActiveReaderTabIntoView()` and call it from `setReaderTab()` and after async renderers (`runRecallEval`, `runMemoryHealth`, `runMemoryReviewQueue`) set `host.innerHTML`. Otherwise async panels may render below the visible `.readerMeta` area with `scrollTop=0`.
6. Browser-verify with geometry, not just screenshots: compare `.readerMeta.getBoundingClientRect()` against the active panel rect and ensure the panel bottom is within the reader bottom after auto-scroll.

Known-good final state from the fix: `.readerActions` static, actions before `.readerSections`, `.readerMeta` has nonzero `scrollTop` for non-overview tabs when needed, and Memory Health/Recall panels are mostly/fully visible without manual scrolling.

## Verification sequence

Run after edits:

```bash
python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py
python3 - <<'PY'
from pathlib import Path
s=Path('/mnt/tb/hermes/obsidian_dashboard.py').read_text()
print('root_count', s.count(':root'))
start=s.index('<script>')+len('<script>')
end=s.index('</script>', start)
Path('/tmp/check_dashboard.js').write_text(s[start:end])
print('js_chars', end-start)
PY
node --check /tmp/check_dashboard.js
systemctl --user restart obsidian-vault-dashboard.service
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6065/
```

Then verify API endpoints:

- `/api/graph` note/link counts should match baseline unless vault content changed.
- `/api/memory-health`
- `/api/recall-eval`
- `/api/memory-candidates`

Browser QA:

- no console JS errors
- notes render
- search and clear work
- folder filter works
- graph renders
- reader tabs work
- Memory Health works
- Recall QA works
- Review Queue works

## Taste rule

Do not call it 10/10 based on appearance alone. For Dr. Sagar, only call it 10/10 after live function checks and browser QA pass. Otherwise call it a “premium redesign candidate” and state the remaining blockers honestly.
