## The blocker nobody mentioned: BUSL-1.1 probably disqualifies you from SFC

Software Freedom Conservancy only fiscally sponsors projects released under an OSI- or FSF-approved free license. BUSL-1.1 is not OSI-approved — it's a source-available license with a delayed conversion date and a non-compete clause, which is exactly the category of license SFC has publicly campaigned against (their whole identity is copyleft/FOSS purity advocacy, including public criticism of companies moving to source-available licenses to block cloud-provider competition). This isn't just a checkbox gap — it's likely a values mismatch with the org.

⚠️ Confirm directly with SFC before spending more time on this path. But plan around "probably no" as the base case, not "probably yes, pending paperwork."

I don't have live web access this session, so treat SFC's fee %, current application backlog, and exact license wording below as "true as of my training, verify before acting" — not current fact.

## You're conflating two different problems

1. **Get sponsorship/contract money out of your personal account, with proper tax and liability handling.** This is urgent — the fintech and the bank want to pay you now, and your accountant is right to hate the current setup.
2. **Whether Cinderpath should live inside a nonprofit foundation home.** This is a slow, separate, mostly irreversible decision about licensing philosophy and governance — not a banking fix.

SFC solves neither problem well here. It's slow (historically months, sometimes with a queue for new member projects), it requires a license you'd have to give up your commercial leverage to adopt, and even if you cleared the license bar, the bank's "pay for two features" ask is a services contract, not a donation — routing that through a 501(c)(3) means it has to be structured as a public-benefit grant (the features ship to everyone under the open license, the bank gets no exclusivity), not a bespoke deliverable-for-money deal. If the bank wants anything exclusive or private, it legally can't go through a nonprofit fiscal sponsor at all.

## Recommended path

**Step 1 (now, days-to-weeks): incorporate a normal commercial entity to receive both payments.** Not a nonprofit. A bank paying for custom features will not wire money to a personal account or a foreign charity anyway — their compliance team needs a real contracting party, which is probably part of what's driving your accountant's complaint. Options, in order of speed:
- The existing consultancy invoices both deals, and pays the third maintainer their share via a contractor/revenue-share agreement. Fastest — an entity already exists.
- A fresh 3-way-owned entity (SAS/SARL/GmbH/LLC depending on jurisdiction) dedicated to Cinderpath. Slower by a couple weeks, but avoids the next problem.

⚠️ Before picking either: check the two consultancy-employed maintainers' employment contracts for IP-assignment clauses. If Cinderpath was built using consultancy time/resources, the consultancy may already have a legal claim on the IP that nobody intended — this needs resolving in writing regardless of which entity you pick, or the third maintainer's stake is undefined.

**Step 2 (parallel, no deadline pressure): settle the license question as a business decision, not a compliance one.** Ask whether you actually want to drop BUSL's non-compete protection. If the fintech/bank are paying partly because Cinderpath isn't freely resellable by a cloud provider, relicensing to satisfy a fiscal sponsor could cost you more than SFC would ever give you. Don't let "someone told me to apply to SFC" drive a licensing decision with real commercial downside.

**Step 3 (only if there's a real reason to want a foundation home later — credibility, neutrality signaling, wanting Cinderpath outside the consultancy's control): revisit with a narrower scope.** A common pattern for BUSL/open-core tools: split out a genuinely OSI-licensed core and apply to SFC (or elsewhere) for that piece only, keeping paid features/extensions outside the sponsorship, in your own entity. This preserves the commercial upside while giving you a legitimate nonprofit-backed core.

**Step 4 (do this regardless of path, in writing, now): address the 2-of-3-same-consultancy structure explicitly.** Put a short governance doc in place — decision rules that prevent the consultancy pair from unilaterally controlling the project, a process for adding maintainers, and clarity on who owns what. Any serious funder (a fiscal sponsor, a bigger sponsor down the line, the bank's own diligence) will ask this question; answering it before they ask is cheap insurance and also protects your third maintainer.

## On the 15-20% "sandbox" archival stat

That figure tracks CNCF's Sandbox tier — a graduation ladder with a technical oversight committee that periodically prunes inactive projects. It is not the risk profile of SFC-style fiscal sponsorship, which has no maturity stages and doesn't "archive" projects for lack of traction the same way. If you're actually evaluating CNCF (plausible, given "infrastructure testing tool"), note CNCF also requires Apache-2.0 — same BUSL blocker applies there.

The real risks to price in for SFC specifically, once/if the license question is resolved: application/review latency delaying access to money you need now, an administrative fee on every dollar processed, and cross-border wire/VAT friction with a US 501(c)(3) that a normal EU-facing contract wouldn't have. None of these are the "1-in-5 gets abandoned" risk you read about — that's a different program solving a different problem.

**Bottom line: solve the money problem with a normal company this month. Treat the foundation question as a separate, unhurried decision that hinges on whether you're willing to give up BUSL's protection — don't let a banking headache drag you into a licensing decision you haven't actually made yet.**