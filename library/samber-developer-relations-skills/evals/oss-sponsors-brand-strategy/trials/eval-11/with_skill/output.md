# Open-source sponsorship dashboard — $240k program, QBR-ready

## First: four requests I'm not building as specified, and what replaces each

A dashboard built from these four metrics will not survive its first audit — this note goes at the top of the deliverable, not buried in an appendix, because the CMO deserves the reasoning before the replacement.

**1. Pipeline sourced from sponsorship, last-click model — refused.**
Nobody clicks a README logo and buys. A last-click model built on this channel collapses the moment finance or a data team traces one deal back to a specific commit. There is no click to attribute — sponsorship buys presence and relationship, not a tracked funnel step. Replaced with placement verification and referral traffic from placement URLs where a URL exists (below), which is the honest, defensible version of "did this generate anything measurable."

**2. Impressions estimated from combined GitHub stars — refused.**
Stars are a lifetime cumulative count with no time dimension, no reach denominator, and no relationship to who actually saw a sponsor logo. Summing them across funded projects doesn't produce an impression number; it produces a number shaped like one. Replaced with placements live and verified, and unaided mentions of the program in developer communities — both real, both countable, neither inflatable by a popular project you fund for $10/month.

**3. Total dollars given as the headline metric — refused.**
Total dollars is spend, not outcome. It answers "how much did we commit" — which belongs in the transparency report, disclosed alongside developer headcount and per-recipient amounts — not "did the $240k do what supply-chain assurance is supposed to do." The headline metric has to be a coverage or health number that moves when the program works and stays flat when it doesn't; total dollars given moves every time finance cuts a check regardless of effect.

**4. Share-of-voice score — refused.**
Share-of-voice needs a defined competitor set and a comprehensive mention-tracking source to mean anything, and neither exists for an open-source funding program — there's no agreed universe of "voice" to take a share of, so the number is unfalsifiable in either direction. It's the same failure mode as star-derived impressions: a real-sounding number with no denominator anyone could audit. The metric actually doing the job share-of-voice is reaching for — is the company's name coming up unprompted when developers talk — is unaided mentions in developer surveys and community threads, already in the table below.

---

## Dashboard, organized by mandate — supply chain primary, reach secondary

Populate **Baseline** from the company's own measurement *before* the next payment goes out — it's the only number in this table with any authority, and it doesn't exist yet if it wasn't captured at program start. Every row carries a named owner; a metric with no owner doesn't get reviewed.

### Supply chain — primary mandate, breaks every tie

| Metric | Baseline (year 0) | Target (year 1) | Actual | Owner |
|---|---|---|---|---|
| Share of fundable direct dependencies covered | *capture before next payment* | **80%** (this skill's own default, not an industry standard — see note below) | — | *assign* |
| Dependencies with a dormant maintenance score | *capture before next payment* | trending down | — | *assign* |
| Median response time on issues the company filed upstream | *capture before next payment* | < 10 days | — | *assign* |

**On the 80% target:** this is a self-set starting point, not a benchmark to defend in the room as industry-standard. The only company that has published a higher coverage figure reported "95% or greater," and described itself as the first company to approach 100% — but that number came out of a dedicated program with a platform integration behind it. Present anything above 80% as ambitious, not as the bar everyone else clears.

### Reach — secondary mandate

| Metric | Baseline (year 0) | Target (year 1) | Actual | Owner |
|---|---|---|---|---|
| Placements live and verified | *capture before next payment* | 100% of paid-for placements | — | *assign* |
| Referral sessions from placement URLs | *capture before next payment* | any measurable, trending up | — | *assign* |
| Unaided mentions of the program in developer surveys / community threads | *capture before next payment* | > 5 per period | — | *assign* |

### Policy — both mandates

| Metric | Baseline | Target | Actual | Owner |
|---|---|---|---|---|
| Policy breaches raised by a sponsee | — | 0 | — | *assign* |
| Depth sponsees with ≥1 documented interaction beyond the payment | *capture before next payment* | 100% | — | *assign* |

---

## Pass threshold (self-set, not an industry norm — say so in the room)

Checked at **12 months**, then annually:

- Every placement paid for is live and verified.
- At least 80% of fundable direct dependencies covered (supply chain is primary here, so this is the line the program is actually judged on).
- Every depth sponsee has at least one documented interaction beyond the payment.
- No policy breach raised by a sponsee.
- A renewal decision made for **every** target before budget close — no target carries over into next year by default.

## Annual report — the disclosure the QBR can show alongside the dashboard

This is where total dollars given belongs: as transparency, not as proof of return. Publish it, but don't present it as the metric that tells the CMO the program worked.

```
# Where our open-source money went in <year>

Total: $240,000 across N destinations.
Breadth: $A across M dependencies (median $B each).
Depth: table of project, amount, why it matters to us.
What we got wrong this year: one honest paragraph.
Next year: budget direction and how to reach us.
```

Minimum disclosure inside it: the year, the number of full-time-equivalent developers on staff, the total paid, the amount per recipient. That's the format the industry pledge uses for its own annual disclosure — it's short enough that skipping it isn't a resourcing problem, it's a choice.

---

**What this dashboard needs from your side before it has real numbers in it:** a baseline pull (dependency coverage %, dormant-dependency count, upstream issue response time, current placement inventory) captured now, before the next sponsorship payment — not retrofitted later. Without that baseline, year-1 "actuals" have nothing honest to compare against.