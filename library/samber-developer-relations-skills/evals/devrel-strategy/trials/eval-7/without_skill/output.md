# Value-per-effort ranking: self-serve devs vs. enterprise accounts

## Ranking

1. **Self-serve individual developers** — highest value per DevRel hour.
2. **Enterprise trust/security collateral** (reusable artifacts) — high value per hour, but a bounded, build-once project, not a recurring hour-sink.
3. **Enterprise bespoke 1:1 account support** (calls, custom demos, live reviewer Q&A) — lowest value per DevRel hour. This is Sales Engineering's job, not DevRel's.

## Why mirroring revenue (60/40) is the wrong split

Revenue share tells you where money already landed, not where the next DevRel hour pays off. The variable that actually decides DevRel efficiency is **leverage**, and the two segments sit at opposite ends of it:

- **Self-serve**: effort is spent once — a doc, tutorial, sample repo, conference talk — and read by every developer who finds it, this month, next year, indefinitely. Marginal cost per additional developer served is near zero, and DevRel is the primary causal driver of both acquisition and activation here.
- **Enterprise**: revenue is concentrated in 30 accounts, gated by a security reviewer. What unblocks a deal is a compliance checkbox, not content depth — and there's a hard ceiling: more DevRel hours don't create more enterprise accounts to sell to. Sales capacity and market size set that ceiling, not you.

So even though enterprise revenue-per-account is roughly 60-100x self-serve revenue-per-account (40% ÷ 30 accounts vs. 60% ÷ a presumably much larger dev base), that per-account premium doesn't translate into per-DevRel-hour efficiency, because most enterprise-facing hours don't compound across the other 29 accounts the way one blog post compounds across thousands of future developers.

## The one enterprise exception worth funding

Split enterprise-facing work into two kinds — they behave completely differently and get lumped together by default:

- **Reusable trust collateral**: security FAQ, SOC2/compliance one-pager, data-flow/architecture diagram, a written answer to "the 20 questions every reviewer asks." Build once, hand to every account — the current 30 and every future one. This behaves like self-serve content: leveraged, compounding, high $/hour. **This is the one enterprise investment that belongs in DevRel's hours.**
- **Bespoke 1:1 support**: live calls, custom demos, one-off reviewer Q&A per account. Scales linearly with account count and doesn't leverage across the other 29. Low $/hour for DevRel specifically — route it to Sales Engineering/Solutions Architects. Folding it into DevRel quietly taxes the segment that has 10-100x the leverage to subsidize the segment that has none.

## Recommended hour split

- **~75-80% self-serve** — content, docs, samples, community, SEO/GEO, conference talks.
- **~20-25% enterprise**, almost entirely front-loaded into building the reusable trust-collateral library.
- Once that library exists, treat it as a **finished project**, not a standing line item — taper enterprise DevRel hours to under 10%, maintenance-only, and push any account-specific ask back to Sales/SE.

## What would flip this recommendation

- If the self-serve dev base turns out to be small (say, under a couple hundred active devs) generating 60% of revenue at a high per-seat price, the leverage argument weakens — check actual active dev count, not just revenue share, before locking the split.
- If a single enterprise deal is large enough that even non-reusable, bespoke DevRel hours reliably unblock it (e.g., one stalled $300K renewal justifies a week of dedicated work), carve out an explicit "deal rescue" allowance separate from the steady-state split, and track it as an exception rather than folding it into the default allocation.
- Validate over one quarter: tag DevRel hours by segment and track (a) signup/activation lift attributable to new self-serve content, (b) enterprise deals where the security reviewer cited DevRel-authored trust collateral as resolving their blocker. If enterprise deals keep stalling on questions the existing collateral doesn't answer, that's a signal to expand the trust-doc library — not to add more bespoke account hours.