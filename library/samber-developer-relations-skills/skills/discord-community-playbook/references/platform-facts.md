# Discord platform facts

Contents:

1. Server types and Discovery
2. Server Web Pages and Web Presence
3. Community setup and newcomer flow
4. Channel types
5. Caps
6. Server Insights
7. Badges, boosts and identity
8. Policy: spam and inflation
9. Per-server promotion rules
10. Searchability cases
11. Sources

All entries labelled **[Discord]** come from support.discord.com articles, discord.com/guidelines, the Platform Manipulation Policy Explainer, or discord.com/community guides. When support.discord.com pages refuse automated reads, the same articles answer through the Help Center API: `https://support.discord.com/api/v2/help_center/en-us/articles/<id>.json`.

## 1. Server types and Discovery

- Friend Server: invite-only, no community tools. Community Server: invite-only, unlocks Insights, Raid Protection, Rules Screening, Onboarding, announcement and forum channels; its invite links never expire. Discoverable Server: a Community Server listed in Server Discovery, discord.com/servers and web search; anyone joins without an invite [Discord, 14078261239831].
- Discovery requirements: 1,000+ members; 8+ weeks old; "certain activity requirements" (no numbers published; older third-party figures of ~10% retention, 20 weekly communicators and 40 weekly visitors are unconfirmed); name, description and channel names within the Discovery Guidelines; 2FA required for moderation. Criteria can change and must keep being met [Discord, 360030843331].
- Discovery Guidelines: Community Guidelines and ToS; healthy environment; no graphic or sexual content, audience 13+; accurate, profanity-free name and description; respect IP; a moderator team; off-platform behaviour may count [Discord, 4409308485271].
- The Discover tab is experimental and reaches only a share of users; it sorts each category "in order of popularity based on the server's member count"; the retired Server Discovery experiment described its search as not personalized [Discord, 25323248535319, 360023968311].
- Turning off Discoverable reverts to Community and takes the Server Web Page down; search engines may keep results for a while [Discord].

## 2. Server Web Pages and Web Presence

Date-bound: verify against articles 4673515000983, 44049845164823 and 44302319454359 before quoting.

- From 2026-11-16 every Discoverable Server has a public Server Web Page, indexable by search engines, auto-generated from the Server Profile when admins publish none. It is mandatory while Discoverable [Discord].
- Channel Summaries on the web: AI-generated summaries of active public-channel conversations from 2026-11-16 onward, no usernames; admins choose channels, curate or turn off; Discord warns summaries "may not always be accurate" [Discord].
- Channel Messages on the web: from mid-December 2026, members' answers in public channels can appear in web search in their own words, text only, no usernames or avatars [Discord].
- Both are on by default for public channels. Private and role-restricted channels, private threads and private forums never appear; public threads and forum posts do when the parent channel is eligible [Discord].
- Who controls what: Channel Summaries follow admin settings; Discord's help articles describe no member control over them. Channel Messages follow admin settings **and** each member's account-wide setting (User Settings > Data & Privacy): default on in most regions, default **off** in the EU/EEA, UK, Canada, Brazil, Australia and South Korea; teen accounts never appear. Turning the member setting off is not retroactive: delete a message to remove it [Discord].
- Turning a feature off stops new content; published content can remain, and search engines keep cached copies [Discord].
- Planning consequence: a vendor server under 1,000 members stays invisible to search. A Discoverable one with a mostly European audience still gets AI summaries of its public channels, but individual answers only from members who opted in. Keep a separate indexed home for answers that must be found for years, and keep pasted secrets out of public channels: they can reach web pages and search caches.

## 3. Community setup and newcomer flow

