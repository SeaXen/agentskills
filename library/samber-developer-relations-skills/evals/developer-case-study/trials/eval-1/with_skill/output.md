# Kestrel Freight case study — working package

## 1. Verdict line

**Qualifies, but not yet publishable as a full case study.** Production status (nine weeks live), a measured before/after number, and a named engineer willing to talk are all in hand — three of the five qualification gates clear outright. What's missing isn't fatal, it's undrafted: no alternatives-considered material, no migration/architecture detail, no limitations material, no verbatim quote, and no approval chain started. As it stands today, the honest deliverable is a short metrics-led draft covering sections 1, 2, 3 and 6 of the spine, with sections 4, 5, 7 and 8 flagged open rather than invented. Filling those needs one more pass with Dana, not a new interview.

## 2. Evidence ledger

| Claim | Class | Instrument | Window | Who can re-derive it |
|---|---|---|---|---|
| Dispatch pipeline moved from cron to the workflow engine; live in production | Reported | Deployment/account record | Cutover, ~9 weeks ago | Dana Okafor or the account owner |
| p95 dispatch latency: 8.4 min → 95 sec | **Measured** | Kestrel's Grafana dispatch-latency board | 4 weeks before cutover vs. 4 weeks after | Dana Okafor, or whoever else reads that board |
| On-call load down "about half" | Reported (engineer's estimate, self-flagged as untracked) | None — Dana's impression, no ticket/page count on either side | Undefined | Dana only — not independently re-derivable |
| "Our own usage telemetry" | **Unused** | Our product's telemetry | Unspecified | Whoever pulled it — no specific figure has reached this draft yet |
| Grafana screenshot | **Unused as evidence** — I haven't seen the image, so the 8.4 min → 95 sec figure above is taken on your word, not verified against it | Kestrel's Grafana | — | Confirm the screenshot's axis labels and dates actually say "p95," "4 weeks either side," before this ships |
| What Kestrel evaluated besides the workflow engine (incl. staying on cron) | **Missing** | — | — | Ask Dana — question-ladder rung 5 |
| Migration effort in engineer-weeks, dual-running period, what broke, what stayed on cron | **Missing** | — | — | Ask Dana — rungs 8–9 |
| Naming, quote, and security sign-off | **Missing** | — | — | Whoever owns the Kestrel relationship — hasn't been asked yet |

Two numbers are strong enough to publish today. Everything else in this ledger is either unverified-by-me or not yet collected — not weak, just not here yet.

## 3. The draft

**1. Headline outcome**
> Kestrel Freight's dispatch pipeline used to have a slow tail: the worst 5% of dispatch decisions took 8.4 minutes. Nine weeks after moving that pipeline off cron and onto our workflow engine, the same p95 figure reads 95 seconds — measured on Kestrel's own Grafana dashboard, four weeks either side of cutover.

**2. The adopter and the system**
> Kestrel Freight runs a dispatch pipeline that assigns and routes freight loads across its fleet. Nine weeks ago, the dispatch team — led on the engineering side by Staff Engineer Dana Okafor — moved that pipeline off cron-scheduled jobs and onto our workflow engine.
> `[NEEDS INPUT — fleet size, loads/day or similar scale marker, what else sits in the stack around dispatch. Question-ladder rung 1.]`

**3. Before-state and its cost**
> Before cutover, dispatch ran on cron. Its p95 latency — the slowest 5% of dispatch decisions — sat at 8.4 minutes, per Kestrel's Grafana dashboard. Okafor estimates on-call load has roughly halved since the move, though that number was never instrumented on either side of cutover — treat it as her impression, not a metric to repeat elsewhere in the piece.
> `[NEEDS INPUT — the mechanism. How did cron actually fail? What got paged at 3am, and how often? What did the slow tail cost downstream — late loads, missed pickup windows, a dispatcher manually intervening? Rungs 2–3. Without this, the piece has a number but no failure a reader can recognize in their own system.]`

**4. Why this technology**
> `[MISSING — nothing in hand states what else Kestrel evaluated, including staying on cron or building in-house, or what the workflow engine did better than the alternative. Ask Dana rung 5 directly: "What else did you evaluate, and what did each one do better?" Skipping this section is exactly the skill's own failure mode for turning a case study into an advertisement — and nobody struck it, it was simply never asked.]`

**5. What they built**
> Kestrel replaced its cron-scheduled dispatch jobs with workflows running on our engine.
> `[MISSING — no named components, no build sequencing, no timeline. Ask Dana rung 6: walk through the components, the order they were built in, who worked on it, what surprised them. Ask for whatever architecture diagram she already has internally rather than redrawing this from memory.]`

**6. Results**
> - **p95 dispatch latency:** 8.4 minutes → 95 seconds. Measured on Kestrel's Grafana dispatch-latency dashboard, over the four weeks immediately before and after cutover.
> - **On-call load:** Okafor estimates it's down by about half since the move. This was never tracked as a metric before or after, so it ships here as her stated impression, not a measured figure. If Kestrel can pull even rough page/ticket counts for the same before/after windows, this stops being an estimate.
> `[Our own usage telemetry was mentioned as available — if it has a number worth adding here (job success rate, retry counts, throughput), it goes in this section with its own instrument and window, not folded into the two above.]`

**7. What it cost and what is unsolved**
> `[MISSING — this is the section vendor-published case studies routinely skip, and where this piece would earn the most trust, so it's the one most worth going back to Dana for specifically. Ask: How many engineer-weeks did the migration take? Did cron and the workflow engine run in parallel, and for how long? What broke during rollout? Did any dispatch workloads deliberately stay on cron? What still doesn't work the way they want? Who should not copy this? Rungs 8–9. Right now this piece is missing its most credible section.]`

**8. What is next**
> `[MISSING — ask Dana what's next for the system, in her own words. Rung 10 — "advice to a peer" — is also usually where the actual quotable line lives; that's the same follow-up call that fixes this section and the missing quote below.]`

**Quote:** `[QUOTE PENDING — no verbatim line has reached me, only a paraphrase of what Dana said. Pull the actual sentence from the recording — rung 10 answers are the likeliest source — and drop it in verbatim, with her exact title confirmed on the call. Do not substitute a reconstructed line: a paraphrased quote reads as vendor copy, and an invented one is a fabricated quote.]`

## 4. Approval package

Decisions to send Kestrel, once the drafting gaps above are closed enough to send a full draft rather than fragments:

1. **Company name and Dana Okafor's name/title** — check your contract's publicity/logo clause first; it may already cover this. It covers nothing else below regardless.
2. **The quote** — once pulled verbatim, send for her sign-off; let her edit her own words freely.
3. **The p95 latency figure** — send with the dashboard name and window attached; ask her (or whoever owns that board) to confirm they can vouch for it.
4. **The on-call estimate** — recommend publishing it as an attributed impression, not a headline stat; confirm Kestrel is comfortable with that framing before it ships.
5. **Architecture and limitations sections** — can't go to Kestrel until they exist. Hold this round.
6. **Security/legal review** — ask who else needs to sign off (comms, security, legal) when you send the draft, not after.

Suggested framing: *"If we don't hear back by \<date\>, we publish the shorter version — the measured latency number, the on-call figure as an attributed estimate, no architecture or alternatives sections."* Pick a real date and hold the default rather than letting it slip.

## 5. Gate report

| Check | Status | Why |
|---|---|---|
| Every claim classified | Blocked | The two claims in hand are classified; sections 4/5/7/8 have no claims yet to classify |
| Every number has instrument + window | Partial | Latency number: pass. On-call number: must ship labeled as an untracked estimate, not stated as measured |
| At least one limitation published | Fail | No limitations material collected yet |
| Alternatives section present | Fail | Not asked yet |
| Every quote verbatim | Fail | No transcript text in hand; quote slot left open rather than filled with a paraphrase |
| Approval evidence on file | Fail | Approval track hasn't been opened |
| Zero unsupported superlatives | Pass | None used in the draft above |

Five of seven checks fail or block — this is not ready to send to Kestrel yet, let alone publish.

## 6. Derivatives

Skipped. Derivatives get built from an *approved* study, and this one isn't drafted, let alone approved — building a one-pager off it now would just mean rebuilding it after Dana's follow-up changes the numbers and the missing sections land.

---

**Fastest path to publishable:** one more short call or async thread with Dana covering rungs 5 (alternatives), 8–9 (migration cost, what broke, what's unsolved), and 10 (the quotable line), plus the actual Grafana screenshot and transcript text handed over so the quote and the latency figure can be verified rather than taken on summary. That closes every open bracket above without a new interview cycle.