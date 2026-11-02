Read the skill and all three references (`metric-catalog.md`, `attribution-methods.md`, `measurement-plan-template.md`). Following it below — including its routing rules, its interview assumptions, and its pass-threshold check.

---

# Kestrel Logic — DevRel measurement work

## Routing first (the skill requires naming who owns what)

| Your four items | Owner |
| --- | --- |
| Discord dead-or-not | `developer-community-health` for the deep treatment; one row lives in this framework |
| UTM mess + GitHub vs analytics disagreement | `devrel-analytics` for the taxonomy; this framework decides *which* number each source is allowed to own |
| $40k DevRelCon booth return | `developer-event-sponsorship` for the full ROI treatment; this framework supplies the attribution rule it must run on |
| What the CTO gets quarterly | **This skill. This is the deliverable.** |

Answer to "where do we start": the CTO question, because it is the only one of the four that is a *decision*. The other three are measurements with no owner, no rule, and no baseline — they become tractable the moment the framework says what each is for.

## Interview answers I had to assume (confirm these — each can move the sheet)

1. **Funded driver: developer adoption** — developers embed Kestrel on their own; commercial licensing/support follows company-led. If the CTO would say "pipeline" first instead, business impact gets promoted to primary.
2. **Reader: the CTO.** Budget sits on an engineering/product line, not sales. Decision she makes: renew / move headcount / kill a channel.
3. **No instrumented success event exists** (embedded DB, likely no accounts, maybe no telemetry). Flagged below as the one engineering ask.
4. **Data on hand:** GitHub traffic panel, a web analytics tool, Discord, some CRM or trial/license request flow.
5. **Small team, few engineering days.**

## Spine (brainstorm mode — three options, pick before anything else is detailed)

- **Driver-anchored** — one primary metric per funded goal. Legible to a CTO in one glance; direct line from metric to budget. Hides where developers leak. Wrong pick if the top question becomes "where do we lose them."
- **Journey-stage** — one metric per drop-off point. Best for leak diagnosis; gives up the budget line. Wrong for a first quarterly report.
- **Function-split** — one number per person. Wrong for a team of one or two; encourages metric fiefdoms.

**Recommendation: driver-anchored.** The reader is an exec reading quarterly, not a funnel analyst. Revisit journey-stage once quickstart step instrumentation exists.

---

# The framework document

## 1. Driver and goals

**Funded driver:** developer adoption — "more engineers embed Kestrel and succeed at it." Owner: CTO.

Goals this horizon (three, one primary each):

1. Raise the share of new developers who reach a working embed.
2. Deepen usage — first success must become real, repeated use.
3. Keep an honest, rule-bound read on whether events and community touch the commercial business.

## 2. Metric sheet

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
| --- | --- | ----- | ---------- | ------ | -------- | --------- | ----- | ------------------ |
| 1 **P** | First-success rate, 7 days | Enablement | share of new installs whose app completes a first write-then-read round trip with Kestrel within 7 days of first install | opt-in telemetry event `first_write_read` — **does not exist yet; one engineering ask** | baselining | set after 3 periods (baseline) | DevRel lead | cold-run the quickstart on a clean machine; fix the top failure before shipping new content |
| 2 | Quickstart step drop-off | Enablement | share abandoning at each documented quickstart step | docs analytics + sample-repo runs — ratios inside one source only | baselining | set at next review (baseline) | DevRel lead | fix the single worst-named step |
| 3 **P** | Second-project rate, 90 days | Product impact | share of first-success developers initializing Kestrel in a second distinct app within 90 days | telemetry | baselining | set after 3 periods (baseline) | DevRel lead | interview five one-project developers before proposing anything |
| 4 | Community questions by non-staff, monthly | Engagement | questions opened by non-staff in Discord + repo issues, with share answered by non-staff | Discord export + forge API; needs a staff/bot flag | baselining (pull 12 weeks now) | below own trailing 12-week median, 2 months running (baseline) | DevRel lead | channel-mix review; if answers fall, add staff coverage or office hours |
| 5 | Unique cloners + registry downloads, monthly | Engagement | period counts, snapshot monthly — GitHub traffic keeps only 14 days | GitHub traffic panel + registry stats | baselining | set after 3 periods (baseline) | DevRel lead | read alongside row 1; falling downloads with stable success rate = discovery problem, not product |
| 6 | Self-reported first touch | Engagement | one question, stable option list, free-text box — on the trial form and a docs survey | signup/trial form | baselining | response rate below 40% (hypothesis — circulating figure, not measured) | DevRel lead | shorten or reposition the question |
| 7 **P** | Influenced pipeline | Business impact | see attribution rule; **reported, not targeted, first two quarters** | CRM + touch log — needs sales-ops cooperation | €0 (rule new) | none — baselining | CTO + DevRel lead | none yet; if sales ops won't cooperate, delete this row and name it in blind spots |
| 8 | Friction findings + verbatims | Qualitative | quotes and cold-run findings with source, date, fix shipped, confidence tag | manual log | 0 | fewer than 2 per quarter (baseline) | DevRel lead | schedule two developer conversations |

