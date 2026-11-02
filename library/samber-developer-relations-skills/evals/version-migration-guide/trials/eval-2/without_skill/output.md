# Upgrading to tarn-sdk 5.0

## Before you start: get onto 4.7 or 4.8 first

If you're running **4.6**, upgrade to **4.7** before you do anything else, independent of your 5.0 plans. 4.6 has a connection-pool leak that 4.7 fixes; 5.0 does not carry that fix backward, and if you roll back from a 5.0 migration attempt, you want to land on 4.7 or 4.8, not back on a leaking 4.6.

We're also shipping **4.8**, a bridge release on the 4.x line, before we freeze that branch. 4.8 adds a runtime deprecation warning for every API that 5.0 changes or removes — same behavior as 4.7, but it tells you at startup and on first use exactly which calls in your codebase need to change. Run your app on 4.8 for a few days, clear the warnings one at a time, and the jump to 5.0 becomes a version bump instead of a rewrite.

Recommended path:

```
4.6 → 4.7 (mandatory: pool leak fix)
4.7 → 4.8 (recommended: surfaces every 5.0 breaking change as a warning)
4.8 → 5.0 (breaking changes below)
```

Skipping straight from 4.6 to 5.0 works, but you'll be debugging two unrelated things at once — a runtime pool bug and eleven API changes — with no way to tell which one caused a given symptom.

### Branch status after 4.8

4.8 is the last feature release on 4.x. After it ships, the 4.x branch is frozen: no new features, no further deprecation passes. We'll backport critical security fixes to 4.x for 90 days after the 4.8 release date; after that window, 4.x is end of life. If you need to stay on 4.x past that point, pin to 4.8 and track our security advisories directly.

## Requirements

5.0 requires:

