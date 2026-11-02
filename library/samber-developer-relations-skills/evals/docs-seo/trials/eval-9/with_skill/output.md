## Docs SEO review — Thessaly v2 retirement plan

**Verdict:** The plan doesn't hold up. Two of its mechanics match named failure modes for retiring a docs version — a blanket redirect to the homepage, and a sitemap update deferred past the cutover — and a third issue sits above SEO entirely: v2's published EOL is 2027‑03‑31, but the plan pulls the docs ~17 months early. That's not a redirect-shape problem; it overrides the whole "cheap plan" calculus, and it's not something an nginx rule can fix. Fix all three before the cutover ships, not after.

**Scope note:** This is a review of the plan as described (1,900 URLs, one nginx rule to the docs root, sitemap cleanup ticketed for next quarter, 160 pages with no v3 successor, 2027‑03‑31 EOL) — not a live crawl of docs.thessaly.dev. I don't have the actual sitemap, robots.txt, or v3 information architecture, so the redirect-mapping recommendation below assumes v3's URL structure roughly mirrors v2's for the ~1,740 pages that do have a successor; verify that assumption with an actual crawl (`docs-seo-crawl.py` against the current sitemap) before finalizing the nginx rules, and again after cutover to confirm the redirects landed where intended.

### Findings

**1. Retiring the version 17 months ahead of its published EOL is the real blocker, not an SEO detail.**
A published EOL date is a support commitment. Anyone still running v2 in production — and with 1,900 pages of docs, someone is — was told the version, and by extension its documentation, would still be around until 2027‑03‑31. Pulling the docs next month breaks that promise regardless of how good the redirects are: bookmarks, support tickets, internal runbooks, and third-party tutorials pointing at specific `/v2/` URLs lose their target with no warning tied to the date people were told to plan around. If that EOL date appears in any customer contract, support tier, or compliance document, this is a commitment breach independent of anything below. Get explicit sign-off from whoever owns the EOL date before shipping the redirect — either hold v2 docs live (archived, clearly bannered as unmaintained, self-canonical — it doesn't need to rank, it needs to exist) until 2027‑03‑31, or have the business formally move the date and communicate it to customers ahead of the cutover, not after.

**2. A single rule 301ing everything under `/v2/` to the docs root is the "redirect to home" failure mode.**
Retiring a version means choosing a redirect target *per page*, not per tree: current v3 equivalent → nearest equivalent → the docs index, in that order, with the index reserved for genuine leftovers. A blanket redirect of the whole tree to the homepage is treated as a soft 404 and throws away whatever standing each individual page had. Practically: anyone who lands via an old external link, a cached search result, or a Stack Overflow answer citing a specific v2 page gets dropped on the homepage with no path back to what they wanted — reads as broken to a human and to a crawler alike.
Fix: build a redirect map, not a single rule. For the ~1,740 pages that do have a v3 successor, this is largely mechanical if v3's IA tracks v2's — path-preserving nginx rewrites (`/v2/guides/(.*) → /v3/guides/$1`, adjusted per section as needed), with manual review only where the IA diverged. Fall back to the docs root only for the genuine remainder that maps to nothing.

**3. The 160 pages for the two removed subsystems should 410, not redirect to an unrelated page.**
301 is for content that has an equivalent; 410 is for content that's genuinely gone with no successor. These 160 pages are the second case — routing them to the homepage compounds finding 2 with a redirect to content that says nothing related to what the page was about, which both users and Google discount. Serve `410 Gone` for these two subsystems' URL patterns instead (the response body can still be friendly — explain the subsystem was removed in v3, link to a migration note if one exists — the status code is what matters here, not the copy).

**4. Deferring the sitemap update to next quarter contradicts "same deploy."**
Update the sitemap in the same deploy as the redirect, or it keeps advertising 1,900 URLs as live canonical pages for a full quarter after they start 301ing or 410ing. That wastes crawl budget on your own domain and delays the Search Console signal (the "page with redirect" / "not found" buckets) that would otherwise tell you the cutover worked cleanly. There's no reason this needs its own ticket next quarter — pulling the `/v2/` entries is a one-line change to whatever generates the sitemap, made the same day the nginx rule ships.

### Fix list

| # | Issue | Pages affected | Fix | Owner | Effort |
|---|---|---|---|---|---|
| 1 | v2 pulled 17mo before published 2027‑03‑31 EOL | all 1,900 | get sign-off to either hold docs live until EOL, or move/communicate the date before cutover | product/support leadership | decision, not build |
| 2 | Blanket redirect to docs home | 1,900 (1,740 with a real successor) | per-page/per-pattern 301 map: successor → nearest equivalent → home as last resort | web team | medium — mostly mechanical, manual review where v3 IA diverged |
| 3 | Orphaned-subsystem pages redirected to unrelated content | 160 | serve 410 on those two subsystems' URL patterns instead of 301 | web team | low — a couple of nginx location blocks |
| 4 | Sitemap cleanup ticketed for next quarter | 1,900 | remove `/v2/` sitemap entries in the same deploy as the nginx rule | docs build | low — move the existing ticket up |

Keep the eventual redirects live for at least one major release cycle after the real retirement date — external tutorials and cached answers keep sending traffic long after a version dies — and re-run a crawl before and after cutover to confirm the map actually landed where intended; that diff is the proof this worked, not the plan itself.