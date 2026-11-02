# Larkspur docs versioning model

## Recommendation

**Version the docs by API date only. Don't make SDK version a docs axis.**

- Full matrix: 3 API dates × every SDK version × 4 languages.
- Tutorials rewritten per cell is not maintainable for two writers. Each new SDK release would add a cell.
- The reference for each SDK version already exists on its registry, and that is the authoritative place for it.

## Why the axes differ

| Axis | What it changes | Docs treatment |
|---|---|---|
| API date | Server behavior: fields, errors, flows | Versioned docs, in the picker |
| Language | Syntax only | Sticky language tab, not a version |
| SDK version | Client surface, usually a thin wrapper over the API | Compatibility data plus registry links |

The API date is the only axis where the prose itself is true or false. SDK versions mostly change method names and types, which generated reference already covers.

## The model

### 1. API date picker (3 values)

- URL: `/docs/2024-10-15/...`. `/docs/latest/` aliases the newest date.
- The picker covers concepts, guides, tutorials, webhooks, and the API reference.
- Generate the API reference from one OpenAPI spec per date.
- Auto-generate a "what changed between dates" page from spec diffs.
- Default for visitors: `latest`. For logged-in customers, default to the date their account pins, and show a banner if it's not the newest.
- SEO: canonicalize older dates to `latest`.
- When a date is sunset, remove it from the picker. Redirect its URLs to the migration guide.

### 2. Single-source pages with version deltas

- Write each page once, with inline blocks tagged `since: 2025-06-01` or `until: 2024-10-15`.
- Fork a page into per-date copies only when the flow differs enough that a delta block would mislead.
- A new API date inherits everything from the previous date. Writers touch only the pages that changed.
- Forks stay rare, so tutorials do not become 3 copies.

### 3. Language as a tab, with CI-tested samples

- Samples exist per (language × API date): 4 × 3 = 12 combinations.
- Run them in CI against a sandbox, so version drift gets caught by tests instead of by customers.
- Each sample shows the minimum SDK version it needs, for example "Requires Python SDK ≥ 3.0".

### 4. SDK versions: a compatibility widget, not pages

Build one "Your combination" lookup. The customer picks an SDK, an SDK version, and an API date. It returns:

- Whether the combination is supported, and the SDK's default API date.
- Whether the SDK version sends the date header automatically, or the customer must set it.
- A link to the exact-version reference on the registry.
- Changelog and migration entries between their SDK version and the current one.

For Python 3.2 on 2024-10-15, this shows their real combination without a rewritten tutorial. Generate the data from SDK release metadata in CI. Don't maintain it by hand.

SDK rules:

- Patch and minor releases never change the docs.
- Only SDK majors get an "Upgrading SDK vN → vN+1" guide.
- Docs samples target the latest minor of the current major.
- Name the oldest supported SDK per language, and state that publicly.

### 5. What "tutorials rewritten for that pair" becomes

The customer gets the tutorial for their API date in their language, with version-tagged callouts and the compatibility widget beside it. If product needs a literal per-pair tutorial, scope it to API date × language (12), and only for the 2–3 top flows. Wait for usage data first.

## Workload for two writers

- Per new API date: review the spec diff, add delta blocks, fork only the pages that truly diverge, re-run the sample tests. That is days of work, not weeks.
- Per SDK release: no writer work. The widget updates from metadata.
- One-time build: delta-block tagging, spec-per-date reference generation, sample CI, and the widget. This needs engineering time.

## What to tell product

- "Every API date × every SDK version" would mean hundreds of hand-maintained cells, and it grows with every SDK release.
- This model gives each customer an accurate view of their combination. The prose stays version-correct on the one axis where it matters, and the SDK axis is handled by data.
- Revisit the model only if analytics show a large cohort stuck on an old SDK major whose tutorial needs differ materially.

## Questions to resolve before building

1. Does each SDK version pin a default API date, or does the customer always set the header? This decides the widget's logic.
2. How many releases per SDK are still supported, and does any SDK major change the call shape a tutorial teaches?
3. Which date-to-date changes are flow-level (needing forks) and which are field-level (needing only deltas)? Diff the three specs to find out.
4. What does docs traffic look like by version? Use it to decide whether any pair-level tutorial is worth writing.
5. What is the sunset policy for API dates, and how much notice do customers get? The picker lifecycle follows it.