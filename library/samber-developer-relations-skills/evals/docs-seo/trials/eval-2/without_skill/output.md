# Diagnosis: docs.fernbrook.io — /v1/, /v2/, and preview subdomains

Both problems have the same root cause: **`Disallow` in robots.txt stops crawling, not indexing.** Google can index a URL it's never fetched if it's linked from anywhere — it just can't show a title or snippet, because it never read the page. That "bare URL, no title, no snippet" result is the textbook signature of a blocked-but-linked page (Search Console labels this "Indexed, though blocked by robots.txt"). Adding `noindex` to the front matter did nothing, because Googlebot was never allowed in to read the front matter in the first place. The two directives were fighting each other, and `Disallow` won by default.

Your infra lead's fix (more `Disallow` lines for preview hosts) repeats the exact same mistake on a bigger, faster-moving surface. Don't do that.

## Priority Fix List

**1. Remove `Disallow: /v1/` and `Disallow: /v2/` from robots.txt.** This is the fix, not a step toward one. Letting Googlebot crawl those paths again is what finally lets it see the `noindex` that's already sitting in the front matter. Nothing else in this plan works until this line is gone.

**2. Confirm `noindex` is actually served correctly once crawling is allowed.** Check it's a real `<meta name="robots" content="noindex">` in the rendered HTML `<head>` (Sphinx templating sometimes drops front-matter values silently) or better, an `X-Robots-Tag: noindex` HTTP header from nginx — the header is more reliable because it doesn't depend on the theme rendering it correctly, and it also covers non-HTML assets under those paths.

**3. Decide if `/v1/`/`/v2/` should be `noindex` or `301` redirected.** If these versions are fully retired and a v3+ equivalent exists, redirect old paths to their current equivalents (or to a version landing page) instead. A redirect resolves permanently in one crawl and passes along any residual link equity; `noindex` requires Google to keep re-crawling dead pages forever just to keep re-confirming "still don't index this." If some content has no current equivalent, `noindex` is fine — just make sure it's reachable.

**4. Speed up de-indexing instead of waiting on natural recrawl.** With ~830 URLs, natural recrawl could take weeks to months depending on crawl budget. In Search Console:
   - Submit a handful of representative URLs via URL Inspection → Request Indexing, to seed the recrawl.
   - Use **Removals → Temporary removal** for immediate suppression from results (hides for ~6 months) while the crawl-allow + noindex/redirect resolves permanently underneath.
   - Make sure `/v1/`/`/v2/` are absent from `sitemap.xml` — don't invite Google back to pages you're retiring.

**5. Verify a Domain-type property in Search Console for `fernbrook.io`** (DNS TXT at the apex), if you don't already have one. It automatically covers every subdomain — including all 60 rotating preview hosts — under one view, so you're not stuck trying to verify `docs-pr-1142.preview.fernbrook.io` individually before you can act on it. This is what makes step 7 tractable.

**6. Stop preview hosts from being publicly indexable at the infrastructure layer, not with per-branch robots.txt entries.** Adding a `Disallow` line per preview host doesn't scale (60 live at once, hostnames rotate as branches open/close, you're always a step behind) and it wouldn't have prevented `docs-pr-1142` from getting indexed anyway — same flaw as #1: `Disallow` blocks crawling, it doesn't block indexing of a linked or discovered URL. It also actively advertises the preview URL pattern to anyone who reads robots.txt. Instead, fix it once at the nginx layer serving `*.preview.fernbrook.io`:
   - Add a single `X-Robots-Tag: noindex, nofollow` response header for the whole wildcard vhost. One config block covers all current and future preview builds — no per-branch maintenance.
   - Better: put preview builds behind HTTP Basic Auth or an authenticated proxy at the same nginx layer. These builds are unreleased/in-progress docs; the real problem isn't just SEO, it's that they're publicly reachable at all. Auth solves discovery, indexing, and accidental leaks of unshipped content in one move.

**7. Clean up already-indexed preview URLs.** Once the domain property from step 5 is verified, use Removals for any preview hostnames already showing in results (like the one that surfaced last week). Going forward, with the header/auth from step 6 in place, no new preview host should ever reach the index, so this becomes a one-time cleanup, not a recurring chore.

## Why this ordering

Steps 1–4 fix the confirmed, currently-visible problem (830 stale URLs); they require no infrastructure change, only a robots.txt edit plus verifying an existing front-matter flag actually renders. Step 5 is a prerequisite for step 7. Steps 6–7 fix the preview-host leak at its source instead of chasing it host-by-host, which is the part of the infra lead's plan that would otherwise turn into permanent manual upkeep.