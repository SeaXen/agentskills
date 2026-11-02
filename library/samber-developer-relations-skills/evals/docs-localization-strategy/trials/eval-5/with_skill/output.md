# Quillstone Spanish docs: diagnosis and fix plan

Your reviews are mixed because the localization breaks the reader's search paths. It also launched without the ownership and freshness controls the plan needs. I haven't seen your analytics, the Spanish traffic, or the team. Every figure below is `ASSUMED` until you replace it with data.

## Why users can't find things

| # | What you did | Why users can't find things | Fix |
|---|---|---|---|
| 1 | Translated CLI flags (`--dry-run` became `--simulacion`) | ❌ This is the worst one. The flag doesn't exist in the binary, so copy-pasting fails. The `--dry-run` that appears in Stack Overflow answers, GitHub issues, and AI assistants no longer matches your Spanish docs. Searching the docs for the flag they know finds nothing. | Revert every flag, identifier, header, and config key to the original. Never translate them. If a Spanish gloss helps, put it beside the flag in prose. |
| 2 | Translated error messages | ❌ Users search for the string the product prints, and the product prints English. Natural Spanish text matches nothing they see in their terminal. | Quote errors verbatim as the product prints them, with the Spanish explanation beside them. |
| 3 | Spanish headings produced Spanish anchors | ❌ Links from support replies, English docs, issues, and other locales break. Anchors also differ between locales, so no one can share a deep link. | Keep anchors in the source language with explicit heading IDs, for example `## Webhooks {#retry-policy}`. The Nuxt Content/MDC setup may need a slug override. |
| 4 | Translated all 400 pages of API reference | ❌ Reference is generated and changes with every release, so it drifts fastest. Reference readers also look up exact identifiers, which translation obscures. | Leave reference in English. At most, translate the top-traffic pages. Facebook for Developers translated guides into 16 languages and left reference untranslated. |
| 5 | Redirect on `Accept-Language: es` | ❌ This traps readers in a locale. Crawlers send no language preference, so they see inconsistent content. | Remove the auto-redirect. Use a dismissible language suggestion plus a persistent switcher that remembers the reader's choice. |
| 6 | Indexed `/es/` on day one | ❌ Nobody had reviewed the pages, so unreviewed Spanish pages entered search, probably competing with and diluting the English results. | Set `noindex` on `/es/` until the first review pass is done. URL, canonical, and hreflang mechanics belong to `samber/developer-relations-skills@docs-seo`; hand them there. |
| 7 | Translated everything at once | ❌ Nothing is pinned to a source revision, so nobody can tell which Spanish pages are stale. Reviews likely include "this page says X, the product does Y." | See the freshness contract below. |

## Gaps you didn't mention that I would check

- **Owners:** do you have two named, fluent Spanish reviewers? If not, the locale fails the launch gate (Kubernetes' rule: nobody approves their own change). MDN removed German in 2022 as unmaintained.
- **Your product is probably English-only:** a Spanish quickstart that ends in an English console and English errors makes the reader switch languages mid-task. Is the product UI localized?
- **Spanish variant:** is the target es-ES or es-419? Say which.
- **Evidence the barrier was real:** was there a traffic, browser-language, or engagement signal before you translated? Country traffic share is not need. Reader preference splits, and MDN's 2024 survey found 62% of German-browser readers preferred English.
- **Payments-specific risk:** mistranslations hurt most on authentication, billing, quotas, deprecations, and parameter semantics. In a payments SDK that is a liability, not a style problem.
- **Quality damage:** published evaluations of LLM-translated READMEs found broken code, URLs, or Markdown in 16-50% of files. Check your code blocks, links, and fence counts.

## What to do (in order)

1. **This week, stop the bleeding:**
   - Add `noindex` to `/es/`.
   - Remove the `Accept-Language` redirect and add a suggestion banner plus a switcher.
   - Revert flags, CLI commands, and config keys to the original text.
   - Restore source-language anchors with explicit IDs, keeping redirects from the old Spanish anchors.
2. **Add a label to every Spanish page:** "Translated from English with AI assistance, [reviewed by NAME | not yet reviewed]. The English page is authoritative. Read it in English → · Report a translation problem →". Link a feedback channel.
3. **Cut the set to a critical-path pack.** Quickstart, install, authentication, the top task pages by traffic, and the site UI strings. Hold everything else, including the 400-page reference, and fall back to English for it with a visible "Read in English" link.
4. **Review by risk, not page order.** Security, authentication, billing, quotas, deprecations, and parameter semantics get human review before the pages return to search. A pack this small can be reviewed in full.
5. **Add the freshness contract.** Put these fields in each page's front matter:
   ```yaml
   source_path: docs/en/guides/webhooks.md
   source_commit: 3f9c2e1
   translated_on: 2026-10-02
   translation_method: human | llm-reviewed | llm-unreviewed | community
   reviewed_by: <name>
   ```
   Pin the source commit at the moment translation starts, not at HEAD. Never copy the source's `tested_with` or `last_verified` stamps into a translation. Run the drift check in CI with full git history:
   ```
   python3 scripts/translation-drift-check.py --source docs/en --locale es=docs/es --format csv --fail-on no-pin,unknown-pin --since <ref>
   ```
   Because the locale already exists, `--since <ref>` lets only pages added or edited after that ref fail the build while you pin the backlog. Show a banner on any `behind` page and fall back to English when a critical-path page goes `far`. Set `--far` from your commits per release.
6. **Close the ownership gate.** You need two named reviewers, a glossary with "do not translate" decisions, the pin field and drift check live, a written retirement threshold, a named person who can pull the locale, and published owner names with a contact.
7. **Mark the locale `gated` until step 6 closes.** Then re-submit `/es/` for indexing, and only after the first review pass.
8. **Set KPIs against a control** (Spanish-market readers on the English pages):
   - adoption: share of Spanish sessions staying on `/es/`
   - outcome: quickstart completion or time to first API call, before versus after
   - freshness: at least 80% of the critical-path pack current at every release (baseline)
   - quality: translation-problem reports per 1,000 views
   - kill rule: adoption or freshness below target for two consecutive quarters retires the locale, with redirects to English (baseline)

## Decision summary

| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| es | `gated` (reduced to a critical-path pack) | No evidence shown of a barrier; ownership unknown; reference, flags, errors, and anchors translated against the rules | Two named Spanish reviewers; Step 6 items closed; engagement data showing a Spanish-reader gap |

## Assumptions

- ASSUMED: no pins exist today, since you didn't mention any.
- ASSUMED: the product UI and CLI output are English-only.
- ASSUMED: you haven't yet checked browser-language share or quickstart completion for Spanish readers.
- ASSUMED: you have no named reviewers.

## Questions I need you to answer to finalize the plan

1. Does Spanish readers' quickstart completion differ from English readers' (baseline: a gap under about 5 percentage points shows no barrier; over about 10 shows one)?
2. Who reviews the Spanish pages, and how many hours per release can they give?
3. Is it es-ES or es-419, and do support tickets or posts arrive in Spanish?
4. How many source commits land per release? That sets the `--far` value.

## Source hardening for all readers

Plain global English, one term per concept, a glossary, `translate="no"` on code, and no idioms. This helps every non-native reader, cuts browser-translation damage, and makes any later translation cheaper.