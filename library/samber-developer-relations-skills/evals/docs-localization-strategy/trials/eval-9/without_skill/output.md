**Next action:** Ask the Riyadh reseller which 5–10 pages the three prospects read. Tier 1 below depends on that answer. It takes 10 minutes.

I did not open the repo, so this scope comes from Docusaurus i18n behavior I know and from your brief. Items marked ⚠️ need checking.

## Recommendation

Ship `ar` as a partial locale: Tier 1 (about 40 pages) first, the other 140 later. Machine translation drafts it and Omar reviews. Do not translate all 180 pages up front. Nobody has shown that deals need them, and every translated page adds maintenance.

## Scope

**In scope**
- Docusaurus i18n locale `ar`, RTL (`direction: 'rtl'`), Modern Standard Arabic.
- Language switcher in the navbar, `hreflang` tags, and an `/ar/` sitemap.
- Arabic font (e.g. IBM Plex Sans Arabic or Noto Naskh), self-hosted.
- An EN→AR glossary, signed off by Omar.
- A stale-translation check in CI.
- A banner on every Arabic page: "Console and CLI output are English."

**Out of scope**
- Console and CLI strings, error messages, and the CLI `--help` output.
- Translating the blog and changelog.
- Translating old doc versions. Translate `current` only.
- Arabic video or voiceover.
- Marketing site.

## Rules for the translators

1. Keep verbatim in English: commands, flags, config keys, error strings, and console UI labels. Console and CLI output stay English, so users will search for the English text.
2. Cite a UI label as English with an Arabic gloss on first use, e.g. `Restore Points` (نقاط الاستعادة).
3. Code blocks stay LTR. Wrap inline English inside Arabic sentences so the bidi (mixed-direction) order doesn't break.
4. Screenshots stay English. Diagrams with text labels need a decision from you: re-export in Arabic or leave English. I recommend leaving them English.
5. Digits: ask Omar. Western digits are the usual choice in technical content.

## Page tiers

| Tier | Pages (est.) | Content |
|---|---|---|
| 1 | ~40 | Overview, install, quickstart, core concepts (backup, restore, retention, encryption), security, compliance, data-handling pages, FAQ |
| 2 | ~60 | Admin guides, CLI reference prose, integrations |
| 3 | ~80 | Long tail, API reference, troubleshooting, release-specific pages |

Page counts are guesses until the reseller answers. Tier 1 should follow what the prospects read, not this table.

## Effort

| Phase | Work | Estimate |
|---|---|---|
| 0. Spike | Add the `ar` locale, RTL, font, switcher. Translate 3 pages end to end. Check search, code blocks, and tables. | 1 day engineering |
| 1. Tier 1 | MT draft, then Omar's review. Glossary first (about 2 h of his time). | Review: 12–16 h Omar, about 2 weeks at 6–8 h/week. Engineering: 1–2 days for build, CI, and banner. |
| 2. Tiers 2–3 | Same pipeline. Gate on Tier 1 feedback and deal outcomes. | Review: 30–45 h Omar. |
| Ongoing | Re-review pages whose English source changed. | 2–4 h/month Omar |

Review speed is an assumption: about 3 pages/hour for careful technical review. Omar is an SE, not a translator, so measure his real speed on the 3 spike pages and re-plan from that. MT cost is negligible. Omar's time is the real constraint.

## Risks

- ⚠️ **Search.** Algolia DocSearch needs a per-locale facet filter for `ar`. Built-in local-search plugins handle Arabic poorly. Check which one you use in Phase 0.
- ⚠️ **Fallback.** Docusaurus should serve the English page when no Arabic file exists. Confirm on a Tier 3 URL in the spike. Without it, links from Arabic pages to untranslated pages will break.
- **Drift.** English edits make Arabic pages stale. Mitigation: store the source commit hash in each Arabic page's frontmatter. A CI job warns when the English file has changed since. Crowdin is overkill for one locale and one reviewer.
- **Legal and compliance pages.** Omar can review the technical content, but I would have a native legal or compliance reviewer check wording that carries contract meaning. Ask the reseller whether they will do it.
- **Mixed-language experience.** Prospects will hit English console screens right after Arabic docs. The banner and the English-labels-with-gloss rule soften this. They do not remove it.
- **Deal assumption.** Nobody has verified that Arabic docs close the deals. The blocker could be data residency or a compliance questionnaire. Ask the reseller directly, and get it in writing if you can.

## Decisions I need from you

1. Which pages do the three prospects read? Ask the reseller.
2. How many hours per week can Omar give, and starting when?
3. Do you have a deal deadline? A hard date would force Tier 1 only.
4. Which search provider do the docs use?
5. Are old doc versions live? If so, confirm Arabic covers `current` only.

## Success check (Phase 1, 4 weeks after launch)

- Reseller confirms the Tier 1 pages cover what prospects asked for.
- At least 1 of the 3 deals cites the Arabic docs as helping.
- Zero broken `/ar/` links in CI, and no English-only banner visible on Tier 1 pages.
- Omar's measured review rate is within 30% of the estimate. If it isn't, re-plan Phases 2–3.

**Next:** send the reseller question (decision 1) and pick the Phase 0 spike date.