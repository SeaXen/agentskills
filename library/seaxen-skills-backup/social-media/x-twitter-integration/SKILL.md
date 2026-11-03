---
name: x-twitter-integration
description: "Choose and operate the right Hermes path for X/Twitter: x_search, xurl, or MCP."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# X/Twitter Integration in Hermes

Use this when the user wants Hermes to work with X/Twitter and the first question is **which path to use**:
- built-in `x_search`
- `xurl` CLI against the official X API
- an X/Twitter MCP server

This skill is for **tool selection, setup sequencing, pricing framing, and safe activation**.

## When to use

Trigger on requests like:
- "Can Hermes use X/Twitter directly?"
- "Should I use x_search or xurl?"
- "Add X/Twitter to Hermes"
- "Set up posting / replying / monitoring on X"
- "Can I do X via MCP?"

## Decision rule

Start by separating the user's goal into one of three buckets.

### 1. `x_search` — best for read-only discovery

Use `x_search` when the user wants:
- search
- monitoring
- topic discovery
- sentiment sampling
- recent-post research

Good fit:
- lower risk
- no account-side effects
- simplest first step for users who mainly want intelligence/research

### 2. `xurl` — best for real account operations

Use `xurl` when the user wants:
- post
- reply
- quote
- like / repost / bookmark
- DM
- media upload
- official X API account automation

Good fit:
- official CLI path
- structured JSON output
- cleaner than MCP for many account-operation workflows

### 3. X MCP server — best for tool-style in-agent automation

Use an X MCP server when the user specifically wants:
- Hermes-native tool exposure for X actions
- MCP architecture consistency with the rest of their stack
- agent workflows where X operations should appear as first-class tools

Good fit:
- unified tool surface inside Hermes
- useful if the user already prefers MCP-heavy workflows

## Default recommendation

If the user is unsure, recommend this order:
1. **`x_search` first** for research/monitoring
2. **`xurl` second** for account actions
3. **X MCP** only if they specifically want MCP-style automation

Blunt rule:
- **research only** → `x_search`
- **posting/account ops** → `xurl`
- **serious full automation** → both `x_search` + `xurl`
- **MCP-centric architecture** → add X MCP too

## Pricing / cost framing

Do not answer "is X free?" with a blanket yes/no. Split the layers.

### `x_search`
- The Hermes tool may already be enabled
- Cost depends on the backend/provider powering it
- Do **not** automatically equate it with official X API billing

### `xurl`
- The CLI itself is free to install
- It uses the **official X API**
- Real usage should be framed as **likely paid / credit-based / pay-per-use** unless you have live proof of a free allowance that fits the user's case

### X MCP
- The MCP server package/runtime can be free
- The underlying X API calls are the potentially paid part
- Same billing reality as other official X API integrations

Reference: `references/x-api-cost-and-tool-choice.md`

## Safe activation sequence

### For `x_search`
1. Check whether the toolset is already enabled
2. If yes, prefer using it immediately for read-only tasks
3. Do not oversell permanence of free usage; backend/provider cost may still exist

### For `xurl`
1. Install the CLI
2. Verify with `xurl --help`
3. Verify auth state with `xurl auth status`
4. If auth is missing, stop and tell the user exactly that `xurl` is installed but **not authenticated**
5. Do **not** ask the user to paste X secrets into chat
6. User completes X app registration and OAuth outside the agent session

Correct status language:
- "installed, not authenticated"
- not "ready" unless auth is actually present

### For X MCP
1. Install the MCP server runtime locally
2. Verify the server executable exists
3. Check whether credentials are available
4. **Do not wire it into Hermes config if credentials are absent**
5. Explain that adding a broken MCP server only creates startup failures/noise
6. Only enable after credentials are present

Correct status language:
- "runtime installed locally, not connected to Hermes yet"
- not "configured" unless it is actually in config and can authenticate

## Important pitfalls

### Pitfall: creating a dead MCP entry

Do not add an X MCP server to Hermes config just because the user said "add all" if there are no X credentials yet.

Why:
- it starts broken
- it adds noisy failures at Hermes startup
- it creates a false impression that X is operational

Better:
- install runtime
- state what is missing
- enable only once credentials exist

### Pitfall: claiming `xurl` is ready after install

`xurl` installation is not the same as X API readiness.

Always distinguish:
- binary present
- auth configured
- actual usable account action path

### Pitfall: collapsing tool cost and API cost into one answer

Users ask "is this paid?" about three different layers at once:
- the Hermes tool
- the CLI or MCP package
- the underlying X API

Answer each layer separately.

## Strong response template

When the user asks what to add, the best practical answer is usually:
- `x_search` for research
- `xurl` for official account actions
- X MCP only if they want MCP-native automation

Then give a state summary in this format:
- `x_search` → ready / enabled
- `xurl` → installed, authenticated or not authenticated
- `x-mcp` → runtime installed or not installed; connected to Hermes or not

## If the path is already chosen

### `xurl` as the execution lane
When the user already knows they want official X account operations, treat `xurl` as the concrete execution lane under this umbrella rather than loading a separate micro-skill first.

Durable lessons from prior `xurl`-specific work:
- installation is **not** readiness; say `installed, not authenticated` until `xurl auth status` is truly good
- never ask the user to paste X secrets into chat
- do not read or surface `~/.xurl`
- in Docker-like Hermes layouts, credential visibility depends on the actual subprocess `HOME`
- a wrong default app profile is one of the most common causes of "auth succeeded but commands still fail"
- keep cost framing separated: CLI package cost, Hermes tool path cost, and underlying X API cost are not the same thing

### Good umbrella behavior
- choose among `x_search`, `xurl`, and MCP when the user is undecided
- once chosen, continue within this umbrella using the chosen lane's operational rules
- avoid fragmenting X/Twitter work into multiple tiny skills unless a genuinely different class of task appears

## References

- `references/x-api-cost-and-tool-choice.md` — concise cost framing and tool-selection matrix
