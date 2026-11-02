# Hacker News plan for a seed-stage database: verdict and cadence

**Verdict:** I'd drop three of the four moves: Launch HN, the company account, and the comment-on-every-competitor plan. Weekly blog submission survives only as an occasional, person-run submission. What replaces them is weeks of useful comments, then one Show HN for the 1.0, posted by a named engineer.

**Next action:** pick the person who will post and check their HN account age and comment history. Everything below depends on that.

## 1. Refusals triggered

| Plan element | Verdict | Why |
|---|---|---|
| Launch HN "like Supabase" | ❌ Not available | Launch HN is YC-only and curated by HN staff [HN]. A non-YC company uses Show HN. Supabase was a YC company, so the precedent doesn't transfer. Your European VC doesn't change this. |
| Submit from the company account | ❌ Refuse | Moderators ask for a person's username, not a brand [HN]. |
| Comment on every competitor Show HN with the comparison link | ❌ Refuse | In a competitor's thread, answer only a direct question, once, disclosed [HN]. An unprompted link on every thread is hijacking. |
| Submit each weekly post | ⚠️ Cut back | Promotion is tolerated "part of the time" [HN]. Repeat submissions from one domain risk invisible site weighting, which only moderators can review [HN]. |

The comparison-link plan has a second problem. A recurring pattern of link-drops reads as a booster pattern. That pushes the account toward flags, and it can drag down your domain for the launch you care about.

**Related rules:**
- **Staff votes:** staff must not upvote or comment to praise the post [HN].
- **Scheduled posting:** any scripted or scheduled submission is banned. "Every week from the company account" drifts into automation [HN].
- **Generated text:** nobody on the team may use AI-drafted or AI-polished text in posts or comments [HN]. I won't draft your text either, and I'm giving shape and examples only.

## 2. Assumptions (I stated one per gap instead of asking)

Tell me where any of these is wrong and I'll redo the plan.

1. **Goal:** a 1.0 launch plus ongoing presence.
2. **Poster:** one DevRel person on a personal account. I don't know its age or history. A new account can't post a Show HN [HN].
3. **Tryable today:** I assume the database runs from a binary or container with no signup, and that the license and pricing are stated plainly. If it's a waitlist, a hosted beta behind signup, or a landing page, it isn't eligible [HN]. Build the no-signup path first.
4. **Staffing:** the DevRel person can stay in the thread for six hours on launch day. Nobody else answers.
5. **Not YC:** a few hours a week are available.

Two questions would change the plan:
- Has the company posted a Show HN before? A new version is allowed only if it's significantly different, once or twice a year, linking the old thread [HN].
- Is the 1.0 a stability milestone or a genuinely different product? "Minor releases" are excluded [HN]. Frame the post around what a reader can try, not around the version number.

## 3. Account readiness verdict

**Not ready until proven otherwise.** HN publishes no karma or age threshold for Show HN [HN], so you can't pre-check eligibility. The only evidence is whether the account can post one. Karma buys no rank [HN].

- **If the account is new or has no comment history:** start the earn-first weeks now.
- **If the author has years of real comments:** skip the earn-first weeks and go straight to launch prep.

## 4. Surfaces ranked for you, and what each moves

| Rank | Surface | What it buys you |
|---|---|---|
| 1 | Substantive comments in database, storage and infra threads you know cold | Compounding account history and the Show HN unlock. This replaces plan 2, in the legitimate form. |
| 2 | **One** Show HN for 1.0 (`/shownew`, then `/show`) | Users, feedback and stars over 24-48 h. This replaces plan 1. |
| 3 | Occasional engineering-post submission | Readers, only if the post teaches something. |
| 4 | Who is hiring post | Only if you're hiring. One per company per month [HN]. |
| 5 | Second-chance pool request | A random front-page slot if the Show HN sank unluckily. |

**How to do plan 2 properly:**
- Comment in threads where your expertise answers the question.
- Mention the product only when it answers the question, and disclose it.
- Set a keyword alert on the HN search API for your product name, so you answer new threads within the hour.
- For competitor threads, reply to a direct question in plain words with the trade-off. Don't send the comparison page unless the asker asks for it. Even then, link it once, disclosed.

**How to do the blog plan properly:**
- Submit only the posts a database engineer would learn from, such as a benchmark method, a postmortem, or an internals deep-dive.
- Use the original title, with no site name and no gratuitous numbers [HN].
- Submit from the person's account.
- Keep own submissions a minority of that account's activity [HN]. If you submit weekly, the share of comments on others' threads stops being the majority.
- Don't ask colleagues to vote or comment on any of them [HN].

## 5. Dated cadence

Today is Fri 2026-10-30. The dates below assume a brand-new account; shorten them if the account has history.

1. **From Mon 2 Nov, weeks -6 to -1:** the posting account comments in its field, with no product links. Add a profile "about" with an email, so moderators can invite reposts [HN].
2. **Week -1 (starts Mon 7 Dec):**
   - Make the no-signup path survive front-page load.
   - Name the license plainly (open source, open core or source-available) and show pricing up front [HN].
   - Send the staff note below.
