# Pgwatch Cloud: Product Hunt launch day, Tuesday 2026-11-03

## Three changes to your plan first

Product Hunt (PH) bans vote manipulation. It removes the votes, demotes the launch, and can ban accounts. I changed three tactics so the plan doesn't risk that.

| Your idea | Problem | Replacement |
|---|---|---|
| $500 "top 10 hunter" | Paid votes or paid promotion break PH rules. A hunter's followers add little now, so it's poor value either way. | Self-hunt, or ask a free hunter who really runs Postgres. Spend the $500 on a 60-second demo video. |
| Upvote swaps in the 300-founder WhatsApp group | This is a classic vote ring. PH detects reciprocal clusters of low-history accounts and discounts or removes them. A flagged launch is hard to recover. | Ask the group for feedback from people who run Postgres in production. Real comments count and are safe. |
| "Please upvote us, every vote counts" email | PH explicitly discourages upvote asks, and a mass ask brings in drive-by accounts that get discounted. | Email 4,200 people with "we launched, try it, tell us what you think." The links are the same and the rules are not at risk. |

**Assumptions:** The times below are Pacific, because PH resets at 12:01 AM PT (09:01 CET in Nantes). You said "6am" for the newsletter. If you meant 6am CET, that is before launch, so the link would be dead. I've put it at 6am PT (15:00 CET). Shift it if you prefer.

## Monday 11-02: prep (about 3h)

1. Finish the listing: tagline, 5 gallery images, 60-second demo video, and a first comment (the maker story, why Postgres query observability, free tier vs $49 team plan).
2. Run a stranger-test of signup → connect first database → first slow-query insight. Fix anything that takes more than 5 minutes.
3. Load-test signup and the dashboard. Check rate limits and the status page.
4. Write the newsletter draft and the social posts. Schedule the PH page for 12:01 AM.
5. Pick 15 to 30 Postgres people you know personally. Message each by name tomorrow, not in bulk.
6. Set up UTM links per channel, so you can measure signups by source.

## Launch day (PT, CET in brackets)

| Time | Action | Owner |
|---|---|---|
| 12:01 AM (09:01) | Listing goes live. Post the maker first comment right away. | Founder |
| 12:15 (09:15) | Post on X and LinkedIn: what it is, the free tier, a link. Wording: "we're live on Product Hunt, would love your feedback." | Founder |
| 1:00 (10:00) | Send the 1:1 personal messages to your Postgres contacts. Ask for honest feedback or questions, not for votes. | Whole team |
| 2:00–5:00 (11:00–14:00) | Reply to every comment within 30 minutes. Answer with specifics, such as a real slow-query example. | Founder |
| 5:00 (14:00) | Post in the WhatsApp group: "Launched today. If you run Postgres, I'd love your blunt feedback." Say nothing about votes. | Growth lead |
| 6:00 AM (15:00) | **Send the newsletter.** Subject: "Pgwatch Cloud is live: try the free tier." Body: what's new, a 3-line pitch, a link to the PH page and a link to signup. Ask for comments and feedback. | Growth lead |
| 7:00–9:00 (16:00–18:00) | Post in r/PostgreSQL and relevant Slack or Discord communities only where self-posts are allowed. Lead with a useful write-up, not an ad. | Founder |
| 9:00–11:00 (18:00–20:00) | Keep answering comments. Convert useful ones into docs fixes or issues. | Founder |
| 11:00 (20:00) | Check signups, activation and support tickets. Fix the top friction point. | Eng |
| 1:00 PM (22:00) | Post a mid-day update on X: a real number or a lesson, not "we're #3!" | Founder |
| 3:00–6:00 PM (00:00–03:00) | Hand over to the US-timezone person if there is one. Keep replying to comments. | Rotating |
| 9:00 PM (06:00) | Post a thank-you and a transparent recap. | Founder |
| 11:59 PM (08:59) | Launch day closes. | n/a |

## What to measure

- **Primary:** signups, then activation (a database connected and a first insight seen).
- **Secondary:** free-to-team conversions, and comment quality. Rank is only a vanity metric.
- **Post-launch follow-up (Wednesday–Friday):**
  - Email everyone who signed up with a short onboarding message.
  - Personally thank commenters.
  - Write the "what we learned" post.

If you want, I can draft the first comment, the newsletter email and the 1:1 message template next.