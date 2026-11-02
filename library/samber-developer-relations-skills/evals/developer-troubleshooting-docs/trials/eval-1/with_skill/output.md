# Before the pages: what this deliverable is actually built on

Running this through the troubleshooting-docs skill (KCS capture model, DITA `<troubleshooting>` topic type, Nielsen heuristic 9, SRE document-vs-fix gate) surfaces a problem worth naming before the content, because the skill's first hard rule is: **stop and say so when there's no signal source, don't write from imagination.**

Here's the honest state:

- I have no Halyard-specific evidence at all — no tickets, no telemetry, no search logs, and I don't have a running `halyard-runner` binary or a Docker daemon in this environment to reproduce anything against (checked — no `docker` binary here).
- What I do have: the shared inbox is a real reported source even though nobody tags it — it's just unmined, not absent. It's worth a one-hour hand-pass before launch (skim the last ~200 threads, tally by error text, keep one raw example per cluster — same method the skill uses when there's no scriptable environment). If Halyard has a public issue tracker or a Discord/Slack, that's a second free source, and it's not clear from your ask whether one exists.
- The 15 topics below are the well-documented, industry-wide failure modes for *any* Docker-backed self-hosted CI runner (permission/socket errors, OOM kills, registry rate limits, DNS-in-container, port collisions, etc.). These strings are real and stable — they come from Docker Engine, git, and OpenSSH, not from guesswork — so they're a legitimate starting draft. What's *not* verified is whether Halyard's own runner wraps them, changes the text, or has a different cause chain in 4.0.

So: every page below ships with an explicit **"reported, not reproduced against Halyard"** flag in its footer, per the skill's rule that confident-and-wrong beats honestly-incomplete only in appearance, never in outcome. That flag is what makes "we'll correct them later" survive contact with reality — it tells whoever corrects a page later exactly what's already been checked (Docker/git semantics) and what hasn't (your product's actual output). Section 4 below turns that correction pass into an actual mechanism instead of a hope.

Ship these now if the 30th is fixed. Just don't strip the verification footers when you publish — that line is the only thing standing between this and a page that costs you more trust than having no page at all.

---

## 1. Ranked queue (provisional — no real cluster data exists yet)

Ranked by industry-base-rate frequency × blast radius ÷ effort, the same ratio the skill uses, substituting documented CI/Docker prevalence for ticket counts since none exist yet.

| # | Cluster | Shape | Evidence tier | Notes / routing |
|---|---|---|---|---|
| 1 | Registration token invalid/expired | Error reference | Industry-standard pattern | First-run blocker — promote regardless of frequency |
| 2 | TLS cert verification fails connecting to server | Error reference | Industry-standard pattern | Common behind corporate proxies/self-signed CAs |
| 3 | 4.0 config field renamed, runner won't start after upgrade | Known-issue | **Needs confirmation from engineering** | Gate: if it's an intentional breaking change, this is a pointer to the changelog/migration notes, not a full guide (out of scope — routes to `version-migration-guide`). If it's an unintended regression, file it, don't document around it. Ship as a 1-paragraph stub until that's answered. |
| 4 | Cannot connect to Docker daemon | Error reference | Industry-standard pattern | Highest-frequency Docker-adjacent failure across every CI runner |
| 5 | Permission denied on docker.sock | Error reference | Industry-standard pattern | Product suggestion: installer could detect and fix this at install time — flag to eng |
| 6 | Job killed, exit code 137 (OOM) | Error reference | Industry-standard pattern | Product suggestion: emit "killed: out of memory" instead of bare 137 — flag to eng |
| 7 | `no space left on device` | Error reference | Industry-standard pattern | Frequent, reproducible, one afternoon |
| 8 | Docker Hub pull rate limit (429/`toomanyrequests`) | Error reference | Industry-standard pattern | Growing cluster industry-wide since Docker Hub's 2020 rate limits |
| 9 | `pull access denied` / `unauthorized` on private registry | Error reference | Industry-standard pattern | Frequent, reproducible |
| 10 | `exec format error` (arch mismatch) | Error reference | Industry-standard pattern | Rising with arm64 runners (Graviton, Apple Silicon CI hosts) |
| 11 | DNS/network failures inside job containers | Troubleshooting how-to | Industry-standard pattern | Multiple causes → triage shape, not a single code |
| 12 | `port is already allocated` on concurrent jobs | Error reference | Industry-standard pattern | **Above the line, tentatively**: looks like a product gap (fixed port mappings instead of ephemeral allocation) — flag to eng, page is the interim measure |
| 13 | Git checkout auth failure (`could not read Username`) | Error reference | Industry-standard pattern | Frequent at private-repo onboarding |
| 14 | Job hangs near completion, no new log output | Troubleshooting how-to | Industry-standard pattern | First-use blocker, no stable string — promote |
| 15 | Cache restore fails / corrupted archive | Troubleshooting how-to | Industry-standard pattern | Multiple causes (disk full mid-write, permissions, format change) |

**Coverage target**: can't set the skill's usual "80% of top 20 clusters" baseline — there are no real clusters yet to be 80% of. Treat this batch of 15 as cycle 0. Set the real target in cycle 1, after the inbox hand-pass in Section 4 gives you actual counts.

**Deleted, not demoted**: nothing dropped for self-serviceability — all 15 are reader-actionable without support intervention, which is why they made this list over other plausible clusters (e.g., account/licensing issues, which are account-state problems, not docs problems, and route to a support macro instead).

---

## 2. The 15 pages

### 1 — `runner registration failed: invalid or expired token`

## Message
```text
Error: could not register runner: registration token is invalid or has expired
```

## Applies to
Halyard Runner 3.x and 4.0, all platforms.

## Cause
The token passed to `halyard-runner register` was copied incorrectly, has already been consumed (registration tokens are single-use in some configurations), or has expired since it was issued.

## Fix

### If the token was mistyped or truncated
1. Regenerate the token from the Halyard server: **Settings → Runners → New registration token**.
2. Copy it directly into the command — avoid retyping:
   ```
   halyard-runner register --server https://<HALYARD_SERVER> --token <TOKEN>
   ```

### If the token already registered a different runner
Registration tokens are consumed on first successful use. Generate a new token per runner rather than reusing one across machines.

### If the token expired before use
Tokens issued with a TTL expire silently. Generate the token immediately before running `register`, not ahead of a scheduled rollout.

## Confirm it worked
`halyard-runner register` prints `runner registered: <RUNNER_ID>`, and the runner appears **Online** on the server's Runners page within 30 seconds.

## Still stuck
Email support with subject `[halyard-runner] registration - <RUNNER_ID or hostname>`, and attach: the exact command run (token redacted), the server version, and the runner's OS/arch.

---
Last verified: not verified against Halyard 4.0 — reported pattern, common to token-based CI runner registration flows (GitLab Runner, GitHub Actions self-hosted use the same shape) · Owner: docs (assign before publish)

---

### 2 — `x509: certificate signed by unknown authority`

## Message
```text
Error: could not connect to https://<HOST>: x509: certificate signed by unknown authority
```

## Applies to
Halyard Runner 3.x and 4.0, any deployment where the Halyard server sits behind a self-signed certificate or an internal CA.

## Cause
The runner's trust store doesn't include the CA that signed the Halyard server's TLS certificate. This is expected for self-hosted deployments using an internal CA, and is not a Halyard defect.

## Fix

### If the server uses an internal or self-signed CA
1. Copy the CA certificate (not the server certificate) to the runner host.
2. Add it to the runner's trust bundle, either the OS trust store or a Halyard-specific override:
   ```
   halyard-runner register --server https://<HOST> --token <TOKEN> --ca-cert /path/to/ca.pem
   ```

### If a corporate proxy is terminating TLS
The certificate the runner sees is the proxy's, not the Halyard server's. Confirm with:
```
openssl s_client -connect <HOST>:443 -showcerts
```
Check the `Issuer` line. If it names your proxy vendor, add the proxy's CA the same way as above — this is a network policy, not a Halyard configuration issue.

## Confirm it worked
`halyard-runner register` completes without a TLS error, and `curl --cacert /path/to/ca.pem https://<HOST>/healthz` returns `200`.

## Still stuck
Email support with subject `[halyard-runner] tls - <hostname>`, attaching the `openssl s_client` output above (redact nothing here — it contains no secrets, only certificate metadata).

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Go/OpenSSL certificate-chain behavior · Owner: docs (assign before publish)

---

### 3 — Known issue: runner won't start after 4.0 upgrade, `unknown field` in `runner.yaml`

**Symptom**: after upgrading from 3.x to 4.0, `halyard-runner start` exits immediately with `error: unknown field "<FIELD>" in runner.yaml` or the process starts but silently ignores a 3.x setting.
**Cause**: **under investigation — needs a decision from engineering before this page is more than a stub.** Two different bugs would produce this text: (a) an intentional 4.0 config schema change with no migration shim, or (b) a genuine parser regression. These need different pages — (a) is a known-issue pointer to the changelog, (b) gets filed and pulled from this list entirely once fixed, per the skill's rule that a page should never be the permanent home for a bug the product could stop emitting.
**Workaround**: run `halyard-runner config validate --file runner.yaml` before restarting the service; it lists every rejected field. Rename or remove the listed fields, cross-referencing the 4.0 changelog's config-changes section (if one exists — if not, that's the actual gap to close before launch, not this page).
**Tracking**: `<link once filed>` **Fixed in**: unreleased

