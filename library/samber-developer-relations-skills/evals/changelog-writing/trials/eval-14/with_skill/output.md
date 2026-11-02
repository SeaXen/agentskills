# Sandhill CHANGELOG.md catch-up — plan and ready-to-fill deliverable

⚠️ No repo access this session — no git log, no PR list, no existing `CHANGELOG.md` content was given. Everything below is real, usable output for this week: a stated cut line, a reduced surface plan, a scaffold, and the exact commands to turn your actual 640 commits into entries. The bracketed placeholders are where your real data goes — nothing below is presented as if it were a real commit or PR.

## 1. Surface plan — cut to two

| Surface | Decision | Why |
|---|---|---|
| `CHANGELOG.md` | Keep | The ask. |
| Release body (git host) | Keep | Same text as the changelog, pasted twice — one edit produces both. |
| Hosted changelog page | Deleted | No frontend team, one-day ceiling. |
| Email | Deleted | No list exists. Don't build one to fill this gap. |
| In-product note | Deleted | No frontend team. |

Tier doesn't change this: even a tier-2 item in this range only earns the changelog/release-body pair, because Q12 (your ceiling) rules the rest out regardless of tier. If a genuinely breaking entry turns up in triage (see §5), it still only gets these two surfaces — it just goes first inside them.

## 2. Format — confirm, don't assume

Run this first:

```bash
head -20 CHANGELOG.md
```

If it already names Keep a Changelog or Common Changelog, stay on it — consistency beats the better spec. If the file is silent or this is effectively a restart, default to **Common Changelog**: Sandhill's readers are Gradle build authors pinning a plugin version and diffing what changed, which is exactly the "library, PRs are the unit of change" case. The scaffold below uses it. Swap headers if you're staying on Keep a Changelog — the entry content doesn't change, only the category names and the imperative-vs-past tense.

## 3. Size the real problem before trusting any plan

```bash
git log --merges --format='%h %s' <last-tag-changelog-covers>..HEAD > merges.txt
wc -l merges.txt
```

`<last-tag-changelog-covers>` is whatever version heading is currently at the top of the file. If tags exist for the six or seven releases that shipped since (check with `git tag --sort=creatordate`), work per-tag rather than as one 18-month blob — see §7. If no tags were cut cleanly, you're doing one range and §7's second option applies.

## 4. Auto-exclude — cheap, run once

```bash
grep -viE 'dependabot|chore\(deps\)|^chore: bump|^ci:|^test:|^style:|^build\(deps|^docs: (typo|format)' merges.txt > candidates.txt
wc -l candidates.txt
```

This is a heuristic on titles, not a final ruling — a PR titled `chore: bump` that quietly changed a default is still consumer-relevant (never exclude on label or path alone). Spot-check anything that looks borderline before trusting the drop. On a project this size, expect this pass to remove somewhere in the 30–45% range as dev-only noise (deps, CI, test, lint) — that's the working assumption, not a guarantee; `candidates.txt`'s line count tells you the real number.

## 5. Stated cut line 🎯

190 PRs in a day means full drafting for all of them isn't happening — set the line explicitly instead of trimming by feel:

1. Rank `candidates.txt` by consumer impact: breaking/floor changes first, then new public API surface (tasks, extensions, DSL options), then behavior/default changes, then fixes, then everything else.
2. **Full entry** (impact-first sentence, PR link) for the top ~10–12 per release — that comfortably covers the real content of an average ~27-PR release without inflating it.
3. Everything ranked below that line but still consumer-observable gets folded into one compressed trailing line per category: `Also in this release: <3–5 short phrases> ([#a](url), [#b](url), ...)`.
4. Everything with no consumer surface goes to the exclusion list (§8), with a reason, not silently.

This line is set by your own hour budget against the real candidate count from §4, not borrowed from any published significance threshold — state it to whoever reviews the result, and hand over the exclusion list alongside it so "what fell below the line" is visible, not implied.

## 6. One-day timeline

