Here's the troubleshooting section. It's built entirely from general knowledge of self-hosted CI runners and Docker — not from Halyard ticket data, since none exists yet. I've used plausible Halyard-style naming (`halyard-agent`, `.halyard.yml`, the Halyard server) to keep it consistent, but every literal error string, exit code, log path, and config key needs a pass against what your runner actually prints before this goes live. I've flagged the spots most likely to need correction inline.

---

# Troubleshooting

## How to use this guide

This section covers the errors people most commonly hit when running Halyard: runner connectivity, Docker failures, disk and memory exhaustion, networking inside jobs, and job-level problems like timeouts and flaky tests.

Each page follows the same structure:

- **Symptom** — what you see in the UI, the logs, or the job output.
- **Likely causes** — ranked roughly by how often they show up.
- **Diagnose** — commands to run and what to look for.
- **Fix** — the actual resolution.
- **Prevent it** — how to stop it recurring.

If a fix here doesn't match what you're seeing, the log excerpt is the most useful thing to send to support — paste it in full, including the lines above and below the error, not just the last line.

Two commands come up on nearly every page:

```bash
halyard-agent logs --since 1h          # agent-side log tail
halyard job logs <job-id> --raw        # full, unfiltered job output
```

*Reviewer note: confirm both commands exist under these exact names before publishing.*

---

## 1. Runner won't register or shows offline

**Symptom**

A new runner never appears in the Halyard dashboard, or an existing one flips to "offline" and stays there. The agent log shows repeated connection attempts:

```
level=error msg="failed to register runner" err="dial tcp: lookup halyard.example.com: no such host"
```

or

```
level=error msg="heartbeat failed" err="context deadline exceeded"
```

**Likely causes**

- Wrong server URL or registration token in `/etc/halyard/agent.yml`.
- Outbound firewall blocking the port the agent uses to reach the Halyard server (typically 443 or a custom control-plane port).
- Clock skew between the runner host and the server — token validation and TLS both reject requests when the two clocks disagree by more than a few minutes.
- The registration token already expired or was already consumed by another host.
- A corporate proxy intercepting TLS and breaking the agent's certificate check.

**Diagnose**

```bash
systemctl status halyard-agent
halyard-agent logs --since 1h | grep -i error
curl -v https://<your-halyard-server>/api/v1/ping
timedatectl status
```

If `curl` fails the same way the agent does, this is network or DNS, not Halyard. If `curl` succeeds but the agent still fails, look at the token and clock.

**Fix**

- Re-generate the registration token from the dashboard and re-run `halyard-agent register --token <token>`.
- If a proxy is involved, set `HTTPS_PROXY` in the agent's systemd unit environment, not just the shell — the agent runs as a service and won't see your interactive shell's env vars.
- Sync the clock: `sudo timedatectl set-ntp true`, then restart the agent.

**Prevent it**

Registration tokens are single-use and time-limited by design — don't share one across multiple hosts or store it in a golden image. Bake NTP into your runner provisioning so clock drift never gets the chance to build up.

---

## 2. "Cannot connect to the Docker daemon" / permission denied on docker.sock

**Symptom**

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

or, when the daemon is up but the agent's user lacks access:

```
dial unix /var/run/docker.sock: connect: permission denied
```

**Likely causes**

- Docker isn't running on the runner host.
- The `halyard-agent` user isn't in the `docker` group (most common cause on freshly provisioned hosts).
- `DOCKER_HOST` points somewhere stale after a Docker upgrade or a switch to rootless Docker.
- SELinux or AppArmor blocking socket access on hardened hosts.

**Diagnose**

```bash
systemctl status docker
ls -l /var/run/docker.sock
id halyard-agent      # confirm group membership
groups halyard-agent
```

**Fix**

```bash
sudo systemctl start docker
sudo usermod -aG docker halyard-agent
sudo systemctl restart halyard-agent   # group changes need a re-login/service restart to take effect
```

If you're on rootless Docker, point the agent at the user-specific socket instead of the system one:

```yaml
# /etc/halyard/agent.yml
docker_host: unix:///run/user/1000/docker.sock
```

