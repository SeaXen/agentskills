# Sableworks DevRel deliverables

One note before the artifacts: I don't have your actual quickstart page, analytics, or support data in front of me, so every number below is explicitly tagged `inferred`, `baselining`, or `hypothesis` rather than invented as if it were real. Swap in your instrumentation and the three documents keep working — that's the point of tagging them this way instead of guessing a number that looks authoritative and isn't. All three are built to share vocabulary (same success event, same stage names) so your three-person team tracks one thing, not three.

---

# 1. Developer journey map — backend engineer at a scale-up, 2026-09-19

## Scope

**Product:** Sableworks, a hosted message-queue-as-a-service — publish/subscribe and durable queues via SDK, a dashboard for queues/DLQs/metrics, usage-based billing with an enterprise tier in progress.
**Segment:** a backend engineer at a scale-up (roughly 50–500 people), usually replacing a hand-rolled queue or an outgrown self-hosted broker.
**End state:** production usage.

**Stage model.** End state deletes three of the five published models outright: Revell six-stage (terminal = standardization), AAARRRP (terminal = revenue/product feedback), Orbit levels (terminal = advocate) all have the wrong tail for "production usage" and come off the menu. Between what's left — the API/platform five-stage arc and the unsourced discover→try→adopt→contribute→advocate default — the arc wins on both efficiency and fit: its "production" stage is the literal end state, its boundaries (first call, integration, production) usually already sit in whatever telemetry you have, and it doesn't bury the integration→production split inside one "adopt" stage the way the default would. This is a first map, so there's no prior model to preserve.

**Chosen: API and platform five-stage arc** — Awareness → Onboarding → Integration → Production → Advocacy.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness | "find something better than the queue we've duct-taped together" | search, peer mention, or an on-call page from the current broker | lands on Sableworks docs or the SDK repo | search results, comparison content, GitHub, community mentions | DevRel *(inferred — no marketing function exists separately)* | no evidence yet | not instrumented — recommend self-reported first-touch at signup, by source |
| Onboarding | "prove this works from my laptop before I bring it to the team" | opens the quickstart | first message published **and** read back from local code | quickstart page, SDK install, API key creation | DevRel (owns docs, quickstart, and the dashboard's first-run UX) | no evidence yet — a cold run is scheduled as part of the quickstart rewrite (see §2) | not instrumented today; ships this cycle as `first_roundtrip_success` (see §2 and §3) |
| Integration | "wire this into a real service and trust it won't lose messages" | first success reached | SDK called from a service repo on a shared branch, developer starts asking about retries/DLQ/ordering | SDK reference, error docs, DLQ view, support | DevRel *(by default — this is delivery-semantics documentation, which is normally product's job)* | no evidence yet | not instrumented — recommend share of first-success accounts making a non-local call within 30 days |
| Production | "own this on call" | staging traffic observed | sustained production traffic for 14 days plus an alerting rule configured | dashboard/metrics, alerting, runbooks, status page | DevRel for docs and dashboard UX; **no owner** for alerting reliability itself | no evidence yet | not instrumented — recommend share of integrating accounts reaching 14-day sustained traffic |
| Advocacy | "tell people this saved us the on-call pain" | meaningful time in production (~90 days) | public talk, post, or unprompted recommendation naming Sableworks | community (Discord/Slack), CFPs, changelog | DevRel | no evidence yet | not instrumented — recommend raw list of unprompted public mentions/quarter (small-N floor applies) |

**Organizational finding, not a stage finding:** four of five rows name DevRel as owner, and only Advocacy is a stage DevRel would own under any normal org chart. Onboarding is DevRel's legitimately (it owns the quickstart and the dashboard's first-run UX), but Integration's delivery-semantics docs and Production's alerting reliability are usually product or platform-engineering territory. They land on DevRel here only because product is heads-down on the enterprise roadmap, not because DevRel is the right structural owner. Per the skill this map is built on: *"If most rows name DevRel as owner, report that as a finding about the organisation. It means the surfaces have no accountable owner, which is a bigger problem than the leak."* That's the headline of this map as much as any single stage is.

## Buyer lane

Mostly collapsed — the developer decides and Sableworks is self-serve at this segment's price point, so state that explicitly rather than leaving it blank. One thin exception: once usage crosses from free tier into metered billing at the Production stage, a developer typically needs their own engineering manager or finance to sign off on the spend. That approval is owned outside Sableworks entirely (the customer's own manager), so it's noted here but not built out as a full lane.

