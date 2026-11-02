# Decision: write 2 now, 1 conditional, 1 cheap fold-in, 1 reject

| # | Cluster | Verdict | Why |
|---|---|---|---|
| 2 | exit code 137 | ✅ **Write now, top priority** | 4,100 error events + 61 tickets/quarter is real support cost; zero content gap risk — we own the root cause |
| 4 | cache key not restored | ✅ **Write now** | 900 searches, incumbent is a dead 2023 thread about a version we don't ship — pure content gap, cheap win |
| 3 | venv activate not found | 🟡 **Confirm root cause first, then write** | Only worth writing if it's a runner-specific defect, not generic Python |
| 5 | secrets rotation | 🟡 **Fold into next sprint, low priority** | Low volume, but half the content already exists in the README — cheap to finish |
| 1 | on-prem pricing calculator | ❌ **Not a docs task — reject as scoped** | Building a calculator conflicts with a quote-only sales motion; low volume doesn't justify the build |

Reasoning below, then the writer brief for each "write" item.

---

## Why reject #1 (pricing calculator)

82 searches/90d (~27/month) doesn't justify building an interactive tool — that's an engineering + design project, not a docs page. More importantly: **quote-only pricing is usually a deliberate sales-qualification gate.** A self-serve calculator would leak pricing logic and could undercut sales conversations on enterprise deals — that's a pricing-strategy call, not something a docs writer should decide unilaterally.

If you still want to capture that search intent: brief a **static explainer page** instead — "How Glasswing on-prem pricing works" (factors considered: node count, support tier, deployment model) ending in a "Request a quote" CTA. No calculator, no exposed numbers. But get sign-off from whoever owns pricing/sales strategy before publishing — this touches how pricing is communicated externally, which is above a docs-only decision.

---

## Brief: exit code 137 (write first)

**Title:** "Exit code 137 in Glasswing: why your job was OOM-killed"
**Target query:** exact error text + "glasswing exit code 137" (problem/error query — highest-intent SEO category)
**Doc type:** troubleshooting how-to

**Structure:**
- **What:** Exit 137 = SIGKILL, almost always the OS OOM killer terminating the container.
- **Why:** explain the container hit its memory limit; Glasswing currently only reports "job failed" (name this honestly — don't hide the gap).
- **How:** steps to diagnose (check job memory usage, common causes — leaky process, undersized limit, wrong image), steps to fix (raise the memory limit, how to set it, how to profile actual usage before raising blindly).
- **Next:** link to resource-limits reference, link to support if still stuck.

**Do not write it around the current vague message.** 5.1 will print the actual memory limit — write the explanation and fix steps to be evergreen (they don't depend on message wording), and add one line: "Newer Glasswing versions surface the memory limit directly in this error." That way the page doesn't go stale the day 5.1 ships, and doesn't need a rewrite — just a one-line edit.

**Get from engineering:** confirmation that 137 is *always* OOM in our runner (never another SIGKILL source), and the exact config key/flag for setting memory limits.
**Success metric:** ticket volume for this error, quarter over quarter.

---

## Brief: cache key not restored (write second)

**Title:** "Why your cache key isn't restoring in Glasswing"
**Target query:** "glasswing cache key not restored" — write the title to directly out-rank the 2023 forum thread; be explicit this covers the current version.
**Doc type:** troubleshooting how-to

**Structure:**
- **What:** one sentence — cache miss vs cache key mismatch are different problems, name both.
- **Why:** matters because it silently slows builds; not an error, just failed acceleration.
- **How:** current key syntax, restore-keys fallback behavior, common misconfigurations (key includes a value that changes every run, branch-scoping mismatch, path mismatch between save and restore steps).
- **Next:** link to caching reference page, link to CI performance guide if one exists.

**Explicitly note the version this applies to** near the top — that's the exact gap the stale 2023 thread leaves open, and the reason we're citable over it.
**Get from engineering:** current cache backend behavior/version, confirm nothing changed recently that the old thread would mislead people about.
**Success metric:** this page ranking above the 2023 thread within ~60–90 days; docs-search-to-resolution (no follow-up ticket).

---

## Brief: venv activate not found (confirm, then write)

**Before writing anything**, get one answer from engineering/support: **is this caused by something in our runner image** (missing `python3-venv` package, ephemeral filesystem wiping a venv between steps, working-directory assumptions), or is it just generic Python behavior unrelated to Glasswing?

- If runner-specific → write it, title exactly matching the error text, structure as a targeted fix ("add this to your runner setup step" / "our default image needs X"). Check whether it's actually downstream of cluster 4 (cache restore failing to restore a cached venv) — if so, cross-link or merge.
- If generic → **don't write it.** We can't out-rank Python's own docs/Stack Overflow with no unique angle, and 1,200 impressions with people still hitting it inside our runners is a signal to fix the runner image, not to document around it.

Don't assign this to the writer until that root-cause answer exists — otherwise you risk a page with no differentiation.

---

## Brief: secrets rotation (cheap fold-in)

Low volume (140/90d) doesn't earn a priority slot on its own, but the README is already half-written — assign as a quick task, not a new research project.

**Action:** ask the writer to diff the README against what a full "How to rotate secrets in Glasswing" page needs (probably: rotation without downtime, rotation for in-flight jobs, verifying old secret is fully retired). Get the missing half from whoever wrote the README or from support tickets that reference secrets rotation.
**Doc type:** how-to, promote from README into a proper docs page once complete.
**Success metric:** none tracked closely given low volume — do it because it's cheap, not because it moves a number.

---

## Standing instructions for the writer (all pages above)

- One page per task — don't combine exit-137 and cache-restore into one "troubleshooting" mega-page.
- Lead with the error text or exact problem as the H1 — that's what search intent matches on.
- No wall of text: code/config blocks before prose explanation, not after.
- State prerequisites (version, config context) at the top, not mid-page.
- Every page ends with a next step (reference link or support link), not a dead end.