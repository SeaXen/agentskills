## Ferrolane commercial model ranking (12-week window)

**1. Dual licensing (commercial license off the AGPL) — top pick**
Full copyright ownership via CLA is the whole ballgame here: you can sell a proprietary license to anyone who can't live with AGPL's network-copyleft clause, with zero product engineering. Your two design partners are the most likely buyers — if they're embedding or hosting the engine themselves, AGPL already forces them to open-source their own changes, which is usually the exact pain that makes a company pay to make the obligation go away. Sales cycle here is legal + a contract, not a build. Closes in 12 weeks if you start the paperwork now.

**2. Managed hosting, flat-fee, manually invoiced — second**
You already run this for two design partners, and 3-of-4 ex-SRE means the ops side is proven, not a risk. Convert one design partner to a paid contract at a flat monthly rate, billed by hand (Stripe Invoicing, wire, net-30) — no metering or self-serve billing pipeline needed for one or two accounts. This sidesteps the "nobody can build billing this year" constraint entirely, because a flat invoice isn't a billing system. Bundle with #1: most buyers will want the license and the hosting together, so this doesn't have to be a separate deal.

**3. Best-effort support retainer — bolt-on, not standalone**
Sell business-hours, best-effort support as an add-on line item to #1/#2, explicitly not SLA-backed. That avoids needing a rota — a rota is only required once you promise response-time guarantees or after-hours coverage. Don't try to sell this alone; on its own it won't close a board-satisfying deal in 12 weeks with a 4-person team, and it invites scope creep toward the SLA you can't staff.

**4. Open-core — defer**
Ranked last because it needs the one thing you don't have: someone to design, build, and package proprietary features, plus eventual billing to sell them. Even a scoped-down version competes for the same 12 weeks as your actual close target. Right model for next year, funded by #1/#2 revenue and a product hire — not this quarter.

**Recommended play:** lead with a bundled deal — commercial license + paid hosting contract — sold to one of your two existing design partners, invoiced manually, support offered best-effort with no SLA language. That's the only path here with zero new engineering dependencies, which is what a 12-week, no-billing-capacity, no-rota constraint actually demands. The one blocking task is legal: get the commercial license terms drafted against your AGPL text in week 1–2, or the 12 weeks evaporate in redlines.