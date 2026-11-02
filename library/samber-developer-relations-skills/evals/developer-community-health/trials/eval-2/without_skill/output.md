Bottom line: tell them the risk is real, but it's an **employer-concentration** risk, not a single-person bus-factor problem — and it's worse than the raw per-person numbers suggest.

**The numbers**

Total commits (12mo): 2,480

| Employer | People | Commits | Share |
|---|---|---|---|
| Northwind Systems | Ana, Chen, Hana | 1,307 | 52.7% |
| Solano Labs | Bruno, Dagny | 850 | 34.3% |
| Independents | Eli, Farid, Gita | 323 | 13.0% |

No single individual clears 50% (Ana alone is 32.7%), so a classic "one maintainer holds the keys" story doesn't hold up. But that framing is the wrong one here.

**Why it's worse than it looks**

Commits inside one employer aren't independent risks — they're correlated. If Northwind reorganizes, deprioritizes the project, gets acquired, or just reassigns its engineers, Ana, Chen, and Hana likely move together, for the same reason, at the same time. That's not "three separate people might leave," it's "one company decision removes 53% of development capacity in one stroke." Same logic for Solano Labs (34%) with Bruno and Dagny.

Stack those two employer risks and you get 87% of all commit activity sitting behind two companies' staffing/roadmap decisions. Only 13% of activity comes from people with no shared employer to pull them off simultaneously — and that's spread across three separate individuals, so it's a poor substitute for continuity, not a safety net.

**What I'd actually tell procurement**

- Frame it as: "no single point of failure at the person level, but a real point of failure at the company level — Northwind Systems alone accounts for a majority of development."
- Commit share isn't the same as knowledge concentration — it doesn't show who owns the core architecture, who has merge/release authority, or who understands the hard parts. Ask for that breakdown too (code ownership / review load, not just commit count) before drawing final conclusions.
- Ask concrete governance questions:
  - Is the project under a neutral foundation, or effectively controlled by Northwind/Solano's contribution?
  - Do Northwind or Solano have any commercial/support relationship with this customer, or contractual commitment to keep contributing?
  - Is there more than one person per employer with release/merge rights, or does it bottleneck through one?
  - How healthy/stable are Northwind and Solano as companies (their exit is the real tail risk)?
  - License and fork rights: if both companies walked away tomorrow, could the customer (or a vendor) fork and self-maintain? Check test coverage and docs quality as a proxy for how expensive that would be.
- Net recommendation: not a red flag severe enough to block adoption on its own, but worth a mitigation clause — e.g., contractual continuity commitments from Northwind/Solano, or a documented fallback/fork plan — rather than treating 8 active contributors as sufficient diversification.