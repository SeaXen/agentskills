# authkit v3 → v4 migration guide — draft deliverable

## 0. Which side of the Churn Rule this is on

State this before anything else, because it changes what "done" means.

Kelvinbridge owns every consumer (61 services, one monorepo, every team internal). This is squarely the case the Churn Rule (*Software Engineering at Google*, ch.1) is written for: **"infrastructure teams must do the work to move their internal users to new versions themselves or do the update in place, in backward-compatible fashion."** A guide that just hands 61 teams a checklist and a deadline moves work that was the platform team's onto them, for no reason other than that writing a codemod is more upfront effort than writing prose.

Recommendation, not a blocker on drafting the guide: build the codemod and open the mechanical PRs yourselves; use the guide for the ~20% of edits a codemod cannot safely decide (the 2 removed helpers, and the 3 signature changes that turn a `bool`/panic into an `error` a caller must actually handle). That's the hybrid this draft is built around. If the platform team truly cannot spend the engineering week a codemod costs, the guide below still stands alone — but say so explicitly to the 61 teams, because "we could have automated this and chose not to" is a different conversation than "this can't be automated."

## 1. Assumptions and open questions

I don't have your real v3→v4 diff — you didn't paste function names or signatures, and I'm not going to invent facts and present them as your API. Everything below uses a **representative, internally-consistent 9-change/2-removal set**, themed around what a v4 like this typically does (thread `context.Context`, replace silent `bool`/panic returns with `error`, replace `map[string]interface{}` with typed structs). Swap in your real symbols; the anchors, search patterns, and ordering logic transfer directly.

**What I assumed, and what only you can confirm:**

| # | Assumption | Why it matters | What to check |
|---|---|---|---|
| 1 | You have not yet run any static call-site count across the monorepo | Everything below ranks changes by *reasoned* usage pattern, not measured usage | Run the `grep`/`ast-grep` patterns in §2 for real; this is the single highest-leverage hour in this whole exercise, because in a monorepo it's a **complete** census, not a sample |
| 2 | v3 has not shipped a deprecation-warning release yet | Determines whether the staged path (§3) is still purchasable | If v4 is already tagged and v3 is frozen, skip straight to single-hop and say so on screen one |
| 3 | No codemod or lint rule exists yet | Changes what rung of automation (§ automated migration) you're publishing | If one already exists, this changes the "automated migration" section's content, not its position |
| 4 | Every service has a CI pipeline the platform team can gate | The strongest lever you have that an OSS maintainer doesn't | Confirm before promising a hard lint gate in the timeline |
| 5 | Each of the 61 services has a discoverable owner (CODEOWNERS, service catalog, on-call rotation) | The internal-audience section needs an ownership map, not just a guide | Needed before you can publish a per-team freeze date |

**Open questions to resolve before you publish, in priority order:**

1. The actual 9 signatures and 2 removed helpers — everything downstream depends on this.
2. Real call-site counts per symbol (§2) — reorders the guide, possibly substantially.
3. Whether an interim v3.x release is still schedulable, or v4 is already cut.
4. The freeze date: the day a service deployed on v3 stops being deployable at all.
5. Who owns the codemod (if you build one) after this release ships — an orphaned codemod rots into a wrong answer.

---

## 2. Inventory table

Ranked by blast radius **reasoning**, not measurement — replace the "evidence" column with real grep output before publishing. In a monorepo, this is free: every consumer is one `grep -rn` away, which is strictly better than the telemetry an external SDK maintainer has to build from scratch.

