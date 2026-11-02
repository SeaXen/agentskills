## Crestmoor contributing-guide readiness — score: 15/30 (50%, D+)

| Dimension | Score | Signal |
|---|---|---|
| Setup accuracy | 2/5 | ❌ Docs say JDK 17+, repo needs 21 exactly — wrong requirement, not a missing one |
| CI/local parity | 5/5 | ✅ Fork green, commands match — no environment drift |
| Structure & discoverability | 2/5 | ⚠️ Right location (`.github/CONTRIBUTING.md`), but no scope section, CLA absent from it |
| Beginner-issue quality | 3/5 | ⚠️ File path + test command present, no mentor named on either |
| Response-time honesty | 1/5 | ❌ README claims 48h, real 90-day median is 9 days — 4.5x gap |
| Retention loop | 2/5 | ⚠️ Contributors credited in release notes, never pointed to a next issue |

## Ship this week: yes, but not as-is

Three items are trust-breaking and each is a same-day text fix — hold the guide until they land:

1. **JDK requirement.** "17+" fails on anything but 21. A wrong requirement is worse than a missing one — it burns 22 minutes before the contributor even suspects the docs, not the code. Fix: state "JDK 21" exactly, or fix the build if 17+ was the real intent.
2. **Response-time claim.** 9 days vs. a published "48 hours" is discoverable by anyone who reads issue timestamps — first broken promise a new contributor hits. Fix: publish the real median, or commit to a process change that closes the gap before republishing the number.
3. **CLA visibility.** Surfacing it only in the PR template means contributors learn about it after writing code, not before. Fix: add a CLA line to CONTRIBUTING.md itself — this is exactly what the new guide should absorb.

Bake the scope section into the new guide while you're at it — one paragraph on what's accepted, since "no scope section anywhere" is a gap the guide is the natural place to close.

Non-blocking, don't hold the release for these:

- Name a mentor on the two beginner issues — raises conversion, doesn't gate shipping.
- Add a "suggested next issue" line to release-note credits — starting with the next release cycle is fine.

**Bottom line:** the mechanics are solid (CI parity, a real beginner-issue funnel, existing credit practice). The blockers are three false or missing facts in public-facing text, not process rework — fixable in a day, then ship.