# Ecosystem strategy — Northfleet API

**Neither.** Better docs is optimizing a channel that isn't the bottleneck. An app store jumps three rungs past a surface that hasn't proven itself, skips every gate that would justify it, and — for an incident-response product specifically — fights your own value proposition. Run the diagnosis below before spending on either.

## Hypothesis

You don't have one. "We wanted an ecosystem" names no complement, no builder, no mechanism. Forced into shape:

> Because our customers need **[unnamed]** that we will not build, **[unnamed builder]** will build it on our API, earning **[unnamed]**, which makes Northfleet more valuable to **[unnamed buyer]** by **[unnamed mechanism]**.

Every blank is empty. That's not a documentation gap — it's the reason 61 teams pulled a key and 59 of them did nothing with it. You shipped a surface before naming who it was for.

## Evidence

What you have: 9 blog posts, 2 hackathon sponsorships, 1 developer advocate, 61 keys issued, 2 things built, both by one customer, both private.

What you don't have, and what actually decides this: a named list of complements customers asked for. Not "integrations" as a theme — specific things, specific customers, specific dates. You haven't mentioned a single refused feature request, a lost deal, or a customer-built script that predates the API. Fourteen months of supply-side investment with zero demand-side evidence collected is the tell. This is the standard failure pattern: nobody counted demand first, so no amount of marketing around the surface was ever going to produce builders.

## Gates

| Gate | Verdict | Why |
|---|---|---|
| G1 — Counted demand | **Fail** | No named list of five-plus requested complements exists in what you've described. Resolver: pull every support ticket, sales note, and feature request that mentions the API or an integration, going back two quarters. Two weeks. |
| G2 — Externalizable interfaces | **Pass, tentatively** | The API and webhooks exist and are documented. Confirm your own product uses them internally (dogfooding) — if it doesn't, the public surface is quietly second-class. |
| G3 — Identified builders | **Fail** | One real builder in fourteen months, and they built for themselves, not to sell or share. You need three named organizations with their own reason to build, two of them already interviewed. You have zero. |
| G4 — Commoditized complement, not core | **Unknown, and load-bearing** | Depends entirely on what the missing hypothesis names. If the complement is "get incident data into the tools we already run" (ticketing, chat-ops, paging), abundance helps you. If it's detection logic, enrichment, or anything that *is* your differentiation, an ecosystem commoditizes you. Resolve before anything else — this is the one failure no amount of demand fixes. |
| G5 — Staffing | **Fail for rungs 4–6** | A developer advocate is a marketing hire, not a security-review, consent/revocation, or tenant-isolation function. An app store needs a standing team you haven't named. |
| G6 — Envelopment | **Unknown** | Name the platform most likely to bundle "incident response integrations" as a feature — PagerDuty, ServiceNow, and your own observability partners are candidates. Not decisive here, but worth an hour. |
| G7 — Complement readiness | **Unknown** | Not evaluable until G1/G4 are resolved. |

G1 and G3 alone kill any rung above what you already have. G5 alone deletes the app store on its own.

## Rung

**Stay at rung 1** (documented API), and treat the next quarter as evidence-gathering, not a relaunch.

**Rejected — installable third-party apps (rung 5, the "app store").** Deleted by G3 (no identified builder population beyond one internal team), G5 (no security-review, revocation, or tenant-isolation function exists), and the complementor economics below. This is also the least reversible rung on the ladder — removing an app model breaks customers who depend on apps you didn't write. You cannot walk this back once a third party's revenue depends on it, and right now nothing justifies opening that door.

**Not yet — partner-built integrations, listed by you (rung 3).** This is the rung your one real data point actually points at, if it points anywhere: ask that customer's platform team whether they'd let you list what they built, even informally. If they decline, that's information too (see below).

**Not recommended — a "bigger relaunch" of what you have.** More docs, more blog posts, more hackathons is the same lever you've already pulled nine times. It fixes discoverability. Your problem is not discoverability — 61 teams found the API and generated keys. Your problem is that almost none of them had a reason to build. Marketing spend doesn't manufacture a reason.

## Complementor economics

Run the one archetype you have data on: the customer's internal platform team. Their return was avoided cost — solving their own problem — which is exactly what the cheapest complementor archetype looks like. Nothing here supports the independent-software-vendor case an app store requires: an ISV needs a market big enough to fund a product line, and 940 total accounts (61 with keys, 1 with output) is a thin base to ask a third-party vendor to bet a roadmap on. The arithmetic that would justify rung 5 doesn't exist yet, and no messaging fixes a supply problem — this is what the worksheet is for, and you haven't filled it in because you haven't talked to a second or third prospective builder.

## The domain-specific risk nobody's named

Incident-response tooling sells risk reduction. An app store means running third-party code with access to incident data inside your product — more attack surface, more vendors to vet, more blast radius when one of them ships a bug. That's in direct tension with what you sell. If you ever clear the gates above, rung 5 obligations (security review, consent and scopes, revocation, tenant isolation) aren't paperwork here — they're the actual product safety story you'd be asked to defend to every security-conscious buyer's procurement team. Cost that honestly before it's a roadmap line.

It also explains something in your own data: the one customer who built something didn't share it. For a security/IR buyer, keeping integration logic private isn't neglect — it may be a deliberate posture. If that generalizes, your addressable complementor supply for anything above rung 1 could be structurally smaller than a normal devtool ecosystem, independent of demand.

## What to actually do, this quarter

1. Talk to the 61 keyholders. Ask each: what were you trying to do, why did you stop, what would you have needed. This is a two-week project, not a hackathon.
2. Talk to the one customer who built something. Ask the mirror-test question: if Northfleet didn't exist, what would you have done instead? And: would you let us list this, even unofficially? Their answer to the second question is a live signal about G3 and the trust risk above.
3. Pull every refused feature request and lost-deal note mentioning integrations from the last two quarters. That's your real G1 evidence, not a survey.
4. Only after that: decide whether the answer is "build one or two vendor integrations ourselves" (rung 2 — cheap, reversible, and the standard way to discover real demand) or "list what the one customer already built" (a real rung-3 test with an n of one).

## Kill / reopen criteria

- If fewer than five distinct complements surface from step 3 above by the next planning round, close the ecosystem question for two quarters and redirect the developer-advocate role toward the customers you already have, not new key-signups.
- Reopen the app-store question only when: G3 shows three named organizations with their own revenue reason to build (not personas), G4 is resolved in your favor, and you've named an owner for security review and revocation who isn't the developer advocate.
- If the one customer declines to let you even list their integration, treat that as evidence about the category, not about that one relationship — re-weight rung 3 and above down accordingly.

Owner: whoever owns this decision internally. Review date: next planning cycle, explicitly — not "eventually," which is how this question comes back in another fourteen months with the same nine blog posts' worth of nothing to show for it.