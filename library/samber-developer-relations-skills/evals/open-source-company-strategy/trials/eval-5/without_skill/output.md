## Should Lindgren open-source the HL7 connector?

**Short answer: probably yes, but not for the reason on the table, and not the way it's being framed.**

The account manager's "just do it, it's goodwill and nobody likes maintaining it" reasoning is wrong on both counts, and the QBR framing ("our biggest account wants it") is the wrong trigger for this decision. Treat it as a build/GTM call, not a renewal favor.

### Decouple it from the renewal

The renewal isn't conditioned on this and closes in October regardless. There's no deal risk forcing a rushed yes. Making the call under QBR pressure means making it on incomplete information — skip that. Also: two other customers in the same regulated segment independently want this. That's not one account extracting a favor, that's a repeated market signal. That's the actual reason to consider it — not "keep our biggest logo happy."

### The real question is what's actually in those 6,000 lines

An HL7 connector for a *normalization platform* is very likely plumbing — parsing/transport for a 30-year-old messaging standard — not the differentiated part of the product. The value you sell is presumably the normalization/mapping/validation engine downstream of it. If that's true, giving away the connector costs you little competitively; you're not handing anyone your moat. Standard, well-trodden pattern in this exact shape: open the adapter, keep the engine. Confirm this before deciding — if any proprietary mapping logic, terminology handling, or business rules got quietly folded into the "connector" over time, that part needs to stay closed or be extracted first.

### Non-negotiable before anything gets published

This is healthcare data. Before any code goes public:

- **Audit and strip** every hospital-specific config, credential, endpoint, custom field mapping, and test fixture. Six years of glue code accumulated by engineers fixing real customer issues is exactly where a hospital's internal system quirks, sample messages, or connection strings end up hardcoded or left in comments/tests. That's the actual risk here — not the license, the leakage.
- **Legal/security review**, not just an engineering sign-off, given the segment. Hospitals' own security teams will diff this against what runs in their environment once it's public.
- Decide the **support boundary explicitly**: community-supported, no SLA, no implied uptime/patch commitment. Publishing code that sits in a clinical data path without stating this invites customers to assume you owe them CVE response times you never agreed to.

### Don't let this set a precedent

If this ships because "our biggest account asked at a QBR," every other large account now knows that's a lever. Reframe it internally and externally as a deliberate ecosystem decision ("we're open-sourcing our HL7 adapter because interoperability plumbing shouldn't be a moat, and three customers in this segment need it") — not a concession won in a negotiation. Say this to the Nordic account directly: you're doing it because it's the right call for the segment, not because they asked. That's a small wording difference with a real effect on what every other €400k+ account learns is negotiable.

### Maintenance burden — don't count on this fixing it

Enterprise-vertical open source connectors rarely attract meaningful outside contribution. Expect to keep paying full maintenance cost internally, plus new overhead: triaging external issues/PRs, a public disclosure process for bugs, and possibly the reputational cost of a stale-looking public repo if it's not tended. The "nobody enjoys maintaining it" motivation is a reason to consider refactoring or better-owning it — it is not, by itself, a reason to open-source it. Don't let it substitute for the actual analysis above.

### Recommendation

1. Pull the connector code and confirm it's genuinely commodity plumbing with no proprietary mapping logic inside it.
2. Run a security/legal pass to strip customer-specific material.
3. If clean, publish under Apache-2.0, community-support-only, positioned as a segment-wide interoperability contribution — not a Nordic-account concession.
4. Tell the account manager to stop using "goodwill for the renewal" as the rationale in front of the customer; the renewal doesn't need it and framing it that way is the part that creates precedent risk.