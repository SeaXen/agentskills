## The actual fight isn't "our protocol vs. their protocol"

Aurelen doesn't make money from EdgeSync. EdgeSync is the tollbooth that protects the two fleet-management products everyone buys alongside it. As long as EdgeSync is the only thing gateways speak, Aurelen owns the toll road. You will lose if you compete as "a better EdgeSync" — you have no path to 80% share in 14 months, and Aurelen can cut price or bundle harder faster than you can burn cash.

You win by **commoditizing the protocol layer**, not by capturing it. Make the thing Aurelen currently charges rent on free, boring, and multi-vendor. That doesn't kill Aurelen directly — it kills the reason the fleet-management bundle is mandatory, which is the actual asset you're attacking. This is the same move Google made open-sourcing Android to commoditize the OS layer Apple was using to lock in the App Store, or Facebook made open-sourcing server designs (Open Compute) to commoditize Dell/HP's hardware margin. You're not trying to become the incumbent. You're trying to make incumbency stop mattering.

Everything below follows from that one bet.

---

## 1. Don't ask anyone to rip out EdgeSync — ask them to also speak yours

Nobody with 80% share loses a forced-migration fight to a 9-person company. So don't start one. Position the open protocol as **dual-stack, zero-risk to add**: gateway OEMs keep shipping EdgeSync support (their existing customers need it) and add your protocol alongside it, at near-zero marginal engineering cost, because *their* customers (utilities, industrial operators) are starting to demand vendor optionality.

This is the wedge. You're not selling replacement, you're selling insurance against lock-in. That's a much easier yes for a hardware OEM than "abandon your biggest partner's ecosystem."

Make this technically true, not just a talking point: ship a reference implementation clean enough to embed alongside an existing EdgeSync stack without a rewrite. The reference implementation *is* the marketing. If integrating it takes an OEM engineer more than a week, you've already lost the OEMs you need most.

## 2. Get the spec and trademark out of Brindle's hands, fast

This does two things at once, and both matter more than they look at first:

- **It answers the only real objection a gateway OEM or fleet-management vendor has**: "why would I build against a 9-person startup's private roadmap that might not exist in 18 months?" A protocol owned by Brindle is a supplier risk. A protocol owned by a neutral, multi-party working group is infrastructure.
- **It's your insurance against the single biggest existential threat you have**: Aurelen buying you and quietly burying the standard, or just waiting out your runway. If the spec, the trademark, and the reference implementation live in a foundation before that conversation ever happens, acquiring Brindle doesn't buy control of the protocol. This is exactly why Let's Encrypt is a nonprofit and why the Kubernetes trademark sits with CNCF, not Google.

You don't have time for a multi-year IEEE/IETF standards track — that's a legitimacy layer to pursue in parallel, not a launch prerequisite. Faster paths that are real and precedented:

- A lightweight, purpose-built working group (GitHub org + public spec repo + a steering committee with named co-founding companies) — this is enough to be credible on day one.
- **UCAIug** (UCA International Users Group) or **NAESB** — both are real, utility-sector-specific standards bodies already trusted by utility security/compliance reviewers. Given your beachhead customer is a utility, this is a much stronger legitimacy signal than a generic dev-tool foundation, and it puts you in front of exactly the buyers you need.
- Linux Foundation Edge / a fiscal-sponsorship nonprofit, if you want general-purpose IT credibility instead of utility-specific.

Recruit 2-4 co-founding organizations before you launch publicly — ideally smaller edge/gateway vendors who also live under Aurelen's thumb. "Enemy of my enemy" alliances are how Matter got Amazon, Google, and Apple to cooperate, and how ONVIF got competing camera vendors to agree on an interop standard specifically to blunt one dominant player. You need this to stop being "Brindle's protocol" before your first press mention.

## 3. Your utility isn't a customer. It's a procurement weapon.

A 40,000-gateway utility that hates Aurelen is worth more than any amount of content marketing you could produce in 14 months. Use it exactly the way OCPP broke proprietary EV-charging lock-in and OpenADR broke proprietary demand-response lock-in: **get the open protocol written into procurement language.**

