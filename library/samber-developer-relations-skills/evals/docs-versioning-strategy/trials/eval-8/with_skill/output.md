# Docs versioning plan: Ashgrove TypeScript SDK

**Do not build branch-per-version this Saturday.** Do the URL flatten and inline 2.x tabs on the dozen pages that differ. Freeze 2.x as a static snapshot when support ends. I couldn't ask you the interview questions, so every sourced fact below is marked as sourced, baseline or `ASSUMED`. The topology and the URL shape are my recommendation, not something you've agreed to.

## Assumptions (correct any of these)

- `ASSUMED` 2.x support ends about **2026-12-04** (six weeks from today). Replace it with the real date.
- `ASSUMED` The payments API has one callable behaviour. Only the SDK differs between 2.x and 3.x.
- `ASSUMED` 3.1 to 3.2 is additive, with no instruction changes.
- `ASSUMED` The docs have no lint capacity in CI.
- `ASSUMED` No customer is contractually pinned to 2.x. **This is the assumption most likely to flip the plan.**
- `ASSUMED` The docs host is Docusaurus-like and supports tabs and redirects. I don't know the tool, so the steps are generic.
- `ASSUMED` TypeDoc or registry reference exists per release.
- Unknown: page views per version path, npm downloads per version, and doc fixes per month.

Unvalidated sections: all of them.

## Product class

- **Primary:** several supported lines with breaking differences. Both 2.x and 3.x are supported, and init and error types differ.
- **Secondary:** old lines unsupported but still installed. This applies from the freeze date. An SDK pinned in a lockfile keeps 2.x installed long after support ends.

## Why not your plan

Your plan is a selector over one docs set per supported line, built with branch-per-version.

- **Your ceiling kills it.** A one-afternoon budget deletes source-layout migrations. Branch-per-version is one.
- **The second line is short-lived.** 2.x leaves support within about two releases. The skill says to compare the selector migration with stamps plus an early freeze, and pick the cheaper.
- **The cost is lopsided (baseline).**

  | Option | One-off cost | Standing cost |
  | --- | --- | --- |
  | Selector | 1 to 2 days: branch layout, two-version build, switcher, banners, redirects, 3.2 release cut | About 36 minutes a month of backports |
  | Stamps + tabs | About 4 hours | About 0 |

  The standing cost for the selector comes from 12 fixes a month × 15% qualifying × 1 maintained version × 20 minutes. Tabs live on main, so they need no backports.
- **You'd rebuild it in December.** When 2.x freezes, the selector collapses back to one live set plus an archive. You would build the layout, then take it apart.
- **"Like the big SDKs" doesn't match your situation.** React, Stripe and Kubernetes run long-lived parallel lines. Vue froze Vue 2 on its own host because two parallel majors weren't sustainable. That is your situation.

### Topologies considered

| | Topology | Verdict |
| --- | --- | --- |
| A | Latest-only with stamps, inline 2.x variants on about 12 pages, then a frozen 2.x snapshot | **Recommended.** About 4 hours now, about 1 hour in December. |
| B | Selector with branch-per-version (your plan) | Cost is higher than A. The layout disappears when 2.x leaves support. |
| C | 2.x on its own static host now | Rejected. A supported major on its own host costs B's backports plus a second deploy. |

Rejected rungs:
- **Cumulative badges:** no lint capacity (`ASSUMED`). One untagged change would silently mislead 2.x readers.

**What flips this to B:**
- Customers are contractually pinned to 2.x.
- 2.x support is extended past about one more release.
- A 4.0 or docs redesign lands within a quarter.

If any of these is true, tell me and I'll re-rank.

## Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 3.x | Current (3.1, 3.2 in about 6 weeks) | Until next major | `current`, built from main | `maintained` when 4.0 ships | Released behaviour |
| 2.x | Supported | About 2026-12-04 (`ASSUMED`) | `maintained` as tabs on the current pages | `frozen` at support end, as a static snapshot at `/docs/2.x/` | Security, data loss, upgrade blockers only |

- **Granularity:** one docs version per major. Minors are additive and carry "added in" stamps.
- **Unversioned content:** tutorials, concepts, changelog, blog, community pages.
- **Components:** the SDK version drives the choice. The API has a single behaviour, so no compatibility matrix is needed.
- **Reference:** link the generated per-release API reference from every page and don't version it.

### URL shape

- `/docs/` is `current`, with line segments (`/docs/2.x/`) rather than releases (`/docs/3.1/`).
- Dropping the release number fixes your confusion. It also means 3.2 needs no URL change.
- **Trade-off:** an unversioned path is only safe with one supported line plus latest-only docs. That is true from the freeze date. Before then, the tabs bridge it.
- **When 4.0 ships,** `/docs/` silently changes meaning. Freeze 3.x to `/docs/3.x/` in the same release cut.
- **Safer alternative:** `/docs/3.x/` behind a `/docs/latest/` alias. Tell me if you want it. Otherwise I'll proceed with `/docs/`.

