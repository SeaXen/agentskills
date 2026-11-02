## Canonical setup for Kelvinstack docs (4 versions, routing freeze, 5-week window)

### The core decision

**Self-referencing canonicals on every indexable version. Do not canonicalize 2.8/3.6/4.2 into each other.** noindex the one version that isn't earning its keep (1.9). This is the opposite of the textbook "duplicate content → consolidate into one canonical" move, and that's deliberate: your business constraint (2.8 and 3.6 must independently rank, not just resolve) overrides the default SEO instinct. Sites with the same shape — Kubernetes, Terraform, Django — run this exact pattern at larger scale.

Canonicalizing LTS versions into 4.2 would "fix" the duplicate-content signal but actively break the thing you're paying LTS contracts to support: someone on 2.8 searching your own docs would land on 4.2 content that may not match their running version. That's a worse outcome than the current flapping.

### Per-version treatment

| Version | Canonical | Meta robots | In sitemap | Rationale |
|---|---|---|---|---|
| 4.2 (current) | self | index, follow | yes | primary version |
| 3.6 (LTS→2029) | self | index, follow | yes | contractual + ~session share requires independent ranking |
| 2.8 (LTS→2029) | self | index, follow | yes | same |
| 1.9 (legacy) | self | **noindex, follow** | **excluded** | no contract backing it; stop diluting the ranking signal for the three that matter |

Confirm with me/your team: is 1.9 genuinely EOL with no support commitment? If it still has real paid usage, don't noindex it — the table assumes it's the tail nobody's contracted for.

### Why Google is currently "picking whichever it likes"

That behavior (GSC calls it "Duplicate, Google chose different canonical than user") almost always means one of two things is true today, and it's worth confirming before you write a line of config:

1. **No canonical tag is being emitted per version at all**, or
2. **`site_url` in `mkdocs.yml` isn't version-scoped**, so every build's generated canonical resolves to the same URL pattern regardless of which version was actually built — Material for MkDocs derives `<link rel="canonical">` directly from `site_url` + page path, so if all four version builds share one `site_url`, they're all telling Google "the real URL is this one," and Google is just doing what you told it to.

Check this first: `curl -s https://docs.kelvinstack.io/2.8/guides/retries/ | grep canonical` against the same for 3.6 and 4.2. If they all print the same href, that's your root cause, and the fix below resolves it directly — no redirect, no new path, config only.

### Implementation (mkdocs.yml + templates only — compliant with the routing freeze)

**Fix `site_url` per version build.** Each version's own `mkdocs.yml` (or the per-version config `mike`/your build pipeline injects) needs:
```yaml
site_url: https://docs.kelvinstack.io/2.8/
```
— literally the version's own prefix, per version. This alone makes every page self-canonicalize correctly; Material computes `page.canonical_url` from this and already emits the `<link rel="canonical">` tag in `base.html`, so no template edit is needed for this part.

**Noindex 1.9 via a template override**, not robots.txt. Add to 1.9's `mkdocs.yml`:
```yaml
extra:
  version_noindex: true
```
and in an overridden `main.html` block:
```html
{% block extrahead %}
{{ super() }}
{% if config.extra.version_noindex %}
<meta name="robots" content="noindex, follow">
{% endif %}
{% endblock %}
```
Use `noindex, follow`, not `robots.txt: Disallow`. Disallow blocks crawling entirely, which means Google can't even see the noindex directive or pass link equity from four years of external backlinks through those pages. `noindex, follow` drops it from the index while keeping the URL fully resolvable and crawlable — zero impact on the external links you can't touch anyway.

**Add a real, server-rendered version banner link** on 2.8 and 3.6 pages (and optionally 1.9), pointing to the equivalent page on 4.2:
```html
{% if config.extra.version_label != "4.2" %}
<p class="kelvinstack-version-banner">
  You're viewing docs for {{ config.extra.version_label }}
  (LTS, supported through 2029).
  <a href="https://docs.kelvinstack.io/4.2/{{ page.url }}">View the latest (4.2)</a>.
</p>
{% endif %}
```
Must be a real `<a href>` in the HTML, not injected by the version-switcher JS — Google needs to see it without executing JS to understand the relationship between versions. This doesn't create a new path (it links to an existing stable URL), so it's inside the freeze.

**Differentiate titles**, one line in the page template:
```html
<title>{{ page.title }} — Kelvinstack {{ config.extra.version_label }}</title>
```
Cheap insurance against near-identical `<title>` across versions reinforcing the "these are duplicates" signal.

### Sitemap and robots.txt

- Leave Material's auto-generated per-version `sitemap.xml` in place (already exists at each version's own path — not a new path). For 1.9, either let Material's own noindex-aware sitemap generation drop those URLs automatically (recent Material versions do this) or, if it doesn't in your version, exclude 1.9 pages from that build's sitemap generation config.
- `robots.txt` (existing file, editing content only): keep all four version paths crawlable — do **not** add a `Disallow` for 1.9. The noindex meta tag is the removal mechanism; robots.txt disallow would prevent Google from ever seeing that tag.
- If `robots.txt` already lists multiple `Sitemap:` lines, make sure 1.9's sitemap URL stays listed (Google still needs to crawl those pages to read the noindex tag and follow their links) — you're just not making it a ranking target.

### 5-week rollout

- **Week 1** — Confirm root cause: diff canonical output across the four live versions, check GSC Coverage for "Duplicate, Google chose different canonical" grouped by URL prefix, confirm 1.9's actual usage/support status.
- **Week 2** — Land `site_url` fix per version, template changes (noindex block, version banner, title suffix) in a branch. Build all four versions locally, diff rendered HTML `<head>` against the table above.
- **Week 3** — Deploy to production (rebuilding existing versions' output isn't a routing change — no new paths created). Submit/refresh sitemaps in GSC for all four version prefixes.
- **Week 4** — In GSC, request validation on a sample of 1.9 URLs (Coverage → noindex) and request indexing on a handful of representative 2.8/3.6/4.2 URLs to accelerate recrawl rather than waiting on natural crawl budget.
- **Week 5** — Check GSC Performance filtered by URL prefix (`/2.8/`, `/3.6/`, `/4.2/`, `/1.9/`): confirm impressions on 2.8/3.6 hold or recover, confirm 1.9 impressions trending down as "Excluded by noindex tag" count rises, confirm the "chose different canonical" flag count drops toward zero.

### What "done" looks like

- Every 2.8/3.6/4.2 URL self-canonicalizes and GSC's canonical-mismatch flag clears for those prefixes.
- 1.9 URLs still return 200 (external links keep working) but drop out of the index over 2-4 weeks post-noindex.
- No new paths, aliases, or redirects were touched — everything above is `mkdocs.yml` + template edits, so it ships inside the platform team's freeze.