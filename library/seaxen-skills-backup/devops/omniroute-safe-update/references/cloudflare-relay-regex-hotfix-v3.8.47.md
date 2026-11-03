# Cloudflare relay regex hotfix on OmniRoute v3.8.47

## Symptom chain
- Cloudflare account add/deploy initially failed with parser errors during Worker upload.
- After the local hotfix removed the bad emitted regex, the relay itself could pass direct probes, but OmniRoute still needed focused verification on the target branch before an upstream PR.

## Root cause
`release/v3.8.47` still emitted this worker line in `src/lib/proxyRelay/cloudflareWorkerScript.ts`:

```js
const upstream = await fetch(target.replace(/\\/$/, "") + relayPath, init);
```

In the generated Cloudflare Worker body that surfaced as:

```text
Uncaught SyntaxError: Invalid regular expression flags at worker.js:64:48
```

Safer replacement:

```js
const targetBase = target.endsWith("/") ? target.slice(0, -1) : target;
const upstream = await fetch(targetBase + relayPath, init);
```

## Fast live verification
1. Confirm OmniRoute container is healthy.
2. Inspect the built chunk in the container:
   ```bash
   docker exec omniroute sh -lc "nl -ba /app/.build/next/server/chunks/_05gd49m._.js | sed -n '60,66p'"
   ```
3. Bad build shows the `target.replace(/\\/$/, "")` line.
4. Good build shows `targetBase = target.endsWith("/") ? ...` and `fetch(targetBase + relayPath, init)`.

## If full source rebuild is blocked
A full Docker rebuild may fail on network/apt issues. Safe fallback:
1. Derive a local image from the current official digest.
2. Patch both:
   - `/app/src/lib/proxyRelay/cloudflareWorkerScript.ts`
   - `/app/.build/next/server/chunks/_05gd49m._.js`
3. Point compose to the local image and recreate.
4. Verify:
   - container healthy
   - compiled chunk fixed
   - direct Cloudflare relay probe returns HTTP 200 with `x-relay-auth`, `x-relay-target: https://api64.ipify.org`, `x-relay-path: /?format=json`

## If upstream `latest` moves before the PR merges
When the official OmniRoute image advances before your Cloudflare fix is merged, do **not** switch compose back to `diegosouzapw/omniroute:latest`.

Safe carry-forward pattern:
1. back up `/mnt/tb/1Apps/omniroute`
2. inspect the new remote digest for `diegosouzapw/omniroute:latest`
3. patch `Dockerfile.cloudflare-relay-hotfix` so `FROM diegosouzapw/omniroute@sha256:<new_digest>`
4. build a fresh local image tag (for example `omniroute:cf-relay-hotfix-YYYYMMDD`)
5. update compose to that new local tag
6. recreate the container
7. verify the live compiled chunk still shows the `targetBase` / `fetch(targetBase + relayPath, init)` lines

This preserves the local Cloudflare fix while still taking the newer upstream image.

## Direct relay probe implementation note
Do not assume an older ad-hoc decrypt recipe. The durable source of truth is OmniRoute source:
- `src/lib/db/proxies/mappers.ts` → `extractRelayAuth(...)`
- `src/lib/db/encryption.ts` → actual field encryption/decryption rules

In the current app version the relay secret path uses OmniRoute's field encryption helper, not the older PBKDF2-style scratch script that was used in an earlier session. Re-check the source helpers first if a manual probe starts failing after an update.

## Interpreting post-fix worker probe results
The parser bug and the worker-edge authorization path are separate failure classes.

Examples:
- `Invalid regular expression flags` / `Unexpected token 'return'` = generated worker script bug
- `HTTP 200` with ipify JSON = worker path + auth both good
- `HTTP 403` with body `error code: 1010` = Cloudflare edge/account rule denial; the worker syntax fix may still be present and correct

So after an update, confirm both:
1. live chunk still contains the fixed `targetBase` code
2. direct worker probe result, interpreted separately from parser status

## Upstream PR workflow lesson
Do **not** open the follow-up PR from the old working branch used for the previous PR.

For this case:
- correct base was `release/v3.8.47`
- create a fresh branch from that release branch
- cherry-pick or restage only the upstream-worthy changes
- rerun the focused Cloudflare relay tests on that clean branch

### Important pitfall
The real target branch may still lack pieces that were merged elsewhere.

On `release/v3.8.47`, the follow-up PR needed not only the regex fix but also Cloudflare deploy route alignment to keep the focused test suite coherent:
- metadata comments should describe `body_part`
- metadata key must be `body_part: "index.js"`, not `main_module`

## Focused verification recipe for the PR
Run:

```bash
DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm \
  --import ./open-sse/utils/setupPolyfill.ts \
  --import ./tests/_setup/isolateDataDir.ts \
  --test tests/unit/relay-deploy-5128.test.ts
```

Target outcomes on the clean branch:
- `#5128A` pass
- `#5128B` pass
- `#5128C` pass
- `#6416` pass
- `#5128D` pass

## Negative proof pattern
To prove the regression test matters:
1. Save the fixed `cloudflareWorkerScript.ts`.
2. Swap in the actual `HEAD` version from the unfixed target branch.
3. Regenerate the worker body.
4. Parse it in a separate Node process with `new Function(...)`.
5. Confirm exact failure:
   ```text
   Invalid regular expression flags
   ```
6. Restore the fixed source and confirm parse success.

## Outcome from this session
Follow-up upstream PR created against `release/v3.8.47`:
- `diegosouzapw/OmniRoute#7063`
