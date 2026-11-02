## Sanity check: don't run this script

**Verdict: kill the contractor's script. It treats a symptom (title length) that isn't the cause, and the h1 change actively makes the real problem worse.** Redirect the approved budget to a one-line template fix instead — it costs a fraction of a per-page script and actually fixes what's rewriting your titles.

### Coverage statement

This is a targeted review of the two proposed fixes against the pattern you described, not a full crawl of docs.voltaic.systems — I didn't fetch live pages or run Search Console. Everything below follows directly from your title shape and the Docusaurus generator; the character-count fix and the h1-prefix fix are both named as classic wrong fixes in this skill's own reference material, worked against this exact failure shape.

### Why Google is rewriting your titles

Google states there's no length limit on `<title>` — the truncation you see in results is a display constraint, not a ranking penalty for going over some cutoff. Google rewrites a title when it decides the page's own title is unhelpful, typically because it's boilerplate- or breadcrumb-shaped. Yours — `Voltaic Docs - Guides - Webhooks - Sending a webhook` — is the textbook case: four segments of navigation chrome before the one string a searcher actually typed. That shape, not the character count, is what's triggering the rewrite.

### Why the contractor's fix doesn't fix it

**Trimming to 58 characters keeps the same shape.** `Voltaic Docs - Guides - Webhooks - Sendin…` is still breadcrumb-first with the query term buried — Google will keep building its own title from your `h1`, headings, and anchor text, exactly as it does now. You'd pay for 1,240 rewrites and see no change in the rewrite rate.

**It's also the wrong kind of fix.** A trim script operates per-page, after the fact — a config or template change reaches all 1,240 pages from one edit and regenerates correctly on every future build. A script has to be re-run (or wired into the pipeline) forever, on every new page and every content edit, for as long as the site exists.

### Why the h1 change is worse than a no-op

Google draws replacement titles partly from `h1` text. Prefixing "Voltaic" onto every `h1` hands the rewriter more brand-first, boilerplate-shaped text to pull from — the same defect you're trying to fix, now duplicated in a second source Google already reads. It also stops the `h1` from doing its actual job: telling a reader (and Google) what the page is about. Brand belongs in the title template, once, at the end. It does not belong on the `h1`.

### What to fix instead

The real defect lives in whatever generates your `<title>` — in Docusaurus that's `docusaurus.config.js`'s site title plus either a swizzled title component or per-page frontmatter that's currently composing the full breadcrumb into the title string. Find that composition point and change its *shape*, not its length:

| | |
|---|---|
| Current | `Voltaic Docs - Guides - Webhooks - Sending a webhook` |
| Target | `Send a webhook \| Voltaic Docs` |

Keep the section only where it disambiguates — e.g., API reference symbols that repeat across sections — not as default chrome on every page.

### Fix list

| Fix | Where | Owner | Effort |
|---|---|---|---|
| Stop the contractor engagement as scoped | — | you | now |
| Rewrite the title template to `{page} \| Voltaic Docs` | Docusaurus config / swizzled title component | whoever owns the Docusaurus config and deploy | hours, one edit reaches all 1,240 pages |
| Revert any h1-prefix change already made, or don't ship it | markdown source / layout | same | none if not yet shipped |
| Leave `h1` as the page's own descriptive heading, no brand | — | same | included above |

### How to verify it worked

Not by counting characters. **Run the crawl script** (`scripts/docs-seo-crawl.py` in this skill) against your sitemap before and after the template change, diff the title list for duplicates and shape, then watch Search Console's title-rewrite rate over the following weeks — that's a search-engine-timed signal, not something this session can confirm same-day.

One more thing worth 20 minutes while you're in the config: if titles are wrong, descriptions are probably falling back to boilerplate too (`ai-seo`/`page-signals-and-snippets.md` pattern: "This page contains documentation for…"). Same root cause, same one-template fix, worth checking in the same pass rather than a second engagement later.