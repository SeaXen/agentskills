# X/Twitter in Hermes — cost framing and tool-choice matrix

## Practical split

### `x_search`
Use for:
- search
- monitoring
- read-only discovery
- topic sampling

Cost reality:
- backend-dependent
- do not automatically present it as official X API billing
- enabled tool != guaranteed free usage forever

### `xurl`
Use for:
- posting
- replying
- quoting
- likes / reposts / bookmarks
- DMs
- media upload

Cost reality:
- CLI install is free
- underlying X API usage is the real billing surface
- frame official X API usage as likely paid / pay-per-use unless live account proof says otherwise

Activation rule:
- `xurl --help` proves install only
- `xurl auth status` determines whether it is actually usable
- if no apps/tokens are present, report: **installed, not authenticated**

### X MCP
Use for:
- MCP-native automation inside Hermes
- users who want X as first-class tools in an MCP-heavy setup

Cost reality:
- MCP runtime/package can be free
- X API calls remain the paid/credentialed surface

Activation rule:
- do not add the server to Hermes config without credentials
- installing runtime alone is fine
- status should be: **runtime installed locally, not connected to Hermes yet** when creds are absent

## Recommended default advice

- research only → `x_search`
- account actions → `xurl`
- full workflow → `x_search` + `xurl`
- MCP-centric architecture → add X MCP after credentials exist

## Durable pitfall

Avoid creating a dead X MCP config entry just because the user asked to "add all". Installing a runtime without creds is fine; enabling a broken startup entry is not.
