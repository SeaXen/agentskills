# Docs localization plan: Lanternfish, pt-BR, 2026-10-30

**Answer: say yes, scoped.** Accept the two PRs and a first batch of about a dozen pages, not "the rest of the docs". Merge the PRs today with the locale switched off. Turn it on once a short checklist closes. Your not reading Portuguese is manageable if you swap judging the prose for CI checks on structure and code, plus a second Portuguese reader.

I couldn't run the skill's one-question-at-a-time interview, so every gap below is marked `ASSUMED`. Reply with the numbers and I'll re-run the plan.

## Stored context
- Locale: `pt-BR` (São Paulo contributors). Decision: `gated`.
- Rung: critical-path pack, run as a community program. Source hardening applies everywhere.
- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift check: `translation-drift-check.py` in CI, with `--fail-on no-pin,unknown-pin`.
- Kill rule: adoption or freshness below target for two consecutive quarters retires the locale.
- Person allowed to pull the locale: you.

## Assumptions
- `ASSUMED` Both contributors are fluent in Brazilian Portuguese and will each review the other's work.
- `ASSUMED` Together they have about 6 reviewer hours per release.
- `ASSUMED` About 3 of the first-batch pages change per release.
- `ASSUMED` Docs are the current version only, with no older versions to translate.
- `ASSUMED` You have no data yet on Brazilian traffic, browser language, quickstart completion or Portuguese support posts.
- `ASSUMED` The CLI and error messages are English only.
- `ASSUMED` The two PRs are in `i18n/pt-BR/docusaurus-plugin-content-docs/current/` and have no pin fields.

## Decision summary
| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| pt-BR | gated | Two fluent volunteers are offering, which is the case where a community program is promoted. The need is not yet measured, and the launch gate is not yet closed. | All six gate items below close. Reopen the scope question if the engagement check shows no barrier. |

## Why this shape
- **Trigger.** Volunteers offering is the trigger, which is a supply signal, not evidence that readers need Portuguese. Country share doesn't prove need either.
- **Cheap evidence check.** It takes about 20 minutes (your analytics, or an English-docs issue asking Brazilian users). It doesn't block merging the PRs. It decides how far past the first batch you go.
  1. Brazilian share of sessions.
  2. Browser-language `pt-BR` share divided by the Brazil-plus-Portugal country share. A ratio under about 0.5 weakly suggests many readers run another browser language (baseline).
  3. Quickstart completion for Brazilian readers versus others. Under 5 points of gap shows no barrier. Over 10 shows one (baseline). Rule out payment, latency and region causes first.
  4. Any Portuguese issues or chat messages.
- **Brainstormed bundles.** Your choice is still pending:

| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
| A | Source hardening only | none | you | ~0 | Wastes two volunteers who are already here. Keep its contents anyway. |
| **B (recommended)** | Critical-path pack, community-run | intro, install, quickstart, auth/config, top ~8 task pages, site UI strings | the two contributors, cross-reviewing | `ASSUMED` 6 h/release | Nothing. It fits the capacity of a solo maintainer. |
| C | Community program over all 220 pages | everything | the same two | unknown | You can't review it or measure its upkeep. An unowned long tail rots, as MDN's did. |
| D | Reviewed LLM set | traffic-ranked pages | contributors | pipeline upkeep | You can't spot-check Portuguese output. Fine as a tool inside B, not as a rung. |

- **Why B.** Pages beyond the first batch get added in rounds. You add a round once the pack's KPIs hold for two releases and the owners report spare hours.

## Source hardening (all markets)
- **Glossary.** The contributors propose it, you approve it, in `docs/glossary.md` or `i18n/pt-BR/glossary.md`. Record each "do not translate" decision with the name of who made it. Decide early how to handle producer, consumer, queue, topic, ack and broker. Keep Lanternfish and every identifier in English.
- **Style.** Plain English, one term per concept, no idioms in new pages. This helps every non-native reader and makes later translation cheaper.
- **Code.** Mark code non-translatable with `translate="no"` where the theme allows it.
- **Anchors.** Give source headings explicit IDs, like `## Install {#install}`. Translated headings keep the same ID: `## Instalação {#install}`. Links from issues and other locales then survive.

## Locale: pt-BR (gated)

