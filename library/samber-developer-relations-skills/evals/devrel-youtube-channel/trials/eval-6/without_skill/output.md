# Pylonmesh YouTube approach

**Recommendation: don't run the docs-to-video pipeline at 30 videos a month. Ship about 8 to 10 real-screen videos a month, voiced by your two docs engineers, and use automation only for drafting and packaging.**

I haven't seen your docs analytics, support tickets or channel stats, so the numbers below are assumptions to check, not measurements.

## Why the current plan fails

- **The audience is hostile to it.** Service mesh viewers are platform and SRE engineers deciding whether to trust a data plane with production traffic. A synthetic voice over stock code visuals signals that nobody ran the thing. Viewers will leave in the first 30 seconds.
- **Docs pages aren't video scripts.** A page is organized for scanning, while a video is organized in time. Most of the 400 pages are reference material (config fields, CRD schemas, CLI flags), and nobody watches a video of a reference page. A video-worthy page has one task and a visible result.
- **Stock visuals prove nothing.** A mesh video has to show a real cluster: traffic shifting, an mTLS handshake failing, a policy denying a request. Stock code visuals can't carry that.
- **Channel-level risk.** YouTube's policy on mass-produced, repetitive content has tightened. I'm working from memory and haven't re-checked it, so verify the current wording. Uploading 30 templated videos a month is the pattern that policy targets. Low retention on a large share of uploads can also drag down recommendations for your better videos.
- **Volume isn't the constraint.** For developer content, one video that fixes a specific error is worth more than ten generic ones, because people find it by search for years.

## What to do instead

### Format mix (about 8 to 10 uploads a month)

| Format | Per month | Who | Effort |
|---|---|---|---|
| Error/fix video (1–3 min): the exact error text on screen, cause in one sentence, then the fix | 3–4 | Any engineer, voiceover or captions | About 1 hour each |
| Task walkthrough or build-along (6–12 min): from the finished result, one path, real cluster | 2 | The two docs engineers, voiceover only | About 1 week each, mostly the demo environment |
| Release clip (30–90 s) per release | 1–2 | Docs engineer | About 1 hour |
| Concept explainer (3–8 min), e.g. how mTLS identity works or why a sidecar proxy adds latency | 1 | Docs engineer plus a diagram | Diagram work first, then recording |
| Shorts cut from the above | 4–6 | Anyone | Minutes |

The engineers never need to be on camera. A voiceover over a real terminal, dashboard and diagrams is enough. The "couple of narrated videos a month" they offered covers the two walkthroughs. Error/fix and release clips need very little time from them.

### Picking which pages become videos

Don't convert pages in order. Rank candidates by these signals and take the top few each month:

1. **Support tickets and Slack/Discord questions.** Repeated errors become error/fix videos.
2. **Docs search queries and top-visited pages.** Demand is already visible.
3. **Quickstart, install and first-success paths.** Evaluators need these most.
4. **Migration and upgrade pages**, which are high-pain and high-search.
5. **Skip reference pages.** Link them in the description instead.

A page qualifies only if it passes this test: "For this viewer, this video shows one specific thing working." If it needs an "and", it's two videos. Expect roughly 40 to 60 of the 400 pages to qualify, which is about 5 to 6 months of backlog.

### Where AI and automation do help

Keep the automation, but move it away from the voice and visuals:

- **Draft the beat-by-beat script from the docs page.** An engineer edits it, and the engineer's edit is the quality gate.
- **Run the docs commands on a clean cluster** (for example in CI on a throwaway kind cluster) before recording. This catches stale docs and gives each video a reproducible starting state.
- **Generate packaging:** chapter lists, descriptions, caption correction, titles built from search wording, and the companion docs link.
- **Cut shorts** from finished long videos.
- **Optionally, synthetic voice for localized dubs** of videos that already work in English. Start this after the channel has proven traction, and put it behind a human review.

### Rules for the engineers' time

- Budget about 2 to 3 hours per error/fix or release clip, and about 2 to 3 days per walkthrough including environment setup. Check this against their real load before committing.
- Keep one demo repo with scripted cluster setups that each video starts from. This lets any video be re-shot alone, and the repo doubles as the companion link.
- Write narration for the ear. Say what's happening, not "as you can see here", so the transcript works as a standalone page.
- Put terminal text at 24pt or larger and editor text at 20pt or larger. Check it on a phone.
- Keep customer names, cluster hostnames and tokens off screen.

## How to pitch it to the growth lead

Reframe the goal. The growth lead wants coverage of the docs and a steady publishing cadence. You can offer both:

- **Coverage:** every video links to its docs page, and the docs page embeds the video. That's the docs-to-video link, without converting every page.
- **Cadence:** 2 to 3 uploads a week including shorts, which looks consistent without becoming mass production.
- **Reach:** error/fix and walkthrough titles built from real search phrasing capture search traffic the docs alone don't get.

## 90-day plan

1. **Weeks 1–2:** pull the top 20 candidate topics from tickets and docs search. Build the demo repo and cluster scripts. Record 3 error/fix videos as a pilot.
2. **Weeks 3–6:** first 2 walkthroughs by the docs engineers. Add 1 release clip. Start Shorts.
3. **Weeks 7–12:** add the first concept explainer. Review the metrics. Decide what to scale.

## How to measure it

Compare each metric against your own earlier videos of the same format, not against outside benchmarks:

- **Retention after 30 seconds**, per format. This grades the opening.
- **Average percentage viewed**, per format.
- **Search-sourced views** on error/fix videos over 90 days. This is the main compounding signal.
- **Docs link clicks** from descriptions, and the next action (quickstart started, repo cloned).
- **Takes per recording.** More than a few takes on one beat means the starting state is wrong.

**Scale or stop rule:** if after 90 days the error/fix videos aren't pulling search views and the walkthroughs hold viewers past the first third, fix the format before adding volume. Only raise the volume once one format has clearly compounding views. Then add capacity (an editor or a third narrator) rather than synthetic output.

## Open questions

- What is the real engineer time budget per month? I assumed 2 to 3 days per walkthrough.
- Is there an existing YouTube channel with history, or is this a new one?
- Does anyone besides the two docs engineers (support, solutions, community) know the product well enough to do error/fix videos?
- Is the goal mostly evaluation (new adopters) or retention (existing users)? It changes the mix toward walkthroughs or release clips.