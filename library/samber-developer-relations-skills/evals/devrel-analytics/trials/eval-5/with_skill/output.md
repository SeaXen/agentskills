# Refusing the 25% target — and what to build instead

Before the plan: I'm not going to bless 25%, and I'd be doing you a disservice if I quietly built a plan that "proves" it.

**Why the number doesn't survive contact:**

1. **It's a borrowed benchmark.** The 20–40% band is explicitly named in this practice's own list of claims to refuse: "The 20-40% activation band that circulates in developer-marketing content rests on repetition rather than on a measured cohort." Nobody can point you to the study, the cohort, or the definition behind it. It's a number that has been quoted so many times it *sounds* measured.
2. **It's the wrong funnel stage even if it were real.** "Activation rate" in developer-marketing content almost always means *signups → reached-value* (a post-signup behavior: first successful API call, second session, whatever your aha-moment is). Your CEO's ask is *docs visitor → signup* — a pre-signup, top-of-funnel number. These are different stages with different denominators. Docs traffic is dominated by people who are not going to sign up today: existing customers hitting a reference page, people Googling one error message, competitors, students, LLM crawlers. Top-of-funnel docs-to-signup conversion for devtools is routinely low single digits to low double digits, not 20–40%. Importing an activation number into a traffic-conversion slot isn't just unverified, it's the wrong shape of number.
3. **Backing into a traffic requirement compounds it.** "25% × X visitors = target signups" turns one made-up number into a second made-up number (required traffic), which then turns into a real marketing spend or headcount ask justified by fiction.
4. **You have five weeks of data and no confirmed join yet.** Even your own docs analytics can't currently tell you how many of those visitors signed up — that requires the identity spine (below), which doesn't exist yet. A ratio without a verified join is two separately-counted numbers held next to each other, not a conversion rate.

**What I'd put in the OKR instead of a borrowed percentage:**

> Q3: Ship docs→signup instrumentation with a verified identity join (≥80% join coverage) and lock a trailing baseline. Q4: commit to a conversion-rate target set from that baseline, not before.

That's a real, falsifiable OKR you can actually report against in the Q3 review — "instrumented: yes/no, join coverage: X%, baseline conversion rate: Y%" — instead of a number someone will ask you to explain in Q4 and that nobody will be able to defend.

Everything below is the plan that gets you there.

---

# Marrowfield Data — docs→signup tracking plan

Version: 0.1 · Owner: *(you)* · Last verified: *(unset — no trace run yet)* · Review trigger: redesign, docs-generator upgrade, consent-banner change, new surface, quarterly

**Assumptions I made in place of the full interview** (correct any of these and the plan below shifts):

- Adoption motion is individual self-serve (not company-buying) — no `account_id` roll-up below. Tell me if signups are actually per-company and I'll add it.
- Implementer is a web/docs team plus you, not a dedicated data team — effort ceiling assumed to be "occasional web-team ticket," not a maintained pipeline.
- The five weeks of existing docs analytics is a client-side script (GA-class), not a first-party proxy or server logs — flagged as a gap below if wrong.
- No launch or conference sits inside this quarter that would destroy the pre-period — if one does, baseline capture becomes step one regardless of everything else.

## Decisions this plan serves

| # | Decision | Question that settles it | Funnel view |
|---|---|---|---|
| 1 | What Q3/Q4 OKR number to commit to for docs→signup conversion | What is our own trailing docs→signup rate, through a verified join, and what's the realistic quarter-over-quarter move? | Docs-to-signup funnel |
| 2 | Whether the quickstart is the bottleneck worth fixing before the number is worth publishing | Where do docs visitors actually stop before signup? | Docs-to-signup funnel (step-level) |

Only two decisions because this is a single-surface request — everything below serves these two, nothing else.

## Surface register

| Surface | Owner | Data source | Retention | Known bias | Snapshot schedule |
|---|---|---|---|---|---|
| Docs site | web/docs team | existing client-side script (assumed) | tool's own setting | under-counts developers heavily — see correction below | none yet — add daily export of raw event volumes once decided |
| Signup / app | product | signup form → app DB | yours, presumably indefinite | none inherent, but currently not stitched to docs | n/a until identity spine lands |

That's the whole register for this request. Repositories, registries, community venues and CLI telemetry aren't part of this decision and are deliberately left out, not deferred silently.

## The blocked-analytics correction, applied here

