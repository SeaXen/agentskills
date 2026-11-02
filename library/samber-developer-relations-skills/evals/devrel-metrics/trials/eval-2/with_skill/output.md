# Calderon Labs — DevRel instrumentation order, first quarter

## Assumptions I'd otherwise have interviewed for

- **Funded driver:** developer adoption feeding the pipeline (the Series B default for a data-pipeline product). **Reader:** exec/board deciding whether to renew the budget.
- **Adoption motion:** company-led — a developer evaluates self-serve, someone else signs. Funnels still readable at the individual level; revenue answers lag.
- If the budget holder's answer is actually "employer brand" or "product input," tell me — only the primary selection changes, not the build order below.

## What your three facts did to the tier ladder

The default build order is an efficiency ratio (`enablement > engagement > product impact > business impact > reach`), and each of your constraints re-ranks it:

- **Amplitude installed and clean** → collapses the effort on enablement *and* product impact; promotes both. Also flips engagement below product impact — engagement only outranks it when product analytics don't exist yet. Yours do.
- **Two engineering days** → room for exactly two instrumentation spends this quarter. Everything else on the sheet must read data someone already collects.
- **CRM fields closed by sales ops** → deletes business impact outright. Not demoted to the bottom — *deleted*. Influenced pipeline and account-expansion metrics cannot exist without a CRM touch record; a ruled-out metric parked low on the sheet reappears next quarter as scope.
- **Series B reader** would normally *promote* business impact (the only tier that survives a budget review). Since it's deleted, the sheet carries a DevRel Qualified Leads log — the one business-tier metric that needs no CRM — plus a product-impact primary, and publishes the gap.

## The order

**Step 0 — hour zero, no engineering.** Inventory events already firing in Amplitude. A clean install on a data-pipeline product very likely already tracks something like a successful pipeline run — your `first_success` event may exist under another name, which refunds an engineering day. Also freeze the signup-question option list now (see attribution rule).

