# Kelvinstack docs SEO — canonical setup, 2026-09-23

## Verdict

Set up **per-version self-canonical for 4.2, 3.6 and 2.8, and noindex-only for 1.9** — not a single `stable`-alias canonical. Google is "picking whichever version it likes" because your four version trees currently send conflicting or absent canonical signals, not because per-version indexing is the wrong posture. Given the paid LTS contracts running to 2029 and the four years of external links landing directly on `/2.8/…` and `/3.6/…`, sending search traffic for a 2.8 query to the 4.2 page would be wrong for a paying LTS customer, not just suboptimal — that's the one case this skill's own ranking explicitly overrides "cheapest posture wins." The whole fix is template- and config-level, so it fits inside your routing freeze and the five weeks.

## Coverage of this audit

No live crawl was run against `docs.kelvinstack.io` — this response is written from what you've described, not from a `docs-seo-crawl.py` pass or Search Console data. Before you ship anything, run:

```bash
python3 scripts/docs-seo-crawl.py https://docs.kelvinstack.io/sitemap.xml --out pages.csv --summary
```

against all four version trees, and pull Search Console's **Pages** report filtered to `/2.8/`, `/3.6/`, `/4.2/`, `/1.9/` separately, plus the **"Duplicate, Google chose different canonical"** bucket — that bucket is the direct readout of whether the fix below actually worked.

Assumptions made below, flagged because the setup changes if any is wrong:

- **1.9 is not under an LTS contract** (only 2.8 and 3.6 are stated as paid). If 1.9 also carries a support commitment, move it into the same bucket as 2.8/3.6 below and drop the noindex.
- **Versions are built and deployed with `mike`** (the standard mkdocs-material versioning tool), each version as its own static sub-tree under `/{version}/`. If you use a different per-version build pipeline, the fixes still apply — only which file you edit changes.
- No locales were mentioned, so this ignores `hreflang` entirely. If Kelvinstack docs are translated, that's a separate pass — say so and I'll fold it in.
- No mention of a second host (`*.readthedocs.io`, `*.pages.dev`, a platform staging domain). If one exists, it needs the same canonical treatment as a fifth "version."

## Postures ruled out, and why

- **Stable-canonical is not available to you, on two independent grounds.** Mechanically, it requires a `stable`/`latest` alias path that every version canonicals to — that's a new path, which your routing freeze forbids outright. Substantively, even if the freeze allowed it, canonicaling 2.8 and 3.6 to 4.2 means a paying LTS customer searching for their own version's retry behavior gets served 4.2's docs in Google — which may describe a different API shape than what they're actually running. That's a support-commitment breach, not a minor ranking tradeoff. This is exactly the exception this skill calls out: *"Promote [per-version indexable] anyway when supported LTS releases carry real traffic, or when a support commitment obliges you to serve each release's own page."* 2.8 and 3.6 are both.
- **Latest-only (noindex everything but 4.2) is deleted for the same reason**, applied to the whole tree instead of just 1.9: it would remove 2.8 and 3.6 from search entirely, contradicting a contract you're being paid to honor and burning four years of inbound links that currently land people on the right version.
- **Per-version indexable for all four, including 1.9,** is deleted because nothing obliges you to keep an unsupported version competing for search real estate against the three you do support — every additional indexed version is duplicate-content surface with no compensating traffic or contract behind it.

What's left is a hybrid, scoped per version rather than applied uniformly — which the skill explicitly allows: *"Re-rank against what you already know: … an existing per-version URL set with years of inbound links all change the answer."*

## The canonical setup

| Version | Canonical target | Indexable | Sitemap | Reasoning |
|---|---|---|---|---|
| 4.2 (current) | self (own URL) | yes | included | current release, no conflict |
| 3.6 (paid LTS to 2029) | self (own URL) | yes | included | contract obliges a real page for this exact release; 4-yr inbound links must keep resolving to matching content |
| 2.8 (paid LTS to 2029) | self (own URL) | yes | included | same as 3.6 |
| 1.9 (no LTS contract) | self, but `noindex` | no | excluded | no support commitment to defend in search; page stays live for anyone with a direct link |

No URLs move. `/1.9/guides/retries/` stays served at that exact path — it just stops competing for the query.

## Blocking defects to clear before anything else lands

These override the canonical work if they exist — a `noindex` or canonical tag that's never crawled is worthless. Verify each with the crawl script and `curl -I`, in this order:

1. **`robots.txt` must not disallow `/1.9/`.** If you noindex 1.9 *and* block it in robots.txt, the noindex is never read and 1.9 stays indexed as a bare URL forever — the single most common self-inflicted version of this exact bug.
2. **Confirm the canonical tag is present in the raw HTML, not injected by JS.** MkDocs Material renders it server-side by default, but if any custom `extrahead` override moved it into a client-side script, it won't be read.
3. **Confirm the sitemap and canonical tags currently agree with each other**, per version, before you touch anything — this tells you whether today's "Google picks whichever it likes" is a *missing*-canonical problem, a *wrong*-canonical problem (e.g. `site_url` statically baked into `mkdocs.yml` so every version's canonical accidentally points at the same URL — a known `mike` + Material footgun when `site_url` isn't set per build), or a sitemap-vs-canonical mismatch. The fix differs by cause; the crawl output tells you which one you have.
4. **Check for a staging/preview host** (`*-preview.*`, a PR-build subdomain). Not mentioned, but worth one `curl -I` before you conclude versions are the only duplicate-content source.

