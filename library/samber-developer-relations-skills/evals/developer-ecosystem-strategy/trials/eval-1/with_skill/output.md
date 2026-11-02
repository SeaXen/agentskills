# Ecosystem strategy — Keelstack app marketplace

## Bottom line

Don't build a marketplace. The evidence you have doesn't clear the bar for any rung above "we build two connectors ourselves." Below is the decision, the gates that failed, what to ship instead, and — because you already told the board Q3 — language to reset that expectation before it lapses in ~10 days.

## Hypothesis

Forced into the required shape, here's the closest honest attempt:

> Because our customers need *webhook-based migration visibility and Terraform-native provisioning* that we build ourselves, **[no external builder — we build it]** will build them on **[an extended project API]**, earning **[nothing, because there is no external builder]**, which makes our product more valuable to **[IaC- and observability-using platform teams]** by **[removing the two friction points visible at Halvorsen Retail]**.

The builder blank cannot be filled with an outsider. That's not a wording problem — it's the finding. You don't have an ecosystem hypothesis; you have two roadmap items. Sending this back to reword it won't fix it, because no third party with a reason of their own to build has been named.

Commoditized complement, for the record: monitoring visibility and IaC provisioning are pieces every buyer expects and nobody wants to own — genuinely the right kind of thing to give away for free once you're building it. That part of the instinct is correct. It just doesn't require a marketplace.

## Evidence (counted demand)

Everything you can point to:

| Complement | Requested by | Customer type | Repeated? |
|---|---|---|---|
| Monitoring hook | Halvorsen Retail | Paying account | No |
| Terraform provider | Halvorsen Retail | Paying account | No |
| Jira sync | One prospect, during a lost demo | Not a customer; deal lost on price | No |

Three complements. One paying customer behind two of them. The third is the weakest evidence tier this framework recognizes — a sales anecdote from a deal that was lost on price, where the missing integration may not have been the reason at all.

Against 210 paying accounts, that's not "integrations are a top theme" — it's one account with two asks. No unsupported glue, scrapers, or wrapper scripts from customers are mentioned, which is usually the strongest signal of real latent demand. If that evidence exists, go find it before deciding anything else; if it doesn't, that itself is informative.

## Gates

| Gate | Verdict | Basis |
|---|---|---|
| G1 — Counted demand | **Fail** | Needs 5+ complements from named customers, 2+ requested by more than one customer. You have 3, from effectively 1 customer, zero overlap. |
| G2 — Externalizable interfaces | **Fail for anything touching the migration engine; pass for CRUD-only extensions** | The migration engine — the part any monitoring hook or status-aware integration actually needs — is reachable only through an internal Go package. The public API covers project CRUD alone. Rungs 3+ need a stable public seam into the engine that doesn't exist yet. |
| G3 — Identified builders | **Fail** | Zero named organizations with a reason of their own to build against you. Halvorsen wants things built *for* them, not a surface to build *on*. |
| G4 — Commoditized complement, not core | **Provisional pass** | Monitoring/IaC/ticketing glue isn't your differentiated value (safe migrations is). Abundance here wouldn't commoditize you. Moot — G1/G2/G3 already decide this. |
| G5 — Staffing | **Fail** | No security review function, no named partner-queue owner, 14 engineers already carrying the core product. |
| G6 — Envelopment exposure | **Unknown** | You haven't named which larger platform could bundle "managed schema migrations" as a feature. Resolver: name the 2–3 competitors whose marketplace prompted this board question, and state what about Keelstack's migration-safety guarantees they can't trivially replicate. Do this before investing further, regardless of rung — 2 weeks. |
| G7 — Complement readiness | Not evaluated | G1/G3/G5 already decide the case; the external dependencies (Terraform, Jira, webhook consumers) are mature, so this wasn't the blocker. |

Three hard fails and one unresolved gate is a clean "no," the same shape as any honest run of this: most of the time the answer is no.

## Rung

**Recommended: Rung 2 (vendor-built) for the Terraform provider, Rung 1 (documented API + a narrow webhook) for migration events — nothing higher.**

Deleted, not parked:

- **Rung 6 (runtime platform), Rung 5 (installable apps)** — no security review function, no standing team. G5's own rule: this alone deletes both.
- **Rung 4 (in-product extension points)** — the internal seam these would freeze isn't externalized yet (G2 fail), and nothing requested actually needs *behavior changed inside* Keelstack rather than *data moved out of it*. A monitoring hook and a Jira sync are both "move data out," which is rung 1 territory, not rung 4.
- **Rung 3 (partner-built integrations, listed by you)** — this is the one the board is picturing. It's unavailable right now, not just expensive: G1 fails (need 5 complements, have 3; need overlap, have none) and G5 is thin even for its lighter review-and-listing burden. Reopen conditions are below — this isn't a permanent no.

