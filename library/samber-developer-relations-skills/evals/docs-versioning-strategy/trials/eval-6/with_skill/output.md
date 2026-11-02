# Docs versioning plan - Larkspur

**Answer:** Version the docs on one axis, the API date. Don't build the API date × SDK version picker, and don't rewrite tutorials per pair. SDK versions get a compatibility page, since-stamps and language tabs instead. They don't get their own docs versions.

**Assumptions** (`ASSUMED`, none confirmed with you):
1. Each SDK major targets or defaults to one or more API dates, and a compatibility table can be written from that.
2. Per-date OpenAPI specs exist, or can be recovered, for 2024-02-01, 2024-10-15 and 2025-06-01.
3. A dated version has a published sunset date. I don't know the dates for the three live versions.
4. The docs are English only, and there is no separate `next` build.
5. The team fixes about 20 docs pages a month.
6. The effort ceiling is 1 week one-off and 8 hours a month standing.
7. Each SDK has about 2 live majors.
8. There's no docs-view or API-request data per version yet.

**Unvalidated sections:** all of them. Product class, policy table, topology, layout, backport rule, routing, retirement and KPIs were written without your agreement.

## Product class

**Primary:** hosted API, several callable versions. Clients pin a dated version per account, and three are callable now.

**Secondary:** the SDKs are libraries with registry-generated reference, so they add nothing to the versioning axis. Sunset API versions are "unsupported" but not callable. Nobody can call them, so they get an archive entry and no live docs.

The selector is capped at the API's concurrent-version count, which is 3. The SDKs don't raise that cap, because a customer can't call an SDK version the way they call an API date.

## Why not the full matrix

| Option | Doc sets | Cost |
| --- | --- | --- |
| Date × SDK version, tutorials per pair | 3 dates × 4 SDKs × 2 majors = 24 (ASSUMED), more if per minor | About 12 tutorials × 24 = 288 pages (ASSUMED) for two writers |
| Date only (recommended) | 3 | Shared guides with a few date variants |

- Docusaurus maintainers advise staying under about 10 versions (sourced). 24 is already over that.
- SDK versions are mostly additive. Each SDK has its own changelog and migration guide, and the registry already generates its reference.
- The pair your customer cares about, "Python SDK 3.2 against 2024-10-15", is answered with these parts:
  - **Date picker:** shows 2024-10-15 behaviour.
  - **Language tab:** shows Python.
  - **"Requires SDK ≥ x.y" stamps:** on every sample that depends on a newer SDK.
  - **Compatibility lookup:** the user picks an SDK and version and gets the API dates it supports, with links to the matching docs.
- To product: the picker covers everything. It does it with one version axis plus a lookup, not a pile of 24 sites.

## Docs version policy table

Support-end dates are `ASSUMED`. Replace them with the real sunset dates.

| Version | Product status | Sunset | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 2025-06-01 | Newest callable | Sunset window opens when a newer date ships | `current` | `maintained` when the next date ships | Released behaviour |
| 2024-10-15 | Callable | ASSUMED, ask | `maintained` | `frozen` at its sunset date | Security, legal, data loss, upgrade blockers |
| 2024-02-01 | Callable | ASSUMED, ask | `maintained` | `frozen` at its sunset date | Same |
| Older dates | Sunset, not callable | Ended | `archived`: changelog and upgrade guide only | `removed` after the evidence check | Never |

- **Granularity:** one docs version per dated API version, because each date is a breaking line. Never per SDK release, SDK major or patch.
- **Unversioned content:**
  - Concepts that never changed.
  - Tutorials, except pages on the date-variant list.
  - Changelog and blog.
  - SDK install and usage pages.
  - Community pages.
- **URL shape:** `current` at a versioned path, `/docs/2025-06-01/`, behind a `/docs/latest/` alias. Segments are dates (lines), not SDK releases. Support replies, the README and the blog link to `latest`.
- **Consolidation redirects:** none, since nothing is being collapsed. Sunset-date docs that already exist get a per-page redirect to the nearest current page when archived.
- **Components:** the API date drives the picker. SDK versions don't. A compatibility matrix page lists SDK × version → supported API dates. Treat the first row of each SDK as authoritative, written with the SDK's release notes.
- **Short-lived line:** if 2024-02-01 sunsets within about two releases, skip building its variants. Use stamps and an early freeze, and compare the cost before deciding.

## Topology

- **Reference:**
  - API reference is versioned per date, generated from each date's spec, with three outputs.
  - SDK reference stays on the package registries. Link it from every version's pages and don't version it on the docs site.
