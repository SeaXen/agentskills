# Tarnhelm Developer Journey Map — Platform Engineers, 1,000+ FTE Accounts (FY27)

## The one-line answer for the board

Your funnel maps how *one developer* adopts Tarnhelm. It has no stage for how *an organization* adopts Tarnhelm. Five accounts have hundreds of individually-activated developers sitting at "advocate" with nobody ever having driven the account through the separate, unowned journey that turns a well-loved tool into a mandated standard. Call it the **Champion Ceiling**: individual enthusiasm saturates a company at 150–300 developers and then flatlines, because nothing after "advocate" was ever designed.

---

## Why 200+ developers and still "that team's tool" isn't a paradox

Discover → try → adopt → contribute → advocate is a complete, correct model — of an individual's relationship with your product. It has no actor for the platform/DevEx team, no actor for security or compliance, no actor for the VP Eng who has to say "this is now how we do flags here," and no event for procurement consolidating three teams' contracts into one. An account can have 50 individual "advocates" and be at stage zero on the axis that actually matters for renewal, because that axis was never drawn.

This also explains why sales ops' account rollup and product's SDK-init/first-eval telemetry both look healthy right up until renewal, and then surface a wall: they're both instrumented against Track A below. Nobody is instrumented against Track B.

---

## The journey map: two tracks that have to interlock

### Track A — Individual Developer Journey (your existing model, instrumentation-graded)

| Stage | Definition | Telemetry today | Gap |
|---|---|---|---|
| Discover | Dev hears about Tarnhelm (docs, internal Slack, colleague) | None — first signal is Try | No source/referrer capture on first SDK pull or docs visit |
| Try | SDK installed in a non-critical service | **SDK init event** — well instrumented | Fine as-is |
| Adopt | First flag gates real production traffic | **First flag evaluation** — well instrumented | Fine as-is, but only proves one dev/one service adopted, not the team |
| Contribute | Dev writes internal wrapper, docs, Slack answers, files good feature requests | Not instrumented | No system of record for internal champion behavior |
| Advocate | Dev recommends Tarnhelm to other teams/orgs, speaks up in internal platform reviews | Not instrumented | Same gap — currently only visible anecdotally to CS/DevRel |

Track A is why product telemetry and the board both see "adoption." It's real, it's just capped at the individual.

### Track B — Organizational Standardization Journey (missing — this is the actual gap)

| Stage | Definition | Who drives it | Signal needed | Current instrumentation |
|---|---|---|---|---|
| 1. Pocket adoption | One team, bottom-up, via Track A | Individual dev | 1 service w/ SDK init in account | ✅ exists (as above) |
| 2. Cross-team spread | 2+ teams independently adopt, uncoordinated, often with divergent flag naming/config patterns | Individual devs, no coordination | # distinct teams/services with SDK init in one account | ❌ not rolled up this way today |
| 3. Champion recognition | An internal champion starts evangelizing horizontally — writes an internal wiki page, answers other teams' questions | The Track-A "advocate" | Internal mentions, cross-team support requests referencing them | ❌ no tracking |
| 4. Platform endorsement | Central platform/infra team wraps Tarnhelm in an internal library, adds it to the service template/scaffold | Platform/DevEx team | Existence of an internal SDK wrapper repo; new-service scaffold reference | ❌ invisible to Tarnhelm entirely |
| 5. Governance lock-in | Security/compliance signs off; SSO, RBAC, audit log, approval workflows actually configured (not just available) | Security/compliance + platform team | Admin console config completeness (SSO on, RBAC roles defined, audit log queried, approval workflow active) | ⚠️ likely captured in-product but not surfaced as an adoption signal |
| 6. Org-wide default | New services get Tarnhelm by default via the scaffold; onboarding docs for new engineers mention it | Eng leadership + platform team | % of *new* services (last 90 days) with SDK init vs. total new services | ❌ not computed |
| 7. Embedded standard | Budget consolidated to one contract, renewal is a formality, account references you externally | Exec sponsor + procurement | Contract consolidation in CRM, active exec sponsor contact on file | ⚠️ CRM has the raw data, nobody reads it this way |

### Where the interlock breaks

Plot your five stuck accounts and the pattern is almost certainly identical: strong stage-4/5 presence on Track A (dozens to hundreds of individual advocates and adopters) paired with stalled stage-2 or stage-3 on Track B — cross-team spread happened organically, but nobody ever became the account's internal Track-B driver, because DevRel and CS were both organized around and measured on Track A. Nobody owns the handoff from "champion exists" to "champion has air cover to mandate."

```
Track A (individual)      Discover → Try → Adopt → Contribute → Advocate
                                                                    ●●●●● (200+ devs sitting here)
                                                                    │
                                                                    ▼ ← THE GAP: nothing carries this forward
Track B (organizational)  Pocket → Cross-team → Champion → Platform → Governance → Org-default → Embedded
                            ✅        ✅          ⚠️           ❌          ❌            ❌           ❌
                                                 (5 stuck accounts sit here)
```

---

## Segment & personas (hypothesis-graded — validate in Week 1, don't ship these to the board unvalidated)

Your segment is platform engineers at 1,000+ FTE companies, but Track B reveals at least three distinct actors inside every stuck account. Treat these as hypotheses pending the interviews below, not finished personas — you don't have primary research yet.

