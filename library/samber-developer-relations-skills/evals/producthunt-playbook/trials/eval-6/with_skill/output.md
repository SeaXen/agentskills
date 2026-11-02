# Verdict on the agency pitch: don't sign as written

One of four claims holds. The 12:01 AM PT go-live matches Product Hunt's own posting flow. The 500-upvote goal, the launch-day ad and the AI replies are each either not allowed or counterproductive. I couldn't browse, so the rules below are as last published, and the relaunch gap and posting flow have changed within the past year. Labels: **[PH]** means Product Hunt states it. **[practitioner]** means it comes from datasets or reverse-engineering.

## 1. Fit verdict

- **Launch is plausible if Hookstream is hosted or has a downloadable CLI that a visitor can try today without a waitlist.** Product Hunt can then anchor the day.
- **Waitlist or email-signup only:** never featured [PH]. Launch once access is open.
- **Pure backend library or protocol with nothing to see:** skip it. Any post starts the two-month gap for the company and root domain. An unfeatured post waits 6 months [PH].
- **Expectation:** Product Hunt's crowd is makers, founders and product people [practitioner]. For devtools, Hacker News sent 3x or more of the traffic and several times the stars [practitioner]. Expect positioning feedback, followers and a permanent page, not code review.
- **Featuring is the scarce gate:** roughly one launch in ten [practitioner]. A curator decides it, so a vote count can't buy it.

## 2. What to do with each agency claim

| Agency claim | Verdict | Reason |
|---|---|---|
| Launch 12:01 AM PT | ✅ Correct time | Go-live is 12:01 AM Pacific [PH]. |
| Tuesday is the best day | ⚠️ Fine, but not a rule | Weekdays draw more traffic, and weekends need about a third fewer points for a daily #1 [practitioner]. The same traffic means more competition. |
| 500 upvotes in 4 hours | ❌ Reject as a target | Points are not upvotes, and the weights are undisclosed [PH]. Vote thresholds in launch guides have no traceable source [practitioner]. A 500-in-4h target forces vote solicitation, which drops the rank, removes the launch from the homepage or disqualifies it [PH]. |
| "Random order for the first 4 hours" | ⚠️ Unconfirmed | Product Hunt tested a randomized homepage in 2023, and its status since is unconfirmed [PH]. Don't build a plan on it. |
| Product Hunt ad on launch day | ❌ Not possible | Ads cannot run on launch day, and Promoted Products exclude brand-new launches [PH]. Ads come after launch day, as leaderboard and newsletter placement [PH]. Ask what exactly they are selling. |
| AI tool replies to every comment within 5 minutes | ❌ Reject | The commenting guideline asks for "No LLMs", and a public Likely AI badge marks such comments [PH]. The comments are labelled, not removed, but the badge puts that label in front of the curator and community on your launch. |

## 3. Refusals this plan triggers

- **Vote solicitation:** asking the team, Slack, Discord, WhatsApp groups or newsletters to upvote [PH]. You can't reach 500 in 4 hours from a standing start without it.
- **Upvote exchanges, bought votes and paid "top spot" services:** these trigger review and removal. Paid hunter or upvote services "will get you unfeatured" [PH]. Ask the agency how they plan to get the votes. If the answer involves their own network or panel, that is this.
- **Famous hunter:** Product Hunt says hunt it yourself. Hunter followers get no email, and the curator reviews "products - not hunters" [PH].
- **Agency posting for you:** only personal accounts can post, vote and comment [PH]. A company-named or agency-named account cannot, and a domain-named username counts as a company. The maker comment and replies should come from your three people.
- **Reschedule or relaunch the same build:** repeated submissions of the same product count as spam [PH]. A botched launch can't be redone by tweaking and resubmitting.

## 4. Account readiness (assumptions, since you gave no answers)

1. **Visitor can try it today:** Hookstream is hosted, or a CLI with a public relay, and needs no waitlist. If not, wait.
2. **Posting maker:** one of the three, on a personal account with full name, own photo and personal bio.
3. **Account age:** the posting account must be at least one week old, unless it subscribes to Product Hunt's newsletter [PH].
4. **Last launch:** none for the product, company or root domain. If there was one in the past 2 months, you need a significant update (a new app, or a redesign with new functionality). New UI or pricing changes don't count [PH].
5. **Deadline:** none fixed. That favors a compounding presence over a one-off spike.
6. **Coverage:** three people in Berlin, so go-live lands at 9:01 AM local. The problem is the end of the day (see section 6).

## 5. Surfaces for a 3-person team, ranked by value per hour

1. **One self-hunted launch** of a tryable product.
2. **Product forum threads** (`/p/<slug>`). These compound, but they notify only existing followers, so the launch comes first [PH].
3. **Reviews from real users.** Asking users to review is invited, unlike asking for upvotes [PH].
4. **Comments on others' launches** with the maker byline, no self-promotion inside the comment [PH].
5. **Shoutouts** [PH].
6. **Ads**, only after launch day [PH].

Default plan: one self-hunted launch, then a monthly forum changelog. An agency adds nothing to this order that your three people can't do.

## 6. Dated cadence

I assumed Tuesday **24 Nov 2026** as the earliest date that fits a 4-week ramp. Tuesday **1 Dec 2026** also works. The date is your call. Avoid the late-December window.

**Time conversion:** US daylight saving ends Sun 1 Nov 2026. 12:01 AM PT is then **9:01 AM Berlin** (PST vs CET, 9 hours apart). It was 8 hours apart between the EU change on 25 Oct and 1 Nov. In spring 2027 it is 8 hours again from 8 to 28 March.

1. **Weeks -4 to -1 (now to 17 Nov):**
   - The posting maker completes their personal profile and comments on launches they've actually tried.
   - Claim the Product Page if one exists.
   - If the account is under a week old, subscribe to the newsletter.
