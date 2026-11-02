# Ledgerline: support migration plan for November 2026

**Recommendation: don't shut down GitHub Discussions.** Give support one front door (Discord #help) and keep Discussions as the indexed archive. The VP's premise is partly true, but it doesn't deliver the SEO consolidation she wants for your audience.

I couldn't browse in this session, so the Discord dates and limits below come from the playbook's reference file, not a fresh read of Discord's pages. Re-read the three web-presence articles (IDs 4673515000983, 44049845164823, 44302319454359) before quoting any date to the VP.

## 1. Why the "shut down Discussions" move fails [Discord]

The playbook refuses the promise that "Discord answers will rank now." Three facts break the plan:

1. **Your members' individual answers mostly won't be indexed.**
   - About 70% of your members are in Germany, France and the Netherlands, all EU/EEA.
   - Discord's per-member "Channel Messages" setting defaults to off in the EU/EEA, so those answers stay out of web search unless the member opts in.
   - The other ~30% default to on in most regions, which skews whatever gets indexed toward non-EU members. You'd be indexing a sample, not your support corpus.
2. **What does reach the web is an AI summary you don't fully control.**
   - Channel Summaries follow admin settings only. Members have no control over them, and Discord says they "may not always be accurate."
   - A wrong summary about idempotency keys, webhook signature checks or refund semantics, sitting on a public page for a payments API, is a support and liability risk.
3. **The dates fall in or after your migration window.**
   - Per the reference file, Server Web Pages and Channel Summaries start 2026-11-16, and Channel Messages start in mid-December 2026. Nothing is indexed today.
   - If you close Discussions first, you lose a working indexed archive for a corpus that may rank thinly, or not at all.

The playbook's own precedents point the same way:
- Nuxt and Vector moved support from Discord to GitHub Discussions for searchability.
- TCGdex runs a Discord forum synced to Discussions.
- PocketHost moved to Discord, then moved back after a user vote.

## 2. Assumptions (correct any that are wrong)

- Support questions arrive daily, so someone can own #help every weekday.
- #help is currently a text channel. If it's already a forum, skip step 2 of the Week 2 work.
- Discussions has existing answered threads with search traffic. Check this in Search Console in Week 1.
- Ledgerline staff cover DE, FR and NL working hours. That's an unknown; the plan's same-day-answer promise depends on it.
- Developers can reach Discord at work. Check with a quick poll, because corporate blocks would weaken the whole plan.

## 3. Job and owner

- **Job:** run your own server, with Discord as the live front door.
- **Owner:** one named support lead for the plan, plus one named person per weekday for #help.
- **VP's real goal:** one place to ask, less fragmentation. You can deliver that without deleting the archive.

## 4. Surfaces, ranked for Ledgerline

| Rank | Surface | Why for this user |
|---|---|---|
| 1 | Forum help channel with required tags, own server | Highest value. Daily support questions justify the standing owner cost. |
| 2 | Discussions kept as the indexed archive | Answers that must be found for years need an indexed home. The playbook's Web Presence guidance says keep a separate one. |
| 3 | Announcement channel (release and API-change notices) | Cheap and compounding. |
| 4 | Discoverable and Web Presence | Already on. This is now a privacy decision first, a growth one second. |
| 5 | Events and office hours | Optional after the migration settles. |

## 5. Decisions needed before 2026-11-16

1. **Web Presence channels.**
   - Choose which channels feed summaries. Recommendation: allow announcements and a sanitized public #help forum only, and make #contributors, staff and customer channels role-restricted.
   - Check every channel's @everyone View permission. Only role-restricted channels stay off the web.
2. **Payments data.** Public help posts will carry post guidelines forbidding pasted keys, tokens, card numbers, customer data and unredacted logs. Route account-specific issues to a private ticket channel. Moderators delete leaks immediately and ask for key rotation.
3. **GDPR check.** Summaries of EU members' public posts are published without a member opt-out. Ask your DPO or legal contact before 2026-11-16. This is my judgment, not a Discord rule [practitioner].
4. **Discoverable fallback.** If legal objects, turn Discoverable off. The server reverts to Community and the web page comes down, though search engines may keep cached copies. You lose Discovery listing, which is the lowest-ranked surface above anyway.

## 6. Dated cadence

**Week 1, Nov 2-6: baseline and decision**
1. Present this plan to the VP. Propose "one front door, two stores" and a review date of 2027-02-15 for any retirement of Discussions.
2. Capture baselines: Discussions posts per week, answered share, Search Console clicks to Discussions URLs, Discord #help posts per week and same-day answered share, and weekly communicators from Insights.
3. Poll developers on whether Discord is reachable at work.

**Week 2, Nov 9-13: build**
1. Convert #help to a forum channel with required tags: bug, question, integration, feature-request, plus a "solved" tag. Posts drop to Older Posts after 3 days of inactivity by default.
2. Publish post guidelines (see template A).
3. Assign weekday owners and set the rule: answered the same working day.
4. Update Onboarding with a "What brings you here?" question routing to #help, announcements or contributing.
5. Restrict channels that must stay off the web.
6. **Send the Web Presence notice** (template B) on Nov 9, a week before go-live. Name which channels feed summaries and which don't, and tell members where to find their data setting.
7. Edit the Discussions welcome post and the README: "Quick questions: Discord #help. Questions that need a lasting public answer: Discussions."

