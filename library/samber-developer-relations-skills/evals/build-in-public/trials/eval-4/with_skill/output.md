## Verdict: don't publish it as specified. The instinct is right, the instrument is wrong.

You're not being paranoid. Three separate problems are bundled into that one page, and any one of them would be enough to stop.

**1. It's an Osborne-effect setup against your own installed base.**

You have 60 paying teams on v2 today. A page that says "v3 GA — Q4" tells every one of them, and every prospect currently evaluating v2, to wait. The Osborne Computer Corporation collapsed this way in 1983: announcing the successor killed sales of the shipping product, before the successor existed to replace it. You'd be doing this to yourself, deliberately, in public, with a rewrite of your storage engine as the headline act — arguably the single riskiest, hardest-to-estimate piece of engineering a four-person team can take on. If a prospect can read "storage engine rewrite, Q2" on your own website, they have no reason to sign this quarter.

**2. "Managed cloud" is a landmine specifically for this product, not a generic roadmap item.**

Your buyers chose self-hosted. For an observability agent, that's almost always a deliberate choice — compliance, data residency, air-gapped environments, "nothing leaves our network." Announcing a managed cloud offering doesn't read to that audience as "we're growing." It reads as "watch for the day self-hosted becomes the deprioritized tier." You'd be handing your own ICP a reason to distrust the deployment model they picked you for. This is a materially different risk than the other two roadmap items and deserves a separate decision, not a shared bullet on the same page.

**3. The commitment isn't credible, and a missed date costs more than the page earns.**

Four engineers. A storage-engine rewrite, a managed-cloud launch (multi-tenancy, billing, infra, probably new security review), and a v3 GA — three of the hardest things a small team can do, compressed into three quarters, while presumably still supporting 60 paying customers on v2. That's not a roadmap, it's a wish list with dates stapled on. When it slips — and a storage-engine rewrite alone slipping is close to the base rate — you haven't shown buyers you're serious, you've shown them your public promises don't hold, which is the opposite of what marketing is trying to buy.

## The part marketing has backwards

Enterprise evaluators don't actually get convinced by a dated roadmap — most procurement teams are trained to discount roadmaps as non-binding, which is exactly why every public roadmap ships with disclaimer language. What convinces an approver is evidence the vendor is alive, responsive, and disciplined *right now*: release cadence, how you handle security issues, how fast you respond, what you've already shipped and why. That's rung 1-2 material (shipping log, decisions), not rung "future financials of our unshipped product." It's cheaper to produce, it's true, and nobody can revoke it by missing a quarter.

## What to publish instead

If marketing wants the "we have a future" page, give them one that can't be weaponized against your own pipeline:

- **Direction and sequencing, no dates**, following the pattern GitHub uses on its own public roadmap: "storage engine v3 (in progress)," "managed offering (exploring)" — order implies priority, nobody can point to a missed date because none was given.
- Every item carries the standard disclaimer: *subject to change, not a commitment, don't buy against this timeline.* Put it in writing, not just in spirit.
- **Only put a real date on something already shipping** — if part of the storage engine work is already merged and in a release candidate, that piece can carry a date. Q2/Q3/Q4 promises on work that hasn't started don't belong on the same page as work that has.
- Split "managed cloud" out from the self-hosted roadmap entirely, or don't publish it until you're ready to pair it with an explicit statement that self-hosted isn't going anywhere. Don't let it sit next to GA dates as a throwaway bullet.
- Lead the page instead with what you can already prove: release cadence over the last N months, response times on issues/CVEs, what shipped in v2 recently. That's the "serious and has a future" signal enterprise buyers actually check.

## One more thing before this goes anywhere

This isn't just a marketing-and-CTO call. You have 60 paying teams whose renewal or expansion timing this page can directly move. Sales and whoever owns those accounts should see the exact wording before it ships — not because they need to approve copy, but because they're the ones who'll hear "we're waiting for v3" on the next renewal call, and they should know it's coming.