## Implementation, within the routing freeze

Nothing here adds a path or alias — every change is a template block or a build-config value.

- **Self-canonical (4.2/3.6/2.8):** Material for MkDocs already emits `<link rel="canonical">` from `page.canonical_url`, computed as `site_url + page.url`. If today's canonicals are wrong or absent, the likely cause is `site_url` in `mkdocs.yml` not being set per version build. Fix at the CI step that invokes `mike deploy`/`mkdocs build` for each version, so each build's `site_url` resolves to that version's own base (`https://docs.kelvinstack.io/2.8/`, etc.) — a build-config change, not a route.
- **Noindex on 1.9 only:** add a conditional block to `docs/overrides/main.html`'s `extrahead` block — `{% if mkdocs_version == "1.9" %}<meta name="robots" content="noindex, follow">{% endif %}` (or equivalent, keyed off whatever variable your `mike`/CI setup exposes per build). `follow` matters: you still want link equity to flow from 1.9's pages, since some of those links point at the pages you *do* want indexed.
- **Sitemap:** MkDocs's built-in sitemap generation has no native per-page exclusion flag. Confirm first whether you publish one combined sitemap or a per-version sitemap under each `/{version}/sitemap.xml`. If combined, add a small build hook that drops `/1.9/*` entries before the file is written. If per-version, simply don't reference 1.9's sitemap from any sitemap index and don't resubmit it in Search Console.
- **In-page version banner**, on 1.9, 3.6 and 2.8 alike — Material's version-warning feature (triggered off the `mike` "latest" alias comparison, customizable via the `outdated` block in `main.html`) covers this if you're already on a recent Material release; otherwise it's a one-block template addition. Ship this regardless of the canonical/noindex split — it fixes the human half of the problem the canonical tag doesn't touch, and it's the cheapest line in this whole list.
- **Title template:** keep the version in the title for 4.2/3.6/2.8 (they're all separately indexable and a searcher needs to know which release they're looking at), drop it from 1.9 since it no longer needs to read well in a result. Shape: `{page title} — v{version} | Kelvinstack Docs`, not the reverse.

## Fix list, ranked and owned

| # | Fix | Pages affected | File / system | Owner | Effort |
|---|---|---|---|---|---|
| 1 | Confirm robots.txt doesn't disallow any version path | all | `robots.txt` | platform | 15 min |
| 2 | Per-version `site_url` at build time, so 4.2/3.6/2.8 self-canonicalize correctly | ~all 4.2+3.6+2.8 pages | CI build step / `mkdocs.yml` | platform | 1–2 days |
| 3 | Conditional `noindex` on 1.9 build only | all 1.9 pages | `docs/overrides/main.html` | platform | 2–3 hrs |
| 4 | Exclude 1.9 from any combined sitemap / sitemap index | 1.9 URLs | sitemap build hook | platform | half day |
| 5 | "You're viewing an old version" banner, 1.9/3.6/2.8 | all non-4.2 pages | `main.html` `outdated` block | platform | half day |
| 6 | Version-tagged title template for indexable versions | 4.2/3.6/2.8 | title template | platform + docs writers (copy) | half day |
| 7 | Re-crawl all four trees, diff canonical/sitemap agreement | all | `docs-seo-crawl.py` | platform | 2 hrs |
| 8 | Submit/verify in Search Console per version prefix, watch the "different canonical" bucket | all | Search Console | platform | ongoing |

Items 1–4 are the ones that actually change what Google resolves; 5–6 are the signals that make the result legible to a human once search sends them to the right page.

## Five-week plan

- **Week 1:** run the pre-flight crawl and robots/JS checks (blocking-defect checklist above); confirm the `site_url`/build-pipeline root cause with the platform team.
- **Week 2:** ship fix #2 (per-version canonical) to a staging build of all three indexable versions; verify with `curl` that each version's canonical now points at itself, not at 4.2 or at nothing.
- **Week 3:** ship #3 and #4 (1.9 noindex + sitemap exclusion) in the same deploy — per the skill's own rule, update the sitemap in the same push that changes indexability, or the sitemap keeps advertising URLs you no longer want indexed.
- **Week 4:** ship #5 and #6 (banner, titles); submit the updated sitemaps in Search Console for all three indexable versions.
- **Week 5:** re-run the crawl, diff against week 1's summary, and start watching the "Duplicate, Google chose different canonical" bucket weekly — that number won't hit zero inside five weeks (re-indexing runs on Google's schedule, not yours), but it should be trending down by the time you report this as shipped.

## Thresholds to agree before the fix pass

These are this skill's baselines, adjusted for a four-version, moderate-page-count docs site — not sourced requirements, so negotiate them, then hold to them:

- ≥95% of 4.2/3.6/2.8 canonical URLs indexed (measured per version prefix in Search Console)
- 0 pages where Google chose a different canonical, per version
- 0 indexed 1.9 URLs (`site:docs.kelvinstack.io/1.9/` should trend to zero over subsequent months — this doesn't happen in five weeks, only the noindex ships in five weeks)
- 100% unique titles across all three indexable versions
- 0 non-200 URLs in any version's sitemap

Report indexing/ranking movement as pending after week 5, not promised — the deploy is verifiable in this window, Google's re-crawl and re-ranking are not.