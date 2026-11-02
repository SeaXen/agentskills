## Candlewick v7: breaking-change entries (draft)

I ordered these by estimated blast radius, with no telemetry behind it: config move, then `close()`, then `fetch()` callbacks. Everyone loads config, most apps call `close()`, and only callback-style callers hit the `fetch()` change. Please confirm that order or give me real usage numbers.

---

### Moved: config from `.cwickrc` to `cwick.config.ts` {#moved-config-cwick-config-ts}

**Affects you if** a `.cwickrc` file exists in your project, or your code relies on `cwick.plugins`, `cwick.retries`, `cwick.baseUrl` or `cwick.logLevel` set there.
Search for `.cwickrc` (for example `find . -name .cwickrc -not -path "./node_modules/*"`).
v7 has no runtime message for this change that I know of. `[CONFIRM: does v7 warn or throw when it finds a .cwickrc?]` If it does, paste the exact text here.

v7 reads configuration only from `cwick.config.ts`. A typed config file gives editors completion and lets the compiler catch a misspelled key. The keys and values are unchanged; only their location moved.

```ts
// Before (v6): .cwickrc
{
  "cwick.plugins": ["cwick-plugin-metrics"],
  "cwick.retries": 3,
  "cwick.baseUrl": "https://api.example.com",
  "cwick.logLevel": "warn"
}
```

```ts
// After (v7): cwick.config.ts
export default {
  "cwick.plugins": ["cwick-plugin-metrics"],
  "cwick.retries": 3,
  "cwick.baseUrl": "https://api.example.com",
  "cwick.logLevel": "warn",
};
```

**Fix:**
1. Create `cwick.config.ts` at the project root, where `.cwickrc` lived.
2. Copy each of the four keys and its value across unchanged.
3. Delete `.cwickrc`.
4. Run your app and confirm the effective values are the ones you had before.

**Escape hatch:** none. v7 does not read `.cwickrc`. `[CONFIRM: v6 line support end date]`

---

### Changed: `Client.close()` rejects on shutdown errors {#changed-close-rejects}

**Affects you if** your code calls `Client.close()` and never handled a rejection from it.
Search for `\.close\(`. At runtime, a shutdown error that v6 hid now surfaces as a rejected promise. If nothing catches it, Node 15 and later terminate the process with exit code 1 and print `UnhandledPromiseRejection`. `[CONFIRM: exact error class and message close() rejects with]`

In v6, `close()` swallowed errors during shutdown, so failed shutdowns looked like clean ones. v7 rejects so you can see the failure and decide what to do. If you want the old behaviour, opt in with `closeTolerant: true`.

```ts
// Before (v6): errors during shutdown were swallowed
await client.close();

// After (v7): handle the rejection
try {
  await client.close();
} catch (err) {
  logger.error("cwick shutdown failed", err);
}
```

**Fix:**
1. Find every `close()` call, including those in `finally` blocks, signal handlers and test teardown.
2. Wrap each in `try`/`catch`, or let it propagate if the caller already handles errors.
3. Decide for each site whether a failed shutdown should be logged, retried or fatal.

**Escape hatch:** pass `closeTolerant: true` to restore the v6 behaviour of swallowing shutdown errors.

```ts
// After (v7): v6 behaviour, kept on purpose
await client.close({ closeTolerant: true });
```

`[CONFIRM: is closeTolerant a close() argument, as drawn above, or a Client constructor option or a cwick.config.ts key?]`

---

### Removed: callback argument to `Client.fetch()` {#removed-fetch-callback}

**Affects you if** you pass a function as the second argument to `Client.fetch()`.
Search for `\.fetch\([^)]*,\s*(function|\(|async|\w+\s*\))`. The pattern is a starting point and will miss callbacks passed by variable name, so also read each `.fetch(` call that has two arguments. At runtime on v7 you will see:

    TypeError: fetch() no longer accepts a callback; await the returned promise.

`fetch()` supported both callbacks and promises, and that two-mode contract made error and timing behaviour hard to reason about. v7 is promise-only, so a callback is rejected immediately with a `TypeError` rather than ignored.

```ts
// Before (v6)
client.fetch("/users/42", (err, res) => {
  if (err) return handleError(err);
  render(res);
});

// After (v7)
try {
  const res = await client.fetch("/users/42");
  render(res);
} catch (err) {
  handleError(err);
}
```

`[CONFIRM: callback is Node-style (err, res); adjust if not]`

**Fix:**
1. Delete the second argument from each `fetch()` call.
2. `await` the returned promise, or chain `.then()`.
3. Move the body of the old `err` branch into a `catch`, and the success branch into the code after the `await`.
4. Make the enclosing function `async` if it is not already.

**Escape hatch:** none. v7 `fetch()` is promise-only. `[CONFIRM: v6 line support end date]`

---

## Assumptions and open questions

- **Not provided, so not invented:** no codemod, no v7 error text for the config and `close()` changes, and no v6 support end date. I wrote no codemod command. If you have one, add it to each **Fix**. If not, the search patterns above are the detection tooling to ship.
- **`.cwickrc` format:** I assumed JSON with the `cwick.*` keys quoted as written.
- **`cwick.config.ts` shape:** I assumed a plain default export. If you ship a `defineConfig()` helper, use it in the **After** block.
- **Pairs still missing:** a staged path through a v6 warnings release would let all three entries emit warnings at each call site first. I don't know whether v6 can still ship, so I haven't picked a path shape. The guide's top should state it.
- **Cold-upgrade verification:** I haven't run these entries against a real project, so the pass threshold isn't met yet.