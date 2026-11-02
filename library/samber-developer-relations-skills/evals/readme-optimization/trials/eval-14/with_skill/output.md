No repo access here (`ambervale/dtx` isn't a path I can read or run commands in), so this is the plan, not a scored audit — Band A2/install-check and A3/claim-check need you to run the real commands and paste output before you trust them.

**Assumed, flag if wrong:** solo/infra-engineer audience deciding alone, no hard launch date, week = your ceiling not a deadline. Wrong audience → add Step 8 enterprise signals later, but not this week regardless. Wrong differentiation set → tell me the real alternatives (Q7), template below needs them.

## Where the week goes

**Day 1 — near-zero-effort stuff, all currently missing (~2h total)**
1. **Repo description** — one sentence, same wording as README opening line once drafted.
2. **Topics** — `terraform`, `terraform-plan`, `cli`, `devops`, `infrastructure-as-code`, `diff`.
3. **Website field** — point at docs if any exist, else leave blank, don't fake one.
4. **Status line in README** — honest one-liner (21.4% of repos bother — cheap differentiator on its own). Template: "dtx is used daily by the author. [X] is stable, [Y] is not built yet." Fill X/Y yourself, don't let me guess.
5. Start install-path check (see Verify, below) — run it now, fixes feed Day 5.

**Days 2–4 — the actual spend: the terminal demo**

Output *is* the product, so this is where the week's real budget goes, ranked above badges, funnel order, everything except the two blocking checks above.

1. Pick one real diff scenario — a plan with an add, a change, and a destroy, so all three colour states show.
2. Script it with **VHS** (`.tape` file), not a hand-recorded GIF — diffable, re-renders in seconds when output changes, doesn't rot into a stale screenshot.
3. Render to GIF/cast, keep it short and legible at embed scale.
4. Grab one static frame at ~1280×640 from the same render — that's your **social preview image**, free, same asset. Fixes the "still default social preview" gap at zero extra cost.
5. Place the demo second in the README, right under the one-liner, per the CLI skeleton (below) — before install, before differentiation.

**Day 5 — assemble and cap it**
1. **Differentiation paragraph** (B1, only 25.7% of repos have any — your highest-leverage prose): name the real alternative — raw `terraform plan` text, or Atlantis/CI diff comments, or terraform-visual/tfcmt — and say what dtx doesn't need (no CI wiring, single binary, runs on the two plan files you already have). Fill in real axis, don't ship "simple and fast."
2. **Badge row**, capped at 4: version, licence, supported OS, terraform-version compatibility. Skip build status, coverage, "PRs welcome" — none of those answer a reader's question.
3. Reorder into the CLI skeleton: name+one-liner → demo → why-over-incumbent → install (package manager one-liners first) → 3–4 common invocations → config (link the rest) → status → licence.
4. Move CONTRIBUTING/CHANGELOG/SECURITY content out to their own files, one-line pointers only.
5. Re-score, run the cold-reader test.

**Explicitly cut, not deferred:** foundation/governance/named-adopters signals (Step 8) — week can't afford them and audience doesn't call for them. Hand-written table of contents — host generates one. Community-health prose inline — link only.

## Verify before you ship (blocking, do this yourself)

1. Fresh shell/container, no prior state. Run the documented install command exactly as written.
2. Run the first usage example exactly as written. Note any undocumented prerequisite (Terraform version, OS package, env var).
3. Grep every flag/env var/config key the README documents against the actual CLI arg parser. A flag in the README that isn't in the parser is a hallucination, not a typo — cut it.
4. Any performance or "handles N resources" claim needs a source in-repo (benchmark, changelog) or it comes out.
5. Run `scripts/readme-audit.sh <repo-root>` from this skill for the mechanical facts (section count, words-before-first-command, badge count, broken relative links).

## Opening line — pick one

1. Mechanical: "dtx diffs two Terraform plan files and prints a colour-coded, resource-by-resource drift report in your terminal."
2. Problem removed (recommended — names the job, pairs with the demo right under it): "dtx turns a wall of `terraform plan` text into a diff you can actually read before you approve it."
3. What it replaces: "dtx replaces scrolling raw `terraform plan` output line by line to spot what changed."

## After ship

Track support-load (install/what-does-this-do issues per month, near-free) and clone-to-visitor conversion (an hour to pull from traffic insights, re-measure 4–6 weeks out). Drop stars — monotonic, can't show a regression, will lie to you about whether the furniture fixes worked.

Next: give me the real alternatives (Q7) and the real status (Q6) so the two templates above stop being placeholders.