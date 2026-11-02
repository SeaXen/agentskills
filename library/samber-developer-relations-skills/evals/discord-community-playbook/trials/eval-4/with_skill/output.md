# Vectrix Discord: finalized setup checklist

**Next action:** cancel the Carl-bot gate and the welcome-DM bot, then build the 7-channel server below. Start with step 1 on Mon 2026-11-02.

Assumptions, since I took one pass instead of interviewing: no existing unofficial Vectrix server, about 8–10 hours a week each, one devrel in the US and one in the EU, and no hard launch date yet. Correct me on any of these and the plan changes.

## 1. Changes to your draft

| Draft item | Verdict | Replace with |
|---|---|---|
| Carl-bot reaction-role gate | ❌ Refused. Discord advises removing bot verification steps and using Raid Protection instead, and bot gates cost you joiners [Discord]. | Verification level Medium, Rules Screening and Raid Protection. Opt-in release pings go through native Onboarding. |
| Welcome DM bot with docs and newsletter | ❌ Refused. Join-DM promotions are "regarded as spammy" and may breach the ToS [Discord]. | Server Guide with the docs link, plus a resource page with the newsletter link. The member clicks it. |
| 12 SDK text channels plus 7 others | ❌ About 20 channels for zero members reads as dead. Discord says 4–5 per category and warns that extra channels "spread the conversation too thin" [Discord]. | One help forum with a required tag per SDK. Add an SDK channel only when its tag overflows. |
| #help | ✅ Kept, as a forum. Text-channel questions get buried within hours [practitioner]. | |
| #general, #off-topic, #showcase | ✅ Kept. | |
| #memes | ⚠️ Merged into #off-topic. | |
| #feedback | ⚠️ Becomes a `feature-request` tag in the help forum. | |
| #jobs | ⚠️ Dropped for now. Recruiting channels attract spam and have no audience at zero members. | Add later if members ask. |

## 2. Server build (Mon 11-02 to Fri 11-06, not public)

1. **Enable Community.** Set the verified-email level, the explicit-media filter on all members, a rules channel and a moderator-only updates channel [Discord].
2. **Set verification level to Medium** (5 minutes after email verification) [practitioner pick]. Turn on 2FA for both moderators now. Discovery will require it later [Discord].
3. **Turn on Rules Screening** (maximum 16 rules, aim for about 6) and **Raid Protection alerts** [Discord]. For the code of conduct and AutoMod rules, use `developer-community-moderation`.
4. **Create these 7 channels.** This is the Onboarding minimum: 7 default channels, 5 writable by @everyone [Discord].
   - Read-only: `#announcements`, `#rules`.
   - Writable: `#general`, `#help` (forum), `#introductions`, `#showcase`, `#off-topic`.
   - Also create the private moderator updates channel. It does not count toward the 7.
5. **Configure the `#help` forum.**
   - Create 12 SDK tags plus `solved`, `question`, `bug` and `feature-request`, which makes 16.
   - ⚠️ I did not find a forum tag cap in the Discord sources I read. Check it in the UI before creating all 16. If it is lower, merge the least-used SDKs under one tag.
   - Require a tag on every post.
   - Paste the post guidelines (template A below).
   - Keep the default 3-day inactivity setting.
6. **Set up Onboarding** with the single question in template B, and an opt-in `releases` role.
   - Never ping @everyone for releases. Ping `releases` instead [practitioner].
7. **Write the Server Guide** (3–5 to-dos, replaces the Welcome Screen [Discord]):
   1. Read `#rules`.
   2. Introduce yourself: SDK plus use case.
   3. Run the docs quickstart.
   4. Ask your first question in `#help`.
   5. Optional: the newsletter, on a resource page as a plain link. Never auto-subscribe anyone from Discord.
8. **Make `#announcements` followable.** Publish releases to followers, which strips mentions in the other servers. The limit is 10 publishes per hour [Discord].
9. **Create one invite link per source:** GitHub README, docs, each SDK README, newsletter, social. Use Server Settings > Invites for attribution [Discord].
10. **Set up the indexed home.** Under 1,000 members, Discord is not indexed at all [Discord].
    - Pin "bugs go to GitHub Issues, long-lived answers go to GitHub Discussions" in the forum.
    - Vector moved off Discord to GitHub Discussions for a searchable knowledge base [practitioner]. Use `github-engagement-playbook` for that.
11. **Set forum owners per weekday.**
    - Proposal: EU devrel owns Mon/Wed and the US devrel owns Tue/Thu. Fri alternates, and each owns the other's backup.
    - The public promise is an answer by the next working day. Track same working day as your internal goal.
    - Two part-timers is thin for a forum. If either is out, the owner slot goes blank, so name a backup.
