**Bottom line:** Co-found a neutral spec. Don't Drive alone. 9 people, 14-month runway, 1 customer — can't fund a standards war solo. Borrow assets from allies instead of owning none. Win on the layer above the wire protocol, give the protocol itself away free.

**Do this month (cap 5):**
1. Name one owner for the standard effort. Part-time ok. Must be a real name, not "the team."
2. List 5-10 targets to recruit as co-founders: independent gateway vendors, integrators, other Aurelen-fatigued buyers.
3. Publish spec text + your reference implementation on a Git repo. Community-Specification-style licence. Royalty-free.
4. Ask the utility (40,000 gateways) to co-sign the launch publicly. Their name is your best asset.
5. Ship a conformance test suite v0. Self-service. Free.

**Landscape:**
- Specs: EdgeSync (Aurelen, proprietary, no public venue, ~80% deployed gateways, 11 yr). Brindle's protocol (new, 1 implementation, no venue yet).
- Implementations: EdgeSync's 80% is Aurelen-controlled, not independently governed. Brindle: 1, itself.
- Demand: 1 named account — the utility, 40,000 gateways, actively anti-Aurelen. No other named account yet.
- Conformance suite / cert mark: none exist for either spec.

**Why Co-found, not Drive:**

Classify the fight first (Shapiro & Varian). EdgeSync is compatible with itself — it's the installed base. Brindle's protocol is not compatible with EdgeSync. That's **Revolution vs Evolution**. The framework's own rule: the compatible incumbent wins slow, by default, unless the challenger has overwhelming performance or a coalition.

Score the 7 assets:
- Installed base: Aurelen 80%. Brindle 1 customer (recruitable — a big customer controls part of the installed base too).
- IP rights: neutral, no big patent blockers either side.
- Ability to innovate: Brindle maybe faster, unproven at 80%-share scale.
- First-mover: Aurelen, 11 yr.
- Operating-cost capability: unknown — don't assume either way.
- Strength in complements: Aurelen owns the 2 fleet-management products bought alongside EdgeSync. This is the real lock, bigger than the protocol itself.
- Brand: Aurelen wins the broad market. Brindle wins only the Aurelen-fatigued segment.

4 of 7 favor Aurelen outright. Brindle holds a sliver of 1. Proposing Drive alone on this asset count is choosing a war you can't fund. Co-found buys assets 1, 6, and 7 back cheaply, by recruiting them instead of owning them.

**Options considered:**

- **A — Co-found, Git-based, royalty-free, fast. (Recommended.)** Cost: shared governance forever, no direct protocol-licensing revenue. Buys: kills "just Brindle's private format" — the one objection blocking your second customer — fast and cheap.
- **B — Drive alone, publish openly, keep control.** Cost: none of your 7 assets improve. "Who else runs this" stays unanswered the whole 14 months. This is exactly the losing shape the framework describes: Revolution, no coalition, hope performance wins.
- **C — Build a compatibility bridge so EdgeSync gateways can run your protocol without a flag-day switch.** Cost: engineering time you don't have, plus legal risk reverse-engineering Aurelen's closed protocol — get counsel's view first. Buys: removes switching cost for buyers still mid-contract with Aurelen. Demote to a stretch goal, fund only once A is on track.

Rejected outright: **Ignore** (real named demand exists — one customer already recruited; doing nothing forfeits the one asset in hand). **Extend / stay proprietary** (fails the commoditization test the moment your revenue plan moves to the layer above the protocol — staying closed caps you below your own stated goal of "get the whole ecosystem on it").

**Venue + IP:**
- Git-based community spec. Weeks, near-zero cost. Matches your clock — IETF/W3C/OASIS/ISO all take years, skip them now.
- Royalty-free patent grant. Lowest adoption cost for other implementers; the only mode that lets resource-strapped vendors build without a legal review cycle they also can't staff.
- Keep the trademark separate from spec governance. Register the mark yourselves even while co-founding the spec.
- Escalate one venue right (foundation-hosted) only if a named co-founder refuses a Brindle-owned repo. Watch for an ISO trigger if a utility-sector regulator later demands a standard number — don't act on it yet.

**Conformance:** versioned mark tied to spec v1.0, self-service testing, free, one public registry page. That registry is the artifact that answers "who else runs this."

**KPIs, review at month 12:**

| Metric | Threshold | Source |
|---|---|---|
| Independent interoperating implementations | 2 | Sourced — RFC 6410 §2.2 |
| Implementer beyond Brindle + the pilot utility | 1, within 12 months | Baseline — sized to your 14-month runway |
| Deals/RFPs naming the open spec itself | any, beyond the 1 utility | Baseline |

**Kill rule:** still 1 implementer (you) at month 12 → de-escalate to Extend. Stop spending runway on governance/ecosystem work. Keep the protocol as a documented, Brindle-controlled product feature. The utility keeps full support under your product roadmap regardless — de-escalating the standard doesn't touch what you already owe the customer live on it.

⚠️ **Legal flag:** Option C (compat bridge) touches reverse-engineering a competitor's closed protocol. Get counsel's view before writing code, not after.

**Next:** name the owner today. Send the first co-founder recruiting email this week.