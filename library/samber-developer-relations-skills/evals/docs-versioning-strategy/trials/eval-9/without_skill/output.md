# Windlass docs: cumulative version badges spec

**First action:** read **Decision 1** below. The 4.0 config rewrite is the one place where badges fail, and it shapes the rollout.

I assumed a static docs generator with component or shortcode support (MDX, Hugo, Docusaurus or similar). I did not inspect your repo. If you have no shortcodes, use plain HTML `<span class="badge">` with the same vocabulary. The build-time validation described later then needs a small script.

## Decisions

1. **Badges cover small deltas only. The 4.0 config schema gets its own pages.**
   - A badge says "this exists from version X" or "this goes away in Y".
   - A rewritten schema reuses the same key names with different meaning, so a reader on 3.x cannot tell which `pipeline:` block applies to them.
   - Keep `config/` for 2.x and 3.x. Add `config-v4/` for 4.0.
   - Put a banner and a link at the top of each. Badge the *concepts* that carry over, such as "Replaced in 4.0".
   - Everything else stays on one cumulative page set.
2. **Untagged means "applies to every supported version".** The writer never has to backfill history. Only changes get badges.
3. **The floor is the oldest supported minor of 2.x.**
   - Anything in the floor version is untagged.
   - Never write "Added in 1.0".
   - When a line reaches EOL, the floor moves up and its badges are deleted (see Retirement).
4. **A badge is one fact in one place.** Do not repeat a version number in prose beside the badge. Prose that says "since 3.2" goes stale.
5. **Granularity is heading, table row or list item.** Never tag paragraphs or sentences. If a paragraph needs two badges, split the section.

## What to tag

Tag these five things:

| Tag | Use when | Example |
|---|---|---|
| `Since` | New feature, flag, config key, API field or endpoint | Runner label `--tags` |
| `Changed` | Same name, different behavior or default | Default concurrency changed |
| `Deprecated` | Still works, scheduled for removal | Old registration token flow |
| `Removed` | Gone from a version on | A flag dropped in 4.0 |
| `Preview` | Documented but unreleased | Anything 4.0 until GA |

Do not tag:
- Bug fixes.
- Internal refactors.
- Anything whose behavior is identical on all supported lines. That is the default case.
- Whole pages that are new. Put one badge on the page title.

A feature that exists on both lines but arrived in different minors gets one badge with both values: `Since 2.8 · 3.1`. A reader on 2.7 sees at once that they lack it.

Priority for the first pass, by reader traffic (pull this from your analytics):
1. Config reference. In 3.x and 2.x, this is the highest-delta page.
2. CLI reference (flags).
3. Runner registration and install.
4. API and webhooks.
5. Everything else, opportunistically.

## How to tag

### Component vocabulary

Four components, one argument style. Use text plus an icon. Color alone must not carry meaning.

```mdx
### Runner labels <Since v="2.8, 3.1" />

| Key | Description |
|---|---|
| `cache_dir` | Cache path. |
| `max_jobs` <Changed v="3.2">Default raised from 1 to 4.</Changed> | Concurrent jobs. |
| `legacy_token` <Deprecated v="3.4" removed="4.0" /> | Use `registration_token`. |
| `old_flag` <Removed v="4.0" /> | See [v4 config](/config-v4/). |
```

Rendered text, which also stays readable to search engines and coding agents:
- `Since 2.8 · 3.1`
- `Changed in 3.2: default raised from 1 to 4`
- `Deprecated in 3.4, removed in 4.0`
- `Removed in 4.0`

### Build-time validation

The "does it build" check is your only CI. Make the badge component enforce the rules, so a bad tag fails the build:

1. Keep `versions.json` listing every released version per line, plus `floor`, plus any `preview` versions.
2. The component throws if `v` is not in `versions.json`. This catches `3.12` typed for `3.2`.
3. It throws if `v` is at or below the floor. Those would be noise.
4. It throws if `removed` is earlier than `v`.
5. It throws on unknown props.

The component takes about 1–2 hours to write. After that, engineers cannot silently break it.

### Engineer workflow (PRs go straight in)

You cannot gate those PRs, so make tagging the path of least resistance:

1. Add one line to the PR template: `Docs: [ ] no user-visible change  [ ] docs updated with badge  [ ] docs follow-up needed`.
2. Put a cheat-sheet in `docs/CONTRIBUTING.md`, one screen: the four components, one example each, and "untagged = all versions".
3. Engineers tag with the **next unreleased version** (from `versions.json`). They do not guess it.
4. The writer reviews **after merge**, not before. This fits PRs that go straight in.

### Writer's weekly sweep (30 min)

1. Read the release notes or changelog since the last sweep.
2. For each "added", "changed" or "removed" item, check that a badge exists on the matching docs section.
3. Fix gaps. Note the recurring ones. If one engineer keeps missing it, ping them.
4. Do this at every release too. It is the only real completeness check you have.

## Version selector (not in v1)

Do not build a "pick your version and hide sections" selector first. Badges alone deliver most of the value. A selector is a later CSS-only filter driven by the same badge data. Consider it after 4.0 GA if readers ask for it.

## Retirement

- When a line reaches EOL, the floor moves up.
- Delete `Since` badges at or below the new floor. This is a mechanical find-and-edit, about 1 hour.
- `Removed`/`Deprecated` badges for versions at or below the new floor, and the text they annotate, can be deleted outright.
- Put the EOL date in the support policy page now. Without it the cleanup never gets scheduled.

## Rollout (about 8 weeks to 4.0)

Time estimates assume one part-time writer.

**Weeks 1–2: foundation (~8 hours)**
1. Write `versions.json` with the floor, supported lines and `preview` for 4.0.
2. Build the four components with validation.
3. Add the PR template line and the one-screen cheat-sheet.
4. Pilot on a single page, the CLI reference. Check it renders, and that a deliberately wrong tag fails the build.

**Weeks 3–5: backfill top pages (~12–15 hours)**
1. Walk the changelog from the floor forward, one release at a time.
2. Tag the config reference, CLI reference, install/registration and API pages, in that order.
3. Skip pages where nothing changed since the floor.
4. Announce the convention to engineers once the first pages are done, so they see real examples.

**Weeks 5–7: 4.0 preparation**
1. Create `config-v4/` once the schema is stable enough to document. Mark it `Preview`.
2. Add `Deprecated … removed="4.0"` badges to 3.x keys that the rewrite kills. These are the highest-value badges for readers planning ahead.
3. Draft the 4.0 migration guide as its own page. Badges flag *that* something changes; the guide says *how* to move. The separation matters here because the schema rewrite is too big for badges.
4. Add banners linking `config/` and `config-v4/` to each other.

**Week 8: 4.0 GA**
1. Flip `4.0` from `preview` to released in `versions.json`.
2. Run the release sweep.
3. Update the support policy with 2.x EOL dates, then schedule the retirement cleanup.

## Risks

- **Engineers skip tagging.** Expect it. The weekly sweep and the release sweep are the safety net. Count misses for the first two releases and adjust the PR template if it is more than a few.
- **Badge clutter.** Dense tables with many badges become unreadable. If a section has more than 3, restructure instead of tagging more.
- **Wrong "next version" guess.** If a release slips, `Since 3.5` may ship as 3.6. Fix in the release sweep. Do not let engineers hard-code version names in prose.
- **Schema rewrite pressure.** If 4.0 scope shifts late, `config-v4/` content may churn. Keep it `Preview` until the schema freezes.

## Next action

Write `versions.json` (floor, supported lines, `4.0` as `preview`). Send it to me and I'll draft the component code for your generator. Tell me which one you use.