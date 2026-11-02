# PortoBuild Discord: review and posting plan

## Verdict

⚠️ **Don't run the plan as drafted.** The themes are good. The load is not.

- The draft needs weekly prompts, 12 AMAs and many new channels, and it assumes 12 months of hours. You have about 2.5 weeks.
- A dead room costs more than a quiet one. Every unanswered post in a new topic channel tells the next newcomer that nobody is here.
- Your edition ended two weeks ago, so attention is at its peak. Spend your limited hours inside that window.

**Recommendation: a 3-week sprint now, then scheduled autopilot, then a spring relaunch tied to edition 5.**

## What to change in your draft

| Draft | Change | Why |
|---|---|---|
| 12 monthly themes | ✅ Keep them, but each theme becomes **one** pre-scheduled post. | The idea survives at about 5% of the cost. |
| Weekly prompts | ❌ Cut to weekly for 3 weeks, then monthly. | Nobody can write them after October. |
| Monthly live AMA | ❌ Cut. At most one async AMA thread, where the speaker answers over 48h. | Live events need a host, a date and promotion. |
| New topic sub-channels | ❌ Cut to one new channel, `#talk-replays`, and use threads for topics. | Twelve empty channels look abandoned. |
| Themes set by the team | Let members vote for the Jan–Mar themes in the sprint. | Voting generates engagement and removes guessing. |

## Assumptions (tell me if wrong)

- You have edition 4 talk recordings or slides. If not, swap in "your favorite talk" threads.
- You have 2–3 volunteers who can each spare about 1 hour a week until October 31.
- You have a way to schedule posts, such as a bot like Carl-bot or Sapphire, or a webhook on a cron job. I haven't checked which one fits your server.

## Phase 1: sprint, Oct 12–31 (about 6 team-hours total)

**Week 1 (Oct 12–18): reopen**

1. Pin in `#general` (10 min):
   > PortoBuild #4 is done, and this server doesn't go quiet with it. Here's the deal: a few threads between now and the end of October, then one prompt a month through spring, when we start planning #5. Say hi in #introductions: your name, what you build, and one talk from this year you're still thinking about.
2. Open `#talk-replays`. Post one replay per week, with the speaker tagged and one question to the room. Example:
   > 🎬 [Talk title] by @speaker. One thing you'd steal from this for your own stack?

**Week 2 (Oct 19–25): get people to share**

3. Post in `#show-what-you-built`:
   > What did you try at work after PortoBuild? Even "I tried it and it broke" counts.
4. Post replay #2 in `#talk-replays`. Ask three speakers by DM to answer one thread each. This is your only outreach task.

**Week 3 (Oct 26–31): vote and hand off**

5. Post a poll in `#general`:
   > Pick the 3 themes for Jan–Mar. Options: CI/CD, observability, plus whatever else is on your list of 12 (cap at 6 options).
6. Post the expectation reset on Oct 31:
   > We're going to quiet mode: one thread a month. Questions still get answered, maybe in days, because we're all volunteers. #5 planning starts in spring and you'll hear it here first.

Also do two small things now:

- Put "volunteer-run, replies may take a few days" in the channel topics.
- Name two moderators. Their job is 10 minutes a week for spam and Code of Conduct problems.

## Phase 2: autopilot, Nov–Mar (about 15 min per month, scheduled in advance in October)

| Month | Scheduled post |
|---|---|
| Nov | "What did you ship this year that you're proud of?" |
| Dec | One post only: "Post your 2026 stack, one thing you'd keep and one you'd drop." Skip the rest of the month. |
| Jan | **CI/CD month**: one thread, "Your slowest pipeline step and what you'd fix." Add a talk replay if you have a matching one. |
| Feb | **Observability month**: one thread, "What alert woke you up most this year?" |
| Mar | Winner of the member vote (or your next theme), plus the edition 5 teaser. |

Schedule all five in October. Then nobody has to remember anything.

## Phase 3: spring relaunch

- Use the edition 5 announcement, CFP and ticket release as your engagement moments. They need no content calendar.
- Add themes 4–12 only if Phase 2 shows people are replying.

## How to know it worked

Record the baseline now, since you have no history yet, and re-read it at the end of March. Use four numbers from Discord's own insights, with no new tooling.

1. Active posters per month (people who wrote something). Count staff separately.
2. Share of messages from non-team members.
3. Questions with zero replies after 3 days.
4. How many people who posted in October post again in January.

I have no benchmark for a ~1,400-member conference server, so don't adopt a target from elsewhere. Your own numbers are the baseline.

⚠️ **If Phase 2 shows near-zero replies**, the honest fallback is an announcements-only server that reactivates in spring. Don't add more content to fix it.

## Your next action

Pick the 2 moderators and the 3 speakers to DM today. Everything else in Phase 1 can be written from the templates above.