12. **Run a humanizer pass on templates A–C** and fill the placeholders before anything goes live.

## 3. Cadence

- **Weeks 1–2 (11-02 to 11-13):** answer in 2–3 ecosystem servers your users already use, such as your SDK-language and vector-search communities.
  - Use your named account and a profile that names Vectrix.
  - Disclose when you mention Vectrix, a competitor or the category.
  - Include no Vectrix links.
  - Send no DMs.
- **Mon 11-09:** server goes live. Invite a founding cohort by hand: contributors, GitHub stargazers who engage, and people you helped in week 1.
- **Weeks 3–6 (11-16 to 12-11):** one weekly ritual, for example release notes or a monthly show-and-tell. Answer every help post the same working day. Prune channels nobody visits.
- **Launch week (date needed):**
  - One published announcement and one scheduled event.
  - Showcase posts only in host servers that allow them, once each.
  - Under 2 weeks out, send the moderator ask now and carry the launch on your own channels.
  - Never compress the earn-first weeks.
- **Monthly (first on Tue 12-01):** hand count, channel pruning and a check of host-server rules.
- **Quarterly:** review moderator 2FA and Discoverable status.

## 4. Discoverable and Web Presence

- ❌ **Not now.** Discovery needs 1,000+ members and 8+ weeks, and it is a privacy decision before a growth one [Discord].
- At that point, check every channel's @everyone View permission. Only role-restricted channels stay off the web.
- Announce it to members first. The EU/EEA and UK members' account setting defaults to off for individual messages, but AI summaries follow admin settings only [Discord].
- Don't promise anyone that Discord answers will rank or reach Google. Under 1,000 members they don't.

## 5. Binding limits

| Limit | Kind |
|---|---|
| Onboarding: 7 default channels, 5 writable | enforced [Discord] |
| About 4–5 channels per category | guidance [Discord] |
| Insights: from 500 members, 120 days of history | enforced [Discord] |
| Discovery: 1,000 members, 8 weeks, moderator 2FA | enforced [Discord] |
| Announcement: 10 publishes per hour, 10 followed channels | enforced [Discord] |
| No invite rewards or join-for-join | enforced [Discord] |
| Host-server rules (no unapproved ads, no copy-pasted AI answers on Python Discord, commerce only in dedicated channels on Reactiflux) | policed [server] |

Also refused: any invite contest or reward for invites. Reward helpers, not inviters.

## 6. Templates (adapted; humanizer pass pending)

**A. `#help` post guidelines**
```text
Before posting:
1. Search this forum and the docs: {docs link}.
2. Title = the error or goal in one line ("Upsert returns 429 at 10k vectors").
3. Pick your SDK tag and one type tag (question / bug / feature-request).
4. Include: Vectrix version, SDK and version, the code, the full error.
   Never paste API keys, tokens, cluster URLs, connection strings or
   customer data. This channel is public and may appear on the web.
   Redact first.
5. Confirmed bugs go to GitHub Issues: {link}.
When solved, add the "solved" tag so the next person finds it.
Staff answer by the next working day (US and EU time zones).
```

**B. Onboarding question** (single question, multi-select)
```text
What brings you here?
- I need help with Vectrix        -> #help, #announcements
- I'm evaluating vector databases -> #general, #showcase
- I'm contributing code           -> #general, #help, role: contributor
- Release news only               -> #announcements, role: releases
```

**C. Release announcement** (`#announcements`, published to followers, no @everyone)
```text
Vectrix {version} is out.
- {change 1}
- {change 2}
- Breaking: {change} (migration guide: {link})
Questions go in #help. Full notes: {link}
```

For going Discoverable later, use the Web Presence notice from the skill's templates, edited for Vectrix.

## 7. Metrics

Count by hand until 500 members, then export Insights monthly. Set your own baseline after the first 8 weeks, since you start from zero.

- Weekly communicators divided by visitors, against Discord's 30% benchmark [Discord].
- New-member retention after one week, and the share of joiners who post in their first week.
- `#help`: share of posts answered the same working day, and share answered by non-staff.
- Joins per invite link, by source.
- Host servers: answers given, accepted or thanked, and joins from your profile link.
- Member count alone is not a result.

## Open questions

1. What is the launch or major release date? It changes the cadence.
2. Where do Vectrix users already talk on Discord? That decides the 2–3 ecosystem servers for weeks 1–2.
3. How many hours a week does each devrel have, and in which time zones? That fixes the weekday-owner table.