# Brightloom YouTube plan: v2 launch and after

I read the skill and both references. I did not re-read the YouTube Help pages, so the limits below come from the skill's reference file and may have changed. You gave no answers to the interview, so I state an assumption for each gap. Correct any that are wrong and I'll re-rank.

## 1. Refusals triggered

- ❌ **Re-uploading the launch event as "the channel."** A full recording answers no search, so recommendations find it no audience. Keep it in one playlist and cut one tutorial from it.
- ❌ **Promising growth from upload frequency.** YouTube found growth is not correlated with time between uploads [YouTube]. The plan uses a cadence your team can sustain for a year.
- ❌ **Judging the channel by subscribers or public views.** Views now count from the first frame [YouTube], and subscribers are not viewers [YouTube]. The metric tiers in section 7 replace both.
- ❌ **Leaving the channel with one person.** Your advocate is great on camera, but they also own docs and the demo. PlanetScale's growth sat with one educator, who was later laid off [practitioner]. The plan adds a company-owned account and a backup presenter.
- ❌ **Putting signup links in Shorts.** Links in Shorts descriptions and comments are not clickable [YouTube].

## 2. Existence verdict

- **Library audit:** none, since there is no channel yet.
- **Verdict:** open a small owned channel, but don't treat it as the launch engine.
- **Standing job:** a channel needs a named human recording narration for about a year. If nobody can commit that, stay on docs-embedded videos and creators only.

Ranking of Menu 1 for you, with the answer that moved each rung:

| Rank | Rung | What moved it |
|---|---|---|
| 1 | Docs-embedded help videos | Cheapest per hour, and works in days. The advocate already owns docs. |
| 2 | 1-2 creator collaborations | The launch date is hard and cannot move. Creators are the only rung that lands within 6 weeks. They also cost cash and need a contract. |
| 3 | Owned channel, search-led tutorials | The advocate can record narration. Pays back over months, not launch weeks. |
| 4 | Owned channel, broad education | Needs a full-time educator. Not available. |

Broad education wins biggest (PlanetScale went from about 1,600 to 29,300 subscribers in 2023, Tailscale from 1,500 to 50,000 in 2.5 years [practitioner]). Both had dedicated presenters, and you don't. Revisit it only if you hire one.

Assumptions:

- The advocate can give about 5 hours a week to video.
- The product can be shown working in 5 minutes on a clean machine.
- "Launch event" means a live event, so the live-stream production belongs to `samber/developer-relations-skills@devrel-live-streaming`. This plan covers the VOD side.

## 3. Concept and pillars

Concepts considered:

- **A. Fix-it library (recommended).** Two thirds Help videos, one Hero video for v2, no series yet. It is cheapest per hour and compounds. It looks quiet at launch.
- **B. Fix-it plus a "what's new" Hub series.** Better return visits, but it adds recurring work the advocate lacks. A series should start only after search growth (below).
- **C. Edge observability explained.** Concept explainers with a personality. Highest brand upside, highest effort, and it starves the Help pillar.

I assume concept A, since you gave no pick.

| Pillar | Type | Funnel job | Share of long-form |
|---|---|---|---|
| Error and how-to fixes, titled with the search phrase | Help | Discovery, activation | at least two thirds |
| v2 flagship demo, cut from the launch demo the advocate builds anyway | Hero | Awareness spike | 1 video, then none until the next major release |
| Concept explainers | Help | Discovery | remainder, only when a fix video needs one |

Rules for choosing topics:

- **Source:** pick Help topics from support tickets, docs searches and sales-call questions. The searcher should be a user or evaluator.
- **Check demand:** validate each phrase against YouTube search suggestions, Studio's Research tab and `developer-keyword-research`.
- **Pair with a page:** give each Help video a written docs page. Coding agents and many developers read text, not video.
- **Example shapes, not claims:** "Why is my edge function slow? [cold start vs. upstream]" and "Trace a request across [your edge runtime]". Fill the slots with what Brightloom does today. Don't invent a feature.
- **Hold the Help share:** keep it at least two thirds of long-form until YouTube-search watch time has grown month over month for three months.
- **Series gate:** start a Hub series only after those three months, and never before.

## 4. Ownership, bench and cadence

**Ownership (new channel, so no transfer needed)**

- Create the channel on a Brand Account.
- Make a company-administered Google account the Owner, plus a second owner. Nobody's personal account owns it.
- Give the advocate Editor or Manager, and any agency or freelancer Editor (Limited).
- The Owner can't transfer ownership later, so get this right now.

**Bench**

- The advocate is the presenter.
- Name a backup who ships at least one video a quarter. Voice-only narration counts, and an engineer or the head of marketing could do it. This is an open question below.
- Write the series format down so a replacement could follow it.

**Cadence arithmetic (all inputs are my assumptions)**

- Advocate: 5 hours a week, minus 1 for comment replies, leaves 4 bench hours.
- A Help video takes about 6 team hours excluding editing: topic check, script, demo setup, record, and the paired docs page.
- (4 × 4) ÷ 6 = 2.67, rounded down to **2 videos a month**. Cap it by editor capacity.
- Below 1 video a month, drop to the docs-embedded and creator rungs only.

**Shorts rule**

- Ship zero Shorts at launch. They cost effort for reach, rarely signups.
- Later, cut them from long-form only, never the reverse.
- Each Short's Related video points at its source long-form.
- Judge Shorts on the long-form views they send, never on public views.

## 5. Engagement recipe, dated

Dates assume launch week of Dec 7, 2026 with the event around Dec 10. Replace them with the real date.

**Weeks -5 to 0 (Nov 2 to Dec 11): build before announcing**

