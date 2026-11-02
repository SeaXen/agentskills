# Release notes — Corvid v1.8.0

**Format:** Common Changelog (library/SDK, readers diff versions, PRs are the unit of change — see the skill's Choosing table). Delivering the top two surfaces per the skill's default (changelog and release body are the same text, pasted twice). Swap to Keep a Changelog if that's what the existing `CHANGELOG.md` already uses.

Net diff before categorizing: `#313` → `#316` (revert) → `#319` (re-add) collapse to one surviving outcome — `retryOn` exists, opt-in, still off by default.

## CHANGELOG.md

```markdown
## [1.8.0] - <fill in release date, YYYY-MM-DD>

### Changed

- Reuse sockets across client instances instead of opening a new connection per
  request, cutting connection overhead under concurrent load (#310)
- Document that `request()` has always retried `502` responses up to three
  times; this clarifies existing behavior only, nothing changed in code (#321)

### Added

- Add an opt-in `retryOn` option for custom retry logic, gated behind the
  `RETRY_ON_EXPERIMENTAL` environment flag and disabled by default
  (#313, #316, #319)

### Fixed

- Fix the auth refresh lock not being released when a token refresh request
  fails, which could leave subsequent requests stuck waiting indefinitely (#325)
```

## Release body (git host)

```markdown
This release reuses sockets across client instances to cut connection overhead,
adds an opt-in `retryOn` option behind an experimental flag, and fixes a
stuck-request bug triggered by a failed auth token refresh.

### Changed

- Reuse sockets across client instances instead of opening a new connection
  per request, cutting connection overhead under concurrent load (#310)
- Document that `request()` has always retried `502` responses up to three
  times — no behavior change (#321)

### Added

- Opt-in `retryOn` option for custom retry logic, behind `RETRY_ON_EXPERIMENTAL`,
  off by default (#313, #316, #319)

### Fixed

- Auth refresh lock now releases correctly on error, fixing requests that
  could hang after a failed token refresh (#325)

**Full changelog**: v1.7.2...v1.8.0
```

## Traceability

| Entry | Source |
|---|---|
| Reuse sockets across client instances | #310 |
| Document 502-retry behavior | #321 |
| Add opt-in `retryOn` option | #313, #316 (revert, folded in), #319 |
| Fix auth refresh lock not released on error | #325 |

## Excluded (3 changes)

| Change | Reason |
|---|---|
| `chore(deps): bump vitest 1.4 -> 1.6` (#311) | dev-only dependency, no consumer surface |
| `refactor(src): rename InternalDispatcher to Dispatcher` (#322) | internal rename, no consumer surface — *assumes `Dispatcher` isn't part of the public exports; see below* |
| `ci: split the matrix job` (#323) | CI-only change, no consumer surface |

## Needs a human

1. **`Dispatcher` rename (#322):** included in the exclusion list on the assumption it's internal-only (the old name was literally `InternalDispatcher`). If it's actually exported from the package, this is a breaking rename and 1.8.0 would need to be 2.0.0 per semver, not a minor bump.
2. **`retryOn` flag (#313/#316/#319):** it's off by default, which the worked example for "feature flag, defaults off" treats as no entry at all. I included it anyway because, unlike a stub flag, it's fully functional and a consumer can turn it on today — but it's still named `RETRY_ON_EXPERIMENTAL`, so confirm you actually want it publicly documented in this release rather than held back.
3. **#310's "40% faster" claim:** dropped per your note — no benchmark in the PR, only an eyeballed load test. Don't restate the number until a real benchmark exists.
4. **Release date and PR links:** placeholder date left in the header; PR numbers aren't linked since I don't have the repo URL to build them from.
5. **Version-number check:** all surviving entries are non-breaking (`Changed`/`Added`/`Fixed`), so 1.8.0 as a minor bump is consistent — this flips if #322 turns out to be a public breaking rename (see #1).