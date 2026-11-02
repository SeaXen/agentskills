**Next action (2 min):** Check whether your thank-you email and recordings link have gone out. If not, send them today. Everything else below can wait.

I loaded `events`, `youtube-devrel`, `hackathon-sponsorship` and `developer-ecosystem-strategy`. For the other skills named here I only had their one-line descriptions, so confirm each fits before you rely on it. I didn't read anything under `skill-wip/`.

## 1. Sequence after the conference

Don't skip the survey. Make it short instead. "People are tired of forms" argues against a 20-question form. It doesn't argue against a 3-question one. The survey is also your only source for edition-6 decisions that isn't sponsor opinion or guesswork.

| # | When | Action | Skill |
|---|------|--------|-------|
| 1 | Now (the 24-48h window may be closing) | Thank-you email with the recordings link. No ask in it. | `events` |
| 2 | Within 3 days | Sponsor reports (reach, leads, session views), sent before sponsors start renewal talks | `events`, `developer-event-sponsorship` |
| 3 | Within 5 days | Micro-survey, 3-5 questions, under 2 minutes (see below) | `devrel-metrics`, `devrel-analytics` |
| 4 | Week 1-2 | Publish the recordings with transcripts and chapters. This feeds item 2. | `events`, `youtube-devrel` |
| 5 | Week 2-3 | Pull the attendance data you already have: scans, session views, talk ratings, repeat attendees | `devrel-analytics` |
| 6 | Week 3-4 | Retro, then edition-6 go/no-go and sponsor renewal pitch | `devrel-metrics`, `devrel-budget-allocation` |

Micro-survey shape:
- Make every question optional except one: "Would you attend edition 6?"
- Ask about the biggest thing to fix and which talk mattered most.
- Ask "how did you hear about us?" in free text. The `attribution` skill treats self-reported attribution as the honest signal.
- Deliver it by QR code or a link in the thank-you email. Don't use a separate form email.
- Offer a reward only if you can deliver it fast.

Skipping the survey and leaning on behavioral data is a fair fallback. Do it only if step 5 actually yields attendee-level data. Without that data, you'd be deciding edition 6 blind.

## 2. Dead YouTube channel plus the docs push

These are two projects. Don't merge them.

### 2a. YouTube channel revival

You already have the content backlog: all talks from edition 5 were recorded. That makes revival a publishing job, not a creation job.

1. `youtube-devrel` for titles, thumbnails, chapters and the posting cadence.
2. `events` (Content Arc section) for slicing each recording into clips, recap posts and quotes.
3. `technical-video-script` for any new explainer videos beyond the talks.
4. `devrel-content-calendar` to spread 40-ish talks over months instead of dumping them in one week.
5. `docs-seo` or `developer-keyword-research` for titles that match what people actually search.

Order matters here. Publish the best 5 talks first, on a weekly schedule. Then see what the numbers say.

Why the channel died is unknown, and the answer changes the plan. If it died because nobody owned it, publishing talks won't fix that.

### 2b. Developer content and docs push for the OSS tooling

The tooling is a different audience from the conference audience. This is a docs and onboarding project that happens to share a brand.

1. `developer-docs-structure-audit` to diagnose what exists before writing anything.
2. `developer-quickstart-guide` and `docs-code-sample-standards` for the entry path.
3. `developer-tutorial` for step-by-step content.
4. `docs-as-marketing` and `docs-seo` for discoverability.
5. `oss-contributor-onboarding` for the community-contribution side.

Later, as needed: `readme-optimization`, `developer-education-strategy`, `oss-distribution-strategy`, `developer-community-health`.

Sequence: audit, then quickstart, then tutorials. Run it as a project in parallel with 2a, with its own owner. Don't let it block the talk publishing.

## 3. Hackathon on the sponsor's public API

It isn't a platform question. A platform question (`developer-ecosystem-strategy`, then `developer-platform-skills`) applies when you decide to open your own product surfaces to outside builders. In this hackathon, outsiders build against the sponsor's API, not yours. The sponsor owns the platform decisions. You own the event.

Skill routing:
1. `events` (hosting) for format, audience, and the before/during/after arc.
2. `hackathon-sponsorship`, read as the host. It is written from the sponsor's side, so flip its advice: what the sponsor should get, and what to require of them.
3. `developer-live-demo-design` for demo and judging sessions.
4. `developer-event-sponsorship` and `oss-sponsors-brand-strategy` for the sponsor relationship and what you promise them.
5. `developer-champions` and `developer-community-health` for keeping participants engaged afterward.

Things to settle with the sponsor before you design anything:
- API readiness. Sandbox keys, rate limits for 1,400 people (or however many hack), and a named engineer on call.
- Judging criteria and prize ownership.
- Participant data sharing and consent. Their follow-up needs consent, so decide it up front.
- Whether your OSS tooling is part of the hackathon. If yes, the item 2b docs push is a prerequisite, so time it.

The hackathon can come last. Edition 6 is the target, so you have room.

## Three questions that change the plan

1. What date was the conference exactly, and is the thank-you email already out?
2. Who owns the YouTube channel and the docs push, and how many hours a week do they have?
3. Is the OSS tooling part of the hackathon, or separate from it?