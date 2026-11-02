# Docs versioning plan: Hollowmere

**Do this first:** don't delete `/1.x/` yet. Freeze it, keep the URLs live, and get your 6 minutes back that way. Delete only after the retirement evidence check below passes.

Assumptions (`ASSUMED`; I couldn't interview you, so correct any that are wrong):
- 2.x and 3.x instructions differ (config, API). 2.x support end date is unknown, treated as "until 4.0".
- 1.x docs views are unmeasured.
- Fix volume is 12 docs fixes per month. That figure is a baseline.
- Docs build from one site, so deleting the folder saves about 6 minutes per deploy.

Unvalidated sections: Topology and Backport rule. I wrote the choices without your agreement.

## Verdict on the request

Two parts of the request are right. Two are wrong.

- ✅ Take 1.x out of the per-deploy build. This fixes the 6-minute cost.
- ✅ Take 1.x out of site search. This fixes the search noise.
- ❌ "Nuke the folder." Deleting is the last state, not the first.
- ❌ One catch-all 301 from `/1.x/*` to `/docs/`. Every old page then lands on the docs home. The skill's rule is to redirect each page to its nearest current equivalent, never wholesale to the docs home. Also, a 301 is cached by browsers and search engines and is hard to undo.

## Why 3% blocks deletion

- **The "CI caches and bots" claim is unchecked.** It is an assumption. Verify it; don't build on it.
- **No project publishes a docs retirement threshold.** The skill sets a baseline: under 1% of docs views and of downloads for two quarters. 1.x downloads are at about 3%, three times over that bar. The threshold is not met.
- **The python-future precedent doesn't fit.**
  - It dropped Python 2.6 support (runtime support, not docs) at 0.04% of downloads.
  - Your 3% is about 75 times larger.
  - The precedent itself says it is only an analogous threshold. It says nothing about retiring docs.
- **The closer precedent is pandas.** It measured about 2% of views on old versions and kept them. One old line was downloaded more than newer ones, likely through a pinned dependency. Kubernetes, PostgreSQL, Python and Django also keep unsupported lines online behind a banner.
- **Pinned dependents would break.** If crates depending on `hollowmere = "1"` exist, their users hit 404s or the docs home.

## Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 3.x | current | until next major | `current` | `maintained` when 4.0 ships | yes, released behaviour |
| 2.x | supported | ASSUMED until 4.0 | `maintained` | `frozen` at support end | security, legal, data loss, upgrade blockers only |
| 1.x | unsupported 26 months, about 3% downloads | ended | `frozen` | `archived` when under 1% of views and downloads for two quarters (baseline); `removed` when no measurable readers | never |

- **Granularity:** one docs version per major. 3.x minors carry "added in 3.x" stamps.
- **Unversioned content:** tutorials that haven't changed, concepts, changelog, blog, community pages.
- **URL shape:** versioned line paths (`/3.x/`, `/2.x/`, `/1.x/`) behind a `latest` alias. `/1.x/` stays where it is.
- **Consolidation redirects:** none now.

## Topology (ASSUMED, unvalidated)

I rejected the other rungs for these reasons:

- **Latest-only with stamps:** rejected because 2.x is a supported line with different instructions.
- **Cumulative badges:** rejected because there is no lint capacity on record, and an untagged change silently misleads old-line readers.
- **Selector over 3.x and 2.x:** chosen.
- **Per-major frozen for 1.x:** chosen, because 1.x is unsupported.

The API reference stays on docs.rs, which generates it per release from the crate. Link it from every version and version only the guides. Confirm docs.rs covers 1.x releases.

## Source layout and release cut

1. Build 3.x (from main) and 2.x (release branch) on each deploy.
2. Serve 1.x as a prebuilt static snapshot at `/1.x/`. This is the 6-minute saving. Frozen builds never rebreak on toolchain upgrades.
3. At the 4.0 cut:
   - 3.x becomes `maintained`.
   - The `latest` alias moves.
   - The switcher and banners update.
   - "Coming in 4.0" marks become "added in 4.0".

## Backport rule (ASSUMED, unvalidated)

- **Keeping `current` in step:** 0 hours, because 3.x builds from main.
- **Maintained backports:** 12 fixes × 15% qualifying × 1 maintained version × 20 minutes = about 36 minutes per month (baseline). Replace the inputs after one month of real data.
- **Rule:** `current` gets every fix to released behaviour. `maintained` gets security, legal, data loss, and upgrade blockers only. `frozen` is never fixed.
- Tag each docs PR with its backport targets at review time, not after merge.

## Reader routing

- **Default landing:** 3.x.
- **Switching:** keeps the same page. If the page is missing in the target version, open the nearest ancestor section and say so.
- **Aliases:** README, support replies and blog posts link to `latest`, not a numbered version.
- **Site search:** scoped to the version being read, 3.x by default. 1.x pages are searchable only from 1.x pages and the "Older versions" link. This fixes the search noise.
- **1.x banner** (frozen template): "1.x is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version (3.x)." Add "has known security issues" only if 1.x has known vulnerabilities.
- **AI feeds** (`llms.txt` and similar): 3.x only.

## Search-entry intent (handed to the docs-seo pass)

- 3.x is the canonical target.
- 2.x gets its own entry, or is folded into 3.x, per the SEO posture.
- 1.x gets no search entry from site search. For web search, it keeps an entry only while downloads stay above the threshold and the SEO posture allows it. docs-seo writes the canonical tags and the redirect mechanics.

## Retirement procedure for 1.x

1. **Now, frozen:** snapshot 1.x as static output, add the banner, remove it from the build and from site search.
2. **Evidence check each quarter:** 1.x share of docs views and of crates.io downloads. The threshold is under 1% of both for two quarters (baseline; replace with your own).
3. **Archived when the threshold holds:** drop 1.x from the switcher and list it on an archive index page.
4. **Removed only with no measurable readers:**
   - Redirect each 1.x page to its nearest 3.x equivalent. docs-seo owns the map.
   - Use a catch-all to the 3.x docs root only for pages with no equivalent.
   - Use 302 until the map is checked, then switch to 301.
5. **Announce:** note the freeze and the later retirement in the changelog and on the archive index.

## KPIs

| KPI | Target (baseline) |
| --- | --- |
| Full build time | down about 6 minutes after the freeze, with no growth at each release cut |
| 1.x share of docs views and downloads | read each quarter against the 1% threshold |
| Wrong-version arrivals from search or AI referrals | falling quarter on quarter |
| Switcher 404s and wrong-version tickets | zero 404s, tickets falling |
| Backport hours per month | within the 36-minute estimate |

## Verify the "CI and bots" assumption

Before you act on the 3% figure either way:

1. Pull the crates.io per-version download series for 1.x. Look for flat, weekday-independent volume (CI or mirrors) versus declining organic volume.
2. List reverse dependencies that pin `hollowmere = "1"`. A popular pinning crate means real readers. This is the pandas pattern.
3. Pull 1.x docs page views and referrers from your analytics.

If dependents are few and views are under 1%, start the two-quarter clock now. Retirement then follows the procedure above, with per-page redirects.

**Next action:** open the crates.io versions page for Hollowmere and read the 1.x download numbers. About 5 minutes.