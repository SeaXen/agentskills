## The page isn't the bottleneck — the payment mechanism is

Four individuals paying $35/mo total, against three companies with money on the line, isn't a copy problem. Copy affects conversion within a channel. You have the wrong channel for the buyer you actually have.

**Individual GitHub Sponsors and corporate spend are two different motions, not two points on the same scale.**

- Individual sponsorship: a personal credit card, a moment of gratitude, no approval chain. That's your $35.
- Corporate spend: needs a vendor record, an invoice, a line item a manager can approve, and a reason that isn't "goodwill." A $2,000/mo tier sitting on a GitHub Sponsors page has none of that. No finance team processes a recurring personal-style subscription as vendor spend without a PO or an invoice trail — most won't even know how to categorize it.

Rewriting the tier copy optimizes conversion *inside* a flow that was never built to take company money. You could 10x the page's conversion rate and still collect $35 × 10, from individuals, because individuals are the only ones who can complete that flow.

## Who you're actually pitching

The two engineers filing issues each month are not your buyer. They're your warmest lead, and you're wasting them.

- They have no budget authority. Even if they *want* to sponsor you, they can't approve $2,000/mo — someone else can (VP Eng, platform lead, or whoever owns the OSPO/tooling budget), and that person has never seen your sponsorship page, because nothing routes it to them.
- An engineer filing a bug report is in "fix my problem" mode, not "evaluate vendor" mode. Nobody browses tier pricing while triaging a production issue.
- You're waiting for inbound (rewrite the page, hope it converts) instead of using information you already have: three companies, publicly pinning your library in their lockfiles, are identifiable by name. That's not a marketing funnel problem, it's an unmade outbound ask.

## What's missing, concretely

1. **No invoiced path.** Add one: Open Collective, a simple Stripe invoice, or a one-person LLC that can send a PDF and accept a bank transfer / NET 30. This is the single highest-leverage fix — it's the difference between "can't pay you" and "doesn't want to."

2. **No product at the $2,000 tier.** What does $2,000/mo actually buy a company? If it's a logo and a thank-you, that's consumer sponsorship framing wearing enterprise pricing. Companies pay for deliverables: a response-time SLA on their issues, priority security-patch turnaround, a private support channel, input on roadmap, an indemnification/commercial-license clause. Sell the support contract, not the badge.

3. **No differentiation that creates urgency.** Nothing forces a decision. If the tool "just works" for free, there's no trigger to get budget approved. A defensible, non-punitive version: publish a real support policy — sponsors get a stated triage SLA (e.g., 48h), everyone else gets best-effort. That's a legitimate value difference, not leverage — and it gives the engineer filing issues a concrete reason to go ask their manager for budget.

4. **No direct outbound.** You have three named companies and (at minimum) two named engineers. Identify who owns tooling/infra spend at each and email them directly: "You're running pgwatch-lite in production — here's what a support agreement gets you, here's what it costs, here's the risk if you're relying on unpaid best-effort maintenance for something in your critical path." That email doesn't exist yet. It will outperform any page rewrite.

5. **No proof of stakes.** You don't currently have a record of how much these companies actually depend on you — incidents you've helped resolve, response time on their issues versus others. Start tracking it. It's the ROI argument that makes $2,000/mo look cheap instead of arbitrary, and cost-based tier pricing ("we need $X to keep the lights on") converts worse than value-based framing ("here's what an outage without support costs you").

## What to do, in order

1. Stand up an invoiced payment path this week — this unblocks everything else, and costs almost nothing to add.
2. Write the actual support-contract offer (SLA, priority triage, private channel) — one product, one price, sized for what a Series-B company approves without a procurement fight (probably not $2,000 cold; test a lower anchor like $300–500/mo for a first deal, then raise once you have a reference customer).
3. Send three direct, personal emails — one per company — to whoever owns tooling spend, not the engineer filing issues. Reference their actual usage (the lockfile, the issues they filed) specifically.
4. Only then, revisit the public sponsorship page — as a place to send people *after* the direct conversation, not as the mechanism that's supposed to generate the conversation.

Stop treating "everyone says rewrite the copy" as consensus worth following. It's the advice people give when the real fix (go ask a specific person at a specific company for money, directly) feels harder than editing a page.