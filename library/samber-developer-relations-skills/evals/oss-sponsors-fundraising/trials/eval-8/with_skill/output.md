Here's the continuation of your NLnet application for ferrolink, built on the grant lane in `oss-sponsors-fundraising` (Step 1b) and its `grant-programs-and-reporting.md` reference.

## Eligibility check first

Your four facts clear NLnet's actual gates:

- **Licence** — MIT satisfies "recognised open-source licence," and NLnet requires code, hardware and documentation to ship under one — not just the code.
- **Who gets paid** — NLnet pays individuals directly, no entity required, so applying as yourself works.
- **Geography** — the gate is a "European dimension," a knockout criterion. Lisbon/Portugal clears it; say so explicitly and early in the application rather than assuming the reviewer infers it from your address.
- **Amount** — €48,000 sits inside the €5,000–€50,000 first-grant band and stays under the €50,000 line above which NLnet may condition payment on an independent security audit. That's worth keeping in mind if you're tempted to round up to €50k later — you'd be buying yourself an audit requirement for €2,000.

One open item I can't resolve for you: NLnet currently runs this fund under three named programmes — Restack, CodeSupply, ELFA — each with its own rolling deadline on the 3rd of every odd month. I don't have verified topic scope for each of the three, so confirm on NLnet's own call pages which one ferrolink fits before you submit — don't guess from the names. Today's date (2026-09-23) puts the next odd-month 3rd at **2026-11-03**; verify that hasn't shifted before you plan backward from it.

## The one structural fix your draft needs

Your opening — 2019 origin story, why solo maintenance has been hard — is the right material for a **sponsor page**. It's the wrong material for a **grant committee**. The skill is explicit about this distinction: a sponsor page sells a maintainer's credibility to a reader who already likes the project; a grant proposal is scored against published criteria by a reviewer reading dozens in a sitting, and the instruction is to "lead with the dependency, not the story."

NLnet's own scoring weights confirm why: relevance/impact/strategic potential is 40% of the score, technical excellence and feasibility 30%, cost effectiveness 30%. None of those three is "how sympathetic is the founding story." Your origin story isn't wasted — it's evidence for a different field (applicant background, where it de-risks execution) — but it can't be the opening move.

So: **don't lead with 2019.** Lead with what ferrolink is, what breaks if it stops, and who's exposed. Move the personal narrative down into the background/track record section, where "I've maintained this alone since 2019" becomes proof you can execute the year you're asking to be paid for, not a plea for sympathy.

## Draft, field by field, in NLnet's own order

Fill the bracketed parts — I don't have ferrolink's technical internals, dependent list, or your actual weekly availability, and inventing those would make this worse, not better.

**Summary of the project and the expected result**

> ferrolink is a low-power mesh networking stack, MIT-licensed, used by [who — embedded/IoT builders, off-grid comms projects, research groups; name three if you can]. This grant funds one year of dedicated hardening: [the 3–5 concrete things "hardening" means here — e.g. formal test coverage of the routing layer, power-consumption regression suite, protocol conformance against X, security review of Y, documentation for Z]. The expected result is a stack that [specific, verifiable end-state] rather than a stack that depends on one person's continued availability.

**Comparison to existing and historical efforts**

This is a scored field — reviewers will check whether you considered contributing to something existing instead. Name the nearest neighbors and say what differs. Candidates worth positioning against, if relevant to ferrolink's actual design: Meshtastic (LoRa mesh), the Reticulum Network Stack, B.A.T.M.A.N. advanced, Yggdrasil Network, Thread/Zigbee, BLE mesh, ESP-NOW-based mesh layers. State plainly why an existing stack doesn't already solve your use case — power budget, protocol layer, topology assumptions, licence — rather than only asserting novelty.

**Expected technical challenges, and the applicant background that de-risks them**

This is where 2019 goes.

> [Name the 2–3 hardest technical problems the year of work will hit.] I've maintained ferrolink alone since 2019, [X releases / X users / X production deployments / X reported and fixed issues] — solo maintenance is exactly why these problems are still open rather than evidence I can't close them. This grant converts unpaid nights-and-weekends maintenance into dedicated time against a fixed scope.

That's the honest, useful version of "why has this been hard alone" — framed as a track record, not a hardship appeal.

**Ecosystem: dependencies, main users, how you'll engage them**

> [What does ferrolink depend on? Who uses it — name real projects/companies if you can, per the skill's own instruction to name dependents rather than assert usage. How will you get hardening feedback from them during the grant — a beta channel, an existing issue tracker, a mailing list?]

**Other funding, past and present**

State plainly if this is the first funding ferrolink has received. If you're also running or considering a GitHub Sponsors page in parallel, disclose it — NLnet asks this to catch double funding of the same work, not to penalize a coffee-money sponsor tier.

**Budget: task/effort breakdown, rate, expenses**

NLnet explicitly says to expect the rate questioned, so show your work instead of a bare total.

> Requested: €48,000 over 12 months.
> [State your actual weekly commitment — this changes the day rate materially.] At full-time (≈220 working days/year), €48,000 works out to ≈€218/day — low enough that a reviewer may ask if it's sustainable, not high enough to need much defense. At 3 days/week (≈132 days/year), it's ≈€364/day, a more typical independent-contributor rate — decide which is true and say so, don't let the number float unexplained.
> Break the €48,000 into named tasks against your milestones below (e.g. €X routing-layer test suite, €X security review, €X documentation, €X CI/tooling), not one lump "my time."

**Milestones for the funding period, and who benefits**

Fix 3–4 milestones with dates inside the year, each tied to a deliverable you'd accept being paid against — NLnet pays per milestone via a memorandum of understanding, not monthly. Plan around that cash-flow shape now rather than discovering it after award: nothing arrives upfront.

**Generative-AI disclosure**

Non-negotiable, and it applies to this document: NLnet wants the prompts and logs used, and says non-disclosure is likely grounds for rejection. Since you're drafting this application with my help, that fact itself needs disclosing — keep this conversation (or an export of it) as your log, and say in the application that AI assistance was used for structuring and drafting, human-reviewed and fact-checked before submission. Don't skip this to look more self-sufficient; skipping it is the thing that gets proposals rejected, not the disclosure itself.

## After you submit

Expect a second stage of clarifying questions specifically on **rate justification** and **sustainability** — have your day-rate math ready (above), and have an answer for "what happens to ferrolink after month 12" that isn't "I go back to unpaid nights and weekends" — even a one-line succession or continued-funding plan strengthens this, per the skill's own note that funders read "even a succession plan" as something they're buying.

If awarded: no money before a milestone is reached, every deliverable ships under an open licence (already true for you), and staying under €50,000 total keeps you clear of the independent-security-audit condition that kicks in above it.