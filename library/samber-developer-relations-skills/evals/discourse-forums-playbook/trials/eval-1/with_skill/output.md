# Quillstack forum seeding plan (forum.quillstack.dev, opening Nov 21)

I read the `discourse-forums-playbook` skill and its templates reference. I haven't seen your Discourse admin settings, so plan tier and live values are unchecked (see "Check before Nov 9").

## Verdict

- Seed the forum with about 8 real questions from your 900 Zendesk tickets. Don't use 15 persona accounts and 60 AI threads.
- Cut 14 categories to 4, and use tags for the SDKs.
- Your team and a short list of invited customers carry the forum until real members arrive.

## 1. Refused moves

| Planned | Verdict | Reason |
|---|---|---|
| 15 persona accounts ("Dana from fintech", "Raj the hobbyist") | ❌ Refused | Discourse's own community manager calls seeding with fake members "a hard no" [practitioner]. Members who discover it leave, and a developer audience will check. |
| 60 ChatGPT-written threads and replies | ❌ Refused | Google's spam policies name generating many pages without adding value as scaled content abuse [Google]. Invented questions also answer nothing a real user asked. |
| 14 categories, one per SDK plus Billing, Roadmap, Jobs, Off-topic | ❌ Refused | Empty rooms announce a dead forum. The skill says start with 3–5 and split later [practitioner]. |
| (Not planned, but common) login required "until we're ready" | ⚠️ Avoid | The whole site drops out of search, and opening login-only posts later breaches what members agreed to [practitioner]. Restrict categories instead (section 5). |

Practical point for the growth lead: Discourse also limits new accounts to 3 per IP and 3 topics and 10 replies on day one, with 30 s between posts [Discourse]. Fifteen accounts created from one office would hit those limits and look like spam to spam detection. Real people have no such problem.

What the growth lead actually wants is a forum that doesn't look empty on day one. Section 6 covers how to get that honestly.

## 2. Assumptions

You gave no answers to the interview, so I assumed these. Correct any that are wrong.

1. **State:** not opened.
2. **Primary job:** support deflection, with search acquisition as upside. Staff answering most solutions is therefore fine at first.
3. **Answerers:** the 4-person support team, weekdays, one time zone. The target is a first reply within one working day, and a daily pass of about 45 minutes by one rotating owner. That is about 4–5 team-hours a week at launch.
4. **Content:** public, except billing and account matters, which go to email.
5. **Plan:** hosted. Solved and AI spam detection depend on the tier [Discourse].
6. **Deadline:** Nov 21, a one-off push followed by a compounding asset.

**⚠️ Nov 21, 2026 is a Saturday.** The skill's welcome post promises a staff answer on weekdays, so the first reply would wait until Monday. Pick one:

- Keep Nov 21 as a quiet public flip and announce Tue Nov 24.
- Move the flip to Tue Nov 17 or Mon Nov 23.

This plan flips on the 21st and announces on Tuesday, Nov 24. If you're in the US, Thanksgiving (Nov 26) falls in the first week, so confirm cover.

## 3. Categories and tags

**Four categories, each with a one-sentence About post.** Staff categories are the Discourse defaults.

| Category | Type | About line |
|---|---|---|
| Support | Q&A, Solved enabled | "Questions about using Quillstack. One problem per topic. Include SDK, version and the full error. Mark the reply that solved it." |
| Announcements | Staff topics, replies open | "Releases and changes. Questions about a release: reply here. Problems with your setup: open a Support topic." |
| Show and tell | Standard | "Projects, plugins and write-ups built on Quillstack. Self-promotion is welcome here and only here: one topic per project, updates as replies." |
| Feedback | Standard | "Feature requests and product criticism, including what you want on the roadmap. Search first and like an existing topic instead of opening a duplicate." |

**What happens to the other ten planned categories:**

- **Per-SDK categories** (Go, Python, Node, Java, Rust, .NET and so on) become **tags**. Per-SDK categories fragment about 4 topics a week across six rooms.
- **Billing:** not a forum category. Billing carries invoices, keys and account data, and contract-covered content must stay restricted from the start. Point to `support@quillstack.dev` in the welcome post.
- **Roadmap:** folded into Feedback, plus pinned release posts in Announcements. A public roadmap category needs staff to reply to every request, and the Feedback About line already commits you to that.
- **Jobs and Off-topic:** skipped. Nobody to post in them yet, and the skill's rule is to split only when one category carries too many unrelated threads.

**Tags:**

- Pre-create `go`, `python`, `node`, `java`, `rust`, `dotnet` and the other SDKs, plus tags for product area and integration. Only TL3 and staff can create tags by default [Discourse], so a missing tag is otherwise a dead end.
- Require one SDK tag in Support.
- Add version tags (for example `v2`, `v3`) only for versions you still support.
- **Homepage:** Categories, until there is daily traffic, then switch to Latest [practitioner].