| Change | Type | Reasoned blast radius | Evidence (run this) |
|---|---|---|---|
| `authkit.NewClient` gains `ctx` + `Config`, returns `error` | Signature change | Highest — every one of the 61 services calls this once, at boot; nothing compiles until it's fixed | `grep -rn "authkit\.NewClient(" --include=*.go` |
| `(*Client).Middleware()` becomes variadic-options | Signature change | Very high — every HTTP-serving service wires this into its router | `grep -rn "\.Middleware(" --include=*.go` |
| `(*Client).Close()` gains `ctx`, returns `error` | Signature change | Very high — every service's graceful-shutdown path calls this | `grep -rn "\.Close()" --include=*.go \| grep -i authkit` |
| `authkit.NewTestClient` requires `testing.TB` | Signature change | High call-site count, low severity — caught by `go build ./...` in CI within minutes, not a production risk | `grep -rn "authkit\.NewTestClient(" --include=*_test.go` |
| `(*Client).Authenticate` gains `ctx` | Signature change | High — used directly wherever auth isn't done through `Middleware` (gRPC interceptors, websocket upgrades, background jobs) | `grep -rn "\.Authenticate(" --include=*.go` |
| `authkit.ParseClaims` returns `*Claims` instead of `map[string]interface{}` | Type change | Medium — services that read custom claims out of the map; a `go vet`/`staticcheck` pass will not catch the type-narrowing, only the compiler will | `grep -rn "authkit\.ParseClaims(" --include=*.go` |
| `authkit.ValidateToken` returns `(*Claims, error)` instead of `bool` | Signature + behavior change | Medium, and likely overlapping legacy call sites from before `Authenticate` existed | `grep -rn "authkit\.ValidateToken(" --include=*.go` |
| `(*Client).RefreshToken` returns `*TokenPair` instead of `string` | Signature change | Medium-low — only services managing long-lived sessions (web BFFs, mobile gateway) | `grep -rn "\.RefreshToken(" --include=*.go` |
| `(*Client).Authorize` returns `(bool, error)` instead of `bool` | Signature + behavior change | Low count, high severity — every silenced error here was previously a fail-open or fail-closed guess; find these first regardless of count | `grep -rn "\.Authorize(" --include=*.go` |
| **Removed:** `authkit.MustAuthenticate` | Removal | Low, but each site is a panic risk in a live request path today | `grep -rn "authkit\.MustAuthenticate(" --include=*.go` |
| **Removed:** `authkit.DebugDumpToken` | Removal | Should be near-zero in production code paths; treat any hit as a standing finding regardless of count — it was logging raw claims | `grep -rn "authkit\.DebugDumpToken(" --include=*.go` |

Two entries — `Authorize` and the two removals — are promoted ahead of raw call-site count because they carry correctness or security weight independent of how many places call them. Say this explicitly in the guide; "ordered by blast radius" should never read as "ordered only by count."

---

## 3. Recommended path shape

**Hybrid: platform-run codemod for the 7 mechanical signature changes, staged deprecation release first, guide covers only what needs a human decision.**

Reasoning, one line per piece:

- **Staged is free here and the default whenever N-1 can still ship** — you own v3's release cadence, so ship one more v3.x that emits a deprecation warning (see §"New deprecations" below) before cutting v4; every affected service's own build/log output becomes its personal inventory, at the cost of one interim release you already control.
- **A codemod is affordable at this scale and this is exactly the case that promotes it** — 61 consumers in one repo you own is the textbook case for moving the codemod to the top of the automation ranking (`automated-migration-tooling.md`): the mechanical majority of the 9 changes (parameter reshuffles, return-type widening) is `go fix`/AST-rewrite territory, and you can run it centrally instead of asking 61 teams to each rediscover the same edit.
- **The guide handles the residue a codemod can't safely decide**: the 2 removed helpers (someone has to choose the replacement error-handling behavior) and the `Authorize`/`ValidateToken`/`RefreshToken` behavior changes (someone has to decide what the caller does with the new `error`, since silently discarding it just reproduces the old bug).
- **Single-hop alone would be the wrong call** given you still control v3 — it's the fallback only if v4 is already tagged and frozen (see open question 3).

---

## 4. The guide

````markdown
# Upgrading authkit from v3 to v4

