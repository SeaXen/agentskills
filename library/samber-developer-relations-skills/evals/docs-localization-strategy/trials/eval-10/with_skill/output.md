# Docs localization plan: Kestrelworks IoT platform (German), 2026-10-30

I read the skill and its three references. I did not run the drift script, because nothing is translated yet.

## Verdict

**Don't build the nightly 2,000-page German pipeline now.** Your customer's hunch is plausible but unproven, and Jonas's 4 hours a week can't support that set. Do three things in order:

1. **This week:** source hardening, plus a 2-week measurement of whether English is a barrier for German readers.
2. **If the data shows a barrier:** a human-reviewed German critical-path pack of about 12 pages and the site UI strings, with LLM drafts. Launch is gated on a second fluent reviewer.
3. **Only after the pack has held for two release cycles:** consider labelled, unreviewed machine translation for low-risk pages.

## Assumptions (none confirmed by you)

- `ASSUMED`: Jonas has 4 h/week. This is "half a day a week" read as 4 hours. All hours below use that.
- `ASSUMED`: no German data has been pulled yet (browser language, quickstart completion, tickets).
- `ASSUMED`: the product is English-only (console, CLI, errors, support). If it is, a German quickstart ends in English UI.
- `ASSUMED`: Hugo with one content tree per language (`content/en`, `content/de`), with front matter on pages.
- `ASSUMED`: Kestrelworks has no contract or regulation that names German.
- `ASSUMED`: one live docs version.

## Decision summary

| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| de | `source hardening only`, moving to `gated` if Step 1 confirms a barrier | One customer anecdote is not evidence. Only one reviewer exists, and the launch gate needs two. | German sessions show a barrier (see Evidence), **and** a second fluent reviewer is named. |
| all others | `declined` | No candidate evidence was given. | A trigger and data per language. |

## Why not "like MDN did"

- **MDN's own readers lean English.** MDN's 2024 survey of German-browser readers found 62% preferred English and 35% German (`sourced`). That is probably an upper bound on English preference, since the survey ran on English pages. Your customer's remark matches the data. MDN still launched, because the 35% is a large minority. Preference evidence decides scope and labelling, not just yes or no.
- **MDN's launch was a labelled experiment.** It had masked code, an "experiment, may contain inaccuracies" notice, a remembered opt-out, feedback buttons, and about a month out of search before indexing (`sourced`). It was a daily pipeline over 12,500+ pages. The reference does not describe per-page human review.
- **MDN's German history is a warning.** MDN removed German in 2022 as outdated and unmaintained (`sourced`). It came back only because a pipeline replaced the missing maintainers.
- **Your stakes are higher.** An IoT platform has device provisioning, auth, OTA updates, quotas and billing. LLM errors on those pages cause harm. In a published evaluation of 50 LLM-translated READMEs, structural, code or URL damage hit 16–50% of files depending on the model, while semantic scores stayed at 94–96% (`sourced`).

## The capacity math

| Check | Calculation | Result |
|---|---|---|
| Review all 2,000 pages once | 2,000 pages × 1 h ÷ 4 h/week = 500 weeks | About 9.6 years (`baseline` pace) |
| Review a nightly-changed set | Say 20 changed pages/week × 0.25–0.5 h = 5–10 h/week | Above 4 h/week (`ASSUMED` churn, `baseline` pace) |
| Critical-path pack: steady state | About 1 changed page/week × 0.5 h = 0.5 h/week | Fits in 4 h/week (`ASSUMED` churn, `baseline` pace) |
| Critical-path pack: launch load | (12 pages + about 2 UI page-equivalents) × 1 h ÷ 4 h/week = 3.5 | About 4 weeks (`baseline` pace) |

So the nightly pipeline over the whole site is a "continuous labelled MT" rung with effectively zero review. The pack leaves about 3.5 h/week of headroom for extending coverage.

**Nightly re-translation also destroys review.** If the pipeline regenerates a page Jonas already approved, his work is overwritten. The pipeline must only act on pages whose source changed since the pin. For reviewed pages, it must produce a draft for Jonas and never publish it directly.

## Step 1: test whether English is the barrier (2 weeks)

Pull these for German readers:

