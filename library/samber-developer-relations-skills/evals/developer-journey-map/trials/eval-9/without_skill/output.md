# Vaneworth Customer Journey Map — v2 (AAARRRP)
**Refresh date:** 2026-09-19 · **Replaces:** v1 "API arc" (5-stage) map · **Segments:** Indie & Small Teams + Enterprise Platform Teams (merged, one map)

## What changed and why

1. **Numbers updated** for three stages (Onboarding, Integration, Production).
2. **Enterprise platform-team audience folded in** — one map instead of two, with segment-specific notes at each stage instead of a separate document.
3. **Framework switched** from the old 5-stage "API arc" (Awareness → Onboarding → Integration → Production → Advocacy) to **AAARRRP**, matching marketing's company-wide AARRR (pirate metrics) standard.

**Design call on the letters** (flag this if marketing disagrees): AAARRRP = **A**wareness, **A**cquisition, **A**ctivation, **R**etention, **R**evenue, **R**eferral, **P**latform. The first six are standard AARRR with "Awareness" prepended, which is the common extension when a top-of-funnel stage sits before paid acquisition. The trailing **P = Platform** is my addition, not a marketing-standardized term — I picked it because it's the natural home for the enterprise-only "roll out to more teams" behavior this refresh needed to capture. Push back if marketing already has a different P in mind.

## Old → new stage mapping

The old model had 5 stages; the new one has 7. Rather than just renaming, each old stage's number was re-homed onto the new stage it actually measures:

| Old stage (v1) | New stage (v2) | Old % | New % | Δ | Note |
|---|---|---|---|---|---|
| Awareness | Awareness | — | — | — | Not updated this cycle |
| Onboarding | **Activation** | 34% | **39%** | +5 pts | First green build — this is the real activation moment |
| Integration | **Retention** | 52% | **49%** | **−3 pts** | ⚠️ Only regression this cycle — see flag below |
| Production | **Revenue** | 28% | **31%** | +3 pts | Production reliance = crossing into paid/production tier |
| Advocacy | Referral | — | — | — | Not updated this cycle |
| *(none)* | **Acquisition** (new) | — | *no baseline* | — | Old model lumped signup into "Onboarding"; now split out |
| *(none)* | **Platform** (new) | — | *no baseline* | — | New terminal stage, enterprise-only for now |

## Stage-by-stage map

### 1 · Awareness
Prospect learns Vaneworth exists as a CI runner option.
- **Indie/small team:** discovery via GitHub, Hacker News, dev-community comparison posts vs. GitHub Actions/CircleCI.
- **Enterprise platform team:** discovery via peer referral, analyst/vendor shortlists, procurement-driven RFPs.
- **Exit events:** bounce off pricing page, unclear docs, no visible self-serve trial.
- **Signal:** not updated this cycle — carried from v1.

### 2 · Acquisition *(new stage)*
Prospect creates an account or starts a trial.
- **Indie/small team:** self-serve signup, connect GitHub/GitLab, no card required.
- **Enterprise platform team:** security review + procurement kickoff often precede account creation; multiple stakeholders (platform lead, security, finance) involved before anyone logs in.
- **Exit events:** signup friction, no SSO for enterprise, security questionnaire stalls procurement.
- **Signal:** no historical baseline — this stage didn't exist as a separate measurement point in v1. Needs an event added before it can be tracked quarter-over-quarter.

### 3 · Activation
User runs their first successful pipeline/job on Vaneworth.
- **Indie/small team:** single-repo first green build.
- **Enterprise platform team:** pilot team's first green build, typically gated behind a platform-team sandbox approval.
- **Exit events:** config-migration friction from prior CI vendor, missing runner image/language.
- **Signal: 34% → 39%** (+5 pts). Improvement — worth understanding what drove it before assuming it holds.

### 4 · Retention
User keeps coming back and embeds Vaneworth deeper into their workflow (multi-repo, multi-pipeline).
- **Indie/small team:** adds Vaneworth to a 2nd/3rd repo.
- **Enterprise platform team:** pilot team requests approval to expand beyond the initial repo — still single-team at this point.
- **Exit events:** pricing-tier surprise, missing feature parity vs. incumbent, flaky runner performance.
- **Signal: 52% → 49%** (**−3 pts**). ⚠️ **The only stage that got worse this cycle, and by a meaningful margin while every other measured stage improved.** Recommend a root-cause dig (support tickets, exit surveys, runner reliability logs from that window) before the next refresh — don't roll this forward unexplained.

### 5 · Revenue
Usage crosses into paid/production-tier reliance.
- **Indie/small team:** hits free-tier minute cap, upgrades to a paid plan.
- **Enterprise platform team:** signs an annual or seat-based enterprise agreement.
- **Exit events:** budget approval stalls, competitor undercuts price at renewal.
- **Signal: 28% → 31%** (+3 pts). Improvement.

### 6 · Referral
User actively promotes Vaneworth, externally or internally.
- **Indie/small team:** public praise, comparison blog posts, community Q&A answers.
- **Enterprise platform team:** internal champion evangelizes to other teams in the same company — this is the direct bridge into Platform below.
- **Exit events:** no referral program exists yet for either segment.
- **Signal:** not updated this cycle — carried from v1.

### 7 · Platform *(new stage)*
Vaneworth becomes the standardized CI runner across multiple teams within one enterprise account.
- **Applies to:** Enterprise Platform Teams only. Marked **N/A** for Indie & Small Teams — a single team has no further "platform" to expand into, so this stage simply doesn't apply to that segment.
- **Exit events:** budget re-approval needed per additional team onboarded, competing internal tooling standard, lack of multi-tenant admin controls.
- **Signal:** no baseline exists yet. This is precisely the gap the map merge was meant to close — in the old two-map setup, enterprise expansion past the first team had nowhere to be tracked at all.

## Open items for the next re-read

- **Investigate the Retention drop (52%→49%)** before the next quarter — it's the one number moving the wrong direction.
- **Instrument Acquisition and Platform** — both are new stages with zero historical data; nothing to compare against yet.
- **Enterprise segment is qualitative only.** Every enterprise-specific behavior above (procurement-gated Acquisition, pilot-gated Activation, Platform rollout) is a reasoned judgment call, not measured data. Recommend instrumenting the current enterprise pilot cohort so the next version can carry real enterprise numbers instead of narrative.
- **Awareness and Referral weren't touched this cycle** — confirm whether that's a genuine data gap or those numbers are just flat and unreported.

**Suggested next re-read: ~2026-12-18** (90-day cadence, consistent with prior journey-map check-ins).