# Vireo Labs Community Slack — Diagnosis & Relaunch Brief

## 0. Assumptions I'm making (flag if wrong)

- Launch ~July 2025 (14 months back from now), lively through ~Jan/Feb 2026, flat since.
- "Platform users" = customers/users of your product, not an OSS/dev-tool community — so this is support + retention + advocacy infrastructure, not a dev-relations play.
- You have Slack admin access (Analytics tab or Enterprise Grid export), or can get it.
- No dedicated community manager has been running rituals — "a few messages a week, mostly us" reads as: nobody owns this.

Everything below still works if these are off — swap in real dates before you present anything.

---

## 1. Reframe before you touch a spreadsheet

"Failed experiment" is a verdict. You don't have evidence yet, you have a symptom (message count dropped). Don't walk into leadership with a counter-opinion ("no, it's not dead") — walk in with a diagnosis they can't argue with, then a decision framework, then a time-boxed bet with a pre-agreed kill switch. That's what makes it defensible: not that you're right, but that you can't be second-guessed on process.

---

## 2. The diagnostic: seasonal or dying — do this first, ~3–5 days

### Step 1 — Pull the raw series

From Slack Analytics (Admin → Analytics → Export) or the Enterprise Grid API, get **weekly** granularity for the full 14 months:

| Series | Why |
|---|---|
| Messages posted | Raw activity |
| Unique posters (not just readers) | Depth of participation |
| Messages from members with an `@vireolabs.com`-style / staff-flagged account vs. everyone else | Staff-ratio — the single most diagnostic number you have |
| New joins per week | Growth didn't stop even if talk did — check this |
| Removals/leaves per week | Slack rarely reports this well; approximate via member-count deltas |
| DAU, WAU, MAU | Standard stickiness |

If Slack's own analytics don't go back the full 14 months (free/standard tier often caps history), export what you can and supplement with a manual scrape of `#general`/`#announcements` message timestamps via the API — it's a one-off script, not a subscription.

### Step 2 — Look for a cliff, not a slope

Plot messages/week and unique-posters/week, 4-week rolling average. You're distinguishing two shapes:

- **Slope (decay curve)** — gradual decline over months → consistent with novelty wearing off, a real lifecycle pattern, survivable.
- **Cliff (step function)** — activity holds, then drops sharply within 1–2 weeks → something *happened*: a champion left, the team stopped seeding, a feature shipped that made the Slack unnecessary, onboarding stopped mentioning it, a CS/support workflow moved elsewhere (Zendesk, in-app chat).

Given what you've described — lively 6–7 months, then flat for ~7–8 straight months including a non-holiday stretch — a **pure seasonal effect is unlikely on its own**. Seasonal dips in B2B Slack communities are real but short: 2–3 weeks around December, a lighter dip in August. A 7-month flatline spanning spring and summer isn't seasonality, it's either a genuine collapse or a step-change event you haven't identified yet. Confirm this with the actual weekly plot before you say it out loud to leadership — but don't expect seasonality to be the answer.

### Step 3 — Segment by cohort, not just by week

Total member count (1,100) is a vanity number that's actively misleading you here — it went up while engagement went to zero, meaning growth and activity decoupled. Instead:

1. Take everyone who posted at least once in months 1–6 (your founding/active cohort). Chart their posting rate over time, isolated from everyone else. Did *they* individually go quiet, or did they leave and get replaced by silent joiners?
2. Take everyone who joined in months 7–14. What % of them ever posted once? If it's near zero, new joiners never had a reason or a prompt to participate — they joined, saw a graveyard, and lurked. That's not decay, that's a broken onboarding loop feeding a dead room.
3. Cross-reference against product usage if you can (even roughly): are the quiet members still active platform users, or did *product* usage also drop for that cohort? If product engagement is fine and only Slack engagement died, the cause is inside the community, not the business. If both died together, this isn't a community problem, it's upstream.

### Step 4 — Check what changed outside Slack

Ask, don't assume:
- Did anyone on your team who used to post regularly change roles, leave, or get reassigned around the cliff date?
- Did support/CS move to a different channel (in-app chat, a ticketing tool, a forum) around the same time?
- Did onboarding/welcome emails stop mentioning the Slack invite?
- Did a major feature ship that answered the most common questions people used to ask in there?

This last one matters because it flips the framing: fewer questions can mean the product got *better*, not that the community failed. Worth explicitly ruling in or out before anyone calls it a failure.

### Step 5 — Read the last 100 real messages before the cliff and the first 20 after

Not for data — for content. Look for: did the tone shift from peer-to-peer help to only official announcements? Did a specific thread go unanswered and visibly kill momentum? Anecdote won't win the argument alone, but it'll tell you *what* broke, which the numbers alone won't.

---

## 3. The dashboard — what to actually watch going forward

Stop watching total members. Watch these, weekly, on one page:

