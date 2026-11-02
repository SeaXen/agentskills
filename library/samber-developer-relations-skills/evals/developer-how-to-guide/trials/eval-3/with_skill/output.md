# Layout: "Deploy a worker" (Corvelle)

I read the skill and its three references. I haven't run or invented any Corvelle commands. This is the layout, not the finished pages.

**Verdict: this can't be one page.** Kubernetes and VM have different prerequisites, different steps and different verification. The skill's split test says to separate pages in that case. Forcing them into tabs would make the page wrong for whichever tab a reader isn't on.

## Goal sentence (internal, not on the page)

A backend engineer with a Corvelle account and a queue wants a worker running and processing jobs from that queue, on their Kubernetes cluster or a single Linux VM.

## Page set

| # | Page | Shape | Ships |
|---|---|---|---|
| 1 | Deploy a worker on Kubernetes | Full how-to | Yes |
| 2 | Deploy a worker on a VM | Full how-to | Yes |
| 3 | Create a worker with Terraform | Separate how-to, linked from the "create the worker" step | Only if a team owns it |
| 4 | Deploy a worker (index) | Links only: two cards, no steps | Optional |

The "create the worker" step (dashboard, five clicks) is identical on pages 1 and 2. Use a docs-site include if the site supports one, so it is maintained once.

## How each variant is handled

| Variant | Shape | Why |
|---|---|---|
| Kubernetes vs. VM | Separate pages with a shared title stem | Prerequisites and verification differ. |
| Python / Node / Go | Tabs, using your synced switcher, on every step where syntax differs | Same steps, different syntax. |
| Dashboard vs. Terraform | Dashboard on pages 1 and 2; Terraform is its own page | Terraform needs state, a provider block and a plan/apply loop. The steps don't map one-to-one. |
| EU vs. US | One inline conditional: "If your account is in the EU region, add `--region eu`." | It is a single flag. |
| Windows (about 3%) | One out-of-scope line, or a link if a Windows page exists | The VM page assumes Linux with systemd. |
| Bare metal, no container runtime | Delete the steps. Keep one line: "Bare-metal hosts without a container runtime aren't supported." | It is unsupported. |

**Bare metal does not go under "Advanced".** The skill says a parked branch silently becomes scope: readers follow it and file tickets. Put the "not supported, here's why" answer in your FAQ or troubleshooting docs, where customers asking about it will find it. Link to that answer from the out-of-scope line.

**Tabs are not free.** Two hosting pages times three languages is six runs per release. The synced switcher makes authoring cheap but not testing.

## Page 1: Deploy a worker on Kubernetes

Front matter: `owner`, `tested_with`, `last_verified`, all `UNVERIFIED` until filled.

**Goal line:** "Run a Corvelle worker on your Kubernetes cluster so it picks up jobs from your queue." Add how long it takes and that it starts consuming real jobs.

**Prerequisites** (each one has a check command or a link):
- Corvelle account and an existing queue. Link to the pages that create them. Don't re-teach them.
- Use a test queue, not a production one, because a running worker consumes real jobs. Give the check that proves which kind the queue is.
- A cluster, with a check that `kubectl` reaches it.
- Permission to create a namespace.
- Helm, with a version floor and a check.
- Name any billable resource the guide creates.
- Wrong-page cue: "Running on a single VM? See [Deploy a worker on a VM]."

**Steps** (about 6, under the 10-step ceiling):
1. Create the worker in the dashboard (include). Copy its token. Say where the token is shown.
2. Create the namespace. Safe to re-run.
3. Store the token as a Kubernetes Secret. Use a no-echo prompt or stdin. Never put the token in a command line.
4. Provide the worker code. **Tabs: Python / Node / Go.** Whether this step exists depends on open question 1.
5. Install the Helm chart. Use an idempotent command (`upgrade --install`). Add the inline EU conditional.
6. Optional: anything not required for the goal.

**Verify the result.** Two checks:
- `kubectl get pods` shows the pod running. Give the expected output.
- A second, independent check that Corvelle sees the worker: it shows as connected in the dashboard. Then enqueue one test job and show it completing.

`kubectl get pods` alone proves the process is up, not that it reached Corvelle. A crash-looping or misauthenticated worker can still look fine for a few seconds.

