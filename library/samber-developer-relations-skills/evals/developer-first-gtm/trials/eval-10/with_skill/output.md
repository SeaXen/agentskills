# Kelbrook — where to begin

I'm answering this as the complete strategic diagnosis and plan you'd want on your desk Monday, using the developer-first GTM framework straight through. A few inputs I don't have (whether you can attribute API usage to a licensed seat today, what the two lost-conviction renewal accounts actually did or didn't do post-sale) I've flagged as assumptions to confirm in week one rather than blocking on them.

## The diagnosis, in one paragraph

Your motion isn't wrong. A $180K–$400K secrets-management contract, sold to a CISO or platform director, is a legitimate top-down sale — that buyer, that deal size, and a compliance-driven purchase decision are exactly the fit signals for a top-down motion. What's broken is that you're running top-down **without the one thing that motion requires you to build**: a genuine developer experience. You've gated the entire technical surface — docs, API reference, pricing, rate limits, even error pages — behind a lead form, which means the engineers who have to actually run this thing never get to touch it before the contract is signed, and often not meaningfully after either. Two renewals came in flat or down with "our engineers never really used it" — that's not a vague satisfaction problem, it's the textbook failure mode of this exact motion: shelfware. The contract closes, activation never happens, and the renewal conversation has nothing to point at.

You are also currently running the one combination this framework says to refuse outright: **top-down enterprise pricing with no self-serve floor and no free surface.** That's not a metaphor for your situation — it's a literal description of it.

## Assumptions I'm making (confirm week one)

- You can attribute contract-level usage to *an account*, but likely not to *which licensed engineers inside it are actually calling the API* — if that instrumentation doesn't exist, it's your first build item, not a footnote.
- The AE team's targets and comp are tied to closing net-new logos and renewals, not to a "leads captured" metric directly — if the CRO's gate is actually driving a marketing-qualified-lead number that's compensated separately, that's a harder political fight and worth knowing before week two.
- Engineers at prospect and customer accounts today have *no* path to touch Kelbrook — sandbox, docs, API reference — without going through an AE first.

## The motion decision

Widen before committing. Three candidates, ranked, led by the recommendation:

**1. Top-down with developer proof — keep as primary, unchanged in buyer or deal size.**
Money path: CISO/platform director signs after a security and compliance evaluation, same as today. What changes is that "developer proof" stops being optional — a real technical evaluation and a real post-sale activation motion become part of what you're required to build under this motion, not an add-on. Prerequisite already holds: the buyer funds this category today, the market is a concentrated list of known enterprise accounts, and a compliance mandate — not a developer — makes the final call. That's exactly when this framework says to promote the highest-effort motion despite its cost. You're not changing motions. You're finishing the one you're already running.

**2. Developer-influenced sales — reject for now, name the revisit trigger.**
This motion needs an existing free/self-serve account base to roll up and a qualification rule to act on. You have neither — there's no free surface to generate the signal. Revisit only if a genuinely smaller-deal segment shows up later with card-based purchase intent; don't build the machinery for it speculatively.

**3. Bottom-up self-serve as the whole motion — reject outright.**
Fails the value gate on the features that justify $180K–$400K: audit, RBAC, SSO, governance are organizational decisions, not something one developer buys alone. An individual engineer was never going to be the signer here. The mistake isn't "we should have gone bottom-up" — it's conflating *the entry a developer needs* with *the motion that closes revenue*. Those are different questions.

