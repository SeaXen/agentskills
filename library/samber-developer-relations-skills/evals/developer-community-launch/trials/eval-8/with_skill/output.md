# Developer Community Launch Brief — Northkeep

## 1. Verdict

**Launch.** All five gates pass, two with an assumption flagged for you to confirm before committing budget.

| Gate | Score | Evidence |
|---|---|---|
| Demand | Pass | The same 8-9 pipeline-tuning questions recur monthly across *different* accounts — repeat questions arriving that another user could answer. Two customers already swapped notes on a call, unprompted — the second, stronger demand signal (peer conversation already happening). Pipeline tuning is a deep enough problem domain to sustain ongoing conversation, not a one-time quickstart topic. |
| Owner | Pass | Marcus, named, 10h/week stated as an ongoing figure, not just a launch-quarter figure. That clears the owned-async-forum floor (~1h/day ≈ 7h/week) with headroom for the unscalable founding phase (answer every post, name-check every member). |
| Purpose | Pass (confirm wording) | Naming it for you, since the brief needs one: **Support** — "peer answers absorb the 8-9 recurring tuning questions currently resolved 1:1 by CS/support engineers; cut repeat 1:1 escalations on these known topics within two quarters." Secondary, unranked: Success (adoption/renewal narrative feeds the VP-facing story in §5). Confirm Support is really the primary you want tracked — if it's actually Success (upsell/expansion) driving this, the thresholds in §7 shift. |
| Venue vacuum | Pass | No existing space already serves these data engineers around this product, and it couldn't structurally — a chunk of the audience works at banks/insurers barred from public spaces at all. Nothing to join instead of building. |
| Seed supply | Pass (confirm coverage) | 30 named invitees clears the 20-person floor. Not yet confirmed: whether those 30 cover all 8-9 recurring topics with a reliable answerer each, and span your customers' time zones. Check this before finalizing the list — headcount alone doesn't pass this gate, coverage does. |

## 2. Audience and outcome

**Primary audience:** data engineers at the 55 customer accounts — the people who'd actually run into tuning problems and want to compare notes. Not the VP of Data buyers, who sign the renewal but won't post.

**B2B.** This changes the plan in ways worth calling out up front:
- User and buyer differ. Section 5 below carries a separate signal path to the VP, since the community itself will never reach them directly.
- A meaningful share of members can't paste code or describe architecture publicly — not a preference, a compliance constraint from their employer. This shapes both the venue (§3) and the ground rules (§5).
- Three accounts have asked for private per-customer channels — a B2B-specific pull toward fragmentation, handled separately in §5.

**Primary outcome (SPACES: Support):** cut duplicate 1:1 pipeline-tuning questions by routing them into durable, peer-answerable threads. Secondary: Success — the resulting archive becomes evidence for renewal conversations, but it isn't what gets measured at day 90.

**Community model: Support-driven** — repeat questions, peers answering faster than your team can. This is the model the SPACES letter picks; it isn't a separate choice.

## 3. Venue

**Chosen: Owned async forum**, invite-only, closed to the public internet (login required, no anonymous read access). This is the *only* venue class left standing once the constraints below are applied — not a top-of-ranking pick among live options.

**Why the other three are gone, not just ranked lower:**

- **Rented public space** and **forge-native discussions** — both deleted outright. The skill's own rule: *"A contractual privacy requirement, or members who cannot post in public under their employer's rules → deletes the rented public space and forge-native discussions, both public by construction."* Your banked/insured customers can't participate in either, and running a public venue that a meaningful slice of your paying base is banned from joining is worse than not launching.
- **Owned real-time chat** — also deleted, on a different rule: *"Answers stay useful for months, or search traffic on them is a wanted acquisition channel → deletes owned real-time chat, which is not indexed."* Pipeline-tuning answers have a long half-life — the same 8-9 questions keep recurring, which is direct evidence today's answer is still the answer in six months. A chat log that scrolls away is the wrong shape for that. (Marcus's 10h/week is a second, weaker argument in the same direction — real-time chat is "a standing job," and 10h/week is better spent as batched forum moderation than as always-on presence.)

