**Do not buy ads this quarter. Fix reply coverage first, then spend.**

Say this to the CEO: "Ads add new askers. Today 38 of every 100 new topics get silence, and two people write 80% of the answers. More traffic makes both numbers worse."

## What your numbers say

- **38% unanswered after a week** is a responsiveness failure. Each new asker has a 38% chance of silence. That is the worst first impression, and it is a cost you pay on every ad dollar.
- **80% of answers from two staff** means you run a support queue, not a community. Two people are a single point of failure and a burnout risk. More traffic lands on those same two.
- **3,100 members over 41 categories** is about 75 members per category. Total members only goes up, so it says nothing about health. Many categories are probably dead rooms, and dead rooms hide questions.
- **One month of data is not a baseline.** ℹ️ If last month had fewer than ~30 new topics, report the list of unanswered topics, not a percentage.

## Plan: next 13 weeks

**Weeks 1-2: baseline (about half a day to pull the data)**

1. Export 3+ months. Compute these per category, with bot accounts excluded:
   - new topics per month
   - % with zero replies
   - median time to first human reply
   - share of answers from non-staff
   - distinct non-staff posters per month
2. Find where the 38% sits. I expect it concentrated in a few categories, in off-hours time zones, or in one topic type. The fix depends on which.

**Weeks 2-4: cut and sweep**

3. Merge 41 categories down to about 10-12. Archive empty ones, and redirect the old URLs.
4. Clear the backlog. Answer, merge as duplicates, or close every topic older than 7 days with zero replies. Mark solutions.

**Weeks 3-13: spread the answering load**

5. Run a weekly triage rota that includes product and support engineers, not only DevRel. About 1 hour per day per person. A daily "unanswered" digest goes to the rota.
6. Recruit 10-20 non-staff answerers from your top existing posters. Give them recognition, early access, and a direct line to engineers. Hand-pick them. Do not run a points leaderboard.

**Weeks 6-13: free acquisition**

7. Link the forum from docs pages, error messages, and the support flow. Keep answered threads public and indexable. This is the cheapest traffic, and it brings people who already have a problem.

## Metric sheet (6 metrics, review monthly)

| Metric | Source of target | Action on breach | Owner |
|---|---|---|---|
| % new topics with zero replies at 7 days | Baseline: 38%. Target is self-set after 3 periods. | Rota lead reassigns the unanswered list | DevRel lead |
| Median time to first human reply | Baselining. VMware's two-business-day rule is one company's internal guideline, not a standard. | Add rota coverage for the slow hours | DevRel lead |
| Share of answers from non-staff | Baseline: ~20%. Raising it is a hypothesis, not a benchmark. | Recruit or recognize more answerers | Community owner |
| Distinct non-staff answerers per month | Baselining | Same as above | Community owner |
| Topics per category (bottom 5) | Baselining | Merge or archive | DevRel lead |
| Solved rate | Baselining | Review the unsolved list weekly | Rota |

Set thresholds from your own trailing median once you have 3 periods. Do not copy another community's numbers. Common figures like "24-hour response" are folklore, not published benchmarks.

## When ads become reasonable

Revisit ads only when both hold for two consecutive months:
- zero-reply rate is well below today's 38% (pick the number after the baseline), and
- non-staff answer share is rising, with the two DevRel people no longer carrying most answers.

Then run a capped test. Measure cost per activated poster, meaning someone who posts and gets an answer. Do not measure cost per signup.

## What I don't know

These could change the advice:
1. How many new topics last month. Below ~30, the 38% is noise.
2. Whether "new topics" includes announcements and off-topic posts. If so, the real unanswered rate is higher or lower.
3. How many of the 3,100 members posted in the last 90 days. If it is under about 5%, your problem is activation, not reach.
4. Whether the unanswered topics are mostly unanswerable or duplicate, or real product questions. That decides whether the fix is a rota or a docs change.

**Next action:** run the weeks 1-2 export and bring the per-category table to the exec review.