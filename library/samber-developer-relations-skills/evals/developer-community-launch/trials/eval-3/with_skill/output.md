**Verdict: Launch. Platform: GitHub Discussions (forge-native), not Discord/Slack/Discourse.** All 5 readiness gates pass on what you gave me. Full brief below — one thing to note: I picked **Support** as your single primary outcome (not all three), because that's the one with hard evidence right now. Product-input and advocacy get built in as secondary, sequenced, not dropped.

---

# Community Launch Brief — Fernbrook

## 1. Verdict

**Launch.** No delay, no mitigation needed.

| Gate | Status | Evidence |
|---|---|---|
| Demand | Pass | Same 4 questions arrive repeatedly by DM (repeat-question evidence); 2 users already answer each other unprompted in your issues (peer-answering evidence). |
| Owner | Pass | One named owner (you), 8h/week committed, stated as ongoing not just launch-quarter. |
| Purpose | Pass | Support, named as one measurable claim (below) — not three unranked wishes. |
| Venue vacuum | Pass | No existing space serves schema-migration-in-production users specifically; general dev forums (r/programming, r/database) don't capture this niche. |
| Seed supply | Pass | 45 named invitable people, above the 20-50 target, includes your 2 known peer-answerers. |

## 2. Audience and outcome

**Primary audience:** engineers who run schema migrations in production, inside your 150 paying teams and the 2,400 WAU installs. B2B: the person in the room (the engineer running `fernbrook migrate`) is often not the buyer (eng manager / whoever pays).

**Primary outcome (S — Support):** *"Cut repeat DM/support questions reaching you directly by 50% within two quarters, holding a <24h answer time inside the community."*

**Secondary outcomes, unranked, sequenced in — not started day one:**
- **P — Product:** once Support is stable, run a dedicated roadmap-input ritual (below) targeting 8+ usable feature/friction signals per quarter from people actually running migrations in prod.
- **A — Acquisition and advocacy:** once a visible core of answerers exists, convert 5+ of them per quarter into public advocates (testimonial, case study, referral).

Running all three as co-equal goals from day one is exactly the failure mode the skill flags ("trying to accomplish too many things makes it hard to track community value"). Support first is also the cheapest to prove — it's the one you already have hard numbers on.

**Community model:** Support-driven. Repeat questions, peers answer faster than you do.

## 3. Venue

**Chosen: Forge-native discussions → GitHub Discussions.** Highest surviving rung, ~1h/week standing presence, batched. You're already fielding this exact interaction pattern in GitHub issues — Discussions is nearly free to run because you're in that repo daily anyway.

**Deleted by constraint:**
- **Owned real-time chat (Discord/Slack)** — deleted. Migration troubleshooting answers stay valid for months (durable-answer test), and real-time chat's archive isn't indexed or searchable. Reopens only if the primary outcome shifts to Engagement/Product-in-the-moment *and* you staff continuous presence beyond your current 8h/week.

