# Docs versioning plan: Quillhaven

**Next action:** run one full 23-version build on a large runner with a raised Node heap (`NODE_OPTIONS=--max-old-space-size=8192`). Save the output as the snapshot source. About 25 minutes.

**Assumptions (ASSUMED, replace with real values):**
- Docs host is static and lets you merge a snapshot tree into the publish output, or route paths by CDN rule.
- No registry-hosted API reference. Config reference and API reference are versioned with the guides.
- Effort ceiling is one week of migration, then 2 hours per month standing.
- About 15 doc fixes per month.
- Build time scales roughly linearly with version count, about 55 seconds per version.
- Support for 2.x ends in March 2027.
- No CI capacity for a docs lint.

**Unvalidated sections:** all of them. I wrote the topology choice and every other section without your agreement.

## 1. Product class

- **Primary:** several supported lines with breaking differences. 3.x and 2.x are both supported, and the config format differs between them.
- **Secondary:** old lines unsupported but still installed. 1.x runs at air-gapped customers.
- Minors never broke an upgrade, so the 22 minors are not a docs axis. Majors are.

## 2. Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 3.x | current (3.4), built from main | until next major | `current` | `maintained` when 4.0 ships | released behaviour |
| 2.x | supported | March 2027 | `maintained` | `frozen` at support end | security, data loss, upgrade blockers |
| 1.x | unsupported, air-gapped use | ended | `frozen` | none while contracted customers run it | never |
| Minors 1.0 to 3.3 (22 releases in all, 3.4 is covered by 3.x) | released | n/a | static snapshot, listed on the archive index | none | never |
| Next | unreleased | n/a | removed as a separate build | n/a | n/a |

- **Granularity:** one live docs version per major. Minors are additive, so they get "added in 3.x" stamps, not pages.
- **Unversioned content:** blog, changelog, tutorials, concepts that never changed, community pages. Move them out of the versioned folders.
- **URL shape:** `current` lives at `/docs/3.x/`. `/docs/latest/` is a 302 alias to it. Use line segments (`3.x`, `2.x`), not releases.
- **Every old URL keeps working.** The snapshots serve `/docs/3.2/...` and the other old paths byte-identical. No consolidation redirects are needed for them.
- **Only two redirect sets are new:**
  - `/docs/next/*` and the current root `/docs/*` both redirect per page to `/docs/3.x/*`, with a 301.
  - If a page is missing in the target, fall back to its nearest ancestor section.
- **Components:** single component, so no compatibility matrix.

## 3. Topology

Brainstorming mode first, no pick yet.

**Deleted rungs:**
- **Cumulative badges:** no lint capacity, they rank last on durability, and the second line leaves in about 5 months.
- **Per-minor versions:** minors never broke an upgrade.

**Surviving options:**

| Option | Live versions | Cost | Verdict |
| --- | --- | --- | --- |
| A. Selector over 3.x and 2.x, snapshots for the rest | 2 | about 45 min/month backports | Recommended |
| B. Latest-only 3.x with stamps, 2.x frozen now | 1 | lowest | Rejected: 2.x readers are supported until March and need their own config pages |
| C. Per-major sites, each on its own host | 3 | backports plus a second deploy for 2.x | Rejected for supported 2.x. The snapshot step already does this job for unsupported lines. |

**Pick A.** In March it becomes B: 2.x freezes and the site runs latest-only with a 3.x stamps set plus frozen archives. Selector migration cost is mostly config, so it is cheaper than stamping every 2.x difference for 5 months.

**Why this keeps every version:** you asked to keep all versions. Freezing is not deleting. All 22 minors stay online at their original URLs. They just leave the build.

## 4. Source layout and release cut

**Layout:**
- `current` (3.x) builds from main. There is no separate Next build. Unreleased content carries "coming in 3.5" marks.
- 2.x lives in `versioned_docs`, backports edit it directly.
- Snapshots live outside the build, in a branch or bucket. The deploy step copies them into the publish output after the build.

**Docusaurus options** (verify against your version):
- `docs.onlyIncludeVersions`
- `docs.includeCurrentVersion`
- `docs.lastVersion`
- `docs.versions[v].{label,path,banner}`
- PR previews build `current` only, driven by an env var.

**Build cost** (ASSUMED linear): about 2 to 3 minutes, down from 21. Previews take about 1 minute. OOM goes away at 2 versions.

