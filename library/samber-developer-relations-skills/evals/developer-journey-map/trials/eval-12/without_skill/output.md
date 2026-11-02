# Sableworks DevRel — Journey Map, Quickstart Rewrite, KPI Framework

One throughline connects all three: your team owns every developer-facing surface (docs, dashboard, SDK, community), so the journey map names the owner per stage, the quickstart is written to be shippable by three people, and the KPI framework only commits you to what three people can actually move.

---

## 1. Developer Journey Map — Backend Engineer @ Scale-Up → Production Usage

**Segment:** backend engineer, 50–500 engineer org, currently running self-hosted RabbitMQ/Kafka or a homegrown SQS wrapper. End state = sustained production traffic, not "sent a test message."

| # | Stage | Trigger / Entry | What they're trying to answer | Owned touchpoint | Exit signal |
|---|-------|-----------------|-------------------------------|-------------------|-------------|
| 0 | Problem recognition | Incident, sharding pain, ops-burden mandate ("stop self-hosting queues") | "Is there a managed option that doesn't lock me in?" | none (pre-funnel) | Opens a search tab |
| 1 | Discovery | Search, HN/Reddit mention, competitor blog comparison | "Does this replace what I have?" | Docs SEO, comparison content, community mentions | Clicks into docs or signup |
| 2 | Evaluation | Reads docs, checks SDK repo activity, lurks in Discord/Slack | "Is this actively maintained? Will I get support?" | Docs (reference + explanation pages), SDK repo signals, community lurk experience | Creates account |
| 3 | Signup / sandbox | Lands in empty dashboard | "What do I do first?" | Dashboard empty state, signup flow | Reaches quickstart |
| 4 | **Activation (aha moment)** | Runs quickstart | "Does this actually work?" | Docs (quickstart), SDK (must work first try), Dashboard (live trace view) | Sees message delivered in the dashboard trace — this is the peak moment, engineer this deliberately |
| 5 | Real integration (staging) | Wires SDK into an actual service | "How do I handle retries, ordering, DLQs?" | How-to guides, SDK ergonomics, dashboard queue config | Staging service runs real (non-toy) volume unattended for 24h+ |
| 6 | Internal buy-in | Needs sign-off from staff eng/EM | "What's the SLA? What does this cost at our volume? Who else our size runs this?" | Docs (architecture, security/SOC2 page), community (case studies, peer proof) | Internal approval to cut over |
| 7 | **Production cutover — END STATE** | First real workload live | "Will I get paged for someone else's outage?" | Dashboard (alerting, throughput, runbooks), docs (production readiness checklist), community (support escalation path) | 7 consecutive days live, no rollback |
| 8 | Expansion (beyond end state, worth tracking) | Confidence established | "What else can I move here?" | Community (champion program), docs (advanced guides) | Second topic or team onboarded within 90 days of stage 7 |

