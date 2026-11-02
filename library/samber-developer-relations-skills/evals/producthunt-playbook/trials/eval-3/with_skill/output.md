# Deployly + deployly-cli on Product Hunt: plan check and dates

## Verdict: ❌ Neither date works (Oct 30 and Nov 3)

Rules below are as last published by Product Hunt. I did not browse to re-check them. The 2-month gap changed within the last year, so confirm it first (see "Check first").

1. **Oct 30 relaunch is blocked twice.**
   - Gap: Oct 30 is 45 days after Sept 15. Product Hunt requires 2 months between launches per product, company or root domain [PH].
   - Update size: dark mode, a new pricing page, a cheaper Hobby tier and the move to `app.deployly.io` do not count as a significant update. "New UI or pricing changes are not significant updates" [PH]. A new app, or a redesign with new functionality, does count [PH].
   - Result: a relaunch of the same build counts as spam [PH]. It would also burn your next slot.
2. **Nov 3 CLI launch is blocked by the gap.** `deployly-cli` shares your company and root domain, and Nov 3 is 49 days after Sept 15 [PH].
3. **Both launches are one slot, not two.** Whichever goes first restarts the 2-month clock for the company and the domain. They cannot sit 4 days apart. Oct 30 is also today, so there was no prep time left anyway.

## Check first

Was Sept 15 featured, meaning on the homepage and not only on the full daily list?

- **Featured (assumed below):** the earliest next launch is Sun Nov 15.
- **Not featured:** you must wait 6 months, until Mar 15, 2027, and resubmit with changes [PH]. Every date below would then move.

## Dates for your calendar

All go-live times are 12:01 AM Pacific. US daylight saving ends Sun Nov 1, so Nov 17 is PST (UTC-8). I assumed Paris time; shift it if your team sits elsewhere.

| Date | Event |
| --- | --- |
| Fri Oct 30 | Cancel the Oct 30 relaunch and the Nov 3 CLI slot. Schedule nothing. |
| Oct 30 – Nov 6 | Posting maker uses a personal account (own name, photo, bio). Comment on launches they actually tried. |
| By Tue Nov 10 | Posting account is at least 1 week old, or has subscribed to the PH newsletter [PH]. |
| Nov 10 – 16 | Build the listing as a draft. Tag all makers. Test the product in production. Name the reply owner for each shift. |
| Sun Nov 15 | Earliest legal date: Sept 15 plus 2 months. Don't use it. |
| Mon Nov 16 | Send the internal team note (no vote asks, no swap groups, no mass DMs). Final check that the listing is scheduled. |
| **Tue Nov 17, 12:01 AM PT (09:01 Paris, 08:01 UTC)** | **Launch.** I picked a Tuesday two days past the gap because the review is judgment-based. Weekdays also draw more traffic [practitioner]. |
| Nov 17 | Maker comment at go-live. Then announce to your own channels and opt-in lists, asking for feedback and never votes. Reply sweeps at least hourly, one named person per shift, from Paris morning to the US afternoon. |
| Nov 18 – 20 | Keep replying. Reach out to people who showed interest. Ask real users for reviews, which PH allows. |
| Nov 24 – Dec 1 | Forum recap thread. Turn feedback into fixes. |
| About Dec 17, then monthly | Forum changelog thread. |
| Sun Jan 17, 2027 | Earliest second launch, 2 months after Nov 17. |
| **Tue Jan 19, 2027** | **Second product's launch**, provided it has a significant update or is a genuinely new product. Jan 18 is a US holiday, so this is the day after. |

You can schedule up to 30 days ahead [PH], so Nov 17 can be scheduled today.

## What goes on Nov 17

Pick one of these:

- **Recommended: launch the CLI, or Deployly with the CLI as new functionality, in one post.**
  - The CLI is the only item that could qualify as a significant update or new product [PH].
  - PH says several products in a short span go in one post [PH].
  - If you are unsure it qualifies, email hello@producthunt.com before building the post.
- **Alternative: launch only the CLI and keep Deployly's relaunch for Jan 19.** Deployly needs a real functionality change by then. Dark mode and pricing won't count.

Fit check on the CLI: if it is open source with a visual demo, Product Hunt is secondary to an engineering aggregator, and you should staff it lightly. For a terminal tool, put an HN launch ahead of PH. See `samber/developer-relations-skills@hackernews-playbook`. For the cross-channel plan, see `samber/developer-relations-skills@oss-launch`.

## Account readiness (assumed)

I assumed one personal maker account with a complete profile.

- Company accounts such as "Deployly" cannot post, vote or comment [PH].
- A domain-named username counts as a company [PH].
- Don't chase a famous hunter. Self-hunt [PH].

## Refusals triggered

- Relaunching or rescheduling the same build to get featured: spam [PH].
- Asking the team, Slack, Discord or your newsletter to upvote, and joining swap groups: drops rank or disqualifies the launch [PH].
- Ads on launch day: not allowed [PH].
- Comment drafts: none received, so nothing to critique. I don't write the maker comment. PH's guideline asks for no LLM comments and labels them "Likely AI" [PH].

## Surfaces, ranked for you

Because your Sept 15 launch gave you followers, forum threads work from day one.

1. Self-hunted launch on Nov 17.
2. Product forum (`/p/<slug>`): a monthly changelog. Every thread notifies all followers [PH].
3. Reviews from real users. They feed the quarterly Orbit Awards [PH].
4. Maker-byline comments on others' launches.
5. Shoutouts.
6. Ads, only after launch day.

## Binding limits

| Rule | Kind |
| --- | --- |
| 2 months between launches per product, company or root domain, plus a significant update | enforced by review [PH] |
| Not featured: resubmit after 6 months with changes | enforced by review [PH] |
| Posting account at least 1 week old, unless it subscribes to the newsletter | enforced [PH] |
| Tagline 60 characters, description 260, up to 3 topics, 2+ gallery images, YouTube only | enforced [PH] |
| No vote requests, incentives or mass DMs | enforced by detection and moderators [PH] |
| No ads on launch day | enforced [PH] |

## Listing fields (draft, confirm against the real product)

```
Name:        deployly-cli                                     (or Deployly)
Tagline:     Create PR preview environments from your terminal   (49 chars)
             Preview environments for every pull request         (43 chars, the Deployly option)
Description: <who it is for, what it does, what is different; 260 chars max>
Topics:      <up to 3, most specific first>
Pricing:     <free | paid | paid with free plan>
Gallery:     <2+ images at 1270x760; first shows the CLI working, a terminal session or before/after>
Makers:      <every builder's PH username>
```

Empty maker-comment skeleton. Fill it in your own words:

1. `<who you are and who built it with you>`
2. `<the problem, where you hit it>`
3. `<what it does, said differently from the tagline>`
4. `<what is different from tools readers already use, named honestly>`
5. `<what it does not do yet>`
6. `<how to try it now>`
7. `<one specific question you want answered>`

Announcement for your own channels (finished text allowed):

> We launched `<Product>` on Product Hunt today. If you try it, we would love your feedback in the comments: `<link>`

## Metrics

- Featured or not, plus rank and points at end of day, read against that day's competition.
- Referral visits, signups or installs per day for 7 days, against your pre-launch baseline.
- Product followers gained, reviews received, and forum thread replies per month.
- Share of launch-day comments answered within an hour.

## Open items for you

1. Was Sept 15 featured? If not, everything moves to Mar 2027.
2. Is `deployly-cli` open source, and does it need a Deployly account? This sets the fit verdict and the HN priority.
3. Which maker account posts, and how old is it?