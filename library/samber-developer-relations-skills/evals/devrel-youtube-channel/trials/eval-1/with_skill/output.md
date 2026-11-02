# Tidewire YouTube channel plan

**Bottom line for your CEO:** run a Help-first, search-led channel at 3 long-form videos a month, with 3–6 Shorts cut from them. Replace the 10,000-subscriber goal with signups from tagged links and YouTube-search watch time. Daily posting would need about 8× your hours.

Assumptions (the interview skipped, since you asked for one pass):
- You can record narration, on camera or voice only.
- The channel is on a personal Google account.
- You can't yet count signups by source.
- The product can be shown working in 5 minutes.
- Q2 means April to June 2027, so the deadline is 30 June 2027, about 8 months away.
- A finished video takes about 8 team hours, excluding editing.
- The editor handles 3 or more videos a month.

I couldn't see your Studio data, so the library diagnosis below is a procedure for you to run, not a result. Please check each assumption.

## 1. Moves I'm declining

| CEO's ask | Why it fails | Instead |
|---|---|---|
| Post daily "because the algorithm rewards consistency" | YouTube found growth "not correlated with time between uploads" [YouTube]. It does list an unusual drop in uploads as a reason for lower recommendation traffic [YouTube]. | Keep the same cadence for a year. That is the true part of his claim. |
| 5 Shorts a week as a standalone feed | Mass-producing near-identical videos breaks the spam policy [YouTube]. Short-form helps awareness more than signups [practitioner, PostHog]. | Shorts cut from long-form (section 5). |
| 10,000 subscribers as the goal | Subscribers are not viewers [YouTube]. From 24 Aug 2026 public views count from the first frame of play [YouTube], so view counts no longer compare with earlier history. | The metric tiers in section 8. |

Daily posting also fails on capacity (section 4).

## 2. Library diagnosis (do this first, about 2 hours)

You have 640 subscribers, so a channel exists. In Studio:
1. **Traffic sources.** Little YouTube-search watch time with high External and Notifications means the channel serves people who already know you, not new searchers.
2. **Top 5 videos by watch time.** Add a tagged signup link to each description and a pinned comment now, before any new upload. Both need advanced features (section 4).
3. **Decaying Help-type videos.** Retitle them with the phrase people search. Leave weak videos up, because one weak video doesn't hurt the channel [YouTube].
4. **Webinars and talks.** Ask whether they convert elsewhere, for example in emails. If not, move them to one playlist and keep them public.
5. **Signup source.** If signups carry no source, add a "how did you hear about us" field and tagged links first. Until then the channel can't be judged.

## 3. Existence verdict and ranking

| Rank | Rung | Payoff | Time to effect |
|---|---|---|---|
| 1 | Docs-embedded help videos | Compounding | Days |
| 2 | 1–2 creator collaborations | One-shot per video; compounding if repeated | Weeks |
| 3 | Owned channel, search-led tutorials | Compounding | Months |
| 4 | Owned channel, broad education | Compounding | A year or more |

**Recommendation:** keep the owned channel, search-led, and reuse every Help video in the docs. The channel is a standing job, so it needs someone able to record narration for a year. That is you plus a named backup.

What moved the ranking:
- Having someone who can record promotes the owned channel from "open when someone can record" to "run it".
- With one DevRel, broad education stays last. PlanetScale grew from about 1,600 to 29,300 subscribers in 2023, but with an in-house educator and broad database topics [practitioner]. Tailscale grew from 1,500 to 50,000 in 2.5 years [practitioner]. Neither fits 8 hours a week.
- No hard launch date, so creators don't move first.

## 4. Concept, ownership, bench and cadence

**Concept options:**
- **A. Help-first library (recommended).** Fix videos titled with the search phrase, plus concept explainers. This is the fastest compounding route at your effort level.
- **B. Help plus an early "what's new" series.** It returns viewers but costs more per video, so it waits for the search gate.
- **C. Postgres-internals education.** It chases subscribers and brand, but it costs a year or more and you lack the hours.

**Pillar mix for A, per month (3 long-form videos):**

| Pillar | Videos | Funnel job |
|---|---|---|
| Error and how-to fixes (Help) | 2 | Discovery, activation |
| Concept explainer (Help) | 1 | Discovery |
| Hub series, customer stories, launch pieces | 0 for now | Added after the search gate (section 7) |