This guide covers `authkit` v3.x → v4.0 for every Go service in the monorepo.
Cold-upgrade time is not yet measured — see §12 of this draft; publish the real
number here once one team has run it, and do not publish a guess before then.

## Before you start

Upgrade to v3.(last) first, if you are not already there, and run your build.
Every change below emits a one-time log line at `WARN` the first time the old
symbol is hit at runtime, tagged `authkit_deprecation=<id>` — that tag is your
personal work list. `staticcheck` also flags every old call site at build time
via the `// Deprecated:` godoc comments, so CI catches what the log misses.

Do not stay on v3.0–v3.(last-1): they do not carry the deprecation warnings
and give you no early signal.

## Requirements

- Go >= 1.23 (v4 uses generics in `authkit.TokenPair`)
- `context.Context` must already be threaded through your request path —
  if it isn't, that's a prerequisite refactor, not part of this guide
- No change to peer dependencies

## Automated migration

Run this from your service's root before anything else:

    go run kelvinbridge.internal/authkit/cmd/authkitfix@v4 ./...

This rewrites, mechanically, across your whole module:

- `authkit.NewClient(key)` → `authkit.NewClient(ctx, authkit.Config{APIKey: key})`,
  wrapping the call site in an error check (`if err != nil { ... }` stub you must fill in)
- `.Authenticate(token)` → `.Authenticate(ctx, token)`, threading the nearest
  `ctx` already in scope, or inserting `context.TODO()` with a `// TODO(authkit-v4)` marker if none is in scope
- `.Close()` → `.Close(ctx)`, same context-sourcing rule
- `authkit.NewTestClient()` → `authkit.NewTestClient(t)` inside `_test.go` files
- `authkit.ParseClaims(token)` call sites are flagged, not rewritten — the
  return type changed from `map[string]interface{}` to `*Claims`, and the tool
  cannot infer which map keys you were reading

**Coverage boundary, stated plainly:** the tool does not touch `Authorize`,
`ValidateToken`, `RefreshToken`, or either removed helper. Those five entries
below all changed what happens on an error path, and a mechanical rewrite that
guesses at your error handling is worse than no rewrite. Every `context.TODO()`
marker it leaves behind is also worth a manual look — it means the tool
couldn't find a real context to thread and picked the safe placeholder.

**Verify after running it:** `go build ./... && go vet ./... && go test ./...`.
This is a review-required rewrite, not fire-and-forget — read the diff before
you commit it.

## Breaking changes

### Changed: `authkit.NewClient` takes `(ctx, Config)` and returns `error` {#changed-newclient}

**Affects you if** you call `authkit.NewClient` anywhere. Every service does,
once, at startup. Search `authkit\.NewClient\(` in your codebase. On v3 built
against v4's package you will see:

    ./main.go:24:9: not enough arguments in call to authkit.NewClient

`NewClient` used to take a bare API key and could not fail — a bad key was
only discovered on the first real request. v4 does a health check against the
auth backend at construction time and returns the failure immediately, so a
misconfigured service fails at boot, not silently in production traffic.

```go
// Before (v3)
client := authkit.NewClient(cfg.AuthKitAPIKey)

// After (v4)
client, err := authkit.NewClient(ctx, authkit.Config{
    APIKey:  cfg.AuthKitAPIKey,
    Timeout: 5 * time.Second,
})
if err != nil {
    return fmt.Errorf("authkit: %w", err)
}
```

**Fix:** `authkitfix@v4` rewrites the call and inserts the error-check stub;
fill in your service's own error-handling convention (return, `log.Fatal` at
boot, etc.) — the tool does not guess that part.

**Escape hatch:** none. The health check cannot be disabled; if your service
boots in an environment with no network path to the auth backend, that's a
deployment-topology problem to raise with the platform team before upgrading,
not a flag to flip.

### Changed: `Middleware()` takes variadic options {#changed-middleware-options}

