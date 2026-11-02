## Which change earns which channel

Channel budget should track **user action/impact**, not engineering effort. By that measure, the two changes trade places from what the effort chart suggests:

| Change | Changelog | Mailing list | In-app banner |
|---|---|---|---|
| Storage engine rewrite (18k lines, 1 quarter, 4 engineers) | ✅ headline entry | ✅ headline, no action needed | ❌ |
| `flush_interval` 5s→60s (1 line) | ✅ explicit "Changed" entry with impact | ✅ separate, clearly flagged item | ✅ |

**Why the rewrite doesn't get the banner:** it changes nothing a user can observe or needs to do — same query results, same file format, same API. That's the textbook "skip or minimize" case ("Refactored authentication module — unless it affects developers"). A banner is an interruption budget; spending it on a no-action item trains users to ignore the next one, which is exactly the item that *will* need their attention.

**Why the one-liner gets the banner:** it silently changes two things for every existing install that hasn't set `flush_interval` explicitly — metrics become visible up to 60s later, and up to 60s of buffered data can be lost on an unclean shutdown instead of 5s. That's a runtime behavior change with a real durability/freshness tradeoff, on by default, for ~4,000 unattended agents. It's small in diff size but exactly the shape of change the skill flags as needing proactive surfacing (its own canonical example is "Default timeout increased from 30s to 60s" filed under Changed, escalated with explicit before/after impact and a way to opt out) — not because it's "breaking" in the semver sense, but because most affected users will never read a changelog before or after upgrading.

## Draft copy

### Changelog

```markdown
## [2.9.0] - 2026-09-XX
### Changed
- Rewrote the on-disk storage engine (new internal representation, same
  query results, same file format, same public API). Substantially lower
  memory churn under load. No action needed on upgrade.
- Default `flush_interval` changed from `5s` to `60s`. The old default was
  hammering small backends with frequent small writes. Impact: metrics
  become visible up to 60s later, and up to 60s of buffered data can be
  lost on an unclean shutdown instead of 5s. To keep the old behavior,
  set `flush_interval: 5s` explicitly in your config before upgrading.
```

### Mailing list (~900 subscribers)

```
Subject: Halyard 2.9.0 — new storage engine, and one setting to check first

We spent this quarter rewriting Halyard's on-disk storage engine from
scratch — same query results, same file format, same public API, just a
lot less memory churn internally. Nothing to change on your end.

⚠️ One thing to check before you upgrade:
The default flush_interval is now 60s (was 5s) — this cuts write pressure
on small backends significantly, but means metrics show up later and a
crash can lose up to 60s of buffered data instead of 5s. If that tradeoff
doesn't work for you, set flush_interval: 5s explicitly in your config.

Full changelog: [link]
```

### In-app banner (flush_interval only)

```
Halyard 2.9.0: default flush interval is now 60s (was 5s) — less load on
your backend, but data shows up later and crash-loss window grows to 60s.
Keep the old behavior: set flush_interval: 5s. [See changelog]
```

Dismissible, shown once to installs upgrading into 2.9.0 — not persistent. That's the one ask worth making of the frontend team for this release; the rewrite doesn't need their time.