**Rejected on the ratio, not deleted (revisit later):**
- **Owned async forum (Discourse)** — good long-term value (search traffic, ownership, durable archive) but costs ~1h/day, eating most of your weekly budget. The rule for promoting to this rung needs thread volume to have *already* outgrown the repo — yours hasn't yet (4 repeat questions, 2 answerers). Promote here once: (a) GitHub Discussions volume outgrows the repo, and (b) you can give it a daily pass.
- **Rented public space (subreddit, ecosystem chat)** — no such space exists for this niche (that's your venue-vacuum pass), so there's nothing to rent into.

**Mechanics** (per GitHub's own docs): free, any authenticated user who can see the repo can post; creating/pinning/deleting categories needs write access; marking answers or locking needs triage access. Zero extra account needed for anyone already using your CLI's GitHub repo.

## 4. Target member mix at 90 days

**Founding cohort:** 35-45 of your 45 named people (drop only the clearly-passive ones). Anchor it on your 2 known peer-answerers — make them contributors from day one, not just members.

**Before sending invites, verify:** the list covers your different supported DB engines (don't seed 40 Postgres users and zero MySQL/other) and more than one time zone. You have the list — confirm the spread, I don't have it.

**Target at day 90:** 8-12 people behaving as contributors/advocates (answering regularly), 40-60 as monthly participants, the rest lurking (expect ~90% lurkers — that's baseline, not a defect).

## 5. Seeding plan

1. **Personal invites, not a blast.** Message each of the 35-45 by name: "Answer questions in [their area] once a week this quarter." Time-boxed ask, not vague.
2. **Seed 5-10 posts before anyone else arrives.** Start with your 4 known repeat DM questions — post and fully answer each yourself as the model behavior. Add one "show your production migration setup" post and one roadmap-input post.
3. **Open only 3 categories:** Q&A / Troubleshooting, Show & Tell, Roadmap & Feedback. No #general, no #jobs, no empty rooms.
4. **Ritual from week 1:** a weekly pinned "Roadmap & Feedback" thread — async, not a scheduled call. Async fits your 8h/week budget and avoids timezone conflict across paying teams.
5. **Publish a response-time commitment:** answer within 24h. Say this publicly on day one.

## 6. First 90 days

**Weeks 1-2 — private founding cohort:**
1. Open the 3 GitHub Discussions categories.
2. Send personal invites to the 35-45 named people (one message each, the specific ask, the time-box).
3. Post and answer the 4 seeded troubleshooting threads yourself.
4. Post the first weekly Roadmap & Feedback thread.
5. Publish the 24h response-time commitment.
6. Track: any post from outside the founding cohort, any question answered by a member (not you).

**Weeks 3-6 — invited beta:** gate this transition on activity, not the calendar. Expand invites to users who've filed 2+ GitHub issues or contacted you twice — but only after zero member-authored answers stops being true. If nobody but you has answered anything by day 30, stop expanding and re-seed instead.

**Weeks 7-12 — public:** announce via the CLI's own output (e.g. an update-notification line), README, changelog, and a direct email to the 150 paying teams. Do not announce to the full 2,400 WAU on day one — that spends your one first impression on a room with no culture yet.

## 7. Thresholds and measurement

**Day-30 leading indicators (watch behavior, not ratios yet):**
- Any post authored outside the founding cohort.
- Any question answered by a member, not you.
- Weekly ritual has run at least twice with replies beyond you.
- Median first response under a few hours during your working hours.

**Day-90 pass thresholds** (published baselines, recalibrate against your own trailing data once you have it):

| Signal | Pass |
|---|---|
| Questions answered within 24h | > 90% |
| Posts written by non-staff (not you) | > 50% |
| New members posting within 7 days | > 40% |
| Monthly active / total members | > 20% |
| Threads with ≥1 reply | > 80% |
| Engagement share of top 5 members | < 50% |

**B2B adjustment:** with 150 paying teams, this stays a small, high-value room. You're allowed to pass on absolute counts (every question answered, 5+ distinct people posting weekly) even if you miss percentage bars — state that trade explicitly rather than chasing a percentage a 40-person room can't hit.

**Who measures:** you, weekly, from GitHub Discussions' native activity view. No extra tooling needed at this size.

## 8. Fold-back criteria

If 2+ day-90 signals fail: **archive the Discussions read-only, redirect new questions back to GitHub issues (your plain support channel today).** No merge option exists — there's no other community for this niche to merge into, which is also why you're launching. Archiving keeps the indexed answers and their search value at near-zero ongoing cost.

**Decision owner:** you.

## 9. Open risks

- **Bus factor.** You're the only named owner. No backup if you're out sick or on vacation for two weeks. Consider naming one of your 2 existing peer-answerers as a standing co-moderator early, or accept this risk explicitly.
- **8h/week needs to survive past the excitement of month one** — confirm this is a standing figure, not a launch-quarter estimate that quietly shrinks.
- **Employer restrictions.** Some engineers at paying-team companies may not be able to post schema/infra details publicly. Post explicit guidance: sanitize examples, no real table/column names, no proprietary data.
- **45-name list is unverified for DB-engine and timezone coverage** — confirm before sending invites, not after.
- **Secondary outcomes creeping into week one.** The Roadmap thread is the only Product-outcome mechanism allowed before day 90 — resist turning every troubleshooting answer into a feature debate this early.

---

**Next action:** pick which 35-45 of your 45 people go in the founding cohort, and confirm they span your supported DB engines and more than one timezone. That list is the one thing only you have.