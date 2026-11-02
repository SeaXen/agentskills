# Marrowgate feedback intake: record-of-truth decision and routing rules

Source: `developer-feedback-loop` (Steps 2-4 and 6, plus its references).

## 1. Decision

**Don't move GitHub feature requests into the PM tool and close them. Don't merge bugs, security reports and Discord how-tos into the same intake.** I'd change the plan in four ways:

1. **Record of truth.** Marrowgate has open-source SDKs around a closed hosted API. For that shape the skill says to make the public tracker (GitHub issues) the record developers see. Each reviewed request is linked one-to-one from an item in the PM tool. Requesters check one place and product plans in another. The link keeps them the same record.
2. **No "tracked internally, closing".** The requester can't see the PM tool, so the reply gives them nothing to follow. A closed issue also reads as a "no" nobody decided. Feature-request issues stay open until product sets a status, and the reply is a real status (section 5).
3. **Stale bot exemption.** Exempt every issue linked to a PM record from the 30-day stale close. Write this exemption into the contract with product. A bot closing an "under review" request is the silent "later" failure mode.
4. **Three input types leave the loop at capture.** Bugs, security reports and how-to questions each have a faster owner (section 3). Pouring them into the same intake buries the feature requests and puts security text in a tool it shouldn't be in.

The PM team's real goal is that nothing is lost and product sees who asked. This design meets it. Everything reviewed lands in their tool, with enterprise names and ARR attached. Developers keep a public place to subscribe, vote and get notified.

## 2. Why not the PM team's version

| PM ask | Problem | Replacement |
|---|---|---|
| Move every request to the private tool | Developers can't see it, vote or subscribe. The conversation splits in two, and Discord and GitHub requesters never learn the outcome. | Public issue stays the record. PM item links to it. |
| Reply "tracked internally, closing" | Closing reads as a no. There is no decision, reason or workaround, and the requester has nothing to follow. | Keep the issue open. Post `received`, then the real status (section 5). |
| Let the stale bot tidy the rest | Closes requests product hasn't decided, 30 days after the last comment. | Linked issues are exempt. Staleness for the other issue types stays with the issue-queue process. |
| Bugs, security and how-tos into the same intake | Different owners and speeds. Security text can't sit in a broadly readable tool. | Route out at capture (section 3). |
| Enterprise names and ARR in the tool | Fine privately, and a legitimate input for product. | Keep them in private fields only, shown beside requester counts and never folded into one score. Never in the public issue. |

## 3. Routing rules

**Rule 0: don't build intake before product agrees to decide.** Is there a named product receiver who will make decisions on these records? I don't know yet. If nobody has agreed, deliver the contract pitch (section 4) first. A pipe feeding nobody gives the PM team a better-organised pile.

| Input | Where it arrives | Route | Owner | Notes |
|---|---|---|---|---|
| Feature request (GitHub) | SDK repos, about 10/week | Stays an open issue. DevRel dedupes, labels type/area, and links it to a PM item. | DevRel | Status mirrored to the issue label. Exempt from stale close once linked. |
| Feature request (Discord) | Discord | Redirect with the `received` reply, pointing to the existing GitHub issue or a new one filed from the feature-request form. Weekly sweep of threads without a link. | DevRel | Paying accounts and blockers: log on the requester's behalf, with their consent. |
| Feature request (support / sales) | Tickets, calls | Support tags the ticket. The AE writes the problem in the customer's words. DevRel creates or joins the record. | Support, sales, DevRel | Ticket text and prospect names stay in the private PM item. The public issue holds only the problem. |
| Bug | Any channel | Issue queue (SDK bug) or support (API or account). | Support / maintainers | Not a feedback record. A feature request hiding inside a bug report is split off and linked. |
| Security report | Any channel, including public issues and Discord | Private disclosure channel only (security contact / GitHub private advisory). Delete or hide the public post and reply with the private path. | Security owner | Never into the PM tool or any shared intake. |
| How-to question | Discord, issues | Answer in place or point to docs. A recurring how-to becomes a docs-gap record. | Support, docs | If the same how-to appears three times or more, file one docs-gap record. |

Intake form for feature requests:

- Make **problem** a required field. Ask "what were you trying to do when you needed this?" before logging a request that arrives as a solution.
- Make **requested fix** a separate field, and **workaround** a required field.
- Give bug, security and question their own issue-form paths. The security path is a link to the private channel, not a form.

## 4. Contract with product

