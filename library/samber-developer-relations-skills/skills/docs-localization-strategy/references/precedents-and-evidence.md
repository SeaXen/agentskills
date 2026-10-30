# Precedents and evidence

Read when choosing a rung, citing a precedent to a stakeholder, or deciding whether a threshold is sourced or a baseline.

## Contents

1. Precedents compared
2. MDN Web Docs: freeze, cut, LLM revival
3. Kubernetes launch checklist
4. Vendor pipelines
5. Reader-preference evidence
6. Machine and LLM translation quality
7. Measured staleness
8. Sourced versus baseline figures

## 1. Precedents compared

| Project | Model | Launch threshold | Ownership | Drift mechanism |
| --- | --- | --- | --- | --- |
| MDN Web Docs | Community locales + one LLM-translated locale (de) | At least one community lead per locale | Maintainers listed per locale | `l10n.sourceCommit` in front matter |
| Kubernetes | Self-sufficient community teams | Two or more contributors + minimum content set | Locale-scoped owners and reviewers teams in OWNERS files | `upstream_changes.py` and `diff_l10n_branches.py` diff against English |
| Python (PEP 545, devguide) | Community teams, gettext PO files | 100% of `bugs`, `tutorial/`, `library/functions` before the language switcher | Coordinator per language; Editorial Board per the devguide | gettext fuzzy marking; untranslated strings fall back to English, so a partial translation can publish |
| react.dev | One repo per language | Main content + UI translated before deploy | Maintainer list per repo, escalation repo | Progress issues, translation dashboard |
| Vue | Community repos per language | Not formal | Repo maintainers | "Checkpoint" (synced English commit), reader-facing status UI, auto sync issues |
| Comprehensive Rust (`mdbook-i18n-helpers`) | gettext over mdBook | Per project | Per project | `msgmerge` fuzzy marking, `i18n-report` |
| Microsoft Learn | MT augmented with GPT models, some human localization | Vendor | Vendor | "Read in English" toggle, English fallback |
| GitLab Docs | AI pipeline + automated post-edit + partial human review | ja-JP only at launch | Globalization team | Progress dashboard |
| Google Cloud | MT with a banner naming the translation API | Vendor | Vendor | Locale parameter, "translation issue" feedback |
| Facebook for Developers (2017) | Guides in 16 languages | - | - | Reference untranslated "at this time" (a status, not a stated policy) |

The community precedents with written launch rules (MDN, Kubernetes, Python, react.dev) require a named owning team before a locale ships. Every large vendor keeps the source language authoritative and says so on the page.

Volunteer supply often precedes planning: its maintainer reports the first Comprehensive Rust translation arrived unprompted about two weeks after publication.

## 2. MDN Web Docs: freeze, cut, LLM revival

- December 2020: every locale frozen read-only on the new platform. The announcement framed it around the platform launch and doubts about automated translation; the March 2021 follow-up added that unmaintained locales confused readers between their locale and English.
- Early 2021: locales with at least one community lead unfrozen for editing (fr, ja, zh-CN, zh-TW, then ru). Display retention judged by each locale's share of total traffic: 11 kept, counting en-US, including es, pt-BR, ko, de and pl, which stayed frozen without a lead.
- 30 April 2021: the other 21 locales stopped displaying, with an estimated traffic loss under 2%. Their URLs redirect to English. Retirement declared one-way.
- August 2022: German removed as incomplete, outdated and unmaintained.
- November 2024: German revived as an LLM-translated locale - 12,500+ pages, code blocks masked with placeholders, daily pipeline, an "experiment, may contain inaccuracies" notice, a remembered language opt-out, feedback buttons, kept out of search for about a month before indexing.

## 3. Kubernetes launch checklist

- At least two contributors, because contributors cannot approve their own pull requests; the team must be self-sufficient.
- Minimum content: Home, Setup, the Basics and Hello Minikube tutorials, all site strings, Releases.
- Localized README with a contact, localized code of conduct, a repository label, a language block in the site config.
- Owners approve changes only inside their locale directory.
- Contributor guide: "Machine-generated translation is insufficient on its own."

## 4. Vendor pipelines

