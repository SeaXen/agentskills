# Prompt panel protocol

## Contents

- [Building the panel](#building-the-panel)
- [The answer key](#the-answer-key)
- [Run rules](#run-rules)
- [Sizing the panel](#sizing-the-panel)
- [Scoring rubric](#scoring-rubric)
- [Ledger row](#ledger-row)
- [Metrics and the re-run](#metrics-and-the-re-run)
- [Worked example](#worked-example)
- [Buying a tracker instead](#buying-a-tracker-instead)

## Building the panel

Draw 20-40 prompts from what developers actually type, in five families:

| Family | Example | Source |
|---|---|---|
| Task | "how do I connect to Acme from Node with TLS" | top docs pages, support tickets |
| Error string | "AcmeError: E_POOL_EXHAUSTED what does it mean" | logs of errors emitted, issue titles |
| Migration | "migrate Acme client v2 to v3" | changelog, migration guide |
| Status | "is acme.connect() deprecated" | removed symbols list |
| Choice | "Acme vs Postgres for time series" | sales and community questions |

- Keep each prompt's wording fixed once the baseline runs. A reworded prompt is a new prompt.
- Collapse near-duplicates: correlated variants inflate n without adding evidence.
- Version the panel. Never compare two periods measured with different panels.
- One row per language client when the code differs: a Python answer key cannot score a Node answer.
- Pick the control design before the baseline (see Metrics and the re-run).

## The answer key

One line per prompt, written before any run:

```
prompt_id | must contain | must not contain | owning docs URL (current)
P07 | acme.Client({tls}) ; acme@^3 | acme.connect( ; acme@2 ; sslmode= | /docs/v3/connect/tls
```

Without a key, "correct" drifts toward whatever the assistant said.

## Run rules

- At least five runs per prompt, per assistant, per mode - this skill's default. Raise it until the rate stops swinging between two batches.
- Run search-on and search-off where the assistant offers both.
- Use a logged-out or fresh profile, with no custom instructions, memory or connected tools. Record the location and plan tier.
- Record the model name and date on every row. A model release mid-panel splits the panel in two.
- Expect the consumer app and the API to answer differently. Measure the surface your users use, by hand, or through the API: scripting a consumer chat app can breach its terms.
- In "auto" search modes, score a run as retrieval only when it shows sources or a search step.

## Sizing the panel

Answers to collect = prompts × runs × assistants × modes. By hand, budget a few minutes per answer including scoring. Through the API, with the must-contain and must-not-contain checks scripted, the default panel takes a day or two, most of it reviewing the flagged answers.

| Panel | Size | Answers | Use when |
|---|---|---|---|
| Minimum viable | 10 core prompts × 5 runs × 2 assistants, search-on; search-off on the 5 worst prompts, one assistant | 125 | a diagnostic baseline under a deadline or a writer's day per week; too small to detect any but very large changes |
| Default | 30 prompts × 5 runs × 3 assistants × 2 modes | 900 | a standing practice with tooling or API access |

Both sizes are this skill's defaults. Grow the panel by adding prompts in families before adding runs: pooled family rates tighten faster than per-prompt rates.

## Scoring rubric

Score every answer on five fields, each settled without taste:

| Field | Values |
|---|---|
| Cited | none / owned docs current / owned docs old version / owned other (blog, repo) / third party (name the domain) |
| Version-correct | yes (every "must contain", no "must not contain") / partial / no |
| Deprecated API present | yes / no |
| Invented API present | yes / no - a symbol that never existed in any version |
| Pipeline | recall / retrieval / fetch, from the tests in pipeline-diagnosis.md |

## Ledger row

```
date | assistant | model | mode | prompt_id | run | cited | version_correct | deprecated | invented | pipeline | likely source | owner
```

`likely source` names the page the wrong fact probably came from. That column becomes the correction list.

## Metrics and the re-run

Per assistant and mode, with n:

- version-correct rate
- deprecated-API rate
- invented-API rate
- owned-current citation rate
- third-party citation share, by domain

Report rates, never a rank position: recommendation lists and their order almost never repeat across runs, while appearance rates over many runs hold up (SparkToro and Gumshoe, 2,961 runs of 12 prompts; independently measured, with a vendor co-author).

Attach an interval to every rate. A Wilson 95% interval suits small n: 2 correct out of 5 spans roughly 12% to 77%, so a single prompt's 5 runs compare nothing. Pool by prompt family: 20 prompts × 5 runs = 100 answers narrows the interval to roughly ±10 points at best, since runs of one prompt are correlated and the effective n sits between 20 and 100. Call a change real only when baseline and re-run intervals do not overlap.

Re-run the identical panel at the agreed horizon, counted from the day the last change went live. Pick the control with the lever:

- **Page-level change**: control = prompts whose owning page was not touched. Report the treated-set change minus the control-set change.
- **Template change** (every page at once): roll out to one section or version tree first, control = the rest. When a staged rollout is impossible, compare against the logged baseline and void the comparison if a model release falls in between.

A change in treated and control sets alike is the model or the index moving, not your fix.

## Worked example

A database vendor deprecated its v2 client a year ago; assistants keep answering with it.

| Prompt | Mode | Runs | Version-correct | Cited | Pipeline read |
|---|---|---|---|---|---|
| connect with TLS from Node | search-off | 5 | 0/5 | none | recall |
| connect with TLS from Node | search-on | 5 | 2/5 | `/docs/v2/connect` ×3, current ×2 | retrieval: v2 page still indexed, same title as v3 |
| E_POOL_EXHAUSTED | search-on | 5 | 1/5 | forum answer from the v2 era ×4 | retrieval: no current error page |
| migrate v2 to v3 | search-on | 5 | 5/5 | migration guide | retrieval works |

Reading: recall is stale and only runtime warnings or a later model fix it; the v2 connect page needs a "superseded by" opener and a distinct versioned title (docs-seo for its index posture); the error string needs a current page; the migration guide works, so its symbol map is the page to link from everything old.

## Buying a tracker instead

Commercial AI-visibility trackers sell the measurement they report. Before trusting one, require:

- the number of runs per prompt, and appearance rates with intervals
- the prompt list, in your developers' words, not generated from keywords
- per-assistant and per-mode breakdowns
- export of raw answers, so you can score version correctness yourself - no tracker scores it

Reject single-run "AI rank" positions, and any tracker that cannot show which prompts it ran.
