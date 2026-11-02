## What's actually going on

Two numbers are being reported and they tell opposite stories. "34 partners" and "up and to the right" is a sales/BD activity metric — it counts *signing*, not *value delivered*. The metrics that actually describe program health are underneath it and none of them are trending anywhere yet:

- **17.6% ship rate** — 6 of 34 announced partners have a live integration. 28 logos on your partner page point at nothing.
- **4% attach rate** — roughly 25 of 620 accounts use any integration at all.
- **81% concentration in the top 2** — of those ~25 adopting accounts, the other 4 live integrations are splitting the remaining 19%, meaning each of them is used by a small handful of accounts, maybe 1–3 apiece.

Read together: nine months in, you have built two integrations that customers actually use, and a partnerships motion that keeps signing partners faster than it can ship or validate them. "Partners signed" will keep climbing regardless of whether integration #7 ever gets used, which is exactly why it shouldn't be the headline number at a board meeting — it's the one metric in this program that's guaranteed to look good no matter what's happening underneath.

## The numbers to show the board

Replace the single "34 partners" slide with a funnel and a concentration view. Five things, in this order:

**1. The funnel, not the top-line count**
Signed (34) → Live (6, 17.6%) → Meaningfully adopted (2, 5.9%). This single chart does more work than any explanation — it shows the board where the drop-off actually is, and makes clear that "partners signed" is an input metric, not an outcome metric.

**2. Attach rate — the headline number**
4% of accounts (≈25/620) have ≥1 integration active. State it plainly, don't bury it. Boards respect a founder who leads with the uncomfortable number over one who gets caught not knowing it.

**3. Concentration / Pareto view**
Top 2 integrations = 81% of usage. Show usage per integration, ranked. This reframes the conversation from "we have 6 integrations" to "we have 2 integrations that work and 4 that haven't found product-market fit yet" — a much more useful and defensible story, and it points directly at what to do next (double down on the 2, diagnose or sunset the other 4).

**4. Attach rate *trend*, even if it's short**
A single point-in-time 4% is hard to interpret — 4% and climbing steadily since launch is a different story than 4% and flat for two quarters. Pull whatever monthly history you have (accounts-with-integration ÷ total accounts, by month since launch) and show the line. If it's flat, say so — that's a more important signal than the ship-rate problem.

**5. Retention/expansion lift, if you have it**
The single most convincing board metric, if you can cut it: churn rate and NRR for accounts with an active integration vs. without. Even directionally (e.g., "integration accounts churn at half the rate") turns this from an "adoption is low" story into an "adoption is low but high-leverage — worth fixing" story. If you don't have this cut yet, say you're building it, and treat it as the thing to bring to the *next* board meeting.

Don't show "partners signed" as a standalone win slide. It's fine as one column inside the funnel, but presenting it in isolation is what created this gap between VP-reported progress and reality — the board should see funnel context, not a headline count.

## What's a good attach rate for a program this age

There's no single published, sourced benchmark for "API-monitoring integration ecosystem attach rate at 9 months" — treat any number here, mine included, as a directional heuristic, not a citation. With that caveat:

Early-stage integration programs (year one, small number of shipped integrations, no app-store-style discovery surface) commonly land in a **5–15% attach rate** across the full customer base, when the shipped integrations have genuine value. Mature marketplaces (Slack's app directory, HubSpot, Salesforce AppExchange) reach 40–60%+, but that's the product of years of investment and built-in discovery — not a fair comparison for month 9.

By that yardstick, **4% isn't damning on its own** — it's low-normal for the age of the program. What makes it a real problem isn't the absolute number, it's that it's carried by 2 integrations while the other 4 are essentially inert, and that 28 of 34 "partners" never shipped anything. A program with 6 focused, well-supported integrations at 4% attach and a visible upward trend is a credible "early but working" story. A program with 34 announced partners, 82% vaporware, and flat 4% attach concentrated in 2 apps is a "the funnel is broken and we've been measuring the wrong stage of it" story — same underlying number, very different board conversation.

Set your own target from your own trend line, not an external benchmark: something like "grow attach rate from 4% to 8–10% over the next two quarters, driven by shipping the highest-intent partners already signed rather than signing more" is a concrete, defensible target the board can hold you to next quarter.

## Before the meeting (3 weeks)

- **Reconcile the partner page with reality.** 28 logos with no live integration is a credibility risk if a board member (or a prospect) clicks through. Either fast-track a subset to ship, or pull the unshipped ones down — a page with 6 real integrations is a stronger trust signal than one with 34 mostly-fake ones.
- **Get the retention/expansion cut**, even roughly, before the meeting — it's the single highest-leverage number you're currently missing.
- **Have the VP Partnerships conversation before the board does.** Their monthly metric (partners signed) and the program's actual health metric (attach rate, ship rate) have decoupled. That's worth resolving internally — realign what they're measured on toward "partners shipped" and "accounts activated" — so the board isn't the one who discovers the gap.
- **Decide what happens to the 4 low-usage integrations.** "We're investing further support in the two that work and re-scoping or sunsetting the four that haven't found traction" is a stronger position to walk in with than silence on them.