**Individual Champion** (Track A "advocate," lives in one team) — wants recognition and a direct line to your team; doesn't have organizational authority to mandate anything; can be burned out by being asked to "sell it internally" with no support.

**Platform/DevEx Lead** (the actual Track-B gatekeeper) — cares about maintenance burden, blast radius, and "one more vendor to own," not features; will not endorse a tool a champion "found," only one platform is comfortable owning long-term; likely never in your CRM as a contact today — check.

**Eng Leadership / VP Eng or Security stakeholder** (the sign-off) — cares about consolidation, cost per seat at scale, and audit/compliance exposure; triggered to act by a renewal, an incident, or a budget review, not by developer enthusiasm.

If the Platform/DevEx Lead isn't a named contact in the CRM rollup for any of the five accounts, that's diagnostic on its own — it means Track B literally has no addressable owner from your side either.

---

## Instrumentation to build before planning closes

| Signal | Tells you | Source | Priority |
|---|---|---|---|
| Distinct teams/services per account with SDK init | Cross-team spread (stage 2) | Product telemetry, rolled up by account via CRM org ID | High — likely a rollup query, not new instrumentation |
| % of *new* services (rolling 90d) using Tarnhelm vs. total new services created | Org-wide default (stage 6) | Requires account to report or infer total service count — may need a lightweight platform-team survey, not pure telemetry | High, but expect manual work for the first pass |
| Admin console config completeness (SSO, RBAC roles, audit log access, approval workflows) | Governance lock-in (stage 5) | Already in-product, just not read as an adoption signal today | High — cheapest win, likely a dashboard query away |
| Internal champion signals (cross-team Slack/support mentions, internal wiki pages referencing Tarnhelm, feature requests filed on behalf of other teams) | Champion recognition (stage 3) | Not systematically captured — start manually for the 5 accounts this quarter | Medium — apply the power-user scoring model (usage + community + content signals) internally, per account, not just per user |
| Platform/DevEx Lead present as a named CRM contact | Whether Track B has an addressable owner | CRM | High, zero engineering cost |
| Exec sponsor present as a named CRM contact + contract consolidation status | Embedded standard (stage 7) | CRM | High, zero engineering cost |

Combine into a single **Standardization Score** per top-10 account (stage reached, 1–7) and report it next to seat count. Seat count answers "are developers using it." Standardization Score answers the board's actual question.

---

## Three-week plan (today 2026-09-19 → planning close ~2026-10-10)

**Week 1 — Diagnose the 5 accounts, especially the 2 renewal-pinned ones**
- Pull CRM rollup + telemetry, compute today's Standardization Score per account.
- Check whether a Platform/DevEx Lead and an exec sponsor are even named contacts — if not, that's your first action item, not a research question.
- Run 5–8 short interviews with individual champions *and*, critically, the Platform/DevEx Lead if reachable, at the two renewal accounts plus three others. Ask the actual 5-why: "Why hasn't this become the default for new services?" Expect answers to cluster into governance friction, no platform-team incentive, competing internal tool, or plain nobody-asked. Don't assume the cause — the fix is different for each.

**Week 2 — Synthesize and design account-specific unblocks**
- Cluster interview findings by cause, tag confidence (High = 3+ accounts, same theme, unprompted).
- For each renewal account, design one "Champion-to-Mandate" play matched to the actual blocker found: an executive briefing deck if it's an awareness gap, a security/governance one-pager if it's compliance friction, a platform-team enablement kit (wrapper library template, migration guide) if it's a maintenance-burden objection.
- Identify and name the top 3–5 individual champions per account using the usage + community + content scoring approach — these are your Week-3 co-pilots for the internal sell, not your target audience.

**Week 3 — Package the FY27 ask**
- Present the two-track map and the Standardization Score for the top 10 accounts.
- Name the two renewal accounts' current stage and the specific play to move each one stage forward before renewal — not to stage 7, one stage.
- Ask for what actually closes this gap: this is rarely more content or a bigger champion swag budget (Track A is already saturated); it's usually a small solutions-engineering or platform-enablement function that works stage 3→5 accounts directly, plus a formal (not ad hoc) internal champion program — invite-only, real benefits (direct engineering access, early roadmap input, executive air cover for their internal pitch), no content quotas.

---

## What to put in front of the board

Reframe the question itself before answering it: not "why hasn't developer love converted to company standard," but "we've been measuring and rewarding an individual funnel; standardization runs through platform teams and executives, and we've never built or measured that path." Show the two-track diagram, the Standardization Score for the ten accounts, and a named stage-by-stage plan for the two renewal accounts. That reframes the ask from "give DevRel more budget for more of the same" to "fund the specific, missing function that carries champions into mandates."

---

## What would falsify this diagnosis — check before you commit to it

- If Week-1 interviews show a competing internal or third-party flagging tool already occupies the platform-endorsement slot, this is a displacement problem, not a coordination gap — different play entirely.
- If the blocker is pricing/procurement structure (per-seat cost that punishes exactly the org-wide-default outcome you want), no amount of champion enablement fixes it — that's a packaging conversation.
- If the SDK genuinely doesn't fit the platform team's stack (a language, a monorepo pattern, a deployment model), stage 4 is blocked on product, not on process — surface that immediately rather than running a Track-B program against a technical wall.