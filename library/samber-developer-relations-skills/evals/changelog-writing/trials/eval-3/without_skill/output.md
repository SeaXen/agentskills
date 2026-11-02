Here's the CHANGELOG.md section:

```markdown
## [2.5.0] - 2026-09-19

### Added
- `--format=ndjson` output option for [command] — streams results as newline-delimited JSON.

### Removed
- **Breaking:** `--legacy-auth` CLI flag. Unused in telemetry for over a year; no replacement.
- **Breaking:** XML export endpoint. Use the JSON export endpoint instead.

### Fixed
- [Bug fix 1 — replace with a one-line description of user-visible symptom + cause]
- [Bug fix 2 — replace with a one-line description of user-visible symptom + cause]
```

Two things worth your attention before this ships:

1. **I left the two Fixed entries as placeholders** — you didn't give me the bug details, and "Fixed a bug" entries are exactly what the Keep a Changelog convention calls out as useless to readers. Fill in the actual symptom/cause (and issue/PR number if you have one).
2. **SemVer mismatch:** removing a CLI flag and deleting an endpoint entirely are both breaking changes by definition. Keep a Changelog itself is format-agnostic on versioning, but if you're following SemVer (common alongside it), this should be `3.0.0`, not a `2.5.0` minor bump — anyone pinned to `^2.x` will auto-pull this and silently break. Worth a quick gut-check with whoever owns the release before it goes out tomorrow, even though I know CI already tagged it.