Using the `developer-troubleshooting-docs` skill's Step 4 (this is a stable, exact-string error → **error reference entry** shape) and Step 5 (six-part entry: message, applies-to, cause, fix, confirm, still-stuck), with the fix branches ordered by cause-likelihood ÷ diagnosis-time (KCS environment field, DITA multi-cause troubleshooting body, Nielsen heuristic 9 for tone).

One gate flagged per Step 3 before the page: the `TESSELLATE_MAX_OBJECT` branch exists only because the client accepts a value above the plan's own ceiling without validating it — that's a product-side gap, not just a support scenario, and it's called out inline below rather than silently documented around. Also, per Step 7, I haven't been able to reproduce this myself against a live `tessellate` install, so the entry ships with an explicit "not reproduced" note instead of a verified stamp — replace that note once someone runs the three checks for real.

---

````markdown
# `cache upload rejected (HTTP 413): object exceeds the per-object limit`

Tessellate was uploading a build artifact to the remote cache and the server rejected it because the object is larger than your plan allows.

## Message

```text
tessellate: error: cache upload rejected (HTTP 413): object <OBJECT_ID> exceeds the per-object limit of <LIMIT_MIB> MiB for plan '<PLAN>'
```

`<OBJECT_ID>` is a per-upload UUID, `<LIMIT_MIB>` and `<PLAN>` vary by plan — for example `512 MiB for plan 'team'`.

## Applies to

- CLI 2.1 through current (2.8), on Linux and macOS.
- **Not Windows**: the Windows build caps object size differently and does not hit this path. If you're on Windows and seeing a 413 or a size-related rejection, the causes below don't apply — go straight to Still stuck.
- Plans `team` and `starter` (each has its own per-object limit, shown in the message). Plan `enterprise` has no per-object limit and cannot produce this error — if you're on `enterprise`, this is a billing/plan-sync bug, not a real cache-size problem.

## Cause

The upload is rejected for one of three reasons, in order of how often each one turns out to be it:

1. The CLI's local override for the per-object ceiling is set above what the account's plan actually allows, and the client doesn't validate that before trying to upload.
2. The artifact genuinely is bigger than the plan's limit.
3. A corporate proxy between the CLI and Tessellate re-chunks the upload and reports a corrupted or mismatched size header, so the server rejects a payload that was never really over the limit.

## Fix

### If `TESSELLATE_MAX_OBJECT` is set above your plan's limit

This is checked first because it's a ten-second check and it's the actual cause about a quarter of the time — cheaper to rule out than to run a ten-minute trace on the off chance it's the rare cause.

1. In the CI job or shell where the upload runs: `echo $TESSELLATE_MAX_OBJECT`.
   - Requires: running this in the *same* environment that performed the upload — a value set only on your laptop won't explain a CI failure, and vice versa.
2. Compare it to your plan's actual limit (the `<LIMIT_MIB>` shown in your own error message is authoritative, not this page's example).
3. If it's set above that limit, unset it or lower it: `unset TESSELLATE_MAX_OBJECT` (or remove it from the CI job's env block).

> Flagged as a product gap, not just a support scenario: the CLI accepts any value here without checking it against the plan, so misconfiguring this variable produces this same 413 instead of a clear "your override exceeds your plan" error at set-time. Until the client validates this, checking the variable's value is on the reader.

### If the artifact really is over the limit

Most common cause (roughly 7 in 10 cases), but confirming it takes a few minutes on a large repo — run this after ruling out the free check above, not before.

1. `tessellate cache inspect --largest 10`.
   - Requires: local access to the same cache the failing upload targeted; on a large monorepo this can take around 3 minutes.
   - Expected: a ranked list of cached objects by size. If the top entry is at or above your plan's `<LIMIT_MIB>`, this is confirmed.
2. If confirmed, either:
   - split or exclude that artifact from the cached build output (the specific target depends on what's producing it — a bundled binary, a monorepo-wide output, a debug symbol file, etc.), or
   - move to a plan with a higher or no per-object limit.

### If a corporate proxy is mangling the upload

Rare (roughly 1 in 20 cases) and the slowest to confirm — only worth it once the two checks above have come back clean.

1. Capture the upload with `curl -v --trace-ascii - <YOUR_TESSELLATE_UPLOAD_ENDPOINT>` for a request of known size, substituting the actual cache endpoint your CLI is uploading to (visible in the CLI's own connection error output, or from whoever configured your Tessellate account).
   - Requires: ability to reproduce the upload through the same network path as CI (same proxy, same egress rules) — running this from an unproxied machine won't reproduce it. Budget around 10 minutes.
   - Expected (healthy): the `Content-Length` header in the trace matches the artifact's real on-disk size, and there's no unexpected `Transfer-Encoding: chunked` injected mid-stream.
2. If the header is wrong or re-chunked, the proxy is the cause: add the Tessellate upload host to your proxy's bypass/`NO_PROXY` list, or ask whoever manages the proxy to stop intercepting TLS for that host.

## Confirm it worked

The next cache upload for the same build completes with no `HTTP 413` line in the CLI output, and re-running `tessellate cache inspect --largest 10` no longer shows an object at or above your plan's limit (unless you upgraded plans, in which case it's expected to still be listed but no longer rejected).

## Still stuck

Open a support request with:

- CLI version (`tessellate --version`) and OS.
- Plan name and the exact `<LIMIT_MIB>`/`<PLAN>` from your own error message.
- Output of `echo $TESSELLATE_MAX_OBJECT` from the failing environment.
- Output of `tessellate cache inspect --largest 10`.
- If proxy interference is suspected: the `curl -v --trace-ascii` capture from the check above.

Never attach the artifact itself or full object contents — the object ID and size are enough to diagnose from.

---

Reported under these conditions, not reproduced here — verify the three checks and the fix steps against a real 2.1–2.8 install before publishing, then replace this line with a `Last verified: <YYYY-MM-DD> on <version> · Owner: <team or handle>` stamp.
````

Findability note (Step 8): give this its own page or a stable anchor (e.g. `#cache-upload-rejected-http-413`), and since the CLI already prints the full text verbatim, add a docs URL to the error payload itself (e.g. append `— see <DOCS_URL>#cache-upload-rejected-http-413` to the printed message) so the fix is one click from the failure, not just one search away.