- Long-form stays at least two thirds Help until YouTube-search watch time has grown month over month for three months.
- Pick topics from support tickets, docs searches and sales-call questions. Check the phrasing against YouTube search suggestions and Studio's Research tab [YouTube].
- Pair each video with a written page. Many developers, and coding agents, read text, not video.
- Topic types to verify against your own tickets: replication slot lag, WAL growth, schema change handling, initial snapshot, ordering and delivery guarantees. I haven't seen your tickets, so treat these as hypotheses.

**Cadence math:**
- Bench: 8 h/week minus about 1 h for comment replies = 7 h × 4 = 28 h a month.
- 28 ÷ 8 h per video = 3.5, rounded down to **3 videos a month**.
- Sensitivity: 6 h per video gives 4 a month, and 10 h gives 2.
- Daily would be 30 videos × 8 h = 240 h a month, about 60 h a week, or **about 8.5× your bench**. Even at 3 h per video it is 90 h, over 3× your bench.
- Daily plus 5 Shorts a week fails the same way.

**Ownership:**
- Confirm the account type. If it is a personal Google account, move it to a Brand Account using the ownership route [YouTube]:
  1. Export audience data first, because the move loses watch history and creator demographic info.
  2. Opt out of channel permissions, then invite a company-administered Google account as Owner, plus a second owner.
  3. Wait 7 days, then make the company account primary owner. Deleting the primary owner's account deletes the channel.
  4. Remove personal access and opt back into channel permissions.
- Give the editor the Editor (Limited) role, or Editor if revenue visibility is fine.
- Request phone verification and advanced features now. Without phone verification, uploads cap at 15 minutes. Advanced features are needed for clickable long-form links, pinned comments, chapters and A/B tests, and aren't available to every channel [YouTube].
- **Backup:** name an engineer or solutions person who ships at least one video a quarter. PlanetScale's growth sat with one educator who was later laid off [practitioner]. You are that risk.

## 5. Shorts rule

- Cut Shorts from long-form, never the reverse.
- Make 1–2 per long-form, so **3–6 a month**, not 20. Seven near-identical clips per video risks the spam policy.
- Each Short's Related video points at its source long-form.
  - URLs in Short descriptions and comments aren't clickable [YouTube].
  - The last spoken and on-screen line is: "Full fix, with the [edge case], is the [topic] video. Tap the related video link on this Short."
- Judge Shorts on the long-form views they send, or on the long-form's tagged link. Never judge them on public views.

## 6. Engagement recipe and dated cadence

**Surfaces:** long-form videos, problem-ordered playlists, chapters, end screens and cards to the next video, channel trailer and profile links, pinned comment with a tagged link, replies in your own comments, Shorts with the Related video link, and occasional polls.

**Do more:** titles and thumbnails that match the content; A/B tests (the winner is picked by watch time share); series that send viewers back to older episodes [YouTube].

**Do less:** misleading titles or thumbnails, repetitive templated polls, "check out my channel" comments elsewhere, and changing a title or thumbnail that already works [YouTube].

**Calendar:**

| Dates | Work |
|---|---|
| Mon 2 Nov to Sun 29 Nov 2026 (weeks −4 to 0) | Library audit, ownership route, verification requests, baselines (section 8), trailer, profile links, comment moderation (held-for-review, blocked words, a named moderator). Bank about 3 Help videos, which is four weeks of cadence. Retag old videos. |
| Mon 30 Nov 2026 to Sun 21 Feb 2027 (weeks 1–12) | Publish 3 a month. Reply to every comment within 48 hours. Post a poll only when you have a real question, and vary it. |
| From Mon 18 Jan 2027 (week 8) | A/B test titles and thumbnails, oldest videos first. |
| From Mon 15 Feb 2027 (week 12) | Invite creators who already cover your category to a Collaboration. |
| About 1 Mar 2027 (month 3) | Set the search-watch-time baseline and decide the Hub series (section 7). |
| Quarterly | Prune pillars by watch time per production hour. Refresh titles on decaying Help videos. |

Because you have an existing channel, skip the launch announcement. Starting a Hub series needs three months of search growth first [YouTube].