- Enabling Community requires: verified-email verification level, explicit-media filter on all members, a rules channel, a moderator-only Community Updates channel, compliance with the Community Guidelines [Discord, 360047132851].
- Verification levels: Low (verified email), Medium (+5 minutes since email verification), High (+10 minutes in the server), Highest (+verified phone). A verified phone bypasses all [Discord, 216679607].
- Rules Screening: up to 16 rules; pending members cannot talk, react or DM; Discord notes bot role-gates do not stop DMs and the step can cut joiners [Discord, 1500000466882].
- Onboarding: default channels plus customization questions that grant channels and roles; publishing needs 7 default channels, 5 open to @everyone to view and send; rejoining members go through it again; Discord advises removing bot verification steps and relying on Raid Protection [Discord, 11074987197975].
- Server Guide: 3-5 New Member To-Dos and resource pages built from read-only channels; replaces the Welcome Screen [Discord, 13497665141655].
- Raid Protection: ML join-raid detection, alert channel, CAPTCHA for joiners for the next hour; Security Actions pause invites and DMs between non-friends [Discord, 10989121220631, 17439993574167].
- Join modes: Invite Only (default), Apply to Join (custom questions, admin approval), Discoverable [Discord, 29729107418519].

## 4. Channel types

- Forum: Community servers only; post guidelines; required tags; list or gallery layout; per-forum search; one pinned post; posts move to Older Posts after 1 h / 24 h / 3 days (default) / 1 week of inactivity; close and lock; AutoMod and slowmode apply. New posts do not notify everyone following the forum [Discord, 6208479917079].
- Threads: hide after inactivity (3 days default); 1,000 members max; private threads need Boost Level 2 [Discord, 4403205878423].
- Announcement: followable by other servers through a webhook; @everyone, @here and role mentions are stripped in following servers; 10 publishes per hour; edits propagate; deletions leave a note [Discord, 360032008192, 360028384531].
- Slowmode: 5 s to 6 h per user per channel [Discord, 360016150952].
- Scheduled Events: voice, Stage or external; voice events cap at 99 participants; Stage holds 10,000 listeners without video [Discord, 4409494125719, 33694251638295].
- Channel structure: about 4-5 channels per category; names truncate near 25 characters; topics in one or two sentences [Discord, community guide "Channel Categories and Names"].

## 5. Caps

From article 33694251638295 [Discord]:

| Cap                                        | Value                                                |
| ------------------------------------------ | ---------------------------------------------------- |
| Servers per account                        | 100 (200 with Nitro)                                 |
| Message length                             | 2,000 characters (4,000 Nitro)                       |
| Members per server                         | 25 million                                           |
| Channels including categories              | 500                                                  |
| Channels per category / categories         | 50 / 50                                              |
| Roles                                      | 250                                                  |
| Invite codes per server                    | 999                                                  |
| Audit log retention                        | 45 days                                              |
| "All messages" mobile push                 | unavailable above 2,500 members; mentions still push |
| Offline member list                        | hidden from 1,000 members, back under 800            |
| Followed announcement channels per channel | 10                                                   |

## 6. Server Insights

- Alpha feature; members can opt out, and announcement stats need posters to allow data use, so counts are partial. Community servers with 500+ members; permission "View Server Insights"; one-day lag; 120 days of history (longer only for Partner and Verified); CSV export [Discord, 360032807371].
- Privacy buckets: referrers, countries and devices under 50 members roll into "Other" [Discord].
- Definitions: Visitor = member who viewed at least one channel; Communicator = member who sent a text message or spoke in voice; New Member Retention = share of new members who return after a week; the Audience tab covers members who visited in the past 28 days [Discord, community guides].
- Benchmarks Discord states: the communicator chart is drawn against "30% communicators"; aim for roughly 50% of members visiting and 50% of visitors communicating; for events "a 1-2% increase in participation is a sign of progress while 3-5% is the gold standard" [Discord, community guides].
- Attribution: one invite link per traffic source; "Most Popular Invites" and "Most Popular Referrers" tables [Discord].

## 7. Badges, boosts and identity

- Partner Program closed to new applications; existing partners keep perks [Discord, 360047236171].
- Verified Server Program: games only; a released Steam game with the Discord invite on its store page, claimed through a Developer Portal team. Companies, films and musicians were dropped [Discord, 360001107231].
- Boost levels: 2 / 7 / 14 boosts. Custom invite link (vanity URL) needs Level 3 and lapses when boosts drop [Discord, 360028038352, 115001542132].
- Server Tags: a 4-character tag plus icon members display on their profile across Discord; 3 boosts; not unique; changing it forces members to re-apply; clicking it opens the Server Profile with a Join button [Discord, 31444248479639].

