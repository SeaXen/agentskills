## Diagnosis first, because your instinct (blog series + Discord + podcast) treats the wrong end of the funnel

900 stars and 3,000 weekly downloads means discovery already works. Nobody who wants this library is failing to find it. Your funnel is:

**Discover → Install → Open issue/PR → Get reviewed → Get merged → Come back**

You have zero drop-off at "discover." You have total drop-off between "open PR" and "get merged" — 14 months, zero external merges, 19-day median first response. A blog series and a podcast sponsorship push more people into the top of a funnel that's already clogged at the bottom. Net effect: more frustrated drive-by contributors, more open PRs rotting, worse median response time, and a public record (open PR threads) of a project that doesn't merge outside work. That's worse than doing nothing.

Fix the mechanics before you spend a dollar or a blog post on awareness.

## What's actually broken — verify these before building anything

You haven't told me (and should check before committing budget):

1. **Has anyone actually opened a PR and been rejected/ghosted, or has literally no one tried?** Different diseases. Ghosted PRs = trust-and-process problem. No PRs at all despite 3K weekly downloads = either nobody knows contribution is welcome, or nobody believes it's worth the effort given a 19-day response time they can see from other issues.
2. **What's the 19 days actually made of?** No triage rotation? One overloaded maintainer? No SLA anyone's accountable to? This determines whether the fix is process (label + rotation) or headcount (you need a second reviewer).
3. **Do you have CONTRIBUTING.md, issue templates, "good first issue" labels?** If not, that alone explains a lot of the silence — people don't know what's wanted or how to start.
4. **Why is the roadmap internal-only — deliberate or default?** If it's default, it's actively suppressing contribution: nobody proposes a PR when they can't tell if it's already planned, already rejected, or off-strategy. Every PR becomes a gamble against an invisible plan.

## 90-day plan

### Phase 1 (weeks 1–2): Make the funnel not actively hostile
- **Commit to a first-response SLA** — 3 business days, publicly stated in CONTRIBUTING.md. Not "we'll try," a number you're accountable to.
- **Add CONTRIBUTING.md, PR/issue templates, and 5–10 real "good first issue" labels.** Pick genuinely small, well-scoped tasks (typo fixes, missing type stubs, a single test) — not "refactor the client."
- **Triage the existing backlog once, publicly.** Close stale issues with an explanation, label the rest, comment on every open external PR within the week even if the comment is "we're reviewing, here's why it's taken this long." Silence is the actual reputational damage, not slowness itself.
- **Publish a *subset* of the roadmap.** You don't need to open the internal tracker — write a `ROADMAP.md` with 5–10 lines: what's planned, what's explicitly out of scope, what's open for proposals. This alone will stop people from wasting effort on PRs you'd never merge, which is a big chunk of why contributors don't come back after a rejection.

### Phase 2 (weeks 2–4): Fix review capacity, not just process
- 19 days usually means one person, not a queue problem. If review capacity is the real constraint, a blog post generating more inbound PRs makes the SLA worse, not better. Get a second trusted reviewer with actual merge rights before you do anything that drives more traffic — even internally, from another team, if you're not ready to extend that to an outside contributor yet.
- Decide, explicitly, on the commit-rights question you've never discussed. You don't have to open it wide. Write down a real bar: e.g., "3 merged PRs + 90 days of good judgment in reviews → triage access; sustained contribution → merge rights on a defined subset of the codebase." A project that structurally can never offer a path past "submit a PR and wait" has a contribution ceiling regardless of how good your funnel is — serious contributors want a growth path, not just an open issue tracker. You can keep the ceiling low. Just stop leaving it undefined; undefined reads as "we will never say yes," which is what your current zero-external-merges track record already signals.

### Phase 3 (month 2, only after Phase 1–2 hold for a few weeks): Narrow, targeted, not broad
- Skip the blog *series*. Write **one** post: "Why we've never merged an external PR, and what we changed." Honest, specific, links to the new CONTRIBUTING.md and the labeled issues. This converts your existing 3K weekly downloaders — people who already use the thing — better than any awareness content aimed at people who don't know you exist yet.
- Skip Discord. At your size, it fragments a small, already-thin community and adds a second surface you have to moderate and monitor on top of an issue tracker you're already 19 days behind on. Turn on **GitHub Discussions** instead — zero new surface to maintain, contributors are already there, and Q&A threads double as documentation. Revisit Discord only if you cross ~50 consistently active non-employee participants and GitHub Discussions is visibly too slow for real-time back-and-forth.
- Skip the podcast sponsorship entirely for this goal. Podcast sponsorship buys awareness/listeners, not contributors, and you don't have an awareness problem. If you want podcast presence, go on one as a guest to talk about the "why we changed our contribution process" story once you have one worth telling — that's earned reach, not paid reach, and it's a contributor-relevant story instead of a generic product pitch.
- Add "good first issue" call-outs to your existing channels (release notes, README badge linking to labeled issues) rather than new content. Cheapest possible surface, reaches people already in your funnel.

### Phase 4 (month 3): Decide if it worked, on the right metrics
Track, weekly:
- Median time to first maintainer response (target: your SLA, not "improving")
- % of opened external PRs that get merged within 30 days
- Number of distinct external contributors with ≥1 merged PR (not total PRs — you want repeat contributors, not one-offs)
- Backlog age of open external PRs

Ignore stars and download count for this initiative — they're already healthy and don't move on anything you're about to do. If you're still at zero merged external PRs after Phase 1–2, the problem isn't discovery or content, it's that review capacity or the commit-rights question is still unresolved — go back and fix that before adding any more top-of-funnel spend.

## Bottom line

Your plan (blog series, Discord, podcast) is a marketing plan for a growth problem you don't have. What you have is a trust-and-throughput problem: nobody merges here, nobody knows what's wanted, and there's no visible path past "open a PR into a void." Fix response time, publish a roadmap sliver, add a second reviewer, and decide the commit-rights question on purpose — then, and only then, spend one honest blog post telling people it changed. That will do more for your merge count than a Discord server and a podcast ad combined.