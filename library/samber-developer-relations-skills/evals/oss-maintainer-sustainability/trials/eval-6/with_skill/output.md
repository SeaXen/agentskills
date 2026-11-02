**Do first (10 min):** open the RubyGems "Reverse dependencies" page for each of the five small gems. Confirm none is a runtime dependency of `hearthstone-csv` or `quillbind`. The archive step below depends on that check.

Your plan has two problems. Fix both before anything else.

1. **Don't split the 4 hours evenly.** 4h ÷ 7 is 34 min per gem. The five unused gems would take 2h50, which is 71% of your budget. `hearthstone-csv` is 3M downloads a month and carries a transitive-dependency risk. It gets most of the hours. The five get none.
2. **Don't accept $600 as a reason to keep the hours.** You want fewer hours in total, so money for your own hours is the wrong lever. The skill ranks funding last, and it calls "funding first" a failure mode. $600 a month doesn't cut inflow or fix succession, and a fintech in production brings expectations, which is new load. It is still useful, because that fintech is your best co-maintainer lead (see Moves).

Assumed from your message: destination is the same gems with far fewer hours, you aren't employer-paid, and there is no hard date. Not yet known: your top drain, monthly inflow, and who holds publish rights. Numbers marked "self-set" are the skill's baselines, not sourced.

# Sustainability plan: seven Ruby gems, 2026-10-23

## Destination
- `hearthstone-csv` and `quillbind` become maintenance-only, at 4h/week total from Mon 2026-11-23.
- The five small gems are archived.

## Ledger
- **Hours:** 15 now, 4 target. The 4h split is:
  - `hearthstone-csv`: 2h30. This includes mentoring a co-maintainer.
  - `quillbind`: 1h15.
  - 15 min buffer for security reports on those two.
  - The five small gems: 0.
- **Transition hours** (self-set, one-time): about 30h.
  - `hearthstone-csv`: ~20h.
  - `quillbind`: ~8h.
  - The five archives: ~2h30.
  - You run at today's 15h/week for about 4 weeks, then drop to 4h. The bridge ends 2026-11-20.
- **Reply capacity** (self-set formula, half your time on the tracker, 15 min per reply):
  - `hearthstone-csv`: 2.5h × 60 × ½ ÷ 15 = 5 first replies a week, about 21 a month.
  - `quillbind`: about 10 a month.
  - If monthly inflow is above that, cut intake before you publish a window.
- **Shape:** `hearthstone-csv` is a "stadium": many users, few contributors. Contributors won't appear on request, so cut the contract before waiting for help.
- **Publish rights:** unknown. Run `gem owner hearthstone-csv` and `gem owner quillbind`. One name means a stranded package if you leave.
- **Top drain:** unknown. See the question at the end.

## Moves
1. **Archive the five (Mon 2026-10-26 to Fri 10-30, ~2h30).**
   - Reason: tiny user base, so archive now with a same-week notice.
   - Per gem: push a final release with the status in the README, post the announcement, archive the repo.
   - Do not yank. It breaks installs, and every published version should stay installable. Check RubyGems' current docs for a deprecation signal first.
   - Keep your RubyGems and GitHub accounts, with MFA and a recovery contact. Never delete them, because a freed name can be claimed. Revoke CI and personal tokens only.
   - If someone offers to adopt one, don't add them as owner on day one. Use the staged ladder below.
2. **Publish the contract for both big gems (10-26, 1h).** Blocks are in Contract below.
3. **Declare maintenance-only (10-27, one afternoon).**
   - In scope: security fixes, Ruby and Rails compatibility, correctness bugs.
   - Out of scope: new features, with a pointer in the README.
   - This is exactly what "keep it going" means for the fintech.
4. **Cut intake (10-28, one afternoon).** Add issue forms with blank issues off and a repro and version required. Add `SUPPORT.md` and point questions to Discussions. Don't limit PRs yet, since move 7 needs that pipeline.
5. **Automate chores (Nov 2–6, one day).** Grouped Dependabot updates and release from CI. You review what the bots produce.
6. **Backlog reset (announce Nov 9, run Nov 16, one day).**
   - Post a pinned notice a week ahead.
   - Label first, close second.
   - Confirmed bugs stay open.
   - Expect a notification wave and some angry replies. Answer none beyond the reopen rule.