**Split rule:** open a dedicated SDK category only when one SDK's tag carries more than about a third of Support topics and its threads are mostly unrelated to the others. Review monthly.

## 4. Trust levels and spam: settings to set

| Setting | Action | Reason |
|---|---|---|
| Trust levels | Keep defaults. No bulk TL3 grants. | TL3 loses nofollow and can recategorize and rename [Discourse]. Earn it. |
| Verified customers | Optional group granting TL1 only. | Skips the sandbox without handing out powers. |
| AI spam detection | Check AI settings first; it is on by default on lower hosted tiers and scans the first 3 posts of TL0–TL1 users [Discourse]. | Day-one spam arrives as TL0. |
| Watched words, disposable email domains | Configure now. | Cheap, and in the skill's spam order. |
| Approval queue | Leave off. During a spam wave only, replace `trust_level_0` with `trust_level_1` in both approval-exempt group settings. | Groups are cumulative. Removing TL0 alone would queue every member [Discourse]. |
| Product-team moderation | Use category group moderation for SDK owners if you want them in Support. | Off by default; avoids granting full staff rights [Discourse]. |

## 5. Pre-launch phase (restricted)

Use category permissions, not site-wide login required. For the three weeks before opening:

1. Create the four categories visible only to staff and a `founding-members` group.
2. Flip them to public on launch day.
3. Tell founders in the invite that everything they post goes public then.

## 6. Cadence

Every pre-launch step is real people under real names. The plan is compressed from the skill's six-week founding phase because you have three weeks.

**Week of Nov 2 (days −19 to −15)**

1. Choose the forum owner and the daily rota. Everyone answers under their own name with staff flair [Discourse].
2. Check the items in "Check before Nov 9".
3. Build the four categories, About posts, tags and the welcome topic (template below).
4. Rewrite the default guidelines and link your code of conduct.
5. **Recruit 10–30 founding members by name.** Draw from:
   - Zendesk requesters who asked good questions or came back.
   - People answering others in GitHub issues.
   - Beta users.

   Send the founding-member invite (below), up to 25 on Mon–Tue.
6. **Ticket triage (2 people, about 4 hours each).**
   - Export the 900 tickets. Cluster by SDK and error.
   - Pick the 8 topics that fit all of the following:
     - Asked at least 3 times.
     - Fully answerable in public.
     - Contain no keys, account data or contract content.
     - Cover a spread of SDKs (at least 4 of your 6 or more).
   - Only for those 8, send the consent request (below) to the original asker.

**Week of Nov 9 (days −12 to −8)**

7. Founders join the restricted categories from Mon Nov 9.
8. Seed 5–8 topics. Each is posted by the asker, or by staff under their own name with the asker's consent, rewritten without company names or logs. Each gets a full answer and a Solved mark.
9. Set the Solved auto-close delay to 7–14 days when staff mark the solution [practitioner], so the asker can say it failed.
10. Post the first weekly ritual topic ("What are you building this week?") for founders.
11. Ask founders for 2–3 real questions each from their own work. Where they really have them, they post them; staff and other founders answer.

**Week of Nov 16 (days −5 to −1)**

