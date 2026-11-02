I can't wire `translation-drift-check.py` yet, because there's no earlier plan in this conversation and no such script that I can see. I won't guess its flags or output format. Below are a CI design that doesn't depend on the script's internals, and a minimal drift check you can use or swap for your own. I assumed GitHub Actions, a `docs/` source directory, and `locale/ja/LC_MESSAGES/` at the root of `thornbury-docs-ja`. Adjust any of these that differ.

## Design decisions

1. **Compare against the POT, not git history.** Build the gettext catalogs from the English source with `sphinx-build -b gettext`. Merge them into the Japanese PO files with `sphinx-intl update`. Count the entries that are untranslated, fuzzy, or obsolete. This catches new English strings as soon as they land.
2. **Check out both repos in one job.** The PO files live in `thornbury-docs-ja`, so the job needs a second `actions/checkout`. If that repo is private, `GITHUB_TOKEN` can't read it. Use a read-only deploy key or PAT stored as a secret.
3. **Report only, never block.** English-side authors can't fix Japanese drift, so a failing check would only train people to ignore it. Write a table to the job summary. Fail only if you later add an explicit threshold.
4. **Run it on two triggers.** Run it on PRs that touch `docs/**`, and on a nightly schedule. Drift also changes when the ja repo changes, and a PR-only trigger never sees that.

## The `.. include::` problem

This affects what the report means.

- **Snippet strings are counted once per including page.** If a snippet sits inside the source tree as a plain `.rst`, Sphinx also builds it as a standalone document. Its strings then appear in the snippet's own catalog as well as in each page that includes it.
- **A single untranslated snippet string makes every including page look behind.** The report then looks much worse than the real backlog.
- **Fix the double counting.** Put snippets in `docs/_snippets/` and add that directory to `exclude_patterns` in `conf.py`. Then dedupe by `msgid` across catalogs in the report, and list snippet-sourced strings in their own section. The Japanese team then sees one fix with a fan-out count instead of dozens of "behind" pages.
- **Check how your build behaves.** Check how `gettext_compact` is set in `conf.py`. If it's `True`, catalogs are merged by top-level directory and per-page counts won't match page names.

## The check script (minimal replacement)

```python
#!/usr/bin/env python3
"""Report untranslated/fuzzy Japanese entries per catalog, deduped by msgid."""
import sys
from collections import defaultdict
from pathlib import Path

import polib

SNIPPET_MARKER = "_snippets/"  # matches the directory excluded in conf.py

def main(po_dir: str) -> int:
    seen = set()
    per_catalog = defaultdict(lambda: {"untranslated": 0, "fuzzy": 0, "total": 0})
    snippet_gaps = set()
    for po_path in sorted(Path(po_dir).rglob("*.po")):
        catalog = polib.pofile(str(po_path))
        name = po_path.relative_to(po_dir).with_suffix("").as_posix()
        for entry in catalog:
            if entry.obsolete:
                continue
            stats = per_catalog[name]
            stats["total"] += 1
            behind = "fuzzy" if "fuzzy" in entry.flags else None
            if not entry.translated() and not behind:
                behind = "untranslated"
            if not behind:
                continue
            if any(SNIPPET_MARKER in loc for loc, _ in entry.occurrences):
                snippet_gaps.add(entry.msgid)  # dedupe: one fix, many pages
                continue
            if entry.msgid in seen:
                continue
            seen.add(entry.msgid)
            stats[behind] += 1

    print("| Catalog | Untranslated | Fuzzy | Total | Behind |")
    print("|---|---:|---:|---:|---:|")
    for name, s in sorted(per_catalog.items(), key=lambda kv: -(kv[1]["untranslated"] + kv[1]["fuzzy"])):
        behind = s["untranslated"] + s["fuzzy"]
        if behind:
            pct = 100 * behind / s["total"]
            print(f"| {name} | {s['untranslated']} | {s['fuzzy']} | {s['total']} | {pct:.0f}% |")
    print(f"\nShared snippet strings behind: {len(snippet_gaps)}")
    return 0  # report only

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
```

The script dedupes by `msgid`, so a string repeated across pages counts once. That's a deliberate choice, and it can hide per-page urgency. If you want a per-page "is this page complete" view, drop the `seen` check and keep the snippet section.

## Workflow: `.github/workflows/translation-drift.yml`

```yaml
name: translation-drift
on:
  pull_request:
    paths: ["docs/**", "locale/**"]
  schedule:
    - cron: "0 5 * * *"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  drift:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/checkout@v4
        with:
          repository: thornbury/thornbury-docs-ja   # confirm org/name
          path: ja
          token: ${{ secrets.DOCS_JA_READ_TOKEN }}   # needed only if private

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - run: pip install -r docs/requirements.txt sphinx-intl polib

      - name: Build English message catalogs
        run: sphinx-build -b gettext docs _build/gettext

      - name: Merge catalogs into the Japanese PO files
        # Runs on the checkout in the runner only; nothing is pushed.
        working-directory: ja
        run: sphinx-intl update -p ../_build/gettext -l ja -d locale

      - name: Report drift
        run: |
          {
            echo "## Japanese translation drift"
            python scripts/translation-drift-check.py ja/locale/ja/LC_MESSAGES
          } >> "$GITHUB_STEP_SUMMARY"
```

Swap `scripts/translation-drift-check.py` for your own script if you have one, and adapt its arguments.

## Checks before you merge it

- **Confirm `sphinx-intl update` rewrites the files in the `ja` checkout only.** It does, but the checkout is throwaway, so keep it out of any later `git push` step.
- **Check the catalog path.** `locale/ja/LC_MESSAGES` inside `ja/` must match the real repo layout. Verify it by running the workflow once with `workflow_dispatch`.
- **Run a positive control first.** Add a new English paragraph on a scratch branch and confirm the table shows it as untranslated. Do the same with an edit to a snippet, and check that it shows up in the snippet line. An empty table doesn't prove the pipeline works.
- **Pin the Sphinx version in CI.** Pin it to the version your docs build uses, because gettext output varies a little between releases.

## Open questions

1. Can you point me to the plan or script you mean? If it exists elsewhere, I'll adapt the wiring to its real interface.
2. Is `thornbury-docs-ja` private? That decides the token setup.
3. Do your snippets live in a dedicated directory today, or are they scattered?