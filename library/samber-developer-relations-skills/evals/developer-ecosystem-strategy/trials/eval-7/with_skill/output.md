# Second opinion: Brightwell customer-Python execution — this is a platform bet, not an infra ticket

**Bottom line:** Don't build the gVisor/quotas/metering platform yet. Two named accounts and an 8-engineer team don't clear the bar for a runtime platform (rung 6 on the extension-surface ladder) — that rung's defining trait is a *permanent* standing team, and you don't have one to give it. The quarter estimate almost certainly prices the build, not the forever-obligation that comes after it: patching gVisor CVEs, being on-call for someone else's Python job hanging or misbehaving, and — given a bank and a healthcare group are the two requesters — a BAA and a vendor-risk review cycle you don't currently carry. Before signing up for that, test whether the customer's code can run in *their* environment instead of yours. That turns a quarter of platform engineering into a much smaller ingestion contract, and it's the option a bank and a healthcare org are likely to prefer anyway — neither wants proprietary compliance logic executing on a startup's shared multi-tenant infra any more than you want their PHI/PII-adjacent code executing on it.

Full run below, using `developer-ecosystem-strategy`.

## Step 1 — Hypothesis

The staff engineer's design implies a hypothesis that's currently vague on two blanks:

**As implied** — "Customers want to write Python, so we'll let anyone run arbitrary code on us."

**Forced into shape** — "Because our customers need **validation logic our rule builder can't express (regulatory/compliance-specific checks)** that we will not build ourselves, **the requesting customers' own data engineering teams** will build it on **a Python execution surface**, earning **control over checks that are core to their own compliance posture, without waiting on our roadmap**, which makes our product more valuable to **compliance-owning buyers at regulated enterprises** by **removing the reason those checks get run outside our monitoring pipeline.**"

Commoditized complement: the *validation logic itself*. That's the piece your rule builder currently sells — worth flagging, see G4.

## Step 2 — Gates

| Gate | Verdict | Evidence / resolver |
|---|---|---|
| G1 Counted demand | **Fail** (as ecosystem-scale evidence) | 2 named customers, 1 complement type. The skill's default bar is 5 distinct complements from named customers. That bar doesn't have to be the deciding factor here — but treat "2 requests" as feature-scale demand, not platform-scale demand, and size the investment accordingly. **Resolver:** check the backlog for other unbuilt-rule requests in the last 2 quarters — if it's just these two, that alone argues against a general-purpose platform. |
| G2 Externalizable interfaces | **Fail → architecture project** | Arbitrary Python execution isn't an existing internal capability you'd expose unchanged; it's new. That's consistent with a real build cost, but it also means you're free to design the *smallest* surface, not just accept the staff engineer's default shape. |
| G3 Identified builders | **Pass** | 2 real named orgs, real reason (compliance logic the rule builder can't express). Thin, but concrete. |
| G4 Commoditized complement, not core | **Unknown** | If the rule builder *is* the product's differentiation, letting customers write Python around it risks commoditizing what you sell, not what you don't. If the product's real value is scheduling/alerting/lineage/dashboards and the rule builder is just one input mechanism, this is fine. **Resolver:** ask directly — would Brightwell still be worth paying for if these 2 accounts wrote 100% of their checks in Python? If yes, G4 passes. Owner: product lead, this week. |
| G5 Staffing | **Fail** | 8 engineers total. "A dedicated platform team funded indefinitely" for gVisor sandboxing + quota management + metering is not something an 8-person shop can carry alongside everything else without it becoming the team's permanent center of gravity. This is the gate that should stop the current proposal on its own. |
| G6 Envelopment | **Real alternative exists, not just a threat** | The usual framing is "which bigger platform could bundle this." Here the sharper question is inverted: does the code need to run *inside your infra* at all? Customer-hosted execution (their Airflow/Databricks/Lambda) with results posted back to you is a well-precedented pattern in this exact product category, and it sidesteps needing to build a runtime platform to compete with it. |
| G7 Complement readiness | **Pass, not a blocker** | No external dependency (standards, adjacent vendor APIs) is missing. |

Two gates already decide this: **G5 fails outright**, and **G1 is thin**. Per the skill's own scoring, a fail on staffing means "pick the rung below" — full stop, independent of how good the demand looks.

## Step 3 — Rungs (brainstorm mode, explicitly)

Walking the ladder rather than accepting rung 6 as the only shape:

**Candidate 1 (recommended) — Documented ingestion contract + customer-hosted execution** *(rung 1/2 territory, with a rung-4-style "custom check" concept added to the product)*
- **Who builds:** the requesting customers' own data engineers, running their own Python in their own environment (their warehouse's UDF layer, their own Airflow/Lambda/Databricks job).
- **What you operate:** a schema for registering a "custom check" (schedule, expected result shape) and an ingestion endpoint for results — no code execution, no sandboxing, no quotas.
- **What it forecloses:** almost nothing. Fully reversible with notice.
- **Earliest signal it's working:** first customer-run check reporting into your dashboard/alerting within days of the contract being documented, not months of platform build.
- **Why it fits:** it also solves the customer's own security posture — a bank or healthcare org keeps its compliance logic and data inside its own boundary. You're very likely raising, not lowering, security friction by asking them to hand you the code to run.

