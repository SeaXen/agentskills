**Don't wire `translation-drift-check.py` into Thornbury's CI. It can't see your Japanese pages.** I read the skill, `references/freshness-contract.md` and the script. Three things in your setup rule it out:

- **PO files.** The skill says to track strings, not files, where gettext tooling exists. It uses fuzzy and untranslated counts as the freshness measure, and the script and per-file pin only apply to mirrored file trees. The script's docstring puts gettext out of scope. It looks for a `source_commit` pin in each page's front matter. PO files have none, so every page would come back `no-pin` or `untranslated`.
- **Separate repo.** The contract says translations kept in a separate repository fall outside the script. It needs the source and the translations in one git history.
- **`.. include::` snippets.** The script doesn't track includes. The string-level check below covers them (see the note after the script).

There is also no earlier plan in this session. The script ships with the skill, so I treated "your plan" as that.

## What to wire instead

Wire a string-level report, informational and non-blocking. The freshness number it produces is the share of PO files with zero fuzzy and zero untranslated entries.

The CI job runs in the Thornbury repo, since that's where the source and `conf.py` live. It does five things:

1. Check out Thornbury and `thornbury-docs-ja`.
2. Run `sphinx-build -b gettext` to regenerate the `.pot` files from the current source.
3. Run `sphinx-intl update` on a CI-local copy of the Japanese PO files. This merges the new source strings in and marks changed strings fuzzy. Nothing is committed.
4. Count fuzzy, untranslated and obsolete entries per PO file.
5. Publish the result as a CSV artifact and a job summary.

### `.github/workflows/translation-drift.yml`

```yaml
name: translation-drift
on:
  schedule:
    - cron: "0 6 * * 1"   # weekly; drift moves with releases, not per push
  pull_request:
    paths: ["docs/**"]
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/checkout@v4
        with:
          repository: <owner>/thornbury-docs-ja   # adjust; add `token:` if private
          path: .ja-docs
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r docs/requirements.txt sphinx-intl polib   # adjust requirements path
      - name: Regenerate .pot from current source
        run: sphinx-build -b gettext docs _build/gettext              # adjust source dir
      - name: Merge new source strings into a CI-local copy of the ja PO files
        run: |
          mkdir -p locale/ja/LC_MESSAGES
          cp -R .ja-docs/locale/ja/LC_MESSAGES/. locale/ja/LC_MESSAGES/  # adjust path inside the ja repo
          sphinx-intl update -p _build/gettext -l ja -d locale
      - name: Report
        run: python3 scripts/po-drift-report.py locale/ja/LC_MESSAGES > drift-ja.csv
      - name: Job summary
        run: |
          echo '### Japanese translation drift' >> "$GITHUB_STEP_SUMMARY"
          echo '```' >> "$GITHUB_STEP_SUMMARY"
          column -s, -t drift-ja.csv >> "$GITHUB_STEP_SUMMARY"
          echo '```' >> "$GITHUB_STEP_SUMMARY"
      - uses: actions/upload-artifact@v4
        with:
          name: drift-ja
          path: drift-ja.csv
```

### `scripts/po-drift-report.py`

```python
#!/usr/bin/env python3
"""Print per-PO-file translation drift as CSV. Read-only. Needs polib.

Run after `sphinx-intl update`, so changed source strings are fuzzy and new ones untranslated.
"""
import csv
import sys
from pathlib import Path

import polib


def main():
    root = Path(sys.argv[1])
    po_files = sorted(root.rglob("*.po"))
    # Fail closed: a path typo or an empty checkout must not look like "no drift".
    if not po_files:
        print(f"error: no .po files under {root}", file=sys.stderr)
        return 2
    writer = csv.writer(sys.stdout)
    writer.writerow(["po_file", "status", "entries", "fuzzy", "untranslated", "obsolete"])
    for path in po_files:
        po = polib.pofile(str(path))
        fuzzy = len(po.fuzzy_entries())
        untranslated = len(po.untranslated_entries())
        status = "current" if fuzzy == 0 and untranslated == 0 else "behind"
        writer.writerow([path.relative_to(root).as_posix(), status,
                         len([e for e in po if not e.obsolete]),
                         fuzzy, untranslated, len(po.obsolete_entries())])
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

I haven't run any of this. Dry-run it once with `workflow_dispatch` and check that the CSV isn't empty. Then run it against a PO file you know is behind, to confirm it reports `behind`.

## How `.. include::` behaves

Sphinx inlines included content at parse time. Strings from a shared snippet should therefore land in the `.pot` of each page that includes it, and any change to the snippet turns those strings fuzzy or untranslated in every affected page. That's the "count includes as changes" rule, handled at string level. Check it once: edit a snippet, rebuild, and confirm the including pages' `.pot` files change.

## Decisions for you

1. **Per-page granularity needs `gettext_compact = False` in `conf.py`.** The default (`True`) merges pages into one catalog per top-level directory, so the report would say "this directory is behind", not "this page is behind". Changing it renames the PO files, which breaks the Japanese team's existing files. Ask them before you flip it. If it stays `True`, the report works but at directory level.
2. **Your Japanese team may not need this job in your repo.** They own the PO files. The same job can run in `thornbury-docs-ja` with Thornbury checked out instead. That version can also fail their PRs. I put it in your repo because you asked which pages are behind.
3. **Keep it non-blocking for now.** Add a gate later, once the critical-path pages (quickstart, install, top task pages) are current. The skill's baseline target is at least 80% of the critical-path pack current at every release. Replace that with your own release cadence.
4. **Gates from the skill that this setup doesn't cover.** There are no outdated banners on pages and no fallback to the English page. The launch gate (two named reviewers, a glossary, a retirement threshold) isn't enforced by this job either. If the Japanese site is already live, ask the team whether those exist.

I assumed your paths and the `<owner>` in the workflow. Tell me your real layout (docs dir, where the PO files sit inside `thornbury-docs-ja`, whether it's public) and I'll fix them.