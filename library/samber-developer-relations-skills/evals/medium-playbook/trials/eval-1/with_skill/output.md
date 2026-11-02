# Driftwave on Medium: 12-week plan

I read `medium-playbook/SKILL.md` and both reference files. I changed the plan's core mechanic because the playbook marks it as spam or no-reach. The changes and the reasons are in the first section. Labels follow the playbook: **[platform]** means Medium states it, **[practitioner]** means writer reports, and **(own reasoning)** is mine.

## 1. What I changed and why

| Original plan | Problem | Replacement |
|---|---|---|
| 300-word summary ending "Read the full post on driftwave.io" | A story clipped to send readers to your site is a teaser, which is spam [platform]. | Import the full post with a canonical link home. |
| 3 posts a week, same format | Templated near-duplicates are spam [platform]. A story posted primarily to drive traffic or rankings to your site is removed without notice [platform]. | About 1 story every 1–2 weeks. |
| Intern generates summaries with Claude | Majority-AI text with little editing gets no General distribution and no Boost, labelled or not, and can't be paywalled [platform]. | Humans write or import. AI may help with grammar, outline and fact-check, which needs no label. Heavier AI help needs a label in the first two paragraphs. |
| A brand account called "Driftwave" | Boost rewards a writer's first-hand experience, which a brand account can't show [platform]. Signup-first stories get Network distribution only [platform]. | Named engineers publish, and a company publication collects the stories. The brand account carries release notes only. |
| Medium's domain authority gives page-1 rankings in days | Medium withholds new or untrusted accounts from search indexing for days to weeks [platform]. | No ranking target. Measure referral sessions and signups, read on your own analytics. |
| It costs nothing | A company publication needs a paid membership [platform], and engineers' time isn't free. | Budget one paid membership on a company-controlled account, plus the hours below. |

Two limits on the backlink goal:
- Imported stories carry a canonical link to driftwave.io. Medium's own copy is therefore not the page you are trying to rank.
- I can't verify the backlink or rankings payoff from the playbook. It makes no such claim, so treat both as unproven (own reasoning).

## 2. Assumptions

You gave no answers to the playbook's interview, so I assumed these. Correct any that are wrong and I'll re-rank the plan.

| Interview question | Assumption | Effect |
|---|---|---|
| Who writes? | 2–3 named Driftwave engineers, plus one marketer running the publication | Publication, not a brand-only account |
| Goal and date | Standing channel through Q1, with signups as the success signal | Compounding rungs ranked up |
| Where originals live | driftwave.io blog, English, canonical URLs | Canonical import is the default rung |
| Hours per week | Marketer 3 h, each engineer about 1 h on average, 1 native story per quarter per engineer | Fits the cadence below |
| Who answers responses within two days? | The marketer, with engineer backup | Assigned in the cadence |
| One-off or compounding | Compounding | Native deep-dives get promoted from week 4 |

If hours drop under 2 a week, keep canonical import and responses only.

## 3. Fit verdict: Syndicate first, upgrade to Invest

- **Now:** syndicate only. The content lives on the company blog, and imports go under named authors with no paywall.
- **Upgrade to Invest** once you have a real incident, migration or benchmark story and an engineer to own it (planned for week 4). That is also when imports should have drawn followers.
- **Skip Medium** if the blog is mostly product announcements or AI-generated drafts. Those get followers-only reach at best [platform].

## 4. Account model and retention agreement

1. **Named engineers** publish under their own accounts [platform].
2. **Company publication:** "Driftwave Engineering". A company-controlled account with a paid membership owns it, never an engineer's personal account [platform: creating one needs membership; one user owns up to 7].
3. **Retention agreement**, signed before the first import. Put it in employment or IP terms, not as a publication condition.
   - Engineers may import company posts.
   - Canonicals stay on driftwave.io.
   - On departure, stories stay up, free and in the publication.
   - Editors may not delete a story or remove it from the paywall without the writer [platform].
   - Never require outside writers to grant republishing rights to submit [platform].
4. **Brand account** "Driftwave": release notes only, written to be useful without the product link, with followers-only reach expected.
5. **Canonical home** stays driftwave.io. Don't point a Medium custom domain at the blog. Medium can redirect custom-domain URLs to medium.com, as Towards Data Science reported in 2025 [practitioner].

## 5. Ranked surfaces and what moved

Ranked by value per hour:

