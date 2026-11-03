# Pitfalls — Fullstack Feature Build

Concrete pitfalls hit during the TradingX 8-feature build, with the actual error messages and how to avoid them.

## 1. JSX patch breakage (the worst one)

**Symptom:** Layered `patch` calls on a JSX file leave dangling `<div>`, `<p>`, or other tags that don't close. Build fails with errors like:

```
ERROR [170:12] Type '"" | { error: string; } | null' is not assignable to type 'ReactNode'.
ERROR [174:8] Cannot find name 'showForm'.
ERROR [176:11] JSX expressions must have one parent element.
```

**Root cause:** When the `old_string` for a `patch` matches a multi-line JSX block, and the surrounding context is large, the patch can land in a slightly different position than intended. Subsequent patches then miss the actual context, leaving the file in a half-applied state.

**How to avoid:**

- After every JSX `patch`, run `npx tsc --noEmit` to verify the file still type-checks.
- If you find yourself doing 3+ `patch` calls on the same file, **stop patching and rewrite the whole file with `write_file`**. Re-read the file first, then write the new version in one shot.
- Keep `old_string` snippets short and unique. Include a few surrounding lines for context, but don't try to match 50-line blocks.
- When a patch fails (returns nothing matched), DON'T try to "fix it" with another patch on the same file — re-read and rewrite.

**Real cost:** 2 wasted patch rounds on `app/exchanges/page.tsx` because I tried to add a button via patch and it landed wrong, then tried to fix the resulting dangling tags via another patch, which made it worse. The fix was to read the full file (360 lines) and rewrite it from scratch with `write_file`. Lesson: 2 minutes of rewrite > 10 minutes of patch-on-patch.

## 2. File-naming collisions

**Symptom:** Create a new file like `lib/filter-presets.ts`, only to find out later that `lib/filterPresets.ts` already exists and is imported elsewhere.

**Root cause:** Skipped the survey step. Went straight to creating files based on conventional naming.

**How to avoid:**

```bash
# Before creating any new lib file:
ls lib/
ls lib/crypto/
```

Specifically, check:
- Kebab-case vs camelCase vs PascalCase — match what's there
- Plural vs singular (`utils` vs `util`, `helpers` vs `helper`)
- Whether the concept already exists with a different name

**Real cost:** Created `lib/filter-presets.ts` with my own `useFilterPresets()` interface, then realized the existing `lib/filterPresets.ts` (camelCase) already had a similar function. Had to delete mine and adapt my new component to the existing API. ~5 minutes wasted.

## 3. Docker terminal blocking

**Symptom:** `docker compose up -d --force-recreate` gets blocked by the terminal tool:

```
BLOCKED: This foreground command appears to start a long-lived server/watch process.
Run it with background=true, verify readiness (health endpoint/log signal), then execute tests in a separate command.
```

**Root cause:** The terminal tool's heuristic flags `docker compose up` as long-running even with `-d`.

**How to avoid:** Use `background=true` and `process(action='wait')`:

```python
terminal(background=true, command="cd /path && docker compose build --no-cache X && docker compose up -d --force-recreate && sleep 4 && echo READY", notify_on_complete=True)
# then
process(action="wait", session_id="...", timeout=180)
```

Or for verification after deploy, use a separate foreground `curl` call.

## 4. Next.js route file rules

**Symptom:** Build fails with:

```
app/api/news/route.ts
Type error: Route "app/api/news/route.ts" does not match the required types of a Next.js Route.
  "getNews" is not a valid Route export field.
```

**Root cause:** Exported a helper function (e.g. `getNews`, `computeRatios`) from `app/api/X/route.ts`. Next.js only allows the specific HTTP method exports.

**How to avoid:**