**Friction points that kill conversion, by stage** (use these as your backlog, ranked by where drop-off compounds):
- Stage 2: docs answer "how" but not "is this dead?" — unanswered community questions past 72h read as an abandoned project to an evaluator.
- Stage 3: any required field beyond email + one action before the first real step (Hick's Law — every extra decision costs conversion).
- Stage 4: broken copy-paste code or no visible proof of delivery. This is the single highest-leverage fix available — it's 100% docs+SDK, zero dependency on product.
- Stage 5: ambiguous delivery/ordering guarantees force a support ticket instead of a doc read — every one of those tickets is a stage-5 drop-off you didn't see in analytics.
- Stage 6: no production-readiness checklist means the engineer has to construct their own pitch to their EM — give them the slide, don't make them build it.
- Stage 7: alerting gaps here don't just block cutover, they cause a rollback after cutover, which resets the engineer to stage 5 with a worse opinion of you than before they started.

Industry baseline to calibrate expectations against (not Sableworks-specific — pull your own numbers before committing targets): 40–60% of new signups abandon after one session, 75–80% within day one. If your stage 3→4 drop looks better than that without instrumentation to back it up, distrust the number before you present it.

---

## 2. Quickstart Rewrite

### Current-page problems this fixes
- No visible proof of success — reads as "trust me it worked," not "watch it happen."
- Config before payoff — API key + queue setup is presented before the developer has seen any output.
- Single-language example with no cURL fallback, so evaluators who don't want to touch Node.js bounce.
- No connection back to the dashboard, so the free "wow" moment of a live trace view goes unused.

### Rewritten page

```markdown
# Send your first message

Publish and receive a message in under 5 minutes. No queue setup required —
your first publish creates one automatically.

## Prerequisites

- Node.js 18+ (or curl, if you just want to see it work first)
- A Sableworks API key → [grab one free, no card required](/signup)

## 1. Install the SDK

```bash
npm install @sableworks/sdk
```

## 2. Publish a message

Create `publish.ts`:

```typescript
import { Sableworks } from "@sableworks/sdk";

const client = new Sableworks({ apiKey: process.env.SABLEWORKS_API_KEY });

await client.publish("orders.created", {
  orderId: "ord_1",
  amount: 4200,
});

console.log("Published to orders.created");
```

```bash
npx tsx publish.ts
```

Prefer curl?

```bash
curl -X POST https://api.sableworks.dev/v1/topics/orders.created/messages \
  -H "Authorization: Bearer $SABLEWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"orderId": "ord_1", "amount": 4200}'
```

## 3. Consume it

```typescript
import { Sableworks } from "@sableworks/sdk";

const client = new Sableworks({ apiKey: process.env.SABLEWORKS_API_KEY });

for await (const message of client.subscribe("orders.created")) {
  console.log("Received:", message.body);
  await message.ack();
}
```

```bash
npx tsx subscribe.ts
```

You should see `Received: { orderId: 'ord_1', amount: 4200 }` within a second.

## 4. Watch it happen

Open your [dashboard's live trace view](https://app.sableworks.dev/trace) —
you'll see the message you just sent travel from producer to topic to
consumer, with delivery latency. This view is the same one you'll use in
production to debug a stuck message at 2am, so it's worth learning now
while nothing is on fire.

## What you built

`orders.created` is a durable topic — messages persist until every
subscribed consumer group acknowledges them, so a consumer that's down for
five minutes doesn't lose anything. You didn't configure retention,
partitioning, or delivery guarantees; Sableworks applies safe production
defaults on auto-created topics, and every one of them is a one-line change
later.

## Next steps

- **Going to production?** Read the [production readiness checklist](/docs/production-readiness) — retries, dead-letter queues, alerting, and the questions your team lead will ask.
- **Wiring this into a real service?** See [handling failures and retries](/docs/guides/retries-and-dlqs).
- **Stuck, or something looks wrong?** Ask in [our Discord](/discord) — median response time is under an hour during business hours.
```

### Why this converts better (for your own review, not for the published page)
- Payoff before configuration — publish/consume happens before any explanation of topics, retention, or guarantees (Do, Don't Show).
- Auto-created topics remove a whole setup step from the minimum path to value.
- The dashboard trace view is positioned as the peak moment, and reused later as the production debugging tool — same UI, so it stops looking unfamiliar exactly when the engineer is under the most stress (stage 7).
- cURL example keeps non-Node evaluators from bouncing at step 2.
- "Next steps" routes directly into the three things that actually block stages 5–7 (retries/DLQ doc, production checklist, community), instead of a generic "explore the docs" link.

---

## 3. DevRel KPI Framework — November Presentation

### Framing for the deck (say this out loud, don't bury it in a footnote)
Three people own four developer-facing surfaces because product is heads-down on the enterprise roadmap. This framework commits to what three people can move and reports the rest as *watched, not committed* — the alternative is a scorecard that quietly fails by January because it was sized for a team you don't have.

### North Star Metric

**Weekly Production-Active Topics** — topics that received and delivered ≥1 message in a production-tagged environment in the trailing 7 days.

Why this one: it's the direct measurement of journey stage 7 (your defined end state), it can't be inflated by signups or trial activity, and it's pulled from your own telemetry — no dependency on product instrumentation you don't control.

### KPI tree, mapped to journey stages and ownership

| Surface | Leading indicator (DevRel fully controls) | Journey stage | Nov baseline needed |
|---|---|---|---|
| Docs | Quickstart completion rate | 3→4 | Yes — pull from current analytics before setting a target |
| Docs | Time-to-first-message (TTFM) | 4 | Yes |
| Docs | "Was this helpful" score, production-readiness checklist page | 6→7 | Yes |
| Dashboard | Signup → first message sent within 24h | 3→4 | Yes |
| Dashboard | Alerting configured before prod cutover, rate | 7 | Yes |
| SDK | Install → first successful call rate | 4 | Yes |
| SDK | GitHub issue first-response time | 2, 5 | Yes |
| Community | First-response time to a question | 2, 5, 7 | Yes — target <24h per community health baseline |
| Community | New-member 7-day retention | 2 | Yes |

Lagging / shared-attribution outcomes (DevRel influences, does not own alone):

- Trial → production conversion rate (stage 3→7)
- Time-to-production, median (stage 0/3→7 elapsed)
- 90-day production retention
- Expansion rate — second topic or team within 90 days of first prod (stage 8)

### Capacity reality — put this on its own slide, not a footnote

| Surface | Fully movable by DevRel alone? | Needs product/eng support you don't currently have |
|---|---|---|
| Docs | Yes | — |
| SDK bug fixes / DX changes | Partial | Merge priority and roadmap slot for anything beyond docs/examples |
| Dashboard (empty states, alerting, trace view improvements) | No | Frontend eng time — currently zero allocated |
| Community | Yes | — |

This is the honest version of the slide: two of four surfaces are fully in your hands, one is partially blocked, and dashboard-side improvements — which the journey map flags as decisive at stages 3, 4, and 7 — are structurally gated on eng time nobody has committed. Say that plainly. It's the difference between a scorecard you can be held to and one that quietly indicts you in Q1 for a dashboard feature you had no path to ship.

### Q4 commitments — pick two, not eight

1. **Time-to-first-message < 5 min for 80% of new signups.** Fully docs + SDK, zero external dependency, directly fixes the highest-leverage friction point identified in the journey map (stage 4).
2. **Trial → production conversion rate: improve over Q3 baseline.** Cross-surface, DevRel-influenced — set the actual target only after pulling the real baseline; don't present a percentage you invented for the slide.

Everything else in the KPI tree above is **watched, not committed** this quarter: reported monthly, no target attached, explicitly framed as "here's what we're tracking so surprises don't happen, not what we're promising to move."

### Reporting cadence

| Cadence | What | Audience |
|---|---|---|
| Weekly | Docs + community ops metrics (response time, completion rate) | Internal, team only |
| Monthly | Activation + SDK metrics | Shared with product |
| Quarterly | North Star + committed KPIs + capacity reality | Exec-facing — this is the November deck |

### Suggested slide order for November

1. North Star metric + why it's the right one
2. Journey-aligned KPI map (the table above, visualized as a funnel)
3. Q4 committed KPIs — baseline, target, current
4. Capacity reality: 3 people, 4 surfaces, explicit table of what's blocked and why
5. Watched metrics — transparency without commitment
6. The ask: sign off on these 2 KPIs as the official scorecard, and note in writing that dashboard-linked targets are contingent on eng time not yet allocated

That last slide is the point of building this now instead of in December — it puts the ownership gap in front of leadership as a decision they need to make, not as an excuse you reach for later.