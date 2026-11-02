Using the developer-champions skill to design this end to end.

---

# Harbourline Champions — program design

## Assumptions flagged for confirmation

You asked for the finished deliverable rather than a live interview, so the design below fills the gaps the skill normally interviews for with labeled, explicit assumptions. Confirm or correct these before you lock anything publicly — they drive every downstream decision:

- ⚠️ **Primary outcome** (skill Q3, must be one, not five): assumed **community support capacity + retention of top contributors** — converting people already answering questions in your forum into a recognized layer, with product feedback as a secondary benefit riding on the access perk. If leadership's real goal is product feedback first, the criteria weighting in Step 5 flips.
- ⚠️ **Access commitment**: assumed at least one PM or engineer will show up to a quarterly briefing and a private channel. Unconfirmed. This is the single most load-bearing assumption — a champions program whose only offer is swag has no engine.
- ⚠️ **Feedback listener**: assumed someone on the product side will actually receive and act on what champions raise. Unconfirmed — without this, the "feedback landed" scorecard row is unfillable by design.
- ⚠️ **Budget per member**: not stated. Assumed **$0 confirmed, funding-tier perks pending sign-off**.
- ⚠️ **Code of conduct / moderation path**: assumed it exists in some form given an active 1,400-person forum, but not confirmed as written and enforceable.
- ⚠️ **Audience mix**: assumed mostly engineers at customer companies plus some independent consultants (typical for a B2B data-pipeline product) — affects the employer-approval and conflict-of-interest questions in compliance.
- ⚠️ **Forum platform**: assumed it supports a badge/role/title natively (Discourse, Discord, Circle, etc. all do) — this is what keeps "zero engineering headcount" true even for the status perk.

## Readiness gate check (Step 1)

| Gate | Verdict | Note |
|---|---|---|
| Candidate pool | ✅ | 1,400 active/90d is far above the ~10-nameable floor. Real check: pull your top ~20-25 forum contributors by sustained activity (not just 90-day presence) before picking names. |
| Owner with recurring time | ⚠️ | Named (you), but 8 hrs/month total is below the skill's 1-2 hrs/champion/month reference for a high-touch design. This forces a **small, low-touch cohort**, not the reference default — sized below. |
| Something only you can give | ⚠️ unconfirmed | Needs a yes from product/eng this week — the whole program is hollow without at least one access beat. |
| Feedback capacity | ⚠️ unconfirmed | Same ask, different stakeholder: someone who reads and answers what champions raise. |
| Conduct baseline | ⚠️ unconfirmed | Confirm a written CoC + escalation path exists before granting anyone a title with implied authority. |

**Kill criteria, set now, before launch:** two consecutive quarters below 50% active share, or your available hours dropping below ~4/month with no backfill, means shrink the cohort or drop to a pure recognition-only tier — not let the roster go quiet with titles still active.

## Archetype decision (Step 2)

Two forces pull in opposite directions here, and the fix is sequencing, not picking one:

- A **locked 6-week date** promotes the invite-only circle or the award/recognition shape — the only two that can stand up from nothing that fast.
- A **"recurring forever" mandate** promotes the application cohort — published criteria and an annual window are what let a roster survive past its founder.
- **Zero engineering headcount deletes the points ledger outright.** Not ranked last — deleted. Elastic's own program outgrew spreadsheet/GitHub tracking and had to build a portal; you have no path to that at all.

**Recommendation: launch Year 1 as an award/recognition-style founding cohort, and write the Year 2 upgrade to a published application cohort directly into the charter.**

Why award over plain invite-only, specifically for you: a stage reveal is structurally a recognition moment — names read out, applause — which is what the award shape is built for. An invite-only circle's whole point is *no public roster*, which sits awkwardly against "announce it on stage." The two are functionally identical in effort and compliance cost (one small-group decision per cycle, nothing running between cycles), so there's no cost to picking the one that actually fits the ask.

This also resolves the tension honestly instead of picking a side: the 6-week clock governs what launches; the recurring mandate governs what the charter *promises*. Publishing the criteria now (even though this cohort is nominated, not applied-for) means the criteria are already field-tested when you open a real application window in Year 2.

---

## The charter

**Harbourline Champions — charter**