Cut outright: **2,100 Discord members** (monotonic stock — cannot fall when you stop working, carries no information), total stars, cumulative downloads, all-time impressions, event count.

## 3. Attribution rule

- **Standing instrument: self-reported first touch** (row 6), reported as "self-reported," never as attribution. Option list includes "a conference, meetup or workshop" — this is the only method that can see your booth at all.
- **Tagged links: artifact comparison only, never program totals.** The taxonomy cleanup is `devrel-analytics`' job; the rule here is one tag per campaign, never reused.
- **Influenced pipeline:** an opportunity is DevRel-influenced when, in the 180 days before it reached stage 2, a contact on the account (a) had a conversation logged by the team, (b) attended a program event, (c) had a question answered by the team in a public venue, or (d) named a program surface as first touch. Influenced value is **always shared credit** — Marketing may claim the same opportunities; "sourced" is a banned word. Rule fixed for the fiscal year; any change is an announced restatement.
- **Rule written before the period starts.** A rule invented after the quarter is a narrative — this is what sank the March booth answer (below).

## 4. Reporting

- Monthly, one page: rows 1-6 against baseline, to the DevRel + product team.
- Quarterly to the CTO: full sheet + qualitative evidence + the five-sentence summary.
- Annually: re-derive from the driver; expect half the sheet to change.
- **Snapshot GitHub traffic monthly, starting today** — the panel keeps 14 days; a metric defined today is otherwise uncomputable for last quarter.

Five-sentence summary the CTO can repeat without you:

> New developers get a working Kestrel embed within a week X% of the time, and we are moving that number. Of those who succeed, Y% start a second project within 90 days — the signal the first one was real. Community health is non-staff questions per month and how many get answers, not member count. Events and community appear in commercial pipeline as *influenced*, never sourced, under a written rule fixed for the year. Everything else we publish is an input to those numbers, not a result.

## 5. Known blind spots

- No `first_write_read` telemetry → the primary metric is an engineering request until shipped (~2 days, via `devrel-analytics`).
- No identity link Discord ↔ CRM account → community-to-expansion unmeasurable; needs an identity map, ~2 engineering days plus a privacy review.
- Docs readers who never install; AI assistants answering from docs without a visit.
- March's pre-period was never recorded → that booth's lift is permanently unclaimable. Only counts remain.
- Client-side analytics under-counts developers badly (Plausible measured 58% of a tech audience blocking GA, Aug 2021, on their own HN/Reddit-heavy traffic) → absolute sessions never appear on this sheet.

## 6. Review

Next quarterly decision read: January 2027. Baselining cycle runs now through then; thresholds set at that review. **Kill rule:** any metric that has not changed a decision in two consecutive cycles is removed — stated here so removal is scheduled, not argued.

---

# The other three, answered honestly

## Is the Discord actually dead?

2,100 members answers nothing — it's a stock. The dead-or-not test is four rates against your **own trailing baseline** (never another community's numbers):