| Signal | How to measure | Reading (`baseline` thresholds) |
|---|---|---|
| Browser language vs country | `de*` browser share ÷ combined share of DE+AT sessions (add German-speaking CH only if you can segment it) | Under about 0.5 suggests many run another browser language. This is weak evidence alone. |
| Engagement gap | Quickstart completion and time to first API call, de-browser vs en-browser, same pages | Under 5 points: no barrier. Over 10 points: barrier. Rule out signup, payment, region and latency causes first. |
| Language of demand | Support tickets, forum posts and search queries written in German | Any steady volume counts. |
| Substitutes | Browser translation, AI assistants, search-engine snippet translation | Reduces need. |
| Commercial weight | German revenue, pipeline, named deals | Raises the priority. |

Also ask your German customer what specifically hurt, and which pages. That gives you a page list.

**Classify the result:**

- **Barrier confirmed:** go to the pack.
- **No barrier:** `declined`, and reopen when the engagement gap or German tickets appear.
- **Demand but no second reviewer:** `source hardening only`.

## Candidate bundles (for the German locale if Step 1 passes)

| Bundle | Rung | Page set | Owner | Standing hours | Verdict |
|---|---|---|---|---|---|
| A. Your plan | Continuous labelled MT | 2,000 pages, nightly | Jonas, unreviewed | 4 h/week, spread over nothing | **Eliminated.** Unreviewed errors on provisioning, auth and billing pages at scale. |
| B. Critical-path pack | LLM draft, Jonas reviews every page | About 12 pages plus UI strings | Jonas plus a second reviewer | 0.5–4 h/week | **Recommended.** It fits capacity and can be shown to be current. |
| C. Reviewed LLM set | LLM draft, tiered review | About 100 traffic-ranked pages | Jonas plus a second reviewer | Over 4 h/week, probably | **Deferred.** Revisit after B holds for two release cycles with spare hours. |

I'd go with **B** (`ASSUMED` that you agree; tell me if you want another bundle). Source hardening applies to all bundles.

## Source hardening (start now)

- **Glossary:** one file in the repo, `data/glossary.yaml` or similar. Owner: you, with Jonas's German column. It lists every IoT term (device, gateway, shadow, provisioning), the German form or "do not translate", who decided, and when.
- **Style rules:** plain global English, one term per concept, no idioms, no phrasal verbs where a plain verb exists.
- **Code marked non-translatable:** `translate="no"` on code blocks, inline code and product names, so browser translation stops mangling them.
- **Heading anchors:** explicit IDs on headings, since Hugo derives IDs from heading text. Anchors then survive translation and links from support replies keep working.
- This also helps every non-native reader, not only German ones.

## Page set for the German pack

- **First:**
  - quickstart
  - installation
  - authentication and device provisioning
  - the top task pages by traffic among German readers (about 9)
  - all site UI strings (navigation, banners, feedback)
  - Check that Hugo's search handles German compounds, and that the language switcher works.
- **Second:** concept pages the quickstart links to.
- **Only if top-traffic, otherwise never:** generated API reference.
- **Never translate:** identifiers, CLI flags, MQTT topics, HTTP headers, config keys, product names, contributor docs, and the docs changelog.
- **Quote verbatim, translate alongside:** error messages and console labels exactly as the product prints them.
- **Keep code runnable:** don't change code. Translate comments only if the sample policy allows and the sample still runs.
- **Defer:** screenshots and diagrams.
- **Hugo layout:** `content/en` and `content/de` with mirrored relative paths, so the drift script works. Hugo's filename-suffix layout (`page.de.md`) is out of the script's scope.

## Review model

- **Human review before publication:** every page in the pack. It is small enough.
- **Mask code before the LLM sees it.** Check per page that code-fence count, link count and heading count match the source.
- **Label text** (in German, on every translated page): "Translated from English with AI assistance, reviewed by Jonas. The English page is authoritative. Read it in English → · Report a translation problem →"
- **Language offer:** a dismissible suggestion plus a persistent switcher that remembers the choice. **Never auto-redirect** by browser language.
- **Search exposure:** index `de` pages only after their first review pass. URL, canonical and hreflang mechanics belong to the `docs-seo` skill.

## Freshness contract

Pin fields on every translated page (identical names across locales):

