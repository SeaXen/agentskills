**Verdict: don't put most of $60k into 15-article agency sprint. Wrong lever, wrong timeframe. Kill it as primary bet.**

## Why this fails as stated

Two facts contradict each other in your plan:

1. Signups already healthy → top-of-funnel not bottleneck. More articles = more people into same leaky funnel. Doesn't fix leak, dilutes ratio.
2. 10 weeks to board meeting. SEO content takes 3–6 months to rank. Agency-rushed 15 articles in 10 weeks won't index, won't rank, won't move any number CEO checks at board meeting. Board sees "$40k spent, zero traceable lift" — worse than not spending it.

Real problem you named yourself: **80% of signups never run second build.** That's activation, not awareness. Fix that, not top-of-funnel.

## The activation lever — cheapest, fastest win

Quillard = build-cache service. Second build IS the aha moment (cache hit, visible speedup). If quickstart only makes user run build once, they never see product's actual value. Fix:

1. **Rewrite quickstart to run build twice inside the tutorial itself.** Second run shows cache-hit speedup live, in the 5-minute window, not as a separate re-engagement problem. "Do, don't show" — don't explain caching, make them feel it.
2. **Add post-build CLI/dashboard message**: "First build: 42s. Run again — cache should cut this to ~4s." Prompt exact command to copy-paste.
3. **Email/in-app nudge for stalled users**: signed up, ran first build, no second build in 24h → send exact re-run command, not generic "come back" copy.
4. **CI templates (GitHub Actions/GitLab CI) that build twice automatically** — cache hit shows in CI logs on run #2 with zero user effort. Ship as copy-paste starter configs.

Items 1–2 cost near-zero — docs + CLI copy change. This is your highest-leverage, lowest-cost move. Ship week 1–2, before spending big money on anything else.

## Budget — $60k over 10 weeks

- **$8k** — instrumentation: define + track `second_build_started` event, cohort dashboard (signup week × % reaching 2nd build within 7 days). Contractor or analytics help if you lack the SQL/dashboard time yourself.
- **$5k** — quickstart + docs rewrite, CLI messaging copy, CI starter templates. Mostly your time; small technical-writer/design contractor budget for polish.
- **$8k** — lifecycle nudge sequence (stalled-user emails) — ESP setup/copy if you don't have one wired.
- **$30k** — content agency, **scope changed**: 5–6 deep pieces, not 15 shallow ones. Target bottom-funnel + activation-adjacent topics: per-CI-platform integration guides, cache-miss troubleshooting, "why is my build not caching" diagnostic content, competitor-alternative comparisons. These serve people already trying to succeed with the product (higher intent, faster to rank — less competitive than generic thought-leadership) and double as onboarding reinforcement.
- **$9k** — buffer/experiments (A/B variants on onboarding copy, incentive for the few pieces that need paid distribution or design assets).

Reject "$60k → agency" as one line item. Split it — most of it still goes toward measurable activation work, not content volume.

## 10-week roadmap

1. **Week 1** — Ship event tracking. Pull baseline: current 2nd-build rate by signup cohort, by source.
2. **Week 2** — Ship quickstart rewrite (build-twice) + CLI post-build message. Brief agency on redefined 5–6 topics.
3. **Weeks 3–4** — Ship stalled-user nudge sequence. First agency drafts in review.
4. **Weeks 5–8** — Run 2–3 short experiments on onboarding (copy variants, nudge timing). Watch weekly cohort dashboard. Publish agency pieces as they clear review — stagger, don't dump all 6 at once.
5. **Week 9** — Compile results: baseline vs current 2nd-build rate, chart with intervention dates marked (quickstart ship date, nudge ship date) so lift traces to specific actions, not vibes.
6. **Week 10** — Board narrative + rehearsal.

## What to show the board

Lead with **activation rate, week-over-week, annotated with what shipped when.** Not pageviews, not "15 articles published," not follower counts — CEO will correctly dismiss those as vanity. If you can, tie activation lift to a downstream number finance already tracks (trial-to-paid rate, expansion) — even directional correlation beats a clean but meaningless content-output metric.

State content investment honestly: these 5–6 pieces are a **seed for Q1 compounding traffic**, not this quarter's proof point. Don't oversell ranking timelines you can't hit — a board that catches one inflated claim discounts the rest of the report.

## Risks

- Quickstart/CLI changes need engineering time you don't control. Ask your eng partner for it **this week** — 20–30 hours, not a project. If refused, that's a real blocker, surface it now, not week 8.
- Baseline unknown until week 1 data lands — don't promise a specific target percentage before then. Set the number after baseline, aim for a defensible relative lift (e.g., +8–10 points), not a guess stated today.

## Next action

Today: message your eng partner, ask for the quickstart/CLI change + one event-tracking hook. That single ask determines whether weeks 1–2 above are even possible.