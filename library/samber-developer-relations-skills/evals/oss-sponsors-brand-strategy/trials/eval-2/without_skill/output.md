# Nord Ledger 2027 Open Source Investment — Sanity Check & Portfolio

## Verdict on the weighting

40/30/20/10 is defensible for a payments company, but it needs three fixes before it goes in front of the board.

**What's right:** Weighting supply-chain risk reduction highest (40%) fits a regulated payments business — PCI DSS 4.0, DORA, and post-xz/Log4Shell board scrutiny all point the same direction. No board member will push back on that being #1.

**What's shaky:**

- **The 10% pledge line isn't a "weight" — it's a fixed liability.** If you signed a public funding pledge last year, that dollar amount is almost certainly contractually or reputationally fixed (e.g., a flat commitment or % of revenue), not something the exec team chose to weight at 10%. Present it to the board as a **floor, carved out first**, not as one of four coequal discretionary buckets. If $31k (10% of $310k) doesn't match what you actually pledged, the whole framework is wrong — check the pledge terms before this goes to the board.
- **"Developer brand" and "engineer engagement" will visibly overlap in execution.** A staff engineer speaking at a conference about your OSS contributions is simultaneously brand spend and engagement spend. Fine operationally, but if the board later asks "why did engagement money pay for a conference sponsorship," you want a rule ready: *brand = external-facing spend (sponsorships, content, swag); engagement = internal-facing spend (time, recognition, training)*, even when the same event funds both.
- **No line for measurement.** A board sanity-checking a security-risk-reduction spend will ask "how do you know it worked." Right now there's no metrics budget or reporting cadence in the 40%. Carve a small slice out for instrumentation (SBOM tooling, dependency-risk scoring) rather than assuming it's free.

**Net:** keep 40/30/20/10 as the *narrative* the board sees, but internally treat the pledge as pre-committed, and make sure "supply-chain risk reduction" has an explicit measurement line, not just spend.

---

## The Portfolio — $310,000, FY2027

### 1. Supply-chain risk reduction — 40% = $124,000

| Line item | $ | Rationale |
|---|---:|---|
| Direct funding to critical upstream dependencies (via Tidelift, Open Collective, or direct sponsorship — target the 5–10 packages your SBOM shows as both critical-path and single-maintainer/underfunded) | $55,000 | This is the highest-leverage line: payments infra typically has 2–4 crypto/parsing/serialization libraries maintained by one or two unpaid people. Fund those specifically, not OSS broadly. |
| OpenSSF membership + Alpha-Omega or equivalent pooled fund | $25,000 | Buys you a security-industry-recognized signature for the board deck ("we fund OpenSSF") and spreads risk across the ecosystem, not just your own dependency list. |
| SBOM/dependency-risk tooling (Sigstore adoption, OSV-Scanner integration, or a paid support contract on whatever scanner you already run) | $20,000 | This is your measurement line — without it you can't tell the board next year whether the $124k reduced risk or just went to good causes. |
| Rapid-response fund for emergent incidents (CVE bounty top-ups, expedited patch funding when a dependency you rely on gets a critical disclosure) | $15,000 | Kept liquid, released ad hoc — supply-chain incidents don't wait for next year's budget cycle. |
| Paid critical-dependency audit (fractional security researcher time to formally rank your top 20 dependencies by blast radius) | $9,000 | Do this **first**, ideally Q1 — it should inform where the $55k above actually goes. |

### 2. Developer brand — 30% = $93,000

| Line item | $ | Rationale |
|---|---:|---|
| Conference sponsorships/CFP travel at 2–3 targeted events (fintech/payments-adjacent + one broad dev conference) | $38,000 | Pick events your engineering candidates and partner-integration developers actually attend — not general "dev brand" spray. |
| Maintenance budget for any public Nord Ledger SDKs/libraries (if you ship public client libraries, this funds the engineer-hours to keep them non-embarrassing) | $28,000 | Brand damage from an unmaintained public repo is disproportionate to its size — this is defensive brand spend, not growth spend. |
| Technical content (blog posts on your OSS contributions, case studies, one dev advocate's content time if you have that role) | $17,000 | |
| Meetup/community sponsorship, swag | $10,000 | |

### 3. Engineer engagement — 20% = $62,000

| Line item | $ | Rationale |
|---|---:|---|
| Structured OSS contribution time (e.g., quarterly "OSS days," stipend or recognition tied to upstream PRs merged) | $27,000 | Needs a real program, not "20% time" left informal — informal versions get eaten by roadmap pressure within two quarters. |
| Internal hackathon focused on OSS/dependency contributions | $15,000 | |
| Conference **attendance** budget for engineers (not speaking — just learning) | $12,000 | |
| Micro-grant pool: small stipends for engineers who contribute fixes to dependencies your own stack uses | $8,000 | Doubles as supply-chain risk reduction in practice — tag it here for the "engagement" narrative, but track it as a two-birds line internally. |

### 4. Public funding pledge — 10% = $31,000

- Treat as a **pre-committed floor**, paid first, not subject to the sanity check above.
- Confirm the actual pledged amount against the signed agreement before publishing $31,000 — if the real number differs, the other three buckets need to be rebalanced against the *remaining* budget, not against $310k gross.

---

## Guardrails for the board deck

- **Lead with the pledge as a fixed obligation**, then present 40/30/20/10 as the split of the *discretionary* remainder — this preempts the "why is a legal commitment only 10%" question.
- **Report supply-chain spend against a named dependency list**, not "open source" in the abstract. Boards fund things they can picture; "we fund curl and our JSON parser's maintainer" lands better than "we fund the ecosystem."
- **Set a Q1 checkpoint**: the critical-dependency audit ($9k above) should land before most of the $55k direct-funding line is committed, so you're not funding based on guesswork.
- **Don't double-report** the micro-grant pool ($8k) in both engagement and risk-reduction totals when you present final numbers — pick one bucket for board accounting even if it serves both purposes.

## What I assumed / what you should check

- I don't know your actual signed pledge amount or terms — verify $31k is correct before it's on a board slide.
- I don't know your dependency stack, so the "$55k to 5–10 critical packages" line is a placeholder shape, not specific vendors — the Q1 audit should name them.
- I assumed no existing dedicated security budget already covers SBOM/scanning tooling; if it does, reallocate that $20k line into more direct maintainer funding.