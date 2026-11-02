## Kelpwood Series A press plan

**Fix this before the board meeting:** the 2,000-signup target is not deliverable by any outlet, and it should not stay in the deck as a press KPI. Pull it, replace with the metrics in section 8, before you present.

**Why:** developers pick tools by trying the docs and the product, not by reading articles — a 115-developer survey found tool selection runs on maturity, usability and documentation far more than visibility signals (Larios Vargas et al., ESEC/FSE 2020). Press buys credibility with people who never touch the product — investors, buyers, analysts, candidates, other reporters — plus durable discoverability. It does not buy a signup number, and no reporter or outlet controls how many people click through and register. Attributing a revenue/signup number to one placement is a named failure mode in this discipline, not a hedge I'm adding — report credibility and discoverability signals instead.

Open questions I answered by assumption — correct me and I'll re-cut the plan:

1. Audience ranking assumed: (1) engineering leaders/buyers evaluating Postgres tooling spend, (2) investors/analysts/candidates, (3) individual developers. Flip this if wrong.
2. Lead investor name, and whether their comms team has its own embargo rules — needed before locking the exclusive.
3. No named customer confirmed on record yet — needed for the strongest developer-press angle (see 2b below).
4. Effort ceiling (spokesperson hours, whether engineering can build anything new) not stated — assumed "founder/you + one engineer, nothing new to build."
5. Existing press page / prior coverage / known reporters — assumed none exist yet.

### 1. Qualification verdict

Scored against the five tests — passes, conditionally:

- **Newness** — real, dated event (round closes Oct 14). Pass.
- **Consequence** — engineering leaders re-evaluating preview-environment/CI database strategy have a reason to act. Pass.
- **Evidence** — round size, lead investor, and a growth number (40→900 teams, ~22.5x in a year) that already exists as a byproduct of running the product — no new data collection needed. Pass, once the growth number's methodology is nailed down (see below).
- **Conflict/shift** — real: Postgres branching / "git for your database" is an active, funded category (Neon, PlanetScale, Xata, Supabase all shipping and raising in this space). Pass.
- **Tellability** — pass, if the customer story in 2b doesn't happen; the round-plus-thesis story is tellable today with zero clearances outstanding.

**Verdict: this qualifies.** The trap named in the playbook is real, though — "we raised $12M" alone is a form, not a story. The round is the occasion; the category thesis is the story.

Before it goes in any pitch, fix the growth number's methodology: exact date range, what counts as a "team" (paying vs. trial), and confirm 40 was the real count a year ago, not a rounded estimate. A technical reporter's readers will check it.

### 2. Angle — recommended

Don't pitch the raise alone. Two viable angles, one removed:

| Angle | What it is | Effort | Recommend |
|---|---|---|---|
| **The shift + the number (combined)** | Category thesis — database branching going from novelty to funded, adopted practice — with the 22.5x team-growth stat as your evidence | Low: reframe facts you hold, no new build | **Yes — primary** |
| **The practitioner** | One engineer's before/after: what breaks when you test migrations against fake data vs. a real branch | Medium: needs 1hr of an engineer's time + customer sign-off | Pursue in parallel if a customer will go on record before Oct 14; don't block the plan on it |
| ~~The underdog~~ | Removed — no public, rerunnable comparison against incumbents exists (question 5 gap) |

Pressure test passed: if Kelpwood didn't exist, a reporter covering database/dev-infra funding would still write "branching is becoming standard practice, money is following" — you're the evidence, not the invention of the trend.

Compliance note: the growth stat is an aggregate customer count, not user activity data, so it doesn't need a consent/anonymization review — just a one-line methodology note in the proof pack.

### 3. Dated runbook (today = Sep 18, announce = Oct 14)

1. **Sep 18–22 (this week)** — Lock the angle above. Build press page + briefing pack drafts. Start the media map (§4). Start capturing baseline metrics now (§8) — you cannot measure a lift without a "before."
2. **Sep 29 (T-15)** — Decide exclusive vs. embargo (§5). If exclusive: pick one outlet, send the offer, give them a firm answer deadline.
3. **Oct 5–7 (T-9 to T-7)** — Open embargo to the rest of tier 1 with the full briefing pack. Run the open-source-style leak check even though you're not open source: check pricing page, careers page, investor's own portfolio page, any scheduled blog/changelog posts, LinkedIn "coming soon" posts from founders — nothing should reveal the round or the number early.
4. **Oct 8–11 (T-6 to T-3)** — Tier 2 pitches go out, adapted, after tier 1 has answered. Run one analyst briefing if you want it (§9, optional, not urgent).
5. **Oct 13 (T-1)** — Restate embargo terms (day, clock time, timezone) to every reporter holding it. Confirm spokesperson availability windows. Stage the owned post privately.
6. **Oct 14 (T0)** — Lift embargo. Owned post + press page go live first, coverage appears, then community channels — posted by a participant in that community's register, never as a press release copy-paste. Staff the whole window (§7).
7. **Oct 17 (T+3)** — Follow up only with reporters who haven't replied, only with new information.
8. **Oct 21 (T+7)** — Final follow-up, then stop. Start second-wave pitches to outlets that passed, using the coverage that did land as proof.
9. **Oct 28–Nov 14** — Pull the measurement window (§8) against your baseline. If the growth-number angle landed well, plan republishing it as a recurring benchmark — that's what makes it a compounding asset instead of a one-day hit.

