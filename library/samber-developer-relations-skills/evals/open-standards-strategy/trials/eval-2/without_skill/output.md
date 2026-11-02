## Big picture

Two decisions got bundled together that have different clocks, different owners, and different justifications. Un-bundle them first, or the slow one (consortium strategy, 2-year horizon) ends up hostage-negotiating the fast one (renewal, 11-week deadline).

- **Decision A — ship FleetLink 2.1 support to close the renewal.** Hard deadline, EUR 1.4M at stake. Engineering execution problem.
- **Decision B — join the consortium technical committee for FleetLink 3.0 influence.** Strategic, recurring EUR 48k/yr cost, 2-year payoff. Business-development problem.

Treat A as urgent and mostly independent of B. Don't let B's timeline (consortium board approval, committee onboarding) gate A.

## First, close one factual gap

Before assigning anyone or approving spend, get a straight answer from the consortium (or your VP Eng, if already known): **does implementing/claiming FleetLink 2.1 support require membership, or is the spec + conformance test suite open to non-members?**

This single fact determines almost everything below:
- If open: you can build and demonstrate compliance without joining anything. Membership becomes a pure Decision-B question, fully decoupled from the renewal.
- If membership-gated (spec access, certification mark, or conformance test suite locked behind membership): the EUR 48k is now a cost of closing THIS deal, not a strategic bet — approve it immediately, it's 3.4% of the contract value.

Also ask procurement directly what "support FleetLink 2.1" means to them: self-declared support, passing an interoperability test with their systems, or a consortium-issued certification mark. Those three have very different engineering scope and different dependence on membership. Don't assume — a vague procurement checkbox item is often satisfiable with less than the maximal reading.

## Renewal track (start Monday, don't wait on Decision B)

1. **Engineer 1**: spec review + gap analysis against current fleet-orchestration message layer. Deliverable by end of week 1: implementation plan + effort estimate + list of unknowns (versioning compatibility with any FleetLink 1.x already deployed at this customer, edge cases, message translation gaps).
2. **Engineer 2**: build the interoperability test harness in parallel — procurement asked for a "hard requirement," which means they will likely want evidence, not a claim. Having a working test/demo ready de-risks the last two weeks of the 11.
3. Re-baseline the estimate after week 1's spike. Protocol implementations routinely blow past a naive "read the spec, write the adapter" estimate — if the real number doesn't fit in 11 weeks, negotiate a **compliance roadmap clause** into the renewal now (signed contract + committed delivery date + credit/penalty) rather than discovering the slip in week 9. Established customers with an EUR 1.4M relationship usually prefer this over losing the vendor relationship.
4. If membership turns out to be required for certification, submit that application this week — approval and onboarding can itself eat calendar time you don't have to spare.

## Consortium track (parallel, owned by VP Eng, not gating the renewal)

Don't approve the recurring EUR 48k/yr on this deal's momentum alone. Get three answers first:

1. **Breadth of need**: how many other current or prospective customers will plausibly require FleetLink compliance over the next 1–2 years? If this renewal is a one-off, EUR 48k/yr forever is expensive insurance for one account. If FleetLink is becoming the vertical's de facto interop standard, it's a platform investment and the answer is an easy yes.
2. **Real time cost of the committee seat**: calls, working groups, travel. Decide now who actually attends — VP personally, or delegated to one of the two engineers — since a seat nobody staffs buys you nothing for FleetLink 3.0 influence.
3. **Who else is in the room**: if direct competitors sit on the same technical committee, weigh the roadmap-visibility upside against the competitive-intelligence exposure of your own roadmap being visible to them.

Once those three are answered, it's a normal build-vs-influence call for the VP to make on its own merits — not something to rush to match an 11-week sales deadline.

## Sequencing summary

| Week | Renewal track | Consortium track |
|---|---|---|
| 1 | Spec gap analysis + test harness build starts | Confirm membership-gating fact; VP gathers breadth-of-need data |
| 2–8 | Build + integration testing | Membership/committee decision made independently |
| 9–10 | Customer acceptance testing, demo | — |
| 11 | Sign renewal (with roadmap clause as fallback if needed) | — |

Bottom line: the two engineers go on the renewal starting Monday regardless of what happens with the consortium. The consortium seat is a real strategic option worth serious evaluation, but it earns its EUR 48k/yr on its own two-year logic, not as a rider forced through by an 11-week sales clock.