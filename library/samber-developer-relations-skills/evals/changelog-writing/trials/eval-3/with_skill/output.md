**Version conflict — fix before shipping.** Keep a Changelog ties categories to SemVer: `Removed` entries require a **major** bump, never minor. You have two removals (`--legacy-auth` flag, XML export endpoint). Shipping these as 2.5.0 breaks that contract for anyone who trusts version ranges. Pick one:

1. Retag as **3.0.0**, or
2. Confirm both removals were pre-announced as deprecated in an earlier release — if so, link that entry here — but the removal release itself still needs a major bump regardless.

I wrote the notes below as if you'll resolve this; swap `2.5.0` for the real number you settle on.

Two more gaps I can't fill without guessing:
- **The two bug fixes** — no description given. Filled with placeholders below. "Various bug fixes" is the one thing this skill explicitly forbids (it hides exactly what a reader needs).
- **XML export replacement** — removing an endpoint outright needs a stated alternative or migration link. Placeholder below.

---

```markdown
## [2.5.0] - 2026-09-19

### Removed

- **Breaking:** Remove the `--legacy-auth` CLI flag. Telemetry shows no
  callers over the past year; any script or CI job still passing this flag
  must drop it.
- **Breaking:** Remove the XML export endpoint. Integrations requesting XML
  output must switch to `<replacement format>`. See `<migration guide link>`.

### Added

- Add `--format=ndjson` to the CLI for newline-delimited JSON output.

### Fixed

- `<one-line description of fix #1>`
- `<one-line description of fix #2>`
```

**Traceability.** Source is your spoken summary, not a diff or PR list — I have no repo access here, so this is unverified against actual commits. Confirm each line still matches what merged before you paste it in.

**Exclusion list.** None — I only have the five items you listed, no fuller commit range to mine for extra changes.

**Open items for you:**
1. Version number: 2.5.0 or 3.0.0?
2. One line each for the two bug fixes (what broke, for whom).
3. What replaces XML export — or a migration guide link.
4. Was `--legacy-auth` ever formally marked deprecated in a past release? If yes, link it; if no, this removal skipped that step, might be worth a heads-up to whoever's still relying on it before it lands.