What's left, Rung 1 and Rung 2, is also what your own forcing conditions point to: a near, already-public date (Q3) promotes the rung whose delivery you control outright, which is rung 2. No standing team and no partner-queue owner rule out everything above the documented API on their own.

## What ships instead

1. **Terraform provider (Rung 2, you build and maintain it).** Standard practice for this category — vendor-owned official providers are the norm, not an ecosystem play. Before committing engineering weeks: check how many of the 210 accounts already use Terraform (support tickets, a one-question survey, or your onboarding data) rather than sizing this off one account. If it's genuinely common in your base, build it; if Halvorsen is an outlier, this is still fine as a single-customer retention move, just don't oversell it internally as a platform bet.
2. **A narrow migration-events webhook (Rung 1), not a general API expansion.** Externalize exactly three events — `migration.started`, `migration.succeeded`, `migration.failed` — as the first stable public seam into the engine. This is the Yegge point in miniature: keep the surface small enough that dogfooding it (your own status page or alerting could consume the same webhook) is realistic, rather than exposing the whole internal package. This satisfies the monitoring-hook ask without pre-committing to extension points.
3. **Jira sync: do not build.** Weakest evidence tier, single non-customer, confounded by a price-driven loss. Log it and wait for a second, independent request before it earns engineering time.

## Complementor economics

There's no complementor to price out yet — both things above are vendor-built, which is exactly the finding, not a gap in the analysis. The only "archetype" present is Halvorsen's own internal team, and per the framework, internal teams need no business case, only low friction — which is consistent with shipping a webhook and a provider rather than a partner program. If a real ISV or agency later asks *in writing* to build against you, that's the trigger to re-run this section for real, not before.

## Obligations (what you're actually signing up for)

Even at rungs 1–2, these are real and need owners today, not after Q3:

- **Webhook contract stability** — commit to a versioning policy and a notice period (suggest 90 days) before any breaking change to the three events. Owner: name a senior backend/platform engineer, not "the team."
- **Terraform provider maintenance** — this runs forever against Terraform's own release cycle. Owner: same person or a named second.
- **Roadmap boundary, stated to the board explicitly** — you are not building a marketplace, partner review process, or third-party app model this year. Say the line out loud so it can't be read later as scope creep by omission.
- **Wind-down** — low stakes at this rung (both are reversible, versioned surfaces), but still write "webhook deprecated with 90 days' notice" down now, while it costs nothing.

## Measurement

Baseline today: 0 webhooks live, 0 Terraform provider, 3 total complement requests in two quarters, 0 known unsupported customer glue, 1 lost deal with an unconfirmed integration objection.

Targets:

- Webhook (3 events) and Terraform provider both GA — realistic date is a real Q3/Q4 boundary call once you've done the Terraform-usage check above, not the date already given to the board.
- Track requests for *new* complements per quarter going forward — you need this number populated honestly to ever clear G1.
- No ecosystem-level metrics (concentration, complementor activation) — there's no ecosystem yet; tracking them now is measurement theatre.

## Reopen conditions for an actual marketplace

Written now, while saying no is cheap:

- Five or more distinct complements requested by five or more distinct **paying** customers within two quarters, with at least two requested by more than one customer (clears G1).
- A named ISV, agency, or adjacent vendor asks in writing to build against Keelstack (clears G3).
- The migration-engine event surface (not just CRUD) is externalized and dogfooded internally (clears G2).
- A named owner exists for security review and partner escalation, with committed capacity for four quarters, not a launch project team (clears G5).
- G6 is resolved and Keelstack's migration-safety guarantees are shown to be non-generic to whichever platform could bundle this category.

Owner: you. Review date: pick a date after the Terraform-usage check above lands, not before.

## What to tell the board

Today is September 20 — if Q3 means the calendar quarter, that deadline is about ten days out. No version of this analysis gets a real marketplace shipped by then, and trying to fake one in ten days is how you end up with the failure mode this framework calls "ecosystem theatre": a partner page with nothing behind it, which reads worse to a sophisticated buyer than no page at all.

The credible move is to go back now, not in ten days, with: "We looked at what a marketplace would actually cost to run responsibly — security review, revocation, an unwithdrawable commitment to whoever builds on it — against what we could actually point to in demand: three requests, one customer. Instead we're shipping the two things that customer actually asked for this quarter, and we've written down exactly what would justify a real marketplace so this isn't a guess next time it comes up." That is a stronger board story than "we have one," because it's falsifiable and dated, and it directly answers "why don't we have one like our competitors" with a reason instead of a promise.