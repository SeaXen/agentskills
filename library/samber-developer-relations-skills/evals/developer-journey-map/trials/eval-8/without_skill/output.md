# Thistlewrap contributor journey map

## Core problem

3,800 stars, 2 outside PRs a quarter, first-timers don't return. Not a discovery problem — stars prove discovery. Not a first-PR problem either — PRs happen. Real leak: nothing turns a one-off merged PR into a second one. Fix that stage first, everything else is secondary.

## The journey, stage by stage

0. **Discovery.** They find Thistlewrap via README, blog post, "best Go migration tools" list, or a coworker. Not your contributor funnel yet. Risk: none contributor-related. Skip.

1. **Adoption.** They `go get` it, wire it into a project. Two very different sub-populations from here:
   - Hobby/side-project user. Low stakes, low urgency.
   - Company running it in production. High stakes, real incentive to fix what breaks them.
   Treat these as separate lanes (more on this below).

2. **First friction.** They hit a bug, a missing driver, unclear docs, or a behavior they didn't expect. This is the actual trigger event for contribution — nobody contributes to a project that never annoyed them.
   - Risk: friction resolves by workaround or fork-in-their-head, they never surface it.
   - Fix: make "file an issue" the path of least resistance. Issue template with 3 fields max, no CLA friction, no login-wall docs.

3. **First contact.** They open an issue, or comment on an existing one.
   - Risk: silence. Nothing kills return-intent faster than a question sitting unanswered for weeks.
   - Fix: 48-hour first-response SLA, even if response is just "confirmed, needs investigation." Set this as a real rule for yourself, not aspiration.

4. **Decision to attempt a PR.** They weigh: is this approachable? Will a maintainer actually look at it? Do I understand the codebase enough?
   - Risk: issue looks scary (no context, assumes deep migration-engine knowledge), or looks already claimed/stale.
   - Fix: every issue open to outside contributors gets 2–4 sentences of context + pointer to the exact file/function. Costs you 5 minutes, saves them an hour of spelunking.

5. **PR submitted.**
   - Risk: review takes too long, or feedback reads as harsh/terse in text form (common misread on OSS PRs).
   - Fix: same 48-hour SLA on first review pass. Acknowledge effort explicitly before critique ("Thanks — nice catch on the transaction rollback path. Two small things:").

6. **PR merged. First contribution complete.**
   - Risk: this is treated as the finish line. It is not — it's the only point where you have their attention guaranteed.
   - Fix, do all three, cost is minutes: add them to CONTRIBUTORS/AUTHORS, credit by name in the next release notes, leave a specific (not generic) thank-you on the PR — name what their fix actually improved.

7. **⚠️ The gap — this is where almost everyone leaves.** PR merged, nothing happens next, contributor drifts back to being a silent user. This stage is currently unmanaged. It's the one costing you the most.
   - Root cause: converting a one-time contributor into a repeat one needs a deliberate second ask. It never happens by itself.
   - Fix, concrete and low-effort (you have ~8 of these a year, do it by hand, no tooling needed):
     1. Within a week of merge, reply on the closed PR or DM: one sentence, one specific follow-up issue that touches code they just proved they understand.
     2. Tag that follow-up issue for them by name in the issue body, don't just drop a link in a channel and hope.
     3. Track this in a plain checklist (spreadsheet, or a pinned GitHub issue) — one row per contributor, one column: "second issue offered? Y/N". At this volume a tracker is a 10-minute setup, not a project.

8. **Second contribution.** If stage 7 lands, this either happens or it doesn't within a few weeks. Someone who does two things is a completely different retention curve than someone who did one.
   - Fix: same review SLA, plus start giving them slightly more context/trust than a stranger — mention you'd value their read on a design question, not just a code fix.

9. **Repeat contributor.** 3+ merged PRs. Give real trust, not just thanks:
   - Triage rights (label issues, close duplicates) if GitHub org settings allow.
   - Ask them directly, by name, for review on PRs in their area.
   - Skip building a Discord/Slack for this — at 2 PRs/quarter a community platform is overhead nobody will animate. A direct email or GitHub DM thread does the job at this scale.

10. **Core contributor / co-maintainer.** Sustained contribution over months, trusted judgment. Offer commit access or co-maintainer status explicitly — don't wait for them to ask, most won't.

## Priority order — do these first

1. **Now:** write down the 48-hour response SLA (issues and PRs) somewhere you'll see it. This one rule fixes stage 3 and 5 leaks, which currently poison everything downstream.
2. **This week:** start the plain contributor tracker (stage 7). One row per merged-PR contributor, one action: did you send them a specific second issue.
3. **This week:** for the next 2–3 merged PRs, personally follow up within 7 days with one tailored second issue each.
4. **This month:** relabel issues (see below).
5. **This month:** decide on the adopters lane (see below) and add a short "used in production by" section to the README if you go that route.

## Q1 — the easy/medium/hard labels

Change them. Difficulty labels talk about the code; what a newcomer needs is a label that talks about *them* — do I belong on this issue or not.

- `easy`/`medium`/`hard` is subjective, and `hard` on a public tracker mostly does one thing: signals "don't touch unless you're an expert" — the opposite of an invitation. Worse case: someone picks it up anyway, gets stuck, quietly vanishes. That's a silent burn of your one shot at them, worse than them never trying.
- Replace with intent-based labels, industry standard, and GitHub's own tooling (contributor suggestion widget) keys off these names specifically:
  - `good first issue` — self-contained, low context needed, exactly what it says.
  - `help wanted` — open to outside contributors, no skill-level claim.
  - `mentored` — you'll pair closely; use this instead of putting "hard" fear on something you're actually willing to walk someone through.
- If you still want an internal difficulty signal for your own triage, keep it — but as a maintainer-only label (different color, not mentioned in CONTRIBUTING.md), never surfaced as guidance to newcomers.

## Q2 — does the map need a buyer lane

No buyer lane. There's no purchase step — nothing to price, no funnel to a sale. Don't force a SaaS-shaped lane onto a project that isn't one.

What you do need: split "production adopter" from "casual user" as its own lane, because it's your highest-value contributor source, and right now it's invisible inside a generic "users" bucket.

Why this segment matters more than any buyer ever would:
- Real incidents → real motivation to fix, not hypothetical interest.
- Employer engineering time → capacity to contribute during work hours, not nights/weekends scraps.
- Dependency risk on an MIT project with a small maintainer team → direct interest in the project staying healthy, which is the actual thing you want more of.

Two concrete, cheap moves instead of a buyer lane:

1. Find out who's running it in production — GitHub's "used by" dependency graph, forks that diverge meaningfully, anyone who's filed a detailed production-shaped bug (migration failure under load, rollback edge case). Reach out directly. Not a sales pitch — nothing to sell. Ask if their team would open to a couple small issues, or want to be listed as an adopter.
2. Add a short "Used in production by" section to the README. Zero cost, and it's a two-way incentive: it's a credibility signal for them too (their logo/name next to a 3,800-star project), which makes the ask-back — "mind if your engineers pick up a small issue sometime" — much easier to land.

This gives you an adopters lane that feeds the same contributor funnel above, at stage 1, with people who already have the strongest reason to move through it.