## Saturday walkthrough (about 4 hours)

**Block 0, preflight (15 min)**

1. Pull page views for `/docs/3.1/*` and npm downloads per version for 2.x. This gives you real numbers for the retirement threshold.
2. Tag the current state: **`git tag docs-pre-flatten`**. It is your rollback point and the base for the December snapshot.

**Block 1, flatten the URL (60 min)**

3. **Move** the content from `/docs/3.1/` to `/docs/`. Use `git mv` and keep the page paths identical apart from the dropped `3.1/` segment.
4. **Add a permanent 301** from `/docs/3.1/:path*` to `/docs/:path*`, per page and never to the docs home.
5. Keep that redirect forever. Published SDK error messages, the npm README and old blog posts link to `/docs/3.1/...`, and you can't edit what is already published.
6. Update internal links, the nav, the sitemap, search index config, analytics path filters, and any "3.1" in page text. Use "3.x" or an "added in" stamp for page text.
7. Update the README, support macros and the SDK's own links to the new path.
8. Hand the redirect list and canonical posture to the docs SEO pass (`docs-seo`). Intent: `/docs/` is the canonical target, and 2.x gets no search entry of its own.

**Block 2, the 2.x tabs on about 12 pages (90 min)**

9. Find the pages: grep for the old client init and the 2.x error class names. Your count is "maybe a dozen", so list them before editing.
10. On each page, add a `3.x | 2.x` tab pair around **only the diverging code** (init and error handling). Default to 3.x. Keep the prose single.
11. Add a stamp "Changed in 3.0" on those blocks.
12. Mark any 3.2 content on main as "coming in 3.2". Main feeds `current`, so unreleased content would otherwise read as installable.

**Block 3, notices and policy (30 min)**

13. Add a site notice: "2.x support ends {date}. See the 2.x to 3.x migration guide."
14. Write the policy table above into `docs/VERSIONING.md`.
15. Add the release cut to the release checklist: "coming in 3.2" becomes "added in 3.2".

**Block 4, verify (45 min)**

16. Run the redirect check on every old URL. Expect 301 with the right `Location`, then 200 on the target.
17. Add a positive control and a failing case. Check that a known-good URL returns 200 and a made-up `/docs/3.1/nope` returns exactly 404. A check that can't fail proves nothing.
18. Run a link crawl and scan for remaining "3.1" strings.

### Deferred, not Saturday

- **2.x to 3.x migration guide:** every tab links to it. If none exists, draft it with `version-migration-guide`, covering init and error types with before/after code and a detection signal. About 1 hour.

## Backport rule

- **Current in step with main:** 0. Main builds `current`, and the tabs sit on main.
- **Maintained (2.x):** 2.x tab content changes only for security, legal, data loss, or an upgrade blocker. This is 0 extra backports because the tabs are on main.
- **Frozen:** never fixed.
- **Total:** about 0 extra hours a month (baseline). That fits any standing ceiling.
- Tag every doc PR with its target at review time.

## Reader routing

- **Default:** `current` at `/docs/`.
- **No switcher.** Each tab links to the migration guide. After the freeze, an "Older versions" link in the footer points to `/docs/2.x/`.
- **Search:** scoped to `current`. The 2.x snapshot is searchable only from its own pages.
- **Aliases:** link `/docs/` from support replies, the README and blog posts.
- **AI feeds:** `llms.txt` on `current` only.

## Release cut and retirement (about 2026-12-04, about 1 hour)

1. Release cut for 3.2: "coming in 3.2" becomes "added in 3.2".
2. Evidence check: 2.x page views and downloads against the retirement threshold.
3. Build the tabbed site once to static output at `/docs/2.x/`. If your tab component allows it, set 2.x as the default tab. Never rebuild it afterwards.
4. Add the frozen banner: "2.x is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version (3.x)." Link to the same page in `current`. Say "insecure" only if known vulnerabilities exist.
5. Remove the tabs from main and replace them with "Changed in 3.0" stamps plus the migration link.
6. Announce the retirement in the changelog.
7. Move 2.x to `archived` when views and downloads stay under **1% for two quarters** (baseline, replace with your own threshold). Remove it only when no readers remain, and redirect per page.

## Search-entry intent (for the docs SEO pass)

- `current` (`/docs/`): the canonical target.
- `maintained` 2.x: folded into `current`.
- `frozen` 2.x: no own entry unless downloads stay high.
- `archived`: none.

## KPIs

| KPI | Target |
| --- | --- |
| Wrong-version arrivals (sessions landing on 2.x content from search or AI) | Falling quarter on quarter |
| Redirect 404s after Saturday | Zero |
| "Wrong version" support tickets | Falling |
| Backport hours per month | About 0 |
| 2.x share of views and downloads | Read each quarter against the 1% threshold |

## Next step

Run Block 0 now (about 15 minutes) and send me three answers:
1. Are any customers contractually pinned to 2.x?
2. What is the real 2.x support end date?
3. Which docs tool do you use?

Question 1 is the one that could flip this plan to B.