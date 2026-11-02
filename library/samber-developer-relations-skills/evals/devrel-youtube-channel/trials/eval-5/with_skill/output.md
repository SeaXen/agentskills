# Kestrel Queue: YouTube creator plan for the half

## 0. Assumptions (one-pass request, so I filled the gaps)

| Gap | Assumption | Change it if |
|---|---|---|
| "This half" | 26 weeks from the week of Nov 2 2026 (to end of April 2027). Dates below are weeks, not calendar days. | Your half ends Dec 31. Then only wave 1 fits. |
| Goal | Activation: developers who evaluate a broker and sign up or download. | The goal is pure awareness. |
| Owned channel | None, and nobody has spare hours to record narration. | Someone can record weekly for a year. |
| Conversion event | A signup or download that you can tag with a link. | Only paid checkouts count. |
| Signup source today | Not counted. | You already have a source field. |
| Buyer | Backend and platform engineers choosing messaging infrastructure. | |

## 1. Refusals triggered

Two of the CMO's three choices hit the skill's refusal table.

1. **Declined: a 60-second pre-roll we write word for word.** Scripted reads lose the trust you are paying for [practitioner]. Replace it with a brief of 2-3 true points. The creator writes the words. We get one accuracy-only review round.
2. **Declined: a promo code as the measurement.** See section 6 for why it fails for an open-core broker. Use a tagged link plus a "how did you hear about us" field.
3. **Declined: the whole $40k on one creator.** One deal gives you no comparison and no repeat relationship. It also puts you in the "long, visible single-vendor sponsorship" trap [practitioner]. Theo's Vercel sponsorship ended publicly in 2024 amid audience distrust.
4. **Required, not a refusal: disclosure.** The paid-promotion box must be ticked and the sponsorship disclosed on camera [YouTube]. Local advertising law also applies.

## 2. Existence verdict

I ranked the skill's Menu 1 against your answers. Creators move to the top because you have budget and no stated spare hours.

1. **Creator collaborations or sponsorships.** Weeks to effect. They buy a borrowed, already-trusting audience, and that is what the board approved.
2. **Docs-embedded help videos.** Cheapest per hour, and they reach developers already mid-task. Add them later from creator footage and engineer time. They cost no fees.
3. **Owned channel, search-led tutorials.** Not this half. It needs someone to record narration for a year.
4. **Owned channel, broad education.** Not this half.

## 3. The CMO's pick: keep him as one test, not the plan

His size is not the problem. PostHog's handbook says larger creators "are often more efficient" [practitioner]. Fit is the problem. A general tech-news audience is mostly not people choosing a message broker. Subscribers are also not viewers [YouTube].

Run him through the same screen as everyone else:

- **Audience fit:** what share of his recent videos touch backend, infrastructure or data?
- **Engagement:** views per video, then comments and likes per view. One vendor's floor is 5,000 views per video, with 0.002-0.005 comments per view as "good" [practitioner].
- **Format:** will he do an integration in his own voice, not a scripted read?

He gets one slot, capped at 20% of the total ($8k). If his quote is above the cap, counter with an integration or hold him for wave 2. If he insists on a scripted read, skip him. Do not raise the cap.

What the CMO hears: "We keep your pick, but as one of four tests, with the same measurement as the others. If he wins, we put more money behind him in wave 2."

I have no rate data for any creator. The caps above are my proposal, not market prices. Quotes decide the real numbers.

## 4. Budget and timeline

| Tranche | Amount | Release | Use |
|---|---|---|---|
| Wave 1 | $14k (35%) | Weeks 5-10 | 4 deals, about $3.5k average. The CMO's pick takes at most $8k of the total, so the others are smaller or he gets deferred. |
| Wave 2 | $20k (50%) | Weeks 13-22, only after the week-12 gate | Repeat deals with the winners, or an extension. A recurring collaboration beats a one-off [practitioner]. |
| Holdback | $6k (15%) | Week 22 or later | Overruns, contract spillover, one late test. Unspent money returns to the board. |