### 4. Media map

I don't have web access approved in this session to verify real bylines and current employers, and this skill's hard rule is: **never invent a reporter, outlet, or email address.** So here's the structure to fill in, not a send list.

Outlet classes to work, in priority order for your audience ranking (engineering leaders first):

- **Developer-native trade press** (The New Stack, InfoWorld-type beats, database/infra columnists) — wants a checkable technical claim + an engineer to interview. Highest priority given your audience ranking.
- **Business/startup press** (TechCrunch-type, funding/infra reporters) — wants the round, the thesis, possibly the exclusive.
- **Enterprise-IT trade press** (TechTarget/SDxCentral-type) — wants deployment scale and buyer-side framing.
- **Practitioner newsletters** covering Postgres/data infra specifically — small audience, high intent, often outperforms trade press for adoption.

(Those named outlets are this skill's own calibration examples of what the classes look like in practice — not verified contacts. Confirm each still covers this beat before using it.)

For each candidate your team adds: read their last 5 bylines dated and on-beat, confirm current employer on the outlet's own site, note stated pitch/embargo preferences, score beat-match×3 / audience-fit×2 / responsiveness×2 / recency×1, tier at 30+ / 18-29 / below 18. I can run this verification myself once WebSearch/WebFetch access is approved for this session — say the word and I'll build the real 20-40 name map instead of the template.

### 5. Exclusive vs. embargo — recommendation

**Split it:** offer the funding scoop as an exclusive to one business/startup reporter with a track record of honoring embargoes (funding stories are exactly what exclusives are for), and run an embargo in parallel to developer trade press + newsletters for the category-thesis/growth-number story, both lifting at the same moment on Oct 14. Reporters with no track record with you get the news at lift time only — no embargo on a first contact.

State day, clock time, and timezone explicitly in every embargo email — "Tuesday morning" is not an embargo. Never offer the same exclusive to two outlets.

### 6. Briefing pack — funding-specific fields

- [ ] Round size, lead investor name, participating investors, prior total raised, what the money changes operationally.
- [ ] Growth stat with methodology (date range, definition of "team," paid vs. trial).
- [ ] Category-thesis paragraph — why branching is going from novelty to standard practice.
- [ ] 2-3 approved quotes that make a claim, not a feeling ("we knew X the day we measured Y" — not "thrilled to announce").
- [ ] Technical proof pack: running artefact/demo, comparison table including where you lose, known limitations, pricing stated plainly.
- [ ] Named press contact with a response time you'll actually honor.
- [ ] Banned words checklist run against every draft: revolutionary, disruptive, game-changing, paradigm shift, seamless, robust, world-class, next-generation, "excited to announce."

### 7. Day-of runbook

- One person owns each channel (owned blog, press replies, community threads) for the whole window — "as needed" is not a review cadence.
- Community post goes up from a real participant in that community's voice — never a press release pasted into a forum, never your own submission upvoted, never the first comment.
- Correct factual errors fast and specifically; let accurate-but-unflattering framing stand.
- If anything security-shaped comes up in a public thread, stop discussing it there — that's a different, private process, not a press-day problem.

### 8. Measurement — what actually replaces the 2,000-signup number

Capture the baseline **this week**, before anything ships — branded search, direct traffic, referring domains, docs/signup traffic. Without it, nothing after Oct 14 is attributable to anything.

| Signal | Worth to the board |
|---|---|
| Sales/procurement conversations citing the coverage | Strongest, slowest to show up |
| Inbound from partners, analysts, other reporters you couldn't have reached otherwise | Strong |
| Referring domains / link authority from the placements | Strong, durable |
| Coverage surfacing in AI-assistant answers about "Postgres branching" | Growing signal, spot-check by asking the question yourself |
| Branded search + direct traffic, 7-14 days vs. baseline | Directional only — useless if another launch overlaps your window |
| Docs/signup traffic in the window | Noisy — report the traffic bump, never claim press caused a specific signup count |

Refuse advertising-value-equivalency math if anyone on the board asks for it — that's not a personal preference, it's the PR industry's own 2010 consensus position (AMEC Barcelona Principles): AVEs are not the value of PR.

### 9. Optional, not urgent

One practitioner-focused analyst briefing (bring the engineer, spend the time on the adoption evidence not the demo) is reasonable given the raise — but it buys a correct mental model in buyer conversations, never placement in a paid evaluation. Skip it if the effort ceiling from question 4 is tight; nothing above depends on it.

**Next action:** get the lead investor's name and their comms contact today — that's the one blocker on locking the exclusive-vs-embargo split in section 5.