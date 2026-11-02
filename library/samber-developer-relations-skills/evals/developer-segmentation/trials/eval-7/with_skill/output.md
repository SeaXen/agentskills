# Developer segment map — Tarnhelm claims API & webhooks, Q4 2026

**Who you're segmenting:** not "developers" in general — there's no open population to reach. The whole audience is your existing broker roster's engineering contacts, a closed, contracted, enumerable set. The real cut isn't by language or company size — it's by **how much internal permission an integration needs to survive past the POC**, because that's where your two dead deals actually died. Quickstarts and a sandbox only serve the half of this audience that was never the problem.

Assumption stated up front, since this was answered from your summary, not an interview: funded driver = **developer enablement** — finishing integrations your commercial team already signed, not landing net-new logos (the API isn't sold separately, so there's no separate buyer to win). If the driver is actually something else — e.g. this is meant to justify unbundling the API as a paid product later — the weighting in Step 5 below changes; say so and I'll re-rank.

## Cut

Dimensions: **role in the decision** (does anyone besides the integrating engineer have to say yes) × **firmographic tier** (broker size / regulatory exposure, which predicts and routes to the right decision-unit bucket before a POC even starts).

Rejected, explicitly:

- **Involvement/motivation** — everyone in this audience is a paid engineer executing a contracted deliverable. No hobbyist, OSS or student population exists here; the family doesn't apply.
- **Technographic** (language/runtime) — claims submission + webhook status sync is stack-agnostic over REST/HTTP. No evidence yet that it changes anything you'd build. Worth instrumenting later for sandbox/sample-code language coverage, but not a segmentation axis this horizon.
- **Sector/workload** — every broker in this program does the same job with the API (submit claims, consume status webhooks). No evidence the *job* varies enough deal to deal to justify different artefacts. Promote this axis only if coding the 3 lost deals (below) shows the failures share a downstream-integration-complexity pattern the decision-unit axis doesn't explain.
- **Seniority** — not raised in your notes, and even if it were: it only matters here insofar as it maps to shipping authority, which the decision-unit axis already captures directly.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where reached | Evidence |
|---|---|---|---|---|---|---|
| Solo integrator brokers | Small/independent brokerage; one engineer or small team owns the whole claims-tech stack and can ship to production on their own authority | Unsized — pull from your broker roster this week; this is a fully enumerable private account list, not a public population, so it'll come back **measured**, not estimated. Today: **inferred**, shape only | User = champion = approver. Nobody else has to say yes. | Fast POC-to-prod path: realistic sandbox with representative claims data, a 10–30 min quickstart, clear webhook retry/idempotency docs, self-serve keys | Partner docs site, direct relationship-manager handoff | Presumed source of most/all of the 4 closed deals — **hypothesis**, not yet coded against actual notes |
| Governed platform brokers | Mid/large brokerage with a distinct IT, platform or security function; the engineer running the POC cannot unilaterally ship | Unsized, as above | User/champion evaluates and builds the POC; an architect and/or security reviewer approves; a budget/priority owner (e.g. Head of Ops) has to allocate ongoing engineering time to finish it | Production-readiness doc (SLA, uptime history, rate limits), data-handling answers for claims PII, webhook security model written for a reviewer who never opens the sandbox, a migration runbook off their current channel, one named peer-broker reference | Account-manager-led technical briefings, solutions-engineering engagement, insurtech/compliance conference tracks — not self-serve docs alone | Presumed source of the 2–3 dead deals — **hypothesis**, same caveat |
| Regulated/high-sensitivity governed brokers | A governed-platform broker additionally bound by a stricter data regime (e.g. health-adjacent claims lines, a specific regional residency rule), adding a legal/DPO sign-off on top of architecture/security | Unsized | Adds legal/compliance approver beyond the governed-platform baseline | Signed DPA template, data-residency answers, audit-log export | Same as governed platform, plus legal/compliance peer groups | 0–3 data points, **below the evidence floor** — hypothesis only |
| Channel-agnostic brokers (anti-segment) | Claims-ops, not engineering, owns the channel decision outright; no engineer is ever empowered to pick the API over the portal, EDI batch or phone, regardless of broker size | Unsized | No technical champion role exists at all — the "economic buyer" (ops) decides without inviting a technical evaluation | Nothing devrel builds moves this segment | N/A | By construction, this segment **will not appear** in your 7 deal notes — those notes only cover brokers who at least started a POC. Sizing it means pulling brokers who use only the other five channels despite having API access offered. |

## Primary

**Governed platform brokers.** Score (weighted for developer enablement — fit and compounding weighted above raw size, since the goal is finishing signed relationships, not landing new ones):

