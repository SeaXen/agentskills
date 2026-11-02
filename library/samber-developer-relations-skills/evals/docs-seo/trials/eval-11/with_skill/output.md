# Docs SEO plan — docs.granthamdata.com

## Verdict

Before touching the fix list: the page set you named (quickstart, Python SDK install, three how-tos) is where *developers* land. It is not where the *deal* lands. You sell six-figure contracts to banks and insurers, and every one goes through a security review — which means a second, unmeasured audience (security engineers, compliance officers, procurement) is reading your limits, security, compliance, self-hosting and migration pages before the deal closes. Traffic analytics cannot surface that audience: if those pages have few inbound links, they get little organic traffic, so they never rank on a "top pages" report — the report is measuring the symptom of the problem, not the value of the page. Your 47 orphan pages and the reference pages that "link nowhere" are the most likely place that cluster is hiding. Start there, in parallel with — not after — the pages you already named.

## Gating questions still open

Per this skill's interview, four of these decide the whole approach. Answer what you can; I've defaulted the rest and flagged the default:

| # | Question | Default assumed here | Why it matters |
|---|---|---|---|
| Versioned? | Which versions are published/supported | **Unknown — ask** | Gates the whole version-posture decision in Step 3 below |
| Translated? | Any locales | Assumed no (not mentioned) | Skips hreflang work if true |
| Preview/staging docs on public hosts? | Netlify/Vercel deploy previews are the default Docusaurus setup | **Check today** — most common source of accidental indexing | |
| Search Console access for this property? | Unknown | Without it, indexation and "different canonical" numbers can't be measured, only inferred from crawl + `site:` queries | |
| Who ships fixes — docs writers, or infra owns the CDN/robots layer? | Unknown | Splits the fix list's owner column | |
| Deadline / effort ceiling | Unknown | Decides stable-canonical vs. latest-only if versioned | |

## Step 1 — Build the real crawl set (do this before anything below is final)

Everything past this point is either a known finding (the 47 orphans, the dead-end reference pages) or a hypothesis that needs the crawl to confirm. Run:

```bash
python3 scripts/docs-seo-crawl.py https://docs.granthamdata.com/sitemap.xml --out pages.csv --summary
```

900 pages is under any sitemap size limit, so a single-file run is fine — no need for `--limit`/`--delay` sampling. The `--summary` output gives you, per URL: status, title/description/canonical, robots directives, first `h1`, word count, and inbound/outbound internal link counts — which turns "47 orphans" and "reference pages that link nowhere" from a crawler's headline into a URL list you can act on.

Also check by hand, since the script doesn't:
- `robots.txt` and the sitemap file itself.
- One page fetched with JS disabled — Docusaurus is SSG so this is usually fine, but confirm Algolia DocSearch or embedded tabs/diagrams aren't hiding body text or canonical links until JS runs.

**Docusaurus-specific shortcut for the orphan pages**: run `docusaurus build` and read the build log for "document is not present in any sidebar" warnings. In Docusaurus, a page with zero inbound links (not even nav) almost always means it exists on disk but was dropped from `sidebars.js` — a stale reference page, a page removed from nav during a restructure, or a plugin (OpenAPI/SDK-reference generator) emitting a route nothing links to. That log will likely name most of your 47 directly, faster than reverse-engineering them from the crawl.

## Step 2 — Blocking defects (check first, in this order)

These override everything else — a title rewrite on a page Google can't crawl is wasted effort:

1. `robots.txt` disallowing a path that also carries `noindex` (the disallow means the noindex is never read).
2. Non-200 URLs still listed in the sitemap.
3. `noindex` inherited from Docusaurus front matter or a theme default, applied to a whole section by accident.
4. Deploy-preview hosts (Netlify/Vercel branch previews are the Docusaurus norm) — verify:
   ```bash
   curl -sI https://<preview-host>/ | grep -i x-robots-tag
   ```
   If nothing comes back, **add `X-Robots-Tag: noindex` at the CDN** — this is a write, flag it for whoever owns infra.
5. Anything only rendered after JS.
6. CSS/JS blocked in `robots.txt`.
7. Per-agent AI-crawler rules — audit per named agent against each vendor's current docs, don't apply a blanket "block AI bots" rule. For a security-conscious buyer base, a developer's coding assistant being able to fetch your docs when asked is usually worth more than it costs.

## Step 3 — Version posture (pending your answer above)

If docs.granthamdata.com is unversioned, skip this — there's no posture decision to make. If it is versioned:

- Given supported bank/insurer integrations tend to stay on a contracted version for years, and a compounding-value docs site is your situation (not a one-off deadline), default to **stable-canonical**: `/en/stable/…` plus `/en/v2.3/…`, every version canonicaling to the stable alias. Docusaurus supports per-version `noIndex` natively (added specifically because deprecated versions were outranking current docs).
- Move to **latest-only** only if just the current release is actually supported.
- Whichever posture: make sitemap, canonical tags, and nav agree, and add an in-page "you're reading an old version" banner regardless — the canonical doesn't fix the human-facing confusion.

## Step 4 — Page signals

Template-level first, per-page second — this is 900 pages, not something to hand-edit.