**Prevent it**

Add the group membership and socket permission check to whatever provisions your runners (cloud-init, Ansible, Terraform) so it's never a manual step done once and forgotten on the next host.

---

## 3. Jobs stuck in "queued", never start

**Symptom**

The job sits in the queue indefinitely. No container starts, no logs appear, and there's no error — just silence.

**Likely causes**

- No runner online that matches the job's required tags/labels.
- All matching runners are already at their configured concurrency limit.
- The runner is online but its Docker daemon is unreachable (see page 2) — some agent versions swallow this as a silent retry loop instead of surfacing an error.
- The job's `.halyard.yml` requests a runner tag that doesn't exist on any registered runner (a typo is the usual culprit).

**Diagnose**

```bash
halyard runners list --status online
halyard runners list --tags <tag-from-your-job-config>
halyard-agent logs --since 30m | grep -i "capacity\|concurrency"
```

Compare the tags in the job's YAML against `halyard runners list` output exactly — trailing whitespace or case differences will silently produce zero matches.

**Fix**

- Free up capacity by raising `max_concurrent_jobs` in the agent config, or add another runner.
- Fix the tag mismatch in `.halyard.yml`.
- If the runner shows online but nothing runs, restart the agent — a wedged Docker connection can leave the agent reporting healthy while unable to actually dispatch containers.

**Prevent it**

Set an alert on queue depth and time-in-queue, not just runner health — a runner can report "online" while still being unable to accept work, which is exactly the gap this symptom lives in.

---

## 4. "No space left on device" — disk pressure, orphaned containers and volumes

**Symptom**

```
write /var/lib/docker/overlay2/.../merged/app: no space left on device
```

Jobs that previously worked start failing mid-build, often at the point they write a large artifact or extract a dependency cache.

**Likely causes**

- Docker's image/layer cache growing unbounded — every unique base image and every layer from every build accumulates on disk indefinitely unless something prunes it.
- Stopped containers and dangling volumes from jobs that crashed instead of exiting cleanly, left behind because nothing cleaned them up.
- Build logs or artifacts written to local disk instead of shipped to object storage.
- The disk backing `/var/lib/docker` is simply undersized for the number of concurrent jobs and image variety you're running.

**Diagnose**

```bash
df -h /var/lib/docker
docker system df -v
docker ps -a --filter status=exited | wc -l
```

`docker system df -v` breaks down images, containers, and volumes separately — it usually makes clear which of the three is actually eating the disk, rather than guessing.

**Fix**

```bash
docker container prune -f
docker volume prune -f
docker image prune -a -f --filter "until=168h"   # keep last 7 days
```

For an immediate emergency, `docker image prune -a -f` reclaims the most space fastest, but it also wipes your build cache — expect the next build on each runner to be slow.

**Prevent it**

Schedule `docker system prune` on a cron job (weekly is usually enough; daily on busy runners) rather than running it reactively after a failure. Set explicit disk-space alerting at 80% on every runner host, not just the control plane.

---

## 5. Container killed unexpectedly — OOMKilled (exit code 137)

**Symptom**

The job container dies abruptly, mid-step, with no application-level error — just a truncated log and:

```
Error: container exited with code 137
```

`docker inspect` on the container (if it still exists) shows:

```json
"OOMKilled": true
```

**Likely causes**

- The job's memory limit (set in `.halyard.yml` or inherited from the runner default) is lower than what the build actually needs — common with JVM builds, large `npm`/`yarn` installs, and test suites that load big fixtures into memory.
- Several jobs running concurrently on the same host, together exceeding the host's physical RAM, even though each job individually fits its own limit.
- A memory leak in the thing being tested, not the CI process itself.

**Diagnose**

```bash
docker inspect <container-id> | grep -i oomkilled
free -h                       # on the runner host, during a run if possible
halyard job show <job-id> --resources
```

