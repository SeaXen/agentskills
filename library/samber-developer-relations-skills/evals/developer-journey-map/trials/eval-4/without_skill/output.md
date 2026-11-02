# Orrery journey map — v0.1

**Segment:** data engineers (IC to staff-level, owns pipeline reliability/on-call)
**End state:** production usage of Orrery Cloud — defined precisely in Stage 6 below, not just "signed up"
**Product shape:** OSS Python data-quality library (free, self-serve) → paid Cloud (hosted checks, dashboards, alerting, lineage)

Everything below is a working v0.1 template. Two data blocks (Discovery, Evaluation) are populated with **illustrative figures**, clearly marked — swap in real pulls before this becomes a live artifact. Where a number is real (the 4.1M headline you gave me), it's marked accordingly.

---

## 1. Stage map

| Stage | Data engineer's mindset (JTBD) | Trigger | Primary touchpoints | Signal that they moved forward | Main drop-off risk |
|---|---|---|---|---|---|
| **1. Discovery** | "Is there a Python-native way to catch bad data before it hits prod?" | Pipeline broke on silent schema drift; searching "data quality python library"; HN/Reddit thread; colleague mention; conference talk | GitHub repo, PyPI page, docs site, HN/r/dataengineering, awesome-lists, conference talks | Clones repo or `pip install`s | Generic Google results surface Great Expectations / Soda / Pandera first — Orrery never gets clicked |
| **2. Evaluation** | "Does this actually work on my data, and is it worth switching to?" | Just installed; running against a sample or local dataset | README quickstart, docs Tier-1 guides, GitHub issues/Discussions, comparison content | Runs a second check type or a second dataset; stars/forks the repo | Install works but first check throws a confusing error, or setup takes >10 min |
| **3. OSS adoption** | "This is now part of how my team ships data." | Wires Orrery into CI or an orchestrator (Airflow/Dagster/Prefect) as a recurring gate | CI config, orchestrator provider docs, Slack/Discord community | Repeat installs across version bumps; opens an issue or PR instead of silently forking | Works for one pipeline, never generalized — stays a personal tool, not a team standard |
| **4. Cloud trigger** | "OSS covers my pipeline. It doesn't cover my team." | Hits an OSS ceiling: no shared dashboard, no historical trend, no alerting/paging, no cross-team visibility | In-CLI upsell message, docs "Cloud" callout, OSS-vs-Cloud comparison page | Visits pricing/Cloud docs from OSS docs; starts a Cloud trial | Never notices Cloud exists because OSS docs don't surface it at the point of pain |
| **5. Cloud onboarding** | "Let me see if this is worth the migration effort." | Signs up for Cloud trial, connects first source | Signup flow, "connect a source" wizard, in-app checklist | First scheduled check runs successfully in Cloud | Data-source connection requires credentials/access the IC doesn't have — stalls waiting on a platform team |
| **6. Production (END STATE)** | "Orrery Cloud is how my org finds out about bad data — not a side project." | — this is the destination stage | Cloud dashboards, alerting integrations (PagerDuty/Slack), admin/billing console | See qualifying criteria below | Stays a demo — connected but only pointed at a staging/sample source, never production-tagged |
| **7. Expansion & advocacy** *(beyond end state, brief)* | "Other teams should be on this too." | Renewal approaching; new team asks how the check that caught the last incident works | Internal Slack, case study interview, renewal conversation | Seat count grows without a corresponding sales cycle | Champion leaves the company and the account has no second stakeholder |

**Stage 6 qualifying criteria** (make "production usage" measurable, not a vibe):
- ≥1 data source tagged `production` (not `staging`/`demo`) connected and scheduled (not one-off manual runs)
- ≥4 consecutive weeks of scheduled check runs on that source
- ≥2 active seats (single-player Cloud accounts churn at a much higher rate than multiplayer ones — this is the earliest reliable expansion/retention signal)
- At least one alert routed to a real on-call channel (PagerDuty/Slack), not just viewed in-app

---

## 2. Discovery deep-dive — the data view you asked for

**Headline signal (real number you gave me):** **4.1M all-time combined downloads** (PyPI + npm, life of project). Put this on the README badge, the Cloud landing page, and the first slide of any sales deck — it's the single strongest "this isn't a toy project" signal for a data engineer doing a 90-second credibility check before reading further.

### GitHub unique visitors & clones — trailing 12 months (illustrative)

⚠️ **Read this before you build the real version:** GitHub's Traffic Insights API and UI only retain a **rolling 14-day window** — there is no native way to pull "last 12 months" after the fact. A true YoY view only exists if you've been snapshotting weekly (a cron job hitting `GET /repos/{owner}/{repo}/traffic/{clones|views}` and appending to a durable store — CSV, warehouse table, whatever). If that snapshot job isn't running yet, start it today; everything before "today minus however long you've been collecting" has to be reconstructed from whatever manual exports you already have, or left blank rather than guessed.