The decision rights in this contract come straight from the skill's product-contract reference. Product decides what gets built and sets planned, not planned and shipped. DevRel captures, merges, writes the evidence, drafts public wording and tells requesters. Dates in public: only product, only when committed.

```
Developer feedback loop - working agreement (Marrowgate SDKs)

Record of truth:   public GitHub issue per request; linked one-to-one from a PM-tool item
Product receiver:  <named person per area (JS / Python / Ruby / API), plus a backup>
Review:            <per planning cycle>, 60 min, chaired by product
Product promises:  every agenda record leaves with a status; "revisit next cycle" at most twice
DevRel promises:   records meet the template; duplicates merged; agenda sent 3 business days ahead;
                   requesters told within 5 business days of a status change
Out of scope:      bugs -> issue queue, security -> private channel, how-to -> docs/support
Staleness:         issues linked to a record are exempt from the 30-day stale bot
Public statements: DevRel drafts, product approves the reason; no dates unless product publishes them
Missed review:     records stay "under review" with a public note; two misses -> raise to product lead's manager
Review of this agreement: <one quarter out>
```

Pitch to product:

- It is one hour per cycle, already deduplicated.
- It brings discovery contacts they'd otherwise recruit.
- It still puts enterprise names and ARR in front of them, beside requester counts.
- Bring one traced leak, such as a request that arrived through three channels and reached nobody.

## 5. Status vocabulary and replies

Statuses: received, under review, needs discovery, planned, not planned, shipped, duplicate. Product sets needs discovery, planned, not planned and shipped. DevRel sets the rest. Each change gets a reply on the issue and in the channel where the requester asked.

**received** (the replacement for "tracked internally, closing"):

```
Thanks - logged here as <issue link>, where <N> others hit the same problem. Add a reaction and
describe your use case; product reviews these every <cycle>. I will post the decision there.
```

**not planned** (the reply that actually closes an issue, with product-approved reason):

```
Product reviewed this on <date> and won't build <problem fix> this year. The reason: <approved
reason>. Until then, the workaround is <link or "none exists">. If your case isn't covered, say so
on <issue link> - that's what would reopen it.
```

Close the GitHub issue only on `not planned`, `shipped` or `duplicate`, with that reply. Use the skill's templates for under review, needs discovery, planned, shipped and duplicate.

Reply timing:

- `received`: at capture.
- `under review`: when the agenda is frozen.
- Decided statuses: one batch in the week after each review.

Publish a short feedback policy page, linked from every reply and from Discord channel topics. It covers where to post, the status list, what decides priority (votes are one input, not a ballot), and what can't be posted here (bugs, security, support).

## 6. Record template

```
Title:            <problem in the developer's words, never the requested feature>
Problem:          <what they were trying to do, what stopped them>
Requested fix:    <verbatim, separate from the problem>
Workaround:       none | painful | acceptable
Severity:         blocker N / slows down N / cosmetic N
Requesters:       <distinct people> / <distinct orgs>, by segment (free / paid / enterprise / prospect)
Sources:          GitHub, Discord, support, sales (links)
Status:           <one value>
Type / Area:      feature request, DX friction, docs gap / JS SDK, Python SDK, Ruby SDK, API
--- private (PM tool only, never the public issue) ---
Accounts:         <enterprise names, ARR band>
Contact consent:  <who agreed to be contacted for discovery>
```

Count requesters once per record across channels. Reactions and votes are reported beside the requester count, not inside it. A vote spike traced to one outside link counts as one event.

## 7. Hours

At about 10 GitHub requests a week plus Discord volume I don't have, the budget depends on question 2 (hours per week available) and the Discord volume. If the weekly hours divided by requests comes to under about 5 minutes per request, drop logging on behalf for everyone except paying accounts and blockers, and drop the weekly digest.

## 8. Open questions

1. Has a product receiver agreed to decide, and is a review slot available? This sets whether we start with the contract or the intake.
2. How many Discord feature requests arrive per week, and how many hours does DevRel have?
3. Is there a date this must feed (planning cycle, launch)?
4. Who may say no in public, and is a public roadmap allowed? Don't start one until two review cycles have produced statuses.

## 9. First steps

1. **Leak trace.** Sample 20-30 recent requests across GitHub, Discord and support. Check which were captured, reached product, got a decision and had the requester told. Fix the stage that loses the most first.
2. Pitch the contract with the trace's worst row as the opening case.
3. Add the stale-bot exemption label and the issue forms once product agrees.
4. Make the security route live before anything else changes. It's the only item here where a misroute causes harm.