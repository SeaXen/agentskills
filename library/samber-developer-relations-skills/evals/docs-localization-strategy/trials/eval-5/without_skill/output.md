# Why Spanish Quillstone docs are hard to use

I haven't seen your site or analytics, so this is a diagnosis from the setup you described. The biggest cause is that you translated things that must stay verbatim.

## 1. You translated strings users have to type or search for (biggest cause)

- **CLI flags.** Unless the CLI really accepts `--simulacion`, the docs now show a flag that doesn't exist. Users copy it, get `unknown flag`, and lose trust in the whole page. Even if you add an alias, every Stack Overflow answer, GitHub issue and teammate's snippet says `--dry-run`.
- **Error messages.** Your SDK emits what it emits, probably English or a code. If the docs show a natural-Spanish paraphrase, nobody can paste the real error into search and land on the page. Error lookup is the main way people use payment-SDK docs.
- **Other literals.** Check that you didn't translate any of these:
  - API fields and enum values
  - Endpoint paths
  - Config keys
  - Code comments and sample output
  - Event names

  Any translated literal is a bug in the docs.

## 2. Spanish anchors break links and cross-language navigation

- Every existing deep link to an English heading (from issues, Slack, blog posts or the dashboard) lands at the top of the page, or nowhere, in Spanish.
- The language switcher can't map `#webhooks-signature` to `#firma-de-webhooks`, so it drops users at the top of the page.
- Any heading edit by a translator silently changes the anchor and breaks inbound links.

## 3. The Accept-Language redirect fights how developers work

- Many Spanish-speaking developers have a Spanish browser but prefer English technical docs. You force them into `/es/` with no obvious way back.
- Check three things:
  - Does the redirect keep the deep path, or send everyone to `/es/`?
  - Is it a 301 (cached forever) or a 302?
  - Does it override the user's choice on every visit?
- Without `Vary: Accept-Language`, a CDN may serve one variant to everyone.
- Someone clicking an English Google result or a pasted English link and getting bounced is a classic "can't find stuff" complaint.

## 4. The SEO setup is probably weak

- **Missing signals.** Look for:
  - Reciprocal `hreflang` tags with `x-default`
  - Correct self-referencing canonicals
  - A separate `/es/` sitemap
- **Indexing day one.** You exposed about 400 new pages with no authority, partly duplicated or mixed-language content, and (if the translation was machine-made) possible thin-content signals. Rankings are typically poor at first.
- **Search behavior.** Developers search technical terms in English ("webhook signature verification", "idempotency key"). Your Spanish pages rank for queries few people type. Meanwhile the English pages still win the queries people do type, then the redirect bounces the visitor away.
- **Rendering.** Confirm Nuxt is serving SSR or prerendered HTML for `/es/`, not client-rendered content. Confirm the locale is in the URL, not just a cookie.

## 5. On-site search probably doesn't handle the split

- If you use Algolia/DocSearch or similar, the index may be English-only or mixed. A search for "dry-run" won't match `--simulacion` and vice versa.
- Build one index per locale. Make each locale also match the verbatim English literals.

## 6. Translation quality and drift

- A 400-page reference has no review path unless you built one. Page-level staleness shows up as wrong parameters after the next SDK release.
- Mixed pages (Spanish prose, English code and errors) read inconsistently unless the rule is explicit.

## Fix plan, in order

1. **Revert literal translations.** This is the same-day fix.
   - Restore flags, error strings, fields, endpoints and code to the real values.
   - Keep Spanish only in explanations, e.g. "`--dry-run`: simula la operación sin ejecutarla".
   - If you want a Spanish alias, ship it in the CLI first.
2. **Pin stable anchors.** Give headings explicit English slugs (`## Firma de webhooks {#webhook-signature}`). Old English links then work in both locales.
3. **Replace the forced redirect with a suggestion.**
   - Show a dismissible "Ver en español" banner.
   - Never redirect deep links.
   - Remember the user's choice in a cookie.
   - Add `Vary: Accept-Language` if you keep any redirect, and use a 302.
4. **Fix the SEO plumbing.** Add reciprocal `hreflang` plus `x-default`, canonicals, and a locale sitemap. Add `noindex` to pages that are stale or only partly translated until they're reviewed.
5. **Fix search.** Use per-locale indexes with English literals as searchable aliases. Add a synonym or redirect layer so English error strings find the Spanish page.
6. **Rethink scope.** Translate the guides, quickstarts and conceptual pages. Leave the API reference in English, or translate descriptions only, with signatures untouched and a link to the English original. This cuts maintenance on 400 pages sharply.
7. **Add a freshness process.** Show a translated-from version, flag pages whose English source changed, and fail CI when a code block or flag differs from the English source.

## How to confirm before you change things

- Search Console: Spanish-country queries and clicks for `/es/` against English pages.
- Site search logs: zero-result queries, split by locale.
- 404s and bounce rate on anchors and on redirected deep links.
- Support tickets and reviews: tag them by cause ("flag didn't work", "couldn't find error", "kept getting sent to Spanish").
- A manual test: paste three real SDK error messages into Google and your site search, and see whether the Spanish page appears.

I expect items 1 to 3 to explain most of the complaints, since they directly break copy-paste, error lookup and linking.