| Metric | Healthy | Warning | Dead | What it catches |
|---|---|---|---|---|
| **Staff message ratio** (your msgs / total msgs) | <30% | 30–50% | >50% | Flywheel reversed: you're broadcasting, not hosting |
| **Unique weekly posters / MAU** | >20% | 10–20% | <10% | Stickiness — is anyone actually talking |
| **New-member 7-day post rate** (% who post within a week of joining) | >40% | 20–40% | <20% | Onboarding — are new joiners activated or just parked |
| **Thread reply rate** (% of posts with ≥1 reply) | high | dropping | near 0 | Is the room reciprocal or a wall people shout at |
| **Non-staff content created** (tutorials, questions, show-and-tell, not just "hi") | rising | flat | zero | Real community-led activity vs. noise |
| **Founding-cohort retention** (% of month-1–6 active posters still posting) | tracked monthly | — | — | Are your original champions still there |

Total member count and join rate still matter, but only as a denominator, never as the headline. A community with 1,100 silent members and one with 150 loud ones are not comparable, and the first is worse.

---

## 4. Leading hypotheses, ranked by how well they fit your description

Given "lively first half year, then mostly us posting a few messages a week":

1. **Founding-cohort exhaustion with no replacement loop.** Classic pattern: the first 100–300 highly-engaged early adopters carried the room organically. Once they extracted what they needed (or moved on), nothing was built to replace their behavior — no rituals, no prompts, no reason for cohort 2 to behave the same way. Most likely, based on the shape you described.
2. **No core loop / no owner.** If nobody on your team had "grow this community" as an actual job, it ran on founder/early-adopter energy until that ran out, then defaulted to occasional company announcements. Also very likely — "mostly us" is the tell.
3. **Channel/identity confusion.** If the Slack was never clearly "this is for X" (peer support? feedback? networking?), there's no reason for a member to open it on a random Tuesday. Worth checking against your original launch framing.
4. **A real step-change event** (team member left, support moved elsewhere, feature shipped). Check Step 4 above — if you find one, this is actually the *easiest* case to present to leadership, because it has a named, fixable cause.
5. **Product matured, fewer questions needed.** Possible but check it against product usage data before leaning on it — don't let this become a convenient excuse without evidence.

You'll likely find it's 1 + 2 compounding: no owner meant no one replaced the founding cohort's energy once it faded.

---

## 5. What makes the case to leadership defensible

Don't bring an opinion. Bring this structure, one page:

1. **Finding** — the actual shape of the decline (cliff or slope), with the chart, dated.
2. **Ruled out / ruled in** — seasonality (ruled out, or in, with the reasoning from Step 2), the named causes from Step 4.
3. **Root cause** — stated as a specific, falsifiable claim ("founding cohort exhausted, no onboarding loop replaced it"), not a vibe.
4. **Decision framework, agreed *before* you relaunch anything**:
   - Define the bet: e.g., 90 days, X hours/week of owned community management, specific interventions (below).
   - Define success criteria numerically, in advance: e.g., staff ratio under 40%, unique weekly posters above 8% of MAU, non-staff posts up 3x from baseline — by day 90.
   - Define the kill criteria too, explicitly, in advance: if none of those move by day 60, sunset formally rather than let it decay quietly again.
5. **Ask** — what you need (headcount/time, budget for a small program, leadership visibility for kickoff).

This is the actual defensibility mechanism: pre-registering success *and* failure conditions means nobody can retroactively move the goalposts, including you. It also directly answers "prove it's not a failed experiment" — because right now nobody can prove or disprove anything, there's no baseline and no owner.

---

## 6. The relaunch plan, if the diagnosis supports "orphaned, not dead"

**Phase 0 (week 1–2): Recruit before you announce.**
Identify the 20–30 most active posters from months 1–6 (pull directly from your Step 3 cohort data). DM them individually, not a broadcast — ask what they got out of it, why they stopped, what would bring them back. This is your qualitative validation of the quantitative diagnosis, and it doubles as your founding-member reseed list.

**Phase 1 (week 3–6): Rebuild the core loop.**
- Pick one weekly ritual and commit to it publicly for 90 days minimum (e.g., a Monday "what are you working on / what's blocking you" thread, or Friday office hours). Rituals create habit; announcements don't.
- Reactivate 10–15 of the Phase 0 members as seeded first responders — ask them to show up for the first month of rituals, tell them explicitly they're being asked because they mattered the first time.
- Get the staff-ratio metric visible to your own team weekly so posting habits don't silently drift back to "mostly us."

**Phase 2 (ongoing): Replace what the founding cohort did for free.**
- New-member journey: a real welcome flow (pinned post + one direct prompt in the first week), not just an invite link.
- Recognition: surface member wins publicly — this is what turns lurkers into posters, and posters into advocates.
- Assign an actual owner. This is the single highest-leverage fix — "no owner" is likely half your root cause, and no ritual calendar survives without one.

**Phase 3 (day 90): Review against the pre-agreed criteria from Section 5.** Report the result either way — including if it says kill it. That's what makes this whole effort credible the *next* time you propose a community investment.

---

## 7. This week, concretely

1. Get the weekly message/poster/staff-ratio export going, full 14-month history.
2. Chart it. Confirm cliff vs. slope and the real date range of the dead period.
3. Pull your top-30 cohort-1 poster list and start the DMs.
4. Check with CS/support/onboarding whether anything moved away from Slack around the cliff date.
5. Draft the one-pager from Section 5 once 1–4 are done — don't present before you have the chart.