**Affects you if** you call `client.Middleware()`. Search `\.Middleware\(`. No
runtime error on v3 usage against v4 — it still compiles with zero arguments —
but the header names and skip-paths that used to be hardcoded now default
differently; see Behavior changes below if your service relied on the old
hardcoded skip-path list.

`Middleware()` previously hardcoded which paths bypass auth (`/healthz`,
`/metrics`) and which header carries the token (`Authorization`). Several
services needed a different skip-path list and worked around it with their own
wrapper handler; v4 makes both configurable so that workaround can be deleted.

```go
// Before (v3)
router.Use(client.Middleware())

// After (v4) — only if you need non-default skip paths or header name
router.Use(client.Middleware(
    authkit.WithSkipPaths("/healthz", "/metrics", "/internal/debug"),
))
```

**Fix:** no codemod needed — this one compiles unchanged unless you want the
new options. Search your codebase for a hand-rolled "skip auth for this path"
wrapper around the middleware and consider deleting it in favor of
`WithSkipPaths` (see Housekeeping).

**Escape hatch:** calling `Middleware()` with no arguments keeps v3's default
skip-paths and header name exactly.

### Changed: `Close()` takes `ctx` and returns `error` {#changed-close-ctx}

**Affects you if** you call `client.Close()`, typically in a graceful-shutdown
handler. Search `\.Close\(\)` and check it's the `authkit` client, not another
`Closer`. On v3 code built against v4:

    ./server.go:88:14: not enough arguments in call to client.Close

`Close` now flushes pending audit-log writes to the central log service before
returning, and that flush can fail or time out — v3 dropped these silently on
shutdown, which is the gap that prompted the change.

```go
// Before (v3)
client.Close()

// After (v4)
shutdownCtx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
defer cancel()
if err := client.Close(shutdownCtx); err != nil {
    log.Warn("authkit close", "err", err)
}
```

**Fix:** `authkitfix@v4` rewrites the call site and threads a
`context.Background()`-derived timeout context if none is in scope; adjust the
timeout to match your service's own shutdown deadline.

**Escape hatch:** none — a swallowed error here is exactly the silent-drop bug
v4 fixes. If you must ignore it, ignore it explicitly: `_ = client.Close(ctx)`.

### Changed: `NewTestClient` requires `testing.TB` {#changed-newtestclient-tb}

**Affects you if** your test suite calls `authkit.NewTestClient()`. Search
`authkit\.NewTestClient\(` in `*_test.go`. Fails at `go build` (test binary),
not at runtime:

    ./client_test.go:15:32: not enough arguments in call to authkit.NewTestClient

The test client used to leak a background token-refresh goroutine per test,
which was harmless individually but made `-race` runs flaky under high test
parallelism. Passing `testing.TB` lets it register `t.Cleanup` to shut that
goroutine down deterministically.

```go
// Before (v3)
client := authkit.NewTestClient()

// After (v4)
client := authkit.NewTestClient(t)
```

**Fix:** `authkitfix@v4` rewrites every call site in `_test.go` files
automatically; this one has no manual residue.

**Escape hatch:** none needed — this is a pure test-code change with no
production-behavior consequence.

### Changed: `Authenticate` takes `ctx` {#changed-authenticate-ctx}

**Affects you if** you call `client.Authenticate` directly (outside
`Middleware` — gRPC interceptors, websocket upgrade handlers, background job
runners). Search `\.Authenticate\(`.

    ./interceptor.go:41:20: not enough arguments in call to client.Authenticate

Context propagation lets the auth backend call be cancelled with the inbound
request and carries trace IDs through to the central auth service's own logs,
closing a long-standing gap where an authenticate call outlived a cancelled
request.

```go
// Before (v3)
user, err := client.Authenticate(token)

// After (v4)
user, err := client.Authenticate(ctx, token)
```

**Fix:** `authkitfix@v4` threads the nearest in-scope `ctx`; if none is found
it inserts `context.TODO()` with a `// TODO(authkit-v4): thread a real context`
marker — grep for that marker after running the tool and resolve every one.

