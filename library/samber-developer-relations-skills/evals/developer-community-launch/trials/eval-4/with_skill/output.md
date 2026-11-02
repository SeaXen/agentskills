# Quillstack Community Launch — Recommendation and Brief

**Routing check:** this is a from-scratch launch decision (no forum exists yet), not a moderation, health, champions, or meetup question — the right skill, run in full.

## On the date, directly

**Don't lock 4 November as the public-open date. Lock it as the date the founding cohort and invited-beta work *starts*, and let the public opening land where the evidence puts it — which, if work starts this week, is plausibly right around 4 November, but that's an outcome to confirm in October, not a promise to make in September.**

Two of five readiness gates are strong beyond the bar (demand, owner); one is a clean pass as stated (purpose); one is accepted as stated but worth a sanity check (venue vacuum); one is weak with a fixable mitigation (seed supply — see below). That's a 4-pass verdict: **launch, on a delayed date, gated on the mitigation landing, not on the calendar.** The skill's own rule for this: *"the date is the cheapest thing to move."* Marketing can still get a 4 November moment — it just shouldn't be "forum is open to everyone," because right now your answering bench is two people, both in the same time zone, covering 40% of your install base.

---

## Approach considered

Three ways to resolve the date-vs-readiness tension:

1. **Slip past November.** Don't open anything until a non-CE answerer is confirmed. Cleanest coverage match to your install base, but forfeits the quarterly-push slot entirely and gives marketing nothing concrete on the 4th.
2. **Open fully on 4 November with Central-Europe-only coverage.** Meets the date, but the first impression for 60% of your users (NA/APAC) is a room that goes quiet outside CEST hours — the exact "one negative experience" failure mode the responsiveness evidence warns about, landing on your largest segment first.
3. **Decouple the announcement from the opening.** Founding cohort starts now (week of 22 Sept); invited beta runs Oct 6–Nov 2; 4 November becomes the earliest possible public-open date, gated on (a) at least one reliable answerer with NA or APAC-friendly hours confirmed, and (b) day-30-style leading indicators (member-authored answers, the ritual running twice) coming back green from the beta. If either isn't green by then, 4 November ships as "beta is open, general availability coming" instead of a full public launch.

**Recommend option 3.** It's the only one that gives marketing something real on the 4th without spending your one shot at a first impression on an under-covered room.

---

# Community Launch Brief — Quillstack

## 1. Verdict

Launch, gated on the seed-supply mitigation landing before the room goes fully public — target public-open date 4 November, contingent, not fixed.

Gates: demand **pass**, owner **pass**, purpose **pass**, venue vacuum **pass (as stated)**, seed supply **weak**.

