---
name: copilotkit-opendots
description: Use when building persistent agents with their own computer.
---

# OpenDots — persistent agent workspace template

Repo: `CopilotKit/OpenDots` · MIT · **created 2026-09-29** · 155 files · 10,259 LOC src · 1.3k stars in week one.
"An open-source template for persistent AI agents, each with its own computer." Node 24, Hono server, Vite+React 19 client, CopilotKit + AG-UI, TanStack AI, TipTap, native `node:sqlite`.

**A template, not a hosted product.** Single-owner. Clone it and configure your own infrastructure.

Verified locally 2026-09-30: `npm ci` then `vitest run` → **156 tests / 34 files, all pass** in ~20s. For a repo one day old that is the strongest quality signal in it.

## Domain model

- **Dots** — persistent agents, each with a name, role, instructions, and permitted tools.
- **Spaces** — homes for working documents. A Dot can be granted access to several; each has a default destination for saved pages.
- **Pages** — documents in a searchable library (grid/list, nested subpages), edited in a TipTap visual editor with slash commands and undo/redo. Conversation per page and per specialist.
- **Dot computers** — per-Dot isolated browser profile + workspace files that persist across stop/start, via OpenBot's container supervisor. Browser, file, and shell permissions set per Dot.
- **Review before saving** — a HITL card pauses the tool call for Approve & save / Decline.

## The five techniques worth stealing

### 1. `runtime-scope.ts` — an authorization allowlist that mirrors the SDK's own router

CopilotKit's runtime exposes many routes; OpenDots enables a subset. The whole design turns on one hard-won comment:

> `// Match the whole path. The SDK accepts suffix matches, so accepting arbitrary prefixes here would validate a different thread than the SDK dispatches.`

So it matches anchored regexes (`/^agent\/([^/]+)\/(run|connect|suggest)$/`), not prefixes — otherwise your guard approves thread A while the SDK dispatches thread B. It also hard-blocks reserved suffixes that resolve *before* the thread handler inside the SDK router: `clear`, `info`, `inspector-metadata`, `inspector-learning`, `transcribe`, `cpk-debug-events`, `annotate`.

Then it cross-checks the agent ID from **path, body, AND query string**, denying on any mismatch, and resolves every thread via `workspace.requireThread()`.

Lesson: an auth check in front of a framework you don't control must reproduce that framework's routing semantics, not approximate them.

### 2. `browser/security.ts` — SSRF defence that resolves DNS

String-matching a hostname for `127.0.0.1` is worthless. This validates by resolving and checking **every** returned address:

```ts
const addresses = await lookup(hostname, { all: true })
if (!addresses.length || addresses.some(i => !isPublicAddress(i.address)))
  throw new Error('Private or special network addresses are blocked.')
```

`isPublicAddress` covers IPv4 (`0`, `10`, `127`, `>=224`, CGNAT `100.64/10`, link-local `169.254`, `172.16/12`, `192.168/0/2`, benchmarking `198.18/15`, `203.0`) and IPv6 (`2001:` Teredo/benchmarking, `2001:db8`, `2002::` 6to4). Plus: HTTP(S) only, no embedded credentials, ports 80/443 only, `localhost`/`.local` blocked.

### 3. `PageAutosave` — autosave as a real state machine with optimistic concurrency

`src/client/editor/autosave.ts`. State is `saved | dirty | saving | error | conflict`. Key mechanics:

- `generation` counter — switching pages bumps it and resets all state, so a late save from the old page can't land.
- `AbortController` per in-flight save.
- `getSnapshot` / `subscribe` shape (drop-in for `useSyncExternalStore`).
- Saves send `expectedRevision`; the server rejects stale writes.
- **On conflict it never discards the draft**: *"This page changed elsewhere. Your draft is safe. Copy it before loading the latest version."*
- `dirty` stays true while a save is pending, content differs, **or** status is `error`/`conflict` — so a failed save can't silently read as clean.

### 4. Layered edge defence in `server/app.ts`

Middleware order matters; each layer is a separate failure mode:

```
bodyLimit 1MB → host allowlist (403) → origin match (403)
→ sec-fetch-site !== 'cross-site' (403) → timingSafeEqual bearer (401)
→ content-type: application/json on mutations (415)
```

Notes worth copying:
- Token compare uses `timingSafeEqual` **with a length pre-check** — otherwise differing lengths throw instead of returning false.
- No token configured + unrecognized host → 403, so an unauthenticated deployment isn't open to the network.
- `index.ts` **refuses to start** if `OWNER_TOKEN` is set but under 24 chars when binding externally.

### 5. Containers isolated by network, not just filesystem

`compose.yml` places `app`, `browser`, and the computer supervisor on **separate** networks (`browser-link`, `app-egress`, `browser-egress`) so the browser cannot reach the app's egress path. Every service: `cap_drop: ALL`, `no-new-privileges:true`, `init: true`; the browser is `read_only: true` with `shm_size: 256mb`. `deployment/computers/harden-supervisor.mjs` hardens the supervisor.

## Also notable

- **`node:sqlite` (`DatabaseSync`)** — zero native deps. WAL mode, `busy_timeout=5000`, `BEGIN IMMEDIATE` transactions with ROLLBACK on throw, and `lease`/`leaseUntil` columns for scheduled-task ownership.
- **HITL as a tool contract.** `shared/page-review.ts` exports a zod schema plus a tool description that constrains the agent explicitly: *"Do not create the page yourself after this tool: its approved result includes the saved page URL. Call once, then wait for the review result."* Retries recover the same saved page rather than duplicating it.
- **Learning containers are owner-gated.** `learningSelector` throws unless `user.id === workspace.ownerId`; Slack threads must be explicitly bound to the configured Dot before they can enroll.
- **Constants read from env with `:?` guards** in compose (`${OWNER_TOKEN:?Set a 24+ character OWNER_TOKEN in .env}`) so misconfiguration fails loudly at container start.

## Gotchas

- Node **24+** required (`engines.node >=24.0.0`); uses `--env-file-if-exists` and `--import tsx`.
- Binds `127.0.0.1:4310` for the API, Vite on `5173`.
- Manual page editing works **before** any service is configured. Chat needs `INTELLIGENCE_API_KEY` + `INTELLIGENCE_API_URL` + `INTELLIGENCE_WS_URL` and a model provider; voice needs `VOICE_API_KEY`/`VOICE_MODEL`/`VOICE_NAME` separately; Slack needs `SLACK_TEAM_ID`/`SLACK_USER_IDS`/`SLACK_DOT_ID`.
- Missing config must produce a clear setup state, and test fixtures must stay visibly separate from live integrations — the repo holds itself to this.
- `npm test` is `vitest run` (34 files); `npm run build` = `vite build && tsc -p tsconfig.server.json`.

## Honest limits (from the README, not inferred)

Single-owner starting point. **Not included:** shared editing, invitations, file uploads, interactive page embeds. Schedules are recurring instructions, not a goal/event-trigger system. Multi-Dot group conversations and automatic delegation are future work. Skills require review and publication in Intelligence; existing conversations are not enrolled retroactively.

**Verified live by the authors** (2026-09-29/30): Intelligence, model responses, page-context chat, OpenBot browsing/file/shell/persistence, realtime speech, call controls, receipt persistence.
**Still unverified:** Slack and spoken compute delegation against connected services; cloud schedules; published-skill delivery.

## Reuse

The runtime-scope allowlist pattern and the DNS-resolving SSRF guard lift into any CopilotKit/AG-UI project — or into any Node service that fronts a framework with its own router. CopilotKit + AG-UI is the reference stack for agent UIs with inline tool renderers.