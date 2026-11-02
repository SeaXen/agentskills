## Docs SEO review: hreflang set for docs.ardenvale.io

**Verdict:** Don't ship this set as-is. Five of the eight codes are invalid, `EU` isn't a hreflang concept at all, and the v2/v3 duplication conflicts with the skill's version rule. The header-vs-sitemap move is also based on a claim Google doesn't make — fix that before it becomes the delivery mechanism for a broken set.

**Coverage:** This is a desk review of the locale set and delivery plan as described — I haven't crawled docs.ardenvale.io. Before shipping, run the live check commands below against the actual pages.

### Blocking defects — invalid codes

Per Google's own localized-versions spec: an hreflang value is ISO 639-1 language, optionally + ISO 3166-1 Alpha-2 region. A region with no language, or a code from the wrong standard, is invalid — report as a defect, not a style note.

| # | Code | Problem | Fix |
|---|------|---------|-----|
| 1 | `eng` | ISO 639-2, not 639-1 | `en` |
| 2 | `en-uk` | `uk` isn't an ISO 3166-1 Alpha-2 region | `en-GB` |
| 3 | `jp` | ISO 3166-1 country code used as a language | `ja` (or `ja-JP` if you deliberately want the region qualifier) |
| 4 | `es-LA` | "Latin America" has no ISO 3166-1 code | bare `es` if the content is one shared Spanish variant, or real per-country codes (`es-MX`, `es-AR`, …) if it isn't |
| 5 | `EU` | region with no language prefix, and not a valid target region either way | delete — see below |
| — | `fr-FR` | valid, no change | — |
| — | `zh` | valid but ambiguous (Simplified vs Traditional) | prefer `zh-Hans` / `zh-Hant` |
| — | `pt` | valid as-is | confirm this isn't masking a pt-BR/pt-PT content split — that's a content question, not a defect |

`EU` deserves its own line: hreflang targets a user's language/region setting, not a trade bloc. There's no browser locale that resolves to "EU," so the annotation can never match anyone. If those landing pages are actually English-for-Ireland, German-for-Germany, etc., give them real `xx-XX` codes. If they're region-agnostic (pricing/currency, not language), hreflang is the wrong mechanism — that's a geo/IP or on-page selector, not an annotation.

Since the set is "generated straight from our locale config," fix it at the config level — this is a template-level bug reaching every page, not a per-page cleanup.

### Blocking defect — same set on v3 and archived v2

The skill's rule: *emit the set for canonical versions only — annotating archived versions creates members that are themselves canonicalized away.* If v2 is genuinely archived (canonicalized to v3, or noindexed), its pages shouldn't carry hreflang annotations at all — the annotations get discarded, and any cross-links from v3's mesh into non-canonical v2 URLs are wasted or actively confuse the return-link check.

Before shipping: confirm which version posture v2 is actually under (stable-canonical, latest-only, or still self-canonical as a supported release). If v2 isn't self-canonical, strip hreflang from it entirely — don't just reuse the v3 template.

### Check before shipping — x-default

The set as described doesn't mention `x-default`. Google's self-reference rule bundles it in: every language version must list itself, all the others, *and* `x-default` for the no-match case. Confirm the locale config emits a distinct `x-default` entry — it's not one of the eight real locales, it's a ninth, reserved value.

### The headers-vs-sitemap move

"Google recommends HTTP headers over sitemap entries once you're past a few thousand pages" isn't something Google states. Google's own position: HTML `<link>` tags, HTTP headers, and sitemap entries are **equivalent delivery methods**, with no stated preference tied to site size. Whoever read that should re-check the source — this may be a conflation with the (real, narrower) guidance that HTTP headers are the *only* option for non-HTML files like PDFs, since those have no `<head>` to put a `<link>` in. That's not your case.

If anything, the direction should go the other way. For a locale × version mesh, HTML `<head>` tags become an operational problem first (hundreds of tags per page), and the skill's own default is to move that weight into the **sitemap**, not into headers. Headers are the worse choice here operationally too:

- On a static Astro Starlight build, per-URL response headers mean either a hand-maintained header-rules file (Netlify `_headers`, Cloudflare `_headers`, etc.) enumerating every URL × locale combination, or standing up edge functions just to inject them — both a heavier, more failure-prone build than a generated sitemap file.
- Headers aren't visible in page source, so nobody can eyeball-check them; verification means `curl -I` per URL instead of one sitemap diff.
- A stale header (post-deploy drift) is invisible until someone specifically probes it; a stale sitemap entry shows up in the next crawl.

**Recommendation:** keep the sitemap as the delivery mechanism. Don't move to headers.

### Fix list

| # | Fix | Where | Owner | Effort |
|---|-----|-------|-------|--------|
| 1 | Correct the 5 invalid codes in the locale config (`eng`→`en`, `en-uk`→`en-GB`, `jp`→`ja`, `es-LA`→`es` or real per-country codes, drop `EU`) | i18n/locale config | docs build | <1h |
| 2 | Split `zh` into `zh-Hans`/`zh-Hant` | i18n/locale config | docs build | 1-2h, content-dependent |
| 3 | Add explicit `x-default` entry to the mesh generator | i18n/locale config | docs build | <1h |
| 4 | Stop emitting hreflang on archived v2 pages (or confirm v2 is genuinely self-canonical and give it its own self-contained mesh) | version/generator logic | docs build | 1-2h |
| 5 | Cancel the headers migration; keep sitemap delivery | platform/CDN plan | platform lead | 0h (don't build) |
| 6 | Regenerate the whole mesh after any locale/version change, verify bidirectional return links | build pipeline | docs build | ongoing |

Verify live once fixed: `curl -s <url> \| grep -i hreflang` per locale (or pull each generated sitemap and check the `<xhtml:link>` entries), confirming every entry lists itself, all siblings, and `x-default`, with matching return links both ways.