- **Node.js 22.11.0 or newer** (22.11.0 is the first Node 22 LTS build; earlier 22.x releases aren't supported)
- **TypeScript 5.7 or newer**, if you consume the package's types

Check before upgrading:

```bash
node --version   # must be >= 22.11.0
npx tsc --version  # must be >= 5.7.0
```

Neither of these is negotiable at runtime: 5.0 uses Node APIs introduced in 22.11 (notably in the pool's disposal path) and TypeScript syntax that 5.7 added. Older versions will fail to install peer checks or fail to typecheck, not silently degrade.

## Breaking changes

### 1. Node 22.11+ required

**Before:** tarn-sdk 4.x supported Node 18.x, 20.x, and 22.x.

**After:** Node 22.11.0 is the floor. `package.json#engines` enforces this; `npm install` warns, and the client throws on construction if `process.version` is below 22.11.0.

**Migration:** Upgrade your runtime before upgrading the package. There's no code change here, only an infrastructure one — check your CI images, Dockerfiles, and Lambda/Cloud Run runtime configs.

### 2. TypeScript 5.7+ required

**Before:** Types were written to be compatible back to TypeScript 4.9.

**After:** The type definitions use TS 5.7 features (namely improved inference for the branded ID types described in change 11). Compiling against an older TypeScript will produce type errors that don't reflect real bugs in your code.

**Migration:** `npm install -D typescript@^5.7`. If you're on a monorepo with a shared TypeScript version, coordinate that bump separately — it's likely to affect other packages too.

### 3. ESM only — no more `require()`

**Before:** The package shipped both CommonJS and ESM builds.

**After:** tarn-sdk 5.0 ships ESM only.

```js
// Before (still works in 4.x)
const { TarnClient } = require("tarn-sdk");

// After (5.0)
import { TarnClient } from "tarn-sdk";
```

**Migration:** If your project is still CommonJS, either convert it to ESM (`"type": "module"` in `package.json`) or use a dynamic `import()` inside your CommonJS entry point. There is no CJS build of 5.0 to fall back to.

### 4. Client constructor takes one options object

**Before:** Positional arguments, with an implicit ordering that was easy to get wrong.

```ts
// Before
const client = new TarnClient("https://api.tarnwell.io", "sk_live_...", 30000);
```

**After:**

```ts
// After
const client = new TarnClient({
  endpoint: "https://api.tarnwell.io",
  apiKey: "sk_live_...",
  timeoutMs: 30000,
});
```

**Migration:** Every call site that constructs a `TarnClient` needs updating. This is mechanical — wrap the existing positional arguments in an object with the field names `endpoint`, `apiKey`, `timeoutMs` (in that order, matching the old positional order).

### 5. Connection pool: explicit disposal, renamed options

The 4.6 leak came from the pool relying on garbage collection and a `process.on('exit')` hook to release connections — fine until a process was killed rather than exited, or a client went out of scope without being explicitly closed. 4.7 patched the immediate leak; 5.0 removes the implicit cleanup path entirely and requires explicit disposal.

**Before:**

```ts
const client = new TarnClient({ endpoint, apiKey, poolSize: 10, poolIdleMs: 5000 });
// ... use client ...
// no explicit close required; pool cleaned up on process exit
```

**After:**

```ts
const client = new TarnClient({
  endpoint,
  apiKey,
  pool: { maxConnections: 10, idleTimeoutMs: 5000 },
});
try {
  // ... use client ...
} finally {
  await client.close();
}

// or, with Node 22's explicit resource management:
await using client = new TarnClient({ endpoint, apiKey });
// client.close() runs automatically at scope exit
```

**Migration:**
- Rename `poolSize` → `pool.maxConnections`, `poolIdleMs` → `pool.idleTimeoutMs`.
- Add an explicit `client.close()` (or `await using`) everywhere a client is created. Omitting it isn't a silent leak anymore — connections that are never closed now hit a configurable `pool.maxLifetimeMs` cap and get force-closed with a logged warning, but you should close deliberately rather than rely on that backstop.

### 6. Callback-style methods removed

4.x kept callback signatures around for compatibility with pre-Promise code. 5.0 drops them, along with two long-deprecated v3-era methods.

**Removed:**
- `client.query(sql, callback)` → use `await client.query(sql)`
- `client.queryLegacy()` → use `client.query()`
- `client.rawQuery()` → use `client.query(sql, { raw: true })`

**Migration:** Search your codebase for `.query(` calls that pass a function as the last argument, and for any remaining `queryLegacy`/`rawQuery` calls (4.8's deprecation warnings will list every call site if you upgrade there first).

### 7. Streaming: `EventEmitter` → async iterators

**Before:**

```ts
const stream = client.stream("SELECT * FROM events");
stream.on("data", (row) => process(row));
stream.on("end", () => done());
stream.on("error", (err) => handleError(err));
```

**After:**

```ts
try {
  for await (const row of client.stream("SELECT * FROM events")) {
    process(row);
  }
} catch (err) {
  handleError(err);
}
```

**Migration:** Any `.stream()` consumer needs rewriting to `for await`. This is the change most likely to touch business logic rather than boilerplate, since error handling and backpressure now flow through the loop instead of separate listeners — budget real review time for this one, not just a find-and-replace.

### 8. Consolidated error hierarchy

**Before:** `ConnectionError`, `QueryError`, `AuthError`, `PoolExhaustedError`, and others as separate exported classes, each with a different shape.

**After:** A single `TarnError` class with a `code` field you switch on.

```ts
// Before
try {
  await client.query(sql);
} catch (err) {
  if (err instanceof AuthError) { /* ... */ }
  if (err instanceof PoolExhaustedError) { /* ... */ }
}

// After
try {
  await client.query(sql);
} catch (err) {
  if (err instanceof TarnError) {
    switch (err.code) {
      case "AUTH_FAILED": /* ... */ break;
      case "POOL_EXHAUSTED": /* ... */ break;
    }
  }
}
```

**Migration:** Replace `instanceof <SpecificError>` checks with `err.code === "..."`. The full list of `code` values and their old class-name equivalents is in the API reference under `TarnError`.

### 9. Retry and backoff: new nested config, new default

**Before:** No retries by default. Retry count set via a top-level `maxRetries` option.

**After:** Retries are on by default (3 attempts, exponential backoff with jitter), configured under a `retry` object.

```ts
// Before
const client = new TarnClient({ endpoint, apiKey, maxRetries: 5 });

// After
const client = new TarnClient({
  endpoint,
  apiKey,
  retry: { maxAttempts: 5, backoff: "exponential" },
});

// to fully disable retries (restore 4.x default behavior)
const client = new TarnClient({ endpoint, apiKey, retry: { maxAttempts: 0 } });
```

**Migration:** If your application already implements its own retry logic around tarn-sdk calls, set `retry: { maxAttempts: 0 }` explicitly, or you'll get retries at both layers. This is the one change in this list that alters behavior even if you touch no code — audit for double-retry before you deploy, not after.

### 10. Package exports restructured

**Before:** A default export, plus deep imports like `tarn-sdk/dist/internal/pool` worked because nothing enforced `exports` in `package.json`.

**After:** Named exports only, plus explicit subpath exports for supported entry points.

```ts
// Before
import TarnClient from "tarn-sdk";
import { MockPool } from "tarn-sdk/dist/internal/pool";

// After
import { TarnClient } from "tarn-sdk";
import { MockPool } from "tarn-sdk/testing";
```

**Migration:** Change default imports to named imports. If you have any deep import from `tarn-sdk/dist/...` or `tarn-sdk/src/...`, it will fail to resolve — those paths were never part of the public API, and `package.json#exports` now blocks them. Check `tarn-sdk/testing` for the supported replacement before assuming something is gone entirely.

### 11. Branded ID types and `TarnTimestamp`

**Before:** IDs were plain `string`; timestamps were `Date`, which loses sub-millisecond precision that the API can return.

**After:** IDs are branded types (`DatasetId`, `UserId`) that aren't structurally compatible with plain `string`; timestamps are `TarnTimestamp`, a thin wrapper around `bigint` nanoseconds.

```ts
// Before
function loadDataset(id: string): Promise<Dataset> { /* ... */ }
const createdAt: Date = dataset.createdAt;

// After
function loadDataset(id: DatasetId): Promise<Dataset> { /* ... */ }
const createdAt: TarnTimestamp = dataset.createdAt;

// converting a raw string you got from elsewhere (e.g., a URL param)
const id = asDatasetId(rawIdFromRequest);

// converting TarnTimestamp for display
const jsDate: Date = createdAt.toDate(); // truncates to millisecond precision
```

**Migration:** This is a compile-time-only change — there's no runtime behavior difference for existing valid IDs. Fix it by running `tsc` and working through the errors: wrap raw strings from outside the SDK (URL params, form input, database rows) with the `asDatasetId`/`asUserId` helpers, and replace direct `Date` usage of timestamp fields with `.toDate()` where you need a `Date`. Prefer keeping values as `TarnTimestamp` end-to-end if you're doing anything precision-sensitive — that's the reason the type exists.

## Rollback

If something goes wrong mid-migration, roll back to **4.8**, not 4.6. 4.8 has the pool-leak fix and the same deprecation warnings you were just working through, so you keep your progress and stay off the known-leaking version while you sort out the issue.

## Compatibility matrix

| Your version | Pool leak fixed | 5.0 deprecation warnings | Node.js | TypeScript |
|---|---|---|---|---|
| 4.6 | No | No | 16+ | 4.9+ |
| 4.7 | Yes | No | 16+ | 4.9+ |
| 4.8 | Yes | Yes | 16+ | 4.9+ |
| 5.0 | Yes (pool redesigned) | n/a | **22.11+** | **5.7+** |

## Getting help

Run on 4.8 first and clear its deprecation warnings — that alone resolves most of the mechanical parts of changes 1–6, 8, and 10 before you touch 5.0. For change 7 (streaming) and change 9 (retry defaults), budget dedicated review time; both can change runtime behavior, not just call syntax. Open an issue on the repo with your 4.8 deprecation warning output if you hit a migration case this guide doesn't cover.