12. Add links from docs, error messages and the product help menu. The skill ranks these among the compounding surfaces.
13. Re-read the seeded Support topics in a logged-out browser window (titles in the asker's words) and fix titles.
14. Write the announcement (template below), but don't send yet.
15. Hold a 15-minute cover rota for launch week, including who answers if two people are out.

**Sat Nov 21: flip to public.** Sitemap and `?print` check on one solved topic (section 9).

**Tue Nov 24: announce once** in the newsletter, docs banner, release notes and email signatures.

**Days 1–90 (starting Nov 21)**

- One owner does a daily pass on unanswered and unsolved topics and welcomes each new member's first post.
- Post the weekly ritual topic every week.
- Monthly: read the admin reports (time to first response, topics with no response, trust-level growth) and Search Console. Promote recurring solved answers into docs, and split or merge categories.

## 7. Why this looks busy enough

An honest launch with 8 solved topics, a welcome post, a ritual topic, 10–30 founders and about 4 weekly Q&As will look small but alive. The seeds are the questions your users actually ask, so search engines can match them. If the growth lead wants more volume, the real levers are:

- A bigger founder list, especially from the 900 tickets.
- Docs and in-product links that send askers to the forum.
- Answering every question fast.

Don't buy ads or run a promotion push while topics sit unanswered. Newcomers arrive as TL0 into silence and don't return.

## 8. Surfaces ranked for this user

1. Support with Solved, seeded from tickets. It is your default rung and your strongest asset.
2. Welcome topic, About posts and guidelines.
3. Weekly ritual topic.
4. Summary email tuning. It is weekly by default for absent members and stops after 180 days of inactivity.
5. Links from docs, error messages and the product help menu.
6. Show and tell, then Announcements, then badges and groups.

**Announcements starve the list.** A forum full of release posts reads as a press room. Post a few by hand, under the author's name, with one real question each. Don't auto-post every blog article or release feed.

## 9. Limits that bind

- TL0 gets 3 topics and 10 replies on day one, 2 links and 0 attachments [Discourse]. Founders will hit this. Grant them TL1 through a group if needed.
- Support: one question per topic. Show and tell: one topic per project.
- Search, user, group and tag-filter pages are never indexed [Discourse].
- Do not enable Solved on any category other than Support. Solved switches the whole category to Q&A markup, and Google wants that only on one-question-with-answers pages [Discourse] [Google].

## 10. Check before Nov 9

- Plan tier: does it include Solved, AI spam detection and category group moderation?
- Live values: TL thresholds, accounts per IP, Solved auto-close default, approval-exempt group settings.
- Sitemap: `/sitemap.xml` lists the solved topics, and `?print` on one shows it public and canonical.
- Subdomain: keep `forum.quillstack.dev`. Discourse recommends a subdomain, and Google states no preference on subfolders [Discourse].

## 11. Templates filled for Quillstack

I drafted these in plain language but did not run them through a humanizer skill.

**Welcome topic**

```
Welcome to the Quillstack forum

This is where Quillstack users help each other build with our SDKs.
The Quillstack team reads every new topic on weekdays and answers within one working day.

- Stuck or seeing an error? Post in Support, one question per topic, with your SDK, version and the full error.
- Built something with Quillstack? Show it in Show and tell.
- Want something changed, or want to see it on the roadmap? Feedback. We reply to every request with a decision, even when it is "not now".
- Billing or account access? Email support@quillstack.dev; never post keys or invoices here.

Please read the guidelines before your first post.
```

**Founding-member invite**

```
Subject: Help us start the Quillstack forum?

Hi [name],

You [specific action, e.g. "answered three other users' questions in our GitHub issues last quarter,
including the retry one we still link to"]. We're opening a forum on Nov 21 so those answers stop
getting buried in tickets and closed issues.

Would you join the first group, about two weeks before it opens publicly? The ask: answer
questions in your area when you see them, for the first three months. In return you get early
access, a Founding member badge and a direct line to the SDK team.
Everything posted before the opening becomes public on Nov 21.

No is a fine answer.
[your name], [role] at Quillstack
```

**Seed-from-ticket consent request**

```
Hi [name],

Your question last month about [topic] is one we get often.
Could we post it on the new public forum with the answer, so others find it?

Two options:
1. You post it yourself (we'll reply with the fix and mark it solved), or
2. We post a rewritten version under my name, with no company names or logs from your account.

If you'd rather we didn't, nothing changes.
[your name], Quillstack
```

**Weekly ritual topic**

```
Title: What are you building this week? (week of [date])

Reply with one thing you're working on with Quillstack, and one thing that's in your way.
Team members answer the blockers in this thread or open a Support topic for them.
```

**Announcement (send Tue Nov 24)**

```
Title: The Quillstack forum is open

The forum is now public at forum.quillstack.dev.
Start in Support for questions (include SDK, version and the full error), or Show and tell for projects.
Eight common questions from our support queue are already answered there.

We answer on weekdays within one working day. Questions about this post: reply here.
```

The skill also has a first-post welcome reply, a solution nudge and duplicate and move notes. They need no Quillstack-specific changes, so use them as written.

## 12. Metrics and stop rule

Target values start as [practitioner] defaults. Reset them from the week-1 baseline (Nov 21–27).

- **Median time to first reply:** under 24 hours. Topics with no reply after 48 hours: near zero. The 7-day figure understates the 48-hour one.
- **Solved share** of Support topics.
- **Non-staff solutions share:** staff answering is the design for support deflection, so this is a trend, not a launch target.
- **TL2 and TL3 member count** and new members' first-week post rate.
- **Search landings** on solved topics, from Search Console.
- **Ticket deflection (Zendesk):** tag tickets whose answer was a forum link. Compare against last quarter's 900.
- **Stop rule:** after 90 days (by about Feb 19, 2027) with no non-staff solutions and no TL2 growth, fold the forum back per the community-launch skill's kill criteria (`samber/developer-relations-skills@developer-community-launch`).

## 13. Decisions I need from you

1. Launch date: keep Sat Nov 21 with a Tue Nov 24 announcement, or move it?
2. Is the forum's primary job support deflection? If it is feedback or an extension ecosystem, the category order changes.
3. What are the team's time zones, and how many weekly hours can the 4 people give?
4. Is any customer content under a contract that bars public posting?
5. Which hosted tier are you on? I need it to confirm Solved and AI spam detection are available.
6. Should I also draft the rota and the founder shortlist criteria?