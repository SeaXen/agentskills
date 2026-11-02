**Next action:** time a build with only `current` + `3.4`, then record a URL baseline. Both take about 30 minutes and change nothing public.

## Plan at a glance

Keep all 23 versions and every URL. Build less often and with fewer versions per build.

1. **Phase 0, 30 min:** baseline URLs and timings.
2. **Phase 1, about 1 h:** small PR previews. This fixes the OOM and the per-PR cost.
3. **Phase 2, about half a day:** unversion blog and changelog. This is the biggest cut in page count.
4. **Phase 3, 1–2 days, optional:** build frozen majors once. Decide after phase 2.
5. **Separate decision:** what `/docs/` root shows publicly.

Minors never broke upgrades, so the dropdown grouping and archive boundaries follow majors: 1.x, 2.x, 3.x.

## Phase 0: baseline (30 min)

1. Save every live URL before you touch anything:

```bash
curl -s https://<docs-host>/sitemap.xml | grep -oE '<loc>[^<]+' | sed 's/<loc>//' > urls-baseline.txt
```

2. Add URLs from GitHub issues, since they may not be in the sitemap. Grep issue bodies fetched with `gh issue list --json body` for your docs host, and append the results. Support tickets need a manual export.
3. Do this before any `noIndex` change. `noIndex` versions drop out of the sitemap.
4. Time the full build and its peak memory, then time the reduced build from phase 1. Per-version cost is roughly build time divided by 23, but blog and changelog inflate it. Measure, don't trust that.

Guard script, to run in CI against each preview or deploy:

```bash
while read -r u; do
  code=$(curl -s -o /dev/null -L -w '%{http_code}' "$u")
  [ "$code" = 200 ] || echo "$code $u"
done < urls-baseline.txt
```

Any output means a broken deep link. Swap the host for the preview host first.

## Phase 1: small PR previews (about 1 h)

Preview builds need only the versions the PR touches.

```ts
// docusaurus.config.ts
const PROFILE = process.env.SITE_PROFILE ?? 'live';

// Previews build only what a PR can change; archives are never edited in PRs.
const PREVIEW_VERSIONS = ['current', '3.4'];

docs: {
  onlyIncludeVersions: PROFILE === 'preview' ? PREVIEW_VERSIONS : undefined,
}
```

1. Set `SITE_PROFILE=preview` in the PR workflow only.
2. Set `onBrokenLinks: 'warn'` for the preview profile. A link from 3.4 into an excluded version otherwise fails the build.
3. Add `NODE_OPTIONS=--max-old-space-size=<n>` sized to the runner. Check for a runner with more RAM.
4. Try `DOCUSAURUS_SSR_CONCURRENCY=<small n>`. It lowers peak memory at some speed cost.
5. Try `future: { experimental_faster: true }` (Rspack). It needs Docusaurus 3.6 or later, so verify your version first.
6. Cache `node_modules/.cache` and `.docusaurus` in CI.

Production URLs are untouched in this phase.

## Phase 2: unversion blog and changelog (about half a day)

Versioning them was convenience. It multiplies those pages by 23 for no reader benefit.

1. Spot-check that the versioned blog and changelog copies are identical to, or a subset of, the latest. Diff 3 or 4 versions.
2. Move the blog to the blog plugin. Move the changelog to a second docs instance, unversioned:

```ts
[
  '@docusaurus/plugin-content-docs',
  { id: 'changelog', path: 'changelog', routeBasePath: 'changelog', sidebarPath: './sidebarsChangelog.ts' },
],
```

3. Keep every old URL alive. `@docusaurus/plugin-client-redirects` works on any static host, with no rule limits:

```ts
[
  '@docusaurus/plugin-client-redirects',
  {
    createRedirects(existingPath) {
      if (!existingPath.startsWith('/changelog/')) return undefined;
      // One stub per old versioned path; slugs must stay identical.
      return ALL_VERSIONS.map((v) => existingPath.replace('/changelog/', `/docs/${v}/changelog/`));
    },
  },
],
```

Repeat the same shape for blog paths.

4. Keep the slugs identical. Run the guard script. Every old URL must now return 200 through a redirect.
5. Delete the versioned copies only after the guard passes. Use `git mv` for moves and `git rm` for removal, so history stays.
6. Client redirects are meta-refresh, not a 301. If your host supports edge redirects, generate a 301 map from the same list later. Check the host's rule limits first.

Expected effect: a large cut in page count. Re-time the full build here.

**Stop point.** Production builds only on merge to main, and the PR pain is already fixed. If the full build is now under about 8–10 minutes and fits in memory, skip phase 3.

## Phase 3: build frozen majors once (optional)

Frozen versions never change, so build them once and reuse the output.

1. Define profiles, one per major plus live:
   - `live`: Next + 3.0–3.4 (6 of 23 versions, roughly 26% of docs pages before other savings).
   - `archive-2x`: all 2.x. Freeze it after March.
   - `archive-1x`: all 1.x. Frozen forever.
2. Each profile uses `onlyIncludeVersions` and the same `baseUrl` and `routeBasePath`. Output HTML lands at the same URLs as today, so no redirects are needed.
3. Cache each archive build in CI. Key it on a hash of `versioned_docs/version-<major>.*`, `versioned_sidebars`, `versions.json`, and the config. Restore on a hit and skip the build.
4. Deploy by merging the outputs into one directory with `rsync`. Only `live` supplies `/index.html`, the `/docs/` root, and `sitemap.xml`.
5. Replace `docsVersionDropdown` with a static dropdown of explicit links, because a profile only knows its own versions. Group it as Next, 3.x, 2.x, 1.x. You lose the "same page in the other version" jump across profiles. A small custom component can restore it later.
6. Check search. Algolia DocSearch crawling the merged site works. A local-search plugin builds one index per profile and breaks.
7. Check for collisions in the merged output. Hashed asset names are safe, but verify `rsync` reports no overwrites of differing files.
8. Freeze rule: when 3.5 cuts, move 3.4 into an archive profile. In March, move the 2.x versions to `archive-2x`.

## Small extras

- Mark old versions with the per-version `banner: 'unmaintained'` (1.x and archived minors), linking to the latest.
- 1.x air-gapped customers can't use the online docs. Publish the frozen `archive-1x` output as a tarball release asset. It costs nothing once it's built.
- Optional, SEO: set `noIndex: true` on archived versions after the baseline is saved, to cut duplicate-content crawling.

## Decision for you: public `/docs/` root

Today `/docs/` serves Next, which is unreleased docs for customers. I recommend setting `lastVersion: '3.4'` for the public site. Next stays at `/docs/next/`. Engineers can still land on Next in an internal deploy where `lastVersion: 'current'` is set via env.

The catch: existing `/docs/<page>` links currently show Next content. After the change they show 3.4. Pages that exist only in Next would 404. Find them by diffing page paths between `current` and 3.4, and redirect those to `/docs/next/...`. The guard script catches any you miss.

## Questions

1. Which host serves the site (Netlify, Cloudflare Pages, S3 + CDN, other)? It decides the edge-redirect option.
2. Do 3.0–3.3 still get doc edits, or only 3.4 and Next?
3. Are you OK switching the public root to 3.4?

**Next:** run the Phase 0 baseline and the `['current', '3.4']` timed build, then paste both numbers here.