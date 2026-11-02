## Two claims to kill first

**⚠️ "Developers are extremely price sensitive" — not a measured fact.** It is a widely repeated practitioner belief with no control-group study behind it (source: this skill's own evidence base, which lists it explicitly as a claim deliberately not used). Stephen O'Grady's *New Kingmakers* argument is real but narrower: developer adoption **precedes and drives** the org purchase — a sequencing claim, not a price-sensitivity claim. Capping *everything*, including the bank rung, at $9/month is not a pricing strategy — it's this unproven belief given veto power over your enterprise revenue.

**⚠️ "The dollar amount where a card swipe becomes procurement" — no verified number exists.** Personal-card → corporate-card → procurement is a real escalation, but the specific thresholds attached to it in practitioner folklore are unsourced. Worse: for a **data-sync product**, a bank's security review usually triggers on *what the product touches* (data flow, residency, audit boundary), not on invoice size. A sync engine moving records between devices and servers is exactly the category third-party risk review exists to catch — pricing $1 under a guessed number won't route around it. Ask Fernbrook's actual prospective bank buyers where their own threshold sits; that number is internal to them, not a market constant.

Building the real architecture below instead.

## Assumptions replacing the live interview

The skill asks these one at a time; answering as a one-shot deliverable, so flagging substitutes instead of blocking on them:

- Model: hosted sync/relay service, client protocol likely OSS (typical of this category — PowerSync, ElectricSQL). **Confirm** — this sets the self-host ceiling.
- Buyer split: indie dev on personal card (self-serve) vs bank platform team (procurement, security review, SSO/audit/residency required regardless of price).
- No stated deadline → treating this as a compounding-asset build, not a one-quarter revenue grab.
- No usage data yet → pricing from floor + ceiling, labelled an experiment with a review date, per step 4's "no data" path.
- All dollar figures below are **illustrative**, not Fernbrook's real COGS. Real numbers replace them before this ships.

## Value metric

Applying the five tests to a sync engine's natural candidates:

| Candidate | Value-correlated | Already counted | Forecastable | Non-perverse | Cost-correlated |
|---|---|---|---|---|---|
| Seats (console access) | no | partial | yes | yes | no |
| Sync operations/mutations | yes | no | no | **no** — punishes retries/heartbeats | yes |
| Monthly Active Synced Users (MASU) | yes | yes — teams already track their own MAU | mostly | yes, if defined as distinct identities not connections | yes, loosely |
| Data synced/stored (GB) | yes | partial | poor early on | yes | yes, strongly |
| Concurrent devices / "spaces" (capacity) | weak | yes | yes | yes | weak |

Sync-operation count fails the same way "test runs" failed in the reference case: billing raw ops rewards bundling and chatty-vs-clean engineering gets punished. **Reject as headline unit.**

**Three candidate architectures**, in the order the skill requires:

1. **Capacity only** (device cap + project count). Cheapest to ship — no metering pipeline. Underprices a bank account processing 50x the data of an indie app on the same device count. Good for month one, wrong for month twelve.
2. **MASU + data-volume hybrid** *(recommended)*. Platform fee → included MASU allowance → metered overage per MASU block, with a secondary per-GB meter so one data-heavy account can't hide inside a light MASU tier. Tracks cost, tracks value, expands without a new sale. Needs a metering pipeline — a standing cost, not a one-time build.
3. **Pure seats**. Rejected outright — sync load comes from end-user devices, not from developers logging into a console. Seat count would sit flat while sync volume grows, the exact seat-collapse pattern the reference metric guide warns about.

**Build order** (no funded metering pipeline yet): ship on **architecture 1** now for self-serve revenue, instrument MASU/GB in parallel, cut over to **architecture 2** within two quarters once usage data exists. Do not billboard architecture 1 as final — it's the on-ramp, not the destination.

## Packaging ladder

| Rung | Buyer | Contents | Price shape | Trigger up |
|---|---|---|---|---|
| Free | indie dev, exploring | full protocol/SDK, 1 project, small device/MASU cap, 7-day offline queue, community support | $0, no card | growth past cap, or moving to production |
| Self-serve | indie dev, personal card | higher MASU/device allowance, longer offline retention, email support | published, instant | second team, or an admin who never syncs |
| Team | small org | roles, shared billing, multiple environments, basic SSO | published, annual option | security review, residency, SLA ask |
| **Enterprise** | **bank platform team** | custom IdP/SCIM, audit logs, VPC or self-hosted deployment, EU/US residency, SLA with credits, DPA, invoicing | "starts at $X", negotiated | — |

This is the rung a flat $9 cap deletes. A bank team doesn't want a cheaper price — it wants risk removed (audit logs, residency, an SLA it can put in front of a regulator). Deleting that rung doesn't make the deal cheaper; it makes the deal **unbuyable**, because nothing on offer answers what their procurement process actually checks for.

Never gate: core SDK, standard auth, basic SSO, usage visibility, data export, security patches — same list for both buyers, per the never-paywall list. Basic SSO sits at Team, not Enterprise; if SSO costs more than ~10% of the base price, that's the sso.tax bar breaking, a documented source of unprompted prospect complaints.

## Price points — floor and ceiling, per buyer (illustrative numbers)

**Floor** (marginal cost + margin target, modelled at the 90th-percentile account):

- Illustrative: $0.023/GB-month storage + $0.05/GB egress + ~$0.002/MASU relay compute + support hours.
- A light self-serve account (2,000 MASU, ~100GB/month synced) costs roughly **$13/month** to serve. At a 70% margin target (chosen deliberately below the 80% software median — sourced — because this is consumption-touching, and usage-only pricing models run a 62% median margin, sourced), the floor for that account sits near **$44/month**.
- A bank-scale account (hundreds of thousands of MASU) moves this cost by two to three orders of magnitude — this is exactly why one flat number can't cover both.

**Ceiling — four checks, lowest one wins:**

*Indie dev:* self-host = roll your own CRDT sync (Yjs/Automerge) + a relay server. Real infra cost is low (~$20–40/month), but conflict-resolution logic is notoriously hard to get right — most solo devs pay a premium over raw infra cost to skip building it. This is why a low self-serve price (plausibly in the $19–49/month band, maybe a $9 entry step) is *defensible* — not because "developers are price sensitive," but because the build-it ceiling for a small app genuinely sits low.

*Bank:* self-host = running the OSS core in-house, likely $150–400k/year fully loaded for infra + dedicated engineers (illustrative). Build-it-from-scratch ceiling is higher still. This ceiling is nowhere near $9 — pricing the enterprise rung in the mid-five to six figures ACV is defensible against it, and consistent with Christoph Janz's sourced heuristic that field-sales economics need roughly six figures of annual revenue per account before a human belongs on the deal.

If the lowest ceiling ever sits below the floor, that's a cost-structure problem — not a pricing problem. Check this per segment; don't average across segments, which is the mistake a single flat price makes invisible.

## Predictability (sync-specific)

- Calculator on the price page taking MASU, devices, GB/month.
- Live usage dashboard + `/usage` API, alerts at 70/85/95% of the limit plus an anomaly alert (self-set baselines).
- **Cap enforcement must never drop a user's local-first data.** Pausing *new* sync on overage is fine; deleting queued local writes on cap breach is an existential UX failure unique to this category — write this into the enforcement policy explicitly.
- Hard cap default on Free/Self-serve, soft cap default on Team/Enterprise, stated plainly.
- Itemized invoices: plan fee, included MASU/GB, overage at rate, credits — separate lines.

## Why the $9 flat-cap plan actually fails

1. Confuses the indie ceiling (DIY build cost, genuinely low) with the bank ceiling (self-host at scale, five to six figures) — they're different products by the skill's own framing, not different discounts.
2. Fails the floor check at bank scale — a heavy account's COGS alone exceeds $9, meaning every large account loses money by design.
3. Deletes the enterprise rung. A stalled bank deal on missing audit logs or an SLA is evidence to *build* that rung, not evidence the market won't pay more than $9.
4. Rests on an unmeasured belief the evidence base explicitly warns against repeating as fact.

## Next action

Send real COGS per GB-synced and per active device, and confirm whether the Fernbrook core is open-source. That replaces the illustrative floor numbers above with real ones and locks the self-serve price — everything else in this memo holds regardless.