Exit code 137 specifically (128 + SIGKILL's signal number 9) is the tell — if you see a different exit code, this isn't OOM, look elsewhere.

**Fix**

Raise the memory limit for the job:

```yaml
# .halyard.yml
resources:
  memory: 4Gi   # was 2Gi
```

If concurrent jobs are the real cause, lower `max_concurrent_jobs` on the runner or move to hosts with more RAM rather than raising every job's individual limit.

**Prevent it**

Set memory limits deliberately per job type instead of relying on one global default — a Go binary build and a JVM test suite have very different footprints, and one default sized for the former will OOM the latter.

---

## 6. Image pull failures — auth, rate limits, private registries, TLS

**Symptom**

```
Error response from daemon: pull access denied for myorg/private-image, repository does not exist or may require 'docker login'
```

```
toomanyrequests: You have reached your pull rate limit
```

```
x509: certificate signed by unknown authority
```

**Likely causes**

- No registry credentials configured on the runner, or credentials that expired (common with short-lived tokens from cloud registries like ECR, which rotate every 12 hours).
- Docker Hub's anonymous pull rate limit, hit because every runner on a shared host pulls as the same unauthenticated IP.
- A private/self-hosted registry using a certificate your runner's CA bundle doesn't trust — frequent on internal registries using self-signed or internal-CA certs.
- Typo in the image name or tag, misread as an auth error because registries return the same generic "access denied" for both "doesn't exist" and "not authorized."

**Diagnose**

```bash
docker pull <image> --debug
cat ~/.docker/config.json | jq '.auths | keys'   # which registries have stored creds
openssl s_client -connect <registry-host>:443 -showcerts
```

**Fix**

- Log in explicitly and confirm it's stored: `docker login <registry>`.
- For ECR/GCR-style short-lived tokens, script credential refresh on a timer rather than logging in once and forgetting — 12-hour tokens will fail silently the next day.
- For rate limits, authenticate to Docker Hub even for public images (authenticated limits are far higher than anonymous), or run a pull-through cache/mirror.
- For untrusted certs, add the registry's CA to the runner host's trust store, not to a per-job workaround — `/etc/docker/certs.d/<registry-host>/ca.crt` is the standard location.

**Prevent it**

Run a local pull-through registry mirror for your most-used base images. It removes rate limits entirely and cuts build time, since most pulls hit the mirror's cache instead of the internet.

---

## 7. DNS and network resolution failures inside build containers

**Symptom**

```
curl: (6) Could not resolve host: registry.npmjs.org
```

Failures are intermittent — some jobs succeed, others on the same runner fail seconds apart, which usually points people at flaky-network theories before they check the actual cause.

**Likely causes**

- Docker's default embedded DNS forwards to the host's resolvers; if the host's `/etc/resolv.conf` points at a resolver unreachable from inside the container's network namespace (common with certain VPN or systemd-resolved setups), every container inherits the failure.
- MTU mismatch between the host network and Docker's bridge network causing large DNS responses (anything using EDNS0, which is most modern DNS) to silently drop instead of erroring cleanly.
- A custom Docker network attached to the job missing DNS configuration entirely.
- Corporate VPN split-tunneling that only routes internal domains, silently blackholing external lookups from inside the container.

**Diagnose**

```bash
docker run --rm alpine nslookup registry.npmjs.org
docker run --rm alpine cat /etc/resolv.conf
ip link show docker0
docker network inspect <network-name> | grep -i mtu
```

**Fix**

Pin explicit, known-good DNS servers instead of inheriting the host's:

```yaml
# /etc/docker/daemon.json
{
  "dns": ["1.1.1.1", "8.8.8.8"]
}
```

Restart Docker after changing this file. If MTU is the cause, set it explicitly to match the host's actual network MTU (often 1450 on cloud VPCs with overlay networking, not Docker's default of 1500):

```json
{ "mtu": 1450 }
```

**Prevent it**

Don't rely on host DNS inheritance on runner hosts that sit behind VPNs or split-tunnel routing — pin resolvers in the Docker daemon config as part of runner provisioning, before the first job ever runs on that host.

---

## 8. Git checkout failures — SSH keys, submodules, Git LFS, shallow clones

**Symptom**

