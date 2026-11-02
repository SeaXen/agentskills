**Next action (20 min):** open YouTube Studio → Analytics → Reach. Export the traffic-source split and your top 10 videos by views. Everything below depends on those numbers.

## Verdict

"Post more" is the wrong fix. More webinars, talks and release videos gives more of the same zero.

- 140 videos × ~300 views is about 42k lifetime views. That is a small audience, and it mostly watches because it already knows you.
- None of your three formats targets someone with a problem who is searching for a solution.
- Webinars (45–60 min) are long, unstructured recordings. Talks are conference-shaped. Release videos serve existing users.
- Zero signups may also be partly a measurement gap. YouTube often shows up as "direct" or "unknown" in signup data. Check this before you claim zero.

## What to change

1. **Fix the plumbing first (1 day).**
   - Put the link to the page you want viewers on in the first line of every video description. Use a unique UTM per video (`utm_source=youtube&utm_content=<video-slug>`).
   - Add a pinned comment with the same link.
   - Add a "How did you hear about us?" field to signup, with YouTube as an option.
   - Send YouTube traffic to a specific page, such as a quickstart. Don't send it to the homepage.

2. **Change what you make: problem-first tutorials, 8–15 min.**
   - Pick topics from what API platform engineers search for.
   - Examples: "rate limiting per API key in [their stack]", "JWT validation at the gateway", "migrate from [Kong/NGINX] to Quarrystack", "canary a route without downtime", "API gateway vs service mesh".
   - Each video ends on a working result, with a repo and a quickstart link.
   - Put the call to action at the moment of value, spoken and in the description. Don't leave it for the end screen.
   - Check titles against YouTube autocomplete. Put the search phrase first in the title.

3. **Repurpose what you already have (2–4 days for the top 10).**
   - Cut the best webinars into 3–8 min clips, one per question or demo. Retitle each by the problem it solves.
   - Add chapters and a keyword-rich description to every video.
   - Retitle the best conference talks the same way: problem first, event name last.
   - Keep the full webinar as a "watch the full session" link.

4. **Demote release videos.**
   - Keep them short, and write them for existing users.
   - Retitle as "What changed in v4.2 and how to upgrade", and link the migration guide.
   - Don't count them toward the YouTube goal. They won't bring signups.

5. **Structure the channel.**
   - Build playlists by job ("Auth", "Traffic control", "Migration"), not by format.
   - Add end screens that point to the next tutorial in the same playlist.
   - Update the channel trailer and the About section so a new visitor sees who the content is for.

## Set honest expectations

A niche B2B channel will not drive hundreds of signups. Illustrative math (assumptions, not your data): one evergreen tutorial gets 3,000 views in 6 months. 2% click the link, which is 60 visitors. 15% of those sign up, about 9. Ten such videos is around 90 signups a year, plus assisted conversions you can't see directly. Tell leadership that target. Don't promise a flood.

## Reply to your manager

> More volume of the current formats won't change the result. Our content answers questions nobody is searching for. We'll run a 12-week test: 6 problem-first tutorials plus retitled top videos, with tracked links. We decide at week 12 on search impressions, click-throughs and attributed signups.

## Test plan

- **Weeks 1–2:** analytics audit, UTM and signup-field setup, retitle the top 10 existing videos.
- **Weeks 3–10:** one tutorial every ~10 days. Budget about 1.5 person-days each at first; it gets faster after the second.
- **Week 12:** review. Keep going if search-sourced views grow and attributed signups are above zero. If not, cut the channel to a low-maintenance archive and move the time elsewhere.

Success metrics, set before you start:
- Share of views from YouTube search, up from your current baseline.
- Click-through rate to your link.
- Signups with `utm_source=youtube`.
- Self-reported YouTube signups.

## Open question

I can't see your analytics, so I can't confirm the diagnosis. Paste the traffic-source split and your top 10 videos by views here. Then I'll pick the first 6 tutorial topics and retitle the top 10 for you.