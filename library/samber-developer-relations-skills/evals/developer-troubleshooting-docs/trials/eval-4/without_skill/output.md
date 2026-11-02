# Cache upload rejected (HTTP 413)

```
tessellate: error: cache upload rejected (HTTP 413): object <uuid> exceeds the per-object limit of 512 MiB for plan 'team'
```

**Applies to:** CLI 2.1–2.8, Linux and macOS. `team` and `starter` plans. (Windows uses different caps and won't hit this. `enterprise` has no per-object limit.)

## What it means

Tessellate rejected one cache object because it's larger than your plan's per-object limit (512 MiB on `team` and `starter`). The UUID in the error identifies the object — it's not automatically the same as your biggest build artifact.

## Diagnose in this order

Check fastest and most likely first.

**1. Check for an env var override (instant)**

```
echo $TESSELLATE_MAX_OBJECT
```

If this is set above 512 MiB, that's your cause (~25% of cases). The CLI doesn't validate this value against your plan, so it'll let you configure a limit the server will still reject.

**Fix:** Lower `TESSELLATE_MAX_OBJECT` to 512 MiB or unset it, in whatever CI config sets it.

**2. Find the actual oversized object (~3 min on a large repo)**

```
tessellate cache inspect --largest 10
```

This is the cause about 70% of the time: a genuine artifact over 512 MiB. Common sources are unpruned `node_modules`, committed build output, lockfiles bundled into the cache scope, or a monorepo package that pulls in a large binary dependency.

**Fix:** Exclude the oversized object from the cache scope, or split it out of the package being cached. If the artifact legitimately needs to stay that large, `enterprise` has no per-object limit.

**3. Check for a corporate proxy mangling the upload (~10 min, rare)**

If steps 1 and 2 don't explain it — no env override, and `cache inspect` shows nothing near 512 MiB — a proxy between your CI runner and Tessellate may have re-chunked the upload and reported a bogus size header. This is rare (~5% of cases).

```
curl -v --trace-ascii trace.log https://<your-tessellate-upload-endpoint>
```

Compare the `Content-Length` your proxy is sending against what your CLI actually generated. If you're behind a corporate proxy or a CI runner with outbound traffic inspection, this is the likely cause.

**Fix:** Add a bypass rule for the Tessellate upload endpoint in your proxy config, or route CI traffic around the proxy for this host.

## Notes

- The 512 MiB limit applies per object, not per upload — a cache with many small objects and one 600 MiB object will fail on the one object, not the whole cache.
- `TESSELLATE_MAX_OBJECT` is a client-side hint, not an entitlement. Setting it above your plan's limit changes nothing server-side — the server will still reject at 512 MiB on `team`/`starter`.

Next: run `echo $TESSELLATE_MAX_OBJECT` first — it's instant and rules out a quarter of cases before you spend 3 minutes on `cache inspect`.