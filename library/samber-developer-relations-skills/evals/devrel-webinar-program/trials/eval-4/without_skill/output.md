**Recommendation: don't move the 14 videos behind a form. Gate nothing that teaches the first ingest. Capture leads inside the content, and gate only the extras.**

## Why the director's plan misfires

1. **The series' job is trial users reaching first ingest.** A registration form is friction placed before the content that causes that outcome. A hands-on query demo is most useful to someone mid-trial or evaluating, and that person will not fill a form for a replay.
2. **"Giving leads away" is a wrong premise.** Public YouTube views are not leads you owned. They are discovery. 14 videos at 2-9k views each are roughly 28-126k total views of free top-of-funnel for a product with a free tier. Gating them removes that traffic and collects a small share of it as emails.
3. **The "on-demand viewers are worth more" claim is unproven.**
   - Finishing a video is a correlation. Motivated people finish, and motivated people convert anyway.
   - Gating also filters out casual viewers, so completion rates rise for mechanical reasons.
   - The claim measures the wrong thing. The goal metric is first ingest, not completion.
   - Test it with your own data before acting on it (see Step 1).
4. **Gating costs search reach.** Gated video is not indexed on YouTube search or by AI assistants. Public transcripts and recordings are what get cited when someone asks how to do X in a time-series DB.
5. **A registration form breaks the funnel at the free tier.** Quartzline has a free cloud tier, so the product already captures the account. A second gate in front of education adds a step to a motion built to remove steps.

## Proposed replay policy

**Rule: replays are public by default. Capture identity through in-product and in-video paths, not a front-door form.**

1. **Keep all 14 existing videos public on YouTube.** Do not migrate them. Moving them also resets view counts and breaks existing links and embeds.
2. **Publish every new replay within 48 hours, public.** Include a chaptered description, a transcript or show notes on a Quartzline page, and the repo or sample dataset used.
3. **Put the conversion path in the content.**
   - Pinned comment and description: "Run this demo on the free tier" with a link to signup that prefills the demo dataset.
   - Spoken CTA at the point of the first ingest in each video, not the end.
   - A tagged UTM link per video so signups are attributable.
4. **Gate only high-intent extras, behind a light form.** Examples: the slide deck, the full notebook or query pack, a Q&A follow-up, a "Query Clinic office hours" invite, and the live-only session where attendees bring their own queries.
5. **Keep the live event registration.** Live registration already captures the lead, and live attendees can ask questions. The registration page should say the replay will be public, so the live room is a reason to attend, not a lead trap.
6. **Retarget instead of gating.** Build a YouTube viewer audience for ads or email to people who watched 50% or more. Those are the people who qualify as warm, with no form.

## What to measure (the goal is first ingest)

| Metric | Why |
|---|---|
| Signups per video (UTM) | Which episodes drive trials |
| Signup to first ingest rate, by source | The series' real job |
| Time to first ingest for replay-sourced signups | Whether the content shortens activation |
| Gated extras downloads | Captured intent, as a lead count |
| Watch-through of replays | Secondary; engagement only |

Vanity numbers (views, completion) do not decide anything here. Cost per first-ingest user is the decision metric.

## Step 1: test the director's claim before changing anything

About 2 hours of work, no risk:

1. Pull UTM or "how did you hear" signups from the last 90 days and group by source: live attendee, YouTube replay, other.
2. Compare signup-to-first-ingest rate across groups.
3. If replay-sourced users ingest at a meaningfully higher rate than live ones, his claim holds for them, but it argues for **more replay discovery**, not gating.
4. If the data is missing, that gap is the first fix. Add UTMs to the 14 descriptions this week.

## Step 2: pilot the gate on one new episode, if he insists

- Run next month's replay as an A/B: one public, one gated, with the same topic and promotion.
- Judge after 30 days on **first ingests per 1,000 viewers**, not form fills.
- Expect the gated version to collect more emails per viewer and fewer total viewers. The winner is whichever yields more first ingests.
- Do not touch the 14 existing videos in the pilot.

## How to put it to the director

- Agree with the goal: capture more value from the series.
- Reframe: "The leads are the trial signups, and the free tier already captures them. A gate adds a step before the content that produces first ingest."
- Offer the compromise: public replays, gated extras, tracked CTAs, and a 30-day A/B on one episode.

## Open question

1. Do you have signup source data tied to first-ingest events today? If not, that decides whether Step 1 takes 2 hours or a week.

**Next:** open YouTube Studio for the 14 videos and add a UTM signup link plus the free-tier CTA to each description (about 30 minutes).