The table below is a placeholder shape showing what a healthy trend + narrative looks like once you have real data:

| Month | Unique visitors | Unique clones | Notable event |
|---|---:|---:|---|
| Sep-25 | 8,200 | 3,100 | baseline |
| Oct-25 | 8,900 | 3,300 | — |
| Nov-25 | 9,400 | 3,500 | — |
| Dec-25 | 7,600 | 2,800 | holiday dip |
| Jan-26 | 11,300 | 4,100 | "State of Data Quality 2026" roundup pickup |
| Feb-26 | 15,900 | 5,900 | **Orrery Cloud GA — HN front page** |
| Mar-26 | 14,200 | 5,400 | GA halo effect |
| Apr-26 | 12,800 | 5,000 | — |
| May-26 | 13,100 | 5,200 | PyCon lightning talk |
| Jun-26 | 12,400 | 4,900 | — |
| Jul-26 | 11,700 | 4,600 | summer slowdown |
| Aug-26 | 13,900 | 5,500 | Airflow/Dagster provider blog post |
| **YoY (Aug vs Sep)** | **+70%** | **+77%** | |

Read this row-by-row with your team, not just the trend line: the Cloud GA month should produce a visible step-change in visitors that *clones* only partially follow — visitors spike on any HN/launch traffic, clones are the more honest "someone intends to actually try this" signal. If visitors spike without a clone spike, the launch got attention but not trial intent.

---

## 3. Evaluation deep-dive — PyPI vs npm, which ecosystem is adopting faster

Assuming the JS companion is a thin client/SDK (e.g. `@orrery/report` or similar — swap in the real package name) used for rendering check results in JS/TS pipelines, CI annotations, or dashboards. Core install is PyPI; npm is the secondary surface.

**Don't compare raw counts** — PyPI will always dwarf npm here because the core product is Python-native and the JS package only serves a subset of users. The useful comparison is **growth rate**, which tells you which ecosystem is accelerating, independent of base size.

| Month | PyPI downloads | npm downloads | PyPI MoM | npm MoM |
|---|---:|---:|---:|---:|
| Sep-25 | 210,000 | 9,800 | — | — |
| Oct-25 | 224,000 | 11,200 | +7% | +14% |
| Nov-25 | 231,000 | 12,600 | +3% | +13% |
| Dec-25 | 198,000 | 11,000 | −14% | −13% |
| Jan-26 | 258,000 | 15,800 | +30% | +44% |
| Feb-26 | 289,000 | 22,400 | +12% | +42% |
| Mar-26 | 301,000 | 26,900 | +4% | +20% |
| Apr-26 | 312,000 | 29,300 | +4% | +9% |
| May-26 | 327,000 | 33,800 | +5% | +15% |
| Jun-26 | 334,000 | 37,100 | +2% | +10% |
| Jul-26 | 341,000 | 40,600 | +2% | +9% |
| Aug-26 | 358,000 | 46,200 | +5% | +14% |
| **YoY (Aug vs Sep)** | **+70%** | **+371%** | | |

**What this says:** npm is growing roughly 5x faster than PyPI YoY, off a much smaller base (~13x smaller in absolute volume). That's the classic "leading indicator, not yet the majority" pattern — worth flagging to the team as a signal that JS/TS-based data platforms are picking up the Cloud SDK path faster than the core Python audience is growing, which argues for investing a bit more in JS-facing docs/DX now, before it's the obvious move.

**How to get the real numbers** (both have long native history, unlike GitHub traffic):
- **npm:** `api.npmjs.org/downloads/range/{start-date}:{end-date}/{package}` — full history back to first publish, no retention limit.
- **PyPI:** `pypistats.org` UI caps at ~180 days, but the underlying `bigquery-public-data.pypi.file_downloads` dataset has full history — query that directly for a true 12-month (or longer) pull.

---

## 4. Beyond the end state — Stage 7 in one paragraph

Once a team clears the Stage 6 bar, the next 90 days determine whether Orrery becomes a single-team tool or an org standard: watch for a second team's Slack question ("how did you set up the check that caught last week's incident") as the earliest expansion signal, and make sure the original champion isn't the only person who knows how the account works — single-stakeholder Cloud accounts are the ones that quietly don't renew.

---

*Everything in §2 and §3 is a template populated with illustrative numbers for shape/narrative — replace both tables with real pulls (GitHub snapshot job, npm API, PyPI BigQuery) before using this outside a planning conversation. Re-read this map at the 90-day mark once Cloud usage data exists to validate or correct the Stage 6 criteria.*