```
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

```
fatal: clone of 'git@github.com:org/submodule.git' into submodule path 'vendor/x' failed
```

```
Encountered 1 file(s) that should have been pointers, but weren't: assets/large.psd
```

**Likely causes**

- The deploy key or SSH key configured for the runner doesn't have access to the specific repo (common right after a repo is transferred between orgs, or when a submodule lives in a different, unauthorized repo).
- Submodules use a different remote protocol than the parent repo (HTTPS parent, SSH submodule, or vice versa) and only one credential type is configured.
- Git LFS isn't installed on the runner image, so LFS-tracked files check out as pointer text instead of actual content.
- A shallow clone (`--depth 1`, often set for speed) breaks a build step that needs full history — `git describe`, changelogs, or version-from-tag logic.

**Diagnose**

```bash
ssh -T git@github.com -i <deploy-key-path>
git lfs env                         # confirms LFS is installed and configured
halyard job logs <job-id> --raw | grep -i "clone\|submodule\|lfs"
```

**Fix**

- Grant the specific deploy key read access to every submodule's repo, not just the parent.
- Standardize submodule URLs to match the parent's protocol (`git config --global url."https://github.com/".insteadOf "git@github.com:"` is a common normalization).
- Install `git-lfs` in the runner's base image and run `git lfs install` once per host.
- If full history is needed, set `clone_depth: 0` (or drop the shallow flag) for that specific job rather than globally — full clones are slower, so scope the fix to jobs that actually need it.

**Prevent it**

Bake `git-lfs` into the runner image build rather than installing it per job. Document which repos use LFS or submodules so the deploy-key access list doesn't drift out of sync as new submodules get added.

---

## 9. Docker-in-Docker (DinD) failures

**Symptom**

```
Cannot connect to the Docker daemon at tcp://localhost:2376. Is the docker daemon running?
```

```
error creating overlay mount to /var/lib/docker/overlay2/.../merged: device or resource busy
```

Jobs that build Docker images themselves (as opposed to just running inside a container) are the ones that hit this — a plain build-and-test job usually never touches DinD.

**Likely causes**

- The DinD sidecar container isn't running privileged, which it must be to manage its own Docker daemon inside a container.
- TLS is enabled by default on the DinD image (recent versions default to `DOCKER_TLS_CERTDIR` set) but the job isn't configured to trust the sidecar's generated certs, or is connecting on the wrong port (2375 unencrypted vs. 2376 TLS).
- The storage driver inside the DinD container defaults to `vfs` on some host kernels, which is correct but extremely slow and disk-hungry — this shows up as jobs timing out rather than erroring outright.
- Nested DinD (a DinD container itself running on a host that's already virtualized in an unusual way) hitting overlay filesystem incompatibilities.

**Diagnose**

```bash
docker inspect <dind-container> --format '{{.HostConfig.Privileged}}'
docker logs <dind-container> | grep -i "tls\|storage driver"
```

**Fix**

Run the sidecar privileged and either disable TLS explicitly for internal-network-only use, or configure the client side to use the generated certs:

```yaml
services:
  - name: docker:dind
    privileged: true
    env:
      DOCKER_TLS_CERTDIR: ""   # disables TLS — only do this on a trusted internal network