---
Last verified: not verified — do not publish as-is. This is a placeholder that needs one answer from engineering (breaking change vs. regression) before the 30th, not a correction "later." Owner: docs + eng, due before launch.

---

### 4 — `Cannot connect to the Docker daemon at unix:///var/run/docker.sock`

## Message
```text
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

## Applies to
Halyard Runner 3.x and 4.0, Linux and macOS hosts, any job that runs a container-based step.

## Cause
The Docker Engine daemon (`dockerd`) is not running, not yet started at boot before the runner service starts, or the runner is pointed at a non-default socket path.

## Fix

### If Docker is simply not running
1. Check the daemon: `sudo systemctl status docker` (Linux) or open Docker Desktop (macOS).
2. Start it: `sudo systemctl start docker`.
3. If the runner starts before Docker on boot, add an explicit dependency: `systemctl edit halyard-runner` and add `After=docker.service` and `Requires=docker.service`.

### If the socket is at a non-default path
Set `DOCKER_HOST` in the runner's environment, or the equivalent `docker.host` key in `runner.yaml`, to match where the daemon actually listens (`docker context ls` shows the active socket path).

## Confirm it worked
`docker info` (as the runner's own user, not root) returns a server section without error, and the next queued job leaves the `pending` state.

## Still stuck
Email support with subject `[halyard-runner] docker-daemon - <hostname>`, attaching `systemctl status docker` output and the runner's `docker.host` config value.

---
Last verified: not verified against Halyard 4.0 — reported pattern, this exact string is emitted by the Docker CLI itself, independent of Halyard · Owner: docs (assign before publish)

---

### 5 — `permission denied while trying to connect to the Docker daemon socket`

## Message
```text
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: ...
```

## Applies to
Halyard Runner 3.x and 4.0, Linux hosts where the runner does not run as root.

## Cause
The runner's service user isn't in the `docker` group, so it can't open the daemon's Unix socket. This is standard Docker Engine access control, not a Halyard-specific restriction.

## Fix
1. Add the runner's user to the `docker` group: `sudo usermod -aG docker <runner-user>`.
2. Restart the runner service so it picks up the new group membership — a re-login alone isn't enough for a systemd service: `sudo systemctl restart halyard-runner`.
3. If you'd rather not grant Docker-equivalent root access to the runner user (it is effectively root-equivalent), run the runner in [rootless Docker mode](https://docs.docker.com/engine/security/rootless/) instead — flag this as the recommended path for security-conscious installs in the page, not just the fast fix.

## Confirm it worked
`sudo -u <runner-user> docker ps` returns a table (even if empty) with no permission error.

## Still stuck
Email support with subject `[halyard-runner] docker-permission - <hostname>`, attaching `id <runner-user>` output and the OS/distro version.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Docker Engine group-based socket ACL · Owner: docs (assign before publish)

---

### 6 — Job container killed, exit code 137

## Message
```text
Job failed: container exited with code 137
```

## Applies to
Halyard Runner 3.x and 4.0, any job with a memory ceiling configured (`resources.memory` in the job spec) or running on a host under memory pressure.

## Cause
Exit code 137 is 128 + `SIGKILL` (9). In a containerized job this is almost always the Linux OOM killer terminating the process for exceeding its memory limit — either the job's configured limit or the host's available memory. It is not a crash in the job's own code.

## Fix

### If the job has an explicit memory limit
1. Check the configured ceiling in the job spec.
2. Raise it, or reduce the job's memory footprint (common culprits: an in-memory build cache, a test suite running unbounded parallel workers, a language runtime's default heap sizing to *host* memory rather than *container* memory — check whether your runtime respects cgroup limits).

### If no limit is set explicitly
The host itself ran out of memory, usually from too many concurrent jobs on one runner. Check host memory at the time of failure: `dmesg | grep -i "oom"` on the runner host will show the OOM killer's own log entry naming the process. Reduce concurrent job count on this runner, or add memory.

## Confirm it worked
The job completes with a non-137 exit code, or `dmesg` shows no new OOM entries for the job's container ID during a re-run.

## Still stuck
Email support with subject `[halyard-runner] oom-137 - <job-id>`, attaching the job's configured memory limit and the `dmesg` OOM line if found.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Linux cgroup OOM behavior · Owner: docs (assign before publish). Product suggestion logged in queue notes: surface "killed: out of memory (limit was X)" in the job log directly instead of a bare exit code — would make this page mostly unnecessary.

---

### 7 — `no space left on device`

## Message
```text
Error: no space left on device
```

## Applies to
Halyard Runner 3.x and 4.0, any self-hosted runner host running Docker over time.

## Cause
The Docker Engine's image/layer/volume storage (usually `/var/lib/docker`) has filled the host's disk, most often from accumulated unused images, stopped containers, and build cache that nothing is pruning automatically.

## Fix
1. Confirm this is Docker's storage, not the job's own working directory: `docker system df` shows reclaimable space by category.
2. Reclaim it: `docker system prune -af --volumes` (this removes **all** unused images and volumes, not just this job's — confirm nothing else on the host depends on a "stopped but wanted" container first).
3. If this recurs weekly, it's a maintenance gap, not a one-off: schedule `docker system prune` on a cron, or configure Docker's built-in log/storage limits (`log-opts.max-size` in `daemon.json`) so it doesn't reach this state again.

## Confirm it worked
`df -h /var/lib/docker` shows free space, and the previously failing job completes.

## Still stuck
Email support with subject `[halyard-runner] disk-space - <hostname>`, attaching `docker system df` output and `df -h` for the partition backing Docker's storage.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Docker Engine storage-exhaustion behavior · Owner: docs (assign before publish)

---

### 8 — `toomanyrequests: You have reached your pull rate limit`

## Message
```text
Error response from daemon: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```

## Applies to
Halyard Runner 3.x and 4.0, any job pulling images from Docker Hub without authentication.

## Cause
Docker Hub rate-limits anonymous image pulls per IP (and authenticated free-tier pulls at a higher ceiling). A shared runner host pulling frequently — many concurrent jobs, no local cache — hits this quickly, especially from a single office/datacenter IP shared across every runner.

## Fix

### Fastest
Authenticate the runner's Docker daemon to Docker Hub with a service account: `docker login`, or configure the credential in `runner.yaml`'s registry auth section. This raises the ceiling immediately.

### Durable
1. Run a [pull-through registry mirror](https://docs.docker.com/docker-hub/mirror/) on your network so repeated pulls of the same base images hit your own cache, not Docker Hub, after the first pull.
2. Point the runner's Docker daemon at the mirror via `registry-mirrors` in `daemon.json`.

## Confirm it worked
`docker pull <image>` succeeds repeatedly in quick succession without the rate-limit error; `docker login` shows the authenticated account if using the fast fix.

## Still stuck
Email support with subject `[halyard-runner] pull-rate-limit - <hostname>`, attaching the approximate pull volume per hour and whether a mirror is already in place.

---
Last verified: not verified against Halyard 4.0 — reported pattern, documented Docker Hub rate-limit behavior since Nov 2020 · Owner: docs (assign before publish)

---

### 9 — `pull access denied` / `unauthorized: authentication required`

## Message
```text
Error response from daemon: pull access denied for <IMAGE>, repository does not exist or may require 'docker login'
Error response from daemon: unauthorized: authentication required
```

## Applies to
Halyard Runner 3.x and 4.0, jobs pulling from a private registry (including a private Docker Hub repo, GHCR, ECR, or a self-hosted registry).

## Cause
The runner's Docker daemon has no valid credentials for the registry, the credentials expired (common with short-lived cloud registry tokens like ECR's 12-hour tokens), or the image name/tag is simply wrong — Docker returns the same "access denied" text for "doesn't exist" and "you can't see it," which is intentional to avoid leaking repo existence to unauthorized callers.

## Fix

### If credentials were never set
Add registry credentials to the runner: `docker login <REGISTRY>` on the runner host, or the equivalent registry-auth block in `runner.yaml` for a per-job credential.

### If credentials expired
Cloud-provider registries commonly issue short-lived tokens. Confirm expiry:
```
docker login <REGISTRY>   # re-run; if it succeeds, the old token had expired
```
For ECR specifically, script the refresh (`aws ecr get-login-password`) on a cron shorter than the token's 12-hour lifetime rather than relying on a one-time login.

### If the image name or tag is wrong
Double-check for a typo before assuming an auth problem — the error text is identical either way.

## Confirm it worked
`docker pull <IMAGE>` succeeds from the runner host using the same credential path the job uses.

## Still stuck
Email support with subject `[halyard-runner] pull-auth - <registry-host>`, attaching the exact image reference used (no credentials) and the registry provider.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard registry auth (OCI distribution spec) behavior · Owner: docs (assign before publish)

---

### 10 — `exec /entrypoint: exec format error`

## Message
```text
standard_init_linux.go:228: exec user process caused: exec format error
```

## Applies to
Halyard Runner 4.0, any runner host on arm64 (Apple Silicon, AWS Graviton) pulling an image built only for amd64, or vice versa.

## Cause
The image's binary was compiled for a different CPU architecture than the runner host, and no matching-architecture layer exists in the pulled manifest. Docker will happily pull an image built for the wrong architecture without erroring at pull time — the failure only surfaces when the container actually tries to execute the binary.

## Fix

### If the image is yours to rebuild
Build and push a multi-arch manifest: `docker buildx build --platform linux/amd64,linux/arm64 -t <IMAGE> --push .`

### If the image is a third-party dependency
1. Check whether an arm64 tag exists (`docker manifest inspect <IMAGE>` lists available platforms).
2. If not, pin that job step to an amd64 runner explicitly (`platform: linux/amd64` in the job spec, if Halyard's job spec supports platform pinning — confirm against the 4.0 job-spec reference) rather than the CI host's native architecture.

## Confirm it worked
`docker run --rm <IMAGE> uname -m` inside the job step reports the architecture you expect, and the step's own entrypoint runs.

## Still stuck
Email support with subject `[halyard-runner] exec-format - <image-name>`, attaching the runner host's architecture (`uname -m`) and the image reference.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard OCI multi-arch manifest behavior. **Whether Halyard's job spec supports a `platform:` pin needs confirming against the actual 4.0 reference before this fix section ships.** · Owner: docs (assign before publish)

---

### 11 — Job containers can't resolve hostnames (DNS failures)

## Symptoms
- A step that calls out to an external host (package registry, API, git remote) fails with `Temporary failure in name resolution`, `Could not resolve host: <HOST>`, or `getaddrinfo ENOTFOUND <HOST>`.
- The same job succeeds when run directly on the runner host, outside a container.

## Before you start
Have the exact failing hostname and the job's network mode (Halyard's default bridge network vs. host network, if configurable) ready.

## Check 1 — Is DNS reachable from inside the container at all
```
docker run --rm <same base image> nslookup <HOST>
```
- Requires: the same image the job uses.
- If this also fails: the container's DNS config is the problem, not the specific job. Continue to Check 2.
- Expected: an IP address back for `<HOST>`.

## Check 2 — Is the Docker daemon's DNS misconfigured
Check `/etc/docker/daemon.json` for a `dns` override that no longer matches your network (a stale VPN-era DNS server is the most common cause). If absent, Docker inherits the host's `/etc/resolv.conf` — check that file resolves the host directly.

## Check 3 — Is a corporate proxy or firewall blocking DNS from the container's network namespace
Bridge-networked containers get a different source IP than the host. If your DNS server or firewall allow-lists by IP, the container's bridge-network IP may not be on the list even though the host's IP is.
- Test: `docker run --rm --network host <same image> nslookup <HOST>` — if this succeeds where the bridge-network version failed, the container's network namespace is the boundary being blocked.

## Confirm it worked
`nslookup <HOST>` and the job's actual network call both succeed from inside a container using the job's real network mode.

## Still stuck
Email support with subject `[halyard-runner] dns - <hostname-being-resolved>`, attaching the output of both `nslookup` runs above (bridge and host network) and your `daemon.json` DNS section if customized.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Docker bridge-networking/DNS behavior · Owner: docs (assign before publish)

---

### 12 — `Bind for 0.0.0.0:<PORT> failed: port is already allocated`

## Message
```text
Error response from daemon: driver failed programming external connectivity on endpoint <NAME>: Bind for 0.0.0.0:<PORT> failed: port is already allocated
```

## Applies to
Halyard Runner 3.x and 4.0, any host running more than one job concurrently where jobs bring up service containers (databases, mock servers) on fixed host ports.

## Cause
Two jobs scheduled on the same runner host both try to bind the same host port — typically because the job's `docker-compose.yml` or service definition hard-codes a port mapping (`5432:5432`) instead of letting Docker assign an ephemeral host port.

## Fix

### Fastest, per job
Change fixed host-port mappings to ephemeral ones — map only the container port, let Docker pick the host side: `"5432"` instead of `"5432:5432"` in compose, then read back the assigned port with `docker port <container> 5432` for anything downstream that needs to connect to it.

### If you don't control the job's compose file
Reduce concurrency on that runner to 1 job at a time (a capacity cost, not a fix), or run each job's services in an isolated Docker network/host namespace if your runner topology supports per-job isolation.

## Confirm it worked
Two jobs using the same service definition complete concurrently on the same host without a bind conflict.

## Still stuck
Email support with subject `[halyard-runner] port-conflict - <hostname>`, attaching the job's compose/service port mapping and how many jobs typically run concurrently on that host.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard Docker port-binding contention · Owner: docs (assign before publish). **Flagged in the queue as a probable product gap** — a runner that schedules concurrent jobs onto one host but relies on the job author to avoid fixed ports is asking every user to solve the same problem. Worth raising with eng as a scheduler-level fix (auto-rewrite fixed mappings to ephemeral, or isolate networks per job) rather than a permanent doc entry.

---

### 13 — `fatal: could not read Username for 'https://...'`

## Message
```text
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

