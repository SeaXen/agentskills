# Next 16 performance hardening + route migration notes

Validated on TradingX during a post-audit optimization pass.

## What was worth doing immediately

- Add `images.remotePatterns` and modern formats (`avif`, `webp`) in `next.config.mjs`.
- Replace remote CoinGecko `<img>` usage with `next/image` where the image is part of normal app rendering.
- Remove globally eager third-party scripts from `app/layout.tsx`.
- Lazy-load heavy widgets only when near viewport.
- Add short `revalidate` windows to read-heavy public endpoints instead of leaving everything uncached.

## TradingView pattern that worked

Problem: TradingView script was loaded eagerly from root layout, so every page paid the cost.

Better pattern:
1. Keep the chart component client-side.
2. Use `IntersectionObserver` with a generous root margin (for example `240px`) to mark the container visible just before scroll arrival.
3. Inject the vendor script only once via a stable DOM marker like `script[data-tradingview-tv="1"]`.
4. If the vendor script load fails, fall back to iframe/embed mode instead of leaving a broken surface.

Why this matters: it shifts the cost from whole-app startup to the single chart surface that needs it.

## Next 16 build failures that surfaced only after full build

### 1. Invalid `dynamic` re-export from route file

Bad:
```ts
export { POST, dynamic } from "../signals/in/route";
```

Good:
```ts
export const dynamic = "force-dynamic";
export { POST, GET } from "../signals/in/route";
```

Route segment config must be statically analyzable in the route file itself.

### 2. Dynamic params context must be awaited

Older route handlers used:
```ts
type Ctx = { params: { id: string } };
```

For Next 16 App Router handlers, move to:
```ts
type Ctx = { params: Promise<{ id: string }> };

export async function GET(_req: Request, { params }: Ctx) {
  const { id } = await params;
}
```

Apply the same change to wrapped POST/PATCH/DELETE handlers too.

## middleware → proxy migration (Next 16)

`middleware.ts` is deprecated. The fix is a file rename plus a function rename, not a cosmetic export alias.

Steps that work cleanly:
1. Create `proxy.ts` at the same project root location.
2. Rename the exported function from `middleware` to `proxy`. The function signature is identical.
3. Keep `export const config = { matcher: [...] };` as-is — Next still reads `config` from `proxy.ts`.
4. Delete `middleware.ts`. Do not leave both files.

After migration, `next build` output shows `Proxy (Middleware)` in the route list. The deprecation warning disappears.

**Anti-pattern that does NOT silence the warning:**
```ts
// still in middleware.ts
export { middleware as proxy };
```
This adds the alias but Next still detects the legacy file. The warning persists until the file itself is renamed.

## Turbopack NFT "unexpected file in NFT list" warning

Symptom: build prints
```
Turbopack build encountered 1 warnings:
./next.config.mjs
Encountered unexpected file in NFT list
...
Import trace:
  App Route:
    ./next.config.mjs
    ./lib/crypto/metrics-db.ts
    ./app/api/metrics/route.ts
```

The trace looks like it blames `next.config.mjs` itself, but the real cause is a transitive Node-only module that does dynamic filesystem work at **module load time**, which the NFT tracer follows into the whole project tree.

Two-part fix:

1. **Add native packages to `serverExternalPackages`** in `next.config.mjs` so Turbopack does not try to bundle/trace them:
   ```js
   const nextConfig = {
     serverExternalPackages: ["better-sqlite3"],
     // ...
   };
   ```

2. **Make filesystem ops lazy** in the modules listed in the trace. Top-level `process.cwd()` + `fs.mkdirSync()` is the worst offender. Move it into the function that needs it, and add `/* turbopackIgnore: true */` comments around the dynamic args:
   ```ts
   // bad — runs at import time, NFT follows the entire project tree
   const DATA_DIR = path.join(process.cwd(), "data");
   fs.mkdirSync(DATA_DIR, { recursive: true });

   // good — runs only when db() is first called
   function resolveDbPath(): string {
     const dataDir = path.join(/* turbopackIgnore: true */ process.cwd(), "data");
     fs.mkdirSync(dataDir, { recursive: true });
     return path.join(dataDir, "tradingx.db");
   }
   ```

   Same pattern for `existsSync`/`statSync` over a list of candidate paths:
   ```ts
   for (const p of [process.env.DB_PATH, "/app/data/tradingx.db", "./data/tradingx.db"]) {
     if (p && existsSync(/* turbopackIgnore: true */ p)) {
       dbSize = statSync(/* turbopackIgnore: true */ p).size;
       break;
     }
   }
   ```

After both changes the warning disappears completely. Build output: `✓ Compiled successfully` with zero warnings.

## Bundle analyzer setup (Turbopack vs webpack mode)

`@next/bundle-analyzer` does NOT produce reports under the default Turbopack build. The analyzer plugin only hooks into the webpack pipeline.

