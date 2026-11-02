**Verdict: skip dashboard. Wrong shape for your case.**

⚠️ Why it fails, ranked:

1. **Capacity kills it.** 4h/month bad-month ceiling. Skill rule: single-digit hours/month deletes open-startup dashboard outright — not "rank low," delete. A weekly-updated 3-metric dashboard (pull data, format, publish, handle replies) eats that budget alone, leaves zero hours to actually ship code — the thing that makes talk credible.
2. **Standing obligation, not project.** Dashboard hardest of any build-in-public practice to stop. Miss one Friday, silence reads as decline. You need a burst before 14 March, not a forever commitment.
3. ℹ️ **"Weekly download counts" not reliably measurable for Go.** No npm-style official download counter for Go modules. pkg.go.dev shows "imported by" count, not downloads. Any download number you publish is third-party-estimated, unverifiable, invites the exact skepticism the skill warns about ("unverifiable numbers draw skepticism, not applause").
4. **Sponsors income backfires with this audience.** Conference room = engineers evaluating job-queue lib for real use — company-adoption reader, not casual browser. Small honest sponsorship number next to established queues (Asynq, Faktory, River) reads as vendor-risk signal, not credibility. Solo-maintainer income also invites unpaid-user entitlement — named cost in the skill.
5. **Wrong disclosure type for goal.** You want a one-time credibility burst for a room of Go engineers. That's proof-of-maintenance work, not an open-startup metrics habit.

✅ **Do instead: release-anchored shipping log.** Cheapest of three practices (link + paragraph, no new artifact), buys exactly what a technical audience checks before adopting a library: proof of active maintenance and reasoning behind decisions. Fits 4h/month with margin.

---

## Build-in-public charter — queuelite

**Goal**
Primary: credibility signal for 14 March Go conference talk. Secondary: adoption confidence (B2B evaluators checking maintenance health before pulling in a job-queue lib).

**Context**
Solo maintainer, full-time job elsewhere. No co-founder, no investor, no customer consent needed. GitHub Sponsors exists but stays out of the public content (see Boundaries).

**Audience**
Mixed: individual Go devs picking a tool for side projects, and engineers who need to justify the pick to a team/approver. Both need same evidence: release cadence, response to issues, reasoning behind decisions. Neither needs revenue.

**Rung**
Release-anchored shipping log (ladder rungs 1-2). Each release gets a short public note: what shipped, why, what's next. Excluded: metrics dashboard, revenue, download counts, contributor-count tracker.

**Stop condition**
N/A for shipping log (publishes only your own completed work — no decline to hide). If you ever add a metric later, write its stop condition before first post, not after.

**Boundaries**
- Never: unpatched vulnerabilities before fix ships, revenue/income figures, roadmap dates for unshipped work (Osborne effect — announcing dates suppresses use of what already exists and costs credibility when missed).
- Grey zone, decided now: talk content stays to what's built and decided, not promised.
- Pre-publish check per post: does this reveal a security gap, name someone without consent, promise an unshipped date, or expose income? Any yes → rewrite or delay.

**Cadence**
One post per real release, sized to whatever actually ships — not a manufactured weekly slot. Budget 30-45 min per post (repurpose CHANGELOG entry into 3-5 sentences: what shipped, why, what's next). At 4h bad-month floor, that's room for 5-6 posts/month if needed, but tie frequency to real releases, not a calendar. Between now (18 Sept) and 14 March: ~6 months runway. Even one release-post per month gets you 6 posts of proof-of-life before the talk — comfortably inside worst-case budget.

Stretch, not committed: one decisions-and-failures essay (architecture choice, a bug postmortem, a rejected design) if a real one exists — highest trust-per-word of any practice, good conference-talk material, costs a day whenever you have one.

**Surfaces**
Anchor: GitHub Releases page (already exists as changelog infra — zero new setup). Amplifier: one channel you already read (r/golang, Gophers Slack, or X/LinkedIn — pick whichever you actually check, don't run two). Post links back to the Release, never duplicates content.

**Support plan**
State response-time expectations in README once. Route feature requests to GitHub issues, not DMs, so each answer becomes reusable public record — extra credibility for free.

**Measurement**
Signal that works: last shipping-log post lands within 2 weeks of the talk (freshness a room can check live). Secondary: contributor count via GitHub's own contributors graph — real signal, don't dashboard it, just glance before the talk. Ignore: stars, followers.

**Pause rule**
If a month gets missed, one sentence on the next post: "Slower month — day job. Back to normal cadence now." Announced gaps cost nothing; unannounced ones read as abandonment right before a talk is the worst possible time for that.

---

**Next action, now, under 2 minutes:** open `CHANGELOG.md`, copy the most recent entry. That's post #1's raw material.