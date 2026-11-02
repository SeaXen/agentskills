## Corvid 1.8.0

### Added

- **Socket reuse across client instances** (#310) — Corvid now reuses connections across separate client instances instead of opening fresh sockets each time. In our own load testing this was noticeably faster on hot paths, though we haven't run a formal benchmark, so treat that as directional rather than a guaranteed number for your workload.
- **Experimental `retryOn` option** (#313, #319) — lets you customize which conditions trigger a retry. Off by default, gated behind the `RETRY_ON_EXPERIMENTAL` flag while we finish shaking it out. Enable it explicitly if you want to try it; expect the API to still move before it's stable.

### Fixed

- **Auth refresh lock not released on error** (#325) — if a token refresh failed, the internal lock could stay held, blocking subsequent requests from ever refreshing again. It's now released on error paths too. Worth upgrading for if you use the built-in auth/refresh flow.

### Documentation

- Clarified that `request()` has always retried `502` responses up to three times (#321). This isn't new behavior — it was previously undocumented — but call it out in case you were working around it on your end.

### Internal

- Bumped `vitest` 1.4 → 1.6 (dev dependency only, no runtime impact).
- Split the CI matrix job for faster builds.
- Renamed the internal `InternalDispatcher` class to `Dispatcher`; this type was never part of the public API, so no action needed on your end.

---

**Upgrading:** 1.8.0 is backward compatible with 1.7.x — no code changes required. If you rely on token-refresh-heavy auth flows, this release fixes a real deadlock risk (#325) and is worth prioritizing.