Plausible's August 2021 measurement (its own proxied script vs. Google Analytics, on a site carrying Hacker News/Reddit traffic) found **58% of tech-audience visitors blocking Google Analytics** — 68.2% on desktop, 88.3% on Firefox, 82.3% on Linux. If your five weeks of docs analytics is a client-side script, your visitor count is a floor, not a total, and the miss rate is worse on the pages that matter most (install/quickstart pages skew Linux/Firefox-heavy, i.e., exactly the pages most likely to be blocked hardest).

What this means for the OKR conversation specifically:

- **Don't report "docs sessions."** Report step-to-step ratios inside the funnel (visited quickstart → completed step 2 → signed up) — those survive the blocking as long as blocking isn't correlated with the step, which is a checkable assumption, not a given.
- **Don't let anyone divide signups by "total docs pageviews from GA" and call it the conversion rate.** That denominator is missing the developer half of your actual audience, so the resulting rate is inflated relative to reality, in a way that varies page to page — not a constant you can correct with a multiplier.
- **Sanity-check once against server/CDN logs** if you have them, per the trace playbook. If you don't, that's a real gap, not a corner to round off.

## Which instrumentation to build, and in what order

The default efficiency order is: tagging vocabulary → snapshot jobs → self-reported source field → docs event collection → identity spine → log analysis → product events → CLI telemetry. But the skill's own override applies directly here: **"promote the identity spine ahead of everything when any decision on the list asks whether a surface produces signups."** Decision #1 is exactly that question. So:

| Rank | What gets built | Effort | What it buys | Deferred, and why |
|---|---|---|---|---|
| 1 | Link-tagging vocabulary for inbound docs links | ~1 hour | Makes future inbound traffic mergeable; unrepeatable if skipped now | — |
| 2 | Self-reported source field at signup ("How did you find us?") | near-zero | The only signal for talks/podcasts/hallway traffic that will never join | — |
| 3 | **Identity spine: `anonymous_id` set on first docs visit, carried to `user_id` at signup** | ~1 week if docs and app share a domain/subdomain, longer if not | The only thing that answers decision #1 honestly | Promoted out of its normal efficiency-rank position because the decision explicitly requires it — see above |
| 4 | Docs event collection (quickstart steps, not just pageviews), first-party or proxied if consent allows | ~1 week of web-team time | Makes the funnel's step-2 count real instead of a raw pageview | If your existing 5-week script is already first-party/proxied, this is partly done — verify, don't rebuild |
| 5 | Server/CDN log spot-check | ~1 week of data time | Sanity check on the client-side undercounting, not a replacement | Do this once, not as a standing job, unless the client-side gap turns out large |

Repository traffic, registry downloads, community metrics, product-side activation events and CLI telemetry are **deleted from this plan**, not deferred — none of the two decisions above need them. If a future decision does (e.g., "does this docs visitor go on to make a first successful API call"), that's a new decision line and a new instrumentation rung, not scope creep on this one.

## Identity spine

