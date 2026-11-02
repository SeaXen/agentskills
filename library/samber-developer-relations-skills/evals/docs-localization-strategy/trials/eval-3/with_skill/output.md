**Verdict: the plan does not hold.** Three of the four parts break the skill's rules, and the shallow checkout breaks the CI job outright. The goal is right. The mechanism is wrong.

## Do first (5 minutes)

1. Copy `scripts/translation-drift-check.py` from the skill into the Harrowgate docs repo.
2. In a full clone, run `python3 scripts/translation-drift-check.py --source docs/en --locale ja=docs/ja --format summary`.
3. Expect `no-pin=140`. That count is your real baseline.

## Part by part

### 1. `translated_at` plus the en git date: replace with a commit pin

- **Date compare is the wrong signal.** The skill says to detect drift by source history after the pin, never by dates.
- **Day granularity hides changes.** An en edit on the same day as `translated_at` is ambiguous.
- **A completion date hides drift.** The translator works for days. Anyone who stamps the date when finishing hides every en change made in between. Pin the en file's last commit when translation starts.
- **Counts are impossible.** A date cannot say 1 commit behind versus 30. You need that count to triage and to set `far`.
- **Renames are invisible.** A moved en file has no history at the new path. The script follows renames and reports `moved`.
- **Bumping the date hides drift.** Someone can bump `translated_at` without applying the content change.
- **Use a commit hash instead.** Add `source_commit` and keep `translated_on` as a display date only.

```yaml
source_path: docs/en/how-to/rotate-secrets.md
# en file's last commit when translation STARTED; hash only
source_commit: 3f9c2e1
translated_on: 2026-10-02
# human | llm-reviewed | llm-unreviewed | community
translation_method: human
reviewed_by: <name>
```

### 2. Shallow checkout (`fetch-depth 1`): this breaks the job

- **Every page looks modified at HEAD.** With one commit of history, `git log -- <file>` returns that single commit for every en file. A date check then sees all en pages as newer than `translated_at`. A first run flags 140 of 140 pages, then stays permanently noisy. A noisy gate gets ignored.
- **File mtime fails too.** On a fresh checkout, mtime is the checkout time.
- **The script refuses shallow clones.** It exits 2 with a shallow-clone error rather than report every pin as unknown.
- **Fix: `fetch-depth: 0`** on `actions/checkout`, or `git fetch --unshallow` as a step. Both assume GitHub Actions (ASSUMED).
- **A cheaper fetch might work.** A blobless clone (`--filter=blob:none`) keeps full history and skips file contents. I have not tested it with this script, because rename detection may fetch blobs lazily. Time it before relying on it.

### 3. Copying `last_verified: 2026-09-12` into ja: do not copy

- **A copy claims a test nobody ran.** A ja page showing the en date claims that someone verified the Japanese page. Nobody did. This is the skill's "borrowed test stamps" failure.
- **A copy goes stale at once.** If en changes or is re-verified, the ja value stays frozen at 2026-09-12.
- **Render the stamp from the source page, and only while the pin is current.** Show "verified on the source page: 2026-09-12 (English)". When the page is `behind` or `far`, show the outdated banner instead of the stamp.
- **Wiring for Hugo (my design, not from the skill):**
  1. CI runs the drift script with `--format json`.
  2. The output goes to `data/` at build time.
  3. The page template reads the status for that path.
  4. When the status is `current`, it looks up the en page's `last_verified` at render time.
- **Own stamps need a re-run.** Add `locale_last_verified` only if someone re-ran the procedure in a Japanese environment.
- **Side effect to expect.** An en commit that only bumps `last_verified` counts as a source change. It makes ja `behind` with no content change. The reviewer clears it by bumping the pin. The script counts a typo fix like a rewrite.

### 4. `source_version: v3.2`: fine as a label, wrong as the pin

- **Tags are too coarse.** A tag cannot show what changed on one page between tags. It cannot show which commit the translator saw if they worked from `main`.
- **The script rejects tags.** A tag name in the pin field gives `unknown-pin` ("not a commit hash").
- **Keep it as a display field.** Use it for "Translated from the v3.2 docs". The script ignores unknown keys, so there is no conflict.
- **Several docs versions are live?** Translate the latest only. Older versions fall back to en.

## Backfill for the 140 existing pages

- **Do not stamp today's date on everything.** That marks every stale page as current.
- **No pin means stale.** Leave existing pages unpinned until a reviewer confirms each against en, then add the pin.
- **Enforce on new work only.** Use `--since <ref>`, where `<ref>` is today's commit, so only pages added or edited afterwards can fail the build. Drop `--since` once the backlog is pinned.
- **Triage queue (optional heuristic, ASSUMED).** For each page, take the en commit at or before the ja file's last edit. Use it only to rank pages for review. Do not write it as a pin, because it overstates freshness.

## CI job

Pin new work and report the rest:

```
python3 scripts/translation-drift-check.py --source docs/en --locale ja=docs/ja \
  --format csv --far <commits per release> \
  --fail-on no-pin,unknown-pin --since <ref>
```

- **Pass `--far`.** Scale it to your commits per release. The default is 5 (baseline); pages with more commits than that since the pin are reported `far`.
- **`behind` and `far` are not build failures.** Show the banner on `behind` pages, and send `far` pages to the review queue. Serve the en page for a critical-path page that goes `far`.
- **Includes are not tracked.** A changed Hugo partial or shortcode changes every page that uses it, but the script does not see that. Pin and check those separately.

## Assumptions

- ASSUMED: Hugo front matter is YAML (`---`). The script does not read TOML (`+++`).
- ASSUMED: `docs/ja` mirrors `docs/en` paths exactly, with `.md` files and no `page.ja.md` suffixes.
- ASSUMED: CI is GitHub Actions.
- ASSUMED: no ja page carries a pin today.

## Not covered by this plan

The skill gates a locale on more than freshness. Check these before you invest in tooling:

1. **Two named ja reviewers**, so nobody approves their own change.
2. **A glossary** with "do not translate" decisions.
3. **A retirement rule** and a person allowed to pull the locale.
4. **A translation label and banner** on every ja page.
5. **Page set versus reviewer hours.** Check whether 140 pages fit your capacity. The skill's baseline is about 15 to 30 minutes per changed page.

If items 1 to 3 are missing, ja is `gated` under the skill's launch rule, and the tooling above comes second.

## Time estimates

- **CI wiring and front-matter template:** about 1 to 2 hours (my estimate).
- **Backlog review:** cannot be sized until the first run shows how many pages are `behind` or `far`. Use the skill's baseline of about 1 hour per page on first review.

**Next question for you:** who are the ja reviewers, and how many hours per release do they have?