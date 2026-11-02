Straight answer first: I won't hand you copy that says "vendor-neutral" today, because it isn't true yet, and the one audience you most need to believe it — a bank's procurement/governance reviewer — is the audience best equipped to catch it. Trademark ownership is a USPTO lookup. Domain ownership is a WHOIS lookup. CLA terms are a PDF they already have. Maintainer affiliation is five LinkedIn profiles. "No minutes, Tuesday internal sync" is one direct question away from an honest "we don't publish those." If a bank's due-diligence team finds daylight between your announcement and those five facts, you don't just lose the neutrality claim — you've taught a risk-averse buyer that your public statements need independent verification, which is a worse position than never having claimed it.

Here's the deliverable: what "vendor-neutral" actually checks against, where you stand, and copy you can actually publish.

## 1. What the claim is measured against

Bank open-source risk reviews (and any competent procurement team) benchmark against the same handful of criteria CNCF/Apache/Linux Foundation use for "neutral" status:

| Criterion | What it requires | Vantablock today |
|---|---|---|
| IP custody | Trademark held by a neutral legal entity, not a vendor | ❌ Held by Corvid |
| Infra custody | Domain/registry/CI not solely vendor-controlled | ❌ Corvid-owned |
| Contribution terms | DCO, or a CLA with no copyright assignment (inbound=outbound) | ❌ CLA assigns broad rights to Corvid |
| Maintainer diversity | Multiple independent employers, no single-company majority | ❌ 5/5 Corvid |
| Governance transparency | Published charter, public meeting notes | ❌ Private, no minutes |
| License | Permissive, OSI-approved, no BUSL/SSPL bait-and-switch | ✅ Apache-2.0 since day one |

One real point in your favor: the license itself. Apache-2.0 from day one means no relicensing rug-pull risk — that's a genuine, checkable, positive fact. Everything else on that table is currently single-vendor, which is normal for a company-founded OSS project and not something to be defensive about — but it is the opposite of "vendor-neutral."

## 2. Why "announce it now, fix it later" is the wrong sequencing

Genuine transitions (trademark transfer to a foundation, CLA rewrite, seating external maintainers with real merge rights) run 3–12 months even when a foundation is receptive. You can't manufacture that in four weeks. Announcing the end-state before the mechanics exist is the textbook definition of open-washing, and it's a known category banks specifically screen for — meaning you're not slipping past a generic reviewer, you're walking into their checklist.

## 3. What to actually say next month

Lead with the roadmap, not a false finish line. This is more credible to a sophisticated buyer than a vendor-neutral claim they can debunk in an afternoon — a bank's vendor-risk team trusts a dated commitment with named steps more than an adjective.

---

**Draft announcement — "Vantablock's path to open governance"**

> Vantablock has been Apache-2.0 licensed since its first commit — no source-available tricks, no relicensing risk, ever.
>
> Today we're starting the next step: moving Vantablock's governance from a Corvid-run project to an independently governed one. Over [timeframe, e.g. the next two quarters] we will:
>
> - Publish a public governance charter defining how maintainers are added and how decisions get made.
> - Open our maintainer sync — public agenda, public notes, open to any contributor.
> - Replace our current CLA with a Developer Certificate of Origin (or a CLA with no copyright assignment), so contributors keep their own rights.
> - Add our first externally-employed maintainers with real merge rights.
> - Begin the process of moving the Vantablock trademark and domain to a neutral home.
>
> We're doing this in the open. Track progress at [governance repo / roadmap link]. If your organization is evaluating Vantablock and wants to shape this process, [contact].

---

This version is true today, verifiable today, and gives you a legitimate "look how fast we moved" story at next year's conference once the steps land.

## 4. What to hand the bank's procurement team directly

They asked for governance — give them the real maturity picture, not marketing copy. This reads as more trustworthy, not less, because it's audit-proof:

- Current state: Corvid-founded, Corvid-maintained (5 maintainers, all Corvid), Apache-2.0, CLA assigns rights to Corvid, trademark/domain Corvid-owned.
- What that means for you: no risk of relicensing (permissive license locked in); bus-factor and roadmap control currently sit with one vendor.
- What's changing, with dates: the five-point roadmap above, plus named milestones.
- What doesn't change: the license. That's your durable answer to "what happens if Corvid disappears or gets acquired" — code stays usable regardless of governance model.

## 5. If you want "vendor-neutral" to be true by conference time, do these first — in order

1. **CLA → DCO or rights-preserving CLA** (weeks, not months — this is a document change plus a contributor re-sign campaign for active contributors).
2. **Publish minutes going forward** (zero cost, immediate, do it this week regardless of anything else).
3. **Invite 1–2 external maintainers** with real commit/merge rights — even provisional, publicly announced, is a genuine step banks can verify via GitHub CODEOWNERS.
4. **Publish a governance charter** — decision process, how maintainers are added/removed, veto rights if any.
5. **Start (don't finish) a foundation conversation** — CNCF, Apache Incubator, or a neutral non-profit. "In discussions with X to home the trademark" is a verifiable, honest claim; "vendor-neutral" is not.

Steps 1–2 are achievable before next month. Steps 3–5 are the actual multi-quarter work — put dates on them publicly, then hit the dates. That's the version of this story that survives a bank's procurement team, and it's the version that's still true a year from now when someone checks.