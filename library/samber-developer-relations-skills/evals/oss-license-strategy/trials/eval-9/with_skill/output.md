# Licensing decision — Bellrook

Not legal advice. Where a decision needs your retainer firm or your January in-house counsel, I say so explicitly.

## What I'm assuming vs. what needs one more answer

The skill this is built on (`oss-license-strategy`) runs as an interview before naming a license. You gave me a single-shot brief, so I answered every question I could from your facts and flagged the two I couldn't:

- **Named competitor for the server, unconfirmed.** You didn't say whether you're defending against a specific hyperscaler or funded rival building a managed version of a scheduler like yours. This is the one fact that would flip my recommendation on the server's license. I give you the default-case answer and the branch if you can name one.
- **Founder IP ownership, unconfirmed.** Two ex-infra engineers writing this pre-incorporation or across a job transition is exactly the case to say out loud, not assume. Confirm with your retainer firm that both founders' code is validly assigned to the company before you publish anything. I'm not asserting it isn't — I'm saying this is the retainer firm's five-minute check, not mine.

Everything else below follows from what you told me: two artifacts in one repo, three reachable outside contributors, retainer counsel now, in-house counsel in ~3 months, a real (if distant) commercial plan, and a 3-week hard deadline.

## Constraints

- **Dependencies: unaudited.** You didn't send a `go.mod`/lockfile, so I can't enumerate inbound licenses. Run `go mod graph` plus a license scanner (`go-licenses`, or GitHub's own detector on each dependency repo) before you publish — a single copyleft dependency in what you *ship* overrides any preference below. This is a checklist item, not a guess.
- **Ownership.** Founder-written code needs a confirmed IP-assignment chain to the company (see above). The three friends' PRs are the opposite case — small, easily reached, no employer complications stated.
- **Contributors: 3, all reachable, low friction.** This is the cheapest moment you will ever have to ask them for anything. It gets more expensive every week after launch.
- **No foundation, no procurement allowlist, no ecosystem license norm stated.** Nothing here eliminates an option outright.
- **Hard constraint: 3 weeks.** Rules out anything requiring a bespoke agreement drafted from scratch. Does not rule out a CLA — you already have retainer counsel, which is the thing that normally makes a CLA too slow for a deadline like this.
- **Business model: confirmed, ~12 months out.** A hosted commercial product is foreseeable, not hypothetical. Per this skill's default ranking, a confirmed business model flips the usual "maximum adoption first" ordering and promotes commercial optionality and the CLA rung to the front — I'm applying that flip below, not the beginner default.

## Posture — brainstorming, not yet a decision

Two candidates worth naming (a third — pure permissive with no CLA — I'm deleting outright: the confirmed 12-month commercial plan means you'll want relicensing or dual-licensing rights later, and getting them from three friends now costs nothing while getting them from hundreds of strangers in month 14 costs a consent campaign):

**A. Split posture (library permissive, server network-copyleft).** MIT/Apache-2.0 on the library, AGPL-3.0 on the server, CLA on the server only. Buys the SaaS-loophole protection now. Costs you every prospective self-hosting customer whose legal department has a blanket AGPL ban (Google's published policy is the checkable example — "code licensed under AGPL MUST NOT be used at Google," including on laptops). Since self-hosted adoption *is* your go-to-market for the next 12 months, that's a real tax on the thing you need most right now, in exchange for protection against a threat you haven't named yet.

**B. Open-core posture (one license, CLA everywhere, monetize later via hosted product + proprietary add-ons).** Apache-2.0 across the whole repo, CLA on all new contributions starting now, no copyleft trigger anywhere. Maximizes self-host adoption during the 12 months before you have anything to sell. Gives up nothing on future optionality, because the CLA is what actually buys the right to dual-license or carve out proprietary pieces later — the *license family* doesn't need to be copyleft for that right to exist.

**Recommendation: B.** Without a named competitor, AGPL on the server buys a defense against a threat you can't yet specify, at the cost of a real chunk of your only current growth channel. The CLA gets you the same future optionality (dual license the server, go open-core, sell a hosted-only proprietary layer) without that cost. Revisit A specifically the day you can name the hyperscaler or funded rival you're actually worried about — at that point the CLA you signed today means you can flip the server to AGPL or a source-available term without chasing anyone's consent.

## Outbound license

**Apache-2.0, one root LICENSE, covering both the library and the server.**

- Beats MIT here specifically because you're not a solo hobbyist: you have investors, will hire engineers who contribute on company time, and will eventually care about the patent grant and the trademark carve-out Apache-2.0 gives you that MIT is silent on. MIT is this skill's default for a small program with no corporate contributors in the picture — you're already past that.
- Single root LICENSE is correct today because both artifacts land on the same license; the moment the server's license diverges from the library's (see posture A above), split it into `server/LICENSE` plus a `LICENSING.md` explaining the boundary, so the root file stops silently claiming the whole tree.
- Trigger for the obligation, either way, is distribution — someone importing the Go module, or someone receiving the server binary/container. Preserve copyright and license notices at that point; that's Apache-2.0's whole ask.
- Rated Silver by the Blue Oak Council (not Gold — only BSD-2-Clause-Patent is), OSI-approved, and it survives procurement filters that check OSI approval directly. None of that is at risk here.

## Contribution policy

**Individual CLA now, on every new contribution, adapted from a standard template — not drafted from scratch — reviewed by your retainer firm, not written by me.**

Why CLA and not just a DCO, despite the 3-week clock: Fogel's ladder says a DCO is "probably the minimum" and a CLA "probably the best tradeoff... when the project genuinely needs those rights" — you do, because a hosted commercial product 12 months out is exactly the kind of plan that needs relicensing/dual-licensing rights the Apache-2.0 grant alone doesn't hand you. The usual objection to a CLA — it's slow, it needs counsel, it scares off drive-by contributors — doesn't apply to you the way it applies to a solo maintainer: you already have retainer counsel who can turn around a boilerplate ICLA in days, and your three contributors are friends who can sign in an afternoon. That's the "re-rank the default against what you actually have" step this skill asks for, applied literally.

Sequence, in order:

1. This week: ask retainer counsel to adapt a standard individual CLA (Apache Software Foundation's ICLA is a reasonable starting text) — do not have them draft one from zero.
2. Get the three friends to sign it before the repo goes public. This is the cheapest that consent will ever be.
3. Wire a CLA bot (CLA Assistant or equivalent) to block merges on unsigned PRs from day one of being public.
4. State the reason in CONTRIBUTING.md, not just the requirement — something like: *"Why we ask: we plan to offer a hosted, commercial version of the server. Signing grants us a license to use your contribution there; you keep your copyright and can use your own work anywhere else."* An unexplained CLA reads as a rights grab; a stated reason reads as a business arrangement contributors actually accept.
5. Hold a corporate CLA template in reserve for the day an outside contributor's employer requires one — you don't need it yet with three friends.
6. When January's in-house counsel starts, have them re-review the retainer-drafted CLA properly. Treat the launch version as a sound stopgap, not the final word.

## Business model

No lever pulled today beyond the CLA. The model is **open core + hosted convenience**: permissive license drives free adoption of the library and self-hosted server (product-led, bottom-up — an engineer adopts it without asking procurement, the company pays later for support, SLA, or a hosted version). The commercial surface in ~12 months is the hosted product itself, plus whatever proprietary add-ons enterprises actually ask for (SSO, audit logs, multi-tenancy) — draw that boundary once you have real customer signal, not now, and never move a feature that's already shipped open-source across it to the proprietary side.

The CLA is what keeps a copyleft/dual-license pivot on the table if a real reseller threat shows up later — that's the entire point of paying that cost now instead of a bigger one in month 14.

## Artifacts to ship in the next 3 weeks

1. `LICENSE` — unmodified Apache-2.0 text, repo root.
2. `NOTICE` — start it now, even close to empty; it's where third-party attributions from your dependency audit land as you find them.
3. `CONTRIBUTING.md` — CLA section with the stated reason, sign-off mechanics, recovery instructions for a rejected PR.
4. CLA text (individual now, corporate template in reserve) + CLA-bot wired into the PR merge gate.
5. `SPDX-License-Identifier: Apache-2.0` headers across source files; collective notice — "Copyright The Bellrook Authors" — rather than an enumerated list of the three friends' names, so it doesn't go stale as the team grows.
6. Confirm the GitHub license detector reads `LICENSE` correctly (it auto-detects unmodified Apache-2.0 text; don't append anything to the file).
7. Before flipping the repo public: get the three existing contributors' retroactive CLA sign-off. Do this before launch, not after — it's the one step on this list with a closing window.

## Revisit this when

- You can name a specific hyperscaler or funded rival threatening to resell the server as a managed service — reopen the server's license specifically (posture A, AGPL or a source-available term), using the CLA you already have to do it without a consent campaign.
- The hosted product actually ships (~12 months) — formalize the open-core boundary.
- January's in-house counsel starts — have them re-issue the CLA properly.
- Any contributor declines to sign — rewrite or remove their code before it becomes a blocker, while the codebase is still small.
- A foundation ever enters the picture — its rules override all of this.

## What I didn't check, and what I refuse to assert

- I have not audited your actual dependency tree — that's your action item, run it before you publish.
- I'm not asserting your founders' code is validly assigned to Bellrook — ask your retainer firm.
- I'm not naming a specific competitor for you, and I'm not asserting AGPL would stop one if you named one — copyleft redirects a compliant competitor into publishing source, it doesn't prevent competition.
- I'm not weighing in on the "Bellrook" trademark, but flagging it: you're going public in 3 weeks for a fundraise announcement, and trademark clearance conventionally wants a longer runway than that. The license protects the code; it does nothing for the name. Get that moving in parallel.