# Known pitfalls — symptom / root cause / fix

Every entry below happened in production on this repo. If you see the symptom, go straight to the fix. The numbering matches SKILL.md.

## 1. `NameError: name 'updated_ids' is not defined` (crash at step [2/6])

- **Symptom**: run dies right after upstream sync; steps 2–6 never execute.
- **Cause**: `sync_all_upstreams()` returns its list; the caller stores it as `updated_repos`, but `sync_active_skills` was called with a stale local variable name.
- **Fix**: call `sync_active_skills(updated_repos)`.
- **Detect**: `python -m py_compile update.py` won't catch it (runtime-only) — read the call site.

## 2. `git add -A` commits ~6,900 junk files

- **Symptom**: giant diffs of duplicate skill dirs; nested `library/library/...` paths appear.
- **Cause**: re-clones create flat parent-prefixed duplicate dirs (`skills/agp-agp-9-upgrade/` beside `skills/agp-9-upgrade/`) because extraction flattens nested upstream paths and disambiguates collisions by prefixing the parent. ~850 such dirs sat untracked; `git add -A` stages them all.
- **Fix**: explicit-path staging in `git_commit_and_push()` — tracked changes directly; untracked only if an ancestor prefix exists in `index_prefixes` (built from `library/skills_index.json` paths). Clean existing dups with a content-hash dedup (compare each untracked dir's SKILL.md against tracked skills in the same repo; delete on match, refresh-in-place when content differs).
- **Detect**: `git status --porcelain --untracked-files=all -- library/` and count `??` entries; anything not in `skills_index.json` is junk.

## 3. Windows `WinError 206` — "The filename or extension is too long"

- **Symptom**: every `git add` chunk fails with WinError 206; commit aborts (but earlier chunks stay staged).
- **Cause**: Windows command lines cap at 32,767 chars; hundreds of ~150-char `library/` paths blow past it.
- **Fix**: `git add --pathspec-from-file=-` reading pathspecs from stdin, in 20K-char chunks, each prefixed `:(literal)` (disables glob magic for paths containing `#`, `*`, `?`).

## 4. Non-ASCII filenames never staged

- **Symptom**: Chinese-named files (e.g. `主视频1封面.png`) stay untracked run after run; whole chunks of 150+ paths silently skipped.
- **Cause**: default porcelain C-quotes non-ASCII as octal (`\344\270\255`); the parser stripped quotes but never unescaped, so the pathspec never matched.
- **Fix**: `git status --porcelain -z` (NUL-separated records; non-ASCII paths come through as raw UTF-8 even with `core.quotepath=true`) + decode UTF-8. Parse `xy = record[:2]`, `path = record[3:]`.

## 5. Duplicate flat skill dirs polluting the index/site

- **Symptom**: the same skill appears twice on the site after a repo updates; skill counts jump by hundreds.
- **Cause**: extraction walks the clone and copies each `SKILL.md` dir to `skills/<basename>`; when that already exists it prefixes the parent name (`<parent>-<name>`), creating a duplicate beside the original. `rebuild_all_indexes` walks `skills/` one level, so any repo that updates again gets its dups indexed and published.
- **Fix**: on collision, compare SKILL.md content — identical → refresh in place (rmtree + copytree); differs → keep the parent-prefix. Purge existing dups with the content-hash dedup from #2.

## 6. Junk files inside skills (`tests/`, `.github/`, `package.json`, lockfiles, `.gitignore`)

- **Symptom**: ~450 junk entries (~60 MB) inside `library/<repo>/skills/<name>/`; some skills ship 40 MB test dirs.
- **Cause**: extraction copies the entire upstream skill dir; the repo-root purge never looks inside skills.
- **Fix**: `clean_skill_internal_junk()` with `SKILL_JUNK_LEVEL1` (direct children: tests, test, spec, `__tests__`, dist, build, coverage, node_modules, `__pycache__`, `.github`, `.git*`, `.env.example`, package.json, lockfiles, tsconfig, Makefile, Dockerfile, `.temp*` strays) and `SKILL_JUNK_ANY_DEPTH` (node_modules, `__pycache__`, `.git`, `.venv`, coverage, `.DS_Store`, `*.log`, `.tsbuildinfo`). Called from `clean_nested()` (first step of every run, incl. the GH Actions cron) and immediately after extraction. **Never delete legitimate content** (references/, scripts/, assets/, examples/, evals/, agents/, templates/, demo/).
- **Boundary**: the user's own repo-root `.gitignore` is off-limits; only copies inside `library/` are junk.

## 7. skills.sh install counts all read "1M"

- **Symptom**: every repo in the audit shows `installs: 1000000`; the `--min-installs` filter matches everything; a phantom "1,543 missing repos" appears.
- **Cause**: the first-match regex grabbed the site-wide header chrome instead of the repo's own stat; the repo badge renders as `31.9M<!-- --> total installs` (an HTML comment between number and words), so the naive `\s*(?:installs|...)` pattern missed it and a wild fallback matched an SVG/JSON token.
- **Fix**: anchor on the repo badge — `([0-9]+(?:\.[0-9]+)?[KMkm])(?:\s*<!--.*?-->)*\s*total\s+installs` (case-insensitive); secondary fallback sums the per-skill leaderboard table. Verify against live pages (badge ≈ table sum). Delete the poisoned `skillssh/.cache_skills_sh.json` (7-day TTL would otherwise keep bad data) and re-audit.
- **Lesson**: any scrape of a shared site chrome is a bug waiting to happen — anchor to content unique to the page.

## 8. Stale hardcoded numbers in docs/frontend

- **Symptom**: AGENTS.md says "20,483 skills · 380 repositories" while the site shows 21,654 · 484; index.html shows 18,722 in ~25 static fallback spots.
- **Cause**: docs and the SPA shell had hand-written numbers; only badge-style lines were auto-updated; static HTML fallbacks (stat IDs, aria-labels, placeholders, pagination) were never touched.
- **Fix**: `sync_frontend_doc_numbers()` — reads fresh `stats.json` + file sizes right after build-catalog, applies number-agnostic regexes to 9 files (incl. the en-dash pagination `Showing 1.50 of N skills` where `.` matches U+2013), writes changes directly. New phrasings only ever need one new rule; the rules then work forever.
- **Gotchas hit while fixing**: a group-ref rule consumed the `>` of `<span>` producing `<span370484 Repositories</span>` — prefer whole-token patterns over group refs unless the prefix must be preserved; verify each new rule with a dry-run replica before the real run.

## 9. `fatal: Unable to create '.git/index.lock': File exists`

- **Symptom**: every git command fails mid-run; nothing commits.
- **Cause**: a crashed git call (often inside a sub-script) left a stale lock.
- **Fix**: `_git_run()` wrapper — on an index.lock error, check `tasklist` for a live `git.exe`; if none, remove the lock and retry once. (Never remove it while git is actually running.)

## 10. Big repos stuck at "preserved existing skills & updated watermark"

- **Symptom**: 5–8 repos never update; log says watermark written without a clone.
- **Cause**: the 15 s clone timeout was too tight for large repos; the fallback writes the watermark so the repo isn't retried until its next upstream commit.
- **Fix**: clone timeout raised to 45 s (ls-remote stays at 5 s). If a repo still stalls, delete its `.upstream_commit` watermark to force a retry on the next run.

## 11. Background runs die mid-job

- **Symptom**: a long run stops without a traceback; the log just ends mid-line; no auto-resume.
- **Cause**: the agent harness kills backgrounded processes when work is moved to background / sessions end.
- **Fix**: run anything longer than ~5 minutes in the user's own terminal. Short offline runs (~3 min) are fine in the background. Ingestion is resumable — re-running picks up where it stopped (ingested repos are skipped, watermarks prevent re-cloning).

## 12. Confusing hot-set counts (90 vs 130)

- **Symptom**: docs say 90 installed skills; the site says 130.
- **Cause**: the site hot-set is the **union** of `skills/` (90) and the parent workspace `../.agent/skills/` (91, outside the repo). `sync_active_skills` and `count_hot_set_skills` must replicate that union or the numbers disagree.
- **Fix**: `count_hot_set_skills()` merges both dirs (guarded); `sync_active_skills` syncs the parent workspace via the unique-name fallback (no lockfile there).

## 13. Docs metrics disagree with the site (two different measures)

- **Symptom**: README badges say 26,852 skills / 484 repos; stats.json says 21,654 / 484.
- **Cause**: doc metrics use *library-reserve* measures (every index record / every repo folder) while the site uses *catalog* measures (unique skills after opt-out/dedup; repo map from the library scan).
- **Status**: both auto-update every run; they intentionally measure different things. If a single number is ever required, quote stats.json (catalog measures) and label the reserve number as such.