7. **Recruit a co-maintainer (starts Nov 2, months of mentoring).**
   - This is net negative for the first months. It is still the only move that compounds.
   - Promote it early here: a single maintainer on a 3M/month gem is the biggest risk in the portfolio.
   - Candidates, best first:
     1. People who reviewed PRs or answered issues well in the last year.
     2. Maintainers of the two Rails gems that depend on `hearthstone-csv`.
     3. An engineer from the fintech.
   - Ask for a named person and hours, not money. Use the invitation template in the recruitment reference.
   - **Keys go slowly:** triage, then review, then merge after a release made together. Publish rights come last, after a supervised release, never in the same act as merge.
   - Red flags: pressure to speed up, or a newcomer asking for publish rights before review rights. Decline in writing. This is the xz-utils pattern.
8. **Funding (last).** See the fintech reply below.

## Fintech reply
Send it this week, after move 2 so they see the terms. Draft:

> Thanks, that's generous. `hearthstone-csv` is moving to maintenance-only at about 4 hours a week across all my gems: security, compatibility, correctness. Status and scope: <README link>. Sponsorship can't buy priority, SLAs or roadmap. What would help most is an engineer of yours, named, giving ~2 hours a week to triage and review, as a path to co-maintainer. If that's not possible, I'd accept the sponsorship on those terms, and I'd put it toward a co-maintainer's hours once there is one.

- **Cash with no terms:** acceptable. It doesn't justify the hours, and the plan doesn't depend on it.
- **If they want service levels:** that's a support contract, a different deal. Hand it to `oss-sponsors-fundraising` and run it only after moves 1–3.
- **Scale check (my arithmetic):** $600 over your 4h/week (~17h/month) is about $35/hour. Split to a co-maintainer's 2h/week it is about $69/hour.
- **Why donations aren't a salary:** core-js's author reported about $400/month for 250M monthly downloads.

## Contract
`hearthstone-csv`, ready to commit. The window assumes inflow ≤ ~21/month, so check that first.

```markdown
## Project status

**Maintenance-only**

- Maintained by one person in their spare time, about 2.5 hours a week.
- Expect a first reply to issues within 30 days; a reply is not a promise of a fix. Security reports: see SECURITY.md.
- In scope: security fixes, compatibility with new Ruby and Rails releases, correctness bugs. Not in scope: new features.
- Questions go to GitHub Discussions, not the issue tracker.
```

`quillbind`: same block with 1.25 hours a week and a 45-day window. I derived that window from ~10 replies a month. Change "Rails releases" to the Rails versions you actually support.

Archive notice for each of the five (short form, adapted from the stepping-down template):

```markdown
**<gem> is archived as of <date>.** I no longer maintain it. Every published version stays installable and nothing breaks. No further fixes, including security fixes. The license allows anyone to fork and continue. Alternative: <if any>.
```

## People
- Co-maintainer for `hearthstone-csv` first, `quillbind` later or the same person.
- Stages: triage (Nov), review (after ~1 month of good triage), merge (after a release together), publish (after one supervised release).
- Target for a second publish holder on `hearthstone-csv`: about Q1 2027 (my estimate, depends on a candidate).

## Exit
No exit planned for the two big gems. Only the five are ended: archive now, notice the same week, accounts kept.

## Review
- Re-read the ledger on **Mon 2026-12-21**, four weeks after the step-down.
- Earlier trigger: hours over 4 for two straight weeks. The answer is the next move, not more effort.
- Health check, current state:
  - **1. Budget held:** check on the review date.
  - **2. Contract kept:** check on the review date. If you missed the window, widen it publicly.
  - **3. No single key holder, or an end date:** passes for the five. **Open for the two big gems** until a second publish holder exists. Plan not finished until this passes.
  - **4. End state written:** passes once moves 1 and 2 ship.
  - **5. Security path named:** passes once SECURITY.md is in place and the archive notices say "no further security fixes".

## One question
What drains you most? Pick one: issue volume, support questions, PR review, AI-generated issues or PRs, hostile comments, security reports, release chores, or backlog guilt. That answer reorders the first targeted move. For example, hostile comments move moderation ahead of the backlog reset.

**Next:** run the reverse-dependencies check on the five gems, then answer the question above.