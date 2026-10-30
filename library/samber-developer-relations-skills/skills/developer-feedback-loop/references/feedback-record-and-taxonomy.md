# Feedback record and taxonomy

Read this before writing the record template or the label set (Step 4).

## Contents

- Record template
- Good and bad record
- Taxonomy starter set
- Dedup rules
- Weighting worksheet

## Record template

One canonical record per distinct problem. Public fields go in the record product and developers both see; private fields go in a linked internal record or a restricted field.

```
Title:            <problem, in the developer's words - never the requested feature>
Problem:          <what the developer was trying to do, and what stopped them>
Requested fix:    <what they asked for, verbatim, kept separate from the problem>
Job / use case:   <the outcome they are after - one line>
Evidence:         <repro or friction steps; verbatim quote with a link to the source message>
Workaround:       none | painful | acceptable   <and what it is>
Severity:         <count per value: blocker N / slows down N / cosmetic N>
Requesters:       <distinct people> / <distinct accounts or orgs>, by segment
Sources:          <channels it arrived through, with links>
Status:           <one value from the status vocabulary>
Owner:            <product owner of the area, once reviewed>
--- private ---
Accounts:         <account IDs, tier, revenue band - never in the public record>
Contact consent:  <who agreed to be contacted for discovery>
```

The title rule does most of the work. A title naming a solution ("Add GraphQL support") invites a yes/no vote on one design. A title naming the problem ("Fetching nested resources takes 6 round trips") invites product to compare solutions, which is the decision product owns.

## Good and bad record

```
// ✗ Bad - a solution as title, mention count instead of people, no evidence, revenue in public
Title: Webhooks retry config!!!
Body: Lots of people on Discord want configurable retries. Acme (big customer, $80k) asked too. +14
```

```
// ✓ Good - problem title, distinct requesters by segment, evidence linked, revenue private
Title: Webhook deliveries lost during our consumers' deploy windows
Problem: Consumers redeploy for 5-15 min; our 3 fixed retries exhaust in ~2 min, events are lost,
         and there is no replay.
Requested fix: "let us configure retry count and backoff" (verbatim, 4 of 7 requesters)
Workaround: painful - poll the events endpoint and diff by hand
Severity: blocker for 2 requesters (payments reconciliation), slows down the rest
Requesters: 7 people / 5 orgs - 3 free, 1 paid, 1 enterprise
Evidence: 3 chat threads, 1 support ticket, 1 tracker issue (links); quote: "we lost 212
          payment.succeeded events during Tuesday's deploy"
Status: under review
--- private: enterprise org = account 4411, renewal in Q2
```

The good record lets product see two candidate fixes (configurable retries, or a replay endpoint) instead of one. That is the conversation DevRel wants product to have.

## Taxonomy starter set

Three axes are labels with one value per record. Two are per-requester fields, rolled up into counts on the record, because one record often spans segments and severities. Add an axis only when a recurring decision needs it.

| Axis | Kind | Values | Who sets it |
|---|---|---|---|
| type | label | feature request, DX friction, docs gap | DevRel at capture |
| area | label | the product's own surface names (API, SDK per language, CLI, dashboard, docs) | DevRel at capture |
| status | label | the status vocabulary in `close-the-loop-replies.md` | product sets needs discovery, planned, not planned, shipped; DevRel sets the rest |
| segment | per requester, rolled up | the segments the company already uses (e.g. free, paid, enterprise, self-hosted, prospect) | DevRel, per requester |
| severity | per requester, rolled up | blocker, slows down, cosmetic | DevRel, per requester |

Bugs, security reports and how-to questions are not types here: they leave this pipe at capture (see Step 3 of `SKILL.md`). Source channel is a field on the record, not a label, because one record collects several.

A two-person team needs these three labels and two fields and nothing more. A forty-label scheme is applied inconsistently by the third week and then distrusted by product.

## Dedup rules

1. Search before creating. Attach a new mention to the existing record as a requester plus a link, never as a new record.
2. Merge on same problem, not same request. Two people asking for "retry config" and "a replay endpoint" because events are lost in deploys share one record.
3. Split on different problems behind the same request. "Add GraphQL" from someone with N+1 fetches and from someone wanting typed schemas are two records.
4. Close duplicates toward the canonical record with a link, so requesters subscribe there and the count concentrates.
5. Count a requester once per record, even if they ask in three channels.

## Weighting worksheet

Product weighs; DevRel prepares the inputs. Never hand over a single score.

| Input | How to fill it | Why |
|---|---|---|
| Distinct requesters | deduplicated people | mention counts reward whoever repeats loudest |
| Distinct accounts/orgs | deduplicated organizations | one team of 12 is one customer's need |
| Segment mix | requesters per segment | shows whether enterprise and long-tail want the same thing |
| Representation | requesters ÷ active developers in that segment, as a range; leave blank when no usage data gives the denominator | a loud 20 can be 0.1% of the base |
| Influence | are requesters maintainers, top answerers, integrators others copy? | a small group can shape what thousands believe |
| Severity and workaround | from the record | a blocker with no workaround outranks a popular cosmetic ask |
| Account value | private, from CRM | legitimate input in a commercial company, never the only one |

The representation × influence filter Evan Hamilton and Tyler Swartz describe from their years at Reddit (Lenny's Newsletter, 2023) is the reference shape: high representation and high influence get acted on; low on both get deprioritized with an explained no. They set the representation bar at 10% or more of the user base; this worksheet keeps a range instead, because developer bases split sharply by segment.
