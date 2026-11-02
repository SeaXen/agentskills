# Licensing decision — Finchgate

Below is the full decision record, built the way `oss-license-strategy` builds one: constraints first, postures argued before any license is named, the license and contribution policy picked only inside the chosen posture, then the actual migration steps. I skipped the live interview since you asked for the finished deliverable — the facts I inferred are flagged as assumptions below. Two of them are load-bearing enough that I'd normally stop and ask before writing another line; challenge either one and the recommendation changes.

**This is not legal advice.** Whether your current license already lets you relicense, whether the Polish competitor's product actually contains your code, and what a fork could legally call itself are all counsel questions, not licensing-strategy questions. I've marked each one below.

## The reality check, before anything else

"Move to FSL so nobody can build a business on our work" assumes the license is what's letting them build it. It usually isn't. FSL, like AGPL, restricts what someone may do **with your copyrighted code** — fork it, embed it, resell it as a service. It has no power at all over someone who read your docs, watched your CLI's UX, and wrote their own implementation. If the Polish competitor cloned the *idea* — a similar CLI, similar commands, similar migration model — a license change does nothing to them. It only bites someone who copies your actual source.

So the first question, and it's the one that decides everything else: **did they fork or vendor Finchgate's code, or did they build an independent tool that competes on features?** If you don't know, that's worth finding out before a license change — a support ticket with a suspiciously familiar error message, a binary that reverse-engineers to your code, a changelog that mirrors yours too closely. If it's the latter (independent build), what you're actually reacting to is competition, and no license fixes that. This is the same trap the skill's reference material calls out for AGPL: *"it obliges a network operator to publish source; it does not stop a well-resourced competitor who complies."* FSL's protection is exactly as narrow.

If it *is* copied code, you may have a copyright infringement claim right now, under whatever license you already ship — that's a counsel conversation this week, not a license migration over the next quarter.

## Assumptions (confirm before executing)

1. **Current license is permissive and OSI-approved** (MIT/Apache-2.0/BSD) — inferred from "individual developers install it themselves... nobody goes through procurement." A copyleft or already-restrictive license would change this whole analysis. Check the actual `LICENSE` file before doing anything else.
2. **The $400/month team plan is a separate coordination layer** (shared migration history, CI integration, remote locking, audit trail, SSO — something like this), not a license-key flag that unlocks code already compiled into the CLI binary. This is the single most important fact you haven't told me, and it determines whether you have a real reuse problem or not. I give you both branches below.
3. Finchgate has outside contributors beyond your own team (typical for a project popular enough to worry a competitor), and there's no CLA on file today — also typical for a project that "individual developers install, nobody goes through procurement."

## Constraints (Step 1)

- **Dependency audit — unrun.** Enumerate every shipped dependency's license (build/test-only deps don't count, only what's in the binary). If anything copyleft is in there today, it already forecloses some outbound options — check before, not after, you announce a change.
- **Contributor consent — the hard blocker for any relicense.** Every copyright holder whose code is still present in the repo must consent, unless a CLA already granted you that right. Pull `git shortlog -sne` and see how long that list is. No CLA on file today (per assumption 3) means this is a real, possibly multi-week task, not a checkbox — Mozilla's Firefox relicense took 2001–2006 for exactly this reason.
- **Homebrew is your distribution channel and the thing your entire top of funnel depends on.** Homebrew's core-formula policy has historically restricted non-open-source software, and FSL is explicitly *not* OSI-approved. Verify this against Homebrew's current acceptable-formulae policy before you commit to anything — if core formulae must be OSI-approved and yours stops being, you either move to a custom tap (extra install friction, on every one of your 9,000 weekly installs) or lose the channel that produces your 30 paying teams in the first place. This is the concrete version of "AGPL as a magic shield" for your specific distribution model — verify it, don't assume it either way.
- **No foundation, funder, or procurement allowlist constraint stated** — flag if one exists that you haven't mentioned.

## Posture (Step 2) — brainstorming, no recommendation locked yet

