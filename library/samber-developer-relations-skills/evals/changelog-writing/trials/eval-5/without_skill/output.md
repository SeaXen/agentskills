Here's the 4.3.0 section, written per the [Common Changelog](https://common-changelog.org) spec: `## [version](compare-link) (date)` heading, groups ordered **Changed → Added → Deprecated → Removed → Fixed** (only applicable groups shown), imperative capitalized entries, `**Breaking:**` marker for the breaking change, and no separate "Security" heading — the CVE fix lives under Fixed with its advisory linked inline.

```markdown
## [4.3.0](https://github.com/samber/pgfleet/compare/v4.2.0...v4.3.0) (2026-09-18)

### Changed

- **Breaking:** Drop support for Node.js 18 ([#509](https://github.com/samber/pgfleet/pull/509))

### Added

- Add `poolStats()` method ([#501](https://github.com/samber/pgfleet/pull/501))

### Deprecated

- Deprecate `setMaxIdle()` in favor of `configure({ maxIdle })`; `setMaxIdle()` will be removed in v5.0 ([#504](https://github.com/samber/pgfleet/pull/504))

### Fixed

- Fix a malformed DSN leaking the password into logs (CVE-2026-3311, [GHSA-xxxx-yyyy-zzzz](https://github.com/samber/pgfleet/security/advisories/GHSA-xxxx-yyyy-zzzz), [#507](https://github.com/samber/pgfleet/pull/507))
```

Two things to swap in before you paste this in: the `GHSA-xxxx-yyyy-zzzz` slug (placeholder from your prompt — use the real advisory ID once published) and the `samber/pgfleet` repo path if it differs from your actual org/repo.