# Docs localization plan - Saltmarsh, Arabic (`ar`), 2026-10-30

## Bottom line

- **Decision: `gated`.** Don't launch yet.
  - No one has shown that English is the barrier. Evidence so far is one reseller's claim.
  - There is one Arabic reviewer (Omar), and the launch gate needs two.
- **Scope: a critical-path pack, not 180 pages.**
  - About 12 pages plus the docs-site UI strings, drafted by LLM and reviewed by humans.
  - Estimated launch load is about 4 releases at Omar's assumed hours.
  - Everything else falls back to English.
- **The English-only console and CLI is permanent, so the docs work around it.**
  - Console labels, CLI output and error strings stay verbatim in English.
  - Every translated step carries an Arabic gloss next to the English label.
- **Do now, for free:** pull the evidence in the table below, ask the reseller four questions, and ask for a second Arabic reviewer.

## Stored context

| Field | Value |
|---|---|
| Locale and decision | `ar` (Modern Standard Arabic, one locale for all Gulf markets), `gated` |
| Owner / reviewers | Omar (Saltmarsh SE) plus a second reviewer, not yet named |
| Page set rule | Critical-path pack: top first-success pages by traffic, plus site UI strings. Docusaurus current version only. |
| Pin fields | `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by` (names identical across locales) |
| Drift check | `python3 scripts/translation-drift-check.py --source docs --locale ar=i18n/ar/docusaurus-plugin-content-docs/current --format csv --far 5 --fail-on no-pin,unknown-pin` |
| Kill rule | Adoption or freshness below target for 2 consecutive quarters retires the locale (baseline). |
| Pull authority | Not named yet. Needs one person with authority to pull the locale. |

## Assumptions

All of these are `ASSUMED` until someone confirms them.

1. Omar can give about 4 reviewer hours per release.
2. Saltmarsh ships a release roughly every 2 weeks, so 4 releases is about 8 weeks.
3. The critical-path pack is 12 pages. Replace this with the real top-10 first-success pages from traffic, plus 2 concept pages.
4. The docs site UI is about 300 strings (navbar, footer, sidebar category labels, banners, feedback widget). That is about 1 page-equivalent.
5. About 3 pages in the set change per release.
6. Docusaurus has only a `current` docs version, or older versions are low-traffic.
7. No contract, tender or regulation names Arabic.
8. Western digits (0-9), not Arabic-Indic digits. Omar decides.
9. There is no analytics segmentation by browser language yet.

## Questions to confirm, highest impact first

1. **Reseller:** What exactly in the three deals needs Arabic?
   - Who reads the docs: operators who will run the CLI, or security and procurement reviewers?
   - If it's reviewers, the first pages may be security, encryption and compliance pages rather than the quickstart.
2. **Reseller:** Is Arabic docs a stated condition in the deals, or one of several asks? Do data residency, Gulf region availability, payment or latency also appear?
   - For cloud backup these may block the deals regardless of docs language. Check them before spending reviewer hours.
3. **Reseller:** When do the three deals close?
   - About 8 weeks of build, plus the time to close the reviewer gap, may land after the deals.
4. **Saltmarsh:** Who may pull the locale?
5. **Saltmarsh:** Which search does the docs site use (Algolia DocSearch or a local plugin), and how many docs versions are live?

## Decision summary

| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| `ar` | `gated` | Commercial weight is real but second-hand (reseller, 3 deals). No measured language barrier. One reviewer, gate needs two. | Evidence below read as a barrier, and a second named Arabic reviewer, and all Step 6 items closed |
| All other locales | Out of scope | No request or data | Same Step 1 test per language |

If the evidence shows no barrier (Arabic-browser readers complete the quickstart like English readers) and the deals turn on residency or pricing, the decision becomes `declined`. Source hardening still ships. Reopen if Arabic tickets appear or the engagement gap exceeds 10 points.

## Source hardening (all markets, start now)

- **Glossary owner and location:** Omar owns `docs/glossary/ar.md` (or `i18n/ar/glossary.md`). Saltmarsh's docs lead owns the English term list. Each "do not translate" row records the decision and who made it.
- **Style rules:**
  - Plain global English.
  - One term per concept (backup, snapshot, restore point and recovery point cannot all mean the same thing).
  - No idioms.
