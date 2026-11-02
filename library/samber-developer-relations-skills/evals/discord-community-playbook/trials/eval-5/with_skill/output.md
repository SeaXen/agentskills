# Pipewright Discord announcement routine

**Answer: no second @everyone for hotfixes.** Remove @everyone from the routine altogether.

- Post one weekly digest and ping an opt-in role.
- Ping a separate opt-in role for critical hotfixes only.
- Partner servers follow the announcement channel. No pings cross over, and that's fine.

Claims carry the skill's labels: **[Discord]**, **[server]** and **[practitioner]**. I couldn't browse, so I didn't re-read Discord's support articles. Check the dated limits against them before you rely on them.

## Why the current routine fails

- **Refusal triggered:** @everyone is on the skill's "Do less" list. Members can suppress it server-wide and then miss what matters **[Discord]**. Your muting complaints are that failure happening.
- **Mentions are the only push at your size.** Above 2,500 members nobody gets a mobile push for every message, only mentions and role pings **[Discord]**. That makes @everyone the one lever you can't afford to burn. Pinging 12-18 times a week burns it.
- **Your routine can't run as written.** An announcement channel publishes at most 10 messages per hour **[Discord]**. A release of 12-18 items can't be published to followers as 12-18 messages.
- **A second @everyone makes it worse.** It teaches the muters to stay muted. Hotfixes are the messages that most need to be seen.

## Assumptions

I assumed the following where your request left gaps. Correct me if any is wrong, and the plan changes.

- Community is enabled, since you have an announcement channel.
- One or two people post, and the Thursday release time is fixed.
- Full changelog lives on your docs or GitHub, with one URL per release.
- "Hotfix" means an unscheduled release outside Thursday.
- Partners' mods haven't yet said how they want release posts.

## The new routine

### 1. Channel and permissions

1. Keep **#announcements** as an announcement channel, so followers' servers receive what you publish **[Discord]**.
2. Remove "Mention @everyone, @here and All Roles" from the poster roles, so nobody can ping @everyone by accident **[practitioner]**. Allow mentioning only the two roles below.
3. Create two roles, both opt-in:
   - **@weekly-release**: the Thursday digest.
   - **@critical-fix**: hotfixes that meet the bar below.
4. Add one Onboarding question, using the skill's template 5 shape **[practitioner]** (full text in the templates below). Onboarding grants the roles **[Discord]**.
5. Existing members never saw that question. Publish a one-time pick-your-roles message and use Discord's browse-channels-and-roles screen. The screen is my assumption; verify it exists in your Onboarding setup. Expect the roles to start small, and don't pad them by auto-assigning.

### 2. Thursday digest: one message, not 12-18

1. Post **one** message in #announcements. If you need more room, post a second message in the same hour. Never exceed 10 publishes per hour **[Discord]**. The 2,000-character cap per message applies **[Discord]**.
2. Contents, in order:
   - Version and one-line headline.
   - Breaking changes, always listed, with the migration link.
   - The top 3-5 items, ranked by what changes a user's day.
   - A link to the full changelog (all 12-18 items live there).
3. Ping **@weekly-release** only. Everyone else reads when they open the channel.
4. Use absolute URLs, not `#channel` mentions. Followed servers can't resolve your channels, and role mentions are stripped there **[Discord]**.
5. Publish (crosspost) it after the release tag and docs link are live.
6. Discussion goes to the help forum, linked by URL. Don't thread under the digest.

### 3. Hotfix rule: one ping, one narrow bar

Ping **@critical-fix** only when at least one of these is true:

1. A security fix that needs user action.
2. A bug that loses or corrupts data.
3. A bad release users should roll back or skip.

Everything else is a **silent hotfix**:

- One line in #announcements, no role ping.
- Don't publish it to followers.
- Fold it into the next Thursday digest.

Rules to keep the bar honest:

- A ping requires a named reason in the first line. If you can't write one, it's silent.
- Both approvers are by name: the post author plus one second person. A solo poster picks a named backup.
- Count critical pings monthly. My starting guess is that more than 2 a month means your release quality is the problem, not your ping policy. Treat that threshold as a guess to tune.
- Published critical messages count toward the 10-per-hour publish cap **[Discord]**. A bad day with several corrections stays well under it.
- Edits to a published message propagate to followers; deletions leave a note **[Discord]**. Correct by editing, and don't delete and repost.

### 4. Partner servers (two requests)

1. Answer with a follow of your announcement channel, not custom per-partner posts and not a bot pipe. Followed servers receive what you publish **[Discord]**.
2. Before connecting, send each partner's mods one message. Don't DM members. Use the skill's partnership shape (template below): what they'll receive, the digest weekly plus critical hotfixes only, no pings, edits propagate, and that they can unfollow any time.
3. Ask which channel they'll point it at, and check their own rules for bot or feed posts **[server]**.
4. Go live from the second Thursday, after you've seen the digest format work once. Following the channel is the partner's step, so give them the link and wait.
5. The feed arrives as plain text with no pings in their server **[Discord]**. Set expectations accordingly: partners get the news, not the alert.
6. Announce the partnership to your members with template 8's wording so nothing arrives unexplained.