- `anonymous_id`: set on first docs visit, first-party cookie, carried across the docs subdomain and the app subdomain if they differ. **This is the piece that doesn't exist yet** — confirm today whether docs and app already share a root domain (e.g., `docs.marrowfield.com` / `app.marrowfield.com`) or a completely separate domain, since that decides whether this is a 1-week fix or a quarter-long one.
- `user_id`: assigned at signup, emitted alongside `anonymous_id` on the `signup_completed` event so the pre-signup history stitches.
- `account_id`: not applicable — individual motion assumed. Revisit if signups are actually per-company.
- Unresolvable: talks, podcasts, hallway conversations, and any AI-assistant-driven traffic (roughly 70% of which arrives with no referrer and lands in "direct," per Demand Curve #331) — covered by the self-reported field only, not the spine.

## Events

| Event | Surface | Trigger | Properties | Decision # | Verified |
|---|---|---|---|---|---|
| `docs_page_viewed` | docs | page render | `section` (`docs`/`reference`/`guide`), `path`, `anonymous_id` | 1, 2 | no |
| `quickstart_step_completed` | docs | reader reaches the checkpoint that proves the step ran (not scroll) | `step_number` (int), `step_name` (enum), `anonymous_id` | 2 | no |
| `docs_outbound_clicked` | docs | click on a link leaving the docs domain toward signup | `target` (`signup`/`pricing`/`repo`), `anonymous_id` | 1 | no |
| `signup_completed` | app | account created | `anonymous_id`, `user_id`, `self_reported_source` | 1, 2 | no |

Kept to four events because that's what the two decisions need. Don't add `sample_copied` or `docs_search_performed` unless a third decision needs them — the skill's own rule is one screen, and an event with no decision behind it gets cut, not parked "for later."

## Property registry

| Property | Type | Allowed values | Notes |
|---|---|---|---|
| `section` | enum | `docs`, `reference`, `guide` | closed list — extend by plan version bump, not ad hoc |
| `step_number` | int | 1–n, per your quickstart's actual step count | must map to a fixed `step_name` list, versioned if the quickstart is restructured |
| `step_name` | enum | fixed list matching current quickstart steps | renaming a step is a property-value change, never a rename of the event |
| `target` | enum | `signup`, `pricing`, `repo` | closed list |
| `anonymous_id` | string (UUID) | — | no PII, never the user's email or name |
| `user_id` | string (UUID) | — | assigned at signup, never derived from anonymous_id by transformation |
| `self_reported_source` | enum | fixed short list (`search`, `social`, `referral`, `event`, `other`) | stable across quarters so trend comparisons hold |

## Link tagging vocabulary

| Parameter | Allowed values / pattern |
|---|---|
| source | `x`, `linkedin`, `hn`, `reddit`, `newsletter`, `conf`, `podcast`, `partner` (closed list) |
| medium | `social`, `email`, `referral`, `talk`, `sponsorship` (closed list) |
| campaign | `<yyyy-mm>-<artifact-slug>`, lowercase, hyphen-separated |

Lowercase, one separator, tag only links a third party clicks *into* the docs — never internal docs-to-docs links, which restarts the session and overwrites the real source with your own domain.

## Funnel view

**Docs-to-signup funnel** (serves decisions #1 and #2)

- Entry: `docs_page_viewed {path: /quickstart}`
- Steps: `quickstart_step_completed {step_number: 1..n}` → `docs_outbound_clicked {target: signup}`
- Success: `signup_completed`
- Segment by: inbound `source` tag, and separately by whether `anonymous_id` resolved at all (the join-coverage cut)

## Baselines captured

| Metric | Value | Date | Source |
|---|---|---|---|
| Docs sessions (client-side, unjoined) | *(pull your 5-week number here)* | 2026-08-16 – 2026-09-20 | existing script — **not join-verified, floor estimate only** |
| Signups, same window | *(pull from app DB)* | 2026-08-16 – 2026-09-20 | app DB |
| Docs→signup rate from the above two rows | **do not compute yet** | — | the two counts above have no confirmed common identity — dividing them produces a number that looks precise and isn't |

This is the honest state of the baseline today: two volumes sitting next to each other, not a rate. The rate exists the week the identity spine is traced end to end — not before.

## Quality gate

| Check | Threshold | Current | Status |
|---|---|---|---|
| Decision coverage | 100% of events trace to a decision | 4/4 events map to decisions #1–2 | pass |
| Verified traces | 100% of primary conversion events traced end to end | 0/4 | **fail — nothing traced yet** |
| Join coverage | ≥80% of primary conversions resolve to a first touch (this skill's floor, movable) | unmeasured | **fail — spine not built** |
| Tag well-formedness | 100% of published external links validate | unmeasured | not yet applicable — no tagged links published under this vocabulary yet |

## Known gaps

| Gap | Impact on which number | Owner | Decision |
|---|---|---|---|
| Identity spine not built | Docs→signup rate cannot be computed at all, only guessed | *(assign)* | Build before quoting any rate externally, including in the OKR doc |
| Client-side script likely under-counts developers ~58% (Plausible study) | Any "docs sessions" total is a floor, not a total; absolute conversion % will read artificially high if divided by an undercounted denominator | *(assign)* | Move to first-party/proxied collection, or clearly label the number as client-side-only |
| Five weeks of history is short | A rate computed now will be noisy; the skill's own guidance is that volatility calls for a longer window, not a redefinition | you | Extend capture to a full quarter (12 weeks) before locking the Q4 target, not just before the Q3 report |
| No counter-metric proposed yet | A raw conversion-rate target, once it's a target, invites low-quality traffic that inflates the numerator without inflating real adoption (Goodhart/Strathern) | *(assign)* | Pair the eventual target with 30-day retention or activation of the resulting signup cohort before it goes into an OKR |

---

**Bottom line for the CEO conversation:** the honest Q3 OKR is "instrument and verify the join, publish a real trailing baseline" — not a percentage. Once the spine traces clean and you have a full quarter of data, the real number becomes the Q4 target, and it'll be one you can defend in the room instead of one you hope nobody asks about.