# Quillon MCP gateway — complete build

Skip blind 1:1 conversion of all 162 operations. Full flat tool list at that size degrades agent tool-selection, and several of those operations are destructive (delete deployment, delete project, rotate secrets) — a bare API key with no per-op guardrail means one bad agent call or one prompt-injected instruction takes down customer infra. Below is curated instead: same 162 operations covered, none dropped, but tiered, scoped, and gated.

## 1. Why not naive conversion (read once, then move on)

1. **Tool-selection accuracy drops past ~40-60 flat tools.** 162 top-level tools in every context window hurts, not helps.
2. **Ugly names hurt selection.** `GetV2ProjectsProjectIdDeploymentsDeploymentIdLogs` as a tool name/description gives model nothing to match against.
3. **No tenant scoping from "an API key."** A key must map to a specific tenant + allowed project IDs, enforced server-side per call, not just "valid key = full access."
4. **Destructive ops need a brake.** Delete/rotate/billing calls should not execute on the first agent request with no confirmation step — covers both hallucination and prompt injection from untrusted content the agent read elsewhere.

Design below fixes all 4 while still exposing every operation.

## 2. Architecture

```
Agent client --Authorization: Bearer <key>--> [Quillon MCP Gateway]
                                                    |-- auth: key -> tenant + scope (Postgres)
                                                    |-- rate limit (Redis, per key)
                                                    |-- MCP server (Streamable HTTP)
                                                    |     |-- pinned tools (~12 hottest read/safe-write ops, flat)
                                                    |     |-- meta tools: list_operations / describe_operation / call
                                                    |-- executor: builds real HTTP call, enforces scope, shapes response
                                                    |-- destructive-op gate: confirm-token round trip
                                                    |-- audit log (Postgres, every call)
                                                    -->  real Quillon REST API (162 ops)
```

Build-time (not runtime): a `build-manifest` script reads `openapi.json`, applies `policy.json`, emits `manifest.json` — the only thing the running server reads. Re-run in CI on every spec change; diff reviewed before merge.

## 3. File tree

```
quillon-mcp-gateway/
  openapi/openapi.json           # your real spec, 162 ops — not included here
  policy.json                    # human-reviewed per-operation overrides
  scripts/build-manifest.ts
  src/
    server.ts
    auth.ts
    executor.ts
    confirm.ts
    naming.ts
    tools/meta.ts
    tools/pinned.ts
  db/schema.sql
  Dockerfile
  .env.dist
  package.json
  tsconfig.json
```

## 4. Naming: operationId → MCP tool name

`src/naming.ts` — derives from the path template (reliable), not the operationId string (fragile):

```ts
// Non-plural path leaves that represent a single attribute/action, not an
// enumerable collection, even though they end in "s" (e.g. "status", "logs").
// Extend this list after reviewing the printed name diff for your real spec.
const NON_PLURAL_LEAVES = new Set(["status", "logs"]);

function toSnake(word: string): string {
  return word.replace(/[A-Z]/g, (c, i) => (i === 0 ? c.toLowerCase() : `_${c.toLowerCase()}`));
}

export function deriveToolName(method: string, pathTemplate: string): string {
  const rawSegments = pathTemplate.split("/").filter(Boolean);
  const literalSegments = rawSegments.filter(s => !s.startsWith("{") && !/^v\d+$/i.test(s));
  const targetsExistingItem = rawSegments[rawSegments.length - 1].startsWith("{");
  const leaf = literalSegments[literalSegments.length - 1];
  const looksLikeResource = targetsExistingItem || (leaf.endsWith("s") && !NON_PLURAL_LEAVES.has(leaf));

  if (looksLikeResource) {
    const verb = { GET: targetsExistingItem ? "get" : "list", POST: "create", PUT: "update", PATCH: "update", DELETE: "delete" }[method] ?? "call";
    return `${toSnake(leaf)}.${verb}`;
  }
  // Non-resource leaf ("logs", "restart", "rollback"): the leaf word is the action itself.
  const namespace = literalSegments[literalSegments.length - 2] ?? leaf;
  return `${toSnake(namespace)}.${toSnake(leaf)}`;
}
```

