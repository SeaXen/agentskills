**App model: no. Not as installable third-party apps (rung 5). Works as partner-listed integration (rung 3) — but only after you confirm one thing: real API behind that CSV export, not just CSV export.**

Numbers match Case A in this skill's own worked examples (40/300 accounts, 25% attach, rung 3 chosen) almost exactly — except your case has thinner demand breadth (1 complement vs 7), 2x their build time, and no visible platform-security team. If that case didn't clear rung 5, yours doesn't either.

---

# Ecosystem strategy — Parcelwise

## Hypothesis

Because customers need **carrier-rate comparison** we won't build, **rate-comparison ISVs** will build it on **a Parcelwise API/webhook surface**, earning **~$5,000/year per attached customer**, making Parcelwise more valuable to **ops buyers** by **closing the rate-shopping gap without us maintaining carrier feeds**.

No vague blanks. Commoditized complement: rate comparison. Open flag (G4 below): confirm this doesn't overlap your own routing-cost roadmap.

## Evidence

- 4 customers already built unsupported rate-comparison spreadsheets glued to your CSV export. Strongest evidence tier this skill recognizes.
- "Everyone asks for it" — real but uncounted. Only one complement named, not five.
- 2 ISVs in active talks, quoting build cost themselves. Real conversations, not personas.
- 2 agencies offered to build — **only if paid**. That's a services quote, not demand evidence.

## Gates

| Gate | Verdict | Why |
|---|---|---|
| G1 Counted demand (this complement) | **Pass** | 4 DIY builds, strongest evidence tier |
| G1 Counted demand (ecosystem breadth) | **Fail** | 1 complement named, skill default wants 5 |
| G2 Externalizable interfaces | **Unknown** | Only CSV export confirmed. Real API/webhook status unstated. Resolver: audit current API surface, 1 week |
| G3 Identified builders | **Pass** | 2 named ISVs, real talks |
| G4 Commoditized complement, not core | **Unknown** | Rate comparison sits near routing-cost logic. Resolver: does Parcelwise roadmap include cost-aware routing? Ask product lead |
| G5 Staffing | **Fail (assumed)** | No standing security-review/consent/revocation function mentioned. 260 accounts rarely carries one. Confirm with you |
| G6 Envelopment | **Unknown** | Vendors already live on a 9,000-customer logistics platform. Name that platform, check if it could bundle last-mile routing and threaten Parcelwise itself |
| G7 Complement readiness | **Pass** | Rate data/carrier APIs already proven live elsewhere |

G2 and G5 alone delete rungs 3–6 per this skill's own rule ("no security review function deletes installable apps," "can't expose stable interfaces deletes everything above vendor-built"). G2 is fixable fast; G5 is why rung 5 is dead regardless.

## Rung

**Recommended: Rung 3 — partner-built integration, listed by Parcelwise.** Conditional on G2 resolving yes (real API exists or gets built first — that's rung 1 work, cheap, do it regardless).

Rejected:
- **Rung 5 (installable apps, what you asked for)** — G5 fails (no standing review/consent team), G1 breadth fails (1 complement, not a portfolio), and half your "builder supply" (the agencies) isn't real complementor supply — they want payment, meaning fund them and you own the outcome, no ecosystem leverage.
- **Rung 4 (extension points)** — would fit if internal teams were your *only* positive signal. They're not; ISVs are also positive. Rung 3 captures more value at less cost.
- **Rung 2 (you build it)** — leaves money on the table: 2 ISVs already want to build this for free.

## Complementor case

| Line | ISV | Agency | Internal team |
|---|---|---|---|
| Reachable accounts | 45 | — | 4 (proven) |
| Attach rate | 25% (~11) | — | already active |
| Their return | $5,000/customer/yr → ~$56,250/yr | needs payment from you | none needed |
| Build cost | 12 person-weeks | n/a (you'd pay) | already sunk |
| Maintenance | 4 person-weeks/yr | n/a | ongoing DIY pain |
| Alternative | Sell into their existing 9,000-customer platform | do other paid work | keep CSV glue |
| Net return vs alternative | Positive but small — Parcelwise is <0.5% upside on their existing book | **Fails test** — "if we don't do this, nothing changes for them" unless paid | Positive — friction removal only |

Two flags:
1. **Agencies aren't complementors.** Paying them makes this rung 2 with contractors, not rung 3 supply. Don't count them toward "builder supply."
2. **ISV commitment risk is real.** They quoted the cost, but Parcelwise is a rounding error next to their 9,000-customer platform. Get a signed pilot date, not a friendly conversation.

Value share: 0% take-rate (liquidity doesn't exist yet). Your return is retention/parity on the ~11 accounts, not revenue capture — the $5,000/year is the vendor's money, not yours.

## Flywheel

- Loop: listed integration removes rate-shopping objection → the 45 overlap accounts retain/expand → proof point → second ISV follows.
- Subsidized side: the ISVs — free listing, engineering support for first build, real distribution (you route customers at them, not just list them).
- Founding cohort: the 2 vendors already in talks. Pick whichever commits a build-start date first.
- Minimum credible pool: 1–2 live integrations, not the 5-listing default from bigger playbooks — your addressable pool (45 accounts) is too small to need more.
- You're pushing this wheel for at least 2 quarters, not riding it.

## Obligations

- Surface stability: 90 days' notice on breaking API changes. Owner: unnamed — assign an eng lead.
- Roadmap boundary: state now whether Parcelwise will ever build native rate-cost-aware routing. If unclear, that's G4 unresolved — resolve before publishing anything.
- Escalation: when the vendor's rate feed is wrong, customer calls you first. Owner: support lead.
- Review: even rung 3 needs a lightweight data-access review (shipment data flowing to a third party). Owner: unnamed — flag as gap, resolve before pilot.
- Wind-down: written notice period + data-export plan before you sign the first partner, not after.

## Measurement

Baseline today: 0 partner integrations, 0% accounts with active complement, 4 known DIY scripts.

Targets — none dated yet by you. Suggested, pending your sign-off:
- 1 live integration in 2 quarters.
- 20% of the 45-account overlap pool active within a year of launch (~9 accounts).
- Time from vendor signup to live integration under 8 weeks (accounts for their 12-person-week build).

## Kill criteria

- Stop if the pilot ISV hasn't shipped a working build within 6 months of signed commitment.
- De-escalate to rung 2 (build it yourself) if attach stays under 10% of the 45-account pool a year after launch.
- Re-open rung 5 only if: standing security-review capacity exists, AND the demand list grows past 1 complement, AND accounts scale well past 260.

---

**Next: pick one.**
1. Confirm — does Parcelwise have a real API/webhook today, or only the CSV export? (resolves G2, gates everything)
2. Name the 9,000-customer platform the vendors already ship on. (resolves G6 envelopment risk)
3. Ask product lead: does routing roadmap ever touch carrier-cost logic? (resolves G4)

Answer #1 first — it decides whether rung 3 starts next quarter or needs an API build first.