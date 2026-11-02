# Retiring the Hollowmere 1.x docs

## Recommendation

Go ahead, with three changes to the plan:

1. Verify docs traffic before merging.
2. Replace the pure catch-all with a short stub page, or at least path-mapped redirects.
3. Link to docs.rs for 1.x API docs.

## Why retire

- 1.x has been unsupported for 26 months, and the docs still cost about 6 minutes on every deploy.
- 1.x pages show up in site search next to current docs. That's the sharper harm: someone can follow 1.x instructions for an unsupported version.
- Nothing in the 1.x folder is lost. It stays in git history, and the API reference stays on docs.rs.

## Evidence to correct

**The python-future precedent doesn't support the argument.**
- 3% is about 75 times 0.04%.
- The precedent was a different ecosystem, a different project, and a different share. It sets no threshold.
- Use your own policy instead: unsupported for over 2 years, and docs cost deploy time and search quality.

**The "CI caches and bots" explanation is an assumption.**
- It may well be true. Download counts also include Cargo.lock'd production builds, vendored mirrors, and Docker rebuilds. Those are real users stuck on 1.x.
- Downloads don't measure docs readers anyway. The decision is about docs traffic, so check that directly.

## Pre-flight checks (about 30 minutes)

Do these before merging.

1. **Docs traffic.** Pull 90 days of page views for `/1.x/*`. Get the top 20 paths and their referrers (Google, crates.io, GitHub issues, other sites).
2. **Download trend.** On crates.io, check whether 1.x is flat or falling. A steady 3% with no decline points to locked builds, not bots.
3. **Reverse dependencies.** Check whether any public crate that others depend on pins `hollowmere = "1"`.
4. **Inbound links.** Search your GitHub issues, README, and crate metadata for `/1.x/` links. Update them in the same PR.
5. **Search queries.** Check your site-search logs for queries that land on 1.x pages.

**Go/no-go:**
- If 1.x docs traffic is a small fraction of the total, proceed.
- If a few paths get steady human traffic, map those paths to their 2.x equivalents.
- If the traffic is large, stop and talk to those users before proceeding.

## Redirect design

A single catch-all 301 to `/docs/` is acceptable but weak. Search engines may treat many URLs redirecting to one generic page as soft 404s. Users also land on a page that doesn't say why they were redirected.

Use a layered approach, with the most specific rule first:

1. **Path-mapped redirects** for the top 1.x pages that have a 2.x equivalent, such as the quickstart and the API overview.
2. **A stub page** at `/1.x/` that says the following. Keep it as one small static page that doesn't affect build time.
   - 1.x is end-of-life.
   - Here is the migration guide to 2.x/3.x.
   - 1.x API docs are on docs.rs.
3. **A catch-all** for everything else.

Example for Netlify or Cloudflare Pages `_redirects` (adapt to your host):

```
/1.x/quickstart   /docs/quickstart/   301
/1.x/             /1.x-retired/       301
/1.x/*            /docs/              301
```

Keep the 301s permanent and in place indefinitely. They cost nothing.

## Search cleanup

- Redeploy and trigger a reindex, or purge the `/1.x/` entries from your site-search index. A redirect alone won't remove them.
- Remove `/1.x/` from `sitemap.xml`.
- Don't add `noindex` to pages that redirect. It does nothing useful there.
- Check Google Search Console for coverage errors after one to two weeks.

## Execution plan

1. Complete the pre-flight checks.
2. Open a PR that:
   - deletes the 1.x docs folder
   - removes it from the build config and sitemap
   - adds the redirects and the stub page
   - updates internal links
3. Preview deploy. Request a few old URLs with `curl -sI` and confirm a 301 with the right `Location`, plus a 200 on `/docs/` and on the stub.
4. Merge. Confirm the deploy time dropped by about 6 minutes.
5. Reindex search.
6. Watch for 4xx spikes on `/1.x/*` for two weeks.

## Communication

- Post a short note in the changelog or discussions: "1.x docs retired. Migration guide: [link]. API reference remains on docs.rs."
- Don't yank 1.x from crates.io. Yanking breaks Cargo.lock'd builds for exactly the users in that 3%.
- Optionally add a one-line pointer to the migration guide in the 1.x crate README or metadata on the next patch, if you still publish patches.

## Rollback

Revert the PR. The docs rebuild from git, and the redirect rules go away with it. Nothing is destroyed, so risk is low.

## Alternative if you want the build time without deleting

Build the 1.x docs once, keep the static output in a bucket or branch, and serve it under `/1.x/` without rebuilding. That removes the 6 minutes but not the search clutter, so it only fits if you want to keep the pages online. Since you want them gone, I'd skip it.