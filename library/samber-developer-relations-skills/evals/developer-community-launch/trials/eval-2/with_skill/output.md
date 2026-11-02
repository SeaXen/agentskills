# Community Launch Brief — Orbwright

*Skill used: `developer-community-launch`. Route check: this is a from-zero launch decision, not an existing-community question, so the gates run before anything about Slack gets treated as settled.*

You've already provisioned Slack. Running the gates anyway — same as the skill's own worked example — because the venue is a hypothesis until the gates confirm it, and the date it opens is the cheapest thing to move if the answer changes. **It does change: the evidence here points away from Slack.** Details below.

---

## 1. Verdict and evidence

**Launch.** All five gates pass.

| Gate | Verdict | Evidence |
|---|---|---|
| Demand | Pass | 20–30 configuration questions/month by email, ~1/3 (7–10) duplicates of already-answered questions; separately, 4 users already answer each other unprompted in GitHub issues. Two independent signals, not one. |
| Owner | Pass | Dario, named, 6h/week protected indefinitely — a sustained figure, not just a launch-quarter allowance. |
| Purpose | Pass | SPACES: **Support** — "cut duplicate configuration questions reaching the inbox by half within two quarters, and give error-string searches a page to land on instead of nothing." |
| Venue vacuum | Pass | No third-party space serves this audience for Orbwright-specific config questions. GitHub issues carries some of the peer-answering already, but issues are the wrong shape for open Q&A (they close, aren't organized as an archive) — that's a reason to move it to Discussions, not evidence a venue already exists. |
| Seed supply | Pass | 60 named invitees across 4 topic areas and 3 continents — above the 20–50 range this gate wants. |

No weak gate, so no mitigation-gated delay is needed — this isn't the four-of-five case.

---

## 2. Audience and outcome

**Primary audience:** engineers integrating Orbwright's task queue into production backends, across ~900 paying teams — implementers who hit config and error-handling questions, not evaluators.

**B2B.** Buyer and user likely differ (whoever signs the commercial license vs. the engineer configuring workers/retries). This launch serves the implementer population; it is not a renewal-signal channel. Flag that separately rather than asking one venue to do both jobs.

**Primary outcome (SPACES: Support):** cut duplicate configuration questions reaching Dario's inbox, and turn "googled the error string, found nothing" into "found the answer." Secondary, explicitly unranked: surfacing recurring pain points that could become fixes or docs — don't let this compete with Support for the launch's design.

---

## 3. Venue — and why it isn't Slack

**Chosen: forge-native discussions (GitHub Discussions on the Orbwright repo).**

Walking the skill's own decision rule, in order:

- **Owned real-time chat (Slack) is deleted, on two independent constraints**, not one:
  - *Presence:* "An owner who cannot be present most days deletes owned real-time chat." Dario is heads-down on the engine most of the week and batches community time into 2–3 afternoons — not most-days presence, which real-time chat requires to not go dead between his sessions.
  - *Durability and search value:* "Answers stay useful for months, or search traffic on them is a wanted acquisition channel → deletes owned real-time chat, which is not indexed." Both are true here — config answers hold for a year-plus, and the stated reason you want this at all is that error-string searches land nowhere. Slack's archive doesn't index, and free-tier Slack caps history at 90 days, which would delete the very thing you're building this for.
- **Owned async forum (Discourse) doesn't get promoted, on the skill's own promotion rule**: it only moves up from the default rung when search traffic is a named acquisition channel *and* the owner has a daily pass to give. You have the first (search traffic is explicitly the motivation) but not the second — Dario's pass is batched, not daily. One condition without the other means it stays at the default rung, not that it's ruled out forever.
- **Forge-native discussions survives everything**: no extra account (your 900 customers already use the repo for issues — that's your own evidence), indexed and exportable, an hour a week batched rather than daily presence, and it's where the 4 existing peer-answerers are already behaving like community members. Default rung, nothing here displaces it.

**Rejected on the ratio:** Discourse — right instinct (durable, indexed, search-friendly), wrong owner-availability fit right now. Revisit if thread volume outgrows the Discussions tab or a second person picks up a daily pass.

**Deleted by constraint:** owned real-time chat (Slack) — reopens if a second, dedicated, daily-present owner joins *and* the primary outcome shifts toward Product/Engagement (moment-to-moment value), not Support.

**What to do with the Slack workspace:** don't run it as the primary venue. Per the one-venue rule, two owned venues before either reaches critical mass just splits four answerers across two empty-looking rooms. Park it rather than delete it — no need to announce or promote it. If you later want a distinct, non-overlapping job for it (e.g., a live kickoff call for the founding cohort, not standing support), that's fine — but say so explicitly so members know Discussions is where questions go.

**Mechanics:** GitHub Discussions has no separate cost, needs write permission to create categories, triage permission to mark answers — confirm someone with triage access is assigned (Dario or a delegate) before opening. Confirm all ~900 customers, not just a subset, actually have read/comment access to the repo before treating Discussions as the customer-facing venue — if the repo is private to some contract tiers, that's a real access gap to close first.

---

## 4. Community model and target member mix

**Model: Support-driven** — repeat questions, peers answering faster than the team. This is what the demand evidence already looks like; the launch formalizes it rather than inventing a new dynamic.

Two shapes were on the table before landing here:
- *Support-driven on Discussions, private founding cohort first* (chosen) — lowest risk, matches Dario's batched cadence, and the 4 existing answerers give it a running start.
- *Skip the private phase, open straight to the full 60* — rejected: nothing here is on fire (4-tickets-a-week volume), so there's no reason to spend the single first impression on an unseeded room just to move faster.

**Target mix at day 90:** the 4 known peer-answerers plus 4–6 more recruited from the 60, covering all 4 topic areas and all 3 continents as contributors/advocates; beyond that, participants posting at least monthly from the wider customer base once public. Most of the 900 will lurk — that's the 90-9-1 baseline, not a defect.

---

## 5. Seeding plan

- **Founding cohort — recruit 20–30 of the 60 by name**, not all 60 at once. Specific ask per person: "answer questions in [their topic area], post roughly once a week, for one quarter." Start with the 4 existing GitHub-issue answerers — they're already behaving like advocates. Before inviting, confirm the 20–30 actually cover all 4 topic areas and all 3 continents; don't assume it falls out of a random 30.
- **Open a small surface**: categories matching your real 4 topic areas — name them from Dario's own taxonomy, not generically — plus one "Troubleshooting / error messages" category built specifically to catch the searched-for error strings. Fewer categories with visible threads beats a full tree with empty rooms.
- **Seed 5–10 posts from material you already have**: pull the highest-frequency of the ~7–10 monthly duplicates and Dario's own past email answers — he's already written the content, this is a repost, not new work. Seed the *answers* too, ideally from founding-cohort members rather than Dario every time, so day one doesn't read as "ask Dario."
- **Ritual**: skip a fixed-time live call — 3 continents makes any single slot exclude someone, and Dario's afternoons aren't a fixed slot. Instead, a recurring **async weekly roundup thread**, posted during one of his batch afternoons: unanswered threads from the week, plus one seeded "ask us anything" prompt. Habit-forming without requiring synchronous attendance.
- **Response-time commitment, stated honestly**: aim for first response under 24h from *anyone* — peer or staff, since peer response is the actual point. Dario sweeps every open thread on each of his 2–3 weekly afternoons as a backstop, so nothing sits unanswered past 3–4 days even in the worst case. Publish this commitment as written, not as an implied 24h-from-staff promise Dario's schedule can't keep.

---

## 6. First-90-days calendar

- **Weeks 1–2 (private founding cohort):** invite the 20–30, open categories, seed 5–10 posts and their answers, run the roundup ritual twice.
- **Weeks 3–6 (invited beta → full 60):** expand to all 60 named invitees. Gate the move to public on activity, not the calendar: at least one post from outside the founding cohort, at least one member-answered question, the ritual running on schedule with attendance above Dario, median first response under a few hours during overlapping hours. Zero member-authored answers at day 30 is the signal to fix seeding before going further, not to push promotion harder.
- **Weeks 7–12 (public):** announce to the full ~900-team customer base (release notes / customer email, not a general newsletter blast — this audience is already identified). If Orbwright's error messages or docs can link out, point them at the Discussions category now — that's the direct fix for "people google error strings and land nowhere," and it compounds as more threads get indexed.

---

## 7. Thresholds and measurement

**Day-30 leading indicators:** any post from outside the founding cohort; any question answered by a member, not staff; the roundup ritual run twice with attendance above Dario; median first response under a few hours during overlapping working hours.

**Day-90 thresholds** (baseline, adapted — recalibrate against your own trailing data once it exists):

| Signal | Pass (baseline) | Adjustment for Orbwright |
|---|---|---|
| Questions answered within 24h | >90% | Track alongside "answered within 3 business days" — the 24h bar assumes daily presence you don't have; the 3-day figure is the honest backstop given Dario's batching. |
| Posts from non-staff | >50% | At ~20–30 questions/month total, also track the absolute count (e.g., 4+ distinct non-staff answerers/month) — percentages swing hard on a small base. |
| New members posting within 7 days | >40% | As published. |
| Monthly active / total members | >20% | As published, but measure against the ~60 invited, not the ~900-team base, until the public phase is well underway. |
| Threads with ≥1 reply | >80% | As published — this is the one that matters most for the SEO goal: an unanswered thread ranks for the error string and still fails the user. |
| Engagement from top 5 members | <50% | As published — watch this closely given the founding cohort is deliberately small; concentration risk is real with only 4–6 core answerers. |

Two or more failing at day 90 → re-run seeding on the specific failure, don't add promotion. Report active-member counts alongside every ratio, not membership totals — a big invite list with a quiet room is a failed launch with good optics.

**Basis:** thresholds are published baselines (Nielsen 90-9-1, GitHub/Mozilla 48h-review finding, CNCF recurring-activity rule) with cutoff values set as starting hypotheses per the skill's own caveat — recalibrate after one full quarter of real data.

**Who measures:** Dario, monthly, from GitHub Discussions' native insights plus a manual weekly sample given the low volume doesn't justify separate instrumentation.

---

## 8. Fold-back criteria

If two or more day-90 signals are still failing at day 120, after one targeted re-seeding pass on the specific failure: **archive Discussions to read-only**, republish the top 20 answered threads as permanent troubleshooting pages linked from error output/docs — this keeps the original motivation (search-landing for error strings) alive even in the fail case — and route new questions back to email.

Decision owner: Dario.

---

## 9. Open risks

- **Dario's batched cadence vs. a 24h response bar** — mitigated by the peer-first commitment and the 3-day staff backstop; watch day-30 for whether peers actually cover the gap or it silently becomes "wait for Dario."
- **Repo access for all ~900 customers unconfirmed** — if any contract tier lacks repo access, they're excluded from the venue serving them; verify before the week-7 public announcement.
- **4 topic areas and 3 continents not yet mapped onto the 60 invitees** — confirm coverage before finalizing the founding-cohort list; don't assume it falls out evenly.
- **The parked Slack workspace** — a visible, already-built thing that didn't get used reads as indecision internally; worth one line to the team explaining why Discussions won the gates.
- **Concentration in the founding cohort** — with only 4–6 core answerers at day 90, losing two of them is a real setback; the top-5-engagement-share threshold exists specifically to catch this early.
- **Employer network/access constraints** — low risk here specifically because the audience already uses github.com for issues; no new access surface is being introduced.