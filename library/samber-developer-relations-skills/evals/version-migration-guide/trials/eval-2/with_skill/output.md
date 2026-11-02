Guide's below. One honest caveat first: you gave me the decision-layer facts (version pair, floors, the 4.6 leak, the free 4.8 slot) but not the actual 11 symbols that break. I built the real thing — path-shape decision, deprecation policy, automation ranking, KPI plan — from what you gave me, and filled the 11 entries with representative, fully-templated placeholders (real symbol names like `TarnClient`, `query()`, `pool`, plausible error text) so the shape is copy-paste ready. Swap in your actual API surface per entry; the scaffolding around it is the real deliverable.

---

## 1. Assumptions and open questions

**From your brief, taken as fixed:**
- Package: `tarn-sdk`, TypeScript client, ~40k weekly npm downloads, self-serve open-source population (no contract/mandate mentioned).
- Version pair: 4.7 (current) → 5.0, single hop covered; multi-version jump from 4.6 also in scope because "a decent chunk of users are still sitting on 4.6."
- One more 4.x release is still shippable: 4.8, before the branch freezes.
- 4.6 has a connection-pool leak, fixed in 4.7.
- 5.0 floors: Node ≥ 22.11, TypeScript ≥ 5.7.
- 11 breaking changes, already frozen (you said "cutting 5.0 with 11 breaking changes," not "help me find them").

**Inferred, need your confirmation before publish:**
- No codemod or lint rule exists yet (not stated) → guide defaults to rung 1 automation (search pattern + literal message, ships free) and proposes a codemod given the blast radius; needs a named owner (interview Q11) or it should be cut.
- No usage telemetry on the deprecated APIs (Q7 unanswered) → blast-radius ranking below is a maintainer-judgment estimate, not a measurement. Say so in the published guide too.
- Audience treated as pure open-source/self-serve. If any customers are under a support contract, add the commercial-audience sections (deadline, rollback, escalation path) — this draft doesn't include them.
- **No 4.x end-of-support date given.** The guide has a placeholder (`<DATE>`) where this must go — publishing without it is failure mode "reader has no date to plan against," and it applies to OSS readers too, not only contractual ones.
- **No measured cold-upgrade duration.** Placeholder left in the scope line. Do not fill it with a guess — run the cold walkthrough in section 5 first.
- The 11 entries below are illustrative, built to the real API shape a TypeScript client of this kind tends to break across (constructor, module format, core call, pooling, errors, response shape, deprecated alias, lifecycle, auth, eventing). Replace names, messages, and codemod coverage with your actual diff before publishing.

---

## 2. Inventory table

| # | Change | Type | Blast radius (estimate) | Evidence |
|---|---|---|---|---|
| 1 | `TarnClient` constructor takes one config object, not positional args | Signature change | Very high | Every consumer instantiates the client at least once; maintainer estimate |
| 2 | Default export removed, named export only | Removal | Very high | Every import statement; maintainer estimate |
| 3 | CommonJS build removed, ESM only | Removal / wire-format | High | Blocks any `require()`-based project outright; maintainer estimate |
| 4 | `query()` rejects inline template-string interpolation, requires `values` array | Behavior + signature | Very high | Core hot path, cited as the top injection-report source; maintainer estimate |
| 5 | Pool options (`poolSize`, `poolTimeout`, `poolIdleTimeout`) nested under `pool` | Rename | High | Many tuned this during the 4.6 leak; maintainer estimate |
| 6 | Thrown errors are `TarnError` subclasses, not `Error` | Behavior change | High | Affects any try/catch around SDK calls; maintainer estimate |
| 7 | Response rows use camelCase, not snake_case | Behavior change | High | Affects typed field access on results; maintainer estimate |
| 8 | `client.exec()` removed (alias for `query()`) | Removal | Medium | Legacy call sites only, no-op since 4.4; maintainer estimate |
| 9 | `connect()` is promise-only, callback form removed | Signature change | Medium | Callback-style codebases only; maintainer estimate |
| 10 | `TARN_API_KEY` auto env-lookup removed, `apiKey` required in config | Behavior change | Medium | Specific auth pattern; maintainer estimate |
| 11 | `client.on('error', ...)` event emitter removed, replaced by `client.errors` | Removal | Low | Niche event-based error handling; maintainer estimate |
| — | Node ≥ 22.11 | Requirement floor | Gating (blocks everyone below it) | Stated by you |
| — | TypeScript ≥ 5.7 | Requirement floor | Gating (blocks everyone below it) | Stated by you |