1. **Week -5, Nov 2:**
   - Create the Brand Account, owners and roles.
   - Request phone verification now. It lifts the 15-minute upload cap.
   - Request advanced features (clickable description links, pinned comments, chapters, A/B tests). They need channel history or ID verification, which isn't available to every creator [YouTube].
   - Set the handle, the trailer and the profile links. Profile links (up to 14) are clickable [YouTube], so put the tagged signup link there.
   - Turn on comment moderation: held-for-review, blocked words, a named moderator.
   - Add a "how did you hear about us" field to signup, and create tagged links.
   - Pull the first Help topics from tickets.
2. **Weeks -4 to -1:**
   - Record one Help video, plus the Hero cut from the launch demo recording.
   - Add the same recordings to docs pages as embeds, which are the days-to-effect rung.
   - Plan the launch to work **without** advanced features. If they arrive late, there is no pinned comment or clickable description link. The docs-page embed and the profile link carry the traffic.
3. **Week 0:** publish the Hero video. Keep the event recording in one "Launch event" playlist. Don't promote it as the channel's content.
4. **Fallback:** the advocate is also building the launch demo and docs, and a 5-hour week may not fit three videos. The minimum viable plan is the Hero video, one Help video and the docs embeds. If the time can't be freed, cut the second Help video first.

**Weeks 1-12 (Dec 14 to about Mar 1)**

- Publish at 2 videos a month, with one before about Dec 18 and the rest from January. Seasonality is an external factor you can't control [YouTube].
- Reply to every comment within 48 hours.
- Post a poll only when you have a real question to ask, and vary it.
- Order playlists as a path, one per problem.

**From week 8:** A/B test titles and thumbnails on the oldest videos first, using the winner by watch time share [YouTube]. Don't change a title or thumbnail that already works [YouTube].

**From week 12:** invite creators who already cover your category to a Collaboration. Use Studio's "Channels your audience watches", which will have data by then. Never promote in their comment sections.

**Quarterly:** prune pillars by watch time per production hour. Refresh titles on decaying Help videos.

**Binding limits**

- Uploads stop at 15 minutes until phone verification.
- Clickable description links, pinned comments, chapters and A/B tests need advanced features.
- A/B tests cover long-form only, with up to 3 variants and up to 2 weeks.
- Paid promotion must be ticked and disclosed on sponsored content.
- The spam policy bans mass-produced similar videos, and 3 strikes in 90 days can terminate the channel.
- URLs spoken or shown on screen fall under the external links policy too.

For the pinned comment, creator outreach and creator brief, use `references/templates.md` and fill the slots with Brightloom's real facts.

## 6. Creator plan

A hard launch date promotes creators, so this runs in parallel from week -5.

1. **Shortlist 3-5.**
   - Start with edge, serverless and observability YouTubers your engineers already watch. You have no channel data yet, so "Channels your audience watches" can't help.
   - Screen on audience fit, views per video and comments per view, not subscribers.
   - One vendor's published floor is 5,000 views per video, with 0.002-0.005 comments per view as "good" [practitioner].
2. **Prefer a Collaboration or integration** in the creator's own format over a pre-roll read. Repeat deals that work.
3. **Give early access.** Offer v2 under embargo around week -4 so their video lands launch week.
4. **Brief 2-3 true points,** each with proof such as a docs page. The creator writes the words.
5. **Put disclosure in the contract,** plus the paid-promotion tick.
6. **Track the deal.** Put a tagged link in the top three description lines, and ask the creator to tell viewers to name them at signup.
7. **Compare deals on cost per attributed signup and cost per thousand views** against the owned channel's cost per signup.
8. **Avoid one long, visible single-vendor sponsorship** with a reviewer who covers your category. Theo's Vercel sponsorship ended publicly in 2024 amid audience distrust [practitioner].

Budget is unknown, so I can't size the deals. Reasonable scope is 1-2 deals before launch.

## 7. Metrics, baselines and stop rule

| Tier | Metric | Data source |
|---|---|---|
| Outcome | Signups from tagged links (profile link, docs embeds, creator videos) | Tagged-link analytics |
| Outcome | Signups naming YouTube or a creator | "How did you hear" field |
| Channel health | YouTube-search watch time on pillar topics | Studio |
| Channel health | Regular viewers in the monthly audience | Studio |
| Diagnostic | Intro retention and dips per video; A/B results; search share of traffic | Studio |
| **Not outcomes** | Subscribers, public views | n/a |

**Baselines**

- The owned channel starts at zero on everything. Record that before the first upload.
- If signups carry no source today, add the source field first. The channel can't be judged until it exists.
- Compare across the views redefinition (24 August 2026) with watch time, not view counts [YouTube].
- Set the search-watch-time baseline at month 3, about March 2027.

**Stop rule:** review two quarters after month 3, about September 2027. If search watch time and attributed signups are both flat, fall back to docs-embedded videos and creators, and say so.

## 8. Open questions

1. **Time:** who frees the advocate's 5 hours a week before launch, and what comes off their plate (docs scope)?
2. **Backup:** who ships one video a quarter if the advocate is out?
3. **Editing:** who edits, and what is their weekly capacity?
4. **Creator budget:** is there one, and what is the ceiling?
5. **Attribution:** can you count signups by source today, and can you add the "how did you hear" field this week?
6. **Event format:** is the launch event live, a Premiere, or in person? That decides how much falls under `devrel-live-streaming`.
7. **Existing mentions:** do any independent YouTubers already mention Brightloom or its category?
8. **Concept pick:** do you accept concept A, or do you want B or C?