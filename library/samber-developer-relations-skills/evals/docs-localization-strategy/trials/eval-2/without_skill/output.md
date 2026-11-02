**Say yes, with conditions.** Do these in order. Total about 3 hours for you, then about 20 minutes per PR after that.

I did not open the Lanternfish repo. I'm assuming Docusaurus 3. Check three things before step 1:
- Whether you use versioned docs.
- Which search provider you use.
- Where you host.

## 1. Reply to the contributors (10 min)

Say yes. Ask for three things:
- Each person reviews the other's PRs. You can't read Portuguese, so they are your reviewers.
- Work in small PRs, one doc section at a time.
- Follow a `TRANSLATING.md` that you write in step 4.

Move the two open PRs under the `i18n/` paths from step 2 before you merge them.

## 2. Docusaurus i18n config (30 min)

Use the locale code `pt-BR`, not `pt`. The docs are for Brazil, and `pt-BR` leaves room for `pt-PT` later.

```js
// docusaurus.config.js
i18n: {
  defaultLocale: 'en',
  locales: ['en', 'pt-BR'],
  localeConfigs: { 'pt-BR': { label: 'Português (Brasil)', htmlLang: 'pt-BR' } },
},
```

Files go here:
- Docs: `i18n/pt-BR/docusaurus-plugin-content-docs/current/<same path as docs/>`
- Sidebar labels and navbar/footer strings: JSON files in `i18n/pt-BR/`. Generate them with `npm run write-translations -- --locale pt-BR`.

Preview with `npm run start -- --locale pt-BR`. Build with `npm run build`, which builds every locale. Build time goes up, so check your CI limits.

**Do not add the `localeDropdown` navbar item yet.** Soft launch first (step 5).

Three traps:
- **Untranslated pages fall back to English.** Under `/pt-BR/`, the other ~215 pages would show English. That looks broken, and search engines will see it as duplicate content.
  - Fix: set `noIndex` for the locale until launch. Check that your Docusaurus version supports it in `localeConfigs`.
  - Fix: add a banner (step 5).
- **Translated headings change anchor IDs.** Cross-links break.
  - Fix: require explicit English IDs, like `## Instalação {#installation}`.
  - Keep `id` and `slug` frontmatter identical to the English source.
- **Versioned docs:** if you have them, translate `current` only. Skip old versions.

## 3. CI gates, so you can merge without reading Portuguese (1 hour)

**Gate A: build.** Set `onBrokenLinks: 'throw'` and run the build with the pt-BR locale. This catches broken MDX and broken links.

**Gate B: structure parity.** Add a script that compares each translated file to its English source. It fails on:
- A different number of fenced code blocks.
- A different set of absolute URLs.
- A different `id` or `slug`.

It only warns when code content differs, because translators may translate code comments.

```python
# scripts/check_i18n.py  (run: python3 -I scripts/check_i18n.py)
import re, sys, pathlib
SRC = pathlib.Path("docs")
TR = pathlib.Path("i18n/pt-BR/docusaurus-plugin-content-docs/current")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
URL = re.compile(r"https?://[^\s)>\"']+")
KEY = re.compile(r"^(id|slug):.*$", re.M)
bad = 0
for t in sorted(TR.rglob("*.md*")):
    s = SRC / t.relative_to(TR)
    if not s.exists():
        print(f"FAIL {t}: no English source"); bad += 1; continue
    a, b = s.read_text(), t.read_text()
    if len(FENCE.findall(a)) != len(FENCE.findall(b)):
        print(f"FAIL {t}: code block count differs"); bad += 1
    if set(URL.findall(a)) != set(URL.findall(b)):
        print(f"FAIL {t}: URL set differs"); bad += 1
    if KEY.findall(a) != KEY.findall(b):
        print(f"FAIL {t}: id/slug differs"); bad += 1
    if FENCE.findall(a) != FENCE.findall(b):
        print(f"WARN {t}: code content differs")
sys.exit(1 if bad else 0)
```

**Gate C: staleness report. Non-blocking.** List translated files whose English source changed after the translation's last commit. Post the list as a PR comment or a weekly issue.

```sh
for t in $(git ls-files 'i18n/pt-BR/docusaurus-plugin-content-docs/current'); do
  s="docs/${t#i18n/pt-BR/docusaurus-plugin-content-docs/current/}"
  [ "$(git log -1 --format=%ct -- "$s")" -gt "$(git log -1 --format=%ct -- "$t")" ] && echo "stale: $t"
done
```

**Rule: English PRs never wait on translations.** Stale pages get fixed afterwards by the pt-BR team.

**Optional LLM spot check.** On each PR, back-translate the paragraphs with warnings, data-loss risks, or security guidance, and diff the result against the English. It flags drift, but it is not proof. Treat a flag as a question for the reviewer, not as a verdict.

## 4. Write `TRANSLATING.md` (45 min)

Include these points:
- **English is the source of truth.** The pt-BR pages say so in the banner.
- **Don't translate:**
  - Code, config keys, CLI flags, and identifiers.
  - File names, slugs, and `id`.
  - Release notes, the blog, and generated reference pages.
  - Security advisories and legal pages.
- **Glossary.** Create `i18n/pt-BR/GLOSSARY.md` with a decision per term:
  - "Lanternfish", "broker", "topic", "queue", "consumer", "ack", and similar.
  - Which terms stay in English.
  - The address form: `você`, not `tu`.
  - Have the contributors fill it in. Review it as the first PR.
- **Explicit heading IDs** (see step 2).
- **One section per PR.**
- **Same license as the docs.** Add sign-off or DCO if you use it. Credit translators in a `TRANSLATORS` section or file.
- **Priority order:** intro, install, quickstart, core concepts, then operations. Pull the top ~30 pages from your analytics. Skip the long tail.

## 5. Roles, banner, and soft launch (45 min)

- **Roles:**
  - Add `.github/CODEOWNERS` with `/i18n/pt-BR/ @contrib1 @contrib2` (their GitHub handles).
  - Add the label `i18n/pt-BR`.
  - Give them GitHub Triage permission, not Write.
  - **Branch rule: the PR author can't be the only approver.** The other contributor must approve. You press merge once CI is green.
- **Banner:** swizzle the doc layout, or use `announcementBar` for pt-BR only. Text: "Tradução mantida pela comunidade. O inglês é a versão oficial e esta página pode estar desatualizada." Ask a contributor to check the wording.
- **Soft launch:**
  - Keep the dropdown hidden and `noIndex` on until about 15 core pages are done and CI is green.
  - Then add `{ type: 'localeDropdown', position: 'right' }` to the navbar and remove `noIndex`.
- **Search:** with Algolia DocSearch, add the locale as a facet filter and ask them to re-crawl. Local-search plugins need their per-locale option.
- **Exit rule:** if a page stays stale for 3 months, add a "possibly outdated" banner to it. If the whole team goes silent for 6 months, set `noIndex` again and hide the dropdown. Write this rule in `TRANSLATING.md` now, so removing the locale later is not an argument.

## Merging the two open PRs today

1. Check that they only touch `i18n/pt-BR/...`.
2. Confirm the build and the Gate B script pass.
3. Make each contributor approve the other's PR.
4. Merge into `main`. The locale stays hidden and `noIndex`.

## What stays your job

- Press merge when CI is green and a CODEOWNER other than the author has approved.
- Read the staleness report once a month (10 min).

**Next action:** tell me your Docusaurus version, whether the docs are versioned, and your search provider. Then I can write the config, the CI workflow, and `TRANSLATING.md` for you to review.