**Escape hatch:** `context.Background()` if your call site genuinely has none
(rare — usually means a missing context parameter one layer up that this is a
good time to fix).

### Changed: `ParseClaims` returns typed `*Claims`, not a map {#changed-parseclaims-typed}

**Affects you if** you call `authkit.ParseClaims`. Search
`authkit\.ParseClaims\(`. Fails at compile time on any code that indexes the
old map return:

    ./handler.go:52:19: claims["sub"] (untyped map index) undefined (type *authkit.Claims has no index operation)

The map return type meant a typo'd claim key (`"suub"`) compiled and returned
`nil` silently. `*Claims` makes every claim a named field, so the typo is now
a compile error instead of a production bug that only shows up as an
unexpectedly-nil value.

```go
// Before (v3)
claims, err := authkit.ParseClaims(token)
sub := claims["sub"].(string)

// After (v4)
claims, err := authkit.ParseClaims(token)
sub := claims.Subject
```

**Fix:** flagged, not rewritten, by `authkitfix@v4` — the tool cannot infer
which map keys you read or what type you asserted them to. Manual steps: for
each flagged site, replace `claims["<key>"].(<type>)` with the matching
`Claims` field; see the full field list in `authkit.Claims`'s godoc.

**Escape hatch:** `claims.Extra` holds any claim not promoted to a named
field, still as `map[string]interface{}`, for forward-compatibility with
custom claims your service adds.

### Changed: `ValidateToken` returns `(*Claims, error)`, not `bool` {#changed-validatetoken-claims}

**Affects you if** you call `authkit.ValidateToken`. Search
`authkit\.ValidateToken\(`. Compiles but misbehaves on v3 code built against
v4 without editing — this is the one entry in this guide where the compiler
will not catch you, because a `bool`-shaped call site can still typecheck if
you're only checking truthiness of the first return value in some other way.
Audit every call site by hand.

`ValidateToken` used to return `false` for both "token is invalid" and "the
auth backend timed out" — indistinguishable to the caller, and a transient
backend timeout was silently treated the same as a hostile token. Splitting
the return lets a caller retry a timeout instead of rejecting the user.

```go
// Before (v3)
if !authkit.ValidateToken(token) {
    return errUnauthorized
}

// After (v4)
claims, err := authkit.ValidateToken(ctx, token)
if err != nil {
    if errors.Is(err, authkit.ErrBackendUnavailable) {
        return errRetryable
    }
    return errUnauthorized
}
```

**Fix:** no codemod — this needs a human decision about retry behavior.
Numbered manual steps: (1) find every call site via the search pattern above,
(2) decide whether your service should distinguish `ErrBackendUnavailable`
from a genuinely invalid token, (3) if not, `_, err := ...; if err != nil { return errUnauthorized }`
preserves v3's exact (imprecise) behavior.

**Escape hatch:** collapsing the error to a bare `err != nil` check reproduces
v3's behavior exactly, if you decide the distinction isn't worth carrying.

### Changed: `RefreshToken` returns `*TokenPair`, not a bare string {#changed-refreshtoken-pair}

**Affects you if** you call `client.RefreshToken`. Search `\.RefreshToken\(`.
Compile-time failure on the assignment:

    ./session.go:30:2: cannot use accessToken (variable of type *authkit.TokenPair) as string value

v3 discarded the rotated refresh token, forcing services to keep using the
original refresh token until it expired — v4 rotates it on every refresh
(standard refresh-token-rotation practice) and hands both tokens back so the
caller can persist the new one.

```go
// Before (v3)
accessToken, err := client.RefreshToken(refreshToken)

// After (v4)
pair, err := client.RefreshToken(ctx, refreshToken)
accessToken := pair.AccessToken
// persist pair.RefreshToken — the old refreshToken is now invalid
```