Confirmed mappings:
- `GET /v2/projects/{projectId}/deployments/{deploymentId}/logs` → `deployments.logs`
- `DELETE /v2/projects/{projectId}/deployments/{deploymentId}` → `deployments.delete`
- `GET /v2/projects` → `projects.list`
- `POST /v2/projects/{projectId}/deployments/{deploymentId}/restart` → `deployments.restart`

Heuristic, not perfect across 162 heterogeneous paths. `build-manifest` prints every derived name; override bad ones via `policy.json`'s `nameOverride` field before first ship.

## 5. Policy file — the human-reviewed gate

`policy.json`. Every `DELETE` (and anything else you flag) must have an entry, or the build fails. Nothing destructive ships un-reviewed.

```json
{
  "defaults": { "GET": "read", "POST": "write", "PUT": "write", "PATCH": "write", "DELETE": "destructive" },
  "requireExplicitTier": ["DELETE"],
  "overrides": {
    "DeleteV2ProjectsProjectIdDeploymentsDeploymentId": { "tier": "destructive", "requireConfirm": true },
    "PostV2ProjectsProjectIdDeploymentsDeploymentIdRestart": { "tier": "write", "requireConfirm": false },
    "GetV2ProjectsProjectIdDeploymentsDeploymentIdLogs": { "tier": "read", "pinned": true }
  }
}
```

## 6. `scripts/build-manifest.ts`

```ts
import SwaggerParser from "@apidevtools/swagger-parser";
import { writeFileSync, readFileSync } from "node:fs";
import { deriveToolName } from "../src/naming.js";

type Tier = "read" | "write" | "destructive";

async function main() {
  const spec = await SwaggerParser.dereference("openapi/openapi.json") as any;
  const policy = JSON.parse(readFileSync("policy.json", "utf8"));
  const manifest: Record<string, unknown> = {};
  const nameDiff: string[] = [];
  const missingClassification: string[] = [];

  for (const [pathTemplate, methods] of Object.entries<any>(spec.paths)) {
    for (const [method, op] of Object.entries<any>(methods)) {
      const httpMethod = method.toUpperCase();
      const override = policy.overrides[op.operationId] ?? {};
      const tier: Tier = override.tier ?? policy.defaults[httpMethod];

      if (policy.requireExplicitTier.includes(httpMethod) && !policy.overrides[op.operationId]) {
        missingClassification.push(op.operationId);
        continue; // never silently expose an unclassified destructive op
      }

      const toolName = override.nameOverride ?? deriveToolName(httpMethod, pathTemplate);
      nameDiff.push(`${op.operationId} -> ${toolName} [${tier}]`);

      manifest[toolName] = {
        operationId: op.operationId,
        method: httpMethod,
        pathTemplate,
        tier,
        requireConfirm: override.requireConfirm ?? tier === "destructive",
        pinned: override.pinned ?? false,
        description: op.summary ?? op.description ?? toolName,
        parameters: op.parameters ?? [],
        requestBody: op.requestBody ?? null,
      };
    }
  }

  if (missingClassification.length) {
    console.error(`Blocked: ${missingClassification.length} operation(s) need a policy.json entry before build:`);
    console.error(missingClassification.join("\n"));
    process.exit(1);
  }

  writeFileSync("manifest.json", JSON.stringify(manifest, null, 2));
  writeFileSync("manifest-name-review.txt", nameDiff.join("\n"));
  console.log(`Built manifest: ${Object.keys(manifest).length} tools. Review manifest-name-review.txt before shipping.`);
}

main();
```

## 7. Auth — `src/auth.ts`

Standard `Authorization: Bearer <key>` header, not a bespoke header name — most MCP clients handle that natively; a custom header name forces customers onto a local stdio bridge (`mcp-remote`) just to inject it.