- **GitLab ja-JP:** translation management system + LLM + automated post-editing + terminology management + UI-label integration. Excluded images, diagrams and the contributor section. Disclaimer: English authoritative, Japanese "for reference only", some content not yet human-reviewed.
- **Microsoft Learn:** GPT models augment machine translation; quality measured with metric models; "Read in English" toggle; some pages state translations are for convenience with the English version definitive; feedback by form.
- **Azure Translator transparency note:** escalate a machine-translated item to human review once it passes a page-view threshold. This is guidance to MT customers, not a description of how Microsoft Learn runs. The same note claims MT costs under 1/1,000th of human translation (self-reported).
- **Google Cloud:** banner naming the translation API, "translation issue" feedback option.

## 5. Reader-preference evidence

- **MDN, June 2024:** survey shown to readers whose browser preferred German (60,000+ saw it, 1,900+ completed). 62% preferred English, 35% German. Top requirements: technical correctness 89%, consistent terminology 73%, freshness 68%. A third of native German speakers rated their English below fluent, and German preference rose as English fluency fell. The survey ran on English-language pages, so German-only readers are likely under-represented: 62% is probably an upper bound on English preference. MDN launched an LLM-translated German locale afterwards.
- **Guo, CHI 2018** (840 programming learners, 86 countries): a "prefer English over translations" theme in 7% of coded answers; native-language demand concentrated on learning material.
- **Bhuiyan, Bala Kumar, Staicu, ICSE 2026:** across 9.14 billion GitHub issues, pull requests and discussions, non-English content rose from 4.2% (2015) to 11.3% (2025); repositories with non-English documentation from 3.7% to 13.0%.
- **Search substitutes:** Google may machine-translate titles and snippets of foreign-language results into a list of 21 languages that has excluded Japanese and Chinese; check the current list. It substitutes for discovery, not for reading the page.
- No published study measures rankings, sessions or revenue gained from translated developer docs. Treat SEO-uplift claims for docs as unproven.

## 6. Machine and LLM translation quality

- **Adejumo, Guizani, Vares, Johnson** (arXiv 2508.02497, current version): two LLMs translated 50 READMEs from repositories with over 10,000 stars and forks. Manual validation found structural inconsistencies in 16% of files for one model (URLs 14%, code 2%, Markdown 8%) and 50% for the other (URLs 32%, code 18%, Markdown 24%), while semantic quality scores ran 94-96%.
- Harm concentrates where a mistranslation changes behaviour: security guidance, parameter semantics, deprecations, quotas and billing.

## 7. Measured staleness

- MDN zh-CN, 2026 contributor scan of 14,577 English pages: 7,010 untranslated, 3,070 lagging, 3,368 missing the source-commit field, 1,129 in sync (about 8%).
- MDN es, contributor re-check: 46 pages marked "completed", none current - most lacked the source-commit field.
- A pin field nobody enforces decays into absence. Enforce it in CI.

## 8. Sourced versus baseline figures

| Figure | Status |
| --- | --- |
| Two reviewers per locale | Sourced - Kubernetes (self-approval rule) |
| Critical-path content before launch | Sourced - Kubernetes, Python, react.dev |
| Reference left untranslated | Sourced - Facebook for Developers, 2017 status |
| Code masked before LLM translation | Sourced - MDN |
| Review triggered by page views | Sourced - Azure Translator transparency note |
| 62% prefer English | Sourced - MDN 2024, one locale, likely upper bound |
| Under 2% traffic lost cutting 21 locales | Sourced - MDN 2021, an estimate |
| Browser-language share under half the combined share of countries where the language dominates = weak sign readers use another browser language | Baseline |
| Engagement gap under 5 points = no barrier, over 10 = barrier | Baseline |
| 15-30 min per changed page, 1 h per page on first review, 1 page-equivalent per 300 UI strings | Baseline |
| 80% of the critical-path pack current at each release | Baseline |
| Retire a page `far` for two releases or 180 days | Baseline |
| Retire a locale after two quarters below target | Baseline |
| `far` = more than 5 source commits since the pin | Baseline, `--far` default |
| Vendor pipeline with an independent quality reviewer meets the two-reviewer item | Baseline |