**Release cut checklist:**
1. Convert "coming in X" marks to "added in X".
2. Update the switcher.
3. Repoint the `latest` alias.
4. At 4.0, cut `3.x` into `versioned_docs`, mark it `maintained`, and start `4.x` from main.
5. Price the backports again.

**Snapshot caveats:**
- The snapshot HTML loads its own hashed assets. Test cross-version navigation and watch the console for hydration errors in a preview before going live.
- Snapshot navigation to the live site is a full page load. That is fine.
- If one big build runs out of memory, fall back to one build per slice.

## 5. Backport rule and price

- **Current in step:** 0, because `current` builds from main.
- **Maintained:** 15 fixes × 15% qualifying × 1 version × 20 minutes ≈ 45 minutes per month (baseline). That fits the 2 hour ceiling.
- **Rule:**
  - Backport released-behaviour fixes to `current`.
  - Backport to 2.x only for security, data loss, or upgrade blockers.
  - Never touch snapshots or 1.x.
- **Tagging:** tag backport targets in the PR at review time.
- **Check:** replace the 15 fixes, the 15%, and the 20 minutes with measured values after one month.

## 6. Reader routing

- **Default landing:** `current`, never Next.
- **Switcher:** three entries: 3.x (current), 2.x (maintained), and "Older versions", which links to the archive index.
- **Archive index:** lists all 22 minors, with 1.x prominent. Group by major.
- **Switching:** keep the same page, with ancestor fallback and a one-line notice.
- **Banners:** swizzle `DocVersionBanner` for state-specific wording.
  - 2.x: "This page documents 2.x, a supported older release. See this page for the latest release (3.4)."
  - 3.0 to 3.3 snapshots: "This page is a snapshot of 3.2. See this page for 3.x (3.4)."
  - 1.x: "1.x is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version (3.4)."
  - Add "insecure" only if known vulnerabilities exist.
- **Search:** scoped to the version being read, `current` by default.
- **Aliases:** link `/docs/latest/` from support replies, README, and blog posts.
- **AI feeds:** `llms.txt` covers `current` only.

## 7. Search-entry intent (handed to `docs-seo`)

I write intent only, no canonical tags.
- `3.x`: canonical target.
- `2.x`: own entry, or folded into 3.x, per the SEO posture.
- Minor snapshots: no own entry.
- `1.x`: no own entry by default.

## 8. Retirement procedure

1. **Trigger:** 2.x freezes at support end in March 2027.
2. **Snapshot:** snapshot 2.x as static output, swap to the frozen banner, and remove it from the build.
3. **Threshold** (baseline): under 1% of docs views and of downloads for two quarters.
4. **Air-gapped exception:** air-gapped usage never shows in web analytics or download counts. Do not archive or remove 1.x while any contracted customer runs it. Use your customer list as the evidence source.
5. **Announce** the freeze in the changelog and on the archive index.
6. **Removal** is last. If it ever happens, redirect per page to the nearest equivalent, never to the docs home.
7. **Repo cleanup:** delete the old `versioned_docs` only after the snapshots are verified in production. Tag the repo first (for example `docs-snapshot-2026-10`) so nothing is lost.

## 9. KPIs

| KPI | Baseline | Target |
| --- | --- | --- |
| Full build time | 21 min | under 5 min |
| CI OOM failures | 2 last month | 0 |
| PR preview time | 21 min | under 3 min |
| Versions built per deploy | 23 | 2, then 1 after March |
| Switcher 404s | unknown | 0 |
| Wrong-version tickets | unknown, count now | falling quarter on quarter |
| Per-version share of views | unknown | read each quarter against the threshold |

## Migration order

1. **Full build, once:** save the output as the snapshot source (about 25 min).
2. **Snapshot tree:** store it outside the repo build. Merge it into the publish output.
3. **Staging check:** click through snapshots, banners, and the archive index (about half a day).
4. **Move content:** blog and changelog to single unversioned locations.
5. **Config change:** cut the live build to 3.x plus 2.x, add the two redirect sets, and make previews `current`-only.
6. **Ship, verify, clean up:** go live, verify old deep links, then remove old `versioned_docs`.

Total: about 3 to 4 days (ASSUMED).

## Decisions needed from you

1. **Docs host:** which one, and can the deploy merge a snapshot tree into the output?
2. **Air-gapped bundle:** should I add a downloadable docs tarball per release for air-gapped 1.x customers? It reuses the snapshot and costs almost nothing.
3. **Doc-fix rate:** how many doc fixes land per month? That replaces my 15.

**Next:** answer decision 1, and I will refine step 2 of the migration.