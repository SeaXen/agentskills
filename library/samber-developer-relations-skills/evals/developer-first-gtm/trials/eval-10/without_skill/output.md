Day 1 action: pull renewal data + usage data for every flat/down account before touching any gate. Diagnose first, fix second.

## Root cause (working theory, verify week 1)

Two decisions got fused that should stay separate:
1. Who buys (CISO, top-down, $180K-400K contract) — keep this motion, correct for security infra.
2. Who validates and defends renewal (engineers) — zero self-serve trust path exists. Demo-gate blocks docs, API reference, error codes: material engineer needs to trust and integrate secrets platform, not material that protects pricing or IP.

Result: CISO signs, engineers never touch product deep, no internal champion exists at renewal time. "Our engineers never really used it" = leading indicator, discovered 12+ months too late.

## Week 1: diagnose, don't fix

1. 1:1s (30 min each): CRO, VP Sales, Head of CS/renewals, 2-3 AEs on flat/down deals, eng lead.
2. Pull usage telemetry per account, if exists. If not: finding #1, flag immediately.
3. Read every renewal/churn note, last 8 quarters not just last 4 deals.
4. Walk own funnel as fake evaluator. Time every step from landing page to API reference. Count form fields.
5. List every asset behind "book a demo": pricing, docs, API reference, rate limits, error codes, changelog. Tag each: commercially sensitive (protect) vs technical-reference (should open).

Time: 3-4 days.

## Day 30: build evidence, don't argue opinion

- Build simple account health score: usage trend + seat activity + support sentiment + API call volume, blended with commercial signal (renewal date, price change). Churn model applied to engineering engagement as leading indicator, not just billing health.
- Segment past renewals by this score, retroactive. Confirm or kill hypothesis with real numbers before pitching change.
- Draft reframe for CRO: not "open everything," two-lane model.
  - Lane 1 (stay gated): pricing, contract terms, competitive comparison — commercially sensitive, protects AE motion.
  - Lane 2 (open or lightly gated): API reference, error-code pages, docs, architecture/security whitepaper, scoped sandbox — technical proof, protects renewal.
- Pitch as 90-day experiment, not permanent policy. Un-gate Lane 2 for subset of active deals + at-risk renewals. Measure technical-objection rate in sales cycle + health-score movement.

⚠️ CRO owns "every visitor = lead" as real KPI. Don't change gating unilaterally. Bring data, propose test, get buy-in. Cross-functional fight, not solo product call.

## Day 60: ship technical trust path

1. Un-gate API reference + error-code pages + architecture docs. Zero pricing exposure, high trust payoff.
2. Reorganize docs into 4 types (tutorial, how-to, reference, explanation). Most engineers want tutorial + how-to first, reference second, rarely read conceptual docs.
3. Stand up scoped sandbox, usage-based limits not time-based (capped secrets count, single environment, no HA/compliance features). Genuinely useful for evaluation, not crippled demo.
4. Wire sandbox into AE workflow: "give your champion hands-on access" becomes sales accelerant mid-cycle, not self-serve replacement for $200K deal.
5. Instrument everything day one: sandbox usage + production usage, feed straight into account health score.

## Day 90: close loop on renewal risk

1. Health score live for every account, reviewed monthly with CS. Flags risk 90+ days before renewal, not at renewal.
2. Light champion motion for existing accounts: quarterly engineer-facing release notes, direct Slack channel to platform teams on top accounts, public credit for engineers who build real integrations. Cheap, keeps human defending tool when CISO who signed moved on.
3. Re-pitch CRO with 90-day A/B result: technical-objection rate, cycle time, health-score delta on accounts given sandbox access.

## Skip these

- Don't flip to full self-serve PLG. $180K-400K security contract still needs AE motion.
- Don't un-gate pricing or contract terms. Real commercial exposure.
- Don't build big free tier with no limits. Usage-based caps, not time-boxed trial.
- Don't skip diagnosis step. 2 of 4 renewals suggestive, not proof — get health score before rebuilding anything.

Next: book 5 week-1 conversations for Monday + Tuesday. Start with CRO — everything downstream needs their buy-in.