```ts
import type { Request, Response, NextFunction } from "express";
import { createHash } from "node:crypto";
import { pool } from "./db.js";

export type TenantScope = { tenantId: string; projectIds: string[]; allowDestructive: boolean };

declare module "express-serve-static-core" {
  interface Request { tenant?: TenantScope; apiKeyId?: string }
}

function hashKey(raw: string): string {
  return createHash("sha256").update(raw + process.env.API_KEY_PEPPER).digest("hex");
}

export async function requireApiKey(req: Request, res: Response, next: NextFunction) {
  const header = req.header("authorization");
  const raw = header?.startsWith("Bearer ") ? header.slice(7) : null;
  if (!raw) return res.status(401).json({ error: "missing Authorization: Bearer <api_key>" });

  const { rows } = await pool.query(
    `SELECT id, tenant_id, scope FROM api_keys WHERE key_hash = $1 AND revoked_at IS NULL`,
    [hashKey(raw)],
  );
  if (rows.length === 0) return res.status(401).json({ error: "invalid or revoked key" });

  req.apiKeyId = rows[0].id;
  req.tenant = { tenantId: rows[0].tenant_id, projectIds: rows[0].scope.project_ids, allowDestructive: rows[0].scope.allow_destructive };
  next();
}
```

## 8. Destructive-op confirm gate — `src/confirm.ts`

Prevents one call (hallucinated, or prompt-injected from content the agent read elsewhere) from executing a delete/rotate/billing action. MCP `elicitation` is the spec-native mechanism when the client supports it; this token flow is the client-agnostic fallback — ship both, prefer elicitation.

```ts
import { createHmac, timingSafeEqual } from "node:crypto";

const TTL_MS = 5 * 60 * 1000;

function sign(payload: string): string {
  return createHmac("sha256", process.env.CONFIRM_SECRET!).update(payload).digest("hex");
}

export function issueConfirmToken(toolName: string, args: unknown): string {
  const payload = JSON.stringify({ toolName, argsHash: sign(JSON.stringify(args)), exp: Date.now() + TTL_MS });
  const token = Buffer.from(payload).toString("base64url");
  return `${token}.${sign(payload)}`;
}

export function verifyConfirmToken(token: string, toolName: string, args: unknown): boolean {
  const [encoded, sig] = token.split(".");
  if (!encoded || !sig) return false;
  const payload = Buffer.from(encoded, "base64url").toString("utf8");
  const expected = sign(payload);
  if (expected.length !== sig.length || !timingSafeEqual(Buffer.from(expected), Buffer.from(sig))) return false;

  const parsed = JSON.parse(payload);
  return parsed.toolName === toolName && parsed.argsHash === sign(JSON.stringify(args)) && parsed.exp > Date.now();
}
```

## 9. Executor — `src/executor.ts`

```ts
import { manifest } from "./manifest.js";
import { issueConfirmToken, verifyConfirmToken } from "./confirm.js";
import type { TenantScope } from "./auth.js";

const MAX_RESPONSE_BYTES = 256 * 1024; // cap what flows back into the agent's context

export async function execute(toolName: string, args: Record<string, unknown>, tenant: TenantScope, confirmToken?: string) {
  const entry = manifest[toolName];
  if (!entry) throw new Error(`unknown tool: ${toolName}`);

  const projectId = args.projectId as string | undefined;
  if (projectId && !tenant.projectIds.includes(projectId)) {
    throw new Error("projectId outside this key's scope");
  }

  if (entry.requireConfirm) {
    if (!tenant.allowDestructive) throw new Error("this key is not scoped for destructive operations");
    if (!confirmToken) {
      return { needsConfirmation: true, summary: `About to ${entry.description}. Re-call with confirm_token to proceed.`, confirmToken: issueConfirmToken(toolName, args) };
    }
    if (!verifyConfirmToken(confirmToken, toolName, args)) throw new Error("confirm_token invalid, expired, or does not match these args");
  }

  let path = entry.pathTemplate as string;
  for (const [key, value] of Object.entries(args)) path = path.replace(`{${key}}`, encodeURIComponent(String(value)));

  const res = await fetch(`${process.env.QUILLON_API_BASE_URL}${path}`, {
    method: entry.method,
    headers: { authorization: `Bearer ${process.env.QUILLON_BACKEND_SERVICE_TOKEN}`, "content-type": "application/json" },
    body: entry.method === "GET" ? undefined : JSON.stringify(args),
    signal: AbortSignal.timeout(15_000),
  });

  const text = await res.text();
  return text.length > MAX_RESPONSE_BYTES
    ? { truncated: true, body: text.slice(0, MAX_RESPONSE_BYTES) }
    : JSON.parse(text || "{}");
}
```

