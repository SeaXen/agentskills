Here's what to tell them, and why it's safe to say even with the money side unresolved.

## The reframe: you're conflating two different decisions

"What's free" and "what's the price" are separable questions. You can commit to the first *today*, publicly and permanently, while the second stays genuinely open. Communities asking "what will always be free" aren't usually asking for a price sheet — they're asking "will you rug-pull us later." That's a trust question, not a pricing question, and you can answer it now.

## The precedent you're one decision away from repeating

HashiCorp (Terraform), Redis, and Elastic all relicensed after their ecosystems had already contributed real work on top of the open code — and all three got forked by their own communities (OpenTofu, Valkey, OpenSearch) within months. The pattern every time: build adoption on "open," defer the commercial boundary, then draw it somewhere that retroactively devalues work the community already did for free. You have ~19 community-written connectors. If your eventual model so much as looks like it's monetizing that work, you get the same outcome. This is the one mistake in this space that's actually fatal, and it's avoidable by sequencing the announcement correctly.

## The boundary that fits your architecture

Your four pieces split cleanly along the standard open-core line (same shape as GitLab CE/EE, Sourcegraph, Grafana):

**Commit to free, forever, unconditionally:**
- The agent (it runs on customer machines — nobody installs infrastructure they think can be metered or clawed back later)
- The connector framework/SDK
- Every connector, yours and the community's, with no distinction by authorship
- Self-hosting the control plane and console, full-featured — not a crippled "trial" version of self-host

**Where you build the business (say this is still being worked out):**
- Hosting/operating the control plane for people who don't want to run it themselves
- Enterprise layer on top: SSO/SAML, audit logs, RBAC, SLA, priority support, compliance

This isn't arbitrary — it's the line that makes the free tier still *useful* (self-hosters get a complete product) while the thing you charge for is a real cost center (running infra for someone) plus features only bought by orgs, not individuals. It also sidesteps the authorship trap: don't gate connectors by "official vs. community," ever. The moment you take over maintenance of a community connector, or a contributor builds something as good as one of your 11, "who wrote it" stops being a stable line to gate on. Gate on *category* (connectors are free, full stop), not on origin.

## Make the commitment mechanically real, not just a promise

License the agent, the SDK, and the connectors under a standard OSS license (MIT/Apache-2.0) now. The reason this matters more than the words you say: code already released under a permissive license can't be retroactively relicensed out from under people who are using it — only *future* code is affected by any later license change. That turns "we promise this stays free" from a statement people have to trust into a structural fact they can verify. That's what actually defuses the "what will always be free" question — not a blog post, the license file.

## What to actually post to the community

> **What's always free, and what we're still figuring out**
>
> We've been dodging this question because we hadn't settled our commercial model — that part's still true, and we're not going to pretend otherwise. But we realized we were bundling two different questions together, and one of them we can answer right now.
>
> **Free forever, no exceptions:** the agent, the connector SDK, and every connector — ours and the ~19 the community has built. All of it stays open source under [MIT/Apache-2.0]. Self-hosting the control plane and console will always be a complete, uncrippled product — not a stripped demo of a paid version.
>
> **Where we'll eventually charge:** running the control plane for you (hosted/managed), plus an enterprise layer (SSO, audit, SLA, support) on top of that hosting. We haven't locked pricing or exact packaging for that yet, and we'll bring proposals back to you before we do.
>
> **What we're explicitly ruling out:** gating connectors by who wrote them, or moving anything in the "always free" list above behind a paywall later. If that ever needs to change, it only applies to new code going forward — never to what you've already built or are already running.

## One thing to settle internally before you post this

Decide now whether you're comfortable never monetizing connectors as a category — including your own future ones — because that's the part of this commitment you can't walk back later without the same blowback HashiCorp got. Everything else in the message (hosting price, which enterprise features, tiers) can genuinely stay "TBD, we'll ask you" without costing you any trust, because you've drawn the one line that matters and made it structurally permanent.