2. **Week -1:**
   - Build the listing as a draft and tag every maker.
   - Test the product in production.
   - Send the internal team note (section 9).
3. **Schedule:** up to 30 days ahead, for 12:01 AM PT.
4. **Launch day, three named shifts (Berlin time):**
   - **A, 09:00-14:00:** posts the maker comment at go-live and does the hourly reply sweeps.
   - **B, 14:00-19:00:** hourly sweeps.
   - **C, 19:00-00:00, then one last sweep around 02:00 (5 PM PT):** hourly sweeps.
   - Post the announcement to your own channels and opt-in lists, inviting feedback, never votes.
5. **Days 1-3:** keep replying, reach out to people who showed interest, ask real users for reviews.
6. **Weeks 1-2:** post a forum recap thread and turn feedback into fixes.
7. **Ongoing:** a monthly forum changelog. Relaunch only with a significant update, and no sooner than 2 months.

A 5-minute reply SLA across ~17 hours isn't realistic for three people. Hourly sweeps by one named person per shift is the standard to meet.

## 7. Binding limits

| Rule | Kind |
|---|---|
| Personal accounts only post, vote, comment and use forums | enforced [PH] |
| Posting account at least one week old, unless it subscribes to the newsletter | enforced [PH] |
| 2 scheduled hunts per person per day | enforced [PH] |
| Tagline 60 characters, description 260, up to 3 topics, gallery 2+ images, YouTube only, logo needed | enforced [PH] |
| English submissions only | enforced [PH] |
| 2 months between launches per product, company or root domain, plus a significant update | enforced by review [PH] |
| Not featured: resubmit after 6 months with changes | enforced by review [PH] |
| No vote requests, incentives, mass DMs or coordinated pushes | enforced by detection and moderators [PH] |
| No self-promotion inside comments | removed by moderators [PH] |
| AI-written comments allowed but discouraged | labelled Likely AI, not removed [PH] |
| No ads on launch day | enforced [PH] |

## 8. Questions to put to the agency before signing

1. How exactly will you produce 500 votes in 4 hours? Name every channel and every account used.
2. Which account posts, comments and replies? It must be one of our three personal accounts.
3. What is the "Product Hunt ad" and when does it run? Ads can't run on launch day.
4. Remove the 500-vote target, the launch-day ad and the AI replies from the scope. Re-price what's left.
5. Add a clause: no vote solicitation, no vote exchange, no paid-vote services. If the launch is removed or unfeatured because of agency actions, the fee is refunded.
6. What do you do that three people can't do themselves? If the answer is "votes", the work isn't worth paying for.

## 9. Listing fields and skeletons

**Listing draft** (assumes a hosted relay; adjust to the real product):

```
URL:         <direct product link or docs domain>
Name:        Hookstream
Tagline:     Receive webhooks on localhost through a public relay URL
Description: Hookstream is a webhook relay for local development. It gives you a public URL and forwards incoming webhooks to your machine, so you can build and test handlers without deploying.
Topics:      <up to 3, most specific first, e.g. Developer Tools, API, Open Source>
Pricing:     <free | paid | paid with free trial or plan>
Thumbnail:   <square logo, 240x240>
Gallery:     <2+ images, 1270x760; first image shows a terminal session with a webhook arriving locally>
Status:      released
Makers:      <every builder's Product Hunt username>
Promo:       <optional discount, never tied to votes>
```

The tagline is 56 characters. The gallery should show a terminal session or before/after, not a mock dashboard.

**Maker comment skeleton** (go-live; write it yourselves, no LLM):

1. `<who you are and who built it with you>`
2. `<the problem, where you hit it>`
3. `<what it does, said differently from the tagline>`
4. `<what is different from the tools readers already use, named honestly>`
5. `<what it does not do yet>`
6. `<how to try it now; any discount for Product Hunt visitors>`
7. `<one specific question you want answered>`

**Reply skeleton:**

1. `<the part that is right, or the need behind the question>`
2. `<the fact, trade-off or workaround that answers it>`
3. `<what you will change, or why not>`

**Announcement for your own channels** (post where the team is already active, and to opt-in lists; no mass DMs, no cold email, nothing in swap groups):

> We launched Hookstream on Product Hunt today. If you try it, we would love your feedback in the comments: <link>

**Internal team note** (never posted):

> We launch Hookstream on Product Hunt today at 12:01 AM Pacific. Please don't ask anyone to upvote, don't post in upvote groups, and don't mass-message the link. Product Hunt removes those votes and can drop or disqualify the launch. Sharing it on your own social accounts is fine. Only people tagged as makers comment on the launch, so the Maker badge shows who we are; everyone else sends technical points to <name>.

## 10. Metrics to replace "500 upvotes"

- Featured or not. Rank and points at end of day, read against that day's competition, not a folklore threshold.
- Referral visits, signups or installs per day for 7 days, against a pre-launch baseline.
- Product followers gained, reviews received, and forum thread replies per month after launch.
- Share of launch-day comments answered within an hour. Target 90% or more.

## 11. If points drop or the launch isn't featured

- **Not on the homepage:** check the full daily list. It is live but not featured. Fix the cause and resubmit after 6 months.
- **Points dropped mid-day:** filtered votes, not a penalty for a clean launch [PH]. After a vote push, the launch can be unfeatured, so never rally more votes.
- **Comments hidden:** under review. Complete the profile and stop generic or promotional comments.

## 12. Hacker News

Because Hacker News beat Product Hunt on traffic and stars for devtools [practitioner], consider a Show HN for Hookstream in the same week. See `hackernews-playbook` and `oss-launch` for the cross-channel sequence.