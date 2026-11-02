## Verdict

**Publishable — as a scale/reliability story, not a before/after case study.**

Helio Diagnostics clears four of the five qualification gates: production traffic (five months, real patient-scheduling load), a named engineer willing to be quoted (Marcus Vance), and — on the numbers you do have — a plausible path to approval. It fails the baseline gate outright: no legacy dashboards means no measured "before," so any "X% faster" or "cut errors by Y%" claim is unsupportable. Per this skill's own fallback for that exact failure: drop the delta claim, publish the scale/architecture story instead. That's a narrower story than a full migration case study, but it's a real one — and the honest framing ("we don't have a before number, here's why, here's what we do have") is itself a credibility signal to the engineer reader this format is written for.

## Evidence ledger

| Claim | Class | Instrument | Window | Who can re-derive it |
|---|---|---|---|---|
| SDK in production 5 months, real patient-scheduling traffic | Reported | Marcus's statement | Since go-live | Marcus / your account records — get the actual go-live date |
| 2.1M events/day | Measured, one-sided | Your telemetry (name the specific dashboard/pipeline) | **Unconfirmed** — need trailing-30-day average vs. a single peak day vs. cumulative | Your telemetry team |
| 99.97% delivery | Measured, one-sided | Same telemetry system | Same open question | Your telemetry team |
| Legacy throughput / error rate | **No evidence — drop** | None ever existed | — | — |
| Marcus willing to be quoted and named | Confirmed, engineer-level only | Direct statement | Current | Marcus |
| Manager / comms / legal sign-off on name, quote, metrics | **Not yet obtained** | — | — | Whoever holds each permission — ask at next contact |

Two things to close before drafting further:

1. **Nail the window on both numbers.** "2.1M events a day" and "99.97% delivery" need to say whether that's a 30-day trailing average, a single representative day, or a cumulative five-month figure. Right now they'd fail publication-gate check #2 (instrument and window stated).
2. **Ask whether Helio's side independently confirms the delivery count.** If Marcus's team can cross-check received events against their own downstream count, "99.97%" stops being a vendor-only number and becomes mutually verified — worth one extra question before you draft results.

## The draft (what it can say today)

**Headline outcome (~60 words).**
> Helio Diagnostics never measured its legacy ingest path — there were no dashboards on it, so there's no before-and-after here. What they can show is where they landed: five months of real patient-scheduling traffic through [Product]'s ingest SDK, running at 2.1 million events a day with 99.97% successful delivery, per [Product]'s own delivery telemetry over [confirm: trailing 30 days / cumulative since go-live].

**The adopter and the system (~120 words).**
> Helio Diagnostics runs patient-scheduling infrastructure for [confirm: number/type of clinics or health systems]. The event stream in question is scheduling traffic — appointment creation, rescheduling, cancellation events, or similar — ingested through [Product]'s SDK since [go-live date]. [One line on the surrounding stack, from Marcus.]

**Before-state and its cost — replaces Section 3, since no numeric baseline exists (~150 words, use Marcus's own words, no numbers).**
This is the section to go back to Marcus for. Ask, in Mom-Test style ("what actually happened," not "was it slow"):
- What specifically prompted the move — an incident, a scaling wall, an on-call pattern?
- What would go wrong on the old path, mechanically (e.g., "backlogged during clinic-opening-hour spikes," "silent drops nobody could see")?
- How often did that happen, even if nobody logged it — weekly, during specific hours, during specific events (EHR sync, insurance verification batches)?

Whatever comes back, write it as his own words, unquantified — per the evidence framework, this is "directional" evidence: drop any number, keep the mechanism.

**Why this technology (~200 words) — open.**
Not yet answered. Ask: what else did Helio evaluate (build in-house, another vendor)? What property decided it? Name at least one thing an alternative did better — a section where every alternative loses reads as fiction.

**What they built (~400 words) — open.**
Ask Marcus for the architecture: named components, where the SDK sits in the pipeline, and — given this is patient-scheduling data — any regulatory or compliance constraint that shaped the design (retry limits, data-handling windows, audit requirements). That last one is a strong, credible detail specific to healthcare infrastructure; worth pushing on.

**Results (~150 words) — the one section you can write now.**
> Since go-live, [Product]'s telemetry shows Helio's pipeline processing 2.1 million events a day, with 99.97% successful delivery, measured over [confirm window]. Helio does not have a comparable figure for its previous system — it was never instrumented — so this is reported as a standalone operating figure, not a before/after delta.

**What it cost and what is unsolved (~200 words) — open.**
Ask for: migration effort in engineer-weeks, any dual-running period, anything that broke during rollout, what Helio deliberately left on the old path (if anything still is), and what still doesn't work. Vendor studies routinely skip this section — it's your cheapest differentiation, don't let it go blank.

**What is next (~70 words) — open.**
Ask Marcus what's on his roadmap for this pipeline.

**One quote to lock in now**, so it isn't lost by publication time — ask Marcus for something specific and dated, not sentiment ("It's been reliable" is not usable; "I haven't had a scheduling-ingest page in five months" is).

## Approval package

Decisions to confirm, with a suggested deadline of two weeks out:

1. **Company name and logo** — check Helio's contract for a standing name/logo clause first; don't assume it covers more than that.
2. **Marcus's quote** — he's already consented verbally. Get it in writing from someone who can actually bind Helio (his manager, at minimum) — his personal enthusiasm doesn't authorize the company name.
3. **Metrics** — the two numbers above, once the measurement window is nailed down; flag that "no legacy baseline" will be stated explicitly in the piece, not glossed over.
4. **Architecture section** — once drafted from the interview, needs Marcus's technical sign-off.
5. **Security/compliance review** — flag this explicitly given the domain: even though the SDK appears to touch scheduling events rather than clinical data, "patient-scheduling traffic" at a healthcare company is likely to trigger a compliance review before anyone external signs off on architecture detail. Ask who owns that review at first contact — don't assume Marcus's yes covers it.

Default if no response by the deadline: publish nothing rather than publish unapproved.

## Gate report

| Check | Status | Note |
|---|---|---|
| Every claim classified | Partial | Ledger above does this; several rows still open pending interview |
| Every number has instrument + window | **Fail** | Window unconfirmed on both telemetry numbers — fix before drafting further |
| At least one limitation published | **Fail** | Section 7 not yet gathered |
| Alternatives section present | **Fail** | Section 4 not yet gathered |
| Every quote verbatim, attributed | Pending | No quote captured yet beyond paraphrase ("happy to be quoted") |
| Approval evidence on file | **Fail** | Only informal engineer-level consent so far |
| Zero unsupported superlatives | Pass (draft above) | Keep enforcing as sections fill in |

## Derivatives

Not yet — hold until approval closes. Given a live sales motion likely exists, the one-page summary is the highest-value derivative once the study clears review; skip conference/webinar material unless a slot already exists.

**Next action:** send Marcus five questions — what prompted the move, what else was evaluated, architecture detail, migration cost, and the exact telemetry window/whether Helio can cross-check the 99.97% figure. That interview pass is what turns this from a two-number scale story into a full case study.