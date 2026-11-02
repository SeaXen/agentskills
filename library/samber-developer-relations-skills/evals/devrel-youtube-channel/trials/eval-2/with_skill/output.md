# Quarrystack YouTube: what to change

**Short answer to your manager:** don't post more. Uploading more often isn't correlated with growth [YouTube]. Your problem is what's on the channel, and probably that nothing measures signups from it.

I couldn't open your Studio data, so I assume a value for each gap I couldn't ask about. Section 10 lists them. Where a number is a YouTube rule I tag it **[YouTube]**. Where it comes from a company or creator case I tag it **[practitioner]**.

## 1. Requests I decline

- **"Post more."** YouTube found growth "not correlated with time between uploads" [YouTube]. Choose a cadence the team can keep for a year (section 5).
- **Re-uploading more webinars and talks as the channel.** They rarely match anything people search for, so recommendations find no audience for them.
- **Reporting subscribers or public views as the result.** Subscribers aren't viewers [YouTube]. YouTube has also changed what counts as a view, so compare over time with watch time.
- **Tuning tags or publish hour.** Tags are "not important" and publish time isn't known to affect long-term views [YouTube]. Spend that time on topic, title and thumbnail.

## 2. Library diagnosis

Your numbers: 140 videos at about 300 views each is roughly 42,000 lifetime views. That's about 20 views per subscriber over the channel's life. Three things look wrong:

1. **Content with no search demand.** Webinars, conference talks and "v4.2 is out!" videos mostly answer nothing a developer types into a search box. Release videos serve people who already use the product.
2. **Probably no attribution.** "Zero signups" may mean "zero measured signups". If your signup flow has no source field and the video descriptions have no tagged links, nobody could ever see a YouTube signup. Fix that first (section 9).
3. **Few conversion paths.** Long recordings have no clear next step. I'm assuming the descriptions carry only a generic site link.

**Do this week, before any new upload.** All of it is in Studio and takes about 2-3 hours:

1. Open Studio → Analytics → Reach (traffic sources). If YouTube search is small and External or Notifications is large, the channel serves people who already know you. I expect that result.
2. Rank the 140 videos by watch time. For the top 10-15, add a tagged link to the description and a pinned comment. Both need advanced features; if your account doesn't have them, start verification now (section 5).
3. Leave weak videos up. One weak video doesn't hurt the channel [YouTube].
4. Move the webinars and talks into one playlist, "Webinars & talks", and keep them public. First check whether they convert elsewhere, such as in follow-up emails or embedded on pages. If they do, leave them alone.
5. Capture the baselines in section 9 and write them down.

## 3. Existence verdict

Ranked for Quarrystack (value per team hour, starting from your current state):

| Rank | Rung | Why |
|---|---|---|
| 1 | **Docs-embedded help videos** | Reach developers already mid-task, no audience needed, effect in days |
| 2 | **1-2 creator collaborations** | A borrowed audience that already trusts someone, effect in weeks |
| 3 | **Owned channel, search-led tutorials** | Compounding, but takes months |
| 4 | Owned channel, broad education | Biggest ceiling, most effort, a year or more |

**Recommendation:** keep the channel, but change its job.

- It becomes a **search-led Help library** for API-gateway problems.
- Embed those videos in the docs.
- Add a small creator test.

Opening a channel (or keeping one) is a standing job, so confirm someone can record narration for a year. Voice-only is fine.

- **If nobody can record:** drop the owned rung and run docs-embedded videos plus creators only.
- **If an in-house educator exists with a compounding mandate:** broad education moves up, as with PlanetScale and Tailscale [practitioner]. That's the highest-effort option, so I don't default to it.

## 4. Concept and pillar mix

| Concept | Mix | Trade-off |
|---|---|---|
| **A (recommended): Help-first** | Long-form at least two thirds Help; concept explainers; recordings archived | Slowest to show results, strongest compounding |
| B: Help plus monthly "what's new" series | Adds a Hub series | Feeds regular viewers but costs more effort; only after search growth |
| C: Archive the channel | Docs-embedded and creators only | Cheapest, gives up discovery |