```yaml
source_path: content/en/guides/provisioning.md
source_commit: 3f9c2e1   # commit hash when translation started, never a branch or tag
translated_on: 2026-11-20
translation_method: llm-reviewed   # human | llm-reviewed | llm-unreviewed | community
reviewed_by: jonas
```

- **Pipeline rule:** set `source_commit` to the source file's last commit at the moment translation starts, not HEAD at the end. Bump it only when every source change up to it is applied.
- **Drift check in CI** (full git history, `fetch-depth: 0`):
  `python3 scripts/translation-drift-check.py --source content/en --locale de=content/de --format csv --fail-on no-pin,unknown-pin`
- **`--far`:** set it from your commits per release (default 5, `baseline`). A busy quickstart goes `far` inside one release at the default.
- **Banner:** on any page whose source moved. First line links the English page: "This page was translated from an earlier version of the English page. The English page has changed since. Read the current English version →" (shown in German).
- **Fallback:** to the English page for untranslated pages, and for `far` critical-path pages.
- **Tested-version stamps:** the translated procedure shows the source page's stamps only while its pin is `current`. It never copies `tested_with` or `last_verified`.
- **Retirement (`baseline`):** a page `far` for two releases or 180 days is redirected to English. The locale is retired after two quarters below target.
- **Includes count as changes.** Pin and check shared partials and snippets too.

## Ownership gate (launch refused until all hold)

| Item | Status | Closing action | Expected date |
|---|---|---|---|
| 1. Two named fluent reviewers | **Open**: only Jonas | Name a second (contractor, German-speaking support or sales engineer, or a vendor with an independent QA reviewer) | You set it |
| 2. Pack and UI strings translated and reviewed | Open | About 4 weeks of Jonas's time once item 1 closes | Item 1 + 4 weeks |
| 3. Glossary with "do not translate" decisions | Open | Start now | Week 1–2 |
| 4. Pin field on every page, drift check in CI | Open | Add the CI step before the first page is translated | Before translation |
| 5. Written retirement threshold, and a named person allowed to pull the locale | Open | You decide the person; thresholds as above | Week 2 |
| 6. Published owner names and a contact for problems | Open | Footer plus the "Report a translation problem" link | Before launch |

The 4-week launch-load clock starts only when item 1 closes.

## KPIs and kill rule

Control: the same pages read in English by the same German market.

| KPI | Pre-launch figure | Target | Type |
|---|---|---|---|
| Adoption: German sessions staying on `de` pages vs switching to English | From the 2-week measurement | Set after the first release | measured, then target |
| Outcome: quickstart completion, de readers, before vs after | From the 2-week measurement | Improvement over the gap | measured |
| Freshness: critical-path pages `current` by pin | n/a | At least 80% at every release | `baseline` |
| Quality: translation-problem reports per 1,000 views | n/a | Set after the first release | measured |

**Kill rule:** adoption or freshness below target for two consecutive quarters retires the locale, with redirects to English (`baseline`).

## Rollout schedule

| When | Milestone | Owner |
|---|---|---|
| Week 1 | Glossary file, style rules, `translate="no"`, explicit heading IDs | You, with Jonas on the German column |
| Weeks 1–2 | Pull the German signals above; ask the customer which pages hurt | You |
| Week 2 | Decide `declined`, `source hardening only` or `gated`. Name the second reviewer and the person who can pull the locale. | You |
| Before any translation | Add the drift-check CI step | Docs engineer |
| Gate closed + weeks 1–4 | Translate and review the pack and UI strings | Jonas + second reviewer |
| After launch, two release cycles | Check KPIs. If 80% current and spare hours exist, consider bundle C. | You, Jonas |

## Questions still open

1. What do the German browser-language and quickstart-completion numbers say?
2. Is the console, CLI and error output English-only? If so, a German quickstart ends in English.
3. What is your release cadence and how many docs pages change per week? These replace my `ASSUMED` churn.
4. Who can be the second German reviewer?

## Stored context

- Locale: de, decision pending Step 1.
- Owners: Jonas (4 h/week), second reviewer TBD.
- Page set: about 12 critical-path pages plus UI strings.
- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift command: as above.
- Kill rule: two quarters below target.