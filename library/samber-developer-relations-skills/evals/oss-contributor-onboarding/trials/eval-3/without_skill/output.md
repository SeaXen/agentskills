**Diagnosis: the friend's fix treats the wrong bottleneck.**

19 good-first-issues, zero movement in 7 months, isn't a *visibility* problem — more labels won't fix it. It's three separate failures stacked on top of each other:

1. **The issues aren't actually scoped.** "Add retry backoff config" and "Improve docs for the supervisor" are feature ideas, not tasks. A newcomer can't start without a maintainer first deciding: linear or exponential backoff? configurable how — opts struct, env var, per-queue? Which supervisor doc, which section, what's missing? Until someone makes that call, it's not a good-first-issue, it's an unscoped feature wearing a label.
2. **Stale claims are actively blocking, not neutral.** A newcomer scanning the list sees "claimed since January" and skips it — even though the claimant vanished 8 months ago. Every unclaimed-but-marked-claimed issue quietly subtracts from the real pool.
3. **Maintainer bandwidth is the actual constraint.** Three people shipping weekly releases have limited slack to review, mentor, and merge a first-time contributor's PR. A bigger labeled queue increases the *appearance* of opportunity without increasing the capacity to shepherd anyone through it. That's how you end up with abandoned PRs and worse, not more contributors.

Adding `help wanted` on top just conflates two different asks (help from anyone vs. onboarding for newcomers) without fixing any of the three problems above.

**What to actually do:**

1. **Free the stale claim now.** Comment on the January one: "No activity in a while — unassigning so someone else can pick it up. Feel free to reclaim if you're still on it." Not hostile, just hygiene. Check the second claim's date; if it's approaching the same staleness, ping for a status update before it rots too.

2. **Cut the 19 down to 3–5 that are actually ready.** For each survivor, a maintainer spends 10 minutes adding: exact file/function to touch, a concrete definition of done, and what tests are expected. If an issue needs a design decision first (backoff strategy, doc scope), that decision is a maintainer task, not a community task — do it yourselves in the time it'd take to explain it to a stranger, or explicitly resolve it in the issue *before* relabeling it good-first-issue.

3. **Close or demote the rest.** Zero engagement across 7 months on a supposedly "easy" task is itself a signal — either nobody wants it or it's not actually easy. A long stale list reads worse to a newcomer than a short curated one: 19 untouched "easy" issues says "this project doesn't really support contributors," while 4 sharp, well-specified ones say the opposite. Quality and freshness convert; quantity doesn't.

4. **Name an owner for first-PR review with a response-time commitment** (e.g., 3 business days) before reopening the funnel. A first-time contributor's PR sitting unreviewed for three weeks is worse than never having attracted them — it burns the one shot at turning them into a repeat contributor. This is the piece the friend's plan skips entirely: more labels without a review SLA just moves the bottleneck downstream.

5. **Re-evaluate after 60 days.** Track claim → PR → merge conversion on the trimmed list. If even the well-scoped ones don't move, the constraint isn't the queue, it's that a 3-person team on a weekly release cadence doesn't have mentoring capacity right now — in which case, stop running a good-first-issue program as an unstaffed side-channel and just knock the small ones out internally.

**Bottom line:** don't widen the funnel (more labels). Narrow it, sharpen the few issues worth keeping, clear the dead claims, and put a named person + response-time behind reviewing whatever comes in. That's what turns a stale backlog into a working pipeline — volume of labels was never the constraint.