| # | Surface | Payoff | Value | Low effort |
|---|---|---|---|---|
| 1 | Canonical import, named author, company publication | compounding | ++ | +++ |
| 2 | Substantive responses in your topics (earn-first) | compounding | + | +++ |
| 3 | Company publication, featured credit used weekly | compounding | ++ | ++ |
| 4 | Submission to an established tech publication | one-shot | ++ | + |
| 5 | Native first-hand deep-dive (Boost candidate) | compounding | +++ | − |
| 6 | Publication newsletter | compounding | + | ++ |
| 7 | Brand-account release note | one-shot | − | ++ |

- **Compounding goal:** promotes the native deep-dive from last place to a week-4 start.
- **Hours under 2 a week:** would demote everything except #1 and #2.
- **Your original plan** sits at the bottom of the compliance ladder: an AI-generated, traffic-first teaser is the worst-ranked compliance cost.
- **No paid amplification exists.** Medium sells no ads, and bought traffic harms a publication's standing [platform].

## 6. Publication setup

**Settings for "Driftwave Engineering":**
- Mode: Approved writers only.
- Story type: accept published stories, so engineers import under their own names first.
- Conditions: image and subtitle required; leave "paywalled" off.
- Link a guidelines page (template in section 9).

**Target external publications**, in order of fit. Pick by topic fit first, then by whether the rules allow your call to action.
- **Level Up Coding:** active, about 300k followers [practitioner: early 2026 list by a rival network's owner]. The guide I have is older (email a draft link). Re-read its current rules before pitching.
- **ITNEXT:** publishing on Medium in 2026. Read its current guidelines.
- **In Plain English network** (including JavaScript in Plain English, Stackademic): allows a call to action at the end for a newsletter, free service or open-source project [practitioner: its write-for-us page]. Paid services and sponsored content go through its paid marketplace. Never buy a sponsored slot inside a Medium publication, because third-party advertising is banned [platform].
- **Skip:** Towards Data Science (left Medium 2025-02-03) and Better Programming (reported closed).

Ask the editor before mentioning a paid plan or trial. A free tier or open-source repo usually reads as acceptable. An established publication may require an original, so write a native story for it rather than importing.

## 7. 12-week cadence

Owners: **M** = marketer, **E** = named engineer(s).

| Week | Work | Owner | Hours |
|---|---|---|---|
| 1 | Create the paid-membership company account and the publication, with settings and guidelines page. Complete all profiles. Sign the retention agreement. Audit the blog: tag each post pass/fail on the strip-the-product test (if nothing worth reading remains without the product name, it fails). Pick 3 passing posts and one native-story candidate. Follow target topics. | M, E | M 3, E 0.5 each |
| 2 | Earn first: each writer leaves a few substantive responses a week in target topics, no links (a self-set pace, not a platform rule). Import post #1 under its author and run the canonical check. | M, E | M 3, E 1 |
| 3 | Import posts #2 and #3, a few days apart, each under its named author. If none pass the test, start the native story instead. Feature the strongest story. | M, E | M 3, E 1 |
| 4 | Feature one story. Answer responses within two days. Engineer starts the native deep-dive (incident/migration/benchmark). Set baselines for the metrics in section 10. | M, E | M 3, E 3 |
| 5 | Native draft and review. Import post #4 if it passes. Feature one story. | M, E | M 3, E 3 |
| 6 | Publish the native story. Submit one original story to an established publication, with the editor pitch and CTA question. | M, E | M 3, E 2 |
| 7 | One story (import or native). Feature the strongest. Answer responses. | M | M 3, E 1 |
| 8 | First diagnosis pass (section 8). Monthly review: drop topics that drew no presentations. | M | M 3 |
| 9 | One story. Send the publication newsletter on publish (opted-in addresses only). | M, E | M 3, E 1 |
| 10 | Second native story kickoff if the incident supply exists. Otherwise import #5. | E | M 3, E 3 |
| 11 | Publish. Feature. Optionally submit to a second established publication that fits. | M, E | M 3, E 2 |
| 12 | Quarter review against baselines. Decide: invest more, stay syndicate-only, or stop (section 11). | M | M 3 |

**Volume:** about 8–10 full stories in 12 weeks, versus 36 in the original plan. Never re-post an unlisted story, and never put the same story in two publications [platform].

**Weekly, every week:** feature one story (credits start at 4, refill one per 7 days, cap 4; featured stories are reviewed for Boost first [platform]), answer responses within two days, and remove spam responses on your stories. Leave critical ones up and answer them.

## 8. Diagnosing a story nobody reads

1. Compare presentations with writer plus publication followers. Presentations at or below that suggest Network-only distribution, a signal rather than proof (own reasoning). Confirm with the traffic-source split; stories from before 2025 show no presentations [platform]. Then check:
   - product framing
   - AI-generated text
   - a missing AI label
   - off-topic topics
   - mass mentions
   - non-English text
2. Presentations high, views low: fix the title, subtitle and cover.
3. Views high, reads low: the opening fails its promise. The read ratio counts reads of 30 s or more over views [platform].
4. Rewrite the next story. Leave this one up.

## 9. Filled templates

**Offsite link disclosure**, placed right next to the link [platform]:
> Try Driftwave free for 14 days (this link leaves Medium). `{use the real trial terms}`

**Affiliation line**, in the first paragraph:
> I work on Driftwave, the observability tool this post uses; the limits section covers where it falls short.

**AI assistance label**, within the first two paragraphs, only if AI did more than grammar, outline or fact-check:
> This story was written with the assistance of an AI writing program; the measurements were run and checked by me.

**Earn-first response** (no link, adds a usable fact):
```text
We saw the same cardinality blow-up on high-label metrics once tenants
passed {N}. Dropping {label} at ingest cut storage by {X}%. Did you try
that before sampling traces?
```

**Native story skeleton** (Boost candidate):
1. The incident or decision, in the first paragraph, with one number.
2. What you tried first and why it failed.
3. What you changed, with code blocks and a diagram you made.
4. Results, measured, and what still does not work.
5. One call to action at the end: the repo, the docs page, or the free tier.

Title: what happened and to what. Subtitle: the result. Cover: your own diagram or none.

**Pitch to a publication editor**, through its own channel:
```text
Subject: Submission - "{title}"

Hi {editor name},

I'm an engineer at Driftwave. This draft covers {incident}: {one
sentence of what happened}. About {N} words, {N} diagrams, original to
your publication.

It names our product once, in the closing paragraph, with a link to
{free tier or repo}. Happy to drop that line if it breaks your
guidelines.

Draft: {Medium draft link}
{name}
```

**Company publication guidelines page:**
```text
Write for Driftwave Engineering

Who: Driftwave engineers and invited partners. Partners keep all
rights to their stories; submitting grants us nothing extra.
What: incidents, migrations, benchmarks, architecture decisions,
told by the person who did the work.
Not: product announcements (they go on the Driftwave brand account),
sponsored content, AI-written drafts.
How: publish on your own account, canonical link to the driftwave.io
URL if it ran there first, then Submit to publication.
Paywall: off.
Topics: up to 5, each one the story is about.
AI: no AI-generated drafts; label AI assistance within the first
two paragraphs.
```

**Canonical check before every publish:**
1. Story settings > More settings > Advanced settings shows the original URL.
2. The published page source contains `rel="canonical"` pointing at driftwave.io.
3. Paywall off, topics chosen, AI label present when needed.
4. Submitted to the company publication, and featured if it's the week's best.

Import with Stories > Import a story. If the importer fails, paste and set the canonical by hand; only the story's author can set it [platform]. Run every draft through your humanizer skill.

## 10. Metrics

Targets are self-set; Medium publishes no vendor benchmark. Record baselines in week 4.

- Presentations, feed click-through, reads, read ratio, followers gained per story.
- Referral sessions and signups from UTM-tagged links to the canonical page, read in your own analytics. Medium allows no tracking scripts [platform].
- Boost badges per quarter.
- Each author's third-party AI setting stays on the default "Prioritize maximum reach" [platform].
- **Hygiene, pass threshold zero:** AI-generated or unlabelled stories, teasers, duplicates, paid placements.

## 11. Week-12 decision rule

The thresholds below are my suggestion, not the playbook's. Set the numbers at week 4.

- **Invest more:** UTM referral signups are non-zero and rising, and at least one native story earned presentations well above follower count.
- **Stay syndicate-only:** imports draw some reads but natives don't materialise.
- **Stop:** presentations stay at or below follower count with zero signups, and you've fixed every hygiene item.

## 12. Questions that could change the plan

1. Are the Driftwave blog posts human-written? If AI-generated, they fail the import test too.
2. Do you have 2–3 engineers who'll put their names on stories? Without them, skip Medium (section 3).
3. How many hours a week can the marketer actually give? Under 2 changes the cadence (section 2).