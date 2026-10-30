# Locale plan template

Read when writing the final deliverable. Write a full block for each `launch` or `gated` locale, and the short block for each `source hardening only` or `declined` one.

Tag every figure by type: `measured` (the user's own data), `sourced` (a named project or study), `baseline` (a starting value to replace) or `ASSUMED` (no one could confirm it).

```markdown
# Docs localization plan - <product>, <date>

## Stored context
Locales and decisions, owners, page set rule, pin field names, drift-check command, thresholds, kill rule.

## Assumptions
- <ASSUMED item> (omit when every answer came from the user)

## Decision summary
| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| <tag> | launch / gated / source hardening only / declined | <one line> | <condition> |

## Source hardening (all markets)
- Glossary owner and location: <name, file>
- Style rules adopted: <plain global English rules>
- Code marked non-translatable: <how>

## Locale: <tag> (launch or gated)
### Evidence
| Signal | Value | Type |
|---|---|---|
| Country share of sessions | | measured |
| Browser-language share, ratio to combined share of countries where the language dominates | | measured |
| Engagement gap vs source-language readers | | measured |
| Demand in the language (tickets, posts, queries) | | measured |
| Commercial weight | | measured |
Class: <barrier confirmed, owner named | demand without owner | no barrier shown>

### Candidate bundles
| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
Chosen: <bundle>, because <reason>. Deleted rungs: <rungs, reason>.

### Page set
- Pages: <list or rule>
- Steady state: <changed pages per release> × <hours per changed page> ≤ <reviewer hours per release>
- Launch load: (<pages> + <UI-string page-equivalents>) × <first-review hours> ÷ <reviewer hours per release> = <releases>
- Never translated: <classes>; glossary file: <path>

### Review model
- Human review before publication: <page classes or "every page">
- Review on page-view threshold: <threshold, or "not used - set reviewed in full">
- Label text: <text>
- Search exposure: <condition>

### Freshness contract
- Pin fields: <names>
- Drift check: <command, where it runs, `--far` value>
- Banner, fallback, retirement thresholds: <values with type tags>

### Ownership gate
| Item | Status | Closing action | Expected date |
|---|---|---|---|
Person allowed to pull the locale: <name>

### KPIs and kill rule
| KPI | Pre-launch figure | Target | Control | Type |
|---|---|---|---|---|
Kill rule: <condition> → <action>

## Locale: <tag> (source hardening only or declined)
- Evidence: <the two or three signals that decided it>
- Decision and reopen condition: <text>

## Rollout schedule
| Release or week | Milestone | Owner |
|---|---|---|
```

## Worked example (invented company, illustrative figures)

Input: an API platform, 600 pages, about 40% of docs sessions from Japan and Brazil, no localization, one Japanese-speaking engineer with 4 hours per release, no Portuguese speaker, English-only product.

Output (excerpt):

```markdown
## Decision summary
| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| ja | gated | browser-language share close to country share, quickstart completion well below English readers; one reviewer only | second fluent reviewer (contractor or hire) named |
| pt-BR | declined | most Brazilian sessions run another browser language and complete the quickstart like English readers | engagement gap opens, or Portuguese support tickets appear |

### Page set - ja
- Pages: quickstart, install, auth, 9 top task pages, site UI strings
- Steady state: ~4 changed pages per release × 0.5 h ≤ 4 h (baseline pace)
- Launch load: (12 pages + ~600 UI strings ≈ 2 page-equivalents = 14) × 1 h ÷ 4 h ≈ 4 releases (baseline pace)
- Never translated: code, CLI flags, error strings (quoted verbatim, translation alongside), API reference, changelog
```

The invented figures show the shape, not benchmarks.