3. **Launch day (earliest Tue 15 Dec):**
   - Submit when the author can stay six hours.
   - Put the text in the text field. Post it as the first comment only if it doesn't show [HN].
   - Answer the top-ranked questions first.
4. **Days 1-2:** collect emails and stars now. Front-page posts get most of their stars within 48 hours [practitioner].
5. **If it sinks:** use the recovery steps in section 7.

**Holiday risk:** a mid-December launch leaves days 1-2 landing in the holiday run-up. If the team can't stay in the thread, move it to Tue 12 Jan. Timing shifts odds, not outcomes [practitioner], so pick the slot the author can staff.

## 6. Limits that bind

| Surface | Limit | Kind |
|---|---|---|
| Show HN | New accounts blocked "temporarily"; no threshold published | enforced [HN] |
| Show HN | Tryable, non-trivial, your own work; no landing pages, waitlists or minor releases | enforced [HN] |
| Show HN | Title must start with "Show HN" or it never reaches `/show` | enforced [HN] |
| Show HN | New version only if significantly different, once or twice a year, linking the old thread | policed [HN] |
| All posts and comments | No generated or AI-edited text; no automated posting | enforced [HN] |
| Stories | Original title, no site name, no gratuitous numbers | enforced by edits [HN] |
| Launch HN | YC companies only | [HN] |
| Competitor threads | One disclosed mention at most, no hijacking | policed [HN] |
| Weighted domains | Weighting is invisible; only moderators can review it | [HN] |
| Flag and vouch | About 31 karma to flag; vouching works only on `[dead]` posts | enforced [practitioner] |
| Comment edits | About 2 hours; delete only before replies | enforced; numbers [practitioner] |
| Threads | Closed to comments after two weeks | enforced [HN] |

## 7. Conduct on launch day and after a flop

**Launch-day conduct:**
- One person answers per question [HN].
- Disclose in each comment: "I work on X". No HN rule requires it, but undisclosed staff praise reads as a booster comment, which is banned.
- Answer the strongest reading of each criticism. Find something to agree with and never address users by username [HN].
- Never call critics shills or brigaders [HN].
- Never comment about votes or flags in the thread [HN].

**If it sinks:**
1. Check the post logged out and with `showdead` on: is it `[flagged]`, `[dead]`, or simply sinking?
2. If it's sinking with no flag, compare comments to points, and check whether your domain's other submissions die too.
3. For no traction, repost a small number of times, about a week apart [practitioner]. Never repost after it drew real attention, and never delete and resubmit [HN].
4. If it's flagged, dead or weighted, email hn@ycombinator.com once.
5. For a good post with bad timing, ask for the second-chance pool by email.

## 8. Examples to rewrite in your own words

HN bans generated text, so these are fictional-product examples from `references/templates.md`. They show shape and tone only. The staff note is the only finished text, because it never reaches HN.

**Show HN title** (the title starts with "Show HN" and stays under 80 characters):

```
// ✓ Good - names the thing and what it does, no adjectives
Show HN: Litequeue – a job queue that runs inside SQLite

// ✗ Bad - superlative, hype, version bump, site name
Show HN: The fastest job queue ever! v2.1.3 is out | litequeue.dev
```

**Text field shape:** one paragraph each, with no feature list. Cover these in order:
1. Who you are.
2. What it does, said differently from the title.
3. The problem and where you hit it.
4. How it works technically.
5. What's different from tools readers use, named honestly.
6. What it doesn't do yet.
7. How to try it without signup, linking the repo or demo itself.
8. License and how you make money.
9. An open question.

For a database, expect HN to ask about durability guarantees, benchmarks against a named baseline, and what you don't do. The full example is in `references/templates.md`.

**Disclosure in a thread about your product or a competitor:**

```
Disclosure: I work on Litequeue. For the dead-job problem you describe, we
lease jobs with a timeout and requeue them on expiry; the trade-off is a
duplicate run if a slow job outlives its lease, so jobs need to be idempotent.
```

**Reply to a critic** (agree first, answer with a fact, say what changes):

```
You're right that the README oversells the throughput. The 2,000 jobs/s figure
is from a VPS with a local NVMe disk; on network storage I measured about 300.
I'll put both numbers in the README today.
```

**Internal staff note** (finished text, never posted on HN):

> We're posting a Show HN today. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to praise it. HN detects this and can penalize the post, our accounts and our domain. <Author> answers the thread; send technical points to them instead of commenting. If someone is rude, don't reply; tell <Author>.

## 9. Metrics

- **Points and comments** at 1 h and 6 h, against the median Show HN of 2 points. 50+ is the top 6% [practitioner]. Most posts at even the best slot stay under 50 points, so plan on a modest result.
- **Referrals, signups, installs and stars per day** for 7 days, against a baseline captured before posting.
- **Comment share:** the share of the account's activity that is comments on others' threads. Keep it the majority.
- **Competitor-thread behavior:** the number of competitor threads where you answered a direct question. The target is not "every thread".

## 10. Related skills

- `samber/developer-relations-skills@oss-launch` for the cross-channel launch plan.
- `samber/developer-relations-skills@build-in-public` for the ongoing narrative behind repeat Show HNs.
- `samber/developer-platform-skills@github-engagement-playbook` for converting the star spike into watchers and contributors.