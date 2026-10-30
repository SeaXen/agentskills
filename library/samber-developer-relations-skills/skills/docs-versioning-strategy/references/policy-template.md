# Docs versioning plan template

Load at Step 8 to write the deliverable.

## Template

```markdown
# Docs versioning plan - {product}

Assumptions: {ASSUMED items, or "none"}
Unvalidated sections: {sections written without the user's agreement, or "none"}

## Product class
Primary: {class} - because {signal}. Secondary: {class, or "none"}.

## Docs version policy table
| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |

Support ends: a date, or "until next major" when open-ended.
Unversioned content: {list}
Granularity: one docs version per {major | minor}, because {reason}.
URL shape: current at {unversioned path | versioned path + latest alias}; segments as {lines | releases}.
Consolidation redirects: {old URL pattern -> per-page target, or "none"}
Components: {which component drives the switcher; compatibility matrix page, or "single component"}

## Topology
Reference: {registry-hosted per release, linked | versioned with guides}.
Chosen guide rung: {rung}. Rejected: {rung - what eliminated it}, ...
Short-lived second line: {selector migration cost vs stamps plus early freeze, or "not applicable"}

## Source layout and release cut
Layout: {layout}. Built per deploy: {states}. Snapshots: {where}.
Release cut: old current -> {maintained | frozen}; alias moves; switcher and banners update; {next -> current | "coming in X" marks -> "added in X"}.

## Backport rule
Current in step: {fixes/month} × {share touching released behaviour} × {minutes}, or 0 when current builds from main.
Maintained: {fixes/month} × {share qualifying} × {maintained versions} × {minutes}.
Total: {hours/month} ({baseline | measured}).
Effort ceiling: {one-off} + {standing hours/month}. Fits: {yes | no -> action}.
Rule: current for released behaviour; maintained only for security, legal, data loss, upgrade blockers; frozen never.

## Reader routing
Default: current. Switcher fallback: nearest ancestor. Banners: {states}. Site search scope: {version being read}. Aliases linked from: {surfaces}. AI feeds: {scope}.

## Search-entry intent (handed to the docs SEO pass)
{one line per state}

## Retirement procedure
Trigger: {...}. Evidence threshold: {value} ({baseline | sourced}). Redirects: per page to nearest equivalent.

## KPIs
| KPI | Baseline | Target | Owner |
```

## Worked example

Input: an open-source HTTP client library. Supported lines: 3.x (current), 2.x (security fixes until next June). 1.x unsupported, still about 4% of downloads. Docs are one site rebuilt from main; a dropdown lists 1.0 through 3.2, eleven entries, all rebuilt on every deploy (14-minute build). About 12 doc fixes per month. 2.x to 3.x changed the configuration API. The package registry hosts per-release API reference.

Output, condensed:

- Class: primary "several supported lines with breaking differences", secondary "old lines unsupported but still installed".

| Version | Product status | Support ends | Docs state | Next transition | Backport? |
| --- | --- | --- | --- | --- | --- |
| 3.x | current (3.2) | until next major | `current` | `maintained` when 4.0 ships | released behaviour |
| 2.x | security fixes only (2.9) | June | `maintained` | `frozen` at support end | security, data loss, upgrade blockers |
| 1.x | unsupported, 4% downloads | ended | `frozen` | `archived` below 1% of views and downloads for two quarters | never |

- Granularity per major: 3.x minors are additive and carry "added in 3.x" stamps, so eleven entries collapse to `3.x`, `2.x`, `1.x`. No separate `next` build: `3.x` builds from main, and unreleased 3.3 content carries "coming in 3.3" marks. Consolidation redirects: `/3.0/*` to `/3.x/*` per page, likewise for 2.x and 1.x minors.
- Reference: registry-hosted per release, linked from every version. Guide topology: selector over one site, because two supported lines differ in configuration instructions. Latest-only rejected: 2.x users on security support need their own configuration pages. Re-check at June: once 2.x freezes, latest-only plus frozen archives may suffice.
- Short-lived second line: 2.x leaves support in June; a selector over two live lines costs one build-config change plus the redirect list, cheaper than stamping every 2.x difference.
- Layout: build `3.x` (from main) and `2.x` (release branch) per deploy; serve 1.x as a static snapshot.
- Backport cost: current in step 0 (built from main); maintained 12 × 15% × 1 × 20 minutes = about 36 minutes per month (baseline), inside a 2-hour standing ceiling. With a separate `next` build, keeping `3.x` in step would add about 4 hours and break the ceiling.
- Search-entry intent: `3.x` canonical target; `2.x` own entry or folded into `3.x` per the SEO posture; `1.x` own entry while downloads stay above threshold and the SEO posture allows it.