### Evidence
| Signal | Value | Type |
|---|---|---|
| Country share of sessions | not provided | ASSUMED unknown |
| Browser-language ratio | not provided | ASSUMED unknown |
| Engagement gap | not provided | ASSUMED unknown |
| Demand in Portuguese | two unprompted PRs | measured |
| Commercial weight | not provided | ASSUMED unknown |

Class: barrier unconfirmed but owners named. That qualifies for `gated`, on the volunteer-supply route. Run the check above before widening scope.

### Page set
- **Pages.**
  - Intro and install (already submitted).
  - Quickstart, auth/config, and the top task pages by traffic.
  - Site UI strings: run `docusaurus write-translations --locale pt-BR` and translate navbar, footer and theme strings.
  - Check that your site search handles Portuguese before launch.
- **Never translated.**
  - Identifiers, CLI flags, config keys, wire-protocol terms and product names.
  - Generated reference, except top-traffic pages later.
  - Contributor docs and the docs changelog.
  - Screenshots and diagrams, which are deferred.
- **Error and log strings.** Quote them exactly as the product prints them, with the Portuguese explanation alongside.
- **Steady state.** About 3 changed pages per release × 0.5 h = 1.5 h, within the assumed 6 h per release (baseline pace).
- **Launch load.** (12 pages + ~1 page-equivalent for UI strings) × 1 h ÷ 6 h ≈ 2 to 3 releases (baseline pace, assumed hours). Replace both with the contributors' real pace after the first release.
- **Versions.** Translate only the latest docs version. Older versions fall back to English.

### Review model
- **Before publication.** Every pack page gets a second reader. The pack is small enough to review in full.
  - Security, auth, quotas, deprecations and delivery-guarantee semantics need a reviewer who has run the procedure.
- **Cross-review.** Neither contributor approves their own PR. GitHub enforces this for code owners.
- **LLM drafts.** Allowed, but declared in `translation_method` (`llm-reviewed`). Unreviewed LLM text doesn't ship.
- **Your mechanical checks.** You can't verify the prose. Do these three things instead, per PR.
  1. Code fences must match the source byte for byte, because translated pages never change code.
  2. The set of link targets must match the source.
  3. Heading count and fence count must match.

  The skill requires the last item. The first two are my extension, but they are what makes this safe without reading Portuguese: a translated install guide can't smuggle in a different command or URL. The drift script doesn't do these. A short CI script that diffs fenced blocks and extracts links is the thing to build.
- **Label (Portuguese, on every translated page).** "Translated from English with <human translation | AI assistance, reviewed by NAME>. The English page is authoritative. Read it in English → · Report a translation problem →". The contributors write the Portuguese wording. You check that the links resolve.
- **Search exposure.** Docusaurus emits hreflang once the locale is in the config. Add the locale to the production build only after the gate closes. Canonical and hreflang detail belongs to the `docs-seo` skill.
- **Language switching.** Use a `localeDropdown` in the navbar. No auto-redirect by browser language.

### Freshness contract
- **Pin fields.** Put these in each translated page's front matter:
  ```yaml
  source_path: docs/install.md
  source_commit: <hash>
  translated_on: 2026-10-30
  translation_method: community   # human | llm-reviewed | llm-unreviewed | community
  reviewed_by: <github-handle>
  ```
- **Pin rule.** The pin is the source file's last commit when translation started. Get it with `git log -1 --format=%h -- docs/intro.md` on the branch base. Don't use HEAD at merge time. Update the pin only when every source change up to it has been applied.
- **Existing PRs.** Ask the two contributors to add pins. Pages without a pin are treated as stale.
- **Drift check.** Copy `translation-drift-check.py` into `scripts/`. Run it in CI with `fetch-depth: 0`:
  ```
  python3 scripts/translation-drift-check.py \
    --source docs \
    --locale pt-BR=i18n/pt-BR/docusaurus-plugin-content-docs/current \
    --format csv --fail-on no-pin,unknown-pin
  ```
  - Set `--far` from your commits per release. The default is 5 (baseline).
  - It shows `untranslated` for the other ~200 pages. That is expected. They serve English.
  - Partials, snippets and generated sections count as changes. Pin and check them too.
  - Never use file modification dates for freshness.
  - Pins are only worth having if CI enforces them. An unenforced pin field decays, as it did at MDN.
