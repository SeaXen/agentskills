Flush-interval change earns more channels than storage rewrite. Tiering runs on reader impact, not engineer-hours — quarter of invisible rewrite = tier 4, one-line default change hitting all ~4,000 installs = tier 2.

## Tier call

| Change | Tier | Why | Surfaces earned |
|---|---|---|---|
| `flush_interval` 5s→60s default | **2** — noticeable impact on most, requires action for some | Every install not overriding it gets 55s more staleness by default. Anyone doing near-real-time alerting/dashboards must edit config before upgrading. | Changelog, release body, hosted changelog page, mailing list, in-app banner |
| Storage engine rewrite | **4** — no noticeable impact for most | Same query results, same file format, same public API. Nobody's workflow changes. Memory-churn reduction isn't measured, so it's not even a quantified perf claim. | Changelog + release body only |

Flip side of your instinct: featuring the rewrite on the mailing list or banner spends trust on a change nobody can observe — that's the exact failure this framework exists to catch. The 18k-line/4-engineer story is real and worth telling, just not here — pitch it to `engineering-blog-post` as a narrative piece; changelog tiering has no slot for effort, only for what a reader notices.

Built from your description, not a repo diff — no PR/commit links exist yet, flagged below. Assumed: Common Changelog spec (you mention a public API, readers diff versions — fits better than Keep a Changelog), imperative-present tense, placeholder date `2026-09-18`, integrator/operator audience.

---

## CHANGELOG.md

```markdown
## [2.9.0] - 2026-09-18

### Changed

- Raise the default `flush_interval` from 5s to 60s to reduce load on small
  backends ([#XXXX](url)). Metrics now surface up to 60s later by default —
  set `flush_interval: 5s` to keep the previous cadence.
- Rewrite the on-disk storage engine to reduce memory churn during writes
  ([#XXXX](url)). Query results, the on-disk file format, and the public API
  are unchanged.
```

## Release body (git host)

```markdown
This release raises the default flush interval and rewrites the on-disk
storage engine. No public API or file-format changes — most installs will
only notice metrics arriving up to 55 seconds later than before.

### Changed

- Raise the default `flush_interval` from 5s to 60s to reduce load on small
  backends (#XXXX). Set `flush_interval: 5s` in your config to keep the
  previous cadence.
- Rewrite the on-disk storage engine to reduce memory churn during writes
  (#XXXX). Query results, the on-disk file format, and the public API are
  unchanged.

**Full changelog**: v2.8.x...v2.9.0
```

## Hosted changelog page

```markdown
## September 18, 2026 — Metrics flush interval now defaults to 60s

Halyard's default `flush_interval` moves from 5 seconds to 60 seconds. The
old default pushed writes to small backends too often; most self-hosted
installs should see less backend load, with no change to query results.

If your setup depends on near-real-time metrics — dashboards, alerting on
freshness, anything reading data within seconds of collection — set
`flush_interval: 5s` (or your prior value) explicitly before upgrading.
Everyone else can upgrade without touching config.

Also in this release: an internal rewrite of the on-disk storage engine,
reducing memory churn during writes. No change to query results, file
format, or the public API. [Full changelog](url)
```

## Mailing list email (~900 subscribers)

```markdown
Subject: Halyard 2.9.0 — one default is changing (action may be needed)

Halyard 2.9.0 is out. One change needs your attention:

The default flush interval is moving from 5 seconds to 60 seconds. This
lowers the write load Halyard puts on small backends — the single biggest
source of overload reports we got this year. Most installs will simply see
metrics land up to a minute later than before.

If you rely on near-real-time metrics — fast alerting, live dashboards —
add `flush_interval: 5s` to your config before you upgrade to keep today's
behavior.

Everything else in this release is internal: we rewrote the on-disk storage
engine for lower memory overhead. Same query results, same file format,
same public API — nothing to change on your end.

[Full release notes](url)
```

## In-app banner (needs frontend team)

```markdown
Halyard 2.9.0: default metrics flush interval is now 60s (was 5s), to ease
load on small backends. Need the old cadence? Set `flush_interval: 5s`.
[Release notes]
```

---

## Traceability

| Entry | Source |
|---|---|
| `flush_interval` 5s → 60s | Your description — no PR/commit reference provided |
| Storage engine rewrite | Your description (~18k lines, 4 engineers, one quarter) — no PR/commit reference provided |

## Excluded

None — only these two changes were described. Not verified against a diff, so this isn't a claim that nothing else shipped in the range.

## Needs a human

1. No repo access this pass — run `collect-release-material.sh --from v2.8.x --to HEAD` (or paste the log) to confirm nothing else consumer-visible shipped before you publish.
2. Both entries need real PR/commit links — traceability gate isn't met yet.
3. Storage-engine entry has no memory number, stays qualitative. If you have a benchmark, add it — a real number could bump this to tier 3 (earns the hosted page too, still not email/banner).
4. Confirm actual ship date — `2026-09-18` is a placeholder.
5. Confirm with frontend whether the banner ships *with* 2.9.0. If not in time, drop that surface for this release rather than delay.
6. Worth a gut-check: does your own compat policy count "changes default behavior for everyone" as breaking? Nothing here rejects calls or removes anything, so minor (2.9.0) is defensible — flag if your policy disagrees.