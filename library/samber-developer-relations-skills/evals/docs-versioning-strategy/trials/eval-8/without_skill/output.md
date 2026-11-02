**Next action:** tell me which docs tool you use (Docusaurus, Mintlify, Nextra, Astro Starlight, or other) and where the 2.x page text lives (git history or an old branch). The steps below hold either way. Commands depend on the tool.

## Recommendation: skip branch-per-version

Give 2.x its own docs set and a switcher. Keep it in a folder on `main`, not in a branch.

Branch-per-version costs you for a 6-week payoff:
- Every shared fix needs a backport to two branches.
- Your build has to stitch two branches into one site.
- You need CI, preview, and deploy logic per branch.
- After 2.x EOL, you have a dead branch to maintain or delete.

Only about 12 pages differ. A frozen `/docs/v2/` folder gives the same reader experience for a fraction of the work.

**Decision for you:** if you still want branches, say so and I'll outline that path. I'd advise against it.

## Target layout

| Reader | URL | Content |
|---|---|---|
| 3.x (current) | `/docs/` | Full set, always latest |
| 2.x | `/docs/v2/` | Frozen, with an EOL banner |
| Old links | `/docs/3.1/*` | 301 to `/docs/*` |

Use the major version only in URLs. The switcher shows "3.x (latest)" and "2.x (unsupported after <date>)". When 4.x arrives, you snapshot 3.x to `/docs/v3/`. No URL churn for current readers.

## Plan: 2 PRs, about 4 hours

Ship the URL move first. It is the riskiest change for inbound links. The 2.x work then lands on a stable base.

### PR 1: move `/docs/3.1/` to `/docs/` (about 90 min)

1. **Inventory (15 min).** List every place that links to `/docs/3.1/`:
   - Internal links and nav config
   - Sitemap and canonical tags
   - Search index config (Algolia or similar)
   - SDK `README.md` and `package.json` `homepage`
   - Error messages and JSDoc links inside the SDK source
   - Dashboard, API reference, and blog links
2. **Move the folder (15 min).** Use `git mv docs/3.1 docs` (or your tool's equivalent). Do not copy. Rewrite internal links with a scripted find-and-replace, then review the diff.
3. **Add redirects (20 min).**
   - Rule: `/docs/3.1/:path*` to `/docs/:path*`, status 301.
   - Add the same for `/docs/3.0/*` if it ever existed.
   - Keep these redirects **forever**. Published npm versions embed `/docs/3.1/` links you cannot edit.
4. **Fix SEO signals (10 min).** Make canonical tags and the sitemap point to the new URLs. Do not leave both URL sets live.
5. **Verify (20 min).**
   - Run a link checker on the build.
   - Run `curl -sI https://<site>/docs/3.1/<known-page>`. Expect 301 and the right `Location`.
   - Also curl the plain `/docs/<known-page>`. Expect 200.
   - Test a deep link with an anchor (`#section`).
6. **Update the SDK repo (10 min).** Change `homepage` and README links. Do this in the next SDK release. Redirects cover older ones.

### PR 2: 2.x docs set and switcher (about 2.5 h)

1. **Pick the 12 pages (15 min).** Diff 2.x against 3.x. Expect changes in:
   - Client init
   - Error types and error handling
   - Pages that quote either
   - Quickstart and migration pages
2. **Recover 2.x text (30 min).** Pull the last 2.x-accurate version of each page from git history. Use `git log --follow -- <page>`, then `git show <sha>:<path>`. Check each page against the 2.x SDK types, not only against memory.
3. **Create `/docs/v2/` (30 min).** Two ways to do this:
   - **Full snapshot** (what Docusaurus-style versioning does): copy the whole tree, then overwrite the 12 pages. Simple, no cross-links to worry about.
   - **Overrides only:** put just the 12 pages in `/docs/v2/`, and link or fall through to shared pages. Less to maintain, but 2.x readers can bounce into 3.x pages.
   
   Pick the full snapshot unless your tool makes overrides easy. The folder is frozen after the snapshot, so duplication costs nothing.
4. **Add the switcher (30 min).** Use your tool's version dropdown. On each page, link to the same page in the other version when it exists, otherwise to that version's root.
5. **Add banners (15 min).**
   - On 2.x pages: "2.x is supported until <date>. Upgrade to 3.x" with a link to the migration guide.
   - Optionally on 3.x pages that have a 2.x twin: "Using 2.x? See here."
6. **Handle search and SEO (15 min).**
   - Tag search results by version, or scope the index to the active version.
   - Set 2.x pages to canonical-point at their 3.x twin where one exists.
   - Do not `noindex` yet. 2.x users are still searching for these pages.
7. **Verify (15 min).** Run the link checker. Click through the switcher on 5 pages. Check the sitemap contains both trees.

## Later tasks (not Saturday)

- **When 3.2 ships:** edit `/docs/` in place. No URL work.
- **At 2.x EOL (about 6 weeks):**
  - Change the banner to "no longer supported."
  - Consider `noindex` on `/docs/v2/`.
  - Do not delete it. Old SDK links point there.
- **When 4.x arrives:** snapshot `/docs/` to `/docs/v3/`, then write 4.x into `/docs/`.

## Risks to watch

- 🔴 Forgetting SDK-embedded links. Without permanent redirects, old error messages 404.
- 🟠 Double-indexed content during the move. Fix with canonicals and the sitemap in step 4.
- 🟠 A 2.x page copied from 3.x without being corrected. Verify against 2.x types.
- 🟢 Rollback is easy: PR 1 is one revert, and the redirects are harmless.

## Time check

- PR 1: about 90 min
- PR 2: about 2.5 h
- Total: about 4 h, so tight for one afternoon. If you run short, ship PR 1 Saturday and PR 2 Sunday. PR 1 is the one that fixes the confusing URL.

**Next:** answer the two questions at the top. Then do step 1 of PR 1, the link inventory, which takes 15 minutes.