# Mission Control dashboard: dist-only maintenance example

## Situation
A Hermes dashboard/plugin needed real operator-console improvements, but the repository only exposed built assets under the plugin directory and did not contain an editable source tree for that UI.

## Pattern used
1. Confirmed only bundled assets existed for the dashboard.
2. Backed up the bundle and stylesheet to `*.bak` copies.
3. Added failing tests first:
   - plugin smoke tests for visible bundle/UI surfaces
   - API contract tests for frontend-client/backend wiring
4. Patched the built JS/CSS directly.
5. Added missing backend/client methods where the UI required real mutation.
6. Verified with targeted pytest runs plus syntax checks.

## What this caught
- The dashboard needed more than visual controls.
- Real cron editing required a frontend API client method plus existing backend update-route use.
- Persistent toolset toggles required a new backend endpoint and config-save path, not just local UI state.
- Session-lineage and density features were safe to implement entirely in the bundle once supporting data was already available.

## Durable lessons
- For dashboard/operator-console work, add **bundle smoke tests** for the visible controls and **API contract tests** for real actions in the same pass.
- Reuse existing persistence helpers when possible; do not create a second configuration path just for the dashboard.
- Append feature CSS blocks rather than interleaving scattered edits through generated stylesheets.
- Finish with both behavior tests and parse/syntax checks because generated-bundle edits are prone to subtle breakage.

## Example verification commands
- `pytest tests/plugins/test_mission_control_dashboard_plugin.py tests/hermes_cli/test_mission_control_dashboard_api_contract.py -q`
- `python -m py_compile hermes_cli/web_server.py`
- `node --check plugins/mission-control/dashboard/dist/index.js`

## When to escalate beyond this pattern
If the user wants broad ongoing UI evolution, mobile polish, or frequent iteration, recommend restoring a real source/build workflow after the urgent patch lands. Dist-only edits are best for contained or time-sensitive maintenance.