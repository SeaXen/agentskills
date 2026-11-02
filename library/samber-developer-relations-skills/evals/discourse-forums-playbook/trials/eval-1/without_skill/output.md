# forum.quillstack.dev seeding plan (launch Nov 21)

## 1. Decision first: no persona accounts

I wouldn't create the 15 fake personas. I'd replace them with real staff and real customers. The growth lead's goal is a forum that doesn't look dead on day one, and this plan still meets it.

Why the personas fail:

- **They get found out.** Developers check join dates, avatar style, and posting cadence, and a ChatGPT voice is easy to spot. One screenshot on Reddit or HN ("Quillstack's forum is fake") costs far more than an empty forum.
- **Legal exposure.** Fake users posing as independent practitioners ("Dana from fintech") are deceptive endorsements. The FTC and EU consumer-protection rules cover that, and your counsel should confirm. I'm flagging this, not giving legal advice.
- **The content is worse than your own.** 60 generic LLM threads won't match your real support questions, so they won't rank or help anyone. They will also feed search engines and AI answers with unverified SDK advice under your domain.
- **Cleanup is hard.** Deleting 15 accounts later is a visible moderation event, and real users who replied to them get confused.

## 2. What goes in the forum instead

Seed with real answers from your own history. You have 900 tickets from last quarter, which is the best raw material available.

### 2.1 Mine the tickets (week 1)

1. Export the 900 tickets with tags, SDK, and resolution. Do this only if your Zendesk and privacy terms allow reuse. Ask legal first.
2. Cluster by question. Expect a few dozen recurring problems to cover most volume.
3. Pick the top 25–30 clusters. Rank by frequency × "answer is stable and public-safe."
4. Skip anything that contains account data, billing details, security issues, or an unannounced roadmap item.

### 2.2 Write the seed topics (weeks 1–2)

- Format is a real question with the title a user would type, then an accepted staff answer. Write the question in a generic voice, never as a fake user.
- Rewrite from scratch. Never paste ticket text. Strip names, companies, emails, IDs, and tokens. Search the final text for them.
- Author under the real staff member's own account, with a "Staff" badge, real name, and photo. Pick whoever actually answered the ticket.
- A mild disclosure is fine and builds trust. Example: *"Common questions from our support queue, answered here so you don't need a ticket."*
- Run any code sample before publishing. Every SDK sample is compiled or run by an engineer.
- You can use an LLM to draft from the cleaned clusters. A named human verifies every claim and takes ownership.

Target is about 30 topics, not 60. Spread them by real demand, not evenly per SDK. Add 3–4 pinned posts: welcome, community guidelines, "where to get help" (forum vs. ticket), and a roadmap-feedback thread.

### 2.3 Recruit real founding members (weeks 1–3)

This replaces the personas.

- Build a list of 30–50 people. Include design partners, frequent ticket submitters, beta users, and active GitHub issue authors across your SDKs.
- Send a personal invite from a named person. Say what they get: early access to the forum, direct line to engineers, and a "Founding member" badge.
- Ask each to post one real question or tip they actually have, in the week before public launch. Do not script or write their posts.
- Offer to move their existing open GitHub issue or ticket question to the forum, with permission.
- Realistic outcome is 8–15 genuine posts from outside staff. That is smaller than 60 but real.

### 2.4 Launch-day activity from real people

- Engineer AMA thread, scheduled and announced in advance, with named engineers.
- "Introduce yourself" thread, started by a staff member.
- A pinned "What are you building?" thread.

## 3. Categories: launch with 5, not 14

Fourteen categories on a forum with about 40 topics leaves most categories with 2–3 posts. That looks emptier than one busy category. Your ticket volume (about 70 a week) split six ways is about 12 a week per SDK at best.

| Category | Notes |
|---|---|
| Announcements | Staff-only posting; releases and incidents |
| Help | Main category; **one tag per SDK** (go, python, node, java, rust, dotnet) |
| Show & Tell | Projects and integrations |
| Feedback & Roadmap | Merges Roadmap with feature requests |
| Meta | Forum feedback and guidelines |

Notes on the ones I dropped:

- **Per-SDK categories:** use tags instead. Users can filter and watch an SDK, and you can promote a tag to a category once it carries steady volume, for example 20+ topics a month.
- **Billing:** keep it out of the public forum. Billing questions involve account data. Pin a "Billing and account: contact support" post that links to the ticket form.
- **Jobs:** defer. It attracts spam and recruiters, and moderating it is a cost with no day-one benefit.
- **Off-topic:** defer until there's organic conversation. Add it when members ask.

Check that your hosted Discourse plan supports the solved/accepted-answer feature and tag groups, since I couldn't verify your plan.

## 4. Staffing with 4 support people

- One person on forum duty per day, rotating, about 30–45 minutes of dedicated time at launch.
- Service level for launch month: first staff reply within 1 business day. Say so in the welcome post.
- Name a backup engineer per SDK, to answer questions support can't.
- Update the Zendesk macros so support points people to existing forum answers, and add a "post this on the forum" macro for non-sensitive questions.
- Moderation: pin the guidelines, require approval for first posts for the first month, and assign one moderator per timezone coverage window if you have one.

## 5. Timeline

Today is Sat Oct 31. **Nov 21 is also a Saturday**, and US Thanksgiving week follows. A Saturday launch means no staff on duty when the first real users show up.

I recommend this schedule:

| Date | Step |
|---|---|
| Nov 2–6 | Export tickets, cluster, pick the top 30. Confirm privacy and legal rules. Configure categories, tags, and guidelines. |
| Nov 9–13 | Write and review seed topics. Send founding-member invites. |
| Tue Nov 17 | Soft open to the invite list only. Staff answer everything within hours. |
| Fri Nov 20 | Review the first days: fix gaps, add topics for what people actually asked. |
| Mon Nov 23 | Public announcement, with staff on duty and the AMA scheduled. |

If you must keep Nov 21, make it the public date only if someone covers the weekend.

## 6. Measuring success

Don't measure thread count. Track:

- Median time to first reply, and share of topics answered.
- Share of questions answered by non-staff members, which shows whether a community is forming. Expect it to be low at first.
- Ticket deflection: tickets in the top-30 clusters per week, before and after launch.
- Week-4 posters: how many distinct non-staff people posted at least once.
- Search traffic to forum answers after 60–90 days.

## 7. Open questions for you

1. Do your Zendesk terms and customer contracts allow reusing resolved ticket content, anonymized and rewritten?
2. Is the growth lead open to the founding-member route if the target stays "not empty on day one"? Do you want me to draft the pitch for them?
3. Which hosted Discourse plan are you on? It determines which plugins I can rely on (solved, tag groups).
4. Do you want to keep Nov 21, or move the public date to Mon Nov 23?

I can draft any of these next: the invite email, the welcome and guidelines posts, the ticket-clustering prompt, or the forum-duty rota.