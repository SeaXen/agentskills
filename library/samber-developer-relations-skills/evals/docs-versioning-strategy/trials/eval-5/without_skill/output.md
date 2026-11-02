**Policy does not hold.** Keep its intent, but split it by severity. Add a PR template that forces the split.

## Why it fails

- 30 fixes/month × 80% = **24 fixes** touch released behaviour.
- 3 supported released branches (5.x, 4.x, 3.x) → up to **72 branch applications**. The 24 fixes land on 5.x, so the marginal cost is **48 backports** to 4.x and 3.x.
- Capacity is 180 min/month. That gives 180 ÷ 48 = **3.75 min per backport**.
- A backport needs cherry-pick, a conflict check, a preview build, and a review. Realistic cost is about 10 min each. That is about **8 hours/month** against 3.
- "Applies to a supported version" is also vague. Deciding whether a fix applies to 3.x is itself work. Judge it per PR, and the policy gets argued every time.

## Policy to adopt

1. **Land every released-behaviour fix on 5.x first.** That is the current site and the branch most readers use. The fix PR targets `5.x`, so 5.x costs nothing extra.
2. **Forward-merge `5.x` into `main` weekly.** Because 5.3 is all additive, the merge is safe, and "next" never loses a fix. Conflicts happen only where 5.3 edits the same paragraph.
3. **Tier A (must backport):** following the docs as written would cause data loss, a security problem, or an outage. Tier A also covers a wrong default, flag, or API name, and a command or sample that errors or gives a wrong result. Backport to every supported branch where the behaviour is true. Opening these PRs is the author's job.
4. **Tier B (no backport):** typos, wording, clarity, missing detail, link fixes, and added examples. Fix 5.x and `main` only. Older docs stay as they are.
5. **Monthly sweep, capped at 30 min:** triage open `backport-candidate` Tier B items and pull in the few that are cheap and high-traffic. Stop at the cap. Leftovers wait for next month.

## Budget check

Tier A share is my assumption, not your data. Measure it for one month.

| Tier A share of the 24 | Backports (×2 branches) | At 10 min each | Plus sweep and merges (~50 min) |
|---|---|---|---|
| 15% (~4) | 8 | 80 min | ~130 min |
| 25% (~6) | 12 | 120 min | ~170 min |
| 40% (~10) | 20 | 200 min | over budget |

- Tier A of 25% or less fits the 180 min.
- Above 25%, automate the cherry-picks with a backport bot or action. That cuts the cost to review time, about 3–5 min each.
- Track the Tier A count monthly. If it keeps exceeding the budget, your docs have a quality problem upstream. More backport hours will not fix that.

## Decisions to make before you ship it

- **What does "supported" mean for 3.x and 4.x?** If either is security-fix-only, its docs should get Tier A security fixes only. Write the support level next to each version in the policy.
- **Tier A decides by reader harm, not author effort.** Never downgrade a fix to Tier B because the backport is annoying. Write that rule into the policy.
- **Fixes to unreleased 5.3 content** go to `main` only. They never get backported.

## PR template

Save as `.github/pull_request_template.md` in each docs branch. The 3.x and 4.x branches need it only if they accept direct PRs.

```markdown
## What this fixes

<!-- One or two sentences. Link the issue: Fixes #1234 -->

## Which versions does this affect?

Tick every version where the old text is wrong.

- [ ] 5.3 (unreleased, `main` only)
- [ ] 5.x
- [ ] 4.x
- [ ] 3.x

Base branch: `5.x` for any fix to released behaviour. `main` only if it touches 5.3-only content.

## Severity (pick one)

**Tier A: backport required.** Tick if a reader following the old text would:

- [ ] lose data, open a security hole, or cause an outage
- [ ] hit an error or a wrong result from a documented command or code sample
- [ ] set a wrong default, flag, option name, or API name

**Tier B: no backport.** Typos, wording, clarity, missing detail, links, new examples.

- [ ] None of the Tier A boxes apply (Tier B)

## Backports (Tier A only)

For each older version ticked above, add a label. The bot or the author opens the backport PR.

- [ ] `backport-4.x` (confirmed the old text is also wrong on 4.x)
- [ ] `backport-3.x` (confirmed the old text is also wrong on 3.x)

If the behaviour differs on an older version, say how:

<!-- e.g. "flag was named --foo in 3.x" -->

## Tier B candidates

- [ ] Add `backport-candidate` if an older version would clearly benefit (reviewed in the monthly sweep, not guaranteed)

## Checklist

- [ ] Preview build renders the changed page
- [ ] Code samples and commands run as written
```

**Next (about 10 min):** pull the last month's merged docs PRs and count how many would have been Tier A. That replaces my 15–25% assumption with your real number.