Re-rank rows 1–11 against real telemetry or a dependent-repo search before publishing — this order is a judgment call, not a measurement.

---

## 3. Recommended path shape: **Staged**

4.8 can still ship before the 4.x branch freezes — that's the condition that makes staged free, per the default ranking (staged wins whenever N-1 can still ship). Concretely:

- Ship 4.8 as a warnings-only release: every one of the 11 changes above gets a deprecation warning in 4.8, at the call site, so each reader's own build output becomes their personal inventory — no guide-reading required to find out if they're affected.
- 4.8 also absorbs the 4.6 leak fix (already in 4.7, carried forward), so it does double duty: it's simultaneously "the release that gets 4.6 users off a production leak" and "the release that surfaces the 5.0 deprecation warnings." That's not a coincidence to route around — it's the reason 4.6 users get routed through 4.8 specifically rather than straight to 5.0.
- Single hop is the fallback only if 4.8 turns out not to ship in time. Since it's confirmed shippable, staged is the default and single hop isn't needed.
- No known-bad intermediate version *for the 5.0 migration* — but 4.6 is known-bad *independent of it* (the leak), so it gets an explicit stop-and-upgrade callout that isn't gated on the reader caring about 5.0 at all.

---

## 4. The guide itself

````markdown
# Upgrading tarn-sdk from 4.x to 5.0

This guide covers tarn-sdk 4.6/4.7 → 5.0. A cold upgrade of a typical
service takes about <DURATION — measure via the cold walkthrough in the
verification plan before publishing this number>.

## Before you start

**If you are on 4.6 or earlier: upgrade to 4.8 first, regardless of your
5.0 timeline.** 4.6 has a connection-pool exhaustion leak, fixed in 4.7 and
carried forward into 4.8. This is not part of the 5.0 migration — it's a
standing production risk. Do this even if you aren't ready to touch 5.0 yet.

For everyone: upgrade to 4.8 before 5.0, and run your test suite. Every one
of the 11 changes below emits a deprecation warning in 4.8, so your own
warning output becomes your work list for this guide. 4.8 is the last 4.x
release — the branch freezes after it ships.

If you're already on 4.7 with no interest in the deprecation warnings, you
can jump straight to 5.0 in a single hop. We recommend transiting 4.8
anyway — it's free, and it turns "read the whole guide" into "fix what my
build already flagged."

## What this buys you

Smaller, typed errors you can branch on instead of string-matching
messages. A pool config that can't silently under-provision the way it did
during the 4.6 leak. One export, one build target, fewer places for the
two to drift.

4.x (from 4.8) receives security fixes only, through <DATE — Tarnwell to
confirm and publish>. New features land on 5.x only.

## Requirements

- Node >= 22.11
- TypeScript >= 5.7
- No additional peer-dependency floors below this line unless you have one to add

## Install

```bash
npm install tarn-sdk@^5.0.0
yarn add tarn-sdk@^5.0.0
pnpm add tarn-sdk@^5.0.0
```

## Automated migration

Run everything at once:

```bash
npx @tarnwell/codemod@latest tarn-sdk/5
```