| Weeks | Work | Done when |
|---|---|---|
| 0-2 | Set up attribution (section 6). Capture baselines. Build the shortlist. Align with the CMO. | Signups carry a source. Baselines are written down. 10-12 candidates screened. |
| 2-4 | Outreach with the template below. Collect quotes. Write contracts with disclosure terms. | 4 deals signed within the wave 1 budget. |
| 5-10 | Wave 1 videos go live. Reply to every comment on our own links within 48 hours. | 4 videos live, each with a tagged link. |
| 10-12 | Read results: cost per attributed signup and cost per thousand views per deal. | Gate decision written. |
| 13-22 | Wave 2: repeat the winners. Drop the losers. | 2-3 repeat deals or extensions. |
| 22-26 | Final read. Decide next half's rung. | One-page result for the board. |

## 5. How to pick creators

1. Open Studio's "Channels your audience watches" if you have an owned channel. If not, ask your engineers which YouTubers they watch for backend, infrastructure and event-driven topics.
2. Look for creators who already mention message brokers or your category. Check the last 10 videos for views, comments and likes.
3. Prefer a Collaboration or integration in the creator's own format over a pre-roll read.
4. Use [PostHog's practice](https://posthog.com/handbook) as a pattern [practitioner]: tagged link in the top three description lines, and creators ask viewers to name them at signup.

**Outreach (fill the slots, invent nothing):**

```
Subject: [their video title] + [message brokers / event-driven systems]

Hi [name], [one specific sentence about their video and what it taught your team].
We build Kestrel Queue, an open-core message broker. Would a Collaboration on [problem their audience has] fit your channel? You pick the format and the words; we bring [access, benchmark data, engineer time, budget]. Any paid version is disclosed and ticked as paid promotion.
[Your name], [role]
```

**Creator brief:**

- The viewer's problem, in one sentence.
- 2-3 true points about Kestrel Queue, each with proof you can share (a docs page or a benchmark you ran).
- The tagged link for the top three description lines, plus the line "tell us you came from [creator] at signup".
- Never say: [claims you cannot back], competitor comparisons you did not run.
- Disclosure: spoken, plus the paid-promotion box. One review round, for accuracy only.

## 6. Measurement

**Why the promo code fails for Kestrel Queue.** Open-core means developers can download and self-host for free. A code only measures people who reach a paid checkout and remember to use it. It misses everyone who evaluates first, which is most developers. Codes also leak onto coupon sites, so a code can count viewers who never watched.

**What to use instead:**

1. **A tagged link per creator**, in the top three description lines and a pinned comment. Pinned comments and clickable long-form links need advanced features [YouTube]. Confirm each creator has them.
2. **A "how did you hear about us" field at signup**, with YouTube and creator names as options. Do this first. Without it you cannot judge any deal.
3. **A promo code only as a third signal**, and only if you have a paid checkout. Never as the main measure.

**Metrics:**

| Tier | Metric | Data source |
|---|---|---|
| Outcome | Signups from tagged links per creator | Link analytics, product signup events |
| Outcome | Signups naming a creator in the source field | Signup form |
| Cost | Cost per attributed signup, cost per thousand views | Contracts, Studio-style view counts supplied by the creator |
| Diagnostic | Intro retention for the sponsored segment | Creator screenshot from Studio |
| Not outcomes | Public views, subscribers, promo-code redemptions alone | |

**Baselines to capture before wave 1:** signups per week, signups by source (if any), and your best current paid channel's cost per signup. That last number is the benchmark the gate compares against.

**Week-12 gate.** Compare each deal's cost per attributed signup to your best current paid channel's. Repeat the deals that beat it. Drop the rest. If no deal beats it, do not release wave 2 as planned. Say so and fall back to docs-embedded video and a smaller creator test. I set no numeric threshold because it must come from your baseline. Fill it at week 2.

## 7. What not to do

- Do not buy a pre-roll on his channel in week 1, before the attribution setup exists.
- Do not announce a channel or upload daily to "build an audience". It does not fit this half's resources.
- Do not put product links in other creators' comment sections. Each channel owner polices their own.
- Do not leave a sponsored video without the paid-promotion box ticked.

## 8. Open questions

1. What does "this half" mean in dates? That decides whether wave 2 fits.
2. What counts as a conversion for Kestrel Queue: signup, download, GitHub star, or a paid account? Is there any paid checkout?
3. Can you count signups by source today? If not, who adds the field, and by when?
4. What is your best current paid channel's cost per signup? The gate needs it.
5. Does the CMO's creator accept an integration instead of a read, and what is his quote?
6. Does anyone have spare hours for docs-embedded videos made from creator footage?
7. Which independent YouTubers already cover message brokers or your category?

If you send answers to 1, 2, 3 and 5, I'll fix the dates, the budget lines and the gate.