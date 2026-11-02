# Community Launch Brief — Tenvale (Rust static-analysis tool)

## 1. Verdict

**Do not launch a community.** Two of five gates fail outright, and they're the two a bigger budget can't fix — this isn't a resourcing problem, it's an evidence problem.

| Gate | Status | Evidence |
|---|---|---|
| Demand | ❌ Fail | 5 tickets/month, none repeating; zero observed instances of a user answering another user, anywhere |
| Owner | ✅ Pass | Nils named, 4h/week committed and sustainable (not just launch-quarter) |
| Purpose | ✅ Pass | SPACES: Product — "~10 usable roadmap signals per month," which is a measurable claim, not a restated wish |
| Venue vacuum | ❌ Fail | The Rust ecosystem Discord already runs an active channel on this exact problem space, and some of your users already post there |
| Seed supply | ✅ Pass | 35 named invitees, above the 20-person floor |

3 gates pass, 2 fail → per the readiness rule, that's "do not launch," not "launch on a delayed date." A written mitigation only buys you a delay when *one* gate is weak; here two are dead, for structural reasons (no repeat demand to serve, and a room that already exists).

## 2. Why these two failures are the ones that matter

- **Demand fail is disqualifying on its own.** A community's entire value proposition is peer conversation replacing you. With nothing repeating and zero peer-to-peer answers anywhere — not your channels, not theirs — there's no appetite to house. Opening a room doesn't create the appetite; it just gives you an empty room to explain later.
- **Venue vacuum fail means launching would be building a second, worse copy of something that already works.** The Rust Discord channel already has traffic, moderation, and a handful of your own users in it. A competing Tenvale space would split that conversation across two rooms until both look dead — the exact "audience split" failure mode this playbook warns against.

## 3. What to do instead — and why this one, not the other four

The standard menu, ranked by evidence bought per hour of standing presence:

`answer publicly where the audience already is > forge-native discussions > troubleshooting/FAQ surface > scheduled office hours > email/issue feedback loop`

That ranking re-orders itself in exactly one situation: **when the audience is already gathered in an active ecosystem space, answering publicly gets promoted to the point that nothing else is worth starting.** That's precisely this case. Recommend it, and nothing else:

**Nils spends ~1 of his existing 4 hours/week participating in the Rust ecosystem Discord channel**, under the Tenvale name, answering questions and engaging in threads that touch your problem space. No new venue, no signup flow, no moderation obligation — that channel's owners already carry all of that.

To turn this into the "10 usable roadmap signals a month" the exec team wants, add one cheap piece of process, not a platform:

- **Define a "usable roadmap signal"** up front: a specific, attributable pain point, workflow complaint, false-positive/negative report, or feature ask — not a vibe. Write the definition down before counting anything, so the number can't be gamed later.
- **Nils logs every signal he sees** — from the Discord channel *and* from the existing 5 monthly tickets, which are an underused feedback source in their own right — into a single running doc (a spreadsheet, a private GitHub Discussion, whatever's already at hand). No new tool.
- **Report the count monthly**, alongside where each signal came from (Discord vs. tickets). This is the artifact you bring back to the exec team next time, in place of a launch.

Cost: $0 budget, ~1 hour/week of time Nils already has. Nothing to keep alive if it doesn't work, and nothing to shut down publicly if it fails.

## 4. Why not the other alternatives

- **Forge-native GitHub Discussions** — cheap and durable, but it duplicates a room that already exists elsewhere for this exact audience; opening it now is the same audience-split risk as the Discord idea, just owned by you instead of them.
- **FAQ/troubleshooting page** — this is a Support-outcome instrument. Your outcome is Product, and your ticket volume is already low and non-repeating, so there's nothing to deflect.
- **Office hours** — promoted only when *seed supply* is the failing gate. Yours passes (35 names); this would just be more standing effort than the signal you'd get back.
- **Issue/email feedback loop** — real product-feedback value, but it's a second, parallel effort. There's no reason to build a bespoke intake channel while the Rust Discord conversation you'd be mining is already happening for free.

## 5. Re-decide when, not if

Don't leave this as a permanent no. Re-run the gates when any of these show up:

- The same issue starts repeating 3+ times a month in support (demand gate starts passing).
- You see a user answer another user unprompted, anywhere — that Discord channel, GitHub issues, wherever (demand gate).
- The Rust Discord channel's moderators shut it down, restrict your participation, or the channel goes dead (venue vacuum gate reopens).
- The cheap alternative above stalls well under 10 signals/month for two straight months despite honest effort — that's a sign the venue-vacuum call was wrong, not that you need more budget.

## 6. The line for the exec team

*"We looked at the real numbers — no repeat support demand, no peer-to-peer behavior anywhere, and the room we'd be building already exists and has some of our users in it. A community would cost us a standing moderation job to solve a problem we don't have yet. Instead, Nils spends one hour a week where our users already are, and we'll have a monthly count of roadmap signals with zero new spend. We'll revisit the moment the evidence changes."*