I'm assuming A. Here is the pillar mix:

| Pillar | Hero/Hub/Help | Funnel job | Share of long-form |
|---|---|---|---|
| Error and how-to fixes, titled with the search phrase. Examples to test against search: "rate limiting per consumer", "JWT validation at the gateway", "mTLS to upstream", "canary release", "gateway 502/504 errors" | Help | Discovery, activation | at least 2/3 |
| Concept explainers (API gateway vs service mesh vs reverse proxy; when you need a gateway) | Help | Discovery | rest |
| Cut-down tutorials from each webinar and talk | Help | Discovery | counted in the above |
| Release videos ("v4.2 is out!") | Hero | Awareness spike | Stop as standalone videos. Put the content in the changelog and docs, as a short embed on the release page. |
| Webinar and talk recordings | none | Archive | One playlist, no promotion |
| Shorts | none | Reach | Only cut from long-form (section 6) |
| Hub series (build-along, "what's new") | Hub | Return visits | **Not yet.** Start after 3 months of month-over-month growth in search watch time |

Choose Help topics from support tickets, docs searches and sales-call questions. Check the phrasing against YouTube search suggestions and Studio's Research tab.

**Cheapest first batch:** you already have 140 videos, so you don't start from zero.

- Cut 6-10 search-shaped tutorials out of the best webinars and talks. Each takes a short clip plus a new title.
- Pair each with a written docs page. Coding agents and many developers read text, not video [practitioner: Convex].

## 5. Ownership, bench and cadence

**Ownership.**
- Check whether the channel sits on someone's personal Google account.
- If it does, move it to a Brand Account and add a company-administered Google account as Owner, plus a second owner.
- Start at least three weeks before anyone leaves, because of a 7-day wait.
- Wrong destination deletes the channel already there, and the moved channel loses its watch history, so export audience data first.
- Give staff permissions roles per person rather than sharing the password.

**Verification.** Request phone verification (lifts the 15-minute upload cap) and advanced features. Do this now; some creators can't get advanced features, so plan the launch to work without them.

**Bench.** Name one presenter and one backup who ships at least one video per quarter. Your engineers already give talks, so they are the obvious pool. The format and process must not depend on one person.

**Cadence, with my assumptions flagged.**

- **Capacity assumed:** 5 usable hours a week (about 6 minus 1 for comment replies), and about 10 team hours per finished Help video excluding editing.
- **Calculation:** (5 × 4) ÷ 10 = **2 videos a month**.
- **Check against editor capacity.** If the answer comes out under 1 a month, don't open the owned rung; use docs-embedded and creators.

If you have more hours, re-run this formula with real figures.

## 6. Shorts rule

Shorts come only from long-form, never the reverse.

- Point each Short's Related video at the long-form it came from.
- Don't put signup links in Shorts descriptions or comments. They aren't clickable [YouTube].
- Judge Shorts by the long-form views and tagged-link clicks they send, not by public views.

## 7. Engagement recipe

**Weeks -4 to 0**
- Fix ownership and verification, handle and profile links (up to 14), trailer.
- Set comment moderation and name a moderator.
- Build 6-10 Help videos before announcing anything. You already have the starting library.

**Weeks 1-12**
- Publish 2 a month. Reply to every comment in the first 48 hours.
- Use a Post poll only when you have a real question.
- Pin a comment with a tagged link on every long-form video. Template: *"Code and steps: [tagged link]. Stuck on [the step people ask about most]? Reply with your [error / version] and we answer here."*

**From week 8**
- A/B test titles and thumbnails on the oldest videos first. Winners are picked by watch time share, not click-through rate [YouTube].
- Start a Hub series only if search watch time has grown 3 months running.

**From week 12**
- Invite creators who already cover API gateways to a Collaboration (section 8). Never promote on their comments.

