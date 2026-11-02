# Fennec Labs Discord: Q1 plan (2026-11-02 to 2027-03-31)

ℹ️ I couldn't browse because WebFetch permission was denied. Every limit and date below comes from the playbook's reference file, not from a live re-read of Discord's articles. Before you quote any of them publicly, re-check articles 360030843331 (Discovery), 360047236171 (Partner) and 4673515000983 (Web Pages). Discord changes these often.

Labels used: **[Discord]** is Discord's own articles or policy. **[server]** is one server's published rules. **[practitioner]** is project write-ups and my judgment.

## 1. Two of your three asks are blocked, and the third is a stretch

| Your ask | Verdict | Why |
|---|---|---|
| (1) Invite leaderboard: hoodie + $50 for the top 10 inviters | ❌ Don't run it | "Invite rewards" and "join-for-join" are named examples of banned inauthentic engagement, and policy says rewarded engagement counts as "induced" [Discord]. Removal from Discovery follows enforcement [Discord]. |
| (2) Partner program + verified checkmark | ❌ Don't apply | Partner is closed to new applications. Verified is games-only: a released Steam game with the invite on its store page [Discord]. An observability SDK qualifies for neither. |
| (3) Server Discovery by end of January | ⚠️ Possible but unlikely, and low value | You need 1,000+ members, 8+ weeks of age, and unpublished activity criteria. Moderators need 2FA [Discord]. You're 360 members short. |

Discord's own 2024 member-referral guide suggests rewarding top inviters. Its policy names invite rewards as banned. Follow the policy [Discord].

## 2. Assumptions (nothing in your request answered these)

- You run your own server and also show up in other servers.
- Staff is 1-2 people, roughly 5 hours a week, in European time zones.
- Your members mostly come for SDK support and release news.
- You are not blocked from Discord at work.
- Community mode is on, since you have 640 members. Discoverable is off.
- Correct me on any of these and the dates shift.

## 3. Replacements

**Instead of the invite leaderboard: reward helping, never joins.**

- **Monthly "Fennec Helper" award.** Give a hoodie and $50 cloud credits to up to 3 people, chosen by staff on judgment. Criteria: accepted answers in the help forum, docs fixes, SDK PRs, talks. [practitioner]
- **Why staff judgment.** An automatic count of answers is just another leaderboard to game.
- **Eligibility.** Staff and existing employees are excluded.
- **Keep invites as measurement only.** Create one invite link per source (README, docs, release post, each partner server). Insights lists the top invites and referrers [Discord]. Use it to learn what works. Never attach a prize.
- **Related skill.** The `developer-champions` skill covers this program.

**Instead of the Partner program and checkmark: build credibility with things you can actually get.**

- Run a real help forum with an owner for every weekday.
- Publish release notes in an announcement channel that other servers follow.
- Set a Server Tag once you have 3 boosts [Discord]. It shows your name on members' profiles. This is a cheap badge.
- A custom invite link (vanity URL) needs Boost Level 3, which is 14 boosts [Discord].

**Discovery: treat it as a gated decision, not a promise.**

- Value is low. The Discover tab is experimental and sorts each category by member count [Discord]. At 1,000 members you'd sit near the bottom.
- Effort is the highest of any surface in the playbook.
- It mainly buys you a public Server Web Page. Decide that on privacy grounds first (section 5).

## 4. Surfaces, ranked for you

1. **Forum help channel.** An observability SDK produces constant "why no traces?" questions, which makes this the highest-value surface.
2. **Answers in ecosystem servers** (OpenTelemetry, Go, Python, Kubernetes communities). Disclosed, from a named account, no product links unless the link is the answer.
3. **Announcement channel** followed by partner servers.
4. **Weekly event** on Stage (office hours).
5. **Server Tags**, then **Discovery** last.

## 5. Dated plan

Today is Saturday 2026-10-31.

