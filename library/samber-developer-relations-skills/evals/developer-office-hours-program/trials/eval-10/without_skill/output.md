Verdict: keep the call, but change what it's for and how you measure it. As planned, it likely won't clear the 40 issues.

**Next action (30 min):** open 5 of the 40 issues and ask whether a stranger could finish each in one evening. Each needs the file path, the test, a verify command, and a named mentor. If most fail, the issues are the bottleneck, not the lack of a call.

## Problems with the plan

1. **Attendance is a reach metric.** It can only go up, and no decision changes if it moves 20%. Ten viewers who each merge a PR beat 200 who don't.
2. **"Ask us anything" is a passive format.** Newcomers rarely know what to ask. The call lets them leave without picking a task.
3. **The issues probably aren't the real problem.** Issues sit untouched for these reasons, most likely first:
   - They lack a location, a verify command, and a mentor.
   - Setup breaks on a stranger's machine, silently.
   - Past PRs got slow or no replies.
   - Claimed issues are never released.
4. **YouTube recording draws viewers, not contributors.** Recording is cheap and fine as a by-product. Don't let it set the format, because the audience starts performing for the camera.
5. **A public monthly call costs three maintainers real hours.** If it runs on top of a broken path, it floods you with questions and the same drop-off follows.

## Do first (in order)

1. **Cold-run setup.** On a clean machine, run clone → build → tests. Log every snag. Fix before any call, or the call turns into setup support.
2. **Rewrite the queue.** Cut the 40 down to about 10 good ones, each with:
   - observed and expected behavior
   - file and test
   - verify command
   - named mentor
   - a size of about one evening, setup included
3. **Add a claiming rule with expiry.** For example, a claim lapses after 14 days of silence.
4. **Set a first-reply target you can hold.** Use "within 3 days" if that's honest. Missing a stated 48h is worse.

Estimate: 1 to 2 afternoons total. Step 2 is the longest.

## Redesigned office hours

- **Cadence:** monthly, 45 min, one maintainer hosting on rotation (about 1 hr/month each, plus prep).
- **Before the call:** attendees sign up and pick one issue from the curated list.
- **Run of show:**
  - 10 min on one codebase area.
  - 30 min pairing on 2 or 3 of those issues, live.
  - 5 min to claim the next step.
- **After the call:** a follow-up within 48h with a named next issue.
- **Recording:** optional. Publish it as docs, not as the goal.
- **Cheaper alternative:** if your hours are tight, run an async thread with a fixed weekly answer window. Same effect, fewer hours.

## What to measure

Compute these from raw counts, and take the baseline from the last 90 days before the first call.

| Metric | Why |
|---|---|
| Attendees who open a PR within 30 days | The real conversion |
| Second PR from the same person within 90 days | Retention, the point of the exercise |
| Median time to first maintainer reply on outsider PRs | The silent leak |
| Open claimed-and-idle issues | Queue health |

- **Counter-metric:** pair PR count with merge rate, so trivial PRs don't game it.
- **Small numbers:** with under about 30 events a quarter, report the raw list with dates. Don't report percentages.
- **Attendance:** track it as context only. It is not a goal.
- **Caveat:** one study (Mozilla, 2015) found people who started on good-first-bugs were *less* likely to stay long-term. Track retention yourself and don't assume it works.

## Questions that would change my advice

- How many hours per week can the three of you give outsiders, review included?
- How long does a stranger's setup take today, and when did someone last run it from clean?
- What happened to the last three outside PRs: merged, stalled, or ghosted?

Answer those three and I'll draft the issue template and the call outline.