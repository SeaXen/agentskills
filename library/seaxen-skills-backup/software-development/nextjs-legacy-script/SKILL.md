---
name: nextjs-legacy-script
description: Handling and refactoring Next.js apps that contain giant inline vanilla JS scripts in page.tsx (common in legacy dashboards).
---

# Next.js Legacy Giant Inline Script Pattern

## When to Use
- `page.tsx` contains a 500+ line `const script = String.raw`... block with `document.getElementById`, `onclick` bindings, and state in a closure.
- User reports "nothing working", buttons don't respond, or functionality is flaky.
- Task involves fixing buttons, adding features, or modernizing the app.

## Core Problems
- JSX and the giant script string contain duplicate HTML/attribute strings → `patch` fails with "multiple matches".
- `bind()` function runs once on init; new elements (e.g. Quick Add buttons) need explicit wiring.
- No React state → hard to add loading states, optimistic updates, or reliable re-renders.
- Escaping in patches is extremely fragile.

## Recommended Workflow
1. **First pass**: Remove hero / big marketing sections using precise context (include surrounding Card or grid).
2. **Button fixes**: Extend the existing `bind()` function and add helper functions (`quickAddWatch`, `setBtnLoading`) inside the script block.
3. **New UI elements**: If adding buttons that need JS, always update both the JSX **and** the `bind()` / init section in the same change.
4. **Major changes**: Prefer `write_file` on `page.tsx` over repeated `patch` when the script > ~400 lines.
5. **Long-term**: Extract the script into a separate module or convert to proper React components + `useEffect`.

## Pitfalls
- Never use short unique strings for patch when the file contains a giant script literal — it will match inside the string.
- Do not assume `onclick` bindings will automatically work on newly rendered elements.
- Avoid mixing React state and the closure `state` object without a clear migration path.

## Quick Wins
- Add `data-quick-add` + explicit `querySelectorAll` in `bind()`.
- Introduce `setBtnLoading(id, true/false)` for all action buttons.
- Keep `addWatch` and `quickAddWatch` as separate functions.

## References
- See `references/nextjs-giant-script-pattern.md` for session examples.
