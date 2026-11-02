## What to tell the Stonecourse community about what stays free

You don't need the money model settled to answer this. Four of your five surfaces are already decided by facts you can't undo, not by a strategy call you haven't made yet — and staying silent on those is actively costing you trust it shouldn't.

### Why dodging is the wrong move, not just an awkward one

Silence on "what stays free" reads as intent to close the whole thing later, and your community is already pricing that in. You don't need the business model to answer the free question — you need the paid-boundary test, and you can run that today on what you've already shipped.

### Run the boundary test surface by surface

Stonecourse has four layers: the agent (customer-run), the control plane (you host), the web console (you host), and 30 connectors (11 yours, 19 community's). Against each, ask: is this organization-only, defensible without hostility, has an observable free→paid trigger, is cost-to-serve covered, and is it licence-compatible with what's already shipped.

**The agent.** Fails "organization-only" — a solo developer wants the exact same agent as a 500-person platform team, so there's no boundary to draw even before licensing enters it. And it's moot anyway: it's already open source. Published releases don't come back. This was never yours to decide; it was decided the day you shipped it.

**The 19 community connectors.** These fail on a different, harder rule: features the community contributed are never on the paid side, full stop — it's the single most cited cause of a hostile fork in this market, and you have 19 external authors who could coordinate one if you tried. Sixty-three percent of your connector surface is already, structurally, community property. Trying to monetize any piece of it is the single highest-risk move available to you right now.

**Your 11 connectors.** Don't split these from the community's 19 by authorship — split by buyer. A connector any solo developer would also install (a common database, a popular SaaS tool, a CI provider) stays free whether you or the community wrote it; a connector that only exists because a company needs it (an enterprise IdP a solo dev will never touch, a line-of-business system only procurement buys) is fair game later, regardless of who wrote it. Authorship isn't the line. Organization-only-ness is.

**The control plane and console.** This is your one real candidate paid layer, and it's the layer most platforms this shape eventually charge against — the agent and connectors commoditize toward the community, and the money sits one layer up, in the thing you operate. But three things are permanently off the table there no matter what model you pick:
- Basic authentication hardening, including SSO. Charging for SSO is the "SSO tax" — the argument, catalogued at sso.tax, is that SSO is a core security requirement for any company over five people, not a premium feature. Don't build your paid boundary out of it.
- Security patches for anything free. Withholding a fix turns your free users into adversaries.
- Data export. Configs, credentials, connector mappings, run history, logs — always exportable, self-service, uncapped. Lock-in read as a trap gets punished harder in this audience than almost anywhere else in B2B.

### The always-free list — what you can actually publish today

1. The agent, every version, forever. Already open source; this isn't a promise, it's a statement of fact.
2. All 19 community-authored connectors, in full, forever. Never resold, never gated, regardless of business model.
3. Any connector — yours or the community's — that a solo developer working alone would also install.
4. Security patches for the agent and every free connector, same release cadence as anything paid.
5. Full data export from the control plane: no caps, no delay, no paid tier required.
6. Basic auth hardening and SSO, wherever login lives.

### What to say about the rest

Don't promise the control plane or console "free forever" — a public promise like that is the single most expensive thing on your list to walk back later, more expensive than a licence change, because you haven't even chosen a model yet to know what it would cost you. Instead, give the community the *rule*, not a premature list:

> "Anything you could run for yourself, alone, without a team around it — the agent, every connector, community or ours — stays free, permanently, no exceptions. We'll never charge you for a security patch, for logging in with SSO, or for getting your own data back out. What we haven't decided yet is how we'll eventually charge for the parts of the hosted control plane that only exist because you're running this with a team — think governance and scale features, not the product itself. We'll tell you the shape of that as soon as we've tested it, and it will never touch anything on the list above."

That statement costs you nothing you weren't already committed to, and it's the difference between "we're dodging" and "we've told you exactly where the line can never move."