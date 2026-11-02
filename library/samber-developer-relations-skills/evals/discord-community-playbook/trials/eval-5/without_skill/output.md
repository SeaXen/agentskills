# Pipewright #announcements routine (v2)

## Answer on hotfixes

**No second @everyone ping for hotfixes.** The ping count is the cause of the muting. Replace the blanket ping with a rule about who gets pinged and when:

| Event | Where | Ping |
|---|---|---|
| Weekly release (Thursday) | #announcements, **one** digest post | `@Releases` (opt-in role) |
| Hotfix, no action needed | #announcements, one short post | None |
| Hotfix where users must act, or an active incident | #announcements | `@Alerts` (opt-in role) |
| Security issue, data loss, or an outage affecting most users | #announcements | `@everyone`, rare and by explicit sign-off |

Default stance: `@everyone` is a maintainer-approved emergency tool, not a release tool. If you can't say what members must do or avoid, it isn't `@everyone`.

## Why the old routine fails

- 12–18 messages with @everyone means 12–18 notifications for one release. Members mute the server and then miss real emergencies.
- Discord limits publishing (crossposting) in an Announcement channel to about 10 messages per hour. Partner servers following the channel would lose the tail of a 15-item release. Verify the current limit in Discord's docs before you rely on it.
- Every item gets equal weight, so nothing stands out.

## New Thursday routine

**One digest message, one ping, one place for details.**

1. **Prepare (Wed).** Pick the top 3 changes for the headline. Write one line per item.
2. **Post (Thu).** Send one message in #announcements, under 2,000 characters. Use the template below.
3. **Details.** Link to the full changelog (release notes page or GitHub release). Optionally open a thread on the post for questions. Don't post items one by one.
4. **Publish.** Use the "Publish" button on the post. Once published, followers receive it.
5. **Hotfix.** Use the hotfix template below. Apply the table above for the ping.
6. **Reply window.** Someone from the team watches the thread for about 2 hours after posting.

### Digest template

```
**Pipewright vX.Y.Z is out** @Releases

**Highlights**
• <Item 1: what changed, why it matters>
• <Item 2>
• <Item 3>

**Also in this release**
<N> more fixes and improvements, including <one or two notable ones>.

**Upgrade:** <command or link>
**Full changelog:** <link>
**Questions?** Reply in the thread.
```

### Hotfix template

```
**Hotfix X.Y.Z+1**
**What was wrong:** <one sentence>
**Who is affected:** <versions or setups>
**What to do:** <upgrade command, or "nothing, already rolled out">
**Details:** <link>
```

Add `@Alerts` only when the "What to do" line asks for action.

## Role setup (one-time)

1. Create `@Releases` and `@Alerts`. Make both self-assignable through Discord Onboarding or Channels & Roles.
2. Pre-fill `@Alerts` as a recommended option. It's the low-volume role, so most members will accept it.
3. Remove `@everyone` mention permission from anyone who doesn't need it. Keep it for 2–3 maintainers.
4. Pin a short "How to get notified" message in #announcements.

## Transition plan

1. **Week 0.** Post the role picker and announce the change. Ping `@everyone` once in this post, explaining that it's the last routine ping. This is the one justified use.
2. **Week 1.** Switch to the digest format. Keep the old per-item posts out of #announcements.
3. **Week 4.** Review the numbers below and adjust.

## Partner servers

- Ask both partners to **Follow** #announcements, using Discord's native Announcement Channel follow. Each partner picks their own destination channel, so you build and maintain nothing.
- Only published messages are piped. The digest is a good fit for that.
- Role mentions and `@everyone` in a followed post shouldn't ping people in the partner server. Test this with one partner before you promise it. The partner decides what to do with the post locally.
- Don't put anything in the digest you wouldn't want a partner community to see: roadmap hints, internal links, or unreleased features.
- If either partner wants a different cut, such as only integration-relevant items, offer a separate #partner-releases channel they follow, with its own short template.
- Tell the partners about the format change before it ships.

## What to measure

Compare the 4 weeks before and after the change.

- Members leaving per week, and server-mute reports if you can see them. Mutes are mostly invisible, so ask a few active members.
- Count of `@Releases` and `@Alerts` members.
- Link clicks on the changelog link, if you use a trackable short link.
- Complaints in #feedback or modmail.
- Number of `@everyone` uses per quarter. Target: 0 to 2.

I have no numbers on your current mute rate or retention. The thresholds are for you to set after the first 4 weeks.

## Decisions for you

1. Who signs off on an `@everyone` emergency? I suggest the on-call maintainer plus one other.
2. Do you want the full changelog as a thread, or only a link?
3. Do the partners want the whole digest, or only a subset?