**Step 1 — engineering day 1, one deploy, ship both:**
1. The **success event** — one specific, instrumented action, definition agreed in writing *before* it ships. For a pipeline product the fight is definitional: connected a source? first run completed? first records landed in the destination? Pick one (I'd argue first completed end-to-end run in the cloud tier), write it down, never change it mid-year — a definition change is a restatement.
2. The **self-reported first-touch question** at signup — one question, fixed options, free-text box. This single field is doing triple duty: attribution instrument, and your Amplitude-native **cohort tag** (accounts naming a program surface = your program cohort), which is what replaces CRM attribution given sales ops' refusal. It also adds no new person↔account link beyond what Amplitude already holds — the identity map that *would* trigger a privacy review is exactly the one that's blocked anyway.

**Step 2 — same week, DevRel hours, zero engineering.** Build the Amplitude charts yourself: signup→success funnel, 30-day retention by monthly cohort, activation compare (program-touch cohort vs all accounts). The cohort must be defined *before* the period starts — which is why the question ships on day 1, not at quarter end.

**Step 3 — engineering day 2, later in the quarter is fine.** Quickstart **step-level events**. First-success rate tells you how many; step drop-off tells you where — it's what makes the primary actionable.

**Step 4 — standing, zero engineering.** Docs search terms with no results (the highest-yield free engagement metric — it names its own fix), the DQL routing log, and a verbatim/friction log with source, date, and fix shipped.

**Not this quarter:** anything touching the CRM or an identity map (blocked anyway), any reach dashboard, any event beyond those three. Scale-out of the taxonomy is next quarter's request to `devrel-analytics`, with proof these three earned it.

## Framework document

*(Spine: driver-anchored — one primary per goal, legible to a budget holder. Journey-stage would fit if the complaint were "we don't know where they leak," but step drop-off covers that; function-split fits only when several people each need an owned number. Swapping spines is cheap today, expensive after the first review. Normally you'd approve each section before the next; validate top-down.)*

### Driver and goals

Funded driver: developer adoption feeding pipeline — owner: you, backed by whoever holds the DevRel budget line.
Goals: (1) more signups reach first success; (2) enabled developers stay; (3) program connections reach the teams that can use them.

### Metric sheet

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|--------|------|------------|--------|----------|-----------|-------|--------------------|
| 1 **P** | First-success rate, 7 days | Enablement | share of new accounts completing the defined first-success event within 7 days of signup | Amplitude, `first_success` | baselining (or backfilled from Step 0 proxy) | set at first review (baseline) | DevRel lead | cold-run the quickstart, fix top failing step before new content ships |
| 2 | Median time to first success | Enablement | signup → `first_success`, median only | Amplitude | baselining | set at first review (baseline) | DevRel lead | read step drop-off, locate the slow step |
| 3 | Step-level drop-off, quickstart | Enablement | share abandoning at each documented step | Amplitude step events + docs | baselining | set at first review (baseline) | DevRel lead | rewrite the worst step |
| 4 **P** | 30-day retention of first-success cohort | Product impact | still active 30 days after first success, by monthly cohort | Amplitude | baselining | set at first review (baseline) | DevRel lead | interview five lapsed accounts before proposing anything |
| 5 | Self-reported first touch | Engagement (instrument) | signup question, stable option list | signup form | baselining | response rate below 40% (hypothesis — circulating figure, not measured) | DevRel lead | shorten or reposition the question |
| 6 | Docs search terms with no result | Engagement | count and top terms per period | docs search log | baselining | top unanswered term goes 30 days without a page (baseline) | docs owner | write the page |
| 7 **P** | DQLs routed | Business impact | connections passed to a named receiving team, per period; log also records whether receiver acted within 30 days | maintained log | baselining | set at first review (baseline) | DevRel lead | review routing quality for patterns |
| 8 | Verbatim and friction evidence | Qualitative | quotes and cold-run findings with source, date, confidence tag, fix shipped | manual log | baselining | fewer than 2 per quarter (baseline) | DevRel lead | schedule two developer conversations |

Pairings: metric 1's counter is metric 4 (success made trivially easy shows up as retention collapse); metric 7's counter is the acted-within-30-days share in the same log. DQL counts stay under ~30/period → report the raw list with dates, never a rate.

### Attribution rule

Written before the day-1 deploy — a rule invented after the quarter is a narrative.

- **Self-reported first touch** is the standing instrument. Report as "self-reported," never as attribution. Option list frozen across quarters; read the free text quarterly.
- **Cohort rule:** program cohort = accounts whose first-touch answer names a program surface (talk/workshop, our content, OSS repo, community). Compare activation and retention vs all accounts. State the bias once: memorable touches over-count, and engaging accounts were likelier to succeed anyway — selection, not proven influence.
- **Tagged links** for artifact-vs-artifact comparison only, never program totals. A large "direct" bucket is normal (~70% of AI-assistant traffic arrives referrer-less — directional, one newsletter's figure).
- **Pre/post lift** reserved for one bounded push — the first quickstart rewrite. Record the pre-period *before* shipping it; near-zero cost on the day, impossible afterwards.
- **Influenced pipeline:** unavailable — no CRM touch fields. If access is ever granted: 180-day lookback before stage 2, "influenced" never dropped, shared credit, rule fixed for the fiscal year.
- No two teams claim the same revenue as *sourced*. We claim none.

### Reporting

- Monthly operational read: metrics 1-3, 5-6, one page, trends only.
- Quarterly decision read: full sheet + qualitative evidence, to the budget holder.
- Five sentences the funder can repeat: "We measure whether signing-up developers get a pipeline running and whether they're still running it 30 days later. Step data tells us where the quickstart loses them. Every signup tells us their first touch, and that answer is how we compare cohorts without the CRM. We route qualified connections to Sales, Product and Recruiting by name and report the routing, not revenue. Pipeline influence needs CRM fields sales ops won't open — the gap is published, and everything else is an input to those numbers."
- **Kill rule, stated in the doc:** any metric that hasn't changed a decision in two consecutive cycles is removed at review. The 20-40% activation band you'll hear quoted is folklore — context only, never a target.

### Known blind spots

- Influenced pipeline and community→expansion: **deleted**, not deferred. Cost to restore: sales-ops cooperation, CRM touch fields, a rule held a fiscal year — and the answer lands 2-4 quarters late even then. DQL routing carries the interim.
- Docs readers who never sign up; word-of-mouth inside companies.
- No community↔account identity map — needs the same blocked CRM.
- Web-side absolute numbers undercount developers badly; every ratio stays inside Amplitude, never compared across sources.

### Review

First review: end of quarter. Thresholds set from the first three periods; metrics still "baselining" after two reviews get killed. Annual: re-derive the sheet from the driver.

## Pass-threshold check

8 metrics (cap) ✓ · all six fields per row, thresholds tagged `baseline`/`hypothesis`, no hypothesis presented as target ✓ · product + business impact present (rows 4, 7) ✓ · no monotonic primary ✓ · "so what" and ownership pass per row ✓ · attribution rule written, methods and cohort lookback named, "influenced" reserved for the unavailable CRM rule ✓ · incentivized volumes counter-paired (1↔4, 7↔acted-share) ✓ · blind spots non-empty ✓

**Where you start, in one line:** the event inventory and the written first-success definition this week — the definition fight is the real work; the deploy is an afternoon.