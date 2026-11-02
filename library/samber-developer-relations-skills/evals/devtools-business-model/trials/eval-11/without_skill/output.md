## Verdict: no business model. Run Glintpad as an unmonetized OSS project.

Every standard OSS monetization lever requires something you've explicitly ruled out:

- **Hosted/SaaS tier** — needs a server and network calls. You promised offline-only.
- **Open core / relicense to BSL-style** — needs a license change to gate a paid edition. You promised never to change the license.
- **Dual licensing** — sells companies an exception to copyleft obligations. MIT has no copyleft to buy out of, and no company has ever asked anyway.
- **Plugin marketplace / extension revenue share** — no plugin ecosystem exists.
- **Support or consulting contracts** — needs sales capacity and inbound demand. You have neither.
- **Usage-based pricing** — needs telemetry to meter. You touch no network, so you can't see usage even if you wanted to charge for it.
- **Ads or bundled offers in the binary** — needs network or compromises the "does one thing quietly" trust that hobbyist CLI users rely on. Not worth the reputational cost for a tool this small.

Nothing survives that filter because your constraints aren't obstacles to route around — they're the product's actual shape. A single-binary, offline, MIT, no-plugin hobbyist tool with zero inbound business interest in three years is structurally a **gift, not a business**.

### What's actually left
The only thing compatible with every constraint is **no-strings passive funding**: a GitHub Sponsors button and/or Open Collective link. Not a pricing tier, not a model — a tip jar. It changes nothing about the product, license, network posture, or roadmap, and it converts zero users if nobody feels like giving. Treat any money from it as a bonus, not a plan.

If you want funding without touching any constraint, the only other realistic path is **grants** (Sovereign Tech Fund, NGI Zero, GitHub Accelerator) — but those fund critical infrastructure, and a hobbyist photo-tidying tool is a weak fit. Worth a five-minute look, not a strategy.

### What not to do
Don't invent scope to create a monetizable surface — e.g. bolting on optional cloud sync to have something to meter. That's not "Glintpad's business model," that's a different product decision you haven't been asked to make, and it breaks the network promise you've made publicly. If revenue matters to you, it has to come from something other than Glintpad — not from bending Glintpad until it fits a framework it was never built for.