**Roll back.** Open with the signal: pod in `CrashLoopBackOff`, or jobs failing. Then use Helm's own history or uninstall.

**Clean up.** Delete the namespace and the dashboard worker, and only after the reader has decided not to roll back.

**Next steps.** Three links: scale or configure workers (reference), Terraform page, troubleshooting.

## Page 2: Deploy a worker on a VM

Same skeleton, with these differences.

**Prerequisites:**
- A Linux VM with systemd and SSH access, with a check command.
- The runtime for the chosen language.
- Permission to write a unit file (sudo).
- Wrong-page cue back to the Kubernetes page.
- Windows out-of-scope line.

**Steps** (about 6):
1. Create the worker in the dashboard (include).
2. Install the SDK and runtime. **Tabs: Python / Node / Go.**
3. Write the token to a root-only environment file using a no-echo prompt.
4. Write the systemd unit. **Tabs**, because `ExecStart` differs by language.
5. Reload systemd and run `enable --now`. Safe to re-run.
6. EU inline conditional, in whichever step takes the flag.

**Verify the result.** `systemctl status` shows `active (running)`, then the same dashboard "connected" check and test job as page 1.

**Roll back.** `stop`, `disable`, remove the unit file.

## Page 3: Create a worker with Terraform

Write it only if a team will own it. The skill says an extra page with no owner is a page nobody keeps true. If no team owns it, ship pages 1 and 2 and add one line: "To create the worker with Terraform, see [UNVERIFIED-LINK: Create a worker with Terraform]."

Outline when it is written:
- **Prerequisites:** state backend, provider version floor, credentials loaded without echoing.
- **Steps:** provider block, resource, `plan`, review, then `apply` of the saved plan file. Never `-auto-approve`.
- **Verify:** the resource appears in the dashboard.
- **Roll back:** `terraform destroy` after a plan review.

## Mismatches to resolve (please answer these)

1. **VM vs. bare metal.** Your VM path is a systemd unit. Does it run a container? If it runs the worker as a plain process, that is already "no container runtime", and the bare-metal exclusion contradicts it. What exactly is unsupported: physical hosts, or hosts with no Docker/containerd?
2. **Verification is weaker than you described.** `kubectl get pods` and `systemctl status` prove the process is running, not that it connects to Corvelle. I'd add the dashboard check and test job. Does the dashboard show worker connection status? If not, that is a product gap to report.
3. **Where does the Kubernetes worker code come from?** Does the Helm chart run a prebuilt image that your SDK code plugs into, or does the reader build their own image per language? That decides whether step 4 exists and what the language tabs contain.
4. **Which command takes `--region eu`?** I assumed worker creation or the CLI. If it also changes the Helm values or the SDK endpoint, the conditional appears in more than one place.
5. **Windows.** Is it supported anywhere, or is it only that 3% of readers happen to have Windows hosts?
6. **Production safety.** Is there a test mode or test queue? If the reader's queue is production, a new worker starts consuming real jobs.

## Hand-over (what is not done)

**Required by the skill:**
- **Interview questions I couldn't ask:** 3, 5 and 7 are mandatory in the skill, and the first six mismatches above cover 3 and 5. I assumed the reader is a backend engineer, that the queue is a test queue, and that there is no test mode. I still need an owner team and a cold-run tester (question 7).
- **Run list:**
  - Environment: a disposable Corvelle account with a test queue.
  - Hosting: one cluster and one Linux VM.
  - Variants: 2 hosts × 3 languages = 6 cells, plus one EU and one US run.
  - Also run: the safe-to-re-run steps and the roll back section.
- **Not shippable yet:** every command, output and link is still `UNVERIFIED`. The skill says a page with a marker doesn't ship.
- **Stamps:** `owner`, `tested_with` and `last_verified` are blank.

**Maintenance and measurement:**
- **Docs CI:** you have a synced tab switcher but I don't know if you have docs CI. If yes, run the executable steps against the released product on a schedule.
- **KPIs to wire first:** executable steps passing in CI, then tickets that cite these pages.

If you answer the six mismatches and name an owner, I can draft pages 1 and 2 in full with `UNVERIFIED` markers where I haven't seen real output.