### 5. Dated rollout

| Date | Step |
|---|---|
| Mon 2026-11-02 | Create the two roles. Strip @everyone mention rights from poster roles. Add the Onboarding question. Message both partners' mods. |
| Tue 2026-11-03 | Post the change notice with the role-picker. Whether to use one final @everyone for this notice is your call. It may be the only one left, but members who already muted it will miss it anyway. I'd skip it and pin the notice instead. |
| Thu 2026-11-05 | First digest: one message, **@weekly-release** ping, no partners yet. Re-read it as a follower would see it. |
| Thu 2026-11-12 | Partner follows go live, once their mods agree. |
| Thu 2026-11-26 | Fourth digest under the new routine. |
| Thu 2026-12-03 | Review (see metrics). Adjust the hotfix bar from the real count. |

## Binding limits

| Limit | Kind |
|---|---|
| 10 announcement publishes per hour | enforced **[Discord]** |
| 2,000 characters per message (4,000 with Nitro) | enforced **[Discord]** |
| A channel can follow at most 10 others (this is the follower-side cap; two partners fit easily) | enforced **[Discord]** |
| Role and @everyone mentions stripped in followed servers | enforced **[Discord]** |
| Above 2,500 members, only mentions push to mobile | enforced **[Discord]** |
| Partner servers' own rules for feed posts | policed **[server]** |
| Poster permissions and the hotfix bar | policed, by you |

## Metrics

Insights needs 500+ members and is partial: members can opt out, and history stops at 120 days **[Discord]**. Record a baseline from Insights now, before Nov 5.

1. **Communicators / visitors**, weekly, against Discord's roughly 30% communicator benchmark and your own baseline **[Discord]**.
2. **Visitors as a share of members**, against Discord's roughly 50% benchmark **[Discord]**. This is the closest proxy for people reading announcements again.
3. **Role subscribers**: count of @weekly-release and @critical-fix members, weekly.
4. **Critical pings per month**, with the reason for each.
5. **Complaints about announcements per week**, tallied by hand. Discord exposes no per-member mute count, so treat mute rate as unmeasurable. This is my read of the platform, not a stated Discord limit.
6. **Partner feeds**: whether each partner still follows after 4 weeks, and joins from the invite link in their feed message, if you add one.

Review on 2026-12-03. If role subscribers stay tiny but complaints drop, the routine works. A tiny audience for critical fixes is still a safer failure than muted @everyone.

## Templates

Adapt each to your voice. Run your humanizer pass on them before posting; I haven't run one.

**Weekly digest** (published, pings @weekly-release)

```text
@weekly-release Pipewright {version} is out.
Headline: {one line: what changes for users}.
Breaking: {item}. Migration guide: {link}. (Omit the line if none.)
- {Top item 1}
- {Top item 2}
- {Top item 3}
All {N} changes: {changelog link}
Questions: {help forum URL}
```

**Critical hotfix** (published, pings @critical-fix)

```text
@critical-fix Pipewright {version}: {security fix | data-loss bug | bad release, skip {bad version}}.
Who is affected: {one line}.
What to do: {upgrade command or action}.
Details: {link}
```

**Silent hotfix** (not published, no ping)

```text
Pipewright {version} fixes {one-line bug}. Details in {link}. It will be in Thursday's digest.
```

**Change notice** (pin it)

```text
Announcements are changing. We no longer ping everyone for every item.
- One weekly digest on Thursdays instead of one message per change.
- Pick your pings: {role-picker link}. Weekly releases, critical fixes only, or neither.
- Critical fixes (security, data loss, bad release) are the only hotfixes that ping.
Full changelog stays here: {changelog link}.
```

**Onboarding question**

```text
Question: What do you want to hear from us? (pick one)
- Weekly releases + critical fixes  -> roles: @weekly-release, @critical-fix
- Critical fixes only               -> role: @critical-fix
- Nothing, I'll read #announcements -> no role
```

**Partner mod message** (to mods, not DMs to members)

```text
Hi {server mods}, I work on Pipewright. Your members overlap with ours, so
we'd like to offer our #announcements feed through Discord's channel
follow: one digest a week plus the occasional critical-fix notice. No
pings reach your server. You can unfollow any time. Which channel would
you point it at, and do your rules allow a feed post there? Happy to
follow whatever you prefer.
```

## Open questions that would change the plan

1. Do you have a second poster, so the two-person check on critical pings works?
2. Do your partners want release news at all, or would they prefer a curated post from you?
3. Is your server Discoverable? If so, I'd review the public-channel settings separately.