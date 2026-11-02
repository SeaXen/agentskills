**Verdict:** don't delete 3.x or 2.x this sprint, and don't 301 them to the 4.x home page. Freeze them as static snapshots instead. Your writer then touches only 4.x, which is the relief you want, and no reader loses a page.

**Do this first:** look up 2.x's download share (pepy.tech shows per-version numbers). It takes about 2 minutes and sets 2.x's end state.

## Docs versioning plan - Marlinspike

**Assumptions (ASSUMED, correct me):**
- "Until next November" means Nov 2027. If it means Nov 2026, 3.x leaves support in about 3 weeks. See the note below the table.
- Every section below is unvalidated, because I wrote the plan without your sign-off on each part.
- The docs build from one branch and 4.x builds from main. There is no separate `next` build.
- URLs use line segments (`/3.x/`). The docs tool can build from a release branch.
- 3.x differs from 4.x in instructions, since it is a major.
- You get about 10 doc fixes a month and a standing ceiling of about 2 hours a month.
- No 2.x download figure yet.

### Product class
- **Primary:** several supported lines with breaking differences (4.x current, 3.x LTS).
- **Secondary:** old lines unsupported but still installed. 2.x certainly qualifies. 3.x qualifies after support ends, since the web framework pins it.

### Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 4.x | current (4.6) | until next major | `current`, built from main | `maintained` when 5.0 ships | released behaviour |
| 3.x | LTS, security fixes | Nov 2027 (ASSUMED) | `maintained`, static snapshot | `frozen` at support end | security, data loss, upgrade blockers only |
| 2.x | unsupported | ended 2 years ago | `frozen`, static snapshot | `archived` when under 1% of views and downloads for two quarters (baseline) | never |

- **Unversioned content:** changelog, blog, tutorials and concepts that never changed.
- **Granularity:** one docs version per major. Patches fix code, not instructions.
- **URL shape:** keep the current `/N.x/` paths. Add a `latest` alias for 4.x, and link support replies and the README to it.
- **Consolidation redirects:** none this sprint. Old URLs stay live, so nothing breaks.
- **Components:** single component.
- **If support ends Nov 2026:** 3.x goes straight to `frozen` with the "unsupported" banner. This sprint's work is identical, and only the banner text and the state label differ.

### Why not your plan
- **Docs window narrower than support window.** 3.x gets security fixes for a year. Deleting its docs strands supported users.
- **Pinned readers.** 38% of downloads are on 3.x because a large framework pins it. Those readers cannot upgrade, so "read the changelog" does not help them. pandas had the same shape: about 2% of views on old versions, and one old line downloaded more than newer ones. The maintainers kept the docs.
- **Views understate need.** 2% of views against 38% of downloads is the gap to watch. Downloads decide retirement, not views.
- **Wholesale 301 to the 4.x home page.** The skill says to redirect each page to its nearest current equivalent, never to the docs home. Mass redirects to a home page also look like soft 404s to search engines. Redirects wait until `removed`, and the redirect map goes to the `docs-seo` pass.
- **Delete last.** The order is freeze, banner, redirect, then delete.

### Topology
- **API reference:** your docs host generates it per release. Link it from every version and version only the guides. (ASSUMED: if not, 3.x reference gets frozen into the snapshot.)
- **Chosen rung:** latest-only guides with "added in / changed in" stamps for 4.x, plus frozen or maintained static snapshots of older majors. This is the skill's recommended default.
- **Rejected: selector over a live 3.x build.** It costs backports plus a build for every deploy. It is overkill when 3.x only needs security and blocker fixes.
- **Rejected: cumulative badges.** They need a lint and rank worst on durability.
- **Rejected: delete now.** Pinned readers and the support window rule it out.
- **Short-lived second line:** if 3.x ends Nov 2026, stamps plus early freeze beat any selector migration.

### Source layout and release cut
- **Layout:** branch or tag per version. Build 3.x and 2.x once from their release branches into static output, and serve them at their current paths.
- **Deploy:** the main build contains 4.x only. The 3.x snapshot rebuilds only on a qualifying backport.
- **Release cut at 5.0:** 4.x becomes `maintained`, the `latest` alias moves, the switcher and banners update, and "coming in 5.0" marks become "added in 5.0".

### Backport rule
- **Current in step:** 0, because 4.x builds from main.
- **Maintained:** 10 fixes × 15% × 1 version × 20 min = about 30 min/month (baseline). Replace the 10 with your real count after one month.
- **Ceiling:** one sprint one-off plus 2 h/month standing (ASSUMED). It fits.
- **Rule:** 4.x gets every fix for released behaviour. 3.x gets security, legal, data loss and upgrade blockers only. 2.x gets nothing. Tag each doc PR with its backport targets at review time.

### Reader routing
- **Default landing:** 4.x.
- **Switcher:** 4.x and 3.x are listed with support status. 2.x sits under "Older versions". Switching keeps the page, with a nearest-ancestor fallback and a one-line notice.
- **Search:** scoped to the version being read. 2.x pages are searchable only from their own pages.
- **AI feeds** (`llms.txt`): 4.x only.
- **Banners:**
  - 3.x: "This page documents 3.x, a supported older release. See this page for the latest release (4.6)."
  - 2.x: "2.x is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version (4.6)." Add "has known security issues" only if 2.x has known CVEs.
- **Upgrade path:** write a 3.x → 4.x upgrade guide with `version-migration-guide`. The changelog stays as history, but it is not an upgrade path.

### Search-entry intent (handed to `docs-seo`)
- 4.x is the canonical target.
- 3.x gets its own entry while it is maintained.
- 2.x gets its own entry only while downloads stay above the threshold, and only if the SEO posture allows it.

### Retirement procedure
1. **Trigger:** 3.x → `frozen` at support end. 2.x → `archived` when the threshold holds.
2. **Evidence:** per-version page views and PyPI downloads. The threshold is under 1% of both for two quarters (baseline; no project publishes one). 3.x at 38% will not hit it soon.
3. **Archive:** drop it from the switcher and list it on an archive index.
4. **Remove:** only when no measurable readers remain. Redirect per page to the nearest 4.x equivalent, and announce it in the changelog.

### KPIs

| KPI | Target |
| --- | --- |
| Backport hours per month | at or under 0.5 h (baseline) |
| Full build time | no growth at each release cut |
| Wrong-version arrivals from search or AI | falling quarter on quarter |
| Switcher 404s | zero |
| Per-version share of views and downloads | reviewed each quarter against the threshold |

### Sprint checklist
1. Build static snapshots of 3.x and 2.x from their release branches. About 2–4 h each, depending on your docs tool.
2. Remove both from the main build and serve the snapshots at the same paths.
3. Add the banners above.
4. Trim the dropdown: 4.x and 3.x listed, 2.x under "Older versions".
5. Add the backport rule to the contributing guide and the release checklist.

Steps 1–5 take about 1–2 days (estimate, depends on your docs tool). The standing cost afterwards is about 30 min/month.

**Two questions that change this plan:**
1. Is "next November" 2026 or 2027?
2. What is 2.x's download share?