*(Ecosystem-mediated — a cloud marketplace listing — is a real future lever for procurement drawdown with this exact buyer type, but it doesn't touch the renewal problem you actually have. Park it.)*

**Commit:** top-down with developer proof, primary, no secondary motion yet. What you're adding isn't a second money path — it's the entry design that motion has always required and never had.

## Friction gates — the evidence, as it stands today

- **Entry — fails, and it's self-inflicted.** No account, no key, no doc a developer can read without a form. This isn't product friction (infrastructure, approval, a second person) — it's a policy choice made for lead capture. That distinction matters: infra-driven friction is expensive to remove, policy-driven friction is a decision you can change this quarter.
- **Value — partial, which is the useful finding.** A developer can plausibly see real value alone — pull a secret into a service in minutes instead of a `.env` file. The features that justify the enterprise price (rotation policy, audit, cross-service governance) are genuinely org-scale. That's the correct shape for "top-down plus a self-serve entry," not a contradiction in your motion.
- **Spread — probably fine mechanically, untested because access never happens.** Secrets platforms spread naturally: SDK calls committed to service configs, env references in IaC, one team's adoption becoming the next team's dependency. You likely have a real spread mechanic sitting unused because nobody downstream of the signing CISO ever gets a key.

## Entry design — what opens, what stays gated

Name the first-value moment concretely: **an engineer retrieves a real secret into a running service using their own sandbox key, without talking to a human.** Everything between "arrived" and that moment gets audited and cut.

**Open, permanently, regardless of CRO's lead-capture goal:**
- Documentation and the API reference
- Rate limits
- Error and troubleshooting pages
- A scoped sandbox environment with synthetic secrets, provisioned instantly

This isn't a product opinion, it's the specific, named failure mode of gating these four: it "loses technical evaluations silently" — the visitor doesn't fill out the form, they just leave, and you never see the drop-off because there was no funnel to measure it in.

**Stays gated, and this is the argument that gets the CRO to yes:** pricing negotiation detail, ROI calculators tied to an identifiable prospect, case studies, anything that's actually a commercial conversation. The lead-capture goal and the technical-evaluation goal aren't in conflict — an engineer reading your API reference was never going to fill out a "book a demo" form in the first place; you weren't capturing that lead, you were losing that evaluation. Frame it to the CRO as recovering evaluations you're currently forfeiting for free, not as surrendering the gate.

For active sales cycles specifically: give AEs the ability to hand a prospect's engineers a scoped, time-limited sandbox key mid-cycle. That's a top-down motion doing its own required homework, not a self-serve funnel.

## The signal that actually predicts your renewal problem

You don't have a free-to-paid handoff problem — you have no free tier. What you have is the same signal machinery pointed the wrong direction: instead of "when does a free user deserve a sales call," you need "when does a signed account deserve a customer-success intervention, before the renewal conversation, not during it."

Adapt the same signal families to post-sale accounts:
- **Depth** — is any engineer making live API calls, sustained over weeks, not a one-time integration test at kickoff?
- **Spread** — beyond the original champion (often the platform director who signed), how many *distinct engineers* have authenticated?
- **Boundary contact** — has anyone besides the champion touched SSO/RBAC config, hit a rate limit, or opened the audit log?

Write the threshold as one sentence once you have 90 days of real data. Until then, provisional:

> An account is flagged **adoption-at-risk** when fewer than **N licensed engineers** have made a live API call within **90 days** of provisioning, or when the only authenticated user is still the original signer. Flagged accounts are escalated to **Customer Success plus a Product-side technical contact** within **one week**, with a **technical enablement offer** — not a check-in call. Accounts above threshold get nothing extra; don't manufacture touchpoints where usage is already healthy.

This is the exact leading indicator this motion prescribes for itself: *post-purchase developer activation inside bought accounts, within 90 days.* If Kelbrook had been tracking this, the two flat renewals would have shown up as a risk months before the renewal call, not as a surprise inside it.

## Expansion and renewal-risk vectors

Within your existing accounts, name the vector instead of hoping:

| Vector | Trigger | Owner |
|---|---|---|
| More engineers, same team | Second/third engineer authenticates | Product — needs the invite/spread mechanic to exist |
| More teams, same company | New workspace or service on a known domain | CS, working with the platform-director champion |
| More product surface | Org asks about SSO/audit/policy beyond initial scope | Account owner |

Two enterprise blockers to check for in the two flat-renewal accounts specifically:
- **Champion single point of failure** — if the platform director who signed is the *only* engaged contact, that's very likely your root cause. Multi-thread: a second technical advocate plus one manager-level contact is the bar, deliberately so one departure or one distracted quarter can't stall the account.
- **No standardization decision** — was Kelbrook ever actually adopted as the team default, or just mandated and quietly routed around? If engineers had a competitor's self-serve tool they could evaluate in ten minutes and yours took a sales call, guess which one they reached for on the next service.

## Leading indicators (five, tracked from day one)

1. Post-sale developer activation: share of licensed engineers making a live call within 90 days — currently unmeasured; instrument first.
2. Time from contract signed to first engineer API call.
3. Share of accounts with 2+ engaged engineering contacts vs. single-champion accounts.
4. Net revenue retention on the enterprise cohort — read against the **Enterprise SaaS** published band (~110% good, ~130% great; source: Lenny's Newsletter, *What is good retention?*), not a bottom-up band. Two of four renewals flat-or-down puts this cohort well under the "good" line — say that number out loud to your CRO and CEO, it's the sharpest tool you have.
5. Share of technical-evaluation sandbox usage during active deals that converts to signed contracts — this is the metric that answers the CRO's actual fear directly: does opening the entry cost you leads, or does it close more of the ones you already have.

Indicators 1–3 and 5 are self-set baselines — no published study prescribes them for this motion; treat them as adjustable once you have a quarter of real numbers. Indicator 4 is the one sourced figure in the set.

## Refused

State these so nobody re-proposes them next quarter:
- Not a pivot to bottom-up self-serve or freemium — the buyer and deal size don't support it.
- Not disbanding or routing around the AE team — they remain the primary revenue motion.
- Not opening pricing negotiation detail, ROI tooling, or case studies — those stay behind the form.
- Not turning sandbox/doc activity into a new lead funnel — an engineer reading the API reference gets nothing but the API reference. Selling to them the moment they show technical curiosity is the same mistake as contacting a signup on day one, just relabeled.

## Revisit triggers

- Activation data still doesn't move after the entry opens and multi-threading is fixed → the problem is deeper than gating (onboarding, product fit, missing professional services), reopen the diagnosis.
- A real smaller-deal segment emerges with self-serve purchase intent → reconsider developer-influenced sales as a second motion.
- Competitive losses start citing "couldn't get hands-on before we chose" → escalates the urgency of everything above; you'll likely see this from your own AEs' loss notes before it shows up anywhere else.
- Quarterly review of the adoption-at-risk threshold once real N and M numbers exist.

## Where to actually begin, Monday

**Week 1** — Cold-run your own onboarding on a clean machine, exactly as a prospect's engineer would, and time it. Then pull whatever data exists on the two flat/down renewal accounts and try to answer: how many named engineers ever authenticated? If you can't answer that, that gap *is* the first finding, not a blocker to finding it. Talk to the AE and CS owners on those two accounts for the unfiltered version of "engineers never really used it" — access never granted, evaluated a competitor first, champion left, or genuinely tried and gave up.

**Week 2** — Take the "silent exit" framing to the CRO, scoped narrowly: commercial content stays gated, technical content (docs, API reference, rate limits, errors, a sandbox) opens. Bring indicator 5 as the thing you'll both watch to prove it isn't costing leads.

**Weeks 2–4** — Scope the account-rollup and activation-instrumentation build with engineering; this is the prerequisite everything else depends on.

**End of quarter** — Ship the minimum open entry, get 90 days of real activation data flowing, write the adoption-at-risk threshold sentence with real numbers, and bring the full memo — motion, entry, threshold rule, expansion vectors, indicators — back to the CRO and CEO for sign-off as a named decision, not a product-team initiative running quietly in the background.