**Candidate 2 — Scoped in-product extension point, Brightwell-hosted** *(rung 4, deliberately smaller than the staff engineer's design)*
- **Who builds:** same two customers' teams, but the function is hosted by you.
- **What you operate:** one narrow, versioned contract (e.g., a single-purpose validation function with a fixed input/output shape, hard timeout, hard memory ceiling) — not a general-purpose execution platform. Still needs a safety boundary, but scoped to one job shape, not "run anything."
- **What it forecloses:** the internal seam (the check contract) is now permanent — moderate, not severe.
- **Earliest signal:** one customer's check running reliably in production for a month with no incident.
- **Use only if** candidate 1 turns out to be infeasible — e.g., the check genuinely needs data or timing only available inside your pipeline.

**Candidate 3 — The staff engineer's proposal: general runtime platform** *(rung 6)*
- **Who builds:** anyone, eventually — the design (gVisor, per-tenant quotas, metering) is general-purpose infrastructure, not scoped to these two asks.
- **What you operate:** multi-tenant isolation, resource governance, metering, security review, incident response for other people's code, indefinitely — effectively a second product.
- **What it forecloses:** everything. No walk-back once a bank and a healthcare group depend on it; shutting it down is a migration event for regulated customers.
- **Earliest signal it's working:** hard to get one cheaply — you have to build the whole thing before you learn whether 2 customers' checks even needed this much infrastructure.
- **Recommendation:** park this. Reopen only if candidate 1/2 prove structurally insufficient (see kill/promotion criteria below).

Efficiency order: **1 > 2 > 3**. Value order is the reverse, which is exactly why it's tempting and exactly why it needs gating before committing a quarter to it.

## Step 4 — Complementor economics

Builder archetype here is **customer's internal team**, the cheapest and least demanding of the three archetypes the skill scores — no revenue case needed, only low friction. That argues *for* doing something, but says nothing about which rung; the friction-removal goal is served equally well (better, on security grounds) by candidate 1.

Mirror test: *if we do nothing, what changes for them?* Likely answer — they keep running these checks in tooling you don't see (unsupported glue), and you lose visibility/stickiness on exactly the checks that matter most to a bank or a healthcare org. That's a real reason to act. It is not, on its own, a reason to build rung 6 — candidate 1 captures the same visibility by having them report results to you, without you executing their code.

## Step 5 — Flywheel

Honest answer: there isn't one here, and forcing this into flywheel language would be ecosystem theatre. This is two named accounts with a specific ask, not a complementor market — no founding cohort to recruit, no subsidized side to pick. Treat it as a feature investment decision, not a platform bet, until (if ever) demand broadens past a handful of accounts.

## Step 6 — Obligations, priced by path

This is where the "quarter of work" estimate undercounts the real commitment:

**If you build rung 6 (staff engineer's design):**
- Security review + ongoing patching of a sandbox boundary (gVisor CVEs are a live area) — owner needed, forever.
- Incident response when a tenant's Python job hangs, loops, or triggers a resource-quota fight — arrives as *your* outage.
- **HIPAA exposure:** executing a healthcare customer's code against their data inside your infra plausibly makes you a business associate — a BAA, breach-notification duties, and an expanded HIPAA security-rule program (encryption, audit logging, workforce training) follow from that, not from "just monitoring their data quality."
- **Bank vendor-risk exposure:** executing the bank's proprietary logic on your infra invites a heavier third-party risk review (SOC 2, pen-test reports, possibly a right-to-audit clause) than a SaaS reporting product normally carries.
- Metering/billing support, tenant isolation guarantees, wind-down terms written for a migration event that would hit two regulated customers at once.
- Named owner and 4-quarters-committed capacity out of an 8-person engineering org — that owner is effectively off other roadmap work indefinitely.

**If you build candidate 1 (ingestion contract, customer-hosted execution):**
- Interface stability + deprecation notice on the ingestion schema — small, reversible.
- Support path for "my custom check isn't reporting" — much smaller surface than "your code broke inside our sandbox."
- No BAA trigger, no execution-security review, no per-tenant quota system.

The gap between these two obligation sets is the actual second opinion: the architecture question isn't really "gVisor vs. something else," it's "should this code run inside our boundary at all."

## Kill / promotion criteria

- **Don't start rung 6 now.** Ship candidate 1 first; target: both named customers reporting at least one custom check via the ingestion contract within one quarter, at a fraction of the engineering cost quoted.
- **Promote to rung 4 (Brightwell-hosted, scoped)** only if a customer has a concrete technical reason the check can't run in their own environment (e.g., needs sub-second access to data that only exists mid-pipeline in your system) — get that reason in writing before building.
- **Reopen rung 6** only if all three hold: (a) demand broadens past a handful of accounts requesting *hosted* execution specifically (not just custom logic), (b) you can name a dedicated, funded platform owner for four quarters running — not borrowed time from the 8, and (c) you're willing to sign the BAA/vendor-risk obligations that come with it before the first line of sandbox code is written.
- **Stop the whole line entirely** if, after shipping candidate 1, fewer than 2 checks per account get adopted in 6 months — that would mean the ask was about not-yet-diagnosed rule-builder gaps, not about needing code execution at all.

## Open questions to resolve before finalizing (owner + date, per the skill's own discipline — unknown isn't a pass)

1. Is the rule builder the product's core differentiation, or one of several inputs into scheduling/alerting/dashboards? Decides G4. *Owner: product lead, this week.*
2. Has either customer said *why* the check must run inside Brightwell rather than their own compute — latency, data locality, or just "we assumed that's how it'd work"? *Owner: whoever owns the account relationship, before any build starts.*
3. Do you already have a BAA with the healthcare group, or any HIPAA compliance program in place? If not, that's a multi-month lift on its own, independent of the sandboxing work. *Owner: legal/compliance, this week.*
4. Are there other unbuilt-rule requests in the backlog beyond these two, that would change G1 from "thin" to "real pattern"? *Owner: whoever triages feature requests.*