## Applies to
Halyard Runner 3.x and 4.0, jobs checking out a private repository over HTTPS without stored credentials.

## Cause
Git is trying to prompt interactively for a username/password, which is disabled in a non-interactive CI environment by design. The runner has no credential helper or token configured for this remote.

## Fix

### If using a personal or fine-grained access token
Configure the credential once per runner, not per job: either a git credential helper backed by a token stored in the runner's secret store, or an `Authorization: Bearer <TOKEN>` header injected via `http.extraHeader` in the job's git config — check which mechanism Halyard's job spec exposes for secrets before hard-coding a token in a script.

### If using SSH instead of HTTPS
Switch the remote to `git@github.com:org/repo.git` and provision an SSH deploy key on the runner rather than fighting the HTTPS credential prompt entirely.

### If submodules are the actual failure point
The same error on a submodule checkout means the top-level repo's credentials don't automatically apply — submodule URLs need their own credential resolution; check `.gitmodules` for HTTPS vs SSH URLs matching what's configured.

## Confirm it worked
`git clone` (or the job's checkout step) completes without a prompt and without this error, for both the top-level repo and any submodules.

## Still stuck
Email support with subject `[halyard-runner] git-auth - <repo-host>`, attaching the remote URL scheme used (HTTPS or SSH) and whether submodules are involved. Never attach the token itself.

---
Last verified: not verified against Halyard 4.0 — reported pattern, standard git non-interactive credential behavior · Owner: docs (assign before publish)

---

### 14 — Job hangs near completion with no new log output

## Symptoms
- The job log stops advancing, usually somewhere past the 80-90% mark of typical run time for that job.
- The job doesn't fail — it just never finishes, until a timeout (if configured) eventually kills it.

## Before you start
Have the job's live log open and know whether it has an explicit timeout configured. Without a timeout, this failure mode can run indefinitely and burn a runner slot.

## Check 1 — Is a background process holding the container's stdout open
The most common cause: a step backgrounds a process (`some-daemon &`) and the shell — or the container itself — waits for all file descriptors to close before the step is considered done, even though the "real" work finished. Check whether the job explicitly redirects the background process's output (`some-daemon > /dev/null 2>&1 &`) — if not, that's very likely it.

## Check 2 — Is a lock file from a previous run still held
Package manager caches and some build tools (`npm`, `yarn`, Gradle's daemon) hold a lock file that a killed-mid-run previous job left behind. Check for a stale `.lock` file in the job's cache directory older than the current run's start time.

## Check 3 — Is the job waiting on a network call with no timeout of its own
A step calling an external service with no client-side timeout will hang exactly as long as that service takes to respond — which, on a flaky remote, can be forever. Check the step's own tooling (curl, an SDK client) for a default timeout; most don't set one.

## Confirm it worked
The job completes within its normal duration range, and the log shows continuous forward progress with no multi-minute gaps.

## Still stuck
Email support with subject `[halyard-runner] job-hang - <job-id>`, attaching the full job log (even though it's incomplete) and the job's configured timeout, if any.

---
Last verified: not verified against Halyard 4.0 — reported pattern, common CI hang causes across Docker-based runners generally · Owner: docs (assign before publish)

---

### 15 — Cache restore fails or produces a corrupted cache

## Symptoms
- The job log shows a cache-restore step failing with something like `unexpected EOF`, `archive/tar: invalid tar header`, or the step silently reports a cache miss every run despite a prior save succeeding.
- Build times return to cold-cache duration with no clear cause.

## Before you start
Know the cache backend in use (local disk on the runner vs. a remote cache store) and whether the previous job that wrote this cache entry completed normally or was killed/timed out.

## Check 1 — Was the cache written by a job that was killed mid-write
A job killed by OOM (see entry 6) or a timeout mid-save leaves a partial, corrupted archive behind — the next job's restore fails on that truncated file. Check the writing job's own exit status in its history, not just the current job's failure.

## Check 2 — Did the disk fill up during the write
A save that runs out of disk space (see entry 7) writes a truncated archive without necessarily erroring the save step itself, depending on how the cache tool handles a short write. Check available disk on the cache backend at the time of the prior save.

## Check 3 — Did the cache key format change across a Halyard version bump
If this started right after the 4.0 upgrade, the cache serialization format or key hashing may have changed between versions, making 3.x-written caches unreadable by 4.0. Check the 4.0 changelog for cache-format notes; if none exist, this is worth filing as a gap rather than assuming user error.

## Fix
Once the cause is identified: delete the specific corrupted cache key rather than the whole cache namespace, and re-run the writing job to completion once (uninterrupted) to repopulate it.

## Confirm it worked
The next job's cache-restore step reports a successful hit with the expected size, and build time returns to warm-cache duration.

## Still stuck
Email support with subject `[halyard-runner] cache-corrupt - <cache-key>`, attaching the writing job's exit status and whether this started right after a Halyard version upgrade.

---
Last verified: not verified against Halyard 4.0 — reported pattern, general cache-corruption causes; the version-bump cause (Check 3) is a guess, not a confirmed Halyard behavior — flag to eng before publishing this check. · Owner: docs (assign before publish)

---

## 3. Verification log

Every row says the same thing because the constraint is the same for all 15: no Halyard instance, no Docker daemon, no company signal available in this pass.

| # | Entry | Reproduced against Halyard? | What *is* verified | Owner to close the gap |
|---|---|---|---|---|
| 1–15 | All | No | The exact error strings and root causes for entries 4–13 are real, current Docker Engine / git / OpenSSL behavior — those substrings won't be wrong. Halyard-specific wrapping, exit-code mapping, config-key names, and whether the CLI flags shown (`--ca-cert`, `--token`, `platform:`) actually exist in 4.0 are **not** verified. | Whoever owns the runner codebase — needs 1–2 hours running each command against a real 4.0 install |

**Before publishing any of these**, run this pass once (a couple of hours, not a rewrite):
1. Trigger each failure on a real 4.0 runner and diff the actual emitted text against the `Message` block above.
2. Run each `Fix` step from a clean, non-configured machine, not an already-fixed one.
3. Delete or correct any CLI flag/config key that doesn't exist in 4.0 (entries 2, 10, 13, 3, 15 have flagged assumptions above).
4. Update the `Last verified` footer to a real date, version, and owner once done — that's what makes the next person trust the page without re-checking it.

If the 30th arrives before that pass happens, ship with the footers as-is rather than deleting them — "reported, not reproduced" published beats a silent gap, but a silently-removed caveat is worse than either.

---

## 4. Wiring, capture loop, and what "we'll correct them later" should actually mean

**Findability**
- One page per error string, URL slug = the error identifier (e.g., `/troubleshooting/docker-daemon-not-running`), title = the verbatim string. Readers paste the string into search; they don't browse a troubleshooting index.
- Skip FAQ schema markup — Google retired that rich result in May 2026; it buys nothing here.
- If `halyard-runner`'s own error output can carry a doc link (a `doc_url` field or a bare URL after the error text, the way Stripe does it), that's a one-line product change with a bigger payoff than any of the 15 pages individually — put it on the eng backlog now, not after launch.

**Turning "we'll correct them later" into an actual mechanism** — this is the real fix for the "no ticket system" problem, and it's cheap:
1. **Subject-line convention for the shared inbox**, starting now: every "Still stuck" section above asks the reader to use `[halyard-runner] <topic> - <detail>`. That alone makes the untagged inbox greppable by topic without buying a ticket tool.
2. **Weekly 30-minute pass**: whoever reads the shared inbox tallies subject-line prefixes, updates the queue in Section 1 with real counts, and flags which of the 15 pages got real hits vs. zero — a page nobody's inbox-subject matches in a month is either genuinely rare or not the actual failure text; check before assuming it's fine.
3. **Capture at resolution, not from memory**: whoever answers an inbox thread that isn't yet covered writes down the error text, cause, and fix *in that reply*, before closing the thread — that reply is the first draft of the next page. This is the KCS solve-loop, and it's the same effort as replying anyway.
4. **Re-run this exercise in 4–6 weeks** with real inbox tallies instead of industry base rates. Expect some of these 15 to be wrong priority (something you didn't predict floods the inbox, something here never comes up) — that's the correction, and it's a diff against this list, not a rewrite of it.

**Metrics to actually track** (cheap — no tooling purchase required):
- Inbox thread count per subject-line prefix, week over week.
- Whether a thread with a matching page still needed a human reply (means the page didn't land, or wasn't found).
- Skip "deflection rate" as a headline number — it's not measurable without a ticket system, and the folklore "$X per deflected ticket" figures have no traceable source; don't put them in front of your head of support as if they were real.

**Maintenance triggers to book now**: any 4.0 patch that changes an error's text or a config key invalidates the matching page same-release, not "next cycle" — and entry 3 and entry 15's version-bump guess both need an eng answer before they're more than placeholders.