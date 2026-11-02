# Contributor path audit — Crestmoor — 2026-09-24

## Verdict

❌ **FAIL** — blocking: 1/4 passed, scored: 6/16 (threshold is 4/4 blocking + ≥12/16)

## Blocking checks

| Check                        | Result | Evidence                                                                                                                                                                    |
| ----------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| B1 Contribution is invited    | ✅ PASS | `.github/CONTRIBUTING.md` exists in a forge-surfaced location, states code + docs are accepted.                                                                             |
| B2 Setup runs cold            | ❌ FAIL | Cold run reached passing tests in 22 min, but only because the runner happened to have JDK 21. Docs say "17+." A contributor on JDK 17 hits a build failure with zero documentation pointing at the real requirement — this is exactly the undocumented-step case the cold-run protocol exists to catch. |
| B3 There is work available    | ❌ FAIL | 2 unclaimed beginner issues. Skill's self-set floor is 3 (published-findings.md §2). Below floor. |
| B4 Submissions get answered   | ❌ FAIL | Published target: 48 hours (README). Actual median over 90 days: 9 days — 4.5x the promise. This is worse than publishing an honest slow number: "B4 cannot be faked... if the honest target is two weeks, say so." A broken published promise is a finding, not a near-pass. |

## Scored checks

| Check                          | Score | Evidence                                                                                       | Fix                                                                                     |
| ------------------------------- | ----- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| S1 Out-of-scope stated          | 0/2   | No scope section anywhere.                                                                       | Add 3-6 line "out of scope" section (outline §2.2).                                       |
| S2 Prerequisites pinned         | 0/2   | JDK version stated in prose only ("17+"), and it's wrong.                                        | Pin exact JDK version in a toolchain/version file (`.java-version`, Maven/Gradle enforcer), not prose. |
| S3 Local gates match CI         | 2/2   | Local commands match CI (stated).                                                                | —                                                                                           |
| S4 Fork CI is useful            | 2/2   | Fork CI is green.                                                                                 | —                                                                                           |
| S5 First issues are complete    | 1/2   | Both issues have file path + test command. Neither has a named mentor.                           | Name a mentor on both; a beginner label without one is "a promise of mentoring" left unkept. |
| S6 Claiming is defined          | 0/2   | No claiming convention or stale-claim expiry mentioned.                                          | Publish claim-by-comment + expiry (e.g. 14 days), apply it retroactively to the 2 open issues. |
| S7 Legal gate pre-announced     | 0/2   | CLA appears only in the PR template — discovered after the code is already written, at the gate itself. | Move it into CONTRIBUTING, in the "before you open a pull request" section (outline §2.6). |
| S8 Credit and next step         | 1/2   | Credited in release notes. No pointer to a next issue.                                           | Add "if you want a second one, #NNN is close to this" to the merge message template.       |

**Total: 6/16**, and irrelevant on its own — the blocking gate fails first.

## Findings by barrier category (Steinmacher et al., 2015)

- **B2 / S2 — documentation → technical hurdles.** The JDK version is wrong in the one place a stranger reads it; the failure only shows up on a machine that trusts the docs.
- **B3 / S5 — finding a way to start, and social interaction.** Not enough entry points, and the ones that exist name no human to ask.
- **B4 — social interaction.** A broken promise on response time is the "one negative experience" GitHub's guide points at — it's silence dressed as a commitment.
- **S1 — finding a way to start.** No scope section means a stranger can't self-filter before spending a week on something you'll decline.
- **S7 — prior knowledge / documentation.** The legal gate surfaces after the investment (code written), not before.

## Fix order (damage removed per hour)

1. **Fix the JDK line** in CONTRIBUTING/README: "17+" → "21, exactly." Minutes. Unblocks B2 outright — the highest-damage, lowest-effort item on this list.
2. **Replace the 48-hour claim** with a number the team can actually hold. This needs one input only you have: real reviewer hours/week. Whatever it is — even "7 days" — publish that, not the aspirational one. A held 7-day promise beats a missed 48-hour one on every dimension this skill scores.
3. **Move the CLA mention** from the PR template into CONTRIBUTING, ahead of the setup section. Copy-paste, reposition. Unblocks S7.
4. **Write the scope section** (3-6 lines, outline §2.2). Unblocks S1.
5. **Name a mentor** on both existing beginner issues, and **open a third** with the same seven-part body (see reference examples) to clear the 3-issue floor. This is the one item that needs a real person's time commitment, not just prose — flag who that is before promising it in writing.
6. **Publish the claiming convention** + stale-claim expiry (S6), apply it to the 2 open issues now.
7. **Pin JDK 21 properly** via toolchain file, not just corrected prose (S2) — the prose fix in step 1 is the stopgap; this is the actual fix.
8. **Add the "next issue" line** to your merge-message template (S8).

## Can you ship this week?

**Not as a finished, passing guide — but yes, conditionally, if you close items 1-6 first.** Two things you asked for are in tension: the deliverable is "ship the new contributing guide," but the skill's own rule is explicit — *"documentation describing a broken setup is worse than no documentation"* and *"below the threshold, iterate rather than shipping with a caveat."* Publishing CONTRIBUTING.md today with the JDK line uncorrected and the 48-hour claim intact doesn't just fail the scorecard, it actively worsens the two failures that are invisible from inside the project: a stranger on JDK 17 gets nothing, and a stranger who reads "48 hours" and waits 9 days gets your worst possible first impression, in writing, from you.

What's actually cheap here: items 1, 3, 4, 6 are prose fixes — under a day combined. Item 5 needs a named mentor, which is a real commitment, not a writing task — decide who that is before publishing, not after someone claims an issue and finds nobody there. Item 2 needs one number from you: what response time can this team actually hold, most weeks, not best weeks. That's the one blocker I can't close for you — everything else on the list is yours to finish this week if you choose to.

One more risk worth naming explicitly, since it's this skill's own named failure mode: **you're about to publish a guide that recruits more people into a review queue currently running at 9 days.** If the response-time fix (#2) doesn't land alongside the guide, the guide makes the worst problem worse, not better — more strangers hitting the same silence. Ship the guide and the response-time fix together, or not at all this week.