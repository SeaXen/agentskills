# Hermes dashboard config-panel polish

Use this when a Hermes dashboard Config page has a dedicated operator panel for a setting that also still appears in the generic schema-rendered form.

## Problem shape
- A dedicated panel was added for a config-backed setting such as `command_allowlist`.
- The raw schema field still renders in the normal form.
- The page feels duplicated, cluttered, or visually broken even though the feature technically works.
- The user may specifically ask to move the dedicated panel lower on the page or complain that the action button does not line up with its input.

## Durable fixes
1. **Do not let the dedicated panel interrupt the main settings flow** unless the user explicitly wants it near the top.
   - For Dr. Sagar, secondary operator panels belong below the primary form by default.
2. **If the dedicated panel is the intended UX, hide or demote the raw generic field** from the schema-rendered form.
   - Otherwise users see two surfaces for the same setting and lose trust in which one is canonical.
3. **For input + button rows, verify real alignment with DOM geometry** after the frontend build.
   - Good proof: equal heights, same top edge, same bottom edge.
   - Example browser-console check:
     ```js
     (() => {
       const input = document.querySelector('input[placeholder="e.g. docker ps --format {{.Names}}"]');
       const btn = [...document.querySelectorAll('button')].find(b => b.textContent?.trim() === 'Add pattern');
       const ir = input?.getBoundingClientRect();
       const br = btn?.getBoundingClientRect();
       return {
         inputHeight: ir?.height,
         buttonHeight: br?.height,
         sameTop: ir && br ? Math.abs(ir.top - br.top) < 2 : null,
         sameBottom: ir && br ? Math.abs(ir.bottom - br.bottom) < 2 : null,
       };
     })()
     ```
4. **For list-management panels, a complete UX set is**:
   - list current entries
   - add
   - edit
   - copy
   - delete one
   - clear all
   - exact-match tester if matching semantics are strict
   - runtime refresh/restart hint when changes are not immediately reflected in live sessions
5. **Dashboard restart pitfall**
   - Do not run `hermes dashboard --stop && hermes dashboard ...` as one tracked background job.
   - `--stop` can kill the dashboard process tree you are trying to relaunch.
   - Safer sequence:
     1. stop existing dashboard
     2. start a fresh dashboard command separately
     3. verify `ss -ltnp`, PID, and HTTP 200 on the expected port

## Verification checklist
- frontend build passes
- live browser route shows the panel in the intended order on the page
- add/edit/delete/clear all work against live API
- if alignment was changed, DOM geometry confirms the input/button row is actually aligned
- final real config state is restored after testing
