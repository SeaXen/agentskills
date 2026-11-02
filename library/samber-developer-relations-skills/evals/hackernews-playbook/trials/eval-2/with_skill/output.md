# Acme Observability on Hacker News: plan

**Verdict: don't do the Show HN next Wednesday (2026-11-04). It would fail, and it would use up your one shot.** Nothing I write for that post could fix this. A Show HN needs something readers can try, and you don't have that yet.

Labels: **[HN]** means HN's guidelines, FAQ, Show HN page or moderators say it. **[practitioner]** means a dataset or reverse-engineering. I didn't browse `newsguidelines.html`, `showhn.html` or `showlim` today, so re-read them before you act. The rules move.

I'm assuming no one on the team has a long HN comment history, nobody has agreed to staff the thread, and you're not YC.

## 1. Refusals triggered

| Your plan | Why I refuse it |
|---|---|
| Write the post text for you | Generated and AI-edited text is banned in posts and comments. Moderators ask for "not even a tiny bit" [HN]. I point at problems and show a fictional example, and you write the real text yourself. |
| Post as `acmeobs` | Moderators ask for a person's username, not a brand [HN]. |
| Show HN from a waitlist and a demo video | A landing page or waitlist isn't eligible, and the post must be tryable [HN]. |
| Launch HN | YC-only [HN]. You use Show HN, once you're eligible. |
| Tell the team or the waitlist to upvote or comment | Solicitation penalizes or bans submissions, accounts and sites. Booster comments are "the worst mistake you can make" [HN]. |

## 2. Problems found

- **Nothing is tryable.** The product is invite-only behind signup until December. A waitlist page plus a video fails the "tryable, non-trivial, your own work" test [HN]. Readers also dislike signup walls and unstated pricing [HN].
- **Your goal is backwards.** "Most signups from the waitlist" treats HN as a funnel into a form. HN rewards a link readers can try without signup, and pushing a waitlist from a post gets flagged [HN]. The waitlist can fill after the post, as a side effect. It can't be the post's point.
- **The account is brand-named and a day old.** New accounts are blocked from Show HN "temporarily", and no threshold is published [HN]. A day-old account has no comment history.
- **No one is assigned to the thread.** The author must stay six hours, in a known time zone, on the day.
- **The video doesn't help the post.** It's useful on your site, but it isn't a tryable product.

## 3. Account readiness: not ready

- Move to a personal account, held by the engineer who will answer the thread. Before you rely on `acmeobs`, email hn@ycombinator.com and ask whether a brand-named account is acceptable. I can't confirm how HN treats a day-old brand account.
- Account age and comment history are the Show HN unlock. The cadence below fixes that.

## 4. Surfaces, ranked for you (9 people, not YC, nothing tryable)

1. **Substantive comments in existing threads you know cold** (observability, tracing, on-call, cost). This is compounding, and it builds the history and the Show HN unlock. Mention the product only when it directly answers the question, with disclosure.
2. **Submitting your own engineering posts.** A teaching post from your team works if it's a minority of that account's activity. Your own stuff is tolerated "part of the time" [HN]. This is the one HN route that can bring waitlist traffic before December, as readers who liked the post. Don't link the waitlist as the submission.
3. **Show HN, once there's a no-signup tryable path.** It's one-shot and lasts 24-48 h.
4. **Profile "about" with an email.** This can bring repost invites from moderators [HN].
5. **Second-chance pool**, only if a good post flops. **Launch HN** is not available to you.

Who is hiring only applies if hiring is a goal. Ask HN is not a launch vehicle.

## 5. Dated cadence

Today is Fri 2026-10-30. Target a Show HN around Wed 2026-12-09. It moves with the product, not the other way round.

1. **Mon 2026-11-02 to Fri 2026-12-04 (about 5 weeks):** the personal account comments in its field, with no product links. Keep own-submission activity to a minority of everything it does.
2. **By Fri 2026-12-04:** build the tryable path.
   - A live demo or sandbox with no signup, or a public instance on sample data.
   - It must survive front-page load.
   - Pricing is visible, and the license model is stated plainly (open source, open core, source-available or proprietary).
   - Send staff the internal note below.
3. **Show HN day (target Wed 2026-12-09, or any weekday the author can stay six hours):**
   - Pick the slot you can staff. dang calls `/newest` a lottery [HN].
   - Put the text in the text field. Post it as the first comment only if it doesn't show [HN].
   - Answer the top-ranked questions first, in page order, because comment scores are hidden.
   - Never comment about votes or flags.
4. **Days 1-2:** capture emails and signups with a plain link on the demo itself. Front-page posts get most of their stars within 48 hours [practitioner].
5. **If it flops:** use Diagnose and recover below.
6. **Ongoing:** set a keyword alert on the HN search API for "Acme Observability" and answer new threads within the hour.

