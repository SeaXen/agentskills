# Bluesky platform facts

Numbers and mechanics that change with app releases. Re-check each against Bluesky's own pages (bsky.social blog, docs.bsky.app, the @bsky.app account) before quoting it.

## Contents

- Limits, per surface
- Feeds and discovery
- Identity and verification
- Starter pack research
- Moderation, labelers and lists
- Post format

## Limits, per surface

"Enforced" = Bluesky's systems or moderators act on it. "Policed" = the feed operator, pack curator or community acts on it without a published rule.

| Surface                         | Limit                                                                                                                                                                                          | Kind                                  | Source                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------- |
| Any account                     | 5,000 write points per hour, 35,000 per day; create 3, update 2, delete 1 (about 1,666 likes or follows per hour)                                                                              | enforced                              | [Bluesky] rate-limits doc                            |
| Any account                     | Automated or bulk interactions that notify users (follow, like, reply, message) are spam; the Community Guidelines ban spam with no published threshold                                        | enforced                              | [Bluesky] Developer Guidelines, Community Guidelines |
| Any account                     | No artificial manipulation of likes, reposts, follower counts; no undisclosed ads or sponsored posts                                                                                           | enforced                              | [Bluesky] Community Guidelines                       |
| Any account                     | No impersonating brands, handle-squatting, identity churning, selling or sharing accounts                                                                                                      | enforced                              | [Bluesky] Community Guidelines                       |
| Any account                     | Handle changes: 10 per 5 minutes, 50 per day; sign-ins 30 per 5 minutes, 300 per day                                                                                                           | enforced                              | [Bluesky] rate-limits doc                            |
| Follow pacing                   | No published daily cap; human median around 4 follows a day in one 58k-follow sample; scripted tools stay near 100-150 a day; burst unfollows read as churn                                    | policed                               | [practitioner]                                       |
| Bot accounts                    | Scheduled posting welcome; like, repost or reply only when a user tagged the bot; self-label as bot (bot label in account settings; voluntary)                                                 | enforced (spam flag)                  | [Bluesky] atproto bot tutorial, v1.119               |
| Bluesky Discover                | Users can opt their own posts out of non-follower exposure; "show less" and private dislikes shape each reader's view                                                                          | enforced by ranking                   | [Bluesky]                                            |
| Keyword or hashtag custom feeds | Small feeds often state their entry rule (keyword, tag, emoji, regex); large ones often do not; the operator can exclude accounts or terms                                                     | policed                               | [practitioner] feed descriptions                     |
| Curated or member-list feeds    | Only accounts the operator adds; ask, do not tag-spam                                                                                                                                          | policed                               | [practitioner] feed descriptions                     |
| Starter packs                   | 150 people, 3 custom feeds; curator chooses; blocking the creator removes you; packs are reportable; searchable in app search; creator notified only when a new user signs up through the pack | enforced (size), policed (who)        | [Bluesky] starter packs blog, v1.132                 |
| Direct messages                 | By default only accounts a user follows can DM them; users who open DMs to everyone get strangers' messages in a request inbox                                                                 | enforced                              | [Bluesky] v1.99                                      |
| Replies on others' posts        | The poster may restrict replies (followers, mentioned, nobody) and detach quote posts                                                                                                          | enforced                              | [Bluesky]                                            |
| Mod and block lists             | Anyone publishes one; subscribers block or mute all members; misuse of lists is harassment                                                                                                     | policed (inclusion), enforced (abuse) | [Bluesky] Community Guidelines                       |
| Labelers                        | Independent services label accounts and posts; several flag undeclared automation                                                                                                              | policed                               | [Bluesky] stackable moderation blog; [practitioner]  |
| Third-party schedulers          | Their own posting caps (one lists 100 posts per 24 hours); never a Bluesky rule                                                                                                                | tool limit                            | [practitioner]                                       |

## Feeds and discovery

- Following: reverse-chronological from accounts followed [Bluesky].
- Discover: Bluesky's personalized feed mixing trending posts, followed accounts and accounts near the reader's social graph; "show more / show less like this"; private, non-global dislikes; social-proximity reply ranking; toxicity down-ranking in threads, search, notifications [Bluesky].
- Custom feeds: anyone builds them; users pin them as tabs; operators get like, repost, reply, quote and seen events, so some feeds rank on engagement [Bluesky].
- Developer feeds by likes (counts move; check live): Python Programming about 740, Developers about 660, Indie Dev about 340, Rustlang about 320, golang about 140, DevOps/SecOps/Cloud about 130, #opensource about 60. Many language feeds have single-digit likes. Search the app for your stack's feeds and read each description; when it names no rule, watch the feed or ask the operator.
- Trending topics: detection method unpublished; mostly general news; users can hide it and mute words apply [Bluesky].
- Links: "they will receive the same visibility as your other posts" and Bluesky does not downrank them, per @bsky.app and its CEO [Bluesky]. Analytics referrer: `go.bsky.app` [Bluesky].
- Engagement versus X: a Bluesky staffer reported about 10x engagement rate on identical posts for one account; one sample [practitioner].

## Identity and verification

- Domain handle: TXT record `_atproto.<domain>` with value `did=<the account's DID>`, or `https://<handle>/.well-known/atproto-did` returning the DID as plain text with HTTP 200 [Bluesky].
- Subdomain handles for staff (`name.company.com`); the well-known route scales better than one TXT record per person but needs an HTTPS server answering on each subdomain [Bluesky].
- Switching to a domain reserves the old `.bsky.social` name; old mentions keep resolving; followers stay because identity is the DID [Bluesky].
- Handles revalidate periodically; an expired domain or moved well-known file invalidates the handle [Bluesky].
- Blue check: Bluesky verifies notable, authentic accounts and accepts applications; trusted verifiers (scalloped badge) verify their own people [Bluesky].
- A verification is valid only while handle and display name match the values at issue time; moving to a domain handle counts as a change [Bluesky protocol spec; practitioner reports].

## Starter pack research

Balduf et al., "Bootstrapping Social Networks: Lessons from Bluesky Starter Packs", ICWSM 2025 (arXiv:2501.11605), 25M users, 335k packs [research]:

- Up to 43% of daily follow operations at peak.
- Members: up to 85% more new followers and 70% more likes than matched non-members, rising over four weeks.
- Creators who list themselves: up to 117% more new followers; creators who leave themselves out: about 22%. The benefit largely comes from inclusion.
- The study also found creators asking for money to include members, and complaints from people added without consent.
- Caveats: rich-get-richer effect; few users are in any pack; the matching method may overstate lift. A follow-up study (arXiv:2608.17489) finds packs mostly mirror existing dense communities.

## Moderation, labelers and lists

- Users stack labelers on top of Bluesky's default moderation [Bluesky].
- Block counts are public through third-party trackers [practitioner].
- AI backlash incidents: a one-million-post Bluesky dataset on Hugging Face (November 2024) was removed within a day with an apology over consent [press]; Bluesky's own AI assistant account passed 125,000 blocks within days of its March 2026 launch [press].

## Post format

- 300 characters (graphemes) per post; hashtags count, and links are shortened in the composer [Bluesky].
- Up to 10 photos per post, or one video up to 10 minutes and 300 MB; no mixing [Bluesky].
- Article link cards for blogs and newsletters; pinned post; profile links; a temporary LIVE badge linking a stream [Bluesky].
- Long-form: blogging apps built on the same network (Leaflet, pckt, offprint) publish posts that Bluesky shows as rich cards [Bluesky].