- **Title template**: Docusaurus `titleDelimiter`/theme title config. Target shape `{page} | Grantham Data Docs`, query term first, brand last. If titles currently read as breadcrumbs (`Docs - Reference - Python - install`), that — not length — is why Google may be rewriting them.
- **Descriptions**: write real ones for quickstart, Python SDK install, and the three how-tos, as you planned — **and** for every page in the security/compliance/limits/self-hosting/migration cluster, even though it won't show up on a traffic-ranked list. That's the audience-note override: those pages are read by a smaller number of people who decide a much bigger number of dollars.
- **BreadcrumbList structured data**: Docusaurus's visual breadcrumbs aren't structured data by default — add the markup if missing. Skip `HowTo`/`FAQPage`; Google withdrew both.
- **Headings**: check the auto-generated reference tree specifically for `h1`→`h4` skips (common with OpenAPI/SDK-reference plugins), and keep anchor `id`s stable across builds — a bank's security reviewer citing `#authentication` in an internal doc, then hitting a 404 after your next release, is a bad signal at exactly the wrong moment.

## Step 5 — Internal linking: your two concrete findings

Work in this order, not all at once:

1. **The 47 orphans.** Pull the list from Step 1. Every one gets linked from somewhere or deleted — no third option. Expect a disproportionate share to be exactly the security/compliance/limits/self-hosting/migration cluster the traffic report can't see; if the build-log check above confirms that, it's your strongest argument for reprioritizing.
2. **Dead-end reference pages.** A reference entry that never links to the how-to that uses it ends the session there. Fix as a template change (a "used in" / "see also" block driven by your SDK reference generator), not per-page edits.
3. **Contextual links from your named high-authority pages.** The quickstart, SDK install page, and three how-tos have the most authority to pass — spend it deliberately. Two destinations, not one:
   - into the reference pages for symbols they use (closes the dead-end problem above from the other side), and
   - **at least one link each into the security/self-hosting cluster** (e.g., the quickstart's "before you go to production" pointing at the security page). This is the highest-leverage, lowest-effort fix on this list — it reuses pages you were already committed to editing to fix the buyer-facing cluster you can't see in analytics.
4. Cross-mode links: how-to → reference for symbols used, reference → how-to for the task, troubleshooting → the guide where the failure happens.
5. Real breadcrumbs matching the URL path.

## Step 6 — Page experience

Docusaurus + static hosting is usually fast; the regression is usually one addition. Check Core Web Vitals on three page types specifically — docs home, a long how-to, a reference page — since a domain average would hide a slow addition (embedded API explorer, unoptimized architecture diagrams) on just one of them.

## Fix list (ranked)

Counts marked "TBD" need Step 1's crawl output; everything else is already known from what you described.

| # | Fix | Pages affected | Fix | Owner | Effort |
|---|---|---|---|---|---|
| 1 | Blocking defects from Step 2 (robots/noindex conflicts, preview leakage, non-200s in sitemap) | TBD | per Step 2 | infra | 1–2h once found |
| 2 | **Link or delete the 47 orphans**; check `docusaurus build` log for "not in any sidebar" first | 47 | re-add to `sidebars.js` or delete | docs | 1 day |
| 3 | **Link the security/compliance/limits/self-hosting/migration cluster from quickstart + the 3 how-tos**, write descriptions for that cluster | small page count, hand-promoted past its ranked position — page-count ranking will always starve this | add prose links + front-matter descriptions | docs | 1–2 days |
| 4 | Reference → how-to cross-links for dead-end reference pages | TBD (the "link nowhere" set) | template change in the reference generator | docs/eng | 2–3 days (template), then free per new symbol |
| 5 | Title template rewrite (searched term first, brand last) | all 900, one config change | `docusaurus.config.js` themeConfig | docs | half day |
| 6 | Descriptions for quickstart, SDK install, 3 how-tos | 5 | front matter | docs | half day |
| 7 | Version posture alignment (pending Step 3 answer) | TBD | canonical/sitemap config | docs/infra | 1h–1 week depending on posture |

## Pass thresholds — proposed for a 900-page site

Not industry standard, this skill's own baseline, adjusted for your size (too big for 100% indexation to be realistic, too small for a 20k-page tree's looser bar):

- ≥95% of canonical docs URLs indexed
- 0 pages where Google chose a different canonical
- 0 non-200 URLs in the sitemap
- 100% unique titles
- **0 orphans** (currently 47 — this is the number to zero out)
- 0 indexed preview/retired-version URLs
- ≥90% of docs URLs passing Core Web Vitals
- **New, specific to your motion**: 100% of the security/compliance/limits/self-hosting/migration cluster internally linked from at least one top-traffic page, and 100% carrying a written description — a generic docs-SEO checklist won't include this row, your sales motion earns it one

Agree the exact numbers with whoever owns the fix pass before starting — that's what turns this into a finish line instead of an open-ended score.

## Coverage of this plan

Not verified in this session: no live crawl was run (no site/Search Console/repo access available here), so every "TBD" above is a placeholder for Step 1's actual output. What's already treated as confirmed: the 47 orphans and the dead-end reference pages, both stated directly rather than crawled.