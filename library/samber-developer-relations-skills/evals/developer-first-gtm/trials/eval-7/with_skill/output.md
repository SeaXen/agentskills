## The real question isn't "how do we fix the PLG funnel." It's "why did we ever call this PLG."

Your own numbers already answered the question your growth lead and sales lead keep re-litigating. 100% of revenue from two SDRs cold-emailing free-tier signups, 0% from a working upgrade button, quarter after quarter — that's not a broken self-serve funnel. That's a fully-functioning **bottom-up lead gen** motion (the free tier exists to generate leads, not revenue) that everyone keeps mis-describing as product-led growth. You don't have a funnel problem. You have a naming problem, and the naming problem is what makes the fight un-endable — growth keeps being asked to fix a motion that was never actually running.

Below is the memo to bring into planning, built the way this decision should be documented: one primary motion, evidence for each gate, a rejection list so the wrong ideas don't come back next quarter, and a qualification rule with numbers instead of vibes.

---

# Developer-first GTM — Ridgepin

## Constraints

- **Business model / paid boundary:** freemium API gateway, ~12,000 free accounts, one paid tier. *(Confirm before finalizing: what specifically triggers the paid boundary today — request volume, routes, environments, SSO/governance, custom domains? And does upgrading require a credit card only, or does the paid tier's price point realistically require a manager's approval or a PO? This single fact decides most of what follows, and it isn't in the prompt — get it before the memo is final.)*
- **Product friction:** low at entry — a free tier with 12k signups means people reach the product without a sales conversation. First real value is almost certainly "my first request gets routed through the gateway and I can see it working" — confirm the actual step count.
- **Response capacity:** two SDRs, already fully loaded — and already the entire revenue engine. This isn't hypothetical capacity to plan around; it's a proven, working channel. Nothing in this memo should defund it.

Run the sales-economics check the skill insists on before touching anything: a rep should return ~4x fully loaded cost. You don't need to model this — two SDRs are 100% of revenue today, so they're already clearing that bar by definition. The question this quarter isn't "should sales exist," it's "are they spending their time on the right accounts."

## Friction gates

- **Entry — passes.** 12,000 people got in with no sales conversation. Whatever the signup flow is, it isn't what's blocking revenue.
- **Value — passes for the individual, but the *purchase* doesn't.** A developer can see the gateway working for their own service alone — that's real, single-developer value. But "the button works and nobody presses it" is the classic signature of a purchase decision that isn't actually theirs to make. Most engineers evaluating an API gateway at work don't have a company card wired to a recurring SaaS bill, and won't expense one without asking someone. The gate that's actually failing isn't discoverability of the upgrade button — it's that the *buyer* and the *signer* are different people, and self-serve checkout assumes they're the same person.
- **Spread — likely passes, weakly.** Gateway config typically ends up in a shared repo (env vars, Terraform, k8s manifests, API keys committed or referenced), so a second engineer on the team usually encounters it. Worth confirming with account data, but this is good news: it means land-and-expand is a real option once an account is landed, not just new-logo growth.

**This is the actual diagnosis:** gate 2 fails not on visibility but on authority. The developer can self-activate the *product*. They cannot self-activate the *purchase*, because someone else controls the budget. That's exactly the gap an SDR closes — they find the person who can say yes — and exactly the gap a bigger "improve activation" button can't.

## Rejected motions

- **Top-down with developer proof** — rejected. No stated existing budget line for "API gateway" at target accounts, no concentrated list of known enterprise targets, and this motion needs a standing sales org plus compliance evidence before the first contract. Way past what a two-SDR team can carry.
- **Ecosystem-mediated** — rejected for now, not forever. No partner or marketplace channel mentioned. Revisit if a cloud marketplace listing becomes viable — procurement drawdown could actually solve the "who has budget authority" problem this memo just diagnosed, better than a bigger self-serve button ever will. Put it on the revisit list, not the roadmap.

## Primary motion

**Bottom-up self-serve as the entry, developer-influenced sales as the motion that actually closes revenue** — which, undecorated, is bottom-up lead gen: the free tier's job is to generate qualified accounts, not to check out on its own. Say this plainly in the planning meeting. It's the single sentence that ends the quarterly argument, because it's not a proposal, it's a description of what your own numbers already show.

Money path: developer signs up free → routes real traffic through the gateway → account shows depth (sustained volume) or spread (a second engineer, a shared config) or boundary contact (hits a limit, looks at SSO/audit pages) → an SDR reaches the account with evidence in hand, not a cold blind email → the actual budget holder signs.

Prerequisite that must hold: someone with spend authority exists in the account and can be found. Verify this against your 40-ish (or however many) paying accounts today — who actually signed, and were they the original signup or someone the SDR found later? If it's almost always someone else, that confirms the diagnosis above.

## Entry design

First-value moment: **a request routed through the gateway with a visible result** (logs, a trace, a passing health check) — name the exact screen this happens on and count the steps to it. Whatever that count is, it isn't the problem — 12k people already got there.

Keep permanently open, never gated: full pricing (real numbers, not "contact us"), all rate limits, docs, and error/troubleshooting pages. If pricing is currently hidden behind "talk to sales," that alone would explain some of the zero — a developer evaluating on their own can't build the internal case for their manager without seeing the number first.

## Handoff rule

**Build this first, before anything else in this memo:** roll signups up to accounts (email domain today, workspace/API-key identity as soon as the product models it). Without this, "qualification" is just "email whoever signed up," which is very likely what's happening to some or all of the 12,000 right now — that's the "contacting on signup" failure mode, and it's the fastest way to burn SDR time and teach developers the free tier is bait.

Once rollup exists, replace "cold-email the list" with a real rule. Draft, to validate against your own conversion history before locking it:

> An account becomes qualified when it has **sent production traffic through the gateway for 2+ consecutive weeks** and either **has 2+ engineers with active API keys** or **has hit a rate/quota limit repeatedly**, or when **anyone in the account views pricing, SSO, or the security/compliance page**. Qualified accounts are contacted by **an SDR** within **24 hours** with **a limits-and-architecture conversation**, not a generic intro call. Accounts below the threshold receive **no human contact** — product and docs only.

*(Self-set, not sourced — the N and M above are placeholders. Pull your actual paying accounts' usage history before their first payment and set the real numbers from that. This is the single most valuable data-pull for next week's meeting.)*

Routing: the engineer who's actually using it gets a technical conversation about limits and architecture, never "15 minutes to learn about your needs." Whoever holds the budget gets a cost comparison against the status quo. If there's a technical champion, they get a short internal case they can defend to their own manager — this is very likely the artifact currently missing, since your SDRs are probably improvising it per deal instead of handing over something reusable.

## Expansion path

- **More engineers, same team** — product-owned. Trigger: a second API key or shared config appears in the account. Needs an invite/share prompt at the moment config is generated, if one doesn't exist.
- **More teams, same company** — SDR/AE-owned with the champion. Trigger: a new workspace or subdomain shows up under a known company domain.
- **More workload per account** — product-owned. Trigger: repeated limit hits, new environment, new region.

Multi-threading rule: no paying account should depend on a single named contact — get a second engineer plus one manager-level contact engaged before calling an account "landed," or the next champion departure resets the relationship to zero.

## Leading indicators

| Indicator | Today | Target | By |
|---|---|---|---|
| Time from signup to first routed request | not measured | measure this quarter | end of next quarter |
| Share of free accounts reaching the depth signal (2+ weeks sustained production traffic) | not measured | baseline, then improve | end of next quarter |
| Share of qualified accounts contacted within 24h | effectively "all 12k, eventually" today | 90% of *qualified* accounts | end of next quarter |
| Free-to-paid conversion at account level, 6-month cohort | not measured (only knows lifetime SDR-attributed revenue) | baseline this quarter | end of next quarter |

Four indicators, all self-set — no published number applies until account-level cohort measurement exists, which it currently doesn't. That measurement gap is itself worth saying out loud in planning: right now nobody can answer "what's our real conversion rate," only "how much revenue did the SDRs close."

## Refused

No blasting every free signup with cold outreach — write the do-not-contact line down and mean it. No "just make self-serve upgrade more prominent" as the fix — the button isn't hidden, the buyer isn't the signer. No cutting the SDR team to "focus on PLG" — they're the only proven revenue motion you have; the goal is to aim them better, not replace them. No enterprise-only motion — there's no evidence of a budget line or a concentrated target list yet.

## Revisit triggers

- Qualified-account volume (under the new rule) exceeds what two SDRs can contact within 24 hours → staff a third, or automate more of the qualification pack.
- A cheaper, self-approvable tier is tested (priced under whatever a typical engineer can expense without sign-off) and self-serve conversion moves off zero → bottom-up self-serve becomes a real secondary motion, not just an entry funnel.
- A cloud marketplace or partner channel becomes reachable → revisit ecosystem-mediated; procurement drawdown may solve the budget-authority gap better than anything above.

---

## What to actually walk into planning with

1. **The reframe, said once, in these words:** "We don't run PLG. We run bottom-up lead gen — the free tier generates leads, sales closes them, and it's working. The fight isn't self-serve vs. sales, it's that we've never written down the rule for how the free tier feeds sales." That sentence should end the recurring argument, because it's not a position to debate, it's what the 100/0 split already proves.
2. **One data pull before the meeting:** for every paying account, who signed the contract, and were they the original free-tier signup or someone else the SDRs found? That number either confirms or kills the "buyer ≠ signer" diagnosis above.
3. **One build commitment:** account rollup (email domain to start). Nothing else in this memo works without it, including "which 12,000 accounts are the SDRs even supposed to be emailing."
4. **One thing to stop doing immediately if it's happening:** cold-emailing all 12,000 signups indiscriminately. If that's current practice, it's actively burning the channel that makes the SDRs effective at all.