| Block | Task |
|---|---|
| 0:00–0:30 | §3–§4: pull the range, run the filter, get a real candidate count |
| 0:30–3:30 | Triage `candidates.txt` one line at a time: keep / also-line / exclude. ~2 min/item covers ~90 items in 3h — if the real candidate count is much higher, the cut line in §5 tightens, not the clock |
| 3:30–5:30 | Draft full entries for the kept set, ranked, breaking items first (§9 form) |
| 5:30–6:30 | Assemble scaffold (§7), fill traceability table and exclusion list (§8), paste release body |
| 6:30–7:00 | Verification gate (§10) |

## 7. Splitting the catch-up

Six or seven releases already shipped — document them as six or seven sections with their real dates, not one entry pretending to be a single release:

```bash
git log -1 --format=%cs <tag>   # real date for each section heading
```

If tags don't map cleanly to those releases, say so in the file rather than faking version boundaries — one dated "2024-XX through 2026-03 catch-up" section is honest; six fabricated version boundaries are not. Either is fine; picking one silently and presenting it as the other is the failure mode to avoid.

## 8. `CHANGELOG.md` scaffold

```markdown
# Changelog

This project follows [Common Changelog](https://common-changelog.org/).

## [vX.Y.0] - YYYY-MM-DD <!-- replace: real tag, date from `git log -1 --format=%cs <tag>` -->

### Changed

- **Breaking:** <observable behavior change, e.g. "require Gradle 8.x or later"> <!-- ONLY if the range actually raised a floor — verify against gradle-wrapper.properties / build.gradle.kts diffs, don't assume --> ([#PR](url))
- <default/behavior change, impact-first> ([#PR](url))

### Added

- <new task, extension property, or DSL option — the reason a build-plugin user upgrades> ([#PR](url))
- Also in this release: <compressed phrase>, <compressed phrase> ([#a](url), [#b](url))

### Removed

- <only if something was actually deleted; give it the three-part breaking form too>

### Fixed

- <symptom a consumer would notice, not the internal cause> ([#PR](url))

<!-- repeat this block per real release section, oldest first or newest first — match whatever the rest of the file already does -->
```

Release body: paste the same section, add one summary sentence above it ("This catch-up covers vX.Y.0 through vX.Z.0, shipped over the last 18 months.") and a full-diff link. That's the whole release-body step — it's the same text, not a rewrite.

## 9. Breaking-change form (apply per entry, don't skip parts)

```markdown
**Breaking:** <what changed, observable behavior> ([#PR](url)). Affects <the actual
affected subset — one flag, one task, one API — not "everyone" unless it truly is>.
<One line of action, or a migration-guide link if the fix is more than a rename.>
```

If any of the six-plus releases actually announced a deprecation before removing something, the removal entry should reference that earlier release. If nothing was ever announced and something was removed anyway, say that plainly rather than writing around it — it's a real gap, not a wording problem.

## 10. Hand-off templates

```markdown
## Traceability

| Entry | Source |
|---|---|
| <entry text> | #PR |

## Excluded (N changes)

| Change | Reason |
|---|---|
| <PR title> | dev-only dependency bump, no consumer surface |
| <PR title> | below the impact cut line (§5) — folded into "Also in this release" |

## Needs a human

- <any PR whose title claims a behavior change you couldn't confirm from the diff alone>
- <any performance claim with no measurement attached>
- <the tag/no-tag decision from §7, if genuinely ambiguous>
```

## 11. Before you publish

- Every kept entry traces to a real PR or commit in the range — 100%, not "most."
- Every excluded item is listed with a reason, not dropped silently.
- No number in the file that isn't backed by a measurement in a PR.
- Every breaking entry has all three parts.
- One tense, one spec, for the whole file — don't let six releases drift between past and imperative.

## 12. To stop this happening again — recommend once

Move to a note-fragment workflow: each PR adds its own small entry file in the same patch as the code (`towncrier`/`reno`-style), collapsed into `CHANGELOG.md` at release time. Entries written 18 months later are reconstructed from memory, not from what actually shipped — that's why this backlog built up in the first place, and it will rebuild the same way if the only fix this week is the catch-up itself.