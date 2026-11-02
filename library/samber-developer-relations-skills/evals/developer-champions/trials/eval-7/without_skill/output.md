Before you lock the announcement date, the cohort composition changes the risk profile completely — three of your seven people work for institutions with formal compliance regimes around vendor gifts, vendor software, and public statements. A generic champions playbook (welcome box, NDA, "post 4x/year") is built for independent developers, not for employees of a bank, a hospital network, and a federal contractor. Tighten these four things first.

## 1. The $900 welcome box is your biggest single risk

Retail banks, hospital systems, and federal contractors virtually all cap what an employee can accept from a vendor — often $25–100, sometimes zero without disclosure or written approval.

- **Bank employees**: 18 U.S.C. §215 (the Bank Bribery Act) specifically targets gifts from anyone doing or seeking business with a bank to its employees. $900 is far above any de minimis threshold and could trigger a mandatory disclosure — or a violation — on their side, not yours.
- **Federal contractor employee**: many contractors flow down FAR/DFARS-style business-conduct policies with hard gift caps, precisely because *their* customer is the government. If Vaultmere is or could become a vendor with any nexus to that contract, this gets scrutinized as a potential improper inducement.
- **Hospital network employee**: even non-clinical IT/platform staff usually sit under a vendor-gift policy driven by the org's broader compliance culture.
- Fix: **don't ship a uniform $900 box to this cohort.** Either drop it to a value under typical corporate thresholds (~$50–100, per the skill guidance that champions want quality, not lavish), or explicitly ask each of the four affiliated champions to clear the gift with their own compliance/ethics contact before you ship anything. Do this now — a "no" three weeks out is much cheaper than a "no" the week of announcement. The three independents aren't subject to this at all; treat them differently rather than picking one box value for everyone.

## 2. Pre-release builds of key-management infrastructure need a "where does this run" answer

This isn't devtool swag — it's unreleased, unaudited security-critical infrastructure. Before you hand out builds, know:

- Is each affiliated champion running this on **personal hardware/sandbox**, or inside their **employer's environment**? If it's the latter, you're putting pre-release KMS code inside a bank's, hospital's, or federal contractor's environment without going through that org's own vendor security review (SOC2/TPRM intake, change control, and for the contractor possibly DFARS 252.204-7012-style supply-chain requirements). That's a problem for *their* employer, and it comes back on you as the vendor who enabled it.
- Your "standard company-wide partner NDA" is written for corporate partners, not individuals acting outside their employer's procurement process. It likely doesn't address personal-capacity participation, doesn't confirm the individual isn't violating their own employment agreement (side agreements with vendors, IP assignment) by signing, and doesn't specify environment restrictions.
- Fix: add a short addendum for the four affiliated champions only — testing is personal-sandbox only, never employer production/dev environments, and they represent that participation doesn't conflict with their employer's policies. Independents can stay on the standard NDA.

## 3. The "post about 4 launches a year" expectation collides with employer comms policy — and with OPSEC

- Bank, hospital, and federal-contractor employers commonly require legal/comms pre-clearance before an employee publicly names a vendor, especially for security infrastructure — disclosing "we use Vaultmere KMS" is itself a disclosure about the institution's security posture.
- For a company that sells key management to attackers'-favorite targets, a public list of "here are the specific banks/hospitals/contractors and the named engineers using our KMS" is a target map, not just marketing. Decide deliberately whether champions post as themselves-with-employer-tag or personal-capacity-with-disclaimer ("views my own, not my employer's") — don't leave this ambiguous.
- Separately, per how these programs actually work: **a hard quota ("post 4x/year") is a known way to burn out champions and make it feel like unpaid work** rather than advocacy. Make posting something you invite and support when they want to, not a deliverable they owe you — especially since three of your four affiliated champions may not be able to promise it anyway once their employer's comms policy is in the loop.

## 4. Resolve the NDA-vs-posting timing conflict explicitly

You're simultaneously asking for an NDA on pre-release material and a public post about the launch. Spell out in the agreement exactly when the NDA lifts relative to GA — otherwise a champion posting on launch day risks technically breaching the NDA on pre-release details they saw weeks earlier, and you risk a leak if the boundary isn't crystal clear to them.

## Sequence for the next three weeks

1. **This week**: send the four affiliated champions a short note asking them to check their own gift, vendor-software, and social-media policies before you ship anything or send builds. Get a yes/no back before proceeding with them specifically.
2. **In parallel**: cut the welcome box to a defensible value, or make it conditional per-person on step 1's answer.
3. **Before shipping builds**: confirm sandbox-only testing in the NDA addendum for affiliated champions.
4. **Before announcing**: turn "post 4x/year" into an invitation with employer-disclaimer language, not a quota, and decide your policy on naming affiliated champions' employers publicly.
5. Independents need none of this — ship their box and NDA as planned.

What's fine as-is: the cohort mix itself (mostly independents plus a few high-signal enterprise names is a reasonable champion shape), and the cadence of four launches a year to rally around.