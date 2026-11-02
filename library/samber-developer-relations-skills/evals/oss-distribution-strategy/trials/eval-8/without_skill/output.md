# Distribution plan: harrowbase, 2027

## Diagnosis first

40k monthly downloads and unprompted doc compliments mean top-of-funnel and individual activation already work. Don't spend the 20 hours/month there.

The break is one specific, narrow step: **individual approval → organizational approval.** Four independent cases (bank, two insurers, logistics) all died *after* a developer already loved the product. That pattern points at risk/procurement gates, not product gaps — regulated, risk-averse industries share the same internal reflex regardless of what tool is being evaluated.

An engineer can win a technical argument alone. They cannot win a security review, a vendor-risk questionnaire, or a "who do we call" objection alone — those get decided by people who never read the docs and don't care how good they are.

**So: distribution in 2027 means removing procurement friction, not increasing awareness.** That's a much smaller, cheaper problem than "grow the community," which is good news given the resourcing.

## Before building anything: confirm the diagnosis (Month 1, ~10h)

The four lost deals are informed guesses right now, not facts. Spend the first block of hours going back to those four engineers (if the relationship survives) and asking exactly where it died: legal, security, budget owner, "no support contract," something else entirely. This is the highest-leverage 10 hours available all year — everything below is a bet on the diagnosis being right, and it costs almost nothing to check before building on it.

## What actually kills bottoms-up OSS deals at companies like these

1. No documented vulnerability disclosure process or patch-response commitment — security review has nothing to point to.
2. No visible support/accountability model — "best-effort community support" reads as unacceptable risk for production use, independent of license.
3. Bus-factor anxiety — "two maintainers, is this abandoned next year?" — with no governance answer on record.
4. No same-industry peer proof — generic logos don't move a risk-averse buyer; "another insurer runs this in production" does.
5. No commercial backstop procurement can cite, even one nobody ends up buying — its *existence* changes the risk calculus more than its price.

Harrowbase has one underused structural advantage here: it's **embedded**. Data never leaves the customer's infrastructure. That kills most of the data-processing-agreement and cloud-vendor-risk questions that sink SaaS analytics tools in the same review. Nobody on the champion's side is currently saying this out loud to the security team — it should be the first line of the trust packet, not a footnote.

## The 12-month plan (~240 hours total)

**Phase 1 — Enterprise trust packet (Months 1–2, ~20h).** Five short documents, published on the docs site, self-serve, no maintainer time per deal:
- `SECURITY.md` with a real disclosure process and a response-time commitment.
- SBOM generation wired into existing CI (automate once, near-zero ongoing cost).
- One-page governance/continuity note: who maintains it, release cadence, funding status.
- One-page procurement FAQ answering standard vendor-risk questions, leading with the embedded/no-data-leaves-your-infra point.
- One-page Apache-2.0 explainer for legal teams unfamiliar with OSS licensing — frame it as *the* reason harrowbase is lower-risk than AGPL/GPL alternatives, not just a fact.

**Phase 2 — A minimal paid support tier (Months 2–3, ~15h).** Doesn't need to be elaborate: an SLA, a named contact, a patch-response commitment, priced to exist rather than to scale. This is the single artifact procurement teams most often need to say yes. It also doubles as the revenue proof-point a March 2027 funding conversation wants to see — "we have a monetizable enterprise motion," not just "we have downloads."

**Phase 3 — Champion enablement kit (Month 3, then maintained ~2h/month).** One-pager and short deck the engineer can forward without ever looping in a maintainer, built persona-first (per sales-enablement practice):
- For the security/compliance reviewer: the trust packet, condensed.
- For the economic/procurement buyer: cost, support tier, risk mitigation, in their language.
- For the champion themselves: the internal-selling ammunition — "here's what to say when someone asks X."
Publish it on the docs site next to the trust packet. This is what makes the motion repeatable without adding to the 20 hours.

**Phase 4 — Peer proof (ongoing, ~5h/month).** One short "how [a regulated company like yours] runs harrowbase in production" piece, anonymized if a named logo isn't obtainable. This is the single most reusable asset in the plan — it feeds the FAQ, the champion kit, and the funding narrative simultaneously. Prioritize getting one from the same industries as the four losses (banking, insurance, logistics) over a flashier but irrelevant logo.

**Phase 5 — Re-approach the four lost accounts (once Phases 1–2 ship, ~5h one-time).** "We've since published the security policy, SBOM, and a support tier you asked about" is a far higher-probability pitch than cold outreach, and it costs almost nothing to send.

## What not to do this year

- Don't invest in Discord/Slack/community growth. Not the bottleneck; notoriously time-expensive to maintain on 20 hours/month.
- Don't run launch pushes (HN, Product Hunt, content marketing) to chase more downloads or stars. Top-of-funnel isn't broken.
- Don't build a partner/integration ecosystem or certification program. Right stage for a platform with third-party builders, wrong stage here.
- Don't build the trust packet from assumption. Phase 0 exists specifically to stop that.

## What to tell the March 2027 funding conversation

Don't lead with downloads — they already prove individual product-market fit and don't need re-proving. Lead with: *we found the exact reason bottoms-up adoption stalls at larger companies, shipped the minimum set of artifacts to remove it, and it's converting.* Track and report:
- Number of enterprise evaluations that reach a security/legal review stage (not just "trials started").
- Conversion rate through that stage, before vs. after the trust packet ships.
- Re-engagement outcome on the four specifically-named lost accounts.
- Support-tier signups, even a handful — proof of a monetizable motion, not just a popular library.

Even one or two of the four previously-dead deals converting, traceably tied to a specific published artifact, is a stronger story than any vanity metric — it shows a repeatable GTM motion, which is what a funding decision is actually underwriting.