- All helpers live in `lib/crypto/X.ts` (or wherever the project's lib is)
- The `route.ts` only has `GET`, `POST`, `PUT`, `DELETE`, `PATCH` exports
- Import helpers from `/lib` and call them inside the route handler

```typescript
// lib/crypto/news.ts
export async function getNews(): Promise<NewsItem[]> { ... }
export const FEED_SOURCES = [...];

// app/api/news/route.ts
import { getNews, FEED_SOURCES } from "@/lib/crypto/news";
export async function GET(req: Request) { ... }
```

## 5. LSP diagnostics vs tsc

**Symptom:** LSP shows errors like `ERROR [176:11] JSX expressions must have one parent element` but `tsc --noEmit` passes clean.

**Root cause:** The LSP server caches file state and may show errors from intermediate states that have since been fixed.

**How to avoid:** Trust `npx tsc --noEmit` over LSP. Run tsc after every batch of file changes, and if tsc is clean, the file is clean.

## 6. Pre-existing type errors

**Symptom:** `tsc` reports an error in a file you didn't touch:

```
lib/crypto/db.ts(599,41): error TS18048: 'opts.exchangeIds' is possibly 'undefined'.
```

**Root cause:** Pre-existing strict-null-check from a prior session.

**How to avoid:**

- Don't refactor the file to fix it (out of scope, risks breaking other things)
- Use the minimal fix: `opts.exchangeIds![i]` (non-null assertion) if the type guard above already validates the check
- OR add a one-line guard

**Why minimal:** The build is currently green for the user — they don't care about this specific strictness. Fix the symptom, not the cause. Don't reformat a working file just because tsc is whiny.

## 7. Build vs dynamic vs client functions

**Symptom:** Server-side code (DB calls, secrets) accidentally runs in the browser, OR a page with `useEffect` breaks SSR.

**How to avoid:**

- Any page that uses `useState`, `useEffect`, event handlers → `"use client"` at top
- Any API route that touches DB → default (no `"use server"`)
- Any lib that does server-only work (env vars, fs, child_process) → NEVER imported into a client component
- If you have a server util that needs to be shared with a client, split it: `lib/server/X.ts` and `lib/client/X.ts`

## 8. Stale `.next/` types after adding new routes

**Symptom:** `tsc` shows errors like:

```
.next/types/app/api/coingecko/route.ts(2,24): error TS2307: Cannot find module '../../../../../app/api/coingecko/route.js'
```

**Root cause:** Next.js pre-generates type files for routes. After adding a new route, the old `.next/types/` may have stale references.

**How to avoid:** `rm -rf .next/types` before running `tsc --noEmit` after adding new routes. Or run `npm run build` first to regenerate.

## 9. Patch tool quote-escaping bug

**Symptom:** After using `patch` to edit a TypeScript/JSX file, the file contains literal `\"` backslash-escaped quotes instead of plain `"` quotes. The LSP shows errors like `ERROR [162:20] Invalid character` and `Unexpected token`.

**Example:** You patch `["dark", "light"]` → `["dark", "light", "waves"]`, but the file ends up with `[\"dark\", \"light\", \"waves\"]`.

**Root cause:** The `patch` tool can introduce backslash-escaped quotes when `old_string` or `new_string` contains double quotes, especially in JSX/TSX context where the tool's diff display shows escaped quotes.

**How to avoid:**
- Check the file with `read_file` immediately after patching — the backslashes will be visible
- Fix with `sed`: `sed -i 's/\\"/"/g' app/settings/page.tsx`
- Or avoid the issue: for files with heavy quote content (arrays of strings, JSX className strings), use `write_file` to rewrite the entire file instead of `patch`

**Real cost:** Hit this when adding the "waves" theme variant to `app/settings/page.tsx`. The `["dark", "light", "system", "waves"]` array got escaped to `[\"dark\", \"light\", ...]`. LSP showed 2 errors. Fixed with sed. ~3 minutes wasted.

## 10. Terminal output secret-redaction mimics file corruption

**Symptom:** A grep/read of a test file shows what looks like garbage where `Bearer ${TOKEN}` should be:

```
headers: { Authorization: *** ${AUTH_TOKEN}` },
```

`tsc` then explodes with cascading parse errors (`TS1109 Expression expected`, `TS1160 Unterminated template literal`) across dozens of lines.

**Root cause:** The Hermes terminal layer redacts the literal string `Bearer ` followed by a token-like value to `***` in tool output. The on-disk file is fine. The redaction only happens in the displayed stdout — the file itself still contains `Bearer ${AUTH_TOKEN}`.

**How to confirm:** Read the same lines with `read_file` (not terminal). If they show `Bearer ${AUTH_TOKEN}` correctly, the file is intact and the `***` was display-only redaction. Compile errors in this case come from a different real cause.

**How to avoid:**
- Don't chase phantom corruption when terminal output shows `***`. Cross-check with `read_file` before patching.
- If you do attempt to "fix" it by rewriting, the literal `Bearer ` in your new_string can be redacted in tool transcripts too — making the diff display misleading. Verify with `read_file`, not the patch diff preview.
- Real cause of the TS errors in the original incident: a separate Python rewrite injected actual `*** ${TOKEN}` text into the file because the agent was reacting to the redacted display. The fix was to write `Bearer ${TOKEN}` back via a script that wasn't confused by display redaction.

**Real cost:** ~10 minutes burned chasing "file corruption" that didn't exist on disk, plus one extra patch round that actually broke the file by writing the redacted form back.

## 11. System verification reminders after large edits

**Symptom:** After a large batch of edits (8+ files changed), the system sends a verification reminder: "The workspace does not have fresh passing verification evidence yet."

**Root cause:** The verification system tracks the last command run and compares it against the set of changed files. If you ran verification before the final edits, the evidence is stale.

**How to avoid:**
- After the LAST edit in a batch, always run the full verification chain: `tsc --noEmit && npm test && npm run build`
- If the system sends a reminder, just re-run `npx tsc --noEmit` and `npm test` — these are fast (<2 min) and produce fresh evidence
- Don't argue with the reminder — run the commands, report the results, done

**Key:** The verification reminder is NOT an accusation of failure — it's a freshness check. Run the commands and report the numbers.

## 12. SQLite ALTER TABLE race during `next build` page-data collection

**Symptom:** `npm run build` compiles cleanly but crashes during "Collecting page data" with:

```
SqliteError: duplicate column name: expected_price
    at Database.exec (.../better-sqlite3/lib/methods/wrappers.js:9:14)
    at migrate (.../lib/crypto/db.ts:418:295)
    ...
