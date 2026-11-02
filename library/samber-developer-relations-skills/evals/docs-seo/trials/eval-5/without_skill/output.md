# Hreflang review — issues before shipping

## 🔴 Invalid codes — Google will silently drop these

| Current | Problem | Fix |
|---|---|---|
| `eng` | Not ISO 639-1 (that's the 3-letter ISO 639-2 code); English's 639-1 code exists, so BCP47 requires it | `en` |
| `en-uk` | `UK` isn't a registered ISO 3166-1 region subtag — the assigned code is `GB` | `en-GB` |
| `jp` | `jp` isn't a language code at all — `JP` is the *country* code for Japan, not the language | `ja` |
| `es-LA` | `LA` isn't an ISO 3166-1 country code | `es-419` — the UN M.49 code Google's own hreflang docs cite for Latin American Spanish |
| `EU` | Hreflang only supports an ISO 639-1 language or an ISO 639-1+ISO 3166-1 language-country pair — no continent/supranational targets exist | Drop it. For EU landing pages, target real countries individually, or skip region-targeting and rely on language alone |

`fr-FR` is correctly formed. `zh` and `pt` are valid bare codes but ambiguous (Simplified vs Traditional, Brazil vs Portugal) — confirm that's intentional before locking the config. If `fr-FR`/`es-419` content isn't meaningfully different from a generic `fr`/`es` page, prefer the bare language tag: it matches a wider set of browser locales and it's one fewer value to keep in sync.

## 🟠 Missing x-default
Nothing catches users whose locale matches none of the targets. Add `x-default`, pointed at your primary version.

## 🔴 v3 and archived v2 emitting the "same set"
Two distinct failure modes hide behind that phrase:

1. **If the href targets are literally identical URLs in both versions** — a common Astro/Starlight bug when the hreflang partial isn't parameterized on the version segment — v2 pages lose their self-referencing tag and reciprocity breaks (every URL in a cluster must list every other URL *and itself*). Google treats a non-reciprocal cluster as unreliable and may ignore it.
2. **If v2 is meant to be archived (canonicalized or noindexed to v3)**, giving it its own independent hreflang cluster contradicts that signal — Google resolves hreflang through the canonical target, so tags on a non-canonical page are superseded at best, and at worst you're running two competing language graphs for versions that shouldn't both be eligible to rank.

Fix: decide v2's indexing status first. Archived and out of the index → canonicalize/noindex it and drop its hreflang entirely. Must stay independently indexable → give it its own self-contained cluster pointing only to v2 URLs, never shared targets with v3.

## 🟠 Headers-over-sitemap — check the source before migrating
This reverses Google's own documented guidance, not confirms it. Google recommends **sitemaps** at high page counts specifically because it avoids adding N `hreflang` entries to every single page's response — HTTP headers carry the exact same per-response `Link` overhead as HTML `<link>` tags, so moving from sitemap to headers at scale adds bytes per request rather than removing them. Headers are Google's recommended fix for *non-HTML* files (PDFs, etc.) where a `<link>` tag can't exist — not a scale optimization for HTML docs pages. Worth re-reading whatever your platform lead sourced that from.

If you still want headers on Starlight: remember it's static output, so `Link` headers aren't part of the generated files — they'd need to be added at the hosting/CDN layer (Netlify `_headers`, Vercel `headers()` config, Cloudflare Pages `_headers`), generated from the same locale data driving the pages, per URL × version × language. That's a build step to write and maintain, not a settings flip. During any transition, don't run sitemap and header annotations simultaneously with different values for the same URL — pick one method live at a time.

## ℹ️ Validation
Search Console's old "International Targeting" report (the one that used to surface hreflang errors directly) was retired in 2022. Validate the corrected set with the URL Inspection tool on sample URLs per locale, or a crawler (Screaming Frog/Sitebulb) that checks reciprocity across the full cluster, before rollout — don't rely on GSC catching a broken graph automatically.