- **Banner.** Pages whose source moved show a Portuguese outdated banner with the link to the English page in the first line.
- **Fallback.** Untranslated pages serve English.
- **Test stamps.** Translated procedures never copy `tested_with` or `last_verified`. They show the English page's stamps only while the pin is current.
- **Thresholds (baseline).**
  - A pack page that is `far` serves English until re-reviewed.
  - A page `far` for two releases or 180 days is retired with a redirect.

### Ownership gate
| Item | Status | Closing action | Expected date |
|---|---|---|---|
| 1. Two fluent reviewers, no self-approval | open | Confirm both volunteers. Add `CODEOWNERS` for `i18n/pt-BR/` with both. Require code-owner review. | before locale goes live |
| 2. Pack and UI strings translated and reviewed | open | Finish and cross-review the pack and run `write-translations` | ~2 to 3 releases (`ASSUMED`) |
| 3. Glossary with do-not-translate decisions | open | Contributors draft, you approve | before first merge of new pages |
| 4. Pin field everywhere and drift check running | open | Add pins to the two PRs and add the CI step | this week |
| 5. Written retirement threshold, named puller | open | Paste the thresholds into the contributing guide. The puller is you. | this week |
| 6. Published owner names and contact | open | Add a translation-problem link and owner names to the locale page | before go-live |

Person allowed to pull the locale: you.

**Merge now.** The files in the `i18n/` tree don't publish until `pt-BR` is in `i18n.locales`. Merging the two PRs as soon as pins are added and CI passes is therefore safe. Keep `pt-BR` out of the production config until the gate closes.

**Community program extras.**
- **Permissions.** Review rights are scoped to the locale directory.
- **Progress page.** A status page shows which pages are translated and which are `current`.
- **Silent maintainers.** If neither contributor responds for 90 days (baseline), freeze the locale read-only.
- **Licence.** Translations inherit the docs licence. Make sure the contributors accept the same contribution terms (DCO or CLA) the project already uses.

### KPIs and kill rule
| KPI | Pre-launch figure | Target | Control | Type |
|---|---|---|---|---|
| Adoption (share of pt-BR sessions staying on locale pages) | none yet | set after one release | same pages in English, same market | measured after launch |
| Outcome (quickstart completion, pt-BR readers) | measure now | set after one release | English readers, same pages | measured |
| Freshness (pack pages `current`) | n/a | ≥80% at each release | n/a | baseline |
| Quality (translation-problem reports per 1,000 views) | n/a | set after one release | n/a | measured after launch |

Kill rule: adoption or freshness below target for two consecutive quarters retires the locale, with redirects to the English pages (baseline). Replace it with your own release cadence. Retirement is one-way: revive a locale only through the full launch gate.

## Rollout schedule
| Release or week | Milestone | Owner |
|---|---|---|
| This week | Reply to the contributors. Add `CODEOWNERS` and the CI check. Pins added to both PRs. Merge both with the locale off. | you, contributors |
| This week | Run the 20-minute evidence check | you |
| Release N+1 | Glossary approved. Quickstart, auth and top task pages translated and cross-reviewed. | contributors |
| Release N+2 to N+3 | UI strings done. Gate closes. Add `pt-BR` to the production config, with the switcher, banner and label. | contributors, you |
| After 2 releases of held KPIs | Decide on the next round of pages | you |

## Reply to the contributors today
Thanks, I'd like to say yes. Please add a pin to each PR (the last commit of the English source file when you started), and I'll merge once CI passes. For a first batch I'd like intro, install, quickstart, auth and config, and the most-read task pages, plus the site UI strings. Two conditions: you review each other's PRs (neither approves their own), and you draft a short glossary of terms to leave in English. After two releases we'll look at how readers use it and pick the next round together.

## Questions that would change this plan
1. What are the Brazilian share, browser-language ratio and quickstart completion? A "no barrier" result shrinks the plan to source hardening.
2. How many hours per month can the two contributors commit? This sets the page set.
3. Do you have docs versions beyond the current one?
4. How many docs commits land per release? This sets `--far` and the steady-state number.
5. Is the CLI or any UI localized? If not, the quickstart ends in English output, so the plan keeps error strings verbatim.