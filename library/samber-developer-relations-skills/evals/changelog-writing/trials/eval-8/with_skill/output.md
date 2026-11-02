# Brackenhall v0.10.0 release notes

**Mode:** No repository checkout was available for Brackenhall in this environment, so this was produced in pasted-log mode from the git log and the three PR titles you gave. Confidence is lower on the two items flagged below — hand me the diffs for #140 and #147 (or answer the two questions in "Needs a human") and I'll tighten those two entries.

**Format decision:** the project has never had a changelog, so there's no existing spec to match. Brackenhall reads as a self-hosted product (not a library readers diff programmatically), so I used **Keep a Changelog**, past tense, one version section. Worth recording this choice somewhere so future releases don't re-litigate it.

**Tier:** 3 — noticeable to some users, no action required. That earns CHANGELOG + release body; I produced both since they're the same text pasted twice.

---

## 1. The notes

### `CHANGELOG.md`

```markdown
## [0.10.0] - YYYY-MM-DD

### Added

- Added a dark theme (#143)

### Fixed

- Fixed reconnecting after a session expired (#140)
```

If this is the first entry in the file, add the standard header above it:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
```

Keep the `[Unreleased]` section going forward — it turns the next release into a rename instead of a rewrite.

### Release body (git host)

```markdown
Brackenhall 0.10.0 adds a dark theme and fixes a reconnect issue after session
expiry.

### Added

- Dark theme (#143)

### Fixed

- Reconnecting after a session expired (#140)

**Full changelog**: v0.9.0...v0.10.0
```

---

## 2. Traceability

| Entry | Source | Notes |
|---|---|---|
| Added a dark theme | #143 "Dark mode" (commits: `fix tests`, `Update README.md`) | README update folds in as documentation of this feature, not a separate entry |
| Fixed reconnecting after a session expired | #140 "Handle expired sessions on reconnect" (commits: `wip`, `more wip`, `address review`) | Wrote the effect narrowly — see open item below before this ships |

## 3. Excluded

| Change | Reason |
|---|---|
| #147 "Refactor submission handler" (commits: `final fix`, `Update handler.ts`) | Title names a refactor; no diff available to confirm it changed observable behavior. Common Changelog's own guidance is that refactors belong in notes *when they carry a side effect* — this one is excluded until that's confirmed, not because refactors are categorically dropped. |
| `wip`, `more wip`, `address review`, `fix tests`, `final fix` | Fixup/review-response commits folded into their parent PR's single entry above; carry no separate information. |

## 4. Needs a human

- **#140** — I wrote "Fixed reconnecting after a session expired" rather than inventing a symptom. If you can confirm what users actually saw before the fix (an error, a blank/stuck screen, silent data loss), I'll rewrite the entry to state that effect directly — it's what makes the difference between a reader thinking "does this affect me?" and knowing.
- **#147** — Confirm whether "Refactor submission handler" changed anything a form author or respondent could notice (validation timing, error text, submission latency). If yes, it gets a `Changed` entry; if it's purely internal, the exclusion above stands and no entry is needed.
- **Release date** — I left `YYYY-MM-DD` as a placeholder; fill in the actual ship date.
- **PR links** — entries reference `#140` etc. without full URLs since I don't have Brackenhall's actual host/org slug; swap in real links before publishing.