## 8. Policy: spam and inflation

- Community Guidelines 13-16: no unsolicited bulk messages; no self-bots; no inauthentic engagement or inflated membership; no buying or selling accounts, servers, permissions or vanity URLs [Discord, discord.com/guidelines].
- Platform Manipulation Policy: engagement is inauthentic if "purchased, induced (like promises of financial reward), fraudulent ... or falsified"; named examples "join-for-join", "invite rewards", purchasing fake members; spam includes normal accounts acting manually [Discord].
- Tension: Discord's 2024 member-referral guide suggests rewarding top inviters with roles or rewards. The policy names invite rewards as banned. Reward helping (answers, talks, contributions), never invite counts.
- Partnership ads DMed by a bot on join: "regarded as spammy" and possibly against the ToS. Use a #partners channel or an announcement [Discord, community guide "Understanding Community Partnerships"].

## 9. Per-server promotion rules

Rules change; quote them only after re-reading the server's rules channel or page.

**Reactiflux** (reactiflux.com/promotion, /conduct) [server]:

- "This is a community, not a free audience." Recruiting, lead generation, marketing, market research and solicitation only in dedicated channels; tolerance drops as the server grows.
- Before anything commercial, ask the channel's permission, state intent, follow the response. More leeway for active members.
- Self-test, yes: made it yourself, relevant, usable without paying. No: announcing an announcement, spec work, giveaways or contests, asking people to subscribe.
- `#job-board` paid recruiting only; `#looking-for-group` unpaid non-commercial; `#events` one post per conference milestone; `#i-wrote-this` episodic content at most every 2 weeks; `#i-built-this` "predominantly meant as a showcase for individuals, but may be used for launch announcements of indie works"; `#q-and-a` hosted sessions pitched to the mods by email.
- Paid courses and books only in reply to a member; surveys only from active members, once; other communities generally not promoted.
- No DMs unless the person granted permission in the server.

**Python Discord** (pythondiscord.com/pages/rules) [server]: no unapproved advertising; no paid work offered or asked; no answers copied from ChatGPT or similar tools; stay on the channel topic; reports via ModMail.

**Rules kept only in-app**: many large servers (e.g. The Programmer's Hangout, `#rules-and-info`) publish rules only inside Discord. Read them after joining, before posting.

**Small-server pattern** [practitioner]: one self-promo channel; posts elsewhere deleted, DMs included; caps from once per 24 h to no repeat within 14 days; often no invite links to other servers.

## 10. Searchability cases

[practitioner, project announcements]

- Nuxt (2021, before forum channels existed): moved support to GitHub Discussions because Discord answers could not be searched or indexed and unanswered questions got buried within hours.
- Vector (2024): moved support from Discord to GitHub Discussions for a searchable knowledge base.
- TCGdex: replaced support text channels with a Discord forum synced to GitHub Discussions.
- PocketHost: moved to Discord in 2023, back to GitHub after a user vote in 2024.
- Prisma: adopted an existing unofficial server as official (2023), retired its Slack (2024).
- TypeScript Community: two static help channels broke near 9,000 members as questions stacked unanswered.

## 11. Sources

support.discord.com articles by ID: 14078261239831, 360023968311, 360030843331, 4409308485271, 25323248535319, 4673515000983, 44049845164823, 44302319454359, 360047132851, 216679607, 1500000466882, 11074987197975, 13497665141655, 10989121220631, 17439993574167, 29729107418519, 6208479917079, 4403205878423, 360032008192, 360028384531, 360016150952, 4409494125719, 33694251638295, 360032807371, 360047236171, 360001107231, 360028038352, 115001542132, 31444248479639, 215253258. Policy: discord.com/guidelines, discord.com/safety/platform-manipulation-policy-explainer. Guides: discord.com/community (Understanding Server Insights; Using Insights to Improve Community Growth and Engagement; Understanding Your Community Through Insights; Understanding Event Metrics; Channel Categories and Names; Understanding Community Partnerships; Growing Your Community Through Member Referrals).
