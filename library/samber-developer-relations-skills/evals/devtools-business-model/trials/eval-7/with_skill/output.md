# Business model ranking — Ferrolane

Skipping the interactive interview: your brief already answers most of it. Two assumptions I'm making explicit rather than blocking on:

- **Buyer = an organization**, not an individual developer. "Signed paying customer" and AGPL-driven pain both point at a company, not a solo dev with a credit card.
- **Cost-to-serve for the 2 design-partner hosted instances is currently unquantified.** Fine for a ranking, not fine to skip before finalizing a hosted-model boundary later.

## Step 1 — Constraints

- **Licence already shipped:** AGPL-3.0, every contributor CLA'd since day one, Ferrolane owns copyright outright. This is the rarest prerequisite on the whole archetype page — it exists nowhere else in your stack of options.
- **Where it runs:** both today. You already operate a hosted instance (2 design partners), and the AGPL network-copyleft clause exists specifically because customers can also run it themselves. Nothing forces customer-side-only.
- **Who signs:** an organization. AGPL's obligation (release your modifications to anyone you serve over a network) is a legal/compliance problem companies feel, not one individual developers feel.

Wardley mapping: skipped. One component (the engine), not a multi-layer stack — nothing to map.

## Step 2 — Archetype pass

| # | Archetype | Verdict | Reason |
|---|---|---|---|
| 1 | Proprietary hosted SaaS | **Not distinct here** | The engine is already open; hosting it is archetype 3, not this one. |
| 2 | Open core | Possible, **premature** | Real option later, but a standing two-release-train job — not buildable by a 12-week deadline with 4 engineers. |
| 3 | Hosted open source | **Possible**, secondary | You already run it; 3 of 4 engineers are ex-SRE. Blocked from being *primary* by the missing support rota. |
| 4 | Support & LTS | **Blocked** | No support rota, none planned this year — explicit deletion. |
| 5 | Dual licensing | **Possible — top pick** | Prerequisite (CLA + full copyright) already satisfied. Nothing left to build. |
| 6 | Source-available | **Blocked** | No stated hyperscaler-absorption threat, and it buys nothing you don't already have via dual licensing — plus it's an irreversible lever, wrong tool for a 12-week clock. |
| 7 | Consumption metering | **Blocked** | "Nobody who could build metering and billing this year" — explicit deletion, no exceptions. |
| 8 | Ecosystem take-rate | **Blocked** | No two-sided liquidity, not close to existing. |
| 9 | Embedded/OEM licensing | **Blocked (for now)** | Deal cycles run longer than 12 weeks; also needs a BD function you don't have. Revisit once copyright leverage is proven via dual licensing. |

## Re-ranked for Ferrolane specifically

Default efficiency order puts dual licensing 3rd. Your context promotes it to 1st, for the exact reason the skill calls out: *"An AGPL codebase with a signed CLA promotes dual licensing to the top, since its prerequisite is the rarest one on the page."* You're not approximating that condition — you're a direct hit on it.

Two more re-ranks specific to you:
- No billing engineering this year deletes consumption metering outright, which would otherwise sit #1 on raw efficiency.
- Already operating a hosted instance + ex-SRE bench promotes hosted open source above where the default order puts it — but the missing support rota caps it at *secondary*, not primary, this quarter.

Result: **Dual licensing > Hosted open source > Open core**, everything else blocked or premature.

## Candidates, in order

### 1. Dual licensing — recommended primary
- **Sold:** a commercial licence exempting the buyer from AGPL's network-copyleft obligation.
- **Signs:** the organization's engineering lead or legal counsel — whoever is blocked from running/embedding the engine without releasing their own modifications.
- **Prerequisite:** already true. Full copyright ownership, CLA since day one.
- **Gives up:** nothing you have today. The AGPL release stays exactly as-is; you're not withholding or closing anything.
- **Fits the 12 weeks:** near-zero engineering — an enquiry page, a contract template, a lawyer on call. No billing system, no support rota required.
- **Fits "signed":** literally requires a signature. This is the one archetype where "signed paying customer" is the product, not a side effect.
- **Validation experiment:** add a commercial-licence enquiry page now; work your two design partners and any prospect who's raised the AGPL question directly. Pass condition: an inbound enquiry from an organization that genuinely cannot comply with AGPL, converting to a signed contract inside the 12 weeks.
- **Paid-boundary sanity check (all five pass):** organization-only (legal exposure, not a feature) · defensible without hostility (AGPL version stays fully intact, nothing to fork) · observable trigger (a company embedding/networking the engine without wanting to open their changes) · cost-to-serve near-zero (nothing hosted) · licence-compatible by construction.

### 2. Hosted open source — viable secondary, not this quarter
- **Sold:** running the engine for the customer — the two design partners are the beachhead.
- **Signs:** same buyer, different pain — wants convenience, not a legal exemption.
- **Prerequisite:** genuine operational burden for self-hosting, which a design-partner conversation can confirm directly.
- **Gives up:** ties up your ex-SRE engineers in ops instead of product for however long the rota takes to build.
- **Why not primary now:** it's a standing job (SRE + support rota), and you don't have the rota yet. Committing here first risks missing the quarter chasing infrastructure instead of a signature.
- **Sequencing:** stands up cleanly *after* dual licensing lands — it doesn't compete with it. Dual licensing monetizes "we must self-host and can't take on the copyleft obligation"; hosted open source monetizes "we don't want the operational burden." Same licence, two different buyer motivations, not a conflict.
- **Validation experiment:** waitlist/indicative-price conversation with the two existing design partners. Pass condition: at least one converts to a paid pilot at a unit cost inside your intended margin.

### 3. Open core — premature, revisit in ~2 quarters
- **Blocked by:** the standing two-release-train discipline it demands, which a 4-person team can't absorb alongside a 12-week signature deadline.
- **Revisit trigger:** once dual licensing proves organizations will pay to avoid AGPL obligations, that same signal (who's asking, why) tells you which proprietary modules (SSO, RBAC, multi-tenant management) are worth building.

## Recommendation

**Primary: dual licensing.** It's the only model on the page that requires nothing you don't already have, matches "signed" literally, and fits inside 12 weeks. **Secondary, sequenced after: hosted open source**, using the two design partners as the first conversion target once a support rota exists — don't start it before the quarter closes, or it'll eat the runway you need for the actual deadline.

Two things worth closing before this is final, not before you act on it: confirm the buyer really is organizational (not, say, a platform team inside a larger org with different signing authority), and put a real number on cost-to-serve for the hosted instances before hosted open source becomes anything more than a secondary on paper.