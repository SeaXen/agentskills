# Verdict: the plan doesn't hold as written

I didn't open the repo or run anything, so this rests on how git, Hugo and CI behave. Three of the four pieces have problems. The shallow checkout is the only one that breaks the design outright.

## 1. Shallow checkout makes the CI job meaningless

- With `fetch-depth: 1`, history is one commit. Every file's last-modified commit is that commit, so `git log -1 --format=%cI -- docs/en/x.md` returns the checkout date for all of them.
- Every en page then looks newer than any `translated_at`, so all 140 pages get flagged on every run. If you use file mtime instead, you get the checkout time, which is just as useless.
- The same applies to Hugo's `enableGitInfo` and `.GitInfo` / `.Lastmod`. They are wrong on a shallow clone too.
- Tags are not fetched at depth 1 either (`fetch-tags` is off by default), so a `v3.2` comparison breaks the same way.

## 2. "en modification date > translated_at" is the wrong signal even with full history

- **False positives:** any commit that touches the file counts, including typo fixes, prettier runs, link rewrites, renames, and front matter edits like bumping `last_verified`. One bulk commit flags all 140 pages.
- **False negatives and ties:** a date compares as a day, with timezone ambiguity. An en edit on the same day as the translation looks fresh.
- **Backfill:** you have no true `translated_at` for the existing 140 pages. Whatever you invent will mark them all fresh or all stale.

### Better signal: a content fingerprint

1. Store `source_hash` in each ja page. It is the SHA-256 of the en body, with front matter stripped and whitespace normalized.
2. CI recomputes the hash from the current en file and flags a mismatch.
3. This needs no history, so it works on `fetch-depth: 1`. It ignores renames and bulk touches, and it fires only when the en body changes.
4. Keep `translated_at` as human-readable metadata only. Don't use it for the check.
5. If you want to show what changed, add `source_commit` (the en SHA the translation was based on). The check can then run `git diff <sha> HEAD -- docs/en/x.md`. A diff between two commits only needs their trees, so `git fetch --depth=1 origin <sha>` for each distinct SHA works without full history.
6. If you do want history, use `fetch-depth: 0` with `filter: blob:none`. It's cheap and path-limited `git log` still works.

## 3. Copying `last_verified` into ja is misleading

- `last_verified: 2026-09-12` means someone checked the English content against the product on that date. On a ja page it says the Japanese text was verified, which is false if the translation lags.
- It also drifts. When en bumps `last_verified`, the ja copy goes stale. If you auto-sync it, the ja page claims verification of text that never changed.
- Instead, don't store it in ja at all. Have the ja template look up the en page (`.Translations` or `site.GetPage`) and render a labeled line. For example: "English version verified 2026-09-12. This translation is based on English as of <translated_at>."
- If `source_hash` mismatches, add a "this translation may be out of date, see English" banner.

## 4. `source_version: v3.2` is too coarse to carry the check

- Tags mark product releases, not docs edits. An en page can change several times between tags, and 140 pages stamped `v3.2` tell you nothing per page.
- Stamping every page with the same value says "the batch was translated at v3.2", not "this page matches v3.2".
- Keep it as display and reporting metadata, such as "translated against v3.2". Don't use it for staleness detection. If you do want a tag-based diff, fetch that tag explicitly (`git fetch --depth=1 origin tag v3.2`).

## Revised plan

1. Ja front matter gets `source_hash` (the check), `source_commit` (the diff and audit trail), `translated_at` and `source_version` (display only).
2. Drop the `last_verified` copy. Render en's value, labeled, from the template.
3. Backfill once, locally, on a full clone. For each ja page, `git rev-list -1 --before=<ja last commit date> main -- docs/en/<page>` gives an approximate `source_commit`. Compute the hashes from that revision and mark them as estimated. Anything doubtful goes to a human review list.
4. The CI job runs on `fetch-depth: 1`. It recomputes en body hashes and compares them to each ja `source_hash`. It also reports en pages with no ja counterpart and ja orphans.
5. Make the job report-only, as annotations or a scheduled report. Don't block en PRs on translation lag.
6. Guard against rubber-stamping: a PR that changes `source_hash` should also change the ja body, or carry an explicit "no translation change needed" label.

## Questions for you

- Is `source_version` meant to say "the product version the translation targeted"? If so, it's fine as display metadata.
- Do you want the job to block en PRs or only report? I recommend report-only.