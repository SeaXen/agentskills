# Freshness contract

Read when writing the pin fields, the banner, the drift check or the retirement rules for a locale.

## Pin fields

Put these in each translated page's front matter. Name them once in the plan and keep the names identical across locales.

```yaml
# the page this translates
source_path: docs/en/guides/webhooks.md
# commit hash of the source revision the translation was made from - never a branch or tag
source_commit: 3f9c2e1
translated_on: 2026-10-02
# human | llm-reviewed | llm-unreviewed | community
translation_method: human
# empty when unreviewed
reviewed_by: kenji-t
```

- Pin the source file's last commit at the moment translation starts, never HEAD when it finishes. Source changes made while the translator worked then show as `behind` instead of hiding.
- Update `source_commit` only when the translator has applied every source change up to that commit. Bumping it without the content change hides drift.
- `translation_method` drives the page label and the review tier.
- Formats without front matter carry the pin in a comment: `<!-- source_commit: 3f9c2e1 -->`.

## Tested-version stamps on translated procedures

A how-to or quickstart in the source language may carry stamps such as `tested_with` and `last_verified`. A translation never copies them.

```yaml
# ✗ Bad - the translation claims a test run nobody did in this language
tested_with: "acme-cli 4.2, Ubuntu 24.04"
last_verified: 2026-09-30

# ✓ Good - the translation points at the tested source revision
source_commit: 3f9c2e1
# rendered: "Tested version: see source page (acme-cli 4.2, verified 2026-09-30)" while the pin is current
```

- While the drift check reports the page `current`, render the source page's stamps with "verified on the source page".
- Once the source moves, replace the stamps with the outdated banner. The steps may no longer match what was tested.
- Carry own stamps (`locale_tested_with`, `locale_last_verified`) only when someone re-ran the procedure in the localized environment - localized OS, console language, regional endpoints.

## Drift check

Run `scripts/translation-drift-check.py` from inside the docs repository:

```
python3 scripts/translation-drift-check.py --source docs/en --locale ja=docs/ja --locale pt-BR=docs/pt-br --format summary
```

| Status | Meaning | Action |
| --- | --- | --- |
| `current` | No source commit since the pin | Show the page, render source stamps |
| `behind` | 1 to `--far` source commits since the pin | Show with outdated banner; queue for review |
| `far` | More than `--far` commits (default 5, baseline) | Critical-path page: fall back to source; other pages: banner + priority queue |
| `no-pin` | Translated page without a pin | Treat as stale; add the pin after review |
| `unknown-pin` | Pin is not a commit hash, matches a branch or tag name, is missing from history, or is not an ancestor of HEAD | Fix the pin; the `detail` column says which |
| `untranslated` | Source page with no translation | Serve the source page |
| `moved` | Source page renamed since the pin | Move the translation to the new path, keep the pin; a pure rename is not counted as a change |
| `orphan` | Translation whose source page is gone | Redirect to the source page's replacement, then remove; list locale-only pages as intentional |

- Each locale directory must mirror the source tree's relative paths. Generators that store translations under their own tree need the matching path, e.g. for Docusaurus: `--source docs --locale ja=i18n/ja/docusaurus-plugin-content-docs/current`.
- Translations kept in a separate repository per locale fall outside the script; pin the same way and diff against the source repository's history.
- `far` is more than 5 commits by default; pass `--far` scaled to commits per release, or a busy quickstart goes `far` inside one release.
- Pass every locale directory nested inside the source directory, or the unlisted ones are scanned as source pages.
- The pin is read from a front-matter block starting on line 1 - flat keys (`source_commit` and common spellings) or MDN's nested `l10n.sourceCommit` - or from a comment in the first 20 lines.
- CI needs full history (`fetch-depth: 0` on hosted checkouts); the script refuses a shallow clone rather than report every page `unknown-pin`.
- `--fail-on no-pin,unknown-pin` exits 1 when any page has those statuses; exit 2 means a usage or git error.
- Suffix layouts (`page.ja.md`) are out of scope.
- Never compare file modification dates. Any edit to a translation, including adding a "stale" marker, makes it look newer than its source.
- Commit count is a triage proxy, not a measure of meaning. A typo fix counts like a rewrite; let the reviewer clear trivial changes by bumping the pin.
- Fail new locales on `no-pin` and `unknown-pin` from day one. For an existing locale, pass `--since <ref>` so only translations added or edited after that ref can fail while the backlog gets pinned; drop `--since` once it is. An unenforced pin field decays the way it did at MDN.

## Banner wording

```
✓ Good - says what is stale, links the authoritative page
This page was translated from an earlier version of the English page. The English page has changed since. Read the current English version →

✗ Bad - vague, no link, reader cannot act
This translation may be out of date.
```

Show the banner in the locale's language. Put the link to the source page in the first line.

The translation label sits on every translated page, current or not:

```
Translated from English with <human translation | AI assistance, reviewed by <name> | AI assistance, not yet reviewed>. The English page is authoritative. Read it in English → · Report a translation problem →
```

## Retirement thresholds (baselines - replace with the user's cadence)

| Level | Trigger | Action |
| --- | --- | --- |
| Page | `far` on a critical-path page | Serve the source page until re-reviewed |
| Page | `far` for two releases or 180 days, whichever comes first, without owner renewal | Retire: redirect to the source page |
| Locale | Freshness or adoption below target for two quarters | Retire the locale: redirect every URL to the source page, remove from the language switcher |
| Locale | Last named reviewer leaves, no replacement within one quarter | Freeze read-only with banner, then retire |

Treat retirement as one-way: revive a locale only through the full launch gate, never by unfreezing old pages.