**Fix:** no codemod — persisting the rotated refresh token touches your
service's own session storage, which the tool has no visibility into.
Numbered steps: (1) locate every call site, (2) find where the old refresh
token is persisted, (3) replace it with `pair.RefreshToken`, (4) confirm your
session store's schema allows a refresh-token update, not just an insert.

**Escape hatch:** none — the old refresh token is invalidated server-side
after the next call to `RefreshToken` regardless of whether you persist the
new one, so there's no compatibility mode here.

### Changed: `Authorize` returns `(bool, error)`, not a bare `bool` {#changed-authorize-error}

**Affects you if** you call `client.Authorize`. Search `\.Authorize\(`. Low
call-site count, highest-severity entry in this guide — read it even if your
service isn't in the top of the blast-radius table.

    ./guard.go:19:5: assignment mismatch: 2 variables but client.Authorize returns 1 value

v3 returned `false` for both "denied by policy" and "policy service
unreachable," which meant a policy-service outage silently fail-closed
everywhere or fail-open everywhere depending on how each of the 61 services
happened to write the `if` — undocumented and inconsistent across the
monorepo. v4 forces every caller to make that choice explicitly.

```go
// Before (v3)
if !client.Authorize(user, "billing:read") {
    return errForbidden
}

// After (v4)
ok, err := client.Authorize(ctx, user, "billing:read")
if err != nil {
    return errServiceUnavailable // or errForbidden — this is your call, see below
}
if !ok {
    return errForbidden
}
```

**Fix:** no codemod, deliberately — this is the change most likely to hide a
real security decision inside a rewrite script. Numbered manual steps: (1)
locate every call site, (2) for each one, decide and document whether a
policy-service outage should fail open or fail closed for that specific
resource, (3) write the explicit branch, (4) if you don't know the right
answer for a given resource, default to fail-closed and flag it to the
platform team's on-call rather than guessing.

**Escape hatch:** none. This is the entry where "there is none" is the
correct and complete answer — collapsing the error into the boolean again
just reintroduces the bug the change exists to fix.

## New deprecations

| Deprecated API | Replacement | Warning level in v3.(last) | Removed in |
|---|---|---|---|
| `authkit.NewClient(key string)` | `authkit.NewClient(ctx, Config)` | Runtime (first call, `WARN`, `authkit_deprecation=DEP-AK-01`) + `staticcheck` at build time | v4.0 |
| `client.Middleware()` zero-arg | still valid, not deprecated | — | not removed |
| `client.Close()` | `client.Close(ctx)` | Runtime + `staticcheck`, `DEP-AK-03` | v4.0 |
| `authkit.NewTestClient()` | `authkit.NewTestClient(t)` | `staticcheck` only (test code, no runtime path) | v4.0 |
| `client.Authenticate(token)` | `client.Authenticate(ctx, token)` | Runtime + `staticcheck`, `DEP-AK-05` | v4.0 |
| `authkit.ParseClaims` map return | typed `*Claims` | `staticcheck` only (return-type change, no runtime shim possible) | v4.0 |
| `authkit.ValidateToken(token) bool` | `ValidateToken(ctx, token) (*Claims, error)` | Runtime, `DEP-AK-07` | v4.0 |
| `client.RefreshToken(string) (string, error)` | `RefreshToken(ctx, string) (*TokenPair, error)` | Runtime, `DEP-AK-08` | v4.0 |
| `client.Authorize(user, resource) bool` | `Authorize(ctx, user, resource) (bool, error)` | Runtime, `DEP-AK-09` | v4.0 |
| `authkit.MustAuthenticate` | none — call `Authenticate` and handle the error | Runtime, `DEP-AK-10` | v4.0 |
| `authkit.DebugDumpToken` | none — use `ParseClaims` + your own redacted logging | Runtime, `DEP-AK-11`, escalated to build-time **failure** (not just warning) given the security finding | v4.0 |

`DebugDumpToken` gets a harder gate than the others: since it was found
logging raw claims in production, CI treats any remaining call site as a
build failure in v3.(last), not a warning — the internal-monorepo equivalent
of Node's "runtime, all code" rung, skipping the softer levels because the
harm is active today, not hypothetical at removal time.

