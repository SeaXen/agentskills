**Core move: ship a signed methodology doc before next quarter closes. Rulebook kills spreadsheet. Full doc below, paste-ready.**

## Why the $1.2M dies under questioning

- Post-hoc correlation: "closed account had a workshop attendee" proves influenced at best, not sourced. First analyst who asks "attended when? who attended? was sales already in there?" kills it.
- Unrepeatable: rule lived in one person's head. Next quarter, different assembler, different rule. Trend line becomes noise.
- 8-month cycle: last quarter's closed deals reflect DevRel work from 1-4 quarters earlier. A quarterly closed-won number measures the past, and measures it badly.
- Defensible = strict eligibility + captured-at-the-time data + signed definitions. Not a smaller number — an auditable one.

## The document

> # DevRel Revenue Attribution Methodology — v1.0
>
> **1. Purpose and ownership**
> - Measure DevRel contribution to revenue under rules fixed in advance.
> - Owner: [you]. Number produced by RevOps from CRM. DevRel supplies activity data only. No DevRel-built spreadsheet counts as a source.
>
> **2. Revenue basis**
> - Closed-won ACV, new business, booked at close date. Expansion and renewal reported as separate lines, never merged in.
>
> **3. Credit tiers**
> - **Sourced**: a DevRel activity is the first recorded touch on the account, with no prior SDR outbound or marketing touch. Full ACV.
> - **Influenced**: at least one qualifying DevRel touch (§4) on an opportunity contact role, any time between account first touch and close. Full ACV, labeled influenced.
> - **Supported**: DevRel joined an active deal at sales' request (POC help, technical eval, exec workshop), logged on the opportunity.
> - Sourced is a strict subset of influenced. Headline number is sourced; influenced is context, never summed with it.
>
> **4. Qualifying touch**
> - Activity must exist as a CRM campaign object with member status "attended." Registration alone never counts.
> - Attendee must match the account by work domain and be an opportunity contact role, or hold a buying-committee title there. Attendance by a random employee is not a touch.
> - Personal-email attendees go to a weekly triage queue. No identity match, no touch, no credit.
>
> **5. Attribution window**
> - Touches eligible from account first touch to close. No quarter-boundary cuts.
> - Every report carries the lag note: this quarter's closed-won reflects DevRel work started 1-4 quarters earlier.
>
> **6. Credit arithmetic**
> - Full credit within tier, no fractional weights. Deal count is too low for multi-touch math to mean anything; fractions invite argument without adding truth.
> - **Non-additivity clause (CRO signs this line):** attribution is not additive across functions. Sales, Marketing, and DevRel may each claim the same closed dollar under their own definitions. Summing department claims is prohibited — the total exceeds 100% by construction.
>
> **7. Self-reported source**
> - Free-text "How did you first hear about us?" at demo request and opportunity creation, stored on the contact.
> - A self-reported DevRel mention (community, event, content) counts as a qualifying touch even when tracking missed it. This is the only window into community and word-of-mouth, which is where DevRel actually works.
>
> **8. Quarterly process**
> - RevOps pulls closed-won plus campaign membership, drafts tier assignments.
> - Adjudication, 30 minutes: you, RevOps, one AE. Tier disputes resolved by rule, never negotiation.
> - Random audit: five deals per quarter, full touch trail shown — who, which event, when, which campaign object.
> - Freeze: numbers lock one reporting cycle after adjudication. Later corrections appear as an explicit restatement delta, never a silent overwrite.
>
> **9. Governance**
> - v1.0 signed by CRO, RevOps lead, and owner. Any change ships as a new version with restated history, both shown side by side.
>
> **10. Known limitations**
> - Influenced is correlation: presence on winning journeys, not proof the deal dies without us.
> - Community activity is undercounted — credit requires identity match; GitHub and Discord personas slip through.
> - Excluded by design: booth drop-bys, newsletter opens, no-show registrations.

## Rollout

1. Draft the doc. Half a day.
2. 30-minute sign-off with CRO + RevOps lead. Definitions agreed before any data work — automating an undefined process produces garbage faster.
3. RevOps builds campaign objects + check-in capture. 1-2 weeks.
4. Add self-reported field to demo form + opportunity creation. 1 day.
5. Rebaseline last quarter under v1.0, ~2 hours if campaign data exists. Likely caveat: check-ins may not have been captured for those workshops — baseline via registration + contact-role match, flagged as weaker evidence.
6. First quarterly one-pager ships at next close.

On the $1.2M itself: don't fight it. Recompute under v1.0, expect sourced to land well below, relabel the old figure as "influenced, prior loose rule." Pitch to CRO, one line: same work, honest labels — the strict number survives Finance, the big number dies in the first audit.

## Quarterly one-pager format

- Sourced $ (headline), N deals
- Influenced $, N deals
- Supported $, N deals
- DevRel-sourced pipeline created this quarter (leading indicator)
- Touch coverage: % of closed-won and % of open pipeline
- Method version, adjudication notes, restatement deltas, lag note

Next: block 30 min with the RevOps lead. Bring tier definitions and the non-additivity clause — nothing else needed for that meeting.