Concretely:
- Help them get "must not require a single proprietary vendor protocol" or explicit support for your spec into their next gateway/hardware RFP. Utilities write multi-year technical requirements into tenders as a matter of course — this is a normal, unremarkable ask for them, not a favor.
- Once that RFP language exists, it becomes your sales pitch to gateway OEMs: not "please consider adding our protocol" but "a utility with 40,000 gateways now requires this to bid." That converts an optional favor into a commercial necessity, which is the only kind of argument that moves OEM roadmaps on your timeline.
- Push for a joint case study and a conference slot at **DistribuTECH, EPRI, or UTC Telecom & Technology** — utility-industry venues where the audience is other utility procurement people, not a generic dev crowd. Utilities benchmark vendor decisions against peer utilities constantly; one credible reference utility talking about de-risking vendor lock-in is worth more than anything you say about yourselves.
- Don't attack Aurelen by name in anything public. Let the utility's own frustration carry that message — it's more credible coming from a buyer than from a challenger, and it keeps you out of a fight you can't win on volume.

## 4. Beachhead on utilities/critical infrastructure. Don't chase "all edge devices."

You have 9 people and 14 months. A generic "config-sync for any edge device" positioning spreads you across every OEM conversation, every vertical, every use case — and none of it compounds. Utilities talk to utilities, share vendor risk assessments, and face the same regulatory pressure (NERC CIP, IEC 62443) that makes "proprietary single-vendor protocol in critical infrastructure" a real, nameable risk to a security reviewer. That pressure doesn't exist the same way in, say, retail IoT.

Go deep on one vertical where your one great reference customer gives you compounding leverage, instead of broad on a market where you have none.

## 5. Close the trust gap that actually stops adoption

Before asking any OEM to bet a roadmap slot on you:
- Run a freedom-to-operate check against Aurelen's patents from 11 years of shipping. Getting sued over protocol design is exactly the kind of thing that kills a 9-person company outright, and it's cheap to check now versus catastrophic to discover later.
- Publish an explicit non-assertion / patent pledge for the spec, so adopters know they can't get sued by you either — this is a real, standard move for exactly this situation (see the VP8/VP9 patent-pool fights that scared off early adopters until a pledge was in place).
- Ship a conformance test suite alongside the spec, not just docs. For a utility security reviewer, "there's a test suite proving interoperability" is worth more than any whitepaper.

## What not to do

- Don't out-market or out-spend Aurelen on brand. You lose that fight on cash alone.
- Don't demand rip-and-replace. You have no leverage to win a forced migration against 80% share.
- Don't wait for a full formal standards-body process before launching. Lightweight governance now, formal legitimacy in parallel.
- Don't make Brindle's own product the only thing that consumes the open protocol. If the "open standard" is transparently a funnel into Brindle's paid product, other Aurelen competitors won't help you fight for it, and OEMs will read it as vendor lock-in with extra steps. The protocol needs to be genuinely useful to competitors of Brindle too — that's what makes it a standard instead of a marketing wrapper.
- Don't spread across verticals. Utilities first, everything else later.

## Sequence against your 14-month runway

| Window | Focus | Exit signal you need to hit it |
|---|---|---|
| M0-2 | Freeze v1.0 spec, permissive license (Apache 2.0), production-grade reference implementation built for dual-stack install. Recruit 2-4 co-founding orgs for governance. | Spec + reference impl good enough that an OEM engineer can integrate in under a week. |
| M2-4 | Public launch: spec, GitHub org, steering group named. Trade press in utility/industrial-IoT channels, not general tech press. | 1+ credible non-Brindle name attached to governance publicly. |
| M3-6 | Push utility toward joint case study + conference slot (DistribuTECH/EPRI/UTC). Start FTO/patent-pledge diligence. | Utility agrees to co-present or be named publicly. |
| M4-9 | Direct, hands-on integration support to 5-10 second-tier gateway OEMs selling into utilities. Free engineering time, not sales calls. | 2+ OEMs shipping dual-stack support. |
| M6-12 | Convert utility's RFP cycle into OEM leverage: "this is now a bid requirement." | RFP language exists and is citable. |
| M9-14 | Assess and raise: second reference customer in pipeline? Independent foundation home functioning? 2+ OEMs live? | These three are your Series A story — "we made the incumbent's lock-in optional," not "we out-competed an 11-year player." |

## The tension to hold consciously

Every one of these moves trades control for adoption: putting the spec in a foundation, going dual-stack instead of demanding migration, recruiting Aurelen's other competitors as co-owners. Each individually weakens Brindle's grip on "its" protocol. That's not a bug — a protocol Brindle fully controls is a protocol no one else will build a business on top of, which is the exact trust problem you're trying to solve. The discipline for the next 14 months is resisting the urge to claw control back the moment the ecosystem play starts working — that's the point where founders usually panic and re-centralize, and it's exactly when the OEMs and co-founding orgs will notice and walk.