### Removed: `authkit.MustAuthenticate` {#removed-mustauthenticate}

**Affects you if** you call `authkit.MustAuthenticate`. Search
`authkit\.MustAuthenticate\(`. Does not exist in v4 — a compile error, not a
runtime message:

    ./handler.go:12:9: undefined: authkit.MustAuthenticate

It panicked on an invalid token. In a live request handler, that turned a bad
token from a client into a 500 and a crashed goroutine instead of a handled
401 — the panic-as-control-flow pattern the platform team no longer allows
inside `authkit`.

```go
// Before (v3)
user := authkit.MustAuthenticate(token)

// After (v4)
user, err := client.Authenticate(ctx, token)
if err != nil {
    return errUnauthorized
}
```

**Fix:** no codemod. Manual steps: (1) locate every call site, (2) replace
with `Authenticate` plus an explicit error branch, (3) confirm the branch
returns a 401-equivalent, not a panic/recover shim that reproduces the old
crash behavior with extra steps.

**Escape hatch:** none. If a call site truly cannot handle an error at that
point in the code, that is a design problem in that call site, not a gap in
`authkit` — raise it with the platform team rather than wrapping `Authenticate`
in a new `Must*` helper of your own.

### Removed: `authkit.DebugDumpToken` {#removed-debugdumptoken}

**Affects you if** you call `authkit.DebugDumpToken`. Search
`authkit\.DebugDumpToken\(`. Does not exist in v4:

    ./main.go:201:14: undefined: authkit.DebugDumpToken

It pretty-printed a token's decoded claims for local debugging. A monorepo-wide
grep found call sites still wired into production log statements, meaning
session claims were reaching the central log aggregator in plaintext — a
compliance finding, not a style preference, which is why this entry escalates
to a build failure in v3.(last) rather than a warning.

```go
// Before (v3)
log.Debug("token", "claims", authkit.DebugDumpToken(token))

// After (v4)
claims, _ := authkit.ParseClaims(token)
log.Debug("token", "subject", claims.Subject, "expires", claims.ExpiresAt)
// never log claims.Extra or the raw token — both may carry sensitive fields
```

**Fix:** no codemod, and none is coming — every call site needs a human to
decide which specific fields are safe to log for that service, since blanket
restoration of the old dump defeats the purpose of removing it.

**Escape hatch:** none, by design. If a team believes it has a legitimate
debugging need this doesn't cover, that's a conversation with the platform
team about a properly-redacted debug endpoint, not a request to bring the
helper back.

## Housekeeping

- If your service hand-rolled a "skip auth for `/healthz`" wrapper around
  `Middleware()` to work around the old hardcoded skip-path list, delete it
  and pass `authkit.WithSkipPaths(...)` instead.
- Delete any local retry/backoff wrapper you built around `Authenticate` to
  paper over v3's context-less, uncancellable calls — v4's context threading
  makes those wrappers redundant.
- Delete any `recover()` block you added specifically to catch a panic from
  `MustAuthenticate` — with `Authenticate`'s explicit error return, that
  recover block is now dead code masking nothing.

## Troubleshooting