1. Non-staff messages/questions per week, 12-week trend — declining trend is the real "dead."
2. Share of questions that get *any* human answer, and share answered by non-staff (organic answers are the health signal; staff-only answers = a support channel, not a community).
3. Median time to first human response vs your own trailing median. The "24-hour standard" is folklore — if anyone quotes it, label it a hypothesis under test.
4. Percent of members active in 30 days — compare to your own history only; the "20% monthly-active" figure is also folklore.

Two guardrails: separate burst from trend (a launch or March booth spike is not a baseline), and pair any message-volume target with the organic-answer share or you incentivize chatter. Pull the 12 weeks of history **now** — chat venues keep whatever the plan allows, and the baseline rots. Full treatment (contributor funnel, sentiment) → `developer-community-health`.

## Why GitHub and your analytics tool disagree — and why they never will

The disagreement is structural, not a bug you can fix:

- The GitHub traffic panel retains **14 days** and counts cloners its way; your analytics tool counts sessions its way. Different windows, different units.
- Your analytics tool misses most of your audience at the script level: ~58% of a tech audience blocks client-side analytics (Plausible's own measurement, August 2021), and referrer stripping (aggregators, chat clients, privacy browsers) dumps a large "direct" bucket that is *normal*, not a tracking failure.

So the rule is: **never reconcile, never average, never compare absolutes across sources.** One source per metric — docs funnel ratios from the analytics tool, repo adoption from GitHub/registry — and the source is written into the sheet's Source column. The UTM taxonomy itself (naming convention, one campaign per tag, never reused) → `devrel-analytics`. And remember tagged links only ever *compare artifacts* — which landing page, which post — never program totals.

## What the $40k March booth returned

The honest answer has three parts, because the rule wasn't written before the event and a retroactive rule is a narrative:

1. **What cannot be claimed:** lift or ROI. No pre-period was recorded, no qualified-conversation bar was defined in advance, and the UTMs were unreliable. That's gone, permanently.
2. **What can be counted now (descriptively, to finance):** any logged booth conversations or badge scans that exist; opportunities created since March whose account contacts attended DevRelCon — presented as "conversations that later appeared in pipeline," with shared credit, never as return; and $40k ÷ however many conversations you can reconstruct = cost per conversation, the only comparable figure. Enterprise cycles put real pipeline answers two to four quarters out from March, so Q3-Q4 is when even the influenced view exists.
3. **What changes for the next event:** pre-register the rule — the qualified-conversation definition agreed *before* the event ("has the problem, influences the decision, agreed to a next step"), a dedicated short URL, the destination's pre-period recorded, and every conversation logged to the CRM within a week. Full treatment → `developer-event-sponsorship`.

---

# First two weeks

1. Confirm the driver and the reader with the CTO — everything above re-ranks if she says "pipeline" rather than "adoption."
2. Today: **start the monthly GitHub traffic snapshot** — that data is actively expiring (14-day window).
3. Pull 12 weeks of Discord history; compute the four dead-or-not rates.
4. Deploy the one-question self-reported first touch on the trial form.
5. File the engineering ask: the opt-in `first_write_read` event.
6. Hand the UTM taxonomy to `devrel-analytics`; adopt the one-tag-per-campaign rule meanwhile.
7. Write the attribution rule into the framework before the quarter turns; pre-register the next event's rule.

# Pass-threshold check (reported explicitly, per the skill)

- 8 metrics, 3 primaries, one per goal: ✅
- All six fields on every row (baselines explicitly marked "baselining" — no history exists yet): ✅
- Product-impact (row 3) and business-impact (row 7) present: ✅
- No monotonic metric as primary; members/stars/cumulative counts cut by name: ✅
- Every row carries a named action; incentivized volumes paired with counter-metrics (messages → organic answer share; conversations → pre-agreed quality bar; downloads → second-project rate): ✅
- Attribution rule written, methods and 180-day lookback named, "influenced" wherever credit is shared: ✅
- Every threshold tagged `baseline` or `hypothesis`; no folklore number presented as a target: ✅
- Blind-spots section non-empty: ✅

One flag: the sheet stores nothing in memory yet, per the skill — the driver, thresholds, and attribution rule get recorded only once you and the CTO validate them. The assumptions in the second section are the first thing to check.