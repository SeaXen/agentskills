## Pull order

1. **Denominators first — npm downloads, GA date, beta-vs-GA install split.** Cheap pull. Turns every later number into rate, not raw count. "11 tickets" means nothing without knowing 11-of-40 installs or 11-of-4000.
2. **Sentry, segmented beta vs GA, grouped by error/endpoint.** Biggest N by far (year of data). But beta users = hand-picked design partners, different population than self-serve GA users. Blend them and you conflate two audiences. Split first, read second.
3. **Docs search queries (40).** Unprompted, self-directed intent. Read all 40 verbatim — small N but each one real signal of "what user hunted for and maybe didn't find."
4. **Support tickets (11).** Richest per-item (full text, real language, real frustration) but thinnest N. Read every single ticket in full. Cheap at N=11 — no excuse to skim.
5. **Search Console, 6 queries with impressions.** Pull last. This isn't customer signal — it's an "are we discoverable yet" status check. At 7 weeks GA, answer is almost certainly "no, and that's expected."

## The map

Nimbus Ledger is 7 weeks post-GA. Total usable signal across all 5 sources is small. Treat this stage as evidence-gathering, not a finished research cycle.

**Sentry** — tells you *where* integration breaks (validation errors, auth failures, idempotency collisions, balance/reconciliation edge cases). Does not tell you *why* someone gave up or how they felt. Machine signal, not voice.

**npm downloads** — tells you adoption shape (growing, flat, spiky). Does not tell you who's using it or for what.

**Docs search (40)** — tells you vocabulary and stuck points in the user's own words (e.g. if "idempotency key" or "reversal" spikes, that's a real confusion point). Volume too low to rank by frequency with confidence — read for content, not counts.

**Support tickets (11)** — tells you the sharpest pains, but 11 tickets split across bug/confusion/feature-request/expectation-mismatch buckets probably leaves 2-4 tickets per bucket. Below minimum viable sample (5 per segment) for any generalization.

**GSC (6 queries)** — tells you almost nothing about your users. Confirms no organic discovery yet. That's it.

## Confidence rule

Cluster themes across sources 2-4 (Sentry, docs search, tickets).

- Theme shows in 3 sources → **Medium-High**, worth acting on.
- Theme shows in 2 → **Medium**, worth watching.
- Theme shows in 1 → **Low**, hypothesis only, not a conclusion.

At this volume, expect zero themes hitting "High" (needs 3+ *independent* sources per skill's own guardrail, and you only have 3 candidate sources total). Realistic outcome: a short hypothesis backlog, not a research report with confident claims.

## Don't build personas yet

Total independent data points across all 5 sources won't clear 5-per-segment. Building personas or messaging off this is guessing with extra steps. Deliverable at this stage: **hypothesis backlog + a plan to go get real signal**, not a persona doc.

## Fill the gap — two moves

**Mine what's public (cheap, do first):**
- Competitor reviews for buyers in the same problem space, even though they never touched Nimbus Ledger: Modern Treasury, TigerBeetle, Increase, Medici, Hyperledger-based tools. G2/Capterra where they exist.
- Hacker News — search past Show HN / ledger-design threads. This audience (backend engineers building financial systems) talks here.
- r/fintech, r/accounting less useful (too non-technical); check GitHub issues/discussions if any open-source client or example repo exists.

This is proxy-persona building — walk outward from your differentiator hypothesis to competitor reviews to adjacent audiences. Standard move when a product has no first-party signal yet.

**Go ask (highest signal, do second):**
- Interview all 11 ticket filers. Full 11, not a sample — that's your entire population of people who cared enough to write.
- Add top active accounts by API call volume (pull from Sentry user context or billing). Aim for 5-10 calls total.
- PMF survey ("how would you feel if you could no longer use Nimbus Ledger") — premature to read as a real percentage at this user count, but send to full active list anyway as a pilot. Directional read beats no read.

## Bias traps specific to this data

- Beta and GA are different populations — don't average their Sentry data.
- Raw counts lie without denominators — always convert to rate.
- Support tickets skew toward problems, never value — don't conclude "nobody likes X" from ticket silence.
- Sentry is machine noise, not customer voice — pairs with tickets/docs-search, doesn't replace them.
- 6 GSC queries is not enough to read SEO intent — don't optimize content off this.

**Next: pull npm download counts + confirm exact beta cutoff date, before touching Sentry.**