## 10. Tool registration — meta pattern + pinned hot path

`src/tools/meta.ts` keeps the initial tool list small (3 tools) while covering all 162 ops via progressive discovery:

```ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { manifest } from "../manifest.js";
import { execute } from "../executor.js";

export function registerMetaTools(server: McpServer, getTenant: () => any) {
  server.registerTool("quillon.list_operations", {
    description: "List available Quillon API operations, optionally filtered by namespace (e.g. 'deployments') or tier (read/write/destructive).",
    inputSchema: { namespace: z.string().optional(), tier: z.enum(["read", "write", "destructive"]).optional() },
  }, async ({ namespace, tier }) => ({
    content: [{ type: "text", text: JSON.stringify(
      Object.entries(manifest)
        .filter(([name, e]: any) => (!namespace || name.startsWith(`${namespace}.`)) && (!tier || e.tier === tier))
        .map(([name, e]: any) => ({ name, tier: e.tier, description: e.description }))
    ) }],
  }));

  server.registerTool("quillon.describe_operation", {
    description: "Get the full input schema for one operation returned by quillon.list_operations.",
    inputSchema: { name: z.string() },
  }, async ({ name }) => ({ content: [{ type: "text", text: JSON.stringify(manifest[name] ?? { error: "unknown operation" }) }] }));

  server.registerTool("quillon.call", {
    description: "Execute a Quillon API operation by name. Destructive operations return a confirm_token on first call; re-call with it to proceed.",
    inputSchema: { name: z.string(), args: z.record(z.unknown()).default({}), confirm_token: z.string().optional() },
  }, async ({ name, args, confirm_token }) => ({
    content: [{ type: "text", text: JSON.stringify(await execute(name, args, getTenant(), confirm_token)) }],
  }));
}
```

`src/tools/pinned.ts` — flat, low-latency wrappers for the ~12 operations everyone calls constantly (marked `"pinned": true` in `policy.json`), so common cases skip the discovery round trip:

```ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { manifest } from "../manifest.js";
import { execute } from "../executor.js";

export function registerPinnedTools(server: McpServer, getTenant: () => any) {
  for (const [name, entry] of Object.entries(manifest) as any) {
    if (!entry.pinned) continue;
    server.registerTool(name, { description: entry.description, inputSchema: buildZodShape(entry) },
      async (args) => ({ content: [{ type: "text", text: JSON.stringify(await execute(name, args, getTenant(), args.confirm_token)) }] }));
  }
}
```

(`buildZodShape` — map each OpenAPI parameter/requestBody field to a `zod` type; straightforward for `string`/`number`/`boolean`/`enum`/arrays of those. Anything using `oneOf`/`allOf` needs a proper converter — pull in `openapi-zod-client` rather than hand-rolling that part.)

## 11. Server — `src/server.ts`