**Quarterly**
- Prune pillars by watch time per production hour.
- Refresh titles on decaying Help videos.

**Binding limits [YouTube]**
- Shorts links aren't clickable.
- Pinned comments, chapters, clickable long-form links and A/B tests need advanced features.
- A/B tests cover long-form only, up to 3 variants, up to 2 weeks.
- Paid promotion must be ticked and disclosed.
- Spam policy covers mass-produced similar videos, and 3 strikes in 90 days can terminate the channel.

**Do less:**
- Misleading titles and thumbnails.
- Changing a title or thumbnail that already works.
- Templated polls.

## 8. Creator plan (test, not a program)

1. Shortlist from Studio's "Channels your audience watches" and from creators your engineers already watch.
2. Screen on audience fit and engagement per view, not subscriber count. One vendor's floor is 5,000 views per video, with 0.002-0.005 comments per view as "good" [practitioner: PostHog].
3. Prefer a Collaboration or integration in the creator's own format over a pre-roll read. Repeat deals that work.
4. Brief 2-3 true points, each with proof. The creator writes the words. Disclosure and the paid-promotion tick go in the contract.
5. Put a tagged link in the top three description lines. Ask the creator to tell viewers to name them at signup.
6. Compare deals on cost per attributed signup, against the owned channel's cost per signup.
7. Avoid a long, visible single-vendor sponsorship with a reviewer who covers your category. Theo's Vercel deal ended publicly in 2024 amid audience distrust [practitioner].

Budget isn't known; start with 1-2 deals once the Help library exists. If you have budget but no spare hours, creators move first.

## 9. Metrics, baselines and stop rule

**Capture before any new upload (from Studio):**
- Monthly audience split (new, casual, regular).
- Traffic-source split, and YouTube-search watch time on pillar topics.
- Top 5 videos by watch time.
- Current monthly signups, with a count of how many carry a source.

**Outcome metrics**
- Signups from tagged links (long-form descriptions, pinned comments, creator videos).
- Signups naming YouTube or a creator in a "how did you hear about us" field. **Add that field first** if it doesn't exist. Until you do, the channel can't be judged, and leadership should hear that, not "zero".

**Channel health:** YouTube-search watch time on pillar topics; regular viewers in the monthly audience.

**Diagnostic:** intro retention and dips per video; A/B results; search share of traffic read beside absolute search watch time.

**Not outcomes:** subscribers, public views.

**Stop rule.** Review two quarters after month 3. If search watch time and attributed signups are both flat, fall back to docs-embedded videos and creators, and say so.

**What to tell leadership now:**
- The channel is mostly content nobody searches for.
- Signups aren't measured today.
- The plan is a search-led Help library, tagged links and a source field.
- A fair read of results is possible after two quarters.

## 10. Assumptions and open questions

Answer these and I'll rerun the numbers.

1. **Goal:** I assumed activation and discovery of developers searching gateway problems. Is it awareness, launch support, or retention?
2. **Audience:** I assumed platform and backend engineers evaluating gateways. What do they type when stuck?
3. **Account:** Is the channel on a personal Google account or a Brand Account? Do you have phone verification and advanced features?
4. **Studio data:** What are the traffic sources and the top 5 videos by watch time? My diagnosis assumes search is small.
5. **Bench:** How many hours a week can the presenter and backup give, who edits, and can anyone record narration for a year? I assumed 5 usable hours.
6. **Product demo:** Can the product be shown working in five minutes on a clean machine?
7. **Independent YouTubers:** Do any already cover Quarrystack or API gateways?
8. **Signup attribution:** Do you have tagged links, a "how did you hear" field, both, or neither? I assumed neither.
9. **Webinars:** Do they convert elsewhere (emails, embeds)? If they do, leave them where they are.

I read the skill and both of its reference files but didn't re-check the YouTube Help pages it names, since I had no browsing access. Before relying on a limit or metric definition, re-check the matching page listed in `references/platform-facts.md`.