Working setup:
```js
// next.config.mjs
import bundleAnalyzer from "@next/bundle-analyzer";
const withBundleAnalyzer = bundleAnalyzer({ enabled: process.env.ANALYZE === "true" });
// ...
export default withBundleAnalyzer(nextConfig);
```

```json
// package.json
"scripts": {
  "analyze": "ANALYZE=true next build --webpack"
}
```

Note the explicit `--webpack` flag. Without it, `npm run analyze` runs a normal Turbopack build and produces nothing. With it, reports land in `.next/analyze/{client,nodejs,edge}.html`.

## React hydration mismatch (#418, #423, #425) from localStorage during render

Symptom: Playwright smoke test logs three classes of minified React error on the root page:
- `Minified React error #418` (text content did not match)
- `Minified React error #423` (server-rendered HTML did not match the client tree)
- `Minified React error #425` (similar — hydration text/structure mismatch)

The build is green. `next start` serves the page. Errors only show up at runtime in the browser console.

Root cause pattern: a client component reads `localStorage` synchronously and uses the result during the **first** render. SSR uses the default value; the client's first render uses the stored value; React diffs them and throws.

Two places this typically lives:
1. **App chrome** that decides layout (sidebar vs topbar, collapsed vs expanded) from stored prefs.
2. **Demo/showcase widgets** that gate sample data on a `showDemoData` setting.

Fix pattern: the `useSettings()`-style hook already exposes a `hydrated` boolean. Gate every persisted-value branch behind it:

```tsx
const { settings, hydrated } = useSettings();
// Render the SAFE/default branch until hydrated. Match what SSR produced.
const sidebarMode = hydrated ? settings.layoutMode === "sidebar" : false;
const showDemo = hydrated ? settings.showDemoData : false;
```

Then thread the gated value through every JSX branch that used to read `settings.X` directly. A single missed reference is enough to keep the mismatch firing.

This is invisible in dev unless you look at the browser console. Production build hides the message text but the error number is the same. Smoke tests that capture `console.error` and `pageerror` events catch this class of bug reliably.

## Playwright smoke test pattern (catches what unit tests miss)

The TradingX session validated a thin Playwright config that catches console errors across critical routes without per-page assertions.

`playwright.config.ts`:
```ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: false,
  workers: 1,
  timeout: 30_000,
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || "http://localhost:8799",
    trace: "retain-on-failure",
    extraHTTPHeaders: process.env.AUTH_TOKEN
      ? { "X-Auth-Token": process.env.AUTH_TOKEN }
      : {},
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
});
```

`e2e/smoke.spec.ts`:
```ts
const PAGES = [
  { path: "/",          heading: /Dashboard|TradingX/ },
  { path: "/discover",  heading: "Discover" },
  { path: "/trade",     heading: "Trade Ticket" },
  // ...
];

for (const p of PAGES) {
  test(`smoke: ${p.path} renders without console errors`, async ({ page }) => {
    const errors: string[] = [];
    page.on("pageerror", (err) => errors.push(err.message));
    page.on("console", (msg) => { if (msg.type() === "error") errors.push(msg.text()); });

    const res = await page.goto(p.path, { waitUntil: "domcontentloaded" });
    expect(res?.status()).toBe(200);
    await expect(page.locator("body")).toContainText(p.heading);

    // Filter expected noise (no live keys, no upstream stream)
    const fatal = errors.filter((e) =>
      !/WebSocket|stream|favicon|net::ERR_|TradingView|fetch.*market/i.test(e),
    );
    expect(fatal).toEqual([]);
  });
}
```

Why this works:
- Hits real routes against a real server, so SSR/hydration bugs are caught.
- The console-error capture is what surfaces React #418/#423/#425.
- The noise filter is honest — domain-specific upstream failures (no live exchange keys) get whitelisted explicitly, real bugs do not.
- Runs in seconds against a running container; no `next dev` required.

`package.json` wire-up:
```json
"scripts": {
  "e2e": "playwright test",
  "e2e:install": "playwright install chromium"
}
```

Run order: build → deploy → `npm run e2e`. Do not run against `next dev`; dev mode's React strict-mode double-rendering can produce false positives.

## Verification lesson

A performance pass is not complete after the UI-level fixes. Re-run the full chain:
- `npm test`
- `npm run typecheck`
- `npm run build`
- `npm run e2e` (if Playwright is set up)

In this session, tests/typecheck stayed green while the build first failed on Next 16 route compatibility, then succeeded with the deprecation warning, then succeeded clean after the proxy.ts migration and NFT fix, and finally E2E exposed hidden hydration mismatches. Each step revealed work the previous step had hidden.

## Communication lesson (re-stated, this is the durable rule)

When the user says "fix all and make it 10/10":
1. Do the measurable wins.
2. Verify them.
3. State plainly what remains structural.
4. **Do not claim literal 10/10.** The user will push back, and the trust cost of an inflated claim is higher than the cost of a sober scorecard.

If the user asks "so my app is 10/10?" after a wave, treat it as a test, not a compliment. Run a real audit and report it honestly. See the SKILL.md body "Honest self-rating (mandatory)" section.