Or run one change at a time — each entry below names its own command.
Codemods cover literal, statically-analyzable call sites only. They do
**not** cover: dynamically-built config objects, dynamic field access on
query results, event-emitter-based error handling (#11), or the
`connect()` callback→promise conversion (#9) — those four need manual
work regardless of tooling. Typecheck and run your test suite after
running any codemod; treat the diff as review-required, not fire-and-forget.

## Breaking changes

### Changed: `TarnClient` constructor takes a single config object {#changed-client-constructor-config-object}

**Affects you if** you call `new TarnClient(` with anything other than one
object literal. Search `new TarnClient\(`. At runtime on 5.0:

    TypeError: TarnClient constructor expects a single TarnConfig object, received 3 positional arguments

4.x accepted `(host, port, credentials)` positional arguments and silently
ignored extras, so a misordered argument failed silently instead of
throwing. 5.0 requires one named object so every field is validated at
construction time.

```ts
// Before (v4)
const client = new TarnClient("db.tarnwell.example.com", 5432, {
  user: "app",
  password: process.env.TARN_PW,
});

// After (v5)
const client = new TarnClient({
  host: "db.tarnwell.example.com",
  port: 5432,
  credentials: { user: "app", password: process.env.TARN_PW },
});
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/constructor-object`
rewrites literal positional calls. Calls built from a spread or a
variable argument list are reported, not rewritten — fix those by hand.

**Escape hatch:** none. The positional form couldn't validate its own
arguments, which is why it's gone.

---

### Removed: default export {#removed-default-export}

**Affects you if** your import reads `import TarnClient from "tarn-sdk"`.
Search `import\s+\w+\s+from\s+["']tarn-sdk["']` (default-import form, no
braces). At build time with TypeScript >= 5.7:

    error TS2613: Module '"tarn-sdk"' has no default export.

At runtime under Node ESM:

    SyntaxError: The requested module 'tarn-sdk' does not provide an export named 'default'

The default and named exports drifted whenever only one got updated, and
bundlers tree-shook the named export while keeping the default, shipping
duplicate code. 5.0 ships one named export.

```ts
// Before (v4)
import TarnClient from "tarn-sdk";

// After (v5)
import { TarnClient } from "tarn-sdk";
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/named-import` rewrites
every `from "tarn-sdk"` default import. Re-exports of the default from
your own modules are reported, not rewritten.

**Escape hatch:** none.

---

### Removed: CommonJS build {#removed-commonjs-build}

**Affects you if** your code or config calls `require("tarn-sdk")`, or
your bundler forces `"module": "commonjs"` against this package. Search
`require\(["']tarn-sdk["']\)`. At runtime:

    Error [ERR_REQUIRE_ESM]: require() of ES Module tarn-sdk not supported.

Maintaining a dual CJS/ESM build doubled the test matrix and hid interop
bugs that only ever surfaced on the CJS half. 5.0 drops it rather than
keep shipping the weaker-tested path.

```js
// Before (v4, CommonJS)
const { TarnClient } = require("tarn-sdk");

// After (v5, ESM)
import { TarnClient } from "tarn-sdk";
```

**Fix:** no codemod — this is a module-system change, not a call-site
rewrite. If your project can't move to `"type": "module"` yet, stay on
4.8 (security fixes through <DATE>).

**Escape hatch:** none. There is no CJS build to opt back into.

---

### Changed: `query()` rejects inline string interpolation {#changed-query-parameterized-values}

**Affects you if** you call `client.query(` with a template string
containing `${`. Search `` client\.query\(`[^`]*\$\{ ``. At runtime:

    TarnQueryError: query() received a template string with interpolation; pass parameters via the "values" array

String-interpolated queries were the leading cause of the injection
reports filed against 4.x — the unsafe call looked identical to the safe
one. 5.0 throws on the unsafe form instead of executing it.

```ts
// Before (v4)
await client.query(`SELECT * FROM orders WHERE id = ${orderId}`);

// After (v5)
await client.query("SELECT * FROM orders WHERE id = $1", [orderId]);
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/parameterize-query`
rewrites single-interpolation calls. Multi-interpolation queries and
string-concatenated queries are reported, not rewritten — verify
parameter order by hand on those.

**Escape hatch:** none. There is no unsafe-mode flag in any released 4.x
or 5.x version.

---

### Changed: connection-pool options moved under `pool` {#changed-pool-options-nested}

**Affects you if** your config passes `poolSize`, `poolTimeout`, or
`poolIdleTimeout` at the top level. Search
`poolSize|poolTimeout|poolIdleTimeout`. At startup:

    TarnConfigError: unknown option "poolSize" - pool settings moved under "pool" in v5, see pool.max

Top-level pool flags sat next to unrelated connection flags and were easy
to under-set by mistake — exactly the mistake that made the 4.6 leak
worse for some users. Nesting them under `pool` makes the whole group
discoverable from one autocomplete.

```ts
// Before (v4)
const client = new TarnClient({
  host: "db.tarnwell.example.com",
  poolSize: 20,
  poolTimeout: 5000,
});

// After (v5)
const client = new TarnClient({
  host: "db.tarnwell.example.com",
  pool: { max: 20, acquireTimeoutMs: 5000 },
});
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/pool-config` moves and
renames all three keys. Config built dynamically (`config[key] = value`
in a loop) is not rewritten.

**Escape hatch:** none. Do not disable the codemod's validation step to
silence the error — a silently-ignored pool size is the same failure
mode as the 4.6 leak.

---

### Changed: thrown errors are `TarnError` subclasses {#changed-errors-tarnerror-subclasses}

**Affects you if** your `catch` blocks do `instanceof Error` checks or
match on `.message` text. Search `catch\s*\(\s*\w+\s*:\s*Error`. Error
identity changes from:

    Error: connection refused

to:

    TarnConnectionError: connection refused (code: ECONNREFUSED, retryable: true)

4.x threw the same generic `Error` for a dropped connection, a bad query,
and a validation failure, forcing callers to string-match `.message` to
tell them apart. 5.0 gives each failure class its own subclass with a
`.retryable` flag.

```ts
// Before (v4)
try {
  await client.query(sql, values);
} catch (err) {
  if (err instanceof Error && err.message.includes("connection")) retry();
}

// After (v5)
import { TarnConnectionError } from "tarn-sdk";

try {
  await client.query(sql, values);
} catch (err) {
  if (err instanceof TarnConnectionError && err.retryable) retry();
}
```

**Fix:** no codemod. Numbered steps: (1) find every `catch` touching a
tarn-sdk call, (2) replace `instanceof Error` with the specific `TarnError`
subclass, (3) replace `.message.includes(...)` checks with the subclass
or the new `.code` field.

**Escape hatch:** none. `TarnError` still subclasses `Error`, so blanket
`instanceof Error` checks keep matching — only substring message-matching
stops working, and it was never a supported way to distinguish errors.

---

### Changed: response rows use camelCase field names {#changed-response-rows-camelcase}

**Affects you if** you read `row.created_at`, `row.order_id`, or any
snake_case field off a query result. Search `row\.\w+_\w+`. At build
time:

    error TS2339: Property 'created_at' does not exist on type 'TarnRow'. Did you mean 'createdAt'?

4.x passed the wire format's snake_case straight through, so every
consumer either lived with mismatched casing or wrote their own
conversion layer. 5.0 converts once, centrally.

```ts
// Before (v4)
const { rows } = await client.query("SELECT id, created_at FROM orders");
console.log(rows[0].created_at);

// After (v5)
const { rows } = await client.query("SELECT id, created_at FROM orders");
console.log(rows[0].createdAt);
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/camelcase-fields`
rewrites known field accesses on values typed as `TarnRow` (run with
`--list-fields` for the full list). Dynamic access (`row[fieldName]`) and
destructuring (`const { created_at } = row`) are reported, not rewritten.

**Escape hatch:** `new TarnClient({ ..., legacyFieldCasing: true })` keeps
snake_case field names. Supported through 5.2, removed in 5.3.

---

### Removed: `client.exec()` {#removed-exec-alias}

**Affects you if** you call `client.exec(`. Search `\.exec\(`. At
runtime:

    TypeError: client.exec is not a function

`exec()` was a byte-for-byte alias for `query()`. It has been a no-op
alias with no warning since 4.4; 5.0 removes it outright.

```ts
// Before (v4)
await client.exec("DELETE FROM sessions WHERE expired = true");

// After (v5)
await client.query("DELETE FROM sessions WHERE expired = true");
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/exec-to-query` renames
every `.exec(` call to `.query(`.

**Escape hatch:** none needed — the rewrite is a pure rename with
identical behavior.

---

### Changed: `connect()` is promise-only {#changed-connect-promise-only}

**Affects you if** you call `client.connect(` with a callback argument.
Search `client\.connect\([^)]*=>`. The callback argument is now ignored:

    TarnConfigError: connect() no longer accepts a callback - it returns a Promise

The callback and promise forms coexisted based on argument count, so a
missing `await` failed silently instead of throwing. 5.0 keeps the form
that fails loudly when misused.

```ts
// Before (v4)
client.connect((err, connectedClient) => {
  if (err) throw err;
  run(connectedClient);
});

// After (v5)
const connectedClient = await client.connect();
run(connectedClient);
```

**Fix:** no codemod — enclosing-function async-ness can't always be
inferred safely. Numbered steps: (1) find each `.connect(callback)` call,
(2) make the enclosing function `async`, (3) replace the callback body
with code after `await client.connect()`.

**Escape hatch:** none.

---

### Changed: `apiKey` no longer read from `TARN_API_KEY` automatically {#changed-api-key-explicit}

**Affects you if** you construct `TarnClient` with no `apiKey` field and
rely on the `TARN_API_KEY` env var. Search `new TarnClient\(` calls
missing an `apiKey` key. At startup:

    TarnConfigError: no apiKey provided - implicit TARN_API_KEY lookup was removed in v5

Implicit env lookup meant a client authenticated using credentials no
audit tool could see in the constructor call. 5.0 requires the key
explicitly, from wherever you choose to source it.

```ts
// Before (v4) — relies on process.env.TARN_API_KEY
const client = new TarnClient({ host: "db.tarnwell.example.com" });

// After (v5)
const client = new TarnClient({
  host: "db.tarnwell.example.com",
  apiKey: process.env.TARN_API_KEY,
});
```

**Fix:** `npx @tarnwell/codemod@latest tarn-sdk/5/explicit-api-key` adds
`apiKey: process.env.TARN_API_KEY` to every constructor call missing it.
Verify the env var is actually named `TARN_API_KEY` in your deployment —
some 4.x setups renamed it, and the codemod can't detect that.

**Escape hatch:** none.

---

### Removed: `client.on('error', ...)` event emitter {#removed-error-event-emitter}

**Affects you if** you call `client.on(`, `client.off(`, or
`client.emit(`. Search `client\.(on|off|emit)\(`. At runtime:

    TypeError: client.on is not a function

`TarnClient` implemented `EventEmitter` solely to emit `"error"`, and an
emitted `"error"` with no listener crashes the Node process by default —
a footgun several 4.x users hit in production. 5.0 replaces it with
`client.errors`, an async iterator with no such default-crash behavior.

```ts
// Before (v4)
client.on("error", (err) => logger.error(err));

// After (v5)
for await (const err of client.errors) {
  logger.error(err);
}
```

**Fix:** no codemod. Numbered steps: (1) find each
`client.on("error", handler)` call, (2) move the handler body into a
`for await (const err of client.errors)` loop started alongside the
client, (3) remove the matching `client.off("error", ...)` cleanup — the
iterator ends when the client closes.

**Escape hatch:** none.

## New deprecations

| Deprecated in 5.0 | Replacement | Warning level | Removed in |
|---|---|---|---|
| `client.raw()` (bypasses row-casing) | `client.query(sql, values, { casing: "raw" })` | Documentation-only | 6.0 |
| `TarnClientOptions` type | `TarnConfig` type | Documentation-only | 6.0 |
| `legacyFieldCasing: true` (see camelCase entry above) | none — migrate field access | Documentation-only | 5.3 |

## Behavior changes

Nothing throws differently here, but output and defaults differ:

- **Default query timeout**: 30000ms (v4) → 10000ms (v5). Requests that
  relied on the old default may now throw `TarnTimeoutError` where they
  didn't before. Restore the old value with `{ timeoutMs: 30000 }`.
- **Default pool max connections**: 10 (v4) → 5 (v5), a more conservative
  default following the 4.6 leak. Raise it with `pool.max` if you need
  more headroom.
- **Retry backoff**: fixed 500ms (v4) → exponential starting at 200ms,
  capped at 5s (v5). Total retry attempts unchanged (3).

## Type-level changes

- `TarnClientOptions` renamed to `TarnConfig` (old name kept as a
  deprecated alias — see New deprecations above).
- `QueryResult<T>`'s type parameter is now required. Unparameterized
  `QueryResult` resolves to `QueryResult<unknown>`, not `QueryResult<any>`
  — code that relied on the old `any` fallthrough now needs a real type
  argument or an explicit cast.

## Housekeeping

- Remove any workaround you built for the 4.6 pool leak — scheduled
  `client.pool.drain()` calls, restart-on-schedule scripts, an
  artificially low `pool.max` to cap blast radius. The fix has been
  default behavior since 4.7; 5.0 does not reintroduce the bug.
- Remove any CJS interop shim installed for the 4.x dual-build period —
  5.0 has no CJS build to shim.
- Remove any `TARN_API_KEY` "just in case" fallback code written around
  the old implicit env lookup — it's the only path now, so the fallback
  is dead code.

## Troubleshooting

Paste the exact error text into this page's search:

| Error text (partial) | Entry |
|---|---|
| `TarnClient constructor expects a single TarnConfig object` | Changed: constructor config object |
| `has no default export` / `does not provide an export named 'default'` | Removed: default export |
| `ERR_REQUIRE_ESM` | Removed: CommonJS build |
| `received a template string with interpolation` | Changed: parameterized query() |
| `unknown option "poolSize"` | Changed: pool options nested |
| (any `TarnConnectionError` / `TarnQueryError` type mismatch in a catch block) | Changed: TarnError subclasses |
| `Did you mean 'createdAt'?` | Changed: camelCase response rows |
| `client.exec is not a function` | Removed: exec() |
| `connect() no longer accepts a callback` | Changed: connect() promise-only |
| `no apiKey provided` | Changed: explicit apiKey |
| `client.on is not a function` | Removed: error event emitter |

## Full changelog

See the tagged GitHub release for 5.0.0 for the complete diff. This guide
is the migration path; the changelog is traceability only.
````

---

## 5. Verification plan

1. **Cold-run project:** an internal reference app or example app currently pinned to 4.6 (not 4.7 — this exercises the mandatory 4.6→4.8 leg, the part most likely to be under-specified).
2. **Runner:** someone who didn't write the guide — support engineer or new hire, no author hand-holding.
3. **Task:** upgrade using only the guide text. Any edit not described in the guide is a defect in the guide, not a runner mistake.
4. **Measure elapsed time**, publish that number in the scope line. Don't publish a guessed number — the failure mode table is explicit about this.
5. **Run every codemod** (entries 1, 2, 4, 5, 7, 8, 10) against the cold-run project plus every example app and any public dependents you can clone. Record residue per entry — that residue list is what makes the "Fix" wording in each entry trustworthy.
6. **Typecheck and test** after codemod-only changes, then again after manual fixes.
7. **Repeat starting from a 4.7 checkout**, taking the single-hop shortcut, to confirm that path works too since the guide explicitly offers it as an option.
8. **Pass against all six criteria** before publishing: completeness (diff the guide against the real tag-to-tag API diff, not just this draft), detectability, sufficiency, automation honesty, path validity (both the 4.6 and 4.7 starting points), self-containment.

## 6. KPI list

- **Tickets per 1,000 upgrades** quoting an upgrade error, tagged by which of the 11 entries — free, support already collects it; whichever entry dominates gets rewritten first.
- **4.8 deprecation-warning telemetry** trending toward zero in the weeks before the branch freeze — confirms the staged path is actually reaching people before the door closes.
- **Codemod run rate vs. manual edits**, if the CLI reports usage — shows which entries people automate vs. hand-fix.
- **Guide analytics**: in-page search terms (especially the 11 literal error strings above) and exit-to-support-channel rate.
- **Adoption curve**: share of weekly npm downloads on 5.x vs. 4.x at 30/60/90 days. This is the primary number — start the identity/version join before 5.0 ships, or the first 90 days are unmeasurable.
- **4.6-specific stragglers**: cross-reference the download breakdown to name projects still on 4.6 specifically, separate from the general 4.x-to-5.0 straggler list — that population carries the leak risk regardless of whether they ever move to 5.0, so it's a higher-urgency support list, not a docs problem.