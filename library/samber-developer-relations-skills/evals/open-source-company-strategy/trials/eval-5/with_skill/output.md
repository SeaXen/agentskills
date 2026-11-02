# Should Lindgren Health Data open source the HL7 connector?

**No — not for the reasons on the table.** The account manager's case ("goodwill," "nobody wants to maintain it") and the QBR ask don't survive their own gates. There's a real, narrower version of this that's plausibly a yes — but it isn't the one being proposed. Below is the full brief.

---

## What we sell

Clinical-data normalization to hospital groups — the value a customer pays for is the mapping/validation engine that turns messy hospital source data into a trustworthy canonical clinical model, plus the compliance posture and operational reliability of running that at hospital scale (~€14M ARR, largest account €480k/yr). Customers are not paying for HL7 wire-protocol plumbing; every vendor in this space has to build that just to exist.

## Motive

**Rejected: external demand pull.** The evidence test is "name the party and what happens on refusal." The Nordic network raised it at QBR, but it's not in the contract and the renewal lands in October *regardless*. Refusal costs nothing this cycle. This is the skill's own textbook weak case: *"A request is not a requirement... if the renewal is not conditional, this is a preference dressed as a mandate."* Treat it as a signal worth investigating, not a mandate to execute.

**Rejected: "goodwill" / "nobody enjoys maintaining it."** Neither is a named motive. The second one is worse than decoration — it's the mirror image of *"the team wants to,"* and it predicts the specific failure this skill calls dump-and-run: code shipped to offload a burden internally almost never gets a genuine external-maintenance commitment, because the motive for shipping it was relief, not stewardship. An unmaintained public repo carrying a €480k customer's integration is a liability, not a goodwill gesture, six months in.

**Plausible, unverified: commoditize your complement.** HL7/FHIR connectivity is infrastructure hospitals already expect to be open (regulatory pressure in this direction has been building for years; mature open connectors like Mirth/NextGen Connect already exist). If integration friction is actually costing Lindgren deals in the regulated segment, opening the connector could lower the barrier to adopting the thing that's actually sold — the normalization engine — same shape as Sun/HP funding GNOME to sell hardware. **Evidence test not yet passed**: nobody has checked how many deals stalled on integration effort. Pull that number before adopting this as the real reason.

**Plausible, unverified: cost sharing.** "Two other customers would benefit" is not the same as "two other organizations have a reason to co-fund." Ask them directly whether their integration engineers would commit fix time. Absent that, this is single-vendor open source with extra process.

No motive here currently passes its own evidence test. That's a reason to investigate, not a reason to default to closed — but it rules out shipping *this week* off the QBR ask alone.

## Open / Closed / Not yet

The connector is one asset name covering two different things, and Gate 2 has to be run on each separately — this is the actual decision, and it's currently unmade:

| Asset | Motive served | G1 Irreversible | G2 Differentiating | G3 Value capture | G4 Contributable | G5 Owner | Verdict |
|---|---|---|---|---|---|---|---|
| HL7 transport/parsing layer (message framing, ack handling, connectivity) — *if cleanly separable* | Commoditize complement (unverified) | Fine — standard protocol glue, no proprietary IP | Context/enabler | Managed hosting, compliance posture, mapping engine, support, trademark | Plausible — common pain point industry-wide, real prior art (Mirth) | ⚠️ No name, no hours committed yet | ⚠️ **Not yet** |
| Normalization/mapping logic (field mapping, code-set translation, dedup/entity resolution) — *if entangled in the same 6,000 lines* | none | **Not fine** — this is the product | Differentiating | Nothing left if opened | n/a | n/a | ❌ **Closed** |

**Nobody has confirmed which of these the "6,000 lines of glue code" actually is.** Before anything ships, get someone who isn't the account manager to read the code and answer: does it contain hospital-specific mapping rules, code-set tables, or normalization logic, or is it pure HL7 transport? If the two are entangled, this is a "Not yet" verdict full stop, with the condition being a refactor to split them — not a decision to make on the current code as-is.

Gate 5 fails outright right now: no named maintainer, no hours/week, no issue-response commitment. Per the skill's own rule, a fail on Gate 5 means it does not ship, independent of how good the motive looks once verified.

## Competitive case

Named risk: a systems integrator, or a larger platform vendor bundling health-data interoperability (an existing open connector ecosystem — Mirth/NextGen Connect — already operates here, so this isn't hypothetical), absorbs the transport layer into a "free integration" pitch against Lindgren.

What Lindgren still holds, *if and only if* the mapping logic stays out of the published code: the validated normalization engine, the compliance/audit posture a regulated hospital buyer actually underwrites, support and SLA, the trademark, and the hosted operational track record. If the mapping logic ships by accident because nobody split it out, there's nothing left to hold — that's the scenario Gate 3 exists to catch before publication, not after.

## Decision rights

This is healthcare data infrastructure at a company where one account is 3.4% of ARR — this is not an account manager's call to make unilaterally, and "goodwill" is not a business case a single deal owner should be authorizing alone.

- **Business call** ("should we open this, and what does it buy us"): whoever owns the product P&L — at €14M ARR with a single €480k account driving the ask, this should sit with the CEO or VP Product, not the account manager. *(Assumption: treating Lindgren as a late-stage/growth B2B software company given deal size and regulated enterprise sales motion — confirm company type/stage before finalizing, since a true early-stage startup would route this to a founder instead.)*
- **Compliance review** (parallel, not sequential): legal/privacy on the HIPAA/GDPR special-category health-data exposure of anything touching patient-data mapping, plus a technical reviewer confirming the Gate-2 split actually holds before merge. In this domain specifically, add a review step the skill doesn't default to: confirm a community fork with a subtly wrong mapping can't plausibly get used against real patient data downstream — that's a clinical-safety question, not just a licensing one.

## Commitments

If this goes forward on the narrower interface-open line: publish that the open/closed boundary sits at transport vs. mapping, commit to never moving the transport layer back to closed once shipped, and don't frame the announcement as "granted because you asked" — frame it as a segment-wide decision. Otherwise the account that didn't ask reads it as a favor, and the account that did ask reads any future scoping decision as a broken promise rather than a boundary.

## Operating model

Before this ships: a named owner and a real hours/week number (a credible estimate for a 6,000-line connector with active external interest is 4–8 hrs/week in year one — review, docs cleanup so it's legible without internal context, security-report handling), a security contact and disclosure process (non-negotiable for anything touching hospital data pipelines, even at the transport layer), a release checklist, and a license allowlist entry. This is *additional* load near-term, not relief — it directly contradicts the "nobody wants to maintain it" premise, which is exactly why that premise can't be the reason to proceed.

## Measurement and re-evaluation trigger

Declare the objective now or it gets retrofitted later to flatter the decision: if commoditize-complement is confirmed, the signal is deal velocity / integration-effort objections in the regulated segment, not stars or forks. If cost-sharing is confirmed, the signal is external orgs landing fixes within 12 months.

Re-evaluate at: the October renewal (to see whether the ask resurfaces as an actual condition — that would upgrade this to real demand pull and change the urgency, not the gates); the next planning cycle; or immediately if the named maintainer leaves or a competitor ships an open equivalent first.

---

**Bottom line for the account manager's framing:** "just do it, it's goodwill" skips every gate that exists to prevent exactly the outcome that framing produces — an abandoned public repo the customer complains about next year. The path to a real yes is: split the code, name a real owner, verify the complement-commoditization number, and decide it as a segment-wide call — not as a favor granted at a QBR.