## Kestrelbase: self-serve → inside sales → field sales thresholds

**The question as asked doesn't have a lookup-table answer.** No defensible published band separates self-serve from inside sales from field sales — that's folklore, not data. What decides it is unit economics: whether a rep's fully-loaded cost pays back fast enough against the deals they'd touch. Below is that model, with every number tagged by source.

### The mechanism

For each motion: `required ACV ≈ CAC per deal ÷ (gross margin × payback-fraction-of-year)`

Using David Skok's SaaS-wide reference points [sourced, SaaS-general, not devtool-specific] — LTV:CAC > 3 (best-in-class 7-8x) and CAC payback in 5-7 months — and standard ~80% software gross margin [assumption]:

**Inside sales rep**
- Fully-loaded inside AE cost: ~$140k/yr [assumption — general SaaS comp market range, not refreshed via web search this session]
- Realistic ramped capacity: ~25 closed deals/yr [assumption]
- CAC per deal: $140k ÷ 25 ≈ **$5,600**
- Required ACV for 6-month payback: $5,600 ÷ (0.8 × 0.5) ≈ **$14,000**
- LTV:CAC check: year-1 alone gives ~2x (below Skok's 3x floor) — the economics only clear 3x once you count ~2-3 years of retained seats. **This motion depends on retention, not just the initial deal.**

**Field sales team**
- Fully-loaded field AE + shared SE + travel: ~$300k/yr [assumption]
- Realistic capacity: ~8 closed deals/yr (SOC 2-driven security review lengthens the cycle) [assumption]
- CAC per deal: $300k ÷ 8 = **$37,500**
- Required ACV for 6-month payback: $37,500 ÷ (0.8 × 0.5) ≈ **$94,000**

### Thresholds

| ACV (annual) | Seats @ $39/seat/mo | Motion |
|---|---|---|
| < ~$8k–$10k | < ~20 seats | Self-serve only |
| ~$10k – ~$90k | ~20–190 seats | Inside sales rep |
| > ~$90k–$100k | > ~190 seats | Field sales team |

ℹ️ These dollar figures are a *derived output* of the formula above, built on labeled assumptions (rep cost, capacity, margin) — not an industry benchmark. Swap in your own CAC and close-rate data the moment you have a closed cohort and the number moves; don't treat $90k as gospel.

### The threshold that matters more than ACV

⚠️ Your paid boundary (multi-tenant RBAC, retention policies, **SOC 2 compliance reporting**) is an enterprise-shaped gate sitting behind a pure self-serve motion. SOC 2 reporting specifically is what a security/procurement buyer asks for — the moment that request appears, you have a field-motion deal regardless of seat count. Route on **whichever fires first**: ACV crossing the line above, or an inbound SOC 2/security-questionnaire request. The second signal is more reliable because it's observable before the invoice size is (paid-boundary test #3: someone has to be able to see the crossing).

### Leading indicator to instrument now

Track the rate at which self-serve accounts hit a paid-boundary trigger — a second team provisioning, a SOC 2 report request, an audit ask — segmented by current seat count. That rate moves before revenue does and tells you when to staff, rather than finding out from a stalled Stripe checkout.