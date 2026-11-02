## Voice call before the draft

Two of the skill's own gating questions come out against full editorial whimsy here: your readers are integrating against Wexley, not casually receiving it, and the notes go into 7 locales, where "no idioms, no wordplay" is the standing rule (wordplay doesn't survive translation and just adds defect risk). So I split it the way the skill's surface split already allows: **`CHANGELOG.md` stays terse and mechanical** — that's the file people diff and the file that gets translated verbatim — and **the personality lives in the release-body summary and sign-off**, the one place the skill says prose is allowed to earn its space. Haiku's English-only by design; translate it loosely or drop it per locale rather than transliterating the syllable count.

Format: Common Changelog (SDK/library, readers diff versions — matches your audience). Tier: 3 (noticeable to integrators who batch-process, no required action) → earns changelog + release body, which is what's below. Mode: working from your description, not a diff — flagged wherever that weakens a claim.

---

## 1. The notes

### `CHANGELOG.md`

```markdown
## [X.Y.0] - YYYY-MM-DD

### Changed

- Speed up CSV parsing for large reconciliation files (#___)

### Added

- Add batch mode to `reconcile()` — pass a list of transactions in one call
  instead of invoking it once per record (#___)

### Fixed

- Fix <symptom>, affecting <subset> (#___)
- Fix <symptom>, affecting <subset> (#___)
```

### Release body (git host)

```markdown
> Two ledgers argue,
> one stray cent finally yields —
> the books fall silent.

Wexley reconciled three things this release: a batch of transactions, a stack
of CSVs, and its own conscience. `reconcile()` now accepts a list instead of
one record at a time, large CSV imports parse faster, and two known issues
are fixed. Nothing here breaks your integration.

### Added

- Batch mode for `reconcile()` — pass a list of transactions in one call
  instead of invoking it once per record (#___)

### Changed

- Faster CSV parsing on large reconciliation files (#___)

### Fixed

- <symptom>, affecting <subset> (#___)
- <symptom>, affecting <subset> (#___)

**Full changelog**: vPREV...vX.Y.0

—

Balanced to the last cent. — Wexley
```

The "Balanced to the last cent. — Wexley" sign-off is the running bit — reuse it verbatim (or a same-shaped variant: "Every row accounted for," "No stray cents this time") every release. It's cheap to localize because it's a name + one short line, not a joke that needs to land.

## 2. Traceability table

| Entry | Source |
|---|---|
| Add batch mode to `reconcile()` | User-reported, 2026-09-18 conversation — not diff-verified |
| Speed up CSV parsing | User-reported, 2026-09-18 conversation — not diff-verified |
| Fix #1 (bug fix, unspecified) | User-reported, 2026-09-18 conversation — no symptom given |
| Fix #2 (bug fix, unspecified) | User-reported, 2026-09-18 conversation — no symptom given |

## 3. Exclusion list

None. Everything you described (batch reconcile, CSV parsing speedup, two bug fixes) appears above — nothing was dropped.

## 4. Open items for a human

- **Version number and release date.** Common Changelog has no `[Unreleased]` slot — `X.Y.0` needs the real number before this ships. No breaking entries here, so this reads as a minor bump; flag me if either bug fix actually changes behavior someone was relying on.
- **PR/commit links.** Every `(#___)` is a placeholder. Common Changelog requires them — fill in before publishing.
- **The two bug fixes have no content.** I don't have the symptom or affected subset for either, and I'm not going to invent behavior for a payment-reconciliation SDK's release notes. Give me one sentence each ("what broke, who hit it") and I'll drop them straight into the `<symptom>` slots.
- **CSV parsing number.** Left unquantified — if you have a real benchmark, give me the number and I'll add it; otherwise it stays qualitative per the no-unsourced-numbers rule.
- **Confirm `reconcile()` batch mode doesn't touch the existing single-record call.** I assumed purely additive. Worth a second look before ruling out a Breaking entry, given the audience.
- **Confirm Common Changelog is the right pick** — if Wexley already ships `CHANGELOG.md` under Keep a Changelog, keep that format rather than switching mid-project.
- **Localization pass.** Bullets translate as-is. The haiku and sign-off are the one place I'd hand to a native speaker per locale rather than machine-translate — especially into Japanese, where the haiku form is a much higher bar than in English.