That leaves owned async forum as the only surviving rung, at roughly an hour a day of batched moderation against durable, indexed, peer-searchable answers — which happens to be exactly what the demand evidence (repeat questions, long-lived topic) calls for.

**Vendor: Discourse**, self-hosted or on a hosted plan with a data-residency option, configured fully private (`login required` site setting + private categories, no public-facing pages). Cost is per-instance, not per-seat, which suits a small membership that may grow slowly.

*Not verified in this session — check before committing:* current Discourse pricing/hosting tiers, and specifically whether the hosted plans offer EU (or other) data-residency options if any of your banks/insurers require it. Quote the check date in the final brief.

**Deleted by constraint, with the reopening trigger:**
- Rented public space — reopens only if the regulated-employer constraint stops applying to a majority of the audience (unlikely).
- Forge-native discussions — same trigger; also doesn't apply if Northkeep has no public repository these users would have accounts on.
- Owned real-time chat — reopens if the outcome pivots from Support/durable-answers to Product or Engagement (value that lives in the moment) *and* someone is staffed for daily presence, not 10h/week batched.

## 4. Target member mix at 90 days

Founding cohort: the 30 named invitees, plus the two customers already observed swapping notes on a call — they're your fastest path to a first real advocate pair, since they're already doing the thing you want the forum to enable. Cover all 8-9 recurring topics with at least one reliable answerer per topic; cover every time zone your 55 accounts sit in (confirm this against the 30 names — flagged in §1 and §9).

Given 55 accounts total, this is a **deliberately small, high-value B2B room** — expect a ceiling somewhere around 60-120 eventual members, not thousands. Target absolute counts, not percentages (see §7).

Target mix at day 90: 5-8 members behaving as contributors/advocates (answering unprompted), 15-20 as participants (posting when they have a question or a tip), the rest as explorers. A launch that only recruits explorers produces silence — the founding 30 need to include people who already answer, not just people who ask.

## 5. Seeding plan

**Founding invitations:** personal ask to each of the 30, naming why them specifically and what you want ("answer questions in [topic], post roughly weekly, for one quarter"). Lead with the two who already swap notes — ask them explicitly to keep doing that in the open, in the forum.