| Date | Action |
|---|---|
| **Mon Nov 2** | Baseline from Insights (you're past 500 members). Record weekly joins, communicators, visitors and one-week retention. Check Server Settings > Invites for joins per link. Enable 2FA for every moderator. |
| **Nov 2-13** | Answer in 2-3 ecosystem servers, with no links to your product. Read each server's rules first. Set a server nickname that names Fennec Labs. |
| **Nov 4** | Tell members the leaderboard is replaced by the Helper award. Publish the award criteria. |
| **Nov 9** | Turn on forum post guidelines (template 4 in the playbook). Keep it blunt: no DSNs, API keys or customer logs, because this channel is public. Name an owner for each weekday. |
| **Mon Nov 16** | Discord says every Discoverable server gets a public, indexable Server Web Page from this date, and AI channel summaries start [Discord]. This is why the decision comes first. Check article 4673515000983 now. |
| **Nov 16 - Dec 18** | Weekly ritual: release notes plus Stage office hours. Answer every help post the same working day. Prune channels nobody visits. |
| **Dec 7** | First Helper award (hoodie + $50 credits). Announce it. |
| **Dec 14 (approx.)** | Discord says individual member messages can appear in web search from mid-December [Discord]. Re-check the date. |
| **Dec 19 - Jan 3** | Holiday low-staff window. Keep the announcement channel and forum owner rota running, nothing new. |
| **Mon Jan 4** | Monthly Insights export. Compute net weekly joins since Nov 2. |
| **Fri Jan 15 (decision gate)** | See the gate below. |
| **Mon Jan 18** | If go: post the Web Presence notice to members (template 7) at least 2 weeks before going live. Audit every channel's @everyone View permission. Only role-restricted channels stay off the web [Discord]. |
| **Fri Jan 29** | If gates pass and the Discovery checklist is green, enable Discoverable. |
| **Feb 1 - Mar 31** | Monthly Helper award. Monthly Insights export and rule check on host servers. Quarterly review (Mar 31) of Discoverable status, Web Presence channels and moderator 2FA. |

**The Jan 15 gate** (go only if all hold):

1. Members are at or above ~900 on pace for 1,000, with real joins only.
2. The Discovery checklist in Server Settings shows no blocker.
3. Communicators, visitors and retention hold at or above your Nov 2 baseline. Discord's own benchmark is about 30% communicators.
4. You've decided the privacy trade-off (below).

If the gate fails, slip Discovery to Q2. That costs you nothing.

**Pace check.** From 640 to 1,000 by Jan 29 takes about 28 net joins a week for 13 weeks. If your Nov 2 baseline is well under that, Jan 29 is unrealistic. Say so early rather than chasing it.

**Privacy decision before Discoverable.**

- Channel summaries follow admin settings only. Members have no personal control over them [Discord].
- Individual messages also need each member's own setting. That setting is off by default in the EU/EEA, UK, Canada, Brazil, Australia and South Korea [Discord].
- Observability users paste traces and config into help posts. Keep an indexed home for long-lived answers, such as GitHub Discussions, and keep secrets out of public channels.
- Choose which channels feed web summaries. Keep contributor and private channels role-restricted.

## 6. How to grow from 640 to 1,000 without rewards

- Add one invite link per source: README, docs, each release post, each host server profile.
- Link the invite from the SDK's error messages and docs "get help" pages.
- Follow partner servers' announcement channels, and ask them to follow yours. Publish with no @everyone.
- Pitch hosted Q&As to host servers: "Zero-code tracing for Go services", 45 minutes, no slides (template 3).
- Never run join-for-join swaps, bought members, or bot DMs to new joiners. These can breach the ToS [Discord].

## 7. Binding limits

| Limit | Kind |
|---|---|
| Discovery: 1,000+ members, 8+ weeks old, activity criteria (numbers unpublished), moderator 2FA | enforced [Discord] |
| No invite rewards, join-for-join, bought members, or unsolicited bulk DMs | enforced [Discord] |
| Partner closed to new applicants; Verified is games-only | enforced [Discord] |
| Announcement channel: 10 publishes per hour; one channel follows at most 10 others | enforced [Discord] |
| Insights: 120 days of history, partial counts | enforced [Discord] |
| Host servers (e.g. Reactiflux): commerce only in dedicated channels, no DMs without permission | policed [server] |
| Python Discord: no unapproved ads, no copy-pasted AI answers | policed [server] |

## 8. Metrics

- Communicators divided by visitors each week, against 30% and your Nov 2 baseline.
- New-member retention after one week, and the share of joiners who post in week one.
- Help forum: share answered the same working day, and share answered by non-staff.
- Joins per invite link (measurement only).
- Host servers: answers given, accepted or thanked, and joins from your profile link.
- Don't report raw member count as the result. A join is not activity.

## 9. Templates to adapt

Use the playbook's templates 1 (answers elsewhere), 4 (forum guidelines), 5 (onboarding question), 6 (release announcement), 7 (Web Presence notice) and 3 (hosted Q&A pitch). Swap Kestrel for Fennec Labs and run a humanizer pass before posting.

## 10. Open questions

1. How many net joins per week are you getting now? This decides whether Jan 29 is realistic.
2. Do you have a split between EU/UK and other members? This affects how much of your help content the web will show.
3. Do you already have a GitHub Discussions home for long-lived answers?