Three postures, not the one you walked in asking for:

| Posture | Bundle | What it costs | What it buys |
|---|---|---|---|
| **1. Status quo, monetize the layer, not the code** | CLI stays exactly as licensed today. Team-plan differentiators live entirely outside the OSS repo, in a closed-source service. | Zero — no consent hunt, no Homebrew risk, no fork | Nothing new against a competitor who reimplements independently, because nothing ever protected against that |
| **2. Open-core split (my default recommendation)** | CLI core — the thing 9,000 people/week actually run — stays permissive, untouched. Any new team/collaboration feature ships as a separate proprietary component that never enters the OSS repo. | Near-zero on the existing codebase (no relicense, no consent problem). Real but bounded design discipline going forward: never let a shipped OSS feature migrate to the closed side | The actual thing worth protecting — your paid differentiators — without taxing the funnel that produces them |
| **3. FSL on the CLI itself, the ask as stated** | Relicense the CLI repo to FSL (2-year clock, converts to MIT/Apache-2.0 automatically, no per-adopter use grant), "like Sentry" | The largest: full contributor consent hunt, loss of OSI-approved status, probable Homebrew-core ejection, a fork precedent (Elastic → OpenSearch, Redis → Valkey, HashiCorp → OpenTofu all happened within weeks of an equivalent move), and it's the one posture where the Polish competitor becomes the natural party to lead that fork and get to tell the "we kept it open" story in public | Only stops someone who redistributes **your own code** as a competing product. Buys nothing against independent reimplementation — see the reality check above |

Row 3 is what you asked for, and the order above starves it on purpose, same as the skill's default ranking under a confirmed business model — it's still the highest-*value* row if the threat is genuinely code reuse, it's just the most expensive and least reversible, and every documented precedent produced a fork, not a stopped competitor. Promote it only if assumption 2's second branch is true — see below.

**Recommendation: posture 2.** Sentry's own history actually supports this, not the "just FSL everything" reading — their SDKs (the pieces developers pull directly into their own code, closest analogue to your CLI) stayed permissively licensed; FSL landed on the self-hosted *server* application. The split, not the license name, is the precedent worth copying. Verify this detail against Sentry's own license file history before you cite it publicly — I'm confident in it but it's not in this skill's sourced-claims list.

### The fork in the road, made explicit

