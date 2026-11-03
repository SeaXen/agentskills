# ESLint installation + SQLite migration pitfalls

Two concrete traps that bite when finishing a Next.js feature wave on an
existing app. Both observed in TradingX (Wave B/C).

## 1. ESLint config: don't reference plugins you haven't installed

When the `next build` output nags

> ESLint must be installed in order to run during builds: `npm install --save-dev eslint`

the obvious fix is:

```bash
npm install --save-dev eslint@8 eslint-config-next@<your-next-version>
```

Pin the major to match Next (e.g. `eslint-config-next@14.2.35` for Next 14.2.x).
`next/core-web-vitals` is provided by `eslint-config-next`. Good.

But the next surprise is a wall of:

> Error: Definition for rule '@typescript-eslint/no-unused-vars' was not found.

That rule lives in `@typescript-eslint/eslint-plugin`, which is NOT bundled
with `eslint-config-next`. Two safe options:

**A. Drop the rule from `.eslintrc.json` (preferred for app code):**

```json
{
  "extends": ["next/core-web-vitals"],
  "rules": {
    "react/no-unescaped-entities": "off",
    "react-hooks/exhaustive-deps": "warn",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}
```

Why:
- `react/no-unescaped-entities` is pure noise on every JSX `"` or `'` literal
  — disable it project-wide.
- `react-hooks/exhaustive-deps` as `warn` (not `error`) — intentional non-
  exhaustive deps are common in real apps (mount-only effects, debounced
  effects) and shouldn't break the build.
- `@typescript-eslint/*` rules — drop them unless you also install the plugin.

**B. If you really want typed unused-vars checking:**

```bash
npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

Then add `"plugins": ["@typescript-eslint"]` and `"parser": "@typescript-eslint/parser"`.
Most apps don't need this — `tsc --noEmit` already catches the dangerous cases.

Verify with `npx next lint` — should report only warnings, zero errors. The
build's ESLint nag is then satisfied without changing any product code.

## 2. SQLite `ALTER TABLE ADD COLUMN` races during `next build`

Symptom during `npm run build` collect-page-data phase:

```
SqliteError: duplicate column name: expected_price
    at /app/.next/server/chunks/139.js:...
Error: Failed to collect page data for /api/dca
```

Cause: Next.js spawns multiple route workers in parallel during page-data
collection. Each one imports `lib/db.ts` which calls `migrate()`, which does:

```ts
if (!hasColumn("trades", "expected_price")) {
  d.exec("ALTER TABLE trades ADD COLUMN expected_price REAL;");  // races
}
```

Two workers both see the column missing via PRAGMA, both try to ALTER, one
wins and the second crashes the build. SQLite has no `ADD COLUMN IF NOT EXISTS`.

Fix: idempotent ALTER helper that catches the duplicate-column error:

```ts
const addColIfMissing = (table: string, col: string, ddl: string) => {
  if (hasCol(table, col)) return;
  try {
    d.exec(ddl);
  } catch (e: any) {
    const msg = String(e?.message ?? e);
    if (!/duplicate column name/i.test(msg)) throw e;
  }
};

addColIfMissing("trades", "expected_price", `ALTER TABLE trades ADD COLUMN expected_price REAL;`);
addColIfMissing("trades", "slippage_bps",   `ALTER TABLE trades ADD COLUMN slippage_bps REAL;`);
d.exec(`CREATE INDEX IF NOT EXISTS idx_trades_slippage ON trades(slippage_bps);`);
```

`CREATE INDEX IF NOT EXISTS` and `CREATE TABLE IF NOT EXISTS` are already
safe — only `ALTER TABLE ADD COLUMN` needs the helper.

This is the root cause; do NOT "fix" by running build with single concurrency
or running migrations once externally. The helper is the right shape because
production also imports `db.ts` from multiple route handlers concurrently.

## 3. Docker `compose down` leaves the container when it was created outside compose

If a container was started with `docker run` or recreated by a previous tool
in a different way, `docker compose down` may report

> Warning: No resource found to remove for project "tradingx"

…and then `docker compose up -d` fails with

> Conflict. The container name "/tradingx" is already in use

Fix: `docker rm -f <name>` before `docker compose up -d` when the previous
run was non-compose. Don't waste a turn diagnosing — just remove and recreate.
