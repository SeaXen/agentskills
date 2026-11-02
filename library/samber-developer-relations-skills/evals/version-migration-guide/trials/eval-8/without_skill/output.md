# Candlewick v7: breaking changes

## Client.fetch() no longer accepts a callback

`Client.fetch()` is now promise-only. The callback overload is removed. Passing a callback as the second argument throws:

```
TypeError: fetch() no longer accepts a callback; await the returned promise.
```

**Who is affected:** anyone calling `fetch(url, callback)`.

**Before**
```ts
client.fetch(url, (err, res) => {
  if (err) return handle(err);
  use(res);
});
```

**After**
```ts
try {
  const res = await client.fetch(url);
  use(res);
} catch (err) {
  handle(err);
}
```

**Migration:** replace each callback with `await` or `.then()/.catch()`. Move the error branch into `catch`. Search for the `TypeError` message above to find call sites you missed.

## Configuration moved from `.cwickrc` to `cwick.config.ts`

Configuration now lives in `cwick.config.ts`. These settings move with it:

- `cwick.plugins`
- `cwick.retries`
- `cwick.baseUrl`
- `cwick.logLevel`

The values and their meanings are unchanged. Only the location changed.

**Who is affected:** anyone with a `.cwickrc` file.

**Before** (`.cwickrc`)
```json
{
  "plugins": ["./my-plugin"],
  "retries": 3,
  "baseUrl": "https://api.example.com",
  "logLevel": "info"
}
```

**After** (`cwick.config.ts`)
```ts
export default {
  plugins: ["./my-plugin"],
  retries: 3,
  baseUrl: "https://api.example.com",
  logLevel: "info",
};
```

**Migration:**
1. Create `cwick.config.ts` at the project root.
2. Copy each value across as-is.
3. Delete `.cwickrc`.

## Client.close() now rejects on shutdown errors

`Client.close()` used to swallow errors raised during shutdown. It now rejects with the underlying error.

**Who is affected:** anyone who calls `close()` without handling rejections. An error that was silently ignored now surfaces as an unhandled rejection, or as a failed `await`.

**Before**
```ts
await client.close(); // shutdown errors were swallowed
```

**After (recommended):** handle the error.
```ts
try {
  await client.close();
} catch (err) {
  log.error("cwick shutdown failed", err);
}
```

**After (old behaviour):** set `closeTolerant: true`.
```ts
await client.close({ closeTolerant: true });
```

**Migration:** wrap `close()` in `try/catch`, or opt back into the old behaviour with `closeTolerant: true`. Check teardown paths first (`finally` blocks, test `afterEach` hooks, process exit handlers), because they most often call `close()` without handling errors.

## Open points to confirm before publishing

- **`closeTolerant` placement:** I assumed it is a `close()` argument. If it is a `Client` constructor or config option, fix the example.
- **`cwick.config.ts` shape:** I assumed a plain default export with the four keys at the top level. If you ship a `defineConfig()` helper or nest the keys under `cwick`, update the example.
- **Leftover `.cwickrc`:** the entry doesn't say what v7 does if one still exists (ignored, warning, or error). Add one line once you know.