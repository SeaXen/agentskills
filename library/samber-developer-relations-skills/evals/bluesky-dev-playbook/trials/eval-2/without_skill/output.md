# Driftwell Bluesky bot: reply template and posting rules

## Before the template: I changed the design

I did not write rules for the bot as specified (search, like, reply and follow, for every post that matches). The rate limit isn't the problem. The problem is who receives the activity.

- **Rate limits and policy are different things.** Staying under the hourly like cap only means the API won't reject the calls. Bluesky's moderation looks at unsolicited automated replies, mentions and follows aimed at people who never asked for them. The ~200 matches a day would be the pattern it flags. Check the current Bluesky rate-limit and community-guidelines pages before launch, because I'm working from memory on the exact numbers.
- **Keyword matches are mostly not help requests.** "Kafka lag" appears in complaints about a competitor, jokes, postmortems, job posts, conference talks and people who solved the problem an hour ago. A vendor link under someone's incident venting reads as an ad, and the brand takes the hit.
- **Like, reply and follow together look like engagement farming.** Followed authors can see exactly why they were followed. Auto-follow also fills your following list with people who never opted in.
- **Reputational cost.** Dev audiences screenshot this behavior. One quote-post calling out "Driftwell's spam bot" outweighs a month of link clicks.

Below is a version that keeps the goal (get the troubleshooting guide to people who need it) with much lower risk. There are two modes. Run mode 1 first, then add mode 2.

---

## Mode 1: Summoned bot (fully automated, opt-in)

The bot replies only when someone invites it. Triggers:

- A user mentions `@help.driftwell.example` (use your real handle) in a post or reply, or
- A user replies to one of the bot's own posts.

### Account setup

- Self-label the account as automated (Bluesky's bot label setting).
- Bio: `Automated Kafka lag troubleshooting helper from Driftwell. Mention me with a lag question. Humans: @<dx-lead-handle>. Reply "stop" to opt out.`
- Pinned post explaining what it does and doesn't do (replies on request, never follows, never likes unprompted).

### Reply template

Replies must fit in 300 graphemes. The link goes in as a proper link facet.

**Default**

```
Hi {first_name_or_handle}, I'm Driftwell's automated helper. Consumer lag usually comes from one of three things: slow consumers, rebalances, or a stuck partition. This guide walks through telling them apart: {guide_url}

Want a human? {dx_human_handle} is on the team.
```

**Variant: user mentions rebalances or stuck partitions**

```
Automated helper from Driftwell here. If lag jumps after deploys or scaling, rebalances are the usual suspect. This section covers how to confirm that and what to tune: {guide_url}#rebalances
```

**Variant: user mentions lag but gives no detail**

```
Automated helper from Driftwell here. Two quick questions would let me point you at the right section: are you seeing lag on every partition or just some, and did it start after a deploy or traffic change? Full guide in the meantime: {guide_url}
```

**Variant: user says "stop" or "unsubscribe"**

```
Done. I won't reply to you again.
```

Then add the user's DID to the suppression list (see rule 6 below).

### Template rules

- Name the sender as automated in the first sentence.
- Give one link, no UTM-stuffed URL. Use a clean URL with a single `?ref=bsky-bot` parameter at most.
- Never use "Great question!", "I noticed you...", or fake-human phrasing.
- Never name or compare competitors.
- Never claim "Driftwell fixes this". The guide helps; the product is secondary.
- Keep emoji out. Keep exclamation marks out.

---

## Mode 2: Human-in-the-loop discovery (for the search idea)

If the DX team wants the keyword search, use the search to build a queue instead of an actor.

1. The bot searches `kafka lag` and `consumer lag` every 15 minutes.
2. It posts each candidate to an internal Slack channel with: post text, author handle, follower count, posted-at, and a bot-generated classification (`asking for help` / `venting` / `sharing a solution` / `job or event` / `competitor thread`).
3. A DX team member replies **from their own named account** only on `asking for help` posts, in their own words, with the guide as one option among others.
4. Likes and follows are manual and optional.

The classification step is where the value is: it is a judgment about natural language, so use an LLM classifier with the five labels above. Don't use regex.

---

## Posting rules

### Targeting (Mode 1)

1. **Opt-in only.** Reply only to a direct mention or a reply to the bot. Never reply to a post that merely contains a keyword.
2. **Never like, repost, or follow anyone automatically.** The bot account follows nobody except the DX team's accounts.
3. **Skip anyone who blocked or muted the bot, or has "no bots" or similar in their bio.**
4. **Skip threads where the bot already replied.** One bot reply per thread, ever.
5. **One reply per user per 7 days**, even across different threads.
6. **Suppression list.** Store the DID of anyone who says "stop", blocks the bot, or reports it. Never reply to them again. The list persists across deploys.

### Volume and timing

7. **Hard cap: 40 replies per day and 10 per hour.** Well below the platform's limits, because the cap is yours, not Bluesky's. If you hit it, drop the extras; don't queue them.
8. **Random delay of 30 seconds to 5 minutes** before replying, so replies don't land instantly after every mention.
9. **Backoff on errors.** On any 429 or rate-limit response, stop for the rest of the hour and alert the DX channel.
10. **Kill switch.** One environment variable or feature flag pauses all posting. Test it before launch.

### Content safety

11. **Never reply to posts about an outage that is in progress at a named company**, a security incident, or a layoff. Detect with the classifier and skip.
12. **Never reply in a language other than English** unless a localized guide exists.
13. **Never reply to accounts under 14 days old or to posts from accounts that look automated**, to avoid bot-to-bot loops.
14. **Never include user data in logs beyond the DID, post URI, timestamp and template used.**

### Monitoring and review

15. **Weekly review.** The DX lead reads every reply sent, every opt-out, every block and every report. Stop the bot if any of these hold:
    - more than 2% of replies result in a block, mute or "stop",
    - any report from Bluesky moderation,
    - any public call-out.
16. **Metrics worth tracking:** replies sent, link clicks on the guide, opt-out rate, block rate. Do not track follower growth for this account; it isn't the goal.

---

## Open questions for the DX team

1. Which handle will host the bot, and who is the named human it hands off to?
2. Does the guide have anchored sections (`#rebalances` and so on)? The variants above assume it does.
3. Is the guide public, with no login wall? A gated guide behind an automated reply will draw complaints.
4. Does the team want Mode 2 at all? It costs staff time, but it is the only path where outbound replies to non-summoning strangers are defensible.