- **Explicit heading IDs** on the pack pages in English, so Arabic pages reuse the same anchors.
- **Code non-translatable:**
  - Add `translate="no"` to `<code>` and `<pre>` through the Docusaurus MDX component override.
  - This also stops browser machine translation from mangling commands for every reader.

## Locale: `ar` (gated)

### Evidence

None of this is measured yet. Fill it in before the plan is final.

| Signal | Value | Type |
|---|---|---|
| Country share of sessions (SA, AE, KW, QA, BH, OM) | Not measured. Pull from analytics. | measured (pending) |
| Browser-language share (`ar*`), divided by combined share of Gulf-country sessions | Not measured. Under about 0.5 suggests many readers run another browser language (baseline, weak alone). | measured (pending) |
| Engagement gap: quickstart completion or time to first API call, `ar` browser vs `en` browser | Not measured. Under 5 points = no barrier, over 10 = barrier (baseline). Rule out region availability, payment, latency and phone verification first. | measured (pending) |
| Demand in Arabic (tickets, community posts, site-search queries) | Not measured. Ask support for a count. | measured (pending) |
| Commercial weight | 3 deals, per the Riyadh reseller | reported by the reseller, not verified |
| Substitutes | Browser translation and AI assistants answer in Arabic today | assumed |

**Class: undetermined, leaning `barrier confirmed, owner partial`.**
- The default answer is "not yet" until signals 1-3 say otherwise.
- The reseller request is evidence of commercial weight. It is not evidence that readers can't use English docs.
- The data pull takes a day or two. Do it before anything is translated.

### Candidate bundles

| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
| A (recommended) | Critical-path pack: LLM draft, human post-edit, every page reviewed before publishing | About 12 pages plus UI strings | Omar plus second reviewer | About 1.5 h per release steady state | Chosen |
| B | Reviewed LLM set over a larger traffic-ranked set (about 40 pages) | 40 pages | Same | About 5 h per release steady state (assumed 3 changed pages per release scaled up) | Above Omar's 4 h ceiling, and the pack's KPIs aren't known yet |
| C | Continuous labelled MT of all 180 pages | 180 pages | Nobody | Low reviewer hours, high risk | Unreviewed errors on backup, restore, retention and encryption pages. Wrong restore steps do real harm. |
| D | Full human sync | 180 pages | Vendor | Highest | No contract names Arabic |
| E | Community program | - | - | - | Not open source, no volunteers, and the deal date is inside a quarter |

**Chosen: A.** Bundle B is the next rung up. Move there once the pack's KPIs hold for two release cycles and the owners have spare hours.

**Deleted rungs:** community program, full human sync and continuous labelled MT (reasons above). A one-shot machine-translated dump is not on the ladder.

### Page set

- **First:**
  - Quickstart, install, authentication.
  - The top task pages: first backup, schedule, restore, retention, encryption-key management, storage targets.
  - Every docs-site UI string, including Docusaurus sidebar labels (`current.json`), `code.json`, and navbar and footer files.
  - Confirm Docusaurus's bundled Arabic theme strings, then review them.
- **Second:** concept pages the quickstart links to (for example snapshots and retention, encryption model).
- **Top-traffic only, or not at all:** generated CLI and API reference.
- **Never translated:**
  - Identifiers, CLI flags, config keys, HTTP headers, product names.
  - The docs changelog and contributor docs.
  - Screenshots and diagrams (deferred).
- **Steady state:** about 3 changed pages per release × 0.5 h ≤ 4 h per release. `ASSUMED`, baseline pace.
- **Launch load:** (12 pages + 1 UI page-equivalent) × 1 h ÷ 4 h per release = 3.25, so about **4 releases**. Baseline pace, `ASSUMED` hours.
  - The clock starts only when the gate items below close.
  - A second reviewer contributing hours shortens it.
- **Glossary file:** `docs/glossary/ar.md`.

### Product-gap handling (English-only console and CLI)

