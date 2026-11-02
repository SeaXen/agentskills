# Docs SEO fix: docs.fernbrook.io

## Verdict

Both problems have the same root cause: using `robots.txt` `Disallow` as if it deindexes a page. It doesn't — it only stops crawling. A URL Google already indexed before you added `Disallow: /v1/` and `Disallow: /v2/` can never be recrawled, so Googlebot never sees the `noindex` you put in the front matter. That's exactly why those 830 URLs show as bare links with no title or snippet: it's Search Console's "indexed, though blocked by robots.txt" state, frozen since the day you added the Disallow lines nine months ago.

Your infra lead's proposal — add more `Disallow` lines for the preview hosts — reproduces this same bug on purpose. Do not do it, at least not yet and not alone. The single highest-value fix is: stop blocking crawl access to `/v1/`, `/v2/`, and the preview hosts, and let a real `noindex` signal (HTTP header, verified live) do the deindexing instead.

## Coverage of this audit

No live crawl was run in this session — I don't have network access to docs.fernbrook.io. Everything below is built from the skill's failure-mode patterns matched against what you described, plus the verification commands you should run yourselves before shipping. Not verified: actual robots.txt contents, actual response headers, actual sitemap contents, Search Console data, how many preview URLs (beyond docs-pr-1142) are indexed, and whether the front-matter `noindex` flag actually renders into HTML `<head>` on Sphinx's built output. Run the commands below and correct any assumption that doesn't hold.

## Blocking defects

| # | Defect | Pages affected | Fix | Owner | Effort |
|---|---|---|---|---|---|
| 1 | `/v1/` and `/v2/` disallowed in `robots.txt`, so their `noindex` front-matter flag is never read | 830 | Remove both `Disallow` lines; serve `X-Robots-Tag: noindex` from nginx for those two paths | infra | 1–2h |
| 2 | Preview hosts (`*.preview.fernbrook.io`) serve 200 with no `noindex` signal at all | ~60 live, unknown # indexed | Add `X-Robots-Tag: noindex` at the nginx block that fronts every preview host, before any Disallow | infra | 1h |
| 3 | Already-indexed preview URLs (confirmed: `docs-pr-1142`) sit in results with no owner action taken | ≥1, likely more | Search Console Removals (see fix list) | infra/docs | 30m |
| 4 | Sitemap likely still lists `/v1/` and `/v2/` pages (sphinx-sitemap emits everything built by default) | up to 830 | Exclude `/v1/` and `/v2/` from the sitemap config | docs build | 30m–1h |

Items 1–2 override any score below. Nothing else matters until crawl access is restored.

## Duplication and versioning

Declared posture: `noindex` on `/v1/` and `/v2/`, i.e. **latest-only** — you want the current version to be the only one Google shows. Actual posture: **blocked-and-noindexed**, a fifth state the skill doesn't rank because it's not a real posture, it's a bug — the pages are neither served to Google nor removed from it.

Once crawl access is restored and `noindex` is confirmed live, you land on latest-only as intended, at near-zero ongoing cost. One open question worth a decision, not a fix: are `/v1/`/`/v2/` pages still linked from old tutorials, issues, or bookmarks? If yes, per-page `301` redirects to the nearest current-version equivalent serve those visitors better than a `noindex` page they land on and bounce from — noindex only solves the search-visibility side, not the "someone still has the old link" side. Decide this with the docs team; it's not required to fix the current defect.

## Page signals / internal linking

Not in scope for what you described — nothing here to report. If you want a full audit later, that's a separate pass once the blocking defects clear (a title rewrite on a page Google can't crawl is wasted effort anyway).

## Fix list

Ordered by (pages affected × severity) ÷ effort, blocking defects first:

1. **infra** — Remove `Disallow: /v1/` and `Disallow: /v2/` from `robots.txt`. This alone does nothing for indexing yet; it only lets Google back in. ~15m.
2. **infra** — Add `X-Robots-Tag: noindex` in the nginx `location` blocks for `/v1/` and `/v2/`. Don't rely solely on the Sphinx front-matter meta tag — verify it actually rendered first:
   ```bash
   curl -s https://docs.fernbrook.io/v1/some-page/ | grep -i 'noindex\|robots'
   curl -sI https://docs.fernbrook.io/v1/some-page/ | grep -i x-robots-tag
   ```
   If the meta tag isn't there (common when a theme was never updated to read the front-matter flag), the nginx header becomes your only real signal — ship it regardless, it's more robust than depending on template rendering. ~1h.
3. **infra** — Add `X-Robots-Tag: noindex` to the wildcard nginx config that serves every `*.preview.fernbrook.io` host, so it's a config-level fix that covers all ~60 current previews and every future one automatically, not a per-branch step. **Verify it's live before step 5**:
   ```bash
   curl -sI https://docs-pr-1142.preview.fernbrook.io/ | grep -i x-robots-tag
   ```
   ~1h.
4. **docs/infra** — In Search Console, request prefix removal for `docs.fernbrook.io/v1/` and `docs.fernbrook.io/v2/` under Removals → Temporarily Remove URL, and per-host removal for known indexed preview hosts (`docs-pr-1142.preview.fernbrook.io`, plus any others a `site:` search turns up). This hides them from results in hours instead of waiting weeks for recrawl+drop, and buys time while the permanent `noindex` takes effect. Temporary (~6 months), not a substitute for steps 1–3. ~30m.
5. **infra** — Only after step 3 is confirmed live: add a separate `robots.txt` served on the preview hostnames themselves (`Disallow: /`), as a second layer on top of the header, not instead of it. This is the one place adding a Disallow is safe — because it's added after the noindex signal is already working, not before. ~30m.
6. **infra** — Confirm you have a DNS-verified domain property (`fernbrook.io`) in Search Console, not just a URL-prefix property for `docs.fernbrook.io`. A domain property is the only way to see and manage every `*.preview.fernbrook.io` subdomain in one place; without it you're managing indexing on ~60 hosts you can't even see. ~15m, one-time.
7. **docs build** — Exclude `/v1/` and `/v2/` from the sitemap (sphinx-sitemap config, or a post-build filter). A sitemap that still lists 830 noindexed, disallowed URLs is a third signal contradicting the other two, and it's wasted crawl budget pointed at pages you don't want touched. ~30m–1h.
8. **docs team, decision only** — Decide whether `/v1/`/`/v2/` stay noindexed-forever or graduate to per-page `301`s to current-version equivalents, based on whether real external links still point at them. Not urgent, not blocking.

## Pass threshold

Sourced (not negotiable — these are enforced by the crawler, not a target you're choosing):
- A page disallowed in `robots.txt` never has its `noindex` read. This is *why* the current 830 are stuck.
- `X-Robots-Tag` must be present on the actual HTTP response — a platform's default reputation isn't a substitute for `curl -I`.

Baselines for this skill, agree adjusted numbers with your own team before the fix pass:
- Indexed `/v1/`/`/v2/` URLs → 0 (measured with `site:docs.fernbrook.io/v1/` and `/v2/`, or the Search Console Pages report once the domain property exists)
- Indexed preview URLs → 0 (`site:preview.fernbrook.io`)
- Sitemap contains 0 URLs under `/v1/` or `/v2/`
- `X-Robots-Tag: noindex` returns on 100% of sampled `/v1/`, `/v2/`, and preview-host responses

Report this as pending once shipped, not solved: removing the Disallow lines gets Googlebot back in, but Google drops URLs from the index on its own schedule — typically weeks for organic recrawl-and-drop, hours for the Removals-tool entries. Re-run a `site:` check in 2–4 weeks and diff against today's count; that diff is the proof, not this list.