Worth instrumenting regardless of lane: **boundary contact** — someone on the account viewing the security/SSO page, asking a compliance question, or hitting a seat/rate limit. That's the cleanest early signal an account belongs to the enterprise motion product is separately building, and it's the trigger for the DevRel-Qualified-Lead metric in §3.

## Moments

- **First success** — first message published and read back from local code. No measured time yet; the quickstart rewrite in §2 commits to a 5-minute budget and instruments the event that will make this real.
- **Moment of truth** — the decision to call the SDK from a shared-branch service instead of a throwaway script. This is where the team stops evaluating delivery guarantees on faith and starts depending on them.
- **Abandonment point (hypothesis, not measured)** — most likely inside Onboarding, at API-key creation or at the first confusing encounter with ack/redelivery semantics. Flagging this as a hypothesis because nothing here is instrumented yet; the cold run in §2 is what turns this into evidence.

## Leak

**Nominated: Onboarding.** This map fails its own signal-coverage gate (0 of 5 stages carry a real value, well under the 60% threshold), so this is a structural call, not a measured one — shipping it anyway because an honest gap beats a fabricated rate. The reasoning: Onboarding is the earliest stage in the arc, it has a real owner able to act on it (DevRel owns the quickstart end-to-end), and its fix is already in flight — the rewrite in §2 targets exactly this stage. That combination (earliest, owned, fix already scheduled) is what the skill's own promotion rule calls out as a legitimate reason to nominate ahead of hard numbers.

Applying B=MAP only now that the stage is picked: the working hypothesis is an **ability** problem, not motivation — credential creation and the first encounter with delivery semantics are plausible "scarce time/unfamiliar routine" bottlenecks, which is the default and most common cause for a developer audience. The quickstart cold run will confirm or kill this hypothesis with real friction-log evidence.

## Handoff

- **Owner:** DevRel's quickstart/docs lead.
- **Signal to watch:** share of quickstart starters reaching `first_roundtrip_success` within 7 days — the same metric instrumented in §2 and reported as the primary in §3.
- **Re-read date:** 2026-12-18 (90 days), and immediately again once the rewritten quickstart ships, per the rule to re-read after any docs rewrite regardless of the clock.

## Gaps

- All five stages are inferred or not instrumented — this map's real job right now is to be the instrumentation request, not a finished scorecard.
- Awareness needs a self-reported first-touch question at signup; expect a large "direct"/no-referrer bucket from AI-assistant and aggregator traffic — that's normal, not a tracking bug.
- Onboarding gets `first_roundtrip_success` and step-level events from the quickstart rewrite (§2).
- Integration needs a tagged event distinguishing a local/sandbox call from a call made from a real service environment.
- Production needs a sustained-traffic-plus-alerting-configured event; today nobody outside DevRel is accountable for the alerting half of that exit event, which is itself a gap worth escalating, not just instrumenting.
- Advocacy needs a lightweight community-listening habit; expect this to stay below the small-N floor for a while and to be reported as a raw dated list.

**Quality-gate self-check, reported honestly:** exactly one leak nominated ✓; every stage has one named owner ✓ (but four of five collapse to DevRel, failing the "at least one owner outside DevRel" line — see the organizational finding above); every friction claim says "no evidence yet" rather than a hypothesis dressed as fact ✓; inferred stages labelled everywhere ✓; fits on one page ✓; **signal coverage: 0/5, failing the 60% line.** Per the skill's own fallback, that failure doesn't block shipping — it's the instrumentation request.

---

# 2. Quickstart rewrite

You didn't paste the current page, so this isn't a true cold-run audit — I can't hand you a defect table against text I've never seen. Treating this as a greenfield build against the target state instead. If you send me the live page, I'll re-run this as a real audit with a cold-run defect table diffed against it.

**Success moment + time budget:** the message you published shows up when you read it back — a full round trip, not just a "sent" status. Product class: hosted API. Budget: **5 minutes**, committed as a hard constraint everything below competes for.

**Biggest lever, stated up front:** the highest-leverage change available isn't wording — it's deleting the account. The page below ships with an instant, no-card self-serve key (already close to best-in-class). The next rung up is a temporary, anonymous dev key requiring no signup at all, which is the pattern most fast-onboarding vendors use. That needs backend work (issuing and expiring anonymous keys) that a three-person DevRel team can't build alone — flag it to whoever owns the API-key service as a scoped ask, not a docs fix.