This is the "localized docs, English product" failure mode. It can't be fixed, so it has to be designed around.

- **Quote UI labels and CLI errors exactly as the product prints them.** The reader searches the string they see.
  - Put the Arabic explanation beside it, not in place of it.
  - Example: press **Restore** (استعادة) in the console.
- **Keep commands and flags untouched.** Translate only the prose around them.
- **Add a label-gloss table** at the top of each task page: English label → Arabic meaning. Omar owns it.
- **Give each error-string page** the English message in a code block, then an Arabic explanation and fix.
- **Layout (right-to-left) rules:**
  - Set `direction: 'rtl'` for `ar` in the Docusaurus `localeConfigs`.
  - Force code blocks, inline code, CLI output and tables of commands to `direction: ltr`.
  - Test mixed Arabic and English lines, admonitions, breadcrumbs, the sidebar and the language switcher.
- **Untranslated pages inside the Arabic site:**
  - Docusaurus falls back to English content for missing files, so they would render in right-to-left chrome.
  - Verify on your Docusaurus version.
  - If confirmed, redirect untranslated pages to the English URL or wrap the fallback in `dir="ltr"`. Don't leave them in `ar` chrome.
- **Search:** check that site search tokenizes Arabic. If it's a local plugin, check Arabic language support.

### Review model

- **Human review before publication:** every page. The pack is small enough that tiering isn't needed.
- **Review on page-view threshold:** not used. The set is reviewed in full.
- **Working split:** Omar post-edits the LLM draft, and the second reviewer approves the PR. Swap on alternate pages, so nobody approves their own change. Both are named in `reviewed_by`.
- **Mask code** before the LLM pass. After each page, check that code-fence, link and heading counts match the source.
- **Label text** (shown in Arabic, draft for Omar to correct): "Translated from English with AI assistance, reviewed by <name>. The English page is authoritative. Read it in English → · Report a translation problem →"
- **Search exposure:** keep `ar` out of search until the first review pass is complete. Hreflang and canonical mechanics go to `samber/developer-relations-skills@docs-seo`.
- **Language offer:** a dismissible suggestion banner plus a persistent switcher that remembers the choice. No auto-redirect by browser language.

### Freshness contract

- **Pin fields in each page's front matter:**
  ```yaml
  source_path: docs/guides/first-backup.md
  source_commit: <hash of the source file's last commit when translation started>
  translated_on: 2026-11-XX
  translation_method: llm-reviewed   # human | llm-reviewed | llm-unreviewed | community
  reviewed_by: omar-<surname>, <second-reviewer>
  ```
- **Pin rule:** pin the source commit at the start of translation, not at the end. Bump it only when every source change up to that commit has been applied.
- **Drift check in CI** (not yet run, no pages exist):
  ```
  python3 scripts/translation-drift-check.py --source docs --locale ar=i18n/ar/docusaurus-plugin-content-docs/current --format csv --far 5 --fail-on no-pin,unknown-pin
  ```
  - Needs full git history (`fetch-depth: 0`).
  - Set `--far` from Saltmarsh's commits per release. Use `5` until measured (baseline).
  - Fail on `no-pin` and `unknown-pin` from day one, because this is a new locale.
