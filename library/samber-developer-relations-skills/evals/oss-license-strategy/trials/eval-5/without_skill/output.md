# Finchgate → FSL: Migration Plan

## Before drafting anything: three answers that determine whether FSL even helps

**1. Did the Polish competitor fork Finchgate's code, or build their own?**
A source license restricts what people can do *with your code*. It grants zero protection against someone writing an independent implementation of "a database migration CLI." If their tool doesn't contain your code, relicensing changes nothing about that threat — you'd be adding friction to your own distribution for a problem the license can't touch. Diff their binary/behavior against yours before proceeding. If it's independent, the real levers are trademark, execution speed, and the team-plan feature gap — not licensing.

**2. Is the $400/mo team plan gated inside the same brew-installed binary, or a separate component?**
This decides the entire shape of the plan. If team features live in a separate server/dashboard/API that the CLI talks to, you can protect *that* and leave the CLI untouched. If the team plan is literally the same binary with a license key unlocking flags, there is no way to FSL "the product" without FSL-ing the exact artifact your growth funnel depends on.

**3. Is Finchgate in `homebrew-core` today, or already on a custom tap?**
Homebrew's core repo has historically required an OSI-approved (or public-domain-equivalent) license; FSL is deliberately not OSI-approved (Sentry markets it as "source-available"/"fair source," never as open source). If you're in core, moving the installed artifact to FSL is very likely a formula eviction, not a formula edit. That forces every one of your 9,000 weekly installs through `brew tap finchgate/tap && brew install finchgate` instead of `brew install finchgate` — real, measurable install friction, on the one channel that currently feeds your entire pipeline with zero sales cost. Verify Homebrew's current policy text yourself before committing; this is the single fact most likely to sink the plan if you get it wrong.

⚠️ Answer these before Stage 0. They're cheap to check and expensive to skip.

## What FSL actually is, precisely

- **Not retroactive.** Every version already released under your current license stays under that license forever, for everyone who has it, including a competitor who already grabbed it. FSL only governs *future* releases.
- **Not open source.** OSI doesn't recognize it. Sentry and the fair.io group call the category "fair source" on purpose — say that in public, don't call it open source, or you'll get corrected loudly and correctly.
- **Restricts one thing: "Competing Use."** Roughly: offering the software (or a derivative) to third parties as a hosted/embedded substitute for your own paid product. Internal use, non-competing commercial use, and personal use stay free even during the restricted period.
- **Self-expiring, per version.** Each release converts automatically to a permissive license (you pick MIT or Apache-2.0 up front) after a fixed "Change Date" — Sentry's own standard, and the one nearly every adopter uses, is 2 years from that version's release. It's a rolling window, not a cliff.
- **Simpler than BSL on purpose.** BSL (HashiCorp, CockroachDB, MariaDB) lets each adopter write a custom "Additional Use Grant," which is exactly what made it legally murky and community-hostile. FSL is a fixed template — less flexible, more predictable, easier to defend in public.

## The precedent you're citing, more precisely than "Sentry did it"

Sentry didn't FSL everything. They put FSL on `getsentry/sentry` — the server product a cloud vendor could host and resell against them — and kept their SDKs and smaller tools on permissive licenses, because those are the adoption/distribution surface, not the competitive moat. That split is the actual lesson, not "relicense the repo."

Also worth sitting with before you commit:
- **HashiCorp → BSL (2023)** produced the OpenTofu fork within weeks, backed by the Linux Foundation, forked from the last MPL commit — and package ecosystems now happily distribute *that* instead. The permissively-licensed history didn't disappear; someone else picked it up and kept competing with HashiCorp using HashiCorp's own old code.
- **Elastic → SSPL (2021)** produced AWS's OpenSearch fork; Elastic partially reversed course in 2024 back to AGPL for some products after concluding the trust cost wasn't worth it.
- **Redis → dual-license (2024)** produced the Valkey fork, backed by AWS, Google, and Oracle, now shipping through the same distro channels Redis used to own alone.

Pattern: a relicense doesn't remove your permissively-licensed code from the world. It creates a fork event, and forks are exactly what eat your package-manager presence if the fork is the one that stays OSI-clean. If Finchgate has any real community around it, model for "a fork appears" as a likely outcome, not a tail risk.

