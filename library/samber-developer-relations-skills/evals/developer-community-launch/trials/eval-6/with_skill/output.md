# Vireo Labs Slack — diagnostic plan and relaunch case

This runs on `developer-community-health` (samber/developer-relations-skills), diagnosis mode — not `developer-community-launch`. The community already exists; the job is to measure it honestly before anyone decides to reseed it, fold it back, or relaunch it from zero. If diagnosis shows the demand was never real, that's the moment to re-run the launch gates properly — not before.

**First action, today, before anything else:** check your Slack plan and message-retention/export settings. Free and lower paid tiers cap searchable history (commonly 90 days); if you're on one of those, your first-six-months data — the exact window you need to prove "lively, then dead" — may already be aging out of what's exportable. Pull a full-history export now, or confirm your plan retains it, before you build any of the below on data you can no longer get. This is a 15-minute task and it's the one thing that's actually time-sensitive.

## Two things unconfirmed — settle these before the metric sheet is final

1. **Primary outcome (pick exactly one).** Nobody said why this Slack exists. Default proposal: **support deflection** — users answer each other's product questions instead of all of it landing on your team. That's the most common and most measurable reason a "platform users" Slack gets built, and it's the easiest to defend to leadership because it maps straight to a cost. If the real reason was closer to retention/expansion or product feedback, say so — it changes which metrics matter. Confirm this with whoever owns the P&L before the first review.
2. **B2B or individual adoption.** If members belong to paying customer accounts (likely, given "platform users"), the unit that matters is *accounts represented*, not head count. A 1,100-person Slack could be 40 accounts with one loud champion each, or 400 accounts with real coverage — very different stories. If it's closer to open individual sign-up, ignore the account layer below.

Everything past this point assumes support deflection, B2B. Swap if wrong — the mechanics don't change, only the units.

## Why "seasonal" is the weaker hypothesis, and how to actually test it

You have 14 months of history — one cycle. You cannot prove seasonality with one cycle; that needs at least two passes over the same calendar months to show it recurring. What you *can* check with one cycle:

- **Shape of the decline.** Seasonal dips recover — a slow month, then back to baseline. What you're describing (strong for ~6 months, then flat-near-dead for ~8) is a decay to a floor, not a dip. That shape is the signature of a **launch burst decaying once the initial push stopped** — a named, common failure mode, not weather.
- **Whether the cause moved with it.** Pull the month staff seeding/posting dropped off, and the month organic activity dropped off, and lay them side by side. If they move together, that's your answer, and it's fixable — it's a staffing gap, not a demand gap.
- **Whether the funnel into Slack ever stopped.** Check if new customers are still being invited/onboarded into the Slack at all. A room that stopped getting new joiners around month 6 looks identical to "nobody wants this anymore" but has a completely different fix.

Treat "genuinely dying" and "seasonal" as two of at least four live hypotheses, not the only two: (a) launch burst decayed, never replaced with a habit, (b) the room never had real organic demand — the first six months were staff doing the talking, (c) the audience found a faster answer elsewhere (support tickets, docs) and quietly left, (d) true seasonal dip. The metric sheet below is built to tell these apart, not just to produce a "healthy/unhealthy" score.

## Metric sheet

Seven metrics, four pillars, all within the 8-metric ceiling. Baselines marked "baselining" until you pull the export — with 14 months of history you likely have enough periods (6+) to set a deviation-band threshold immediately instead of waiting three more months.

| Metric | Pillar | Formula | Source | Baseline | Threshold (origin) | Action if breached |
|---|---|---|---|---|---|---|
| Median time to first human response | Responsiveness | thread opened → first non-bot reply, elapsed time | Slack export, bot accounts excluded | baselining — pull last 6 months minimum | >24h sustained (folklore, unsourced — replace with trailing median after pull) | Recruit answerers to cover the gap window |
| Zero-reply rate | Responsiveness | % question threads with no human reply within 7 days | Slack export | baselining | >25% (folklore, unsourced) | Weekly sweep of unanswered threads |
| Active posters per month | Activity | distinct non-bot identities who posted, by month | Slack export (not Slack's own "active members" figure — that counts reads, re-derive from raw messages) | baselining — this is the core trend line, pull all 14 months if retention allows | deviation band once 6 periods plotted (self-set) | Diagnose before reacting — check for burst/staff-seeding confound first |
| Staff/non-staff share of messages | Activity | staff messages ÷ total messages, by month | Slack export + staff account flag | baselining | non-staff <35% sustained (self-set) | If it was always staff-heavy, demand was never proven — escalate as a launch-gate question, not a reseed question |
| First-time posters per month, plus raw join count | Funnel | count of identities with no prior post; separately, count of new Slack joins | Slack invite log / export | baselining | new joins ≈0 for 2+ months (self-set) | Check whether onboarding still invites new customers at all |
| Lapsed-member signal | Sentiment | one-question DM to members active in months 1–6, silent 60+ days: "you stopped posting — what changed?" | direct outreach, this week | none — first read | n/a, qualitative | Route answers into the decision below |
| Recommendability (quarterly, once stable) | Sentiment | "How likely to recommend this community?", NPS-style | quarterly pulse survey | not yet run | n/a — first wave sets it | Add once the room is live again |

Bot exclusion and staff-account flagging apply to every row above — skip this and the responsiveness numbers lie.

## Decision, written down before you look at the data

Commit to this now, so nobody re-argues the call after seeing a number they don't like.

| If the read shows... | Verdict | Move |
|---|---|---|
| Decline tracks staff seeding stopping; funnel still feeds new members; lapsed members say "just went quiet, no complaint" | Structural, fixable | **Reseed in place**: new founding cohort recruited by hand, published response-time commitment, one weekly ritual, 90-day re-measure against this sheet |
| Staff share was always high; non-staff activity barely existed even in the "lively" months | Demand was never proven | **Re-run the launch gates properly** (developer-community-launch) before reopening anything |
| Lapsed members say they get answers faster elsewhere (support tickets, docs) | Venue vacuum, not death | **Merge/redirect**: point effort at the venue that's already serving the need |
| Nothing above lands cleanly and the funnel is dry with no case for support demand | No case | **Archive to read-only** — keeps the answers searchable, drops the standing cost, is the version of "failed experiment" you can say plainly instead of quietly maintaining a ghost room |

## The case for leadership

Don't answer "healthy or dead" with an adjective. Bring: the monthly trend line with the staff-seeding drop-off marked on it, the staff/non-staff split for months 1–6 versus now, and the lapsed-member answers. If the shape says "we stopped feeding it," that reframes "failed experiment" as "under-resourced after month six" — a different, more defensible conversation, and one only the data can make for you.

Also worth surfacing directly, not softened: if nobody had protected weekly hours to run this after the launch quarter, that's a staffing decision, not a community failure — name it as that rather than absorbing it as a diagnosis problem.

## Timeline

- **This week (~3–4 hours total):** confirm Slack plan/export access, pull the raw export, build the metric sheet, send the lapsed-member DMs.
- **Week 2:** first read against baseline, pick the verdict from the table above.
- **Next review: 2026-10-18** — re-check the trend line with a full month of fresh data, and whether lapsed-member replies changed the read.

**Next concrete action:** open Slack admin settings → check your plan tier and message retention window. Do this before anything else in this plan.