- **Chosen guide rung:** latest-only guides with stamps ("added in", "changed in", "removed in" an API date), plus a small inventory of date-variant pages.
  - **Variant pages:** only pages whose steps differ by date. The picker serves the variant for that date; other pages are shared. Identify them with `developer-docs-structure-audit` before building any.
  - **Upgrade guides:** one per date step, written with `version-migration-guide`.
  - **Changelog:** carries the history, via `changelog-writing`.
- **Rejected:**
  - **Selector over all guides:** each live date's backports multiply across every page.
  - **Cumulative badges:** needs a lint for untagged changes and you may have no CI capacity. One untagged change misleads old-date readers.
  - **Per-major frozen sites:** dated APIs don't have majors. Frozen sites fit the archived dates only.
- **Re-rank trigger:** pinned readers (account-level pin) promote the selector. That is why variant pages exist. If tickets show readers on old dates failing on shared guides, grow the variant list page by page.

## Source layout and release cut

- **Layout:** version folders in one branch. That fits three live versions and a small docs set. The reference folders are generated, so only guides and variants are hand-written.
- **Built per deploy:** `current` and both `maintained` dates. Frozen and archived dates are static snapshots, not rebuilt.
- **Release cut:** when a new date ships:
  1. The old `current` becomes `maintained`.
  2. The `latest` alias moves.
  3. The picker and banners update.
  4. "Coming in {date}" marks become "added in {date}".
  5. The upgrade guide and changelog entry publish.
  6. The oldest date past its sunset leaves the build as a static snapshot.
- Add the cut to the release checklist.

## Backport rule

- **Current in step:** 0, because `current` builds from main with no separate `next`. Unreleased content carries "coming in {date}" marks.
- **Maintained:** 20 fixes × 15% qualifying × 2 maintained dates × 20 minutes = about 2 hours a month. Fixes and shares are baseline, replace them after one month.
- **Effort ceiling:** 1 week one-off plus 8 standing hours a month (ASSUMED). The plan fits: about 2 hours of backports plus the release cut.
- **Rule:**
  - Backport to `current` every fix touching released behaviour.
  - Backport to `maintained` dates only for security, legal exposure, data loss, or an upgrade blocker.
  - Never fix `frozen` or `archived`.
  - Tag each docs PR with backport targets at review.

## Reader routing

- **Default landing:** `current`.
- **Switcher:** keeps the same page. If the page is missing in the target date, it opens the nearest ancestor with a one-line notice.
- **Banners:** every non-current page carries one, with status, consequence and a link to the same page in `current`.
  - Maintained: "This page documents API version 2024-10-15, a supported older version. See this page for the latest version (2025-06-01)."
  - Frozen: "API version 2024-02-01 is sunset and this page is a static snapshot. Upgrade, and see this page for the current version."
- **Site search:** scoped to the version being read.
- **AI feeds:** `llms.txt`-style feeds cover `current` only.
- **Logged-in preselect (optional, later):** a logged-in dashboard user could land on their account's pinned date. Stripe tailors its reference per account (sourced). It needs engineering, so keep it out of v1.
- **Aliases linked from:** support replies, the README, blog posts and SDK READMEs.

## Search-entry intent (for `docs-seo`)

- **current:** canonical target.
- **maintained:** own entry or folded into `current`, per the SEO posture.
- **frozen:** own entry only while request volume stays above the threshold and the SEO posture allows it.
- **archived:** none.

## Retirement procedure

1. **Trigger:** the contractual sunset date, which moves `maintained` to `frozen`. No traffic threshold is needed for that step.
2. **Snapshot:** save the version as static output, swap the banner, remove it from builds.
3. **Evidence check (baseline):** move `frozen` to `archived` when accounts pinned to that date and API requests under it stay below 1% for two quarters. Request volume by pinned date from the gateway beats docs views, since the API logs show real use.
4. **Removal:** only with no measurable readers. Redirect each page to its nearest current equivalent, never to the docs home.
5. **Announce:** post each retirement in the changelog and on the archive index.

## KPIs

| KPI | Baseline | Target | Owner |
| --- | --- | --- | --- |
| Wrong-version arrivals from search or AI referrals | Measure first | Falling each quarter | Writer 1 |
| Backport hours a month | About 2 (baseline) | Within the estimate | Writer 2 |
| Build time and versions built per deploy | Measure first | No growth at each release cut | Writer 2 |
| Per-date share of docs views and API requests | Measure first | Read each quarter against the 1% threshold | Writer 1 |
| Switcher 404s and "wrong version" tickets | Measure first | Zero 404s, falling tickets | Writer 1 |

## Next steps

1. Answer the open assumptions: SDK-to-date mapping, sunset dates, per-date specs, fixes a month, ceiling.
2. Run the docs structure audit to find the date-variant page list.
3. Build the compatibility matrix and lookup page.
4. Generate the three reference sets and the picker.

Each step can be reviewed separately.