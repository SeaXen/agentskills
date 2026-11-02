# Overtone — 30/60/90 Ramp Plan: Developer Advocate (starts March 2)

**Two assumptions made to tighten this** (flag for veto before circulating — full interview wasn't run given the Friday deadline):

- **Funding driver:** developer enablement + product input (the pair a product-led motion typically funds — swap this if the role is actually funded to drive outbound adoption or sales enablement instead).
- **Metric:** self-serve activation — time from signup to first working alert/dashboard, and the top recurring onboarding friction points, since that's what a PLG API-observability product with ~400 self-serve teams lives or dies on. Substitute your team's actual north-star if different.

Each phase below replaces a vague activity list with a shipped artefact and a decision point — a ramp plan without a milestone is the one failure mode nobody catches until day 90.

---

## Day 0–30: Learn the product as a self-serve customer would

- Sign up and instrument a real service through Overtone's actual self-serve path — no internal shortcuts, no white-glove setup. Get to a first working alert and dashboard exactly as one of the 400 self-serve teams would.
- Meet: the eng/product owners of the signup and API surface, the support team fielding self-serve onboarding tickets, and 3–5 currently active self-serve customers (short calls or async).
- **Deliverable:** a friction log covering every confusing point from signup through first alert — each entry severity-rated with a proposed fix, handed to product/eng, not filed and forgotten.
- **Gate:** can explain the instrument → ingest → alert → dashboard workflow to a developer stranger with no notes, and can state the current activation baseline (time-to-first-value, or whatever the team already tracks) in one sentence.

## Day 31–60: Ship the first real artefact

- Ship one artefact in the enablement pillar — a rewritten getting-started guide, a reference integration repo, or a "here's how the top 3 friction points get fixed" doc — paired with an existing eng or docs owner, not solo.
- Land at least one fix from the day-30 friction log end-to-end: drive it through eng/docs review into production, not just log it.
- Produce a rough baseline number for the activation metric above — doesn't need to be polished, needs to exist.
- If outreach is genuinely part of this role's mix, replace "attend a conference" with a named, scoped output: one piece of public content (blog post or talk) drafted and scheduled against a specific CFP or publish date — an unscoped travel line item isn't a milestone.

## Day 61–90: Self-directed ownership of one named slice

- Own one recurring, explicitly scoped program slice without a pairing partner — e.g., the developer-facing changelog cadence, a monthly office-hours session, or the doc-fix pipeline for the top 3 recurring support tickets. **Not** "own the community" — handing a three-month-old hire an entire unscoped function with no team and no stated resourcing is the exact pit-trap pattern this kind of plan is supposed to avoid; if community ownership is the real long-term goal, name the specific slice of it this hire owns now and what's still out of scope.
- Deliver a written plan for the activation metric: target for two quarters out, and how it'll be tracked (dashboard, cadence, owner).
- Manager and hire jointly sign off in writing at day 90: continue at current scope, adjust it, or escalate a concern. Silence past day 90 is not an acceptable default outcome.

## Early-warning check

If the day-30 friction log, the day-60 artefact, or the day-90 metric baseline hasn't shipped on schedule, that's a scheduled conversation, not an unstated grace period.