**Binding limits:**
- URLs in Shorts descriptions and comments aren't clickable. Each Short gets one Related video link.
- Uploads cap at 15 minutes until phone verification.
- Clickable long-form links, pinned comments, chapters and A/B tests need advanced features.
- A/B tests are long-form only, up to 3 variants, up to 2 weeks.
- Paid-promotion tick and local-law disclosure are required on sponsored content.
- Spam policy: 3 strikes in 90 days can terminate the channel.
- A daily upload cap exists but its number is unpublished, so stagger any back-catalogue upload.
- Other creators' comment sections are policed by their owners, so never leave product links there.

**Templates (fill the slots with real facts):**
- Pinned comment: `Code and steps: [tagged link]. Stuck on [step people ask about most]? Reply with your [error / version] and we answer here.`
- Reply to criticism: `Fair point on [specific criticism]. [What is true]. [Workaround or issue link]. [If fixed later: we'll pin the update here.]`

## 7. Creator plan

- Start with **1–2 deals**, budget permitting. I don't know your budget.
- Shortlist from Studio's "Channels your audience watches" and from creators your engineers already watch.
- Screen on audience fit, views per video, and comments and likes per view, not subscribers.
  - One vendor's published floor is 5,000 views per video, with 0.002–0.005 comments per view as "good" [practitioner, PostHog].
- Prefer a Collaboration or integration in the creator's format over a pre-roll read. Repeat deals that work.
- Brief 2–3 true points with proof. The creator writes the words. Disclosure and the paid-promotion tick are contract terms.
- Put a tagged link in the top three description lines. Ask the creator to tell viewers to name them at signup.
- Compare deals on cost per attributed signup and cost per thousand views, against the owned channel's cost per signup.
- Avoid a long, visible single-vendor sponsorship of a reviewer who covers your category. Theo's Vercel sponsorship ended publicly in 2024 amid audience distrust [practitioner].

## 8. Metrics, baselines and stop rule

Capture all baselines **before the first new upload**.

| Tier | Metric | Data source |
|---|---|---|
| Outcome | Signups from tagged links (long-form, pinned comments, creator videos) | Signup source field plus link tags |
| Outcome | Signups naming YouTube or a creator in "how did you hear" | Signup form |
| Health | YouTube-search watch time on pillar topics | Studio traffic sources |
| Health | Regular viewers in the monthly audience | Studio Audience tab |
| Diagnostic | Intro retention and dips per video, A/B results, search share of traffic next to absolute search watch time | Studio retention and A/B reports |
| Not outcomes | Subscribers, public views | Tracked, not targeted |

**Baselines to capture:**
- The 640 subscribers.
- The monthly audience split (new, casual, regular).
- Traffic sources and top 5 videos by watch time.
- Signups per month by source.

**Targets:** I won't invent numbers. Set the signup and search-watch-time targets at about 1 Mar 2027 from the first three months of data. Until then the goal is: search watch time grows month over month for three months, and every signup is attributable.

**On the 10,000 subscribers:**
- Reaching it needs about 9,360 net subscribers in about 8 months, roughly 1,170 a month. That is 15× the channel's current total, in a niche audience, at 3 videos a month.
- The only comparable growth I found is broad-education programs with dedicated people [practitioner]. Subscribers are not viewers [YouTube].
- Ask him what 10,000 would buy: signups, credibility, or sales conversations. Then pick the metric that measures that.

**Stop rule:**
- Review two quarters after month 3, about early September 2027.
- If search watch time and attributed signups are both flat, fall back to the docs-embedded and creator rungs, and say so.
- That review lands after his 30 June deadline. Agree this with him now, so Q2 isn't judged on subscribers.

## 9. Open questions for you

1. Is the channel on a personal Google account or a Brand Account? This sets how urgent the ownership move is.
2. What do the Studio audit numbers show: traffic sources, audience split, top 5 videos?
3. Who is the backup presenter?
4. How many videos a month can the contractor edit, and at what cost?
5. Is there a creator budget?
6. What does a finished video really cost you in hours? If it is 6 h you can do 4 a month, and if 10 h only 2.
7. Does Q2 mean the calendar quarter or a fiscal one?
8. Is there any signup source tracking today?