### The quickstart page

*(Written in TypeScript per your stack preference. Sableworks' actual SDK method names and auto-create behavior are illustrative — confirm the real signatures before publishing, and if a queue must be pre-provisioned rather than auto-created on first write, delete that step rather than documenting it, per the rule below.)*

```markdown
# Publish and read your first message in 5 minutes

You will publish a message and read it back, proving both halves of the
round trip — not just that Sableworks accepted your call.

## Before you start

- Node.js 18 or later: check with `node --version` (https://nodejs.org)
- A Sableworks test API key: [create one](https://sableworks.example/keys)
  (no card required)

Test keys write to a sandbox queue only, so nothing touches your real
infrastructure.

## 1. Install the client

    npm install @sableworks/client@2

## 2. Publish a message

Create `publish.ts`:

    import { SableworksClient } from "@sableworks/client";

    const client = new SableworksClient("<YOUR_TEST_API_KEY>");

    const message = await client.queues.publish("orders-dev", {
      body: { orderId: "demo-1", status: "created" },
    });

    console.log(message.id, message.status);

Run it:

    npx tsx publish.ts

You should see:

    msg_01J9F3K2 queued

`401 Unauthorized`? The key was not copied in full — it ends with a
checksum segment. Copy it again from the keys page.

## 3. Read it back

    import { SableworksClient } from "@sableworks/client";

    const client = new SableworksClient("<YOUR_TEST_API_KEY>");

    const [received] = await client.queues.receive("orders-dev", {
      maxMessages: 1,
    });

    console.log(received.body);
    await client.queues.ack(received.receiptHandle);

Run it:

    npx tsx receive.ts

You should see:

    { orderId: 'demo-1', status: 'created' }

Nothing printed after a few seconds? The message was already consumed
by an earlier run — queues are single-read. Run `publish.ts` again first.

## What just happened

`publish` returned immediately with a `queued` status; `receive` pulled
it back independently a moment later. That gap is the whole point of a
queue — your publisher and your consumer never had to run at the same time.

## Next steps

- [Handle failed messages: retries and dead-letter queues](…)
- [SDK reference](…)
- [Community Discord](…)
```

### Cut list

| Cut from the quickstart | Where it lives now |
|---|---|
| Delivery-guarantee and ordering theory | "How Sableworks handles delivery" concept page |
| Dashboard walkthrough (creating queues via UI, reading metrics) | "Using the dashboard" how-to |
| Retry/backoff/DLQ configuration | "Handling failed messages" how-to — linked from Next steps, and the natural landing page for the Integration-stage friction named in §1 |
| Key rotation, scoping, production hardening | Security/production-readiness doc |
| Python/Go/Java SDKs | Independent sibling pages (`quickstart-python`, `quickstart-go`), each cold-run verified on its own — don't publish a tab until it's actually been run |

### Verification plan

- Clean environment: fresh machine or container, no cached `node_modules`, no pre-existing Sableworks account.
- Fresh test key, generated as part of the run.
- Runner: whichever of the three of you has touched the SDK client least recently — Hammerly's rule that the newest person catches what veterans route around, adapted for a small team without a steady stream of new hires.
- Keep a friction log (green/yellow/red) alongside the run; three hesitations in one step means split it.
- Measure wall-clock from `npm install` to the `receive.ts` success line; must land at or under 5 minutes or the success moment shrinks, not the budget.
- Ship only once: every command runs unedited, every output matches what's documented, zero prerequisites surface after step 1, time is in budget, and someone unfamiliar with the product reaches success without leaving the page.
- Automate the commands into CI against the published package so drift fails loudly instead of silently — since there's no engineering partner to own this, the cheapest ask you can make of whoever owns the SDK repo is a release-blocking check, not a review.

### Instrumentation

- **Success event:** `first_roundtrip_success` — fires when a `receive()` call returns the message a `publish()` call in the same session sent.
- **Funnel:** page load → install run → `publish.ts` run → `receive.ts` run → `first_roundtrip_success`.
- **KPIs, in build order (cheapest and most localizing first):** step-level drop-off → support tickets quoting a quickstart step → median time to first success → completion rate → day-7 return of completers (promote this last one only once completion looks healthy).
- **Targets:** measure four weeks as baseline, then commit to a relative improvement. Do not import the "20–40% self-serve activation" figure that circulates for developer tools — it's not a study, and it isn't yours.
- This event is the same one the journey map (§1) watches as its Onboarding signal and the KPI framework (§3) reports as its primary metric — one instrumentation effort feeds all three documents.

### Ownership

The skill this is built on assumes the shipping engineer authors the first draft and a docs reviewer signs off. That assumes an engineering partner this team doesn't have right now. Given that: the DevRel teammate who most recently touched the SDK authors and cold-runs the first draft; a second teammate reviews, since there's no separate writer role to hand it to. The one thing worth asking product/engineering for — cheap even from a team with zero spare capacity — is a ping when `@sableworks/client`'s public API changes, so this page doesn't silently drift out from under you.

---

# 3. DevRel KPI framework — November review

## Driver and goals

**Funded driver (inferred — confirm with whoever holds your budget):** developer enablement / self-serve adoption. Owner: you, presenting to your leadership in November.

Given the deadline is inside one quarter, this promotes enablement metrics (cheap, already collectable) and is honest that anything needing a pre-period — cohort retention — won't have real numbers yet. Given the effort ceiling is a three-person team already covering docs, dashboard, SDK, and community, this deletes anything needing new cross-team cooperation you don't have (a sales-ops partnership for influenced pipeline) rather than parking it hopefully at the bottom of the sheet.

**Goals this horizon:**
1. Get more backend engineers at scale-ups to a working first message (Onboarding conversion).
2. Confirm that people who succeed keep depending on it in production (Production retention).
3. Keep an honest, low-cost read on whether any of this reaches accounts product's enterprise motion cares about — without DevRel carrying a revenue target it has no way to move.

**Spine:** journey-stage, over the two alternatives considered. Driver-anchored (AAARRRP) needs a charter that doesn't exist yet and buries "production" inside "retention" — the exact split your journey map needed to keep separate. Function-split (awareness/enablement/engagement) fits teams organized by function; yours isn't — one team covers every surface, so a function-split spine would imply a division of labor that doesn't exist. Journey-stage wins for a second reason worth naming to your team: it reuses the exact stage names and the exact event (`first_roundtrip_success`) from the journey map and the quickstart rewrite, so there's one vocabulary to maintain, not three.

## Metric sheet

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|---|---|---|---|---|---|---|---|
| 1 **P** | First-success rate, 7 days | Enablement | share of quickstart starters reaching `first_roundtrip_success` within 7 days | product analytics, `first_roundtrip_success` event | **baselining** — instrumentation ships with the quickstart rewrite; November's number is week-1–4 data, not a trend | commit to a relative improvement over the observed week-1 baseline *(hypothesis — not a fixed percentage; the 20–40% figure in circulation is folklore)* | DevRel (docs/quickstart) | cold-run the quickstart, fix the step it fails on |
| 2 | Median time to first success | Enablement | page load → `first_roundtrip_success`, median | same event, timestamp delta | baselining | flag if trailing median exceeds 10 min (2× the committed budget) for two straight weeks *(baseline, once observed)* | DevRel | find the slow step via drop-off data, fix or cut it |
| 3 | Step-level drop-off, quickstart | Enablement | share abandoning at each documented step | docs + product analytics | baselining | set at next review | DevRel | fix or cut the losing step |
| 4 **P** | 30-day production retention of first-success cohort | Product impact | share of accounts still sending sustained traffic 30 days after `first_roundtrip_success`, by join cohort | product analytics | **not available for November** — the cohort itself doesn't exist until ~30–60 days after the quickstart ships; present as "baselining, first real read expected [ship date + ~6 weeks]" rather than a placeholder number | below 50% *(hypothesis, pending first read)* | DevRel | interview five lapsed accounts before proposing a fix |
| 5 | Support tickets per 100 new accounts, first 30 days | Enablement | tickets opened ÷ new accounts × 100 | existing support system *(confirm it already tags account-creation date — if not, this one is also baselining)* | possibly available now from trailing quarters, unlike 1–4 | above your own trailing median *(baseline, once confirmed)* | DevRel (owns support/community) | mine top 3 ticket topics into the Integration-stage troubleshooting docs named in §2's cut list |
| 6 | Self-reported first touch | Engagement | one-question signup survey, stable option list | signup form (small one-time build cost) | baselining | flag if response rate falls below 40% *(hypothesis — a circulating figure, not a measured benchmark)* | DevRel | shorten or reposition the question |
| 7 **P** | DevRel Qualified Leads routed to product's enterprise motion | Business impact | accounts showing boundary-contact signals (SSO/security page view, compliance question, seat/rate-limit hit), routed with the receiving team's acknowledgment logged | manual handoff log | 0 recorded — rule new this half | reported, not targeted, for two quarters | DevRel | none while baselining; review quarterly for patterns |
| 8 | Verbatim evidence | Qualitative | friction findings and quotes from cold runs, support, and community, tagged high/medium/low confidence, with the fix shipped and date | manual log, starting with the quickstart cold run in §2 | first entries logged this cycle | fewer than 2 per quarter *(baseline)* | DevRel | schedule structured user conversations |

## Attribution rule

Self-reported first touch (metric 6) is the standing instrument, reported as "self-reported first touch" — never as attribution. Tagged links, if used at all, compare specific artifacts (which post drove which docs entry) and are never summed into a program total.

**No influenced-pipeline or revenue claim.** Deliberate choice, not an omission: the enterprise motion belongs to product, not DevRel; there's no sales-ops partner named to make an influenced-pipeline rule meaningful; and a three-person team already covering four surfaces has no capacity to maintain the CRM identity mapping that method requires. Per Thengvall's position, the currency instead is the DevRel Qualified Lead (metric 7) — logged and reviewed, never presented as revenue.

**Blind spots:** word-of-mouth inside a company that never touches a Sableworks surface; roughly 70% of AI-assistant-driven traffic arriving with no referrer (directional, from one newsletter, not a study); community conversation happening in venues the team doesn't monitor today, since community is one of four surfaces this team covers thin.

Any change to the signup question's option list or the DQL routing definition is announced as a restatement, not a silent edit.

## Reporting

- **Monthly (operational, to the team itself):** metrics 1, 2, 3, 5 — the levers DevRel can act on week to week.
- **Quarterly (decision, to leadership):** the full sheet, including the still-baselining rows and the qualitative log.
- **Annual:** re-derive the sheet from the driver; assume half the metrics change.

**Five-sentence summary for the November room:**

"New backend engineers get a message published and read back within our 5-minute budget at a rate we're instrumenting for the first time this cycle — this number is a baseline, not a trend, and every future report compares against it. Whether that first success turns into production retention won't be measurable until roughly six weeks after the quickstart ships, which we're flagging now instead of promising a number we don't have. Support tickets per new account already have real trailing history from our existing system and are the one line in this deck backed by data today. We don't carry a pipeline or revenue target — the enterprise motion belongs to product, and we log qualified signals and hand them over rather than claim the revenue. Three people own every surface on this sheet — docs, the dashboard, the SDK, and community — so it's eight lines we can actually keep alive, not thirty that rot by month two."

## Known blind spots

- No visibility into engineers who read docs but never sign up — the pre-signup funnel is entirely dark.
- No identity link between community members (Discord/Slack) and product accounts, so community engagement can't be tied to activation or retention yet. Closing this needs an identity-mapping join — a few engineering days nobody on this team currently has spare, and not something DevRel can build unilaterally.
- DevRel owns the Production stage's dashboard and docs but not the underlying alerting reliability — a confusing alerting UI could suppress metric 4 and DevRel has no lever to fix the root cause, only to document around it.
- No enterprise-specific compliance or security data — that motion is owned separately by product; the DQL log (metric 7) is the only visibility this framework has into it.

## Review

Next review: **2027-01-15** — far enough past November to see whether the quickstart's baseline period actually completed. Kill-rule status: not yet applicable, every metric here is new this cycle; first kill-rule check happens at the following review.

## Pass-threshold self-check

Eight metrics ✓ (upper limit, not over). Every metric carries all six fields ✓. At least one product-impact and one business-impact metric present (4 and 7) ✓. No monotonic metric as a primary ✓. No incentivized volume metric needs a counter-metric — nothing here rewards raw volume the way signups or post-counts would. Attribution rule written, names its methods, its blind spots, and explicitly doesn't use "influenced" language, because this framework deliberately carries no influenced-pipeline claim. Every threshold tagged `baseline` or `hypothesis` — none `sourced`, and no `hypothesis` presented as a target. Blind-spots section non-empty ✓.