**`not enough arguments in call to authkit.NewClient`** — you're on v4's
package with v3-shaped code; run `authkitfix@v4` or see [Changed:
NewClient](#changed-newclient).

**`assignment mismatch: 2 variables but client.Authorize returns 1 value`** —
see [Changed: Authorize](#changed-authorize-error); this is the entry that
needs a real decision, not just a rewrite.

**`undefined: authkit.MustAuthenticate`** — see [Removed:
MustAuthenticate](#removed-mustauthenticate).

**`undefined: authkit.DebugDumpToken`** — see [Removed:
DebugDumpToken](#removed-debugdumptoken); do not re-add an equivalent helper
without platform-team sign-off, given why it was removed.

**Service builds but claims lookups return zero values** — you're on
`ParseClaims`'s old map-shaped code path that still compiles against `*Claims`
via `claims.Extra["key"]`; see [Changed: ParseClaims](#changed-parseclaims-typed)
and move promoted fields off `.Extra`.

**CI fails on `DEP-AK-11` even though I don't call `DebugDumpToken` directly**
— check a shared internal helper package your service imports; the security
sweep found this helper wrapped in at least one internal logging package, not
only called directly.

## Full changelog

See the `authkit` v4.0 release notes for the complete change list, including
non-breaking additions. This guide is the migration path; the changelog is
not — do not send a reader here mid-upgrade looking for the next step.
````

---

## 5. Verification plan

**Cold run:** pick one real service, not an example app — ideally one that touches most of the entries (calls `Authenticate` directly, uses `Middleware`, calls `Authorize`, and had at least one `MustAuthenticate` or `DebugDumpToken` site in the pre-audit grep). Someone from **that service's team**, not the platform team, upgrades it using only the published guide, with a platform-team member present only to answer "is this expected" questions, not to drive.

**What passes, against this skill's six-point bar:**

1. **Completeness** — diff the guide against the real v3→v4 API diff (not the changelog) once you have it; every removed or resignatured public symbol needs an entry.
2. **Detectability** — every entry's search pattern actually finds every real call site in the cold-run service; every literal error string matches what the compiler/linter actually prints.
3. **Sufficiency** — the cold-run engineer makes no edit the guide doesn't describe. Any such edit is a missing entry, not a gap in their understanding.
4. **Automation honesty** — run `authkitfix@v4` against the cold-run service and at least a handful of others first; publish the exact residue it leaves (the `context.TODO()` markers, the flagged-not-rewritten `ParseClaims` sites) before anyone else runs it.
5. **Path validity** — since only one hop is promised (v3.(last) → v4), this is satisfied by the cold run itself; no multi-version jump to separately validate.
6. **Self-containment** — the cold-run engineer never opens `authkit`'s source or the issue tracker. If they do, that's the exact gap to close before wider rollout.

**Measure and publish:** the elapsed wall-clock time of that cold run, as the guide's own stated expected effort — don't publish a number before this run happens. If the service is large or the diff turns out bigger than 9+2 once you have the real one, shard the guide and the verification per module rather than dropping entries, per the skill's own guidance on large surfaces.

---

## 6. KPI list

Ordered by value per hour of wiring, per the skill's own instrumentation order — and note the monorepo changes what's cheap versus what's a standing job compared to an external SDK:

- **CI-gate hit rate on `DEP-AK-*` codes**, per service, trending to zero before the v4 cutover — free, since it's the same CI output you already generate; this is your monorepo's version of "deprecation-warning telemetry," and it's stronger than an OSS maintainer's version because you can make it a build failure, not just a log line, whenever a finding (like `DebugDumpToken`) warrants it.
- **`authkitfix@v4` run rate versus manual edits**, from the tool's own summary output — free if you add one counter line to the tool.
- **Support/on-call tickets referencing an `authkit` v4 error string** — cheap, your on-call already collects these; whichever entry generates the most is the one to rewrite first.
- **Adoption curve: services on v4 versus v3, at 2/4/8 weeks post-release** — this is the number that matters, and it's cheap here specifically because you don't need a registry-download proxy: query the monorepo's own dependency graph (go.mod / internal module graph) directly for an exact count, not an estimate. Expect a long tail even inside one company — plan the last handful of services as named accounts your platform team works directly, not as a guide problem.
- **Stragglers list**: named services still on v3 past the freeze date, with owning team and tracking issue — this is what turns the freeze date from a suggestion into an enforceable one.

Start hard enforcement (the CI gate that makes v3 undeployable) only once the adoption curve visibly flattens, not on the date you first announced — even inside a company you fully control, expect this to take longer than the first announcement implies.