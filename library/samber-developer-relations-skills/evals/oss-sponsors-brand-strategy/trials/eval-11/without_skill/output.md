No filesystem write access here, so I'll deliver the dashboard directly.

---

# Open Source Investment Program — QBR Dashboard (FY2026)

**Before the numbers: the four metrics you asked for don't match the mandate you stated.** Supply chain is the primary mandate, but pipeline (last-click), impressions (stars), total dollars, and share-of-voice are all sponsorship/brand metrics — none of them measure supply chain risk reduction. I've built the dashboard with supply chain leading, per the mandate, and kept your four requested metrics as a secondary section, corrected where the methodology would mislead the board. Nothing below is a fabricated number — cells that need a real data pull are marked `pending`, not filled with a plausible-looking placeholder.

## 1. Program Investment (input metric — not an outcome)

| Metric | Value | Note |
|---|---|---|
| **Total dollars given, FY26** | **$240,000** | Confirmed, grants ledger. This is spend, not impact — keep it visible but don't let it stand in for "did it work." |
| Cost per critical dependency covered | pending | `$240,000 ÷ # Tier-1 SBOM deps funded` — reframes the headline as unit economics instead of a bare total |
| Projects / maintainers funded | pending | Count of unique grant recipients |

## 2. Supply Chain Risk Reduction — PRIMARY MANDATE

Not part of your original ask — added because none of the four requested metrics cover it, and it's the thing this program is supposedly for.

| Metric | Formula | Source |
|---|---|---|
| Critical dependency coverage | funded Tier-1 SBOM deps ÷ total Tier-1 SBOM deps | Internal SBOM/dependency scanner + grants ledger |
| Maintainer bus-factor uplift | # funded projects moving bus-factor 1 → 2+ | OpenSSF Scorecard "Contributors" check, pre/post grant |
| Median vulnerability patch time | funded vs. unfunded deps, disclosure→patch days | OSV / GitHub Security Advisories |
| Avg. OpenSSF Scorecard score | mean across funded projects, QoQ trend | OpenSSF Scorecard API |
| SBOM audit coverage | % of production dependency tree with a generated SBOM | Internal SBOM tooling |

Confirm these are the right five with Security/Eng, or swap in whatever they already track — the point is that *something* representing the primary mandate leads the dashboard, not that these exact five are sacred.

## 3. Sponsorship-Influenced Pipeline — as requested, plus the correction

| | Last-click (requested) | Influenced, 180-day lookback (corrected) |
|---|---|---|
| Pipeline $ | pending | pending |

**Flag — last-click will structurally understate this, not just slightly misstate it.** Sponsorship is a top-of-funnel brand touch in a long B2B cycle; nobody clicks a README badge and closes in the same session. Last-click hands 100% of the credit to whatever happened right before the opportunity was created — usually a sales call or a branded-search visit — so a sponsorship program that's genuinely working can report near-$0 last-click pipeline. That's not evidence it failed; it's evidence the model can't see it. Report both numbers side by side, always — the gap between them *is* the brand-influence signal.

To compute either number, RevOps needs to define a "sponsorship touch" (referral click, docs/README backlink hit, or a self-reported field) and a lookback window. **Recommend adding a self-reported "how did you hear about us" field at demo/signup** — this is the one channel that reliably catches sponsorship-driven, dark-social influence that no click-tracking will ever see.

## 4. Developer Brand & Visibility — SECONDARY MANDATE

| Metric | Status | Note |
|---|---|---|
| Combined GitHub stars, funded projects | pending | Relabeled — see flag below. Not reported as "impressions." |
| Share of voice | **blocked** | No competitive set or data source defined — see flag below |

**Flag — stars are not impressions.** Stars are an all-time cumulative count with no time window; they can't substitute for a period metric like impressions. Summing them across your funded projects also double-counts — the same developers who star one project in an ecosystem tend to star the others, so the total overstates unique reach rather than measuring it. If the board needs an actual reach number, here are real, period-bound substitutes:
- **GitHub repo traffic** (unique visitors/views, 14-day windows) via the Insights API — needs the funded maintainers to share it
- **Referral traffic** from funded projects' README/docs links to your own site — Ahrefs or GA4, fully first-party
- **Earned-media impressions** tied to sponsorship announcements — a mention-monitoring tool (Ahrefs mentions, Brandwatch, Meltwater)

**Flag — share of voice needs two decisions from you before it's computable, not a data pull.** It requires (1) a named competitive set — which peer companies' OSS sponsorship programs are we benchmarked against? — and (2) a mention/backlink data source covering that set. Proposed proxy once both are named: `our sponsorship mentions ÷ (our mentions + named competitors' mentions)` across docs backlinks and social, trailing 90 days.

## 5. What's needed to make this real for the QBR

| Data connection | Feeds | Owner |
|---|---|---|
| SBOM / dependency scanner export | Critical dependency coverage, SBOM audit coverage | Security/Eng |
| OpenSSF Scorecard pulls | Bus-factor uplift, scorecard trend | DevRel / program owner |
| OSV / GHSA advisory timestamps | Vulnerability patch time | Security |
| CRM export + defined sponsorship-touch field + lookback window | Last-click & influenced pipeline | RevOps |
| Self-reported "how did you hear about us" field | Influenced pipeline, dark-social capture | RevOps / Sales |
| GitHub API pull (stars, optionally traffic) | Combined stars, real reach alternative | DevRel |
| Named competitor set + mention/backlink tool (Ahrefs or equivalent) | Share of voice | CMO names the set; Marketing runs the pull |

---

**Bottom line for the CMO conversation:** the dashboard is structured and every metric is formula-defined — what's missing is data access (five connections above) and two judgment calls only she can make (the competitive set for share of voice, and sign-off on reporting last-click pipeline next to influenced pipeline rather than alone). I'd rather hand her a dashboard with honest `pending` cells than one with numbers that won't survive a follow-up question in the room.