```

If disabling TLS isn't acceptable, mount the shared cert volume (`docker:dind` writes to `/certs/client`) into the job container and set `DOCKER_CERT_PATH`/`DOCKER_TLS_VERIFY` to match.

**Prevent it**

Where possible, prefer building images without full DinD — a rootless build tool (buildkit's `img`, Kaniko, or Buildah) avoids the privileged-container requirement entirely and sidesteps this whole category of failure.

---

## 10. Build cache issues — stale, corrupted, or ineffective caches

**Symptom**

A build passes locally but fails on the runner with errors that look like a dependency version mismatch, or a build that should take two minutes consistently takes twenty because the cache never seems to hit.

**Likely causes**

- The cache key includes something that changes every run (a timestamp, a random build ID) by accident, so it never matches a previous cache and silently rebuilds from scratch every time.
- A genuinely corrupted cache entry — a previous job was killed (OOM, timeout) mid-write, leaving a partial cache archive that later jobs load and choke on.
- Cache scoped too broadly, so two branches with incompatible dependency trees overwrite each other's cache and each sees the other's stale state.
- Local package manager caches (`node_modules`, `.m2`, `~/.cache/pip`) mixed with the CI cache mechanism, producing two caching layers fighting each other.

**Diagnose**

```bash
halyard job show <job-id> --cache-key
halyard job show <job-id> --cache-status   # hit / miss / corrupted
```

Compare the resolved cache key across two consecutive runs of the same branch — if they differ, that's the cache-key problem, not corruption.

**Fix**

- Fix the cache key to include only files that should invalidate it (a lockfile hash, not a timestamp):

  ```yaml
  cache:
    key: "{{ checksum 'package-lock.json' }}"
    paths: [node_modules]
  ```

- Clear a suspected-corrupted cache explicitly rather than guessing: `halyard cache clear --key <key>`.
- Scope cache keys per branch or per dependency-lockfile hash so unrelated branches stop overwriting each other.

**Prevent it**

Key caches off a checksum of the file that actually determines their contents (lockfile, `go.sum`, `Gemfile.lock`), never off anything time-based or branch-name-based alone.

---

## 11. Secrets and environment variables not available in the job

**Symptom**

A step that reads an expected environment variable gets an empty string instead, or authentication to a third-party service fails with what looks like a blank/missing credential rather than an invalid one.

**Likely causes**

- The secret is scoped to a different environment or branch than the one the job is running on (production secrets not exposed to a feature-branch job, by design, is the most common "is it broken" report that turns out to be working as intended).
- The variable name in `.halyard.yml` doesn't match the name it was stored under — case sensitivity trips people up here specifically.
- The secret is injected only into the top-level job but the actual command runs inside a nested container or a sub-shell that doesn't inherit the parent's environment.
- A masking/redaction feature is replacing the value with asterisks in logs, which people misread as the variable itself being wrong rather than just hidden from output.

**Diagnose**

```bash
halyard secrets list --scope <branch-or-env>
halyard job show <job-id> --env-keys   # names only, values are never shown
```

Confirm the secret is scoped to the branch/environment actually running, not just that it exists somewhere in the project.

**Fix**

- Re-scope or duplicate the secret to cover the branch/environment that needs it.
- Fix the name mismatch — copy the exact key from `halyard secrets list`, don't retype it.
- If a nested container is the issue, pass the variable through explicitly rather than assuming inheritance:

  ```yaml
  steps:
    - run: docker run -e API_KEY="$API_KEY" myimage
  ```

**Prevent it**

Name secrets consistently across environments (`API_KEY`, not `API_KEY_PROD` in one place and `PROD_API_KEY` in another) so a job config can move between environments without needing its variable references rewritten.

---

## 12. Job timeouts, hung builds, and flaky/non-deterministic failures

**Symptom**

```
Error: job exceeded maximum duration of 30m and was terminated
```

Or worse — no timeout error at all, the job just never finishes and has to be cancelled manually. Separately: a test suite that passes on most runs and fails on a small percentage with no code change in between.

**Likely causes**

*Timeouts / hangs:*
- A process waiting on interactive input it will never receive (a package manager prompting to confirm, a git operation waiting for a passphrase) — this hangs forever rather than failing fast.
- A test or service waiting on a network resource that's unreachable from the runner (an external API, a database that isn't actually up yet) with no request timeout configured on the client side.
- A genuinely slow step that used to fit inside the timeout and has grown past it as the codebase grew.

*Flaky tests:*
- Tests sharing mutable state (a database, a port, a temp file) and running in parallel, so ordering affects the outcome.
- Fixed `sleep()` calls standing in for a real readiness check, timing out under load on a busy shared runner even though they pass on a quiet one.
- Test execution order not fixed, so a test that depends on another test's side effect passes only when the suite happens to run in the lucky order.

**Diagnose**

```bash
halyard job logs <job-id> --raw | tail -100    # what was it doing right before it died
halyard job show <job-id> --duration-history   # is this timeout new, or has it crept up over time
```

For flaky tests, re-run the specific failing test in isolation several times — a test that fails alone at the same rate as in the suite points to the test itself; a test that only fails inside the full suite points to shared state or ordering.

**Fix**

- Add explicit non-interactive flags to anything that can prompt (`-y`, `--non-interactive`, `CI=true` where the tool supports it).
- Set explicit, generous-but-finite timeouts on every network call inside the job, so a hang becomes a fast, legible failure instead of an opaque one.
- Raise the job-level timeout if the work genuinely grew, but treat that as a last resort, not the first fix.
- For flaky tests, isolate shared resources per test (random ports, per-test database schemas or containers) and replace `sleep()` with a real readiness poll.

**Prevent it**

Track duration and flake-rate per job over time, not just pass/fail — a job that's crept from 12 minutes to 28 minutes over a quarter is a much cheaper problem to catch early than after it starts timing out under normal load.

---

## 13. Artifact upload and download failures

**Symptom**

```
Error: failed to upload artifact "dist/": connection reset by peer
```

```
Error: artifact "build-output" not found for job <id>
```

**Likely causes**

- The artifact exceeds a size limit (either Halyard's own limit or the underlying object storage's per-request limit), and the failure surfaces as a generic connection error instead of a clear "too large" message.
- Network interruption mid-upload on a large artifact with no retry configured.
- A path in the artifact glob that doesn't actually exist at upload time (build step produced output somewhere else, or failed silently before producing it) — this fails as "not found" on download, which looks like a storage bug but is actually an upstream step problem.
- Artifact retention already expired by the time something tries to download it.

**Diagnose**

```bash
halyard job show <job-id> --artifacts     # what was actually captured, and its size
du -sh dist/                              # compare against what the job expected to upload
```

**Fix**

- If size is the issue, compress before upload (`tar.gz` the directory) rather than uploading many small files individually — this also reduces the connection-reset risk on flaky networks.
- Confirm the artifact path glob actually matches what the build step produces; a renamed output directory after a build-tool upgrade is a common silent cause.
- Add retry-on-upload if your job definition supports it; a single network blip shouldn't fail the whole job.

**Prevent it**

Treat "artifact exists and is non-empty" as an explicit assertion in the job itself, right after the step that's supposed to produce it, rather than discovering it's missing only when a later job tries to download it.

---

## 14. Runner/agent version mismatch and upgrade issues

**Symptom**

```
Error: runner agent version 3.8.2 is incompatible with server API version 4.0
```

Jobs that used a feature introduced in `.halyard.yml` schema v2 fail to parse, or succeed but silently ignore the new field, on older runners.

**Likely causes**

- Runners not auto-updated, left behind after the control plane upgrades (this is the expected failure mode right around a major version bump like 4.0).
- Mixed fleet — some runners updated, some not — causing jobs to behave differently depending on which runner happens to pick them up, which looks like flakiness until someone checks runner versions.
- A job config using a new schema feature without a `min_agent_version` guard, so it silently degrades instead of failing clearly on old runners.

**Diagnose**

```bash
halyard runners list --columns name,version,status
halyard-agent version
```

**Fix**

```bash
sudo halyard-agent self-update
# or, for a pinned/controlled rollout:
sudo halyard-agent self-update --version 4.0.1
```

For a fleet, update runners in small batches rather than all at once, so a bad agent build only affects a fraction of capacity while you confirm it's healthy.

**Prevent it**

Enable auto-update on runners unless you have a specific reason to pin versions (regulated environments, air-gapped hosts). Before a major version launch, audit fleet versions ahead of time rather than discovering the mismatch from job failures on launch day.

---

*Reviewer note for the whole section: every exit code, log line, config key, and CLI command above reflects common patterns across self-hosted CI tools and Docker itself, not a confirmed Halyard string. Before publishing, grep the actual `halyard-agent` and `halyard` CLI source (or run each scenario against a live 4.0 runner) and swap in the real strings — that's a faster and more reliable pass than trying to reconstruct them from a shared support inbox after the fact. Once telemetry or a ticket tagging system exists, revisit this section using actual frequency data instead of the "common in the ecosystem" ordering used here.*