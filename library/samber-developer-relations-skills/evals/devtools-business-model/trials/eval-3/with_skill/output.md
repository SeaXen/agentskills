Using the **devtools-business-model** skill. Its own instructions are explicit about this exact request — a canvas is refused as a first move ("Fill in a business model canvas for our CLI → refuse the framing before filling anything... run steps 1-3 instead. Produce the canvas afterwards if the user still wants one"). Since this has to land as one complete deliverable rather than an interview, I've run steps 1–3 against labeled assumptions (⚠️ marks what to verify before Thursday) and built the canvas on top of that, rather than on adjectives.

---

## Why not just the canvas

A canvas fills nine boxes without asking the three things that actually decide a devtool's model: what's already published, where the software runs, and whether any paid boundary can hold. Skipping that produces a canvas that looks complete and commits to nothing. Here's that groundwork, compressed.

**Constraints**
- **Licence already shipped:** BSD, two years of releases. Permissive — this permanently rules out dual licensing (no forcing function) and makes any future relicensing a trust-destroying, effectively irreversible move, not a lever to hold in reserve.
- **Where it runs:** ⚠️ assumed — the CLI/agent talks to devices on the customer's network today, no vendor-hosted backend exists yet. Edge devices themselves must stay customer-side (data gravity, often behind corporate or industrial networks). That does *not* rule out a hosted **coordination/visibility layer** reaching devices via outbound-only agents — common in this category (balenaCloud, Teleport, FleetDM) — so hosted models stay in play for the control plane, not for the devices.
- **Who signs:** ⚠️ assumed — "fleet" implies an org buyer (platform/infra team), not an individual managing one device. Individuals stay the adoption base, not the payer.

**Brainstorm, eliminated with reasons**
- *Dual licensing* — dead on arrival: BSD is permissive and already published.
- *Ecosystem take-rate* — no third-party plugin marketplace exists; premature.
- *Embedded/OEM* — no evidence anyone wants to embed this inside their own product; it's an operator tool, not a component vendors ship.
- *Source-available* — no confirmed hyperscaler is reselling this specific software as a service; general IoT-platform competition (AWS IoT, Azure IoT Edge) is a product problem, not a forking threat. Costs contributors for nothing bought.
- *Consumption metering as primary now* — nothing is instrumented yet, no billing engineering exists. Real candidate for the value metric later, not a standing primary today.

**Survivors, in efficiency order for this shape:** open core (hosted control plane as the boundary) as primary, support & LTS as secondary for accounts that can never send fleet data out.

**Paid-boundary test on that primary**
1. Organization-only — pass: multi-tenant dashboard, RBAC/SSO, audit trail, orchestrated rollout policy are org needs; a lone operator on a handful of devices doesn't need them.
2. Defensible without hostility — pass: a multi-tenant, SSO/RBAC/audit hosted service isn't a weekend fork.
3. Observable trigger — ⚠️ unresolved: the fleet-size or multi-team threshold where ad hoc scripting breaks down isn't known. Needs opt-in telemetry before pricing anything.
4. Cost-to-serve — ⚠️ unresolved: nothing is hosted today, so per-device ingestion/control-plane cost is unmeasured. Per the skill's own rule, an unmeasured free-tier cost means the model is untested, not proven.
5. Licence-compatible — pass: the control plane is new proprietary code; BSD core stays free forever, no relicense needed.

Two of five gates are open. That's the honest state of the model going into the board meeting — worth saying out loud there rather than papering over it in the canvas.

---

## Business model canvas — Lanternctl

**Key Partners**
- Edge-hardware and device OEMs / ODMs (reference images, pre-integration).
- Systems integrators and MSPs who deploy and operate fleets for retail, industrial, telco and logistics customers — the likely resale/referral channel once a paid tier exists.
- Package ecosystems (Homebrew, apt/yum, Go module proxy) for open-source distribution.
- Hyperscaler IoT platforms (AWS IoT, Azure IoT Edge) — treat as coexistence/integration targets, not channel partners; they compete at the platform layer.

**Key Activities**
- Maintain and release the BSD CLI/agent — the adoption and credibility engine.
- Design, build and operate the hosted fleet control plane (inventory, orchestrated updates, RBAC, audit) — does not exist yet; this is the actual build.
- Instrument opt-in telemetry to find the real paid-boundary trigger before pricing it.
- Backport and security-patch engineering for the support/LTS secondary.
- Community maintenance (issue triage, docs) to keep the free layer credible regardless of which paid layer ships.

**Value Propositions**
- Free (BSD): vendor-neutral, scriptable, auditable control over edge devices with no lock-in — the reason two years of adoption exists.
- Paid: fleet-wide visibility and control at the organization level — inventory, orchestrated rollouts, guardrails, RBAC/SSO, audit trail, uptime — removing the operational and compliance risk of coordinating many devices, sold to the team that owns the fleet, not the engineer running one.

**Customer Relationships**
- Free CLI: self-serve, community-supported (GitHub, docs, chat).
- Paid control plane: inside sales once a fleet crosses the (currently unknown) size trigger.
- Regulated/air-gapped accounts: named-account, procurement-driven relationship built on the support/LTS contract, not the hosted product.

**Customer Segments**
- Individual developers / small teams — adoption base, not payers.
- Platform and infra teams operating device fleets at scale (retail POS, industrial IoT, telco edge, logistics) — the paying organization.
- Regulated or air-gapped operators (defense, healthcare, critical infrastructure) who can never send fleet telemetry to a vendor cloud — support/LTS segment.

**Key Resources**
- The BSD codebase and its two years of adoption/reputation.
- Engineering capacity to build and operate a hosted service — a gap today, not an existing asset.
- Opt-in telemetry / usage data to find the paid-boundary trigger — doesn't exist yet.
- Any existing design-partner or pilot relationships to validate the boundary before building it out fully.

**Channels**
- GitHub, package registries, the CLI's own docs site — organic open-source discovery and activation.
- Direct/inside sales for the hosted control plane once built.
- Field sales / procurement path for support & LTS.
- SI/MSP partners as an indirect route into large existing fleets.

**Cost Structure**
- Core OSS maintenance (engineering time, CI, releases) — today's baseline, currently unrecovered by revenue.
- Hosted control-plane infrastructure (compute, storage, device-telemetry ingestion) — cost-to-serve unmeasured; quantify before pricing.
- Support/LTS: backport engineering and an on-call/support rota — a standing headcount cost not incurred today.
- Community/DevRel overhead to keep the free layer trustworthy under either paid layer.

**Revenue Streams**
- Today: none.
- Primary candidate: subscription on the hosted fleet control plane, priced on enrolled/active managed devices — the fleet-size number customers already track themselves.
- Secondary candidate: support & LTS contracts (SLAs, backports, indemnification) for self-hosted/regulated fleets.
- Deliberately excluded: dual licensing, ecosystem take-rate, OEM licensing, source-available — each with a named reason above.

---

**Before Thursday, confirm these — the canvas is only as good as they are:**
- ⚠️ Does a hosted backend already exist in any form, or is this fully greenfield?
- ⚠️ Real cost-to-serve for one hosted device connection, in currency.
- ⚠️ The fleet-size or multi-team threshold that actually makes self-hosted coordination hurt (needs telemetry, doesn't exist yet).
- ⚠️ Whether any inbound support/LTS or hosted-pilot interest already exists — the cheapest evidence you could bring into the room.

**Leading indicator to propose to the board:** self-host-to-paid-pilot conversion among fleets that hit the size/multi-team trigger, once instrumented — read monthly, not GitHub stars or downloads.