## Sandhill catch-up changelog — ready to execute today

You don't have time to hand-summarize 640 commits. Don't try. Use GitHub's own release-notes generator to do the categorization, then spend your day editing, not transcribing. Below is the exact sequence, the commands, and a filled-in template — publish through GitHub Releases, which costs you zero infrastructure and reaches everyone already watching the repo.

### Step 1 — Let GitHub do the sorting (10 minutes)

GitHub can auto-generate categorized release notes between any two refs, grouped by PR label, with a "New Contributors" section built in — no server, no page, no email tool needed.

```
gh api repos/<org>/sandhill/releases/generate-notes \
  -f tag_name="v<next-version>" \
  -f target_commitish="main" \
  -f previous_tag_name="<last-published-tag>" \
  --jq .body > catchup-raw.md
```

If PRs were never labeled consistently, pull the raw list instead and bucket it yourself with `gh`:

```
gh pr list --repo <org>/sandhill --state merged --limit 200 \
  --json number,title,labels,mergedAt \
  --jq '.[] | [.mergedAt, .number, .title, (.labels|map(.name)|join(","))] | @tsv' \
  > merged-prs.tsv
```

Sort that TSV by date, skim titles for `feat|fix|BREAKING|deprecat`, drop it into four buckets: **Breaking**, **Added**, **Fixed**, **Everything else**. With 190 PRs this triage takes under an hour if you don't read anything twice — title only, no diffs, unless a title is ambiguous.

### Step 2 — Pick the shape: one entry, not seven

Management asked for one entry, and that's the right call given your time — don't try to reconstruct six release boundaries from memory. Structure it as a single **"Catch-up: 18 months of Sandhill"** entry, organized by *theme*, with a compare link doing the archival job for anyone who wants tag-by-tag detail:

```
Full diff since <last-changelog-tag>: 
https://github.com/<org>/sandhill/compare/<last-changelog-tag>...<HEAD>
```

That one link substitutes for the "hosted page" you don't have — GitHub's compare view already renders every commit and file diff, for free, permanently.

### Step 3 — The entry itself

Drop this into `CHANGELOG.md` and publish the same content as a GitHub Release. Every bracketed item below is a placeholder — pull the real value from `merged-prs.tsv` before publishing. Do not ship this with brackets still in it.

```markdown
## [<next-version>] — 2026-09-18

_This entry covers ~18 months of unlogged work (640 commits, 190 merged PRs)
since the last published changelog entry at [<last-tag>]. Grouped by theme,
not by the individual releases that shipped in between — see the
[full compare](https://github.com/<org>/sandhill/compare/<last-tag>...<next-version>)
for the complete commit-by-commit history._

### ⚠️ Breaking changes
- [<real breaking change #1, from a PR titled "BREAKING: ..." or a major DSL/task-name change>] (#<pr>)
- [<breaking change #2, e.g. minimum Gradle/Kotlin version bump>] (#<pr>)

### Added
- [<biggest new feature/task/DSL block, one line, plug-consumer-facing impact stated>] (#<pr>)
- [<second feature>] (#<pr>)
- [<third feature>] (#<pr>)
- (bundle minor additions into one line): Also added [<x>], [<y>], [<z>] — see compare link for details.

### Changed
- [<behavior change that isn't breaking but affects output/build times/defaults>] (#<pr>)
- [<performance improvement, with a number if you have one — e.g. build cache hit rate, configuration time>] (#<pr>)

### Deprecated
- [<anything phased out but still working>] — will be removed in <version>. Migrate via [<if a guide exists, link it; otherwise state the one-line replacement API>].

### Fixed
- [<highest-impact bug fix, one line, plain language>] (#<pr>)
- [<second>] (#<pr>)
- Dozens of smaller fixes and dependency bumps — full list in the [compare view](link).

### Upgrading
[One paragraph: what a consumer needs to touch in their `build.gradle.kts` to go from
<last-tag> straight to <next-version>. If nothing beyond a version bump, say so explicitly —
that's reassuring, not filler.]

### Thanks
Shipped by [<n> contributors] over 190 PRs. Particular thanks to [<names, if you know them
offhand — GitHub's auto-generated notes list first-time contributors automatically, reuse that>].
```

### Step 4 — Publish (no infrastructure needed)

1. Commit the `CHANGELOG.md` update on `main` (or a short-lived branch + fast-merge if you gate on review).
2. `gh release create <next-version> --title "<next-version> — 18-month catch-up" --notes-file catchup-final.md`
3. That's your distribution. Anyone watching the repo (Releases-only watch) gets notified natively. Pin a link to it at the top of the README's "Changelog" section if one exists — that's the only "page" you need, and it costs one line, not a frontend.
4. Send the same GitHub Release URL to whoever in management asked for this — that satisfies "published" without building anything new.

### Time budget for your one day

- **09:00–09:30** — generate-notes API call + raw PR export.
- **09:30–11:00** — triage 190 titles into the four buckets, no diff-reading.
- **11:00–13:00** — write Highlights/Breaking/Deprecated prose from the bucketed list (this is the only part that needs real writing judgment — everything else is mechanical).
- **14:00–15:00** — trim "Added"/"Fixed" to the entries that matter, fold the rest into the compare-link line. Resist listing all 190 — nobody reads a 190-line changelog, and a link to the full diff is more honest than padding.
- **15:00–15:30** — publish CHANGELOG.md commit + GitHub Release.
- **15:30–16:00** — buffer for whatever the label taxonomy turns out to be messier than expected (it will be, on an 18-month-stale repo).

That's a same-day, zero-new-infrastructure path from "640 unlogged commits" to one published, linkable entry.