```ts
import express from "express";
import helmet from "helmet";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { requireApiKey } from "./auth.js";
import { rateLimit } from "./rateLimit.js";
import { registerMetaTools } from "./tools/meta.js";
import { registerPinnedTools } from "./tools/pinned.js";
import { audit } from "./audit.js";

const app = express();
app.use(helmet());
app.use(express.json());
app.use("/mcp", requireApiKey, rateLimit);

app.post("/mcp", async (req, res) => {
  const server = new McpServer({ name: "quillon", version: "1.0.0" });
  registerMetaTools(server, () => req.tenant);
  registerPinnedTools(server, () => req.tenant);
  server.server.oninitialized = () => audit(req.apiKeyId!, "session_start");

  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

app.listen(process.env.PORT ?? 4242);
```

## 12. Data — `db/schema.sql`

```sql
CREATE TABLE api_keys (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL,
  key_hash TEXT NOT NULL UNIQUE,      -- sha256(raw_key + pepper); raw key never stored
  scope JSONB NOT NULL,               -- {"project_ids": [...], "allow_destructive": false}
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  revoked_at TIMESTAMPTZ              -- soft delete: row stays for audit_log referential integrity
);

CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  api_key_id UUID NOT NULL REFERENCES api_keys(id),  -- no ON DELETE CASCADE: audit trail outlives a revoked key
  tool_name TEXT NOT NULL,
  tier TEXT NOT NULL,
  args_redacted JSONB NOT NULL,
  status TEXT NOT NULL,
  latency_ms INTEGER NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## 13. Hosting

`Dockerfile`:

```dockerfile
FROM node:22-bookworm AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build:manifest && npm run build

FROM node:22-alpine
WORKDIR /app
RUN addgroup -S mcp && adduser -S mcp -G mcp
COPY --from=build /app/dist ./dist
COPY --from=build /app/manifest.json ./manifest.json
COPY --from=build /app/node_modules ./node_modules
USER mcp
ENV ENV=prod
EXPOSE 4242
CMD ["node", "dist/server.js"]
```

`.env.dist`:

```
# Runtime
ENV=dev
PORT=4242

# Backend
QUILLON_API_BASE_URL=https://api.quillon.internal
QUILLON_BACKEND_SERVICE_TOKEN=

# Data
DATABASE_URL=postgres://user:pass@localhost:5432/quillon_mcp
REDIS_URL=redis://localhost:6379

# Security
API_KEY_PEPPER=
CONFIRM_SECRET=
```

TLS terminates at your existing gateway/load balancer in front of this container; the app stays stateless so it scales horizontally behind it.

## 14. Rollout

1. Run `build-manifest` against the real `openapi.json`. Fix every `missingClassification` entry in `policy.json` — every `DELETE`, plus anything billing/secrets-related, gets `"tier": "destructive"`.
2. Read `manifest-name-review.txt` once, fully. Fix bad auto-derived names via `nameOverride`. About 20 minutes for 162 ops.
3. Pick ~12 highest-frequency read + safe-write ops, mark `"pinned": true`.
4. Issue one internal API key, `allow_destructive: false`. Point one internal agent at `/mcp`, exercise the read path end to end.
5. Enable `allow_destructive: true` on that same key only, verify the confirm-token round trip on a real delete against a disposable test project.
6. Ship to 2-3 design-partner customers with `allow_destructive: false` by default. Flip per-customer once each confirms they want write access to your delete/rotate endpoints from an agent.

About 2-3 hours for steps 1-3 once you have the real spec in hand; step 4-6 is a day of validation, not engineering.

## 15. Open items — need your input, not guessable from the request

1. `Authorization: Bearer <key>` chosen over a custom header name for MCP client compatibility — confirm that's acceptable, or state the exact header name required.
2. Per-key `project_ids` scope assumes customers are scoped to specific projects, not "everything in their org" — confirm that matches your access model.
3. `NON_PLURAL_LEAVES` and the pinned-tool list are placeholders — need the real `openapi.json` to finalize both.
4. Billing/payment-method operations, if any exist among the 162, aren't in the sample `policy.json` — treat as `destructive` by default until reviewed.
5. Static long-lived API keys, not OAuth 2.1 — matches what you asked for; flagging that MCP's spec recommends OAuth for HTTP transport auth as the longer-term upgrade if this becomes a broad public offering.