- **If the $400/month plan's features already live in a separate closed-source service** (assumption 2, branch A): you have nothing to relicense. A fork of the free CLI cannot reproduce your product, because your product was never in the open repo. Stop here — posture 1 is functionally what you already have, just say so and skip the rest of this document.
- **If the team-plan features are compiled into the same OSS binary, gated by a license key** (branch B): a fork *can* strip the gate and ship your paid features for free. This is a real problem — but the fix is moving those features to a genuinely separate, closed component (posture 2's actual mechanic), not relicensing the whole CLI. Relicensing the whole CLI to stop a key-gate bypass is using a sledgehammer on a build-configuration problem.

## Outbound license (Step 3)

- **CLI core: no change.** Stays on its current permissive license. This is what eliminates the consent hunt, the Homebrew risk, and the fork precedent in one move — there's nothing to relicense because nothing about it changes.
- **New team-coordination component, if and when it's split out:** doesn't need to be open source at all. It's new code, wholly owned by you, with no consent problem — you can make it fully proprietary (simplest), or source-available under FSL specifically *if* you want the trust signal of publishing it while still banning a hosted-resale competitor. FSL's actual mechanics: two-year clock, converts to MIT or Apache-2.0 automatically, no per-adopter grant, "you can do anything with FSL software except economically undermine its producer." That's the correct, narrow place for the "like Sentry" instinct to land.

## Contribution policy (Step 4)

- **CLI core:** if there's no DCO today, add one — a commit trailer plus an automated check, near-zero friction, and it buys you the provenance trail that makes any *future* relicense (if one is ever genuinely needed) faster to execute, since you'll have a clean signed-off history instead of an unreachable-contributor hunt.
- **Do not add a CLA to the CLI core** for this. Nothing in posture 2 requires it, and a CLA appearing on a project that "individual developers install with zero friction" reads exactly like the failure mode this skill calls out: a rights grab with no stated need, paid for in lost drive-by contributions.
- **New team-layer component, if it ever takes outside contributions:** CLA before the first external PR, not after — cheap to add on day one, expensive to retrofit (this is the exact mistake this migration would otherwise be making at the whole-CLI scale).

## Business model (Step 5)

This is product-led B2B: individual adoption with zero procurement, converting to a company contract later. The skill's own rule for this motion is explicit — *"source-available terms that block the individual developer's free adoption break the PLG funnel."* Your 9,000 weekly installs are the entire top of that funnel; your 30 team-plan customers are what survives it. Anything that makes an individual developer pause to read a license before running `brew install finchgate` — a non-OSI badge, a Hacker News thread asking "wait, is this still open source?", a Homebrew tap migration — taxes the exact number that currently costs you nothing and produces your $144K ARR (30 × $400 × 12). Defend the layer that's actually sold; don't put a toll booth in front of the free tier that finds your buyers for you.

Also worth saying plainly: **trademark, not license, is what stops someone from calling their product "Finchgate."** If part of what's rattling you is a copycat riding your name or look, that's a separate, cheaper lever — monitor for it, and it works under your current license unchanged.

## Migration plan — concrete steps

1. **This week — verify the two load-bearing facts.** (a) Read your own `LICENSE` file, confirm it's permissive as assumed. (b) Confirm whether team-plan features live in a separate service or in the same gated binary. Everything downstream depends on this.
2. **This week — determine what the competitor actually did.** Diff their binary or CLI output against yours for anything resembling copied code, strings, or error messages. If you find copying, that's a counsel call, immediately, under your license as it stands today — don't wait for a relicense to act on it.
3. **Week 2 — dependency and contributor audit.** Run the license enumeration on everything shipped. Pull the contributor list and check for a CLA history (there almost certainly isn't one, per assumption 3) — this tells you whether "relicense the CLI" is even executable in under a quarter, independent of whether you decide to.
4. **Week 2–3 — architectural boundary, if branch B applies.** Move any team-plan feature that's compiled into the public binary out to a separate, closed-source service or module. This is the actual fix for "someone could unlock our paid features from the OSS repo," and it needs no license change on the CLI at all.
5. **Week 3 — add the DCO to the CLI repo** if not already present. Cheap, and it's the thing that makes any future licensing decision on this codebase faster, whichever way it goes.
6. **Ongoing — leave the CLI's license alone.** Publish, if you want the trust signal, a one-line commitment that the CLI stays permissively licensed — the thing your funnel actually depends on is confidence that it won't be pulled out from under existing users, not a stronger license.
7. **Only if you build the new team-coordination component and want it source-available:** apply FSL there, scoped to that component alone, following Step 6's playbook — map who'd need to consent (nobody, it's new code), fix the version boundary, decide what stays permissive (everything upstream of it), and write the announcement before finalizing the decision. Draft skeleton:

```markdown
# Finchgate [component] licensing

What changes: new [component] releases ship under FSL (Functional Source License),
converting to Apache-2.0 two years after each release.
What does not change: the Finchgate CLI stays [current license], forever, unchanged.
Who this affects: a company reselling [component] as a hosted competing service.
Who this does not affect: every individual using the CLI, every existing team-plan customer,
anyone self-hosting [component] for their own use.
Why: [name the situation plainly, not "sustainability"]
```

## Revisit triggers

Reopen this decision if: the team-plan features can't be architecturally separated from the CLI binary within a reasonable engineering effort (then posture 3's cost-benefit changes), you confirm actual code copying by the Polish competitor (then this becomes an infringement matter, not a licensing one), Homebrew's policy turns out not to gate on OSI approval after all (removes one cost from posture 3), or weekly installs or team-plan conversions move meaningfully after any change here (tells you whether the funnel-protection argument above was right).