1. **Purpose** — Recognize and retain the forum's most active contributors, sustaining community-driven support capacity, with product feedback as a secondary benefit through the access perk. *(self-set — confirm with leadership; this is the assumption everything else cascades from.)*
2. **Room** — Engineers and data practitioners at customer companies running Harbourline in production, plus independent consultants active in the forum. 18+. No regional/language weighting yet — revisit once you've pulled the forum's geographic mix.
3. **Archetype** — Award/recognition for Year 1 (nomination-only, closed review, dated cohort). Moves to a published application cohort from Year 2, once the criteria below have been field-tested against a real cohort and you've measured your actual hours-per-champion cost from one full cycle.
4. **Size** — 8 founding champions *(self-set, calibrated to your 8 hrs/month ceiling — roughly 1 hr/champion/month, deliberately leaner than the skill's 1-2 hr high-touch reference)*. Pipeline: ~20 named candidates (2-3× cohort) pulled from forum activity data before you finalize the list.
5. **Criteria** — any two of: sustained, recognized answering of others' questions in the forum (12+ months); running or organizing a Harbourline user group or workshop; publishing non-paywalled content about running it in production; mentoring a newcomer to a first successful pipeline; filing reproducible feedback that shaped the roadmap. **Anti-signals**: reach without production depth, activity starting the week nominations open, condescension toward beginners, asking for the title as compensation.
6. **Obligations** — follow the code of conduct; be constructive with newcomers; give honest feedback including public criticism; respect embargoes on anything shared pre-release. **May not**: speak for Harbourline, promise roadmap items, act as unpaid frontline support, handle customer escalations. No content quotas, ever — a quota converts recognition into unpaid work, which is a community problem and a legal one.
7. **Perks** — led with the highest-value, lowest-marginal-effort rungs given your constraints:
   - *Access*: one quarterly call combining a roadmap/pre-release briefing with the cohort catch-up (one beat serves all 8 — don't run these separately); a private channel with 1-2 named engineers.
   - *Platform*: a reserved champions spotlight at next year's conference; a feature on the Harbourline blog/community page.
   - *Skill-building*: light speaking/writing coaching ahead of their conference appearance — folds into prep you'd do for any speaker anyway.
   - *Funding*: pending leadership sign-off — comped conference ticket/travel for the founding cohort. **Not promised at launch until budget is confirmed.**
   - *Status*: a "Harbourline Champion" badge on their forum profile, named on stage, listed on a simple champions page.
8. **Term** — 12 months, running from this conference to next year's — the renewal window and the annual stage moment become the same beat by design. Renewal judged on the same criteria over the last term only, activity record sent 90 days ahead. Pause available for parental leave, illness, job change, or burnout — no reason required beyond the category.
9. **Exit** — no visible activity or contact for 6 months → ineligible for renewal, moved to alumni. Conduct removal decided by the moderation process, never by you alone. Alumni keep the dated title ("Harbourline Champion, 2026-2027"), stay on a low-frequency digest, and are invited to nominate and review the Year 2 cohort — this is also your cheapest source of extra review capacity for the harder Year 2 process.
10. **Compliance** — intake confirms employer and whether it competes with Harbourline, and whether the employer requires approval for the title; perk value is declinable without penalty for anyone under public-sector/finance/healthcare gift limits; 18+ required; comped travel/tickets flagged as possibly taxable to the recipient; supplied wording for any public post disclosing the relationship; NDA scoped only to material shared in the private pre-release channel, nothing blanket.
11. **Operations** — Owner: you, 8 hrs/month steady-state *(self-set, deliberately below the skill's high-touch reference given no dedicated headcount)*. Budget: **TBD, pending leadership**. Beats: one combined quarterly call (cohort + roadmap merged to save hours), a short quarterly written feedback digest ("here's what shipped from what you told us"), an annual nomination/renewal window 6-8 weeks before each conference, one formal recognition moment per year (the stage reveal) plus informal monthly shout-outs in the forum (minutes, not a production).
12. **Bar** — charter 12/12 answered before stage launch; quarterly active share ≥ 50% *(self-set, lowered from the skill's 60% default for a lean-touch design — recalibrate after two quarters)*; renewal acceptance ≥ 70%; median response to a champion ≤ 5 business days; ≥1 product decision traceable to champion input per quarter *(your highest-risk row — depends on the unconfirmed PM commitment above)*; pipeline ≥ 4 named-but-not-admitted candidates on file at all times. Kill criteria as stated in the gate check above.

---

## The public page (draft copy)

**Harbourline Champions**

*Purpose* — Harbourline Champions recognizes the people already making this community work: the ones answering questions, running workshops, writing about running Harbourline in production, and telling us what's broken before it becomes a ticket.

*Who qualifies* — Any two of: sustained, recognized help answering others' questions in the community; organizing a user group or workshop; publishing non-paywalled content about using Harbourline in production; mentoring a newcomer to their first successful pipeline; filing feedback that changed something we shipped. We don't count reach on its own, activity that starts the week nominations open, or condescension toward beginners.

*What we ask* — Follow the code of conduct. Be constructive with newcomers. Tell us the truth, including when it's critical. Respect embargoes on anything we share early. Champions don't speak for Harbourline, promise roadmap items, or handle customer support — this is recognition, not a job.

*What you get* — A quarterly roadmap briefing and a private channel with our engineers. A spotlight at our annual conference and on our blog. Speaking and writing coaching. A Champion badge and a place on this page. (Travel and ticket support: pending — we'll update this page once confirmed.)

*Term* — One year, renewed each year around our conference, judged on the same criteria you were nominated for. Life happens — pause your term any time for parental leave, illness, a job change, or burnout, no explanation required.

*If your term ends* — No hard feelings, no deletion. You keep the dated title, stay on our low-frequency alumni digest, and get first pick at nominating and reviewing next year's cohort.

*Disclosure* — If you post publicly about a perk or early access, say so — we'll give you the exact wording.

*How this works right now* — Year 1 is a small, nominated founding cohort — we're picking names, not opening applications. From Year 2, we'll open a real application window with these same published criteria.

---

## 6-week launch reality check

Your steady-state budget is 8 hrs/month. The launch sprint (naming ~20 candidates, confirming ~8, drafting this charter and page, lining up a PM/engineer, coordinating with your events team) does not fit inside 12 hours (8 × 1.5 months). Two honest options:

1. **Ask leadership for a one-time launch-sprint bump** — roughly 10-15 extra hours across the six weeks, framed explicitly as a one-time investment, with 8 hrs/month resuming after the conference. This is the cleaner ask precisely because you can point to the number instead of quietly overworking it.
2. **If that's refused, cut scope further**: cohort of 6 instead of 8, no individual onboarding calls (one group email instead), skip the public page's polish for a one-page version, and defer the pipeline list to the top 12 names you already know instead of a fresh 20-name pull.

I'd ask for option 1 before defaulting to option 2 — a founder-owner burning unplanned hours in month one is exactly the failure mode this design is trying to avoid (see the kill criteria above).

## What's still open

Before this can go on stage, get explicit yes/no answers on the five flagged assumptions at the top — access commitment, feedback listener, budget, code of conduct, and audience mix — plus a decision on the launch-sprint hours. Everything else in this charter is ready to run once those land.