**Timing [practitioner]:**
- One dataset finds the best odds near 00:00 UTC and on weekends, and the best mean scores at 12:00-15:00 UTC on weekdays.
- Even at the best slot, about nine in ten posts stay under 50 points.
- Treat timing as a nudge, not a plan. Avoid the post-18 December holiday dip.

## 6. Limits that bind

| Limit | Kind |
|---|---|
| Show HN needs a tryable, non-trivial, own-work product. Landing pages, waitlists and fundraisers are out. | enforced [HN] |
| New accounts are blocked from Show HN, with no published threshold. | enforced [HN] |
| Title must start with "Show HN", or it never reaches `/show`. | enforced [HN] |
| No generated or AI-edited text, and no automated posting. | enforced [HN] |
| Titles keep the original wording: no site name, no gratuitous numbers. | enforced by edits [HN] |
| A new version gets a Show HN only if it is significantly different, once or twice a year, linking the old thread. | policed [HN] |
| Own submissions stay a minority of the account's activity. | policed [HN] |
| Flag and vouch need about 31 karma. Comment downvote needs about 501. | enforced [practitioner] |
| Comments are editable for about 2 hours. Threads close to comments after two weeks. | enforced [HN]; numbers [practitioner] |
| Competitor threads: one disclosed mention at most, no hijacking. | policed [HN] |

## 7. What to do in your thread

- Disclose in the comment: "I work on X." No HN rule requires it, but undisclosed praise reads as a booster comment.
- One person answers per question. Colleagues don't pile in.
- Answer the strongest reading of each criticism and find something to agree with. Never address users by username. You win the silent readers, not the critic.
- Never call critics shills or brigaders. Email hn@ycombinator.com instead.
- Answer criticism of company conduct. Don't ask moderators to remove it.

## 8. Diagnose and recover (if the Show HN dies)

1. Check the post logged out and with `showdead` on. Is it `[flagged]`, `[dead]` or just sinking?
2. If it's sinking without a flag, compare comments to points. Check whether your domain's other submissions die too (site weighting).
3. If it had no traction, repost a small number of times, about a week apart [practitioner]. Never repost after it drew real attention [HN]. Never delete and resubmit.
4. If it's flagged, dead or weighted, email hn@ycombinator.com once. Never ask anyone to vouch, because that is solicitation.
5. If it was a good post at a bad time, email for the second-chance pool.

## 9. Examples to rewrite in your own words

These are for a fictional product. They show shape and tone only, so write yours from scratch about your own work.

**Title.** Shape: `Show HN: <Name> – <what it does, in plain words>`, under 80 characters.
- ✓ `Show HN: Litequeue – a job queue that runs inside SQLite`
- ✗ `Show HN: The fastest job queue ever! v2.1.3 is out | litequeue.dev` (superlative, hype, version bump, site name)

**Text field.** One paragraph each, with no feature list:
1. Who you are.
2. What it does, said differently from the title.
3. The problem and where you hit it.
4. How it works technically.
5. What's different from tools readers use, named honestly.
6. What it doesn't do yet.
7. How to try it with no signup, linking the demo itself.
8. License and how you make money.
9. An open question for readers.

Fictional example opening: "I'm Maya, and I maintain Litequeue, a background job queue that stores jobs in the SQLite file your app already uses." It closes with: "What it doesn't do: no multi-machine workers… The repo has a two-minute quickstart, no signup… I'd like to hear from people running jobs on SQLite in production: what broke first?"

**Reply to a critic.** Say what's right in the criticism, give the fact or measurement that answers it, then say what you'll change or why you won't.
- ✓ "You're right that the README oversells the throughput. The 2,000 jobs/s figure is from a VPS with local NVMe; on network storage I measured about 300. I'll put both in the README today."
- ✗ "@foo123 you clearly didn't read the docs. Are you from <Competitor>?"

**Disclosure.** One mention, only when it answers the question. Example: "Disclosure: I work on Litequeue. For the dead-job problem you describe, we lease jobs with a timeout and requeue on expiry; the trade-off is a duplicate run if a slow job outlives its lease."

**Internal staff note (finished text, never posted on HN):**

> We're posting a Show HN today. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to praise it. HN detects this and can penalize the post, our accounts and our domain. `<Author>` answers the thread; send technical points to them instead of commenting. If someone is rude, don't reply; tell `<Author>`.

## 10. Metrics

- **Post:** points and comments at 1 h and 6 h. The median Show HN gets 2 points, and 50+ is the top 6% [practitioner].
- **Conversion:** referrals, waitlist or demo signups, and stars per day for 7 days. Capture the baseline before you post.
- **Account health:** the share of the account's activity that is comments on others' threads. Keep it the majority.

## Next step

Decide who is the human behind the HN account. They own the comments from Monday and the six-hour thread slot in December. Then tell me the opening date for the no-signup path, and I'll adjust the cadence.