Short version: don't build the cron job. Here's why, and what to do instead.

## Name the ask for what it is

A script that commits to a throwaway public repo daily has no purpose other than making the graph look different from your real activity. That's the "fill my contribution graph" request specifically, and it's one of the few things worth refusing outright rather than optimizing:

- **It's cheap to spot.** A single-file, single-line, mechanically-timed commit to a repo disconnected from any real project is the textbook shape of graph-padding. Anyone who knows the counting rules — and the reviewers who actually weigh this signal do — discounts it on sight. Backdating or scripting a commit takes one environment variable; it carries zero evidentiary weight to begin with.
- **It can make things worse, not better.** A blank graph next to "I work at a fintech, everything's private" is a neutral, easily-explained fact. A visible pattern of daily filler commits to a scratch repo, sitting next to that explanation, reads as manufactured evidence — in fintech specifically, that's a worse look than sparse activity, if anyone in an interview loop, a review, or a background check ever notices it.
- **It doesn't fix the actual page.** The graph is a verification surface for people who already suspect something, not a discovery surface. What they actually weight is activity history and work on projects other people use — a decoy repo supplies neither.

## What's actually going on, and the real fixes

Everything you described — private repos, feature branches, squash-merges by a bot — maps directly onto how the graph counts, and two of the three causes are fixable in minutes without faking anything:

1. **Turn on "Include private contributions on my profile."** Settings → Profile. GitHub's own stated position is that this is the more accurate representation of your work, so this isn't a workaround, it's the correct first move for exactly your situation. Given "everything is private repos," this alone probably fills most of the last eight months.
2. **Check who ends up as author on the squash-merge commits landing on main.** The graph only counts commits on the default branch, authored under an email linked to your account (or GitHub's noreply address). If your service bot performs the squash-merge under its own git identity instead of preserving yours (via the Author field or a `Co-authored-by` trailer), your real, merged, shipped work gets zero credit — permanently, not just for eight months. Pull one recent merged PR's resulting commit and run `git log --format='%an <%ae> / %cn <%ce>' -1 <sha>`. If the bot shows up as author, that's a real bug worth fixing at the source (ask whoever owns the bot to preserve original authorship on the squash commit) — a durable fix, unlike a cron job that has to run forever to keep working.
3. **Confirm your commit email is linked.** If you push from a work machine using an email never added to your GitHub account's verified emails, those commits silently never counted, feature branch or not.

Do 1 and 3 today; 2 is the one actually worth digging into, since it's the difference between "my graph doesn't show real work" and "my graph never will, no matter what I do."

## Calibrate what this buys you

Even fixed, don't expect the graph itself to carry much weight — the same discounting that applies to the fake version applies, more mildly, to a merely-decorated real one. The evidence that actually moves a technical reviewer is merged PRs on projects other people use and a coherent story in your profile README/pins, not graph density. If the underlying goal is "look credible when someone checks," that's where five minutes is better spent than on the cron job.