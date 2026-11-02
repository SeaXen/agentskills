# Driftwell Bluesky bot: reply template and posting rules

## Direct answer

I can't write the bot you described. It searches for "kafka lag" or "consumer lag", then likes, replies with a link and follows the author. Bluesky treats that as spam, whatever the volume.

- **Automated likes, follows and replies to untagged users are spam.** Bluesky's rules call automated or bulk interactions that notify a user spam. Bots may like, repost or reply only when a user tagged them. [Bluesky]
- **Your 1,666-per-hour figure is a write budget, not permission.** The cap is 5,000 points per hour and 35,000 per day, and a like or follow costs 3 points. That works out to about 1,666 per hour. Bulk interactions count as spam far below that. At 200 a day you would be under the budget but still violating the rules. [Bluesky]
- **There is no published spam threshold, so there is no safe volume.** [Bluesky]
- **Auto-following the author makes it worse.** Scripted follow tools stay near 100–150 a day, and a mass follow pattern gets reported and policed. [practitioner]
- **The likely outcomes are bad for a vendor.** The bot account gets flagged or removed, and block lists and labelers that flag undeclared automation can pick it up. Kafka engineers who get an unprompted vendor reply will mute or block it. The Driftwell name ends up on block lists. [Bluesky] [practitioner]

What you can build instead is below. It gets the same people to the troubleshooting guide, with the bot kept to what the rules allow.

**Assumptions** (I skipped the interview, so tell me if any are wrong):
- Driftwell has no verified Bluesky account yet.
- A named DX person can spend an hour or more a week on it.
- The product is not AI-forward.
- Driftwell controls a domain.

## Verdict: Go

Kafka audiences are on Bluesky, and the plan has a person to run it. Check this before you launch: search the app for Kafka, data-engineering and DevOps feeds and starter packs. Confirm that people in your stack are active there. If they aren't, the verdict flips to Skip.

## What the bot may do

- **Post on a schedule.** Examples: guide updates, release notes, a "common consumer-lag causes" series. [Bluesky]
- **Interact only when a user tags it.** If someone mentions `@lag-help.driftwell.io`, the bot may reply, and it may like that post. [Bluesky]
- **Never** search for keywords and act on strangers' posts. Never auto-follow anyone. Never DM. [Bluesky]
- **Do not collect posts from the firehose** for "insights" or a dataset. Consent is the norm on Bluesky. [press]

## Account setup

| Account | Handle | Display name | Notes |
|---|---|---|---|
| Brand hub | `driftwell.io` | Driftwell | Reposts staff teaching posts and announces releases. |
| Person | `name.driftwell.io` | The DX person's real name | Does the real conversation work. |
| Bot | `lag-help.driftwell.io` | Driftwell lag help (bot) | Own handle, bot label on, 2FA on. |

- Set domain handles with a DNS TXT record on `_atproto` whose value is `did=<account DID>`. [Bluesky]
- Turn on the bot label in account settings. [Bluesky]
- Put "bot" in the display name and bio, and name the human operator. [practitioner]
- Apply for the blue check only after the handle and display name are final. Never promise it. [Bluesky]
- Do not rename an account after it gets the check. [Bluesky]

### Bot profile (draft for the named person to rewrite)

```
Handle: lag-help.driftwell.io
Display name: Driftwell lag help (bot)
Bio: Automated. Posts Kafka consumer-lag tips and replies only when you mention it. Run by @name.driftwell.io, who works at Driftwell (Kafka monitoring).
Settings: bot label on.
```

## Reply template (tagged replies only)

Use this only when a user mentions the bot. It is a draft for the named person to rewrite.

```
Hi, I'm Driftwell's bot (run by @name.driftwell.io, who works at Driftwell, a Kafka monitoring tool). Our consumer-lag troubleshooting guide covers the usual causes (slow consumers, rebalances, partition skew) with the checks for each: [guide link]
```

Variant when the tagged post has no clear question:

```
Bot here (Driftwell, Kafka monitoring). Tell me what the lag looks like, for example one partition or all of them, steady or growing, and I'll point you to the right section of our guide. For a real person, @name.driftwell.io is on here too.
```