**Ground rules, written before day one, not after a policy violation:** the bank/insurer constraint means "how do I ask this without pasting real config or architecture" has to be modeled from the first seeded post — sanitized examples, describe the shape of the problem rather than paste the pipeline. This is the single most important piece of the "vibe" doc for this audience; skipping it is what produces either silence (people afraid to post) or an incident (someone posts what they shouldn't).

**Opened surface:** categories built around the 8-9 recurring questions you already track from support/call notes — not a generic taxonomy. Fewer categories with visible activity beats a complete tree of empty ones; add a category only once an existing one gets noisy.

**Seeded content:** turn the 8-9 known recurring questions into 5-10 real seeded threads with real answers — this content already exists in your support history, it just needs to move into the open. Seed the answers too; an unanswered seeded question teaches newcomers that questions go unanswered here.

**Ritual:** monthly "pipeline tuning office hours" call, run by Marcus, layered on top of the forum. This gives the founding cohort a live, recurring reason to show up (and a second, faster channel to surface material worth writing up as a forum thread afterward) without asking Marcus for daily real-time presence.

**Published response-time commitment:** replies within 24 business hours — matched to a weekday-business-hours B2B cadence and to what 10h/week can actually sustain, not the 24-hour-including-weekends bar the published threshold anchors on.

**What does *not* go in this venue:**
- The three accounts asking for a dedicated private channel. Per the B2B pattern this skill flags directly: private per-customer channels fragment the community and drift into support contracts. Gate them on contract value (e.g., top-ACV tier) and staff them as CS-owned support, out of Marcus's 10h/week and out of the shared forum's scope entirely. Don't let this quietly become three more things Marcus owns.
- A path to the VP of Data. Since the buyer won't post, build a separate, lightweight artifact instead: a quarterly one-pager per account ("N questions resolved, M tuning wins, contributors from your team") that CS/AE carries into QBRs and renewal conversations. This is a report, not a second community surface, so it doesn't trip the one-venue rule.

## 6. First 90 days

**Weeks 1-2 (private, founding cohort only):** the 30 invitees + the two known note-swappers. Seed the 5-10 threads from existing support history. Publish the ground rules (including the no-real-config guidance) before the first real question lands.

**Weeks 3-6 (invited beta):** widen to additional data engineers across all 55 accounts, gated on observed activity in the cohort — specifically, at least one non-staff (non-Marcus) answer having appeared — never on a calendar date. Run the first office-hours call in this window.

**Weeks 7-12 ("public" = full customer base, still closed to the internet):** open the invite to every eligible data engineer at all 55 accounts, folded into onboarding for new accounts going forward. This is not a public announcement in the open-source sense — the room stays invite-only throughout, given the regulated-industry constraint; "public" here means "everyone who's entitled to be in the room," not "anyone on the internet."

## 7. Thresholds and measurement

**Day-30 leading indicators:**
- Any post authored by someone other than Marcus.
- Any question answered by a member rather than by Marcus.
- Both known note-swapping customers active as posters.
- Median first response under a few hours during weekday business hours.

Zero member-authored answers at day 30 predicts a failed day-90 gate — act then, don't wait for the quarter to close.

**Day-90 thresholds, set as absolute counts** — per the skill's own guidance for a small, high-value B2B room, where percentage bars misread a 60-120-person room the same way they'd misread a healthy 40-member customer community:

| Signal | Pass |
|---|---|
| Recurring topics (of the known 8-9) with at least one peer-authored answer | ≥ 7 of 9 |
| Distinct accounts represented among posters | ≥ 10 of 55 |
| Members other than Marcus who've answered someone else's question at least once | ≥ 5 |
| Median first-response time | ≤ 24 business hours |
| Office-hours attendance | above Marcus alone, at least 2 of the first 3 sessions |

Basis: the topic-coverage and account-breadth rows are set here for this room's size, adapting the skill's published-baseline percentage table (>50% non-staff posts, >80% threads with a reply) down to counts a ~60-120-person B2B room can actually produce. The response-time row descends from the Mozilla 48-hour finding GitHub's Open Source Guides cites, tightened to 24h to match a paid-support relationship. Re-baseline all of these against Northkeep's own trailing data once one quarter of real numbers exists — treat this table as a starting hypothesis, not a standard.

**Who measures:** Marcus, weekly, by manual sampling — at this size, the forum's native analytics will be thin, and instrumentation Marcus can't maintain alongside 10h/week of moderation isn't worth building.

**Reading rule:** if two or more of the five rows fail at day 90, that's a signal to re-run the seeding steps (recruit more reliable answerers, reseed dormant topics) or trigger the fold-back below — not to push a wider invite into a quiet room, which only dilutes the ratios further.

## 8. Fold-back criteria

If fewer than 7 of the 9 recurring topics have a peer-authored answer, or fewer than 5 non-Marcus members have answered anything, by day 90: **archive to read-only**, keeping the seeded Q&A as a searchable reference, and fold the recurring-question handling back into the CS/support queue as an internal knowledge base fed by the same 8-9 topics.

("Merge into the space the audience already uses" is skipped, not chosen last — the venue-vacuum gate passed precisely because no such space exists for this audience.)

Decision owner: Marcus, with sign-off from whoever owns his 10h/week allocation.

## 9. Open risks

- **Purpose gate wording** (§1) — confirm Support is the outcome you want tracked, not Success; the day-90 table changes if it's actually the latter.
- **Seed-supply coverage** (§1, §4) — the 30 named invitees clear the headcount floor but haven't been checked against topic and time-zone coverage. Do that before the week-1 invitations go out.
- **Data residency** (§3) — if any of the bank/insurer accounts have a stated residency requirement, confirm Discourse's hosting options satisfy it before signing anything; not checked in this session.
- **Three private-channel requests** (§5) — these need a decision from whoever owns the CS/support budget, separate from Marcus's community time. Left unresourced, they'll either get absorbed into Marcus's 10h/week (breaking the owner gate's own math) or the three accounts will escalate past DevRel to their AE anyway.
- **VP renewal artifact** (§5) — the quarterly one-pager needs an owner on the CS/AE side; it doesn't run itself off the forum.