Error: Failed to collect page data for /api/dca
```

**Root cause:** Next.js runs multiple API route workers in parallel during page-data collection. Each worker calls `db()` → `migrate()`. The classic `if (!hasCol(...)) d.exec('ALTER TABLE ...')` pattern races: both workers read the pragma and see "column missing", both attempt the ALTER, the loser throws `SQLITE_ERROR: duplicate column name`. SQLite has no `ADD COLUMN IF NOT EXISTS`.

**How to avoid:** Idempotent helper that swallows only the duplicate-column error:

```ts
// In migrate() after the hasCol definition:
const addColIfMissing = (table: string, col: string, ddl: string) => {
  if (hasCol(table, col)) return;
  try {
    d.exec(ddl);
  } catch (e: any) {
    const msg = String(e?.message ?? e);
    if (!/duplicate column name/i.test(msg)) throw e;
  }
};

// Use it for ALTERs:
addColIfMissing("trades", "expected_price", `ALTER TABLE trades ADD COLUMN expected_price REAL;`);
addColIfMissing("trades", "slippage_bps", `ALTER TABLE trades ADD COLUMN slippage_bps REAL;`);
// CREATE INDEX IF NOT EXISTS is already idempotent — leave outside the helper
d.exec(`CREATE INDEX IF NOT EXISTS idx_trades_slippage ON trades(slippage_bps);`);
```

**Why the pattern works:** The pragma check eliminates the common case (column already exists from a prior run). The try/catch eliminates the race case (both workers past the pragma, one wins the ALTER, loser swallows the duplicate error). Non-duplicate errors (syntax, constraint violations) still throw.

**When it fires:** Only during `next build` page-data collection, not at runtime in production. But it still blocks the build, so fix it.

**Real cost (this session):** Build passed → added slippage columns → build failed with duplicate column error → 5 minutes to diagnose the root cause (parallel workers) → 2 minutes to write the helper → build passed. Total: 7 minutes. Without the fix, every `npm run build` would fail unpredictably (~50% of the time).