**Week 3, Nov 16-20: go-live**
1. Nov 16: the Server Web Page and summaries start. Spot-check the generated page and summaries against your channel list. Remove or restrict any channel that appears and shouldn't.
2. Staff answer in #help with a named account, not a shared brand account. No automating the account; self-bots are banned.
3. Copy answers worth keeping into Discussions by hand (template C). Keep this manual for now; syncing needs a bot, which is out of this playbook's scope.

**Weeks 4-5, Nov 23-Dec 4: tune**
1. Prune dead channels. Discord says too many channels "spread the conversation too thin."
2. Publish release notes through the announcement channel, without @everyone.
3. Re-read Discord's articles in the first week of December and confirm the mid-December Channel Messages date and regional defaults before telling anyone.

**Dec 15 (check-in):** re-check member-level behavior after Channel Messages starts. Verify nothing sensitive surfaced in summaries.

**Monthly:** Insights export (history stops at 120 days), channel pruning, spot-check of what the web page shows. **Quarterly:** review Discoverable status, Web Presence channels and moderator 2FA.

## 7. What changes for Discussions

- **Keep it open and indexed.** Don't delete it. Closing existing threads or archiving read-only preserves the URLs, but only after the Feb review.
- **Re-scope it** to long-lived questions: integration patterns, error-code explanations, and anything with a lasting answer.
- **Redirect the live traffic** by pinning "ask in Discord for quick help." This gives the VP her single front door without destroying search assets.

## 8. Binding limits

| Limit | Kind | Source |
|---|---|---|
| Server Web Pages and Channel Summaries start 2026-11-16 (verify) | enforced | [Discord] |
| Channel Messages start mid-December 2026 (verify) | enforced | [Discord] |
| Messages: EU/EEA, UK and others default off per member | enforced | [Discord] |
| Summaries: no member control; admins pick channels | enforced | [Discord] |
| Turning a feature off stops new content; cached copies can remain | enforced | [Discord] |
| Onboarding: 7 default channels, 5 writable | enforced | [Discord] |
| Forum posts move to Older Posts after 3 days by default | enforced | [Discord] |
| No invite rewards or join-for-join campaigns | enforced | [Discord] |
| Insights history: 120 days | enforced | [Discord] |
| Same-day answer promise depends on staffing | policed | [practitioner] |

## 9. Templates (adapted; run your humanizer pass before posting)

**A. #help post guidelines**
```text
Before posting:
1. Search this forum and the docs: {docs link}.
2. Title = the error or goal in one line ("Webhook signature fails after key rotation").
3. Include: API version, SDK and version, request ID, the full error response.
   Never paste API keys, card numbers, customer data or unredacted logs.
   This channel is public and can appear on the web. Redact first.
4. Pick one tag: bug / question / integration / feature-request.
Account-specific problems: use {private support link}, not this forum.
When solved, add the "solved" tag so the next person finds it.
Staff answer every post by the next working day ({time zones}).
```

**B. Web Presence notice (post Nov 9)**
```text
Heads-up: from Nov 16 our server page becomes public.
- AI-written summaries of #announcements and #help appear on our public
  server page and in web search, without usernames. Discord offers no
  personal setting for summaries; we choose the channels.
- Later, individual messages from those channels can appear too, but only
  if your own setting allows it (User Settings > Data & Privacy). It is
  off by default in the EU, UK, Canada, Brazil, Australia and South Korea.
- #contributors and #customer-support never appear.
- Never post keys, card data or customer data in public channels.
Questions: reply here.
```

**C. Pointer to the archive**
```text
Solved. I've written this up as a permanent answer: {Discussions link}.
```

## 10. Metrics

| Metric | Target or benchmark | Cadence |
|---|---|---|
| Communicators / visitors | Discord's ~30% benchmark, then your own baseline | weekly |
| New-member retention after a week | your baseline | weekly |
| Share of #help posts answered the same working day | decide after Week 1 baseline | weekly |
| Share answered by non-staff | rising | monthly |
| Joins per invite link per source | one link per source | monthly |
| Search Console clicks to Discussions | do not let this fall during the migration | monthly |
| Discord web page impressions and clicks | new signal; establish after Nov 16 | monthly |

Do not report member count as the result.

## 11. Message for the VP

> We can consolidate where people ask, not where answers are stored. About 70% of our members are in the EU, where Discord won't publish individual messages by default, so Discord alone can't carry our search presence. Discussions keeps working for search today. We'll make Discord the front door, keep Discussions as the archive, and review in February with real data whether either can be retired.

## Open questions for you

1. Is #help a forum or a text channel today?
2. How much traffic does Discussions get from search?
3. Who can own weekday coverage, and in which time zones?
4. Can your DPO or legal contact review the Web Presence setup before Nov 16?