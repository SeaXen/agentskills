# authkit v4 Migration Guide

**Audience:** all 61 service teams consuming `authkit`
**Owner:** Platform team
**Status:** Draft — fill bracketed placeholders `[ ]` with the real signatures/dates before publishing

---

## TL;DR

- authkit v4 changes 9 function signatures and removes 2 helpers.
- v3 and v4 **can coexist** in the monorepo — this is not a flag day. See [Coexistence strategy](#coexistence-strategy).
- Estimated migration time per service: **[X minutes/hours]**, mostly mechanical.
- Hard deadline: **v3 import path deleted on [DATE]**. Migrate before then.
- Questions → `#authkit-v4-migration` Slack channel. Office hours: **[day/time]**.

---

## 1. Why v4

[One paragraph, plain language, no marketing tone. State the concrete problem v3 had — e.g. inconsistent context propagation, panic-based error handling, an API shape that caused a specific incident — and what v4 fixes. Reference the incident or RFC if one exists. Teams tolerate breaking changes much better when they understand *why*; skip this section and adoption slows.]

Example of the level of specificity to aim for:

> v3's `Authenticate()` swallowed context cancellation, which caused goroutine leaks under load ([INCIDENT-1234]). v4 makes `context.Context` the first parameter everywhere and returns errors instead of panicking, closing that entire class of bug.

---

## 2. Coexistence strategy

Because this is a major version, Go's module rules already require the v4 import path to carry a `/v4` suffix:

```
// v3 (current, unchanged)
import "github.com/kelvinbridge/platform/authkit"

// v4 (new)
import "github.com/kelvinbridge/platform/authkit/v4"
```

This means **v3 and v4 are two independent packages that can be imported side by side in the same monorepo, even in the same binary**, for the duration of the migration. No service is forced to move on anyone else's schedule.

Implications:

- Migrate one service at a time. There's no coordinated cutover.
- A service can depend on `authkit/v4` while its neighbor still depends on `authkit`.
- The platform team commits to maintaining `authkit` (v3) with security fixes only, until the removal date below.
- **`authkit` (v3) will be deleted from the monorepo on `[DATE]`.** After that date, unmigrated services stop compiling. Set the deadline far enough out that teams can plan it into a sprint — 60–90 days is typical for an internal library with this many consumers.

If your service embeds authkit types in a public API you own (e.g. a gRPC/HTTP contract), flag it in `#authkit-v4-migration` before you migrate — swapping the type may ripple into your own consumers.

---

## 3. Quick migration checklist

1. Update your import: `authkit` → `authkit/v4`.
2. Run `go build ./...`. Fix compile errors using the [signature reference](#4-breaking-changes-reference) below — most are mechanical.
3. Run `go vet ./...` and your existing test suite.
4. Search your service for the 2 removed helpers (`[HelperA]`, `[HelperB]`) and replace per [Removed helpers](#5-removed-helpers).
5. Deploy to staging. Confirm auth flows manually if your service has custom auth logic (SIWA, token refresh, mTLS, etc.) — automated tests don't always catch behavioral changes.
6. Open a PR titled `chore(authkit): migrate to v4`. Tag `#authkit-v4-migration` reviewers if you want platform-team eyes.
7. Update your row in the [migration tracker](#8-migration-tracker).

Most services should be able to complete steps 1–4 in one sitting.

---

## 4. Breaking changes reference

Each entry below follows the same format: v3 signature, v4 signature, why, and whether the change is **mechanical** (compiler will find every call site, fix is find-and-replace) or **semantic** (behavior changed — read the note, don't just satisfy the compiler).

> Replace the 9 placeholder entries below with the real diff. Keep the mechanical/semantic tag — it's the single most useful piece of information for a team triaging 40 compile errors at once.

### 4.1 `[FunctionName1]` — mechanical

```go
// v3
func Authenticate(token string) (*User, error)

// v4
func Authenticate(ctx context.Context, token string) (*User, error)
```

**Why:** [reason]
**Fix:** pass the `context.Context` you already have in scope. If you don't have one, use `context.Background()` as an interim step, but prefer threading a real request-scoped context — that's the whole point of the change.

### 4.2 `[FunctionName2]` — semantic

```go
// v3
func (c *Client) Authorize(userID string, scope string) bool

// v4
func (c *Client) Authorize(ctx context.Context, userID string, scopes ...string) (Decision, error)
```

**Why:** [reason]
**Fix:** this is not a drop-in replacement. v3 returned `bool`; v4 returns a `Decision` struct with `Allowed bool` plus a `Reason` field for audit logging, and an `error` for transport/auth-service failures that v3 silently mapped to `false`. **Any call site that treated a v3 `false` as "denied" needs to distinguish "denied" from "couldn't check" in v4** — this is the change most likely to hide a real bug if you rush it.

### 4.3–4.9 `[FunctionName3]` through `[FunctionName9]`

| # | Function | v3 | v4 | Type | Note |
|---|----------|----|----|------|------|
| 3 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 4 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 5 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 6 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 7 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 8 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |
| 9 | `[Name]` | `[sig]` | `[sig]` | mechanical/semantic | `[note]` |

---

## 5. Removed helpers

These have **no v4 equivalent** — no shim, no deprecated-but-present stub. Every call site must be rewritten, not just re-pointed.

### `[HelperA]`

```go
// v3 — removed in v4
func MustParseClaims(token string) Claims
```

**Why removed:** [e.g. it panicked on malformed input, which took down 3 services during a token-format rollout in 2025].
**Replace with:**

```go
claims, err := authkitv4.ParseClaims(ctx, token)
if err != nil {
    return fmt.Errorf("parsing claims: %w", err)
}
```

### `[HelperB]`

```go
// v3 — removed in v4
func (c *Client) RefreshOrPanic(token string) string
```

**Why removed:** [reason]
**Replace with:** `[replacement pattern]`

If your service can't find a clean replacement for either helper, say so in `#authkit-v4-migration` before working around it — a repeated workaround across several teams is a signal the platform team should add a v4 helper, not something every team should independently reinvent.

---

## 6. Automated migration

For the mechanical changes (import path, added `ctx` parameters, renamed fields), a codemod removes most of the manual editing:

```bash
# platform team ships this alongside the v4 release
go run github.com/kelvinbridge/platform/authkit/v4/cmd/authkit-migrate ./...
```

It handles:
- import path rewrite (`authkit` → `authkit/v4`)
- inserting `ctx` as the first argument where a `context.Context` is already in scope in the calling function
- mechanical renames (`[old]` → `[new]`)

It does **not** handle the semantic changes in §4.2 or the removed helpers in §5 — those need a human to read the note and decide the right fix. The tool will leave a `// TODO(authkit-v4):` comment at every site it couldn't safely rewrite; `grep -rn "TODO(authkit-v4)"` after running it to find your remaining work.

If a codemod isn't ready yet, say so and drop this section — don't ship instructions for a tool that doesn't exist. A gofmt-based `-r` rule or a small `comby`/`ast-grep` script covers the pure rename cases even without a full codemod binary.

---

## 7. Verification

Before merging your migration PR:

- [ ] `go build ./...` — no errors
- [ ] `go vet ./...` — clean
- [ ] Existing unit/integration test suite passes unmodified
- [ ] If you touched `[FunctionName2]` (the `Authorize` semantic change): add a test asserting your service distinguishes "denied" from "auth-check failed"
- [ ] Manual smoke test in staging for any custom auth flow
- [ ] No `TODO(authkit-v4)` comments left unresolved

Passing tests confirm the code compiles and old behavior is preserved where expected — they do not confirm you handled the semantic changes correctly. Read §4 for every function your service actually calls; don't rely on green CI alone for those.

---

## 8. Migration tracker

Track all 61 services centrally so the platform team knows who's stuck and who's done. A shared sheet or an internal dashboard both work — pick whichever your org already checks.

| Team | Service | Status | Owner | PR |
|------|---------|--------|-------|-----|
| `[team]` | `[service]` | not started / in progress / in review / done | `[@owner]` | `[link]` |
| ... | ... | ... | ... | ... |

Generate the initial list with a repo-wide grep rather than asking teams to self-report — that's the actual ground truth of who imports authkit:

```bash
grep -rl '"github.com/kelvinbridge/platform/authkit"' --include='*.go' . | \
  xargs -I{} dirname {} | sort -u
```

Re-run weekly against `.../authkit/v4` vs `.../authkit` to compute real migration percentage, rather than trusting the tracker sheet to stay current.

---

## 9. Timeline

| Date | Milestone |
|------|-----------|
| `[T+0]` | v4 released, coexists with v3, codemod available |
| `[T+0]` | This guide published, `#authkit-v4-migration` channel opened |
| `[T+2w]` | First office hours |
| `[T+4w]` | Migration tracker review — platform team follows up with teams still "not started" |
| `[T+8w]` | v3 enters security-fixes-only mode |
| `[T+~10w]` | Final reminder to remaining unmigrated services |
| `[DATE]` | **v3 deleted from the monorepo.** Unmigrated services stop compiling. |

---

## 10. FAQ / common compile errors

**`not enough arguments in call to authkit.Authenticate`**
You're calling the v3 signature after switching your import to v4. Add the `ctx` parameter — see §4.1.

**`cannot use false as type Decision`**
You migrated `Authorize`'s import but not its call sites. This one needs a real code change, not just a compiler-guided fix — see §4.2, the "denied" vs "check failed" distinction matters here.

**`undefined: authkitv4.MustParseClaims`**
That helper was removed, not renamed. See §5.

**My service does something unusual with authkit that isn't covered here.**
Post it in `#authkit-v4-migration` rather than guessing — if it's a case others will hit too, we'll add it to this guide.

---

## Support

- Slack: `#authkit-v4-migration`
- Office hours: `[day/time, link]`
- For urgent production issues tied to migration: `[on-call/escalation path]`

---

*Fill every `[bracketed]` placeholder with the real signatures, dates, owners, and incident references before publishing. The structure, the coexistence strategy (§2), and the mechanical/semantic distinction (§4) are the load-bearing parts of this guide — the placeholders are the only authkit-specific facts I don't have access to from here.*