Rules for this template:
- Stay under 300 characters, and count the link. [Bluesky]
- The first line always says it is a bot and that it works at Driftwell.
- One link, to the guide. Links get normal visibility on Bluesky, so no tricks are needed. [Bluesky]
- Never reply twice in the same thread unless the user tags the bot again.

## Posting rules

### Scheduled bot posts
1. Post at most a few times a week, on a schedule.
2. Content: one lag cause or fix per post, or a guide update.
3. Add alt text to every image. [practitioner]
4. No hashtag stuffing. Use a feed's tag only on posts that belong in that feed, and only after reading its description or asking its operator. [practitioner]
5. Label any sponsored or affiliate content. [Bluesky]

### Tagged replies
1. Reply only to a direct mention of the bot.
2. Use the template above, edited to the question.
3. Stop replying if the user says "show less", mutes the bot or asks it to stop.
4. Review the bot's tagged replies weekly. Check them for wrong answers and for hostile threads.
5. If a thread turns hostile, stop replying. Hand it to the human operator or let it go.

### Humans
1. The named DX person runs a saved search for "kafka lag" and "consumer lag". This is a listening tool, not a firehose scrape. [Bluesky]
2. They reply to posts where they have something useful to say. Weeks 1–2: no product links unless asked. [practitioner]
3. They add a disclosure line to any reply that mentions Driftwell, for example "(Disclosure: I work at Driftwell, a Kafka monitoring tool.)". [practitioner]
4. They like and follow by hand, as they would anyway. No quota, no script.
5. They never ask staff or a Discord to like or repost posts. The Guidelines ban artificially manipulating social signals. [Bluesky]
6. They never DM people asking for follows or clicks. By default only followed accounts can DM. [Bluesky]

### Account hygiene
- Each person and tool signs in with its own app password, with 2FA on, so access stays revocable. [practitioner]
- Do not squat competitor handles or impersonate other projects. [Bluesky]

## Cadence

1. **Week 0:** domain handles, bios, bot label, pinned post, disclosure line.
2. **Weeks 1–2:** the named person replies daily to Kafka conversations from their saved searches.
3. **Week 3:** ask each relevant community starter pack's curator, in a public reply, to consider one named person. Give a reason the pack's readers gain. Never ask for the whole team.
4. **Week 4 onwards:** a few original posts a week per person, and release posts on the hub. After about a month of replies, build your own pack from community people you now talk with. Ask each first, and announce it once in a post. [practitioner]
5. **Monthly:** check block-list inclusion and labels on your accounts, and drop surfaces that returned nothing.

## Limits that bind

| Limit | Kind | Source |
|---|---|---|
| Automated or bulk interactions that notify users are spam, no published threshold | enforced | [Bluesky] Community Guidelines |
| Bots like, repost or reply only when tagged | enforced (spam flag) | [Bluesky] bot tutorial |
| 5,000 write points per hour, 35,000 per day; a like or follow costs 3 | enforced | [Bluesky] rate-limits doc |
| Follow pacing: no published cap, scripted tools stay near 100–150 a day | policed | [practitioner] |
| Direct messages: followed accounts only by default | enforced | [Bluesky] |
| Feed and pack entry rules | policed | [practitioner] |
| Block lists and labelers can list your accounts | policed | [Bluesky] |
| 300 characters per post, links included | enforced | [Bluesky] |

These limits can change with app releases. I took them from the skill's reference file and did not re-check them against Bluesky's live pages.

## Metrics

Bluesky shows no impression counts, so measure what you can see. [practitioner]
- Replies, reposts and quote posts per post, not likes alone.
- Guide referral sessions with referrer `go.bsky.app`, plus UTM-tagged links, because some clients strip referrers. Compare against a pre-launch baseline. [Bluesky]
- Tagged-reply outcomes: replies, follow-ups and mutes.
- Block lists or labelers that list your accounts. Any increase after a post is a stop signal.
- Never report raw follower totals as the headline.

Do not promise follower growth or virality. Users can opt out of being shown to non-followers in Discover. [Bluesky]

## Notes

- Every template here is a draft. The named person rewrites it in their own voice before posting.
- I did not run the humanizer skill on these drafts.
- The skill covers how a bot account behaves, not how to code it. For the build, use the AT Protocol developer docs.