Evidence:
- **Demand** — 40+ repeat setup questions last quarter, ~12 (≈30%) exact duplicates, users already answering each other unprompted in the repo. Comfortably clears the bar.
- **Owner** — Priya, 7h/week, manager-signed-off through next year and beyond. Stronger than the gate requires (it only asks for a sustained figure *after* the launch quarter; you have a standing multi-year commitment).
- **Purpose** — SPACES: Support — "cut duplicate setup tickets by half within two quarters." Single, named, measurable.
- **Venue vacuum** — taken as given ("no existing space covers us"). Worth one explicit check before fully banking this: feature-flagging has an emerging shared space (OpenFeature's CNCF community) — confirm nobody's already having this conversation there before you build a competing room next to it.
- **Seed supply** — 24 nameable invitees clears the 20+ headcount bar, but coverage fails on both axes the gate actually checks: only 2 of 24 are trusted to reliably answer (you and one other), and all 24 sit in Central Europe while 60% of installs are NA/APAC. Headcount was never the risk here — coverage is.

## 2. Audience and outcome

Primary audience: developers integrating the Quillstack SDK, asking setup/configuration questions.

B2B or B2C: **assumed B2B developer tool** (paid feature-flag SDK sold to companies, with individual engineers as implementers) — flag if this is wrong, since it changes the buyer/user split and the per-customer-channel handling below. Not stated in the brief; confirm.

Primary outcome (SPACES: **Support**): cut duplicate setup tickets by half within two quarters. Baseline: ~12 duplicates/quarter out of 40+ total setup questions. Target: ≤6 duplicates/quarter by the two-quarter mark. Track this number specifically — the 40+ total may not fall much (legitimately distinct questions won't), the duplicate slice should.

Community model: **Support-driven** — repeat questions, peers answering faster than the team.

## 3. Venue

**Chosen: Owned async forum** (hosted Discourse) — the highest surviving rung, at roughly an hour a day of batched moderation against durable, indexed, searchable answers. Setup/config answers have a multi-month half-life, and search-discoverability of existing answers *is* the deflection mechanism the purpose gate names — someone finding the answer via search before filing a duplicate ticket is the whole point. Priya's 7h/week maps almost exactly onto this class's ~1h/day standing-presence requirement, with margin left over for the ritual and FAQ curation.

**Considered, not chosen: forge-native discussions** (GitHub Discussions in your existing repo) — the cheaper default rung, and the audience is already partly there. Didn't win because: the duplicate-question rate you're seeing despite existing peer-answering suggests the *format* (unindexed issue threads) is the actual failure, not the willingness to answer — a structured forum with categories and "mark as answer" solves that directly, and you have daily-scale budget, not just weekly-scale. Keep this as the fold-back target if the forum underperforms (see §8) — the audience and the habit are already there.

**Not applicable: rented public space** — nothing to rent into, since the venue-vacuum gate passed (no existing space serves this need, pending the OpenFeature check above).

**Deleted by constraint: owned real-time chat** — deleted because the answers need to stay searchable for months, which real-time chat structurally can't do. Reopens only if the primary outcome shifts toward Product/Engagement and a second person is staffed for continuous presence.

Mechanics to re-verify before committing (pulled from skill reference, not live-checked): Discourse hosted Pro listed at $100/month, Business at $500/month, free self-host option. Re-check current pricing, data-residency options, and export terms on discourse.org/pricing before signing — these move.

## 4. Target member mix at 90 days

Founding cohort: 24 named invitees today; actively recruit 5–10 more, prioritized for NA/APAC working hours, before the public-open gate. Target founding cohort: 30, covering every major topic area in the 40+ historical questions with at least one reliable answerer, and at least two time zones.

Target at day 90: 5–8 contributors/advocates actively answering (up from the current 2), 15–20 participants posting at least monthly. Expect ~90% of the total membership to never post — that's the baseline, not a defect.

## 5. Seeding plan

Founding invitations: personal, specific asks to all 24 — not just the 2 you already trust. State exactly what you want ("answer questions in [topic], post at least once a week, for the first quarter") and time-box it. The skill's own failure pattern here is instructive: a vague ask produces silent non-answerers, and you may be undercounting your real bench because nobody's been asked concretely yet. Separately, and in parallel: source 5–10 NA/APAC candidates specifically — customers, community champions, sales/CS introductions — this is the actual gate-closing work, budget it as its own task with an owner and a deadline inside the next 3–4 weeks.

Seeded content: you already have the raw material — pull 8–10 of the most-asked historical questions straight from the repo, post them as the first threads, and have Priya (plus the one trusted second answerer) write real answers to all of them before anyone else sees an empty category.

Opened surface: start with 2–3 categories matching your actual topic clusters (e.g. install/setup, SDK-specific config, targeting rules) — not a full taxonomy. Add a category only once an existing one is visibly active.

Ritual: a weekly "resolved this week" recap thread, highlighting questions that got answered — models the behavior you want and gives lurkers a low-effort entry point. Add monthly office hours once a second reliable answerer is confirmed, timed to catch NA or APAC hours specifically (this doubles as your coverage test).

Published response-time commitment: publish a target once you know your actual coverage — while CE-only, commit to next-business-day for NA/APAC rather than same-day, and revise to <24h once a second-region answerer lands.

## 6. First 90 days

**Weeks 1–2 (private founding cohort, from ~22 Sept):** invites go out with specific asks, seeded threads go live, categories open, ritual starts.

**Weeks 3–6 (invited beta, ~6 Oct–2 Nov):** widen to the full founding cohort plus any newly recruited NA/APAC answerers; watch for the day-30 leading indicators (any post from outside the founding cohort, any question answered by a member rather than staff, the ritual running twice with attendance above the organizer, median first-response under a few hours in working hours). This is also where the seed-supply mitigation either lands or doesn't.

**Weeks 7–12 (public, earliest 4 Nov, gated):** open publicly only once the mitigation and the day-30 indicators are both green. If not, ship "beta open, general availability soon" messaging on the 4th instead, and re-check weekly.

## 7. Thresholds and measurement

Day-30 leading indicators: as listed above (member-authored answers is the one to watch hardest — zero at day 30 predicts a failed day-90 gate).

Day-90 pass thresholds (baseline, not yet recalibrated to Quillstack's own data — revisit once a month of real data exists):

| Signal | Pass |
|---|---|
| Questions answered within 24h | >90% |
| Posts written by non-staff | >50% |
| New members posting within 7 days | >40% |
| Monthly active / total members | >20% |
| Threads with ≥1 reply | >80% |
| Engagement share of top 5 members | <50% |

Given the thin current bench, also track the absolute count directly against the headline business metric: duplicate setup tickets/quarter, baseline ~12, target ≤6 by two quarters out — this is the number that actually justifies the effort to Priya's manager, independent of percentage bars.

Read every number against a trailing baseline, not the launch month — a marketing push produces a spike that decays, and comparing a quiet month to that spike is the most common false trend in community reporting.

Who measures: Priya, weekly during the beta window, monthly after; source is Discourse's native analytics plus a manual weekly sample while volume is low.

## 8. Fold-back criteria

If non-staff posting share is under 30% at day 90, or duplicate tickets haven't moved by one quarter out, merge back into the repo's own Discussions (the audience and the habit already exist there) rather than keeping a second, underperforming venue alive. If even that goes quiet, archive to read-only and publish the top 20 answers as static troubleshooting pages — near-zero standing cost, keeps the search value.

Decision owner: Priya.

## 9. Open risks

- **B2B assumption unconfirmed** — changes the buyer/user split and whether per-customer private channels get requested (gate those on contract value, staff as support, not community, if they come up).
- **Venue vacuum taken on your word** — worth one explicit check against OpenFeature/CNCF's community before fully banking this gate; a duplicate room next to an existing ecosystem space would split both.
- **Seed-supply mitigation is the real critical path** — everything else is ready; whether you find one NA/APAC-hours answerer in the next month decides whether 4 November is a real public-open date or a beta announcement.
- **Single point of failure** — with only 2 reliable answerers today, either one's absence stalls the room; the recruitment push above is also basic redundancy, not just coverage.
- **Data residency** — if any NA/APAC customers are enterprise with data-location requirements, check Discourse's hosting region options before committing to a plan.