- **Includes:** pin and check shared partials and snippets too.
- **Thresholds** (baselines, replace with Saltmarsh's cadence):
  - Banner on any page whose source moved since the pin.
  - Critical-path page `far`: fall back to English until re-reviewed.
  - Any page `far` for 2 releases or 180 days: retire it with a redirect to English.
  - Last reviewer leaves with no replacement within a quarter: freeze read-only, then retire.
- **Tested-version stamps:** Arabic procedures never copy `tested_with` or `last_verified`.
  - They show the English page's stamps while the pin is `current`.
  - After that, the outdated banner replaces the stamps.
- **Banner draft** (Omar to correct): "تمت ترجمة هذه الصفحة من نسخة أقدم من الصفحة الإنجليزية، وقد تغيّرت الصفحة الإنجليزية منذ ذلك الحين. اقرأ النسخة الإنجليزية الحالية ←"

### Ownership gate

| Item | Status | Closing action | Expected date |
|---|---|---|---|
| 1. Two named fluent reviewers | Open: Omar only | Ask the reseller for a named Arabic-speaking reviewer, or hire a contractor or vendor with an independent QA reviewer (meets the item, baseline). A reseller reviewer is a conflict risk, so note it in the plan. | `ASSUMED` within 2 weeks |
| 2. Pack and all UI strings translated and reviewed | Open | About 4 releases of work (see launch load) | About 8 weeks after items 1, 3, 4 close |
| 3. Glossary with "do not translate" decisions | Open | Omar drafts. Proposed starting terms for Omar to confirm: backup = نسخ احتياطي, restore = استعادة, retention = احتفاظ, encryption = تشفير. Decide transliteration vs Arabic for "snapshot", "vault", "bucket". | Release 1 |
| 4. Pin field on every page, drift check running | Open | Add the CI step before the first page is translated | Release 1 |
| 5. Written retirement threshold and a named person who may pull the locale | Threshold written above; person open | Saltmarsh names one person | This week |
| 6. Published owner names and a contact for translation problems | Open | Localized contact line on each page and in the locale README | Before launch |
| Right-to-left layout and search check | Open | Build the Docusaurus `ar` locale, test chrome, code blocks, search | Release 1-2 |

Person allowed to pull the locale: **not named. Ask.**

A locale missing any item stays `gated`. It never launches conditionally. A private, unindexed preview for the reseller and the second reviewer is not a launch.

### KPIs and kill rule

Control: the same pages read by Gulf-country sessions on `en`, and Arabic-browser sessions on `en` pages before launch.

| KPI | Pre-launch figure | Target | Control | Type |
|---|---|---|---|---|
| Adoption: share of `ar`-browser sessions staying on `ar` pages vs switching to English | Not measured | Set after the first release | `ar`-browser readers on `en` pages | measured (pending) |
| Outcome: quickstart completion or time to first API call, `ar` readers | Not measured | Set after the first release; close the gap to English readers | Same pages in English | measured (pending) |
| Freshness: share of pack pages `current` by pin | n/a | At least 80% at every release | - | baseline |
| Quality: translation-problem reports per 1,000 views | n/a | Set after the first release | - | measured |
| Commercial: the 3 Riyadh deals | 3 open, per the reseller | No target. Record whether each prospect cites the Arabic docs. | - | reported by the reseller, unverified |

**Kill rule:** adoption or freshness below target for two consecutive quarters retires `ar`. Every URL redirects to English and the locale leaves the switcher (baseline). Retirement is one-way.

Don't promise the reseller that Arabic docs closes the deals. Report adoption and outcome numbers instead.

## Rollout schedule

Release numbers assume a 2-week cadence (`ASSUMED`).

| Release or week | Milestone | Owner |
|---|---|---|
| This week | Pull the evidence table. Send the reseller the four questions. Ask for a second reviewer. Name the person who may pull the locale. | Saltmarsh docs lead |
| This week | Add browser-language segmentation to analytics | Saltmarsh docs lead |
| Release 1 | Review-decision checkpoint: evidence says `launch`, stay `gated`, or `declined`. Glossary draft. CI drift step. Source-hardening edits (explicit heading IDs, `translate="no"`). | Docs lead, Omar |
| Release 1-2 | Docusaurus `ar` locale scaffold (RTL, fallback behaviour, search check). UI strings translated. | Docs lead, Omar |
| Release 2-4 | Pack pages: LLM draft, Omar post-edit, second reviewer approves. Private preview for the reseller. | Omar, second reviewer |
| Release 4 or later | Gate closed: publish, expose to search, add switcher and suggestion banner | Docs lead |
| Release 6 | First KPI read (one release after launch). Set targets. | Docs lead |
| Two quarters after launch | Kill-rule review | Person who may pull the locale |

## Next action

Pull the evidence (sessions by country and browser language, quickstart completion by browser language, Arabic tickets). Send the four reseller questions in the same message that asks for a second Arabic reviewer.

I didn't run the drift-check script. There are no Arabic pages yet, so it ships as a CI step in this plan.