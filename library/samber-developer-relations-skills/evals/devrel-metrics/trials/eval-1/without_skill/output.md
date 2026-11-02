# DevRel Monthly Report — Rebuilt

## 1. The answer to "what is any of this actually for?"

Say this first, in the email and in the hallway:

> Infrastructure gets evaluated hands-on, not through a sales call. DevRel owns the hands-on path. We turn our engineering credibility into three returns: **developers who deploy Meridian Stack** (the top of our pipeline), **a community that answers questions we'd otherwise pay engineers to answer**, and **product feedback no other channel gets**. Stars and impressions count who heard of us. The job is what they do next.

Your current report never gets to "what they do next" — that's why the VP's question stung and why you had no answer. The fix isn't new numbers bolted on; it's a report organized around returns instead of reach.

## 2. Why the current five can't answer it

| Current metric | What it actually is | The problem |
|---|---|---|
| 11,400 GitHub stars | A bookmark | Says nothing about whether anyone cloned or ran it this month |
| ~90k blog impressions | Eyeballs | No action attached, no denominator (impressions of what, doing what?) |
| 8,900 Twitter followers | Audience size | Inflates with any follow-back; measures popularity, not influence |
| 2.1M cumulative npm downloads | A counter | Cumulative metrics only go up — zero signal about this month; CI jobs pollute it |
| 9 conferences | A cost | An input reported as if it were a result |

Three structural flaws: every number measures **reach or spend, never response**; two are **cumulative** (unfalsifiable); none connects to a **dollar or a product decision**. Keep them — but demoted to an appendix, each paired with the metric that gives it meaning.

## 3. The new report: five questions leadership actually has

| Question | Metrics | Notes |
|---|---|---|
| **Are more developers adopting?** | • Activated developers: signed up **and** hit first success within 7 days (count + % of signups) • Weekly active developers (WAD) • New orgs represented | Activation, not registration. Orgs matter more than individuals — orgs become customers |
| **Do they stay?** | • 30-day retention of activated devs • Orgs with ≥3 weekly active devs • Repeat external contributors | Team depth (≥3) predicts expansion; single users churn silently |
| **Does it feed revenue?** | • PQLs created (DevRel-sourced/assisted) • Attributed pipeline $ • Signup source mix from "How did you hear about us?" | Directional attribution is fine at your scale — just say the method |
| **Does it save us money?** | • % of community questions answered by community • Median time-to-answer • Estimated deflected tickets × support cost | This is DevRel as capacity, and it's your counterweight in slow adoption months |
| **Does the product improve?** | • Feedback items logged → accepted into roadmap • External PRs merged • One named example per month | The feedback loop is real product work; name it or it didn't happen |

**North star: weekly active developers.** Downloads can be CI, stars can be hype, followers can be bought — a developer running our CLI/SDK every week cannot be faked. Second ticker: organizations with active developers, because that's what monetizes at an infrastructure company.

## 4. The email to send next month

```text
Subject: DevRel — October: what the work produced

Hi all,

Fair challenge last month: "what is any of this actually for?"

Short answer: infrastructure gets evaluated hands-on, not through sales calls.
DevRel owns the hands-on path. We turn engineering credibility into developers
who deploy Meridian Stack, a community that answers what we'd otherwise staff,
and product feedback no other channel gets. The old report showed how many
people heard of us. This one shows what they did next.

October is the baseline month — deltas and targets start with November.

HEADLINE
- Weekly active developers: [n] (first month instrumented)
- Activated developers: [n] — [n]% of signups reached first success within 7 days
- Organizations with active developers: [n] new, [n] total
- DevRel-attributed PQLs: [n] (method: self-reported source + tracked links)
- Community answers: [n] of [n] questions, median [n]h to first answer
- Product feedback: [n] items logged, [n] accepted into roadmap

WHAT WE LEARNED
- [e.g. Our talk at [event] drove [n] tracked signups in 30 days — $[n] per
  signup vs $[n] through paid search]
- [e.g. [n]% of new signups stall at quickstart step [n]; fix shipped [date],
  watching activation rate]
- [e.g. Community answered [n]% of questions with zero staff involvement —
  roughly [n] tickets deflected at $[n] each]

ASKS
- Engineering: emit one activation event (first successful [deploy/run]) — ~[n]h
- Sales: 30 min to lock the PQL definition and a source field in the CRM

APPENDIX — activity snapshot (the numbers you're used to, with their pairings)
Stars 11,400 (+[n] this month; [n] clones) · Blog [n]k impressions, [n]%
click-through to docs · Twitter 8,900 followers, [n]% engagement · npm [n]k
downloads/week (2.1M cumulative) · Conferences 9 YTD, [n] attributed activations

Definitions: Activated = signed up and reached first [success event] within
7 days. PQL = account with ≥[n] activated devs or ≥[n] usage. Attribution =
self-reported "how did you hear" + last-touch tracked links — directional,
not exact.
```

## 5. Instrument this before the send (4 weeks, mostly cheap)

1. **Define the activation event** with engineering and emit it — one event, roughly half a day. This is the single highest-value item; without it nothing else works.
2. **Add "How did you hear about Meridian Stack?"** to signup — free text, parse monthly. Self-reported attribution beats guessed attribution.
3. **Tag everything**: UTM convention for content, plus a short link per talk (`meridianstack.io/t/<event>`).
4. **Lock the PQL definition with sales** and add a DevRel source field in the CRM — one meeting.
5. **Switch npm reporting to weekly** via the registry stats API; retire the cumulative figure.
6. **Enable answered-flags** in the community channel; export stats monthly.
7. **Track cost per event** (travel + time) in the same sheet as attributed signups.

## 6. Rules that keep it credible

- **Never report a cumulative number again.** Monthly deltas and weekly rates only.
- **State the attribution method every time.** Directional honesty now beats false precision exposed later.
- **Footnote-define every metric.** Numbers leadership can't challenge are numbers they ignore.
- **One page**: six numbers, three insights, asks. The appendix absorbs the legacy five so nobody accuses you of hiding them.
- **Don't promise targets this month.** Baseline in October, targets in November — a report built on made-up historicals dies on first inspection.

## 7. What the report buys you once it has two months of data

- **Conference decisions**: rank events by cost per attributed activation; cut or renegotiate the bottom quartile. Your biggest line item becomes your most defensible cut.
- **Budget defense**: cost per activated developer vs paid-acquisition CAC — the "is DevRel worth it" question answered with arithmetic instead of vibes.
- **Product pull-through**: quickstart drop-off data is something the product team will start asking *you* for. That's the strongest possible answer to what any of this is for.