## Recommended shape: open-core, not blanket relicense

Given the diagnostics above will very likely show "team plan ≠ pure CLI" and "brew install = growth engine you can't afford to break":

- **Keep the CLI — parsing, diffing, drivers, `brew install finchgate` — exactly as licensed today.** This is your top-of-funnel. Don't touch it.
- **FSL only the code that constitutes the paid product**: hosted dashboard, team collaboration server, SSO/audit, license-gating backend — whatever actually justifies $400/mo. If that code already lives in a separate repo, this is a clean cut. If it's tangled into the CLI binary, untangling it is a prerequisite, not a step you can skip.
- This gets you the actual thing you want — nobody clones your paid product and resells it — without putting your acquisition channel at risk for a threat it can't even address.

If diagnostic #2 comes back "there is no separate component, the team plan is a license key on the same binary," say so explicitly to your leadership before proceeding: FSL-ing the CLI in that scenario trades a real, working growth channel for protection against a threat (independent competitor) the license doesn't stop.

## Staged plan, assuming the open-core split applies

**Stage 0 — Diagnose (1–2 weeks)**
- Confirm brew distribution path (core vs. tap) and exact formula source.
- Confirm the code split between CLI-core and team-plan surface; if tangled, scope the untangling work first.
- Diff the competitor's product against Finchgate's source to settle fork-vs-independent.
- `git shortlog -s -n` on the paid-product repo/paths to inventory every external contributor and how much of the code they own.
- Confirm current LICENSE file is actually a permissive license you have the right to move away from.

**Stage 1 — Legal scope (2–4 weeks)**
- Get real counsel to review the FSL text against Finchgate's actual product — "Competing Use" needs to match what you're actually worried about, and this is a real contract, not boilerplate to copy-paste.
- Pick the fallback license (MIT or Apache-2.0) and Change Date (2 years, absent a specific reason otherwise).

**Stage 2 — Contributor consent (2–6 weeks, blocking)**
- FSL isn't OSI-approved, so relicensing any file with outside contributions needs affirmative consent from each contributor — silence isn't consent, and you can't paper over this later.
- No CLA/DCO history today likely makes this the longest step: contact every contributor with non-trivial contributions to the paid-product paths, track sign-off explicitly, and either rewrite or permanently exclude any file where consent doesn't land.
- Add a CLA/DCO gate on future PRs to the FSL-covered repo so this doesn't recur.

**Stage 3 — Cut line (1 week)**
- Tag the last fully-permissive commit of the paid-product repo (e.g. `last-mit`) — a permanent, public marker of exactly what stays free forever.
- Replace the **LICENSE** file and per-file headers in the paid-product repo/paths only; leave the CLI-core **LICENSE** untouched.

**Stage 4 — Packaging (1–2 weeks)**
- Re-verify the Homebrew formula only ever points at the still-permissive CLI artifact.
- Check every other distribution surface with its own license gate (Linux distro packages, language package registries) for the paid-product component specifically — most won't carry it at all once it's FSL, which is fine, since it was never meant to be `pip install`-able.
- Fix every "License: MIT" claim across README, website, and registries that's now only true for part of the codebase.

**Stage 5 — Communicate on launch day**
- One plain-language post: what changed, what didn't, and an explicit, quotable promise that `brew install finchgate` stays exactly as free and exactly as licensed as it is today.
- Call it "source-available" or "fair source," never "open source" — you will be corrected publicly and immediately if you don't, and the correction will dominate the conversation more than the change itself.
- Expect the two standard threads (HN/Reddit): "is this still open source" and "will old versions be restricted retroactively." Have both answers ready before launch, not while reading the comments live.

**Stage 6 — Set a rollback trigger now, not after**
- Define failure upfront: sustained brew-install drop past some threshold, a credible fork gaining real traction, or team-plan conversion rate unchanged 90 days out (which would mean licensing was never the actual lever on your revenue). Review against baseline at 90 days before treating this as permanent.

## Bottom line

FSL is the right tool only if the thing you're protecting is separable from the thing driving your 9,000 weekly installs, and only if the competitor is actually running your code, not their own. Nail down those two facts first — everything above the diagnostics stage is expensive and hard to reverse (contributor consent, a possible fork, a possible Homebrew eviction), and none of it is worth starting until you know it's aimed at the real threat.