| Criterion | Score (1–3) | Why |
|---|---|---|
| Size | 2 | Fewer accounts, but each carries more claims volume |
| Reachability | 2 | Needs account-management routing, not self-serve docs — harder, but a named, known channel |
| Fit | 3 | This is the literal, named pain — 2 of your 3 lost deals live here on the working assumption above |
| Value | 3 | Larger broker = larger claims volume shifted off costlier manual/phone channels once it ships |
| Effort | 3 | Compliance pack, reference architecture, named case study, possibly dedicated solutions engineering — none of it exists yet |
| Competitive position | 2 | Their incumbent channel (EDI/portal) already clears their compliance bar; the switching case has to be made explicitly |
| Compounding | 3 | One shipped governed-broker reference + compliance pack becomes reusable proof for every subsequent governed deal (Moore: proof only travels inside a segment) |

Ratio (value-ish criteria ÷ effort) puts this segment **behind** Solo integrator on pure efficiency — it's the classic "big, high-value, high-effort segment that loses every round it's ranked on ratio." Promoted to primary anyway under the named exception: **one reference unlocks the rest of the segment** — the missing artefact today (a production-readiness pack + one named peer case study) is reusable across every future governed deal, not a one-off cost per broker.

## Secondary

**Solo integrator brokers** — served entirely by what devrel already wants to build (quickstart, sandbox realism). No new dedicated investment this horizon beyond what's already planned; this is the one place your devrel person's instinct was already pointed correctly.

## Anti-segment

**Channel-agnostic brokers.** Reachable in theory, but the blocker is commercial/organizational (ops owns the decision, not engineering) — no docs or sandbox investment moves them. Naming this stops the sandbox/quickstart budget from quietly trying to serve an audience that was never going to write code.

## Hypotheses

**Regulated/high-sensitivity governed brokers** — 0–3 data points, below the 5–10 floor. Test before funding anything segment-specific: re-read the 3 lost deals for a data-residency or legal blocker specifically (not just "security" generically). If none mention it, drop this row next quarter and fold it back into Governed platform.

## Implications

- **Do first, this week, before building anything:** code all 7 deals (4 won, 3 lost) against the decision-unit questions — *who first tried it, who else had to say yes, which question stalled it longest, who signed, in the losses which role blocked it.* This is hours of work against data you already hold, and it's what upgrades this whole map from hypothesis to measured. It will also confirm or break the assumption that the 2–3 dead deals are specifically the Governed-platform segment — if they turn out to be Solo-integrator deals lost for unrelated reasons (pricing, staffing, priority), this map's primary flips.
- **Build:** production-readiness pack (SLA, uptime, rate limits), webhook security doc written for a reviewer who won't touch the sandbox, data-handling/PII answers, one named governed-broker reference and migration runbook.
- **Continue, unchanged:** the quickstart/sandbox work already planned — it's correctly scoped for Solo integrator, just don't expect it to move the dead-deal problem.
- **Stop:** any instinct to fix the post-POC drop-off with better docs or a nicer sandbox — that's optimizing the stage that already works.
- **Don't start:** content or community programs aimed at "developers" broadly — there is no open developer population here to reach; everything routes through existing account relationships.

## Review

Re-read: **2026-12-19** (one quarter out). Early re-read on any of:

- the 7-deal decision-unit coding finishes (do this immediately — it's the load-bearing evidence for this whole map);
- the broker contract or channel model changes (e.g. the API gets unbundled and separately priced — this reintroduces a real buying-mode cut that doesn't exist today);
- a new claims-data regulation lands in a region you sell into;
- a third integration dies or a governed deal closes — either updates the primary segment's confidence directly.

## Quality gate

- Segments: 4 — within range. ✅
- Each segment names an artefact, channel and proof differing from at least one sibling. ✅
- Sizes: no fabricated numbers; every row states the pull method and flags current confidence as inferred pending that pull. ✅ (honest, not "measured" yet)
- Decision unit named per segment, including the anti-segment's "no technical champion" case. ✅
- Evidence floor: **fails** for Primary and Secondary as things stand — both are hypothesis-tier until the 7 deals are actually coded, not just summarized. Flagged explicitly rather than presented as measured. ⚠️
- Anti-segment named and non-empty, and it's an audience (channel-agnostic brokers) devrel's current instinct would otherwise have kept in scope. ✅
- Two-page length: at gate. ✅
- Review date named. ✅

Bottom line on the one open gap: this map's structure and reasoning are solid, but its primary/secondary call rests on an assumption about which broker type the 2 dead deals belong to. Code the 7 deals against the decision-unit questions before committing engineering time to the compliance pack — that's a two-hour task that turns this from a well-argued hypothesis into a measured one.