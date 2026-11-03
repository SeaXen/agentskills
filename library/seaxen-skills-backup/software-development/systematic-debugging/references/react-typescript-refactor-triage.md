# React/TypeScript Refactor Triage

Use when a previously working dashboard/app breaks after splitting a large component or hook.

## Fast triage order

1. Run the build once and keep the full compiler output.
2. Group errors by contract surface:
   - extracted component props
   - shared hook return object
   - shared types/interfaces
   - stale domain field names
   - union/enum drift
3. Fix top-level contract mismatches first.
4. Rebuild after the contract pass.
5. Only then chase any remaining local errors.

## Common break patterns seen in session

### 1) Prop/callback signature drift
Examples:
- component expects `{ label, run }[]`, caller sends `{ label, execute }[]`
- component expects `(view: SavedSessionView) => void`, caller sends `(viewId: string) => void`
- component expects `handleOpenMcpLog(serverName)`, caller passes zero-arg function

### 2) Shared hook return shape drift
After extraction, pages often still expect keys that the hook no longer returns.
Examples restored in session:
- `sessionMcpTools`
- `selectedPlanSummary`
- `analyticsKpis`
- `topAnalyticsSessions`
- `mcpServers`
- `mcpServerOptions`
- `filteredMcpInventory`
- `analyticsSettings`
- `analyticsExports`
- `triggerSessionArtifactDownload`

Rule: compare every page prop against the hook return object before editing business logic.

### 3) Type/schema drift after renames
Examples:
- saved view wrote `columns` but type required `sessionColumns`
- apply handler still read `item.columns`
- refactor introduced new required fields like `searchQuery` and `densityMode`

Rule: when a type exists, trust the type and make stored-shape code match it.

### 4) Stale domain fields
Example:
- session code used `source_platform` after API type had only `source`

Rule: check the authoritative API/domain type before assuming an older field still exists.

### 5) Union drift
Example:
- `SortMode` type allowed `recent | messages | tools`
- implementation still checked `tokens | priority`

Rule: when union comparisons fail, fix the implementation to the current union first.

## Good recovery pattern

- Keep the split if the architecture is still sound.
- Repair contracts.
- Rebuild.
- Verify chunking/output.
- Continue smaller follow-up refactors only after green build.

## Why this matters

One stale interface can create 10-20 downstream compile errors. Treating them individually is noise. Fixing the contract surface collapses the error set fast.
