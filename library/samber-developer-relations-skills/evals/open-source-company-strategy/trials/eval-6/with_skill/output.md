**Routing call, per this skill's own scope check:** your question is not "what do we open source" — that line is already drawn (SDK is Apache-2.0, staying that way). It's two sibling problems: **oss-contributor-onboarding** (why zero merged PRs) and **oss-governance** (commit rights, roadmap visibility). Answering with both.

## Diagnosis first

Numbers you gave, read against the funnel:

- 900 stars, 3,000 weekly downloads = "land" step is fine. Awareness is not your problem.
- 0 merged external PRs in 14 months + 19-day median first response = leak is downstream, at **submit** and **survive review** (Steinmacher categories: social interaction, finding a way to start).
- Internal-only roadmap = contributors can't tell what's wanted. That's a "finding a way to start" barrier, not a marketing barrier.
- No external commit rights, never discussed = absence factor is effectively 1 (all authority sits inside the company). Not inherently wrong at this stage, but it means there's no ladder for anyone to climb toward, even in principle.

19 days vs the 48-hour reference point GitHub cites: you're roughly **9x** over. That number alone predicts the zero-merged-PR outcome without needing any other explanation.

## Kill the blog/Discord/podcast plan — not because it's bad, because it's early

Named failure mode in the onboarding skill: **"optimizing recruitment while review is the bottleneck."** Promoting a repo whose review queue takes 19 days doesn't produce contributors, it produces more abandoned PRs and more people who tried once and left annoyed. A blog series today just pours more strangers into the same broken funnel that already lost everyone who found you organically.

Fix order, cheapest damage-removed-per-hour first:

1. **Baseline it.** Pull last 10 external issues/PRs, oldest comment first. Note where each stalled and what (if anything) a maintainer said. This gives you real numbers instead of "19 days median," which hides variance.
2. **Cold-run your own setup.** Fresh machine, no cached anything, follow only what's written. If nothing's written, that's finding #1.
3. **Fix fork CI before anything else.** If your CI needs secrets to run, every fork PR shows red through no fault of the contributor — the single most demoralizing thing a first-timer can see. Split into a credential-free lane that runs on forks.
4. **Stock 3+ real beginner issues.** Each needs: expected behavior, file + test location, required skill, verification command, named mentor. Not "easy" bugs — bugs you understand and a stranger doesn't yet.
5. **Write CONTRIBUTING.md**, one copy, root or `.github/`. Order matters: scope → out-of-scope → non-code ways to help → setup → find-work → pre-PR checklist → what-happens-after → recognition. Publish a response target you can actually hold. "7 days, met" beats "48 hours, missed."
6. **Design the review loop**, specifically the two-clock rule: acknowledge same-day ("seen this, full review by Thursday"), review later. Silence is the expensive failure, not slowness — your 19 days is almost certainly mostly silence, not review time.

Re-score after each round. Threshold: 4/4 blocking checks (invited, setup runs cold, work available, response target held) + 12/16 on the scored checks. Below that, don't ship a CONTRIBUTING file "with a caveat" — iterate.

## The governance gap you're not asking about but should be

"Nobody outside has commit rights, never discussed" plus "roadmap lives internally" is two separate things wearing one sentence:

- **Not discussing external commit rights is fine right now.** You have zero external contributors with a track record — there's nobody to grant anything to yet. Don't build a governance council for a population that doesn't exist. That's the skill's own explicit anti-pattern: buying the expensive model before you have the problem it solves.
- **What you're missing is the staged ladder**, so the first person who does earn trust has somewhere to go: Contributor → Triager (labels, closes, no merge rights — cheap to grant, real signal) → Reviewer (approvals count in one area) → Maintainer. Publish this now, even with zero people on it. It's the difference between "we might let someone in eventually" and a stated path.
- **Roadmap privacy is the more urgent fix of the two.** A contributor who can't see direction can't tell if their PR is wanted before they write it — that's exactly the "answer scope in the first comment" failure, just one step earlier. You don't need to open the internal tracker. A public, even lightweight, "here's what we're prioritizing next / here's explicitly out of scope" note removes most of the ambiguity at near-zero cost and no loss of control.

Skip the rest of oss-governance for now — no fiscal host question, no foundation question, no multi-vendor neutrality problem. Revisit if: a second company's engineers start contributing, or someone external accumulates enough reviews that the ladder above has a real candidate on it.

## Where your three ideas actually land

- **Blog post series** — good tactic, wrong sequence. Once steps 1-6 hold, write posts that document the mechanics (how a PR gets reviewed, a walkthrough of one real beginner issue), not generic thought-leadership. Sequence it after, not before.
- **Discord** — hold off. It adds a channel you now have to staff on top of a review queue you're already not answering in 19 days. If review capacity is fixed later and you still want it, scope it narrow (contributor coordination only, not general support) so it doesn't become a second unanswered inbox.
- **Sponsoring a podcast** — this is a demand-gen/awareness tactic. You don't have an awareness problem (900 stars, 3k weekly downloads prove that). It won't move contributor count; it's solving a funnel stage you've already cleared. Fine as a separate marketing bet, not as a fix for this.

## What to actually track afterward

- New external contributors per quarter
- Second-contribution rate within 90 days (this is the number that says "onboarding," not just "attention")
- Median time to first human response vs. the 48-hour reference point
- External PR merge rate, tracked separately from internal PRs
- Contributor absence factor (currently ~1 — watch it move once the ladder has occupants)

At your current volume these are dated anecdotes, not a dashboard. Don't overread a single quarter.

## This week, in order

1. Pull the last 10 external issues/PRs and log where each one actually stalled.
2. Check whether your CI needs secrets to run on fork PRs — if yes, that's fix #1, ahead of any writing.
3. Draft 3 real beginner issues from bugs you already know, don't invent new ones.
4. Write the CONTRIBUTING file, response-target section first — it's the section every downstream fix depends on being honest.
5. Publish a one-page "what we're prioritizing / what's out of scope" note — doesn't require opening the internal tracker.