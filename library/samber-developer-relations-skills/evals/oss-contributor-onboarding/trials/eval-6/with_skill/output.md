## Verdict: Not yet — you're buying the wrong layer first

The two symptoms you named — `psycopg2 build failed`, "which Python version?" — are both **technical hurdles** in Steinmacher's newcomer-barrier taxonomy, and specifically a **Step 3 (environment) problem**: nothing written down pins the Python version or the Postgres client headers `psycopg2` needs to compile, so every contributor's setup outcome depends on whatever happens to already be on their machine.

That is exactly the failure a container definition removes, and you're closer to already having one than you think.

### The fact that changes the order: CI already runs in Docker

Per the skill's own re-ranking rule: *"a team already running containers in CI has paid that tier's effort, which moves it to the top of the efficiency line for that project alone."* You've paid the hard part already — a working image with `libpq`/`psycopg2` build deps and a pinned Python version exists in your CI config right now. Turning that into a `.devcontainer/devcontainer.json` that points at the same Dockerfile (or a thin variant of it) is close to free. That single file fixes both stated symptoms directly: pinned interpreter kills "which Python version," pinned system packages kill the `psycopg2` build failure.

Codespaces is not required to get that fix. It's required to *host* that fix in the cloud.

### Why the purchase should come second, not first

The skill is explicit on sequencing: **adopt the container definition before adopting any hosted workspace vendor.** `.devcontainer/` is portable across VS Code Dev Containers, Codespaces, Gitpod, and DevPod; the vendor relationship is not. Buy the seats before the config exists and you've bought a hosting bill for a setup you haven't proven works — and you'd be locking contributor docs to Codespaces specifically, which is the exact mistake Gitpod's 2024 self-hosted shutdown made painful for projects that had baked its name into their CONTRIBUTING file.

### About the numbers on that page

3–5 minutes → 10–30 seconds, one-to-two-weeks → near-instant: these are **vendor-published marketing figures with no peer-reviewed measurement behind them.** Not false, necessarily — just not evidence. Don't let them anchor the budget conversation; anchor it on your own cold-run time instead (see below).

### Three things to settle before spending the approved budget on seats

1. **Who pays for compute.** This is the one point in Codespaces' favor here: you're corporate-backed, so an org-billed plan is realistic, unlike a volunteer project where free-tier caps would just relocate the friction onto new contributors.
2. **Portability before hosting.** Write the devcontainer config first. Codespaces becomes one of several ways to consume it, not the thing itself — so if you ever need to leave the vendor, contributor docs don't need a rewrite.
3. **Drift.** A cloud environment your own 6 maintainers don't use in their daily work will bit-rot silently, and the next contributor pays for that in a fresh support thread. If you buy seats, your maintainers need to actually develop in Codespaces sometimes, not just tell newcomers to.

### Recommended sequence

1. Write `.devcontainer/devcontainer.json` reusing your existing CI Docker image/definition.
2. **Cold-run it** — fresh container, no warm caches, only the README/CONTRIBUTING steps, timed to first passing test. Don't take "should fix it" on faith; that's the whole point of the cold-run protocol. This also gives you a real before/after number instead of the vendor's number.
3. Once the cold run passes clean, the config is portable — Codespaces, Gitpod, DevPod, or a contributor's own machine all consume the same file.
4. *Then* decide on seats, sized to actual usage (how many external contributors per quarter are you really onboarding — four a quarter doesn't need a seat budget built for forty).
5. Keep local setup documented as a first-class path regardless — for contributors with poor connectivity to whichever region you host in, and as the fallback if you ever drop the vendor.

**Bottom line:** the approved budget isn't wasted, it's just aimed one step too early. Ship the `.devcontainer/` config against your existing CI image, cold-run it to confirm it actually kills the `psycopg2` and Python-version reports, then spend the seats on hosting a fix you've already proven — not on hoping the fix arrives with the invoice.