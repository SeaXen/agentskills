Using the **developer-troubleshooting-docs** skill. The ranking runs on four named frameworks: **KCS** (capture-while-resolving), **OASIS DITA `<troubleshooting>`** (the entry structure), **Nielsen heuristic 9** (error-content usability), and **Google SRE postmortem practice** (the document-vs-fix gate). Below is Step 2 (cluster + rank) and Step 3 (document-vs-fix gate) applied to your 340-ticket pull — this is the ranked queue artifact the skill produces before any writing starts.

Two clusters get merged first: the 61-ticket and 57-ticket "connection refused" tickets are one failure (wrong port) worded two ways by two client versions — that's the skill's own textbook example of "merge clusters that are one failure worded two ways." Combined: **118 tickets**, now your largest cluster.

## Writing order

| # | Cluster | Volume | Shape | Why this slot |
|---|---|---|---|---|
| 1 | `could not connect to server: Connection refused` / `connection to server failed: Connection refused` (merged) | 118 | Error reference entry, both verbatim strings quoted in one block | Highest volume, single cause (wrong port), reproducible in minutes, fully self-serviceable. Best reader-hours-unblocked-per-writing-hour ratio in the set — write it first. |
| 2 | `FATAL: remaining connection slots are reserved` | 84 | Error reference entry | Same efficiency profile as #1: reproducible, single fix, ~4 min support cost today. Second-cheapest win. |
| 3 | `ERROR: could not extend file` (WAL exhaustion, dedicated clusters) | 14 | Error reference entry, causes as successive fall-backs (long-running tx / stuck replication slot / disk full) | Low raw count, but the skill's rule is explicit: *promote a rare-and-expensive cluster when it hits a contract-bound customer in production or shows up in an incident review.* Yours hits both. Write this paired with the engineer who ran that incident review — pull cause and fix straight from the postmortem while it's fresh (KCS capture-while-resolving), don't reconstruct it from memory later. |
| 4 | Branch creation hangs on first use during signup | 22 | Conditional — see below | First-use blocker on the signup-to-first-call path with the worst business outcome in the set (half never return). The rule says promote it above the frequent/reproducible clusters — but it's gated. See "Before you write #4." |

**Coverage target for this cycle:** all four items above (3 solid + 1 conditional). That's full coverage of everything that clears the document-vs-fix gate — the other four clusters are routed away below, correctly, not because they're low priority but because a docs page is the wrong artifact for them.

### Before you write #4

"Hangs forever" with no stated cause is not yet a fact you can document — writing around an undiagnosed hang either produces a page nobody can act on (fails the self-serviceability gate) or documents a defect into permanence. Do this first, same day as starting #1, in parallel, not sequentially:

1. Ask support: is there already a manual workaround being given verbally (retry, refresh, wait N minutes, use the CLI instead of the dashboard)?
   - **Yes** → write it now as a **known-issues entry** (cause: under investigation / confirmed if known; workaround: the steps; tracking: the eng ticket). Cheap, ships today, stops the bleeding.
   - **No** → this is an escalation, not a writing task yet. Flag it to engineering as the top-priority item in this whole set — 22 tickets at 35 min each is real support cost, but the churn (half never come back) is the number that should move engineering, not the ticket count. Hold the page until a cause exists to verify against (Step 7: don't ship steps you couldn't reproduce). Revisit next cycle.

### Routed away from docs — do not queue these for the writer

| Cluster | Volume | Where it goes | Why |
|---|---|---|---|
| `ERROR: permission denied for schema public` | 11 | Changelog entry + confirm removal from any support macros, timed to the 5.0 release | The skill's rule is explicit: a cluster the next release removes is a changelog entry and a product ticket, not a page held in the queue. Writing an entry that dies in four weeks is the wrong use of the hour. |
| Account suspended for non-payment (generic error) | 9 | Product ticket: make the error message name the cause and the fix (e.g. "Account suspended — payment failed, update billing at \<link\>") | Cause is account state, not something a doc page explains better than the error string itself. A doc page here would just be a slower version of fixing the message. Route to product/support-macro, not a public page. |
| `panic: send on closed channel` during failover (all 7 filed within 2 weeks of 4.6) | 7 | Engineering regression report | Textbook "cluster right after a release" — that's a regression to report, not a page to write. First check whether it's already fixed in a later 4.6.x patch; if it recurred after the fix, that's new information for engineering, not a docs gap. |

## What this leaves the writer with, in order

1. Connection-refused (merged) — error reference, both message variants in one block.
2. Connection-slots-reserved — error reference.
3. WAL-exhaustion — error reference, paired with the incident-review engineer.
4. Branch-hang known-issues stub — conditional on the same-day workaround check above.

Items 1–2 are each a genuine "afternoon" per the skill's own estimate: single cause, reproducible in minutes, low verification risk. Item 3 needs an engineer's time alongside the writer's, budget closer to a day including pairing and verification against the actual incident. Item 4 is either an hour (if a workaround exists) or zero writing hours this cycle (if it doesn't — the hour goes into chasing the escalation instead).

Two things I don't have that would sharpen this further: your target ship date for the first batch, and how many writing/verification hours per cycle this one writer actually has. Neither changes the order above, but they'd tell you whether items 1–3 fit in one cycle or need to split across two.