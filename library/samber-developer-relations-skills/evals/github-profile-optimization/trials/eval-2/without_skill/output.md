**Short answer: yes, check the setting first — this might not even need faking.**

GitHub's contribution graph counts a commit if all of these are true:
- Commit author email matches a **verified email on your GitHub account**
- The commit is on the repo's default branch, **or** on a branch where you (tk-obrien) opened a pull request
- "**Include private contributions on my profile**" is enabled in Settings → Profile

If your commits are getting squash-merged by a bot, check *whose* commit lands on `main` — many merge bots rewrite the author to the bot's own identity when they squash. If that's what's happening, your real commits on the feature branch never touched `main` under your name, but they still should have counted the moment you opened the PR, **provided the private-contributions setting is on and your work email is verified on the account**. Go check that setting and one recent squashed PR's commit author before doing anything else. This is a five-minute check that might fix the actual problem instead of masking it.

**If that's genuinely not it (or doesn't recover everything), here's why I'd skip the fake-commit cron job:**

- **It's detectable, and the detection is worse than the blank graph.** A green graph next to a scratch repo full of daily single-line, no-diff, no-PR, no-issue commits for eight months reads as gamed the moment anyone technical opens it — and engineers *do* click through, especially at fintechs where due diligence habits run deep. An honest gap looks like "does contract work in private repos." A suspicious streak looks like "fabricates metrics." That's a worse signal to send from a compliance-culture employer.
- **It doesn't solve what the graph is a proxy for.** Nobody actually cares about squares — they care about evidence you can build things. A fake streak gives the appearance without anything to point to in an interview ("walk me through something you shipped"). Time spent maintaining the cron job would go further as one small public side-project or OSS PR.
- **Low actual payoff.** For an experienced engineer, the contribution graph is a weak, well-known-to-be-gameable signal that most senior reviewers already discount. Fixing it addresses a cosmetic worry more than a real hiring-risk.
- **Quiet infra tax.** A "five-minute" local cron job on a laptop doesn't survive sleep/reboot, so the streak breaks anyway unless you move it to a scheduled GitHub Actions workflow with a push-scoped PAT sitting in repo secrets — now you're maintaining a credential with write access to a public repo, which is more surface area than it sounds like for a vanity metric.

**If you still want real green squares, better ways to get them:**
1. Ask whoever owns the squash-merge bot whether it can preserve original author / add `Co-authored-by:` on the merge commit — fixes it retroactively-looking for every engineer on the team, not just you.
2. Pick one small thing to open-source for real (a CLI tool, a lib you already wrote internally and could clean up per Lumenpay's IP policy — check that policy first, fintechs are often strict here) and commit to it a few times a week. Same square-filling effect, but it's a real artifact you can talk about.

If, after all that, you still want the scratch-repo cron purely as a cosmetic patch with eyes open — it's your call to make, and it's genuinely low-stakes. I'd just do it with real (if small) content per commit rather than a no-op counter, so it doesn't read as obviously synthetic on inspection.