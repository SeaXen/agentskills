# Pilot protocol and decision record

## Pilot page set

Port the same pages to every candidate. Pick five to eight from the current site:

1. The page with the most custom components or embedded widgets.
2. One generated reference page per spec format, from the real spec or docstrings.
3. The quickstart.
4. One page that differs between live versions, if versions exist.
5. One translated page, if locales exist.
6. The longest page.
7. A customer-only page, if gated content exists.

## Task script

| Task                        | Who                             | Pass threshold (write before the pilot)                      |
| --------------------------- | ------------------------------- | ------------------------------------------------------------ |
| Publish a one-line fix      | Least technical editor, unaided | Done, no developer help                                      |
| Approve from a preview      | Reviewer                        | Preview link exists; nothing went live before approval       |
| Full-size build or import   | Build owner                     | Completes; build minutes recorded                            |
| Ten real search queries     | Anyone                          | Right page in top three for at least eight                   |
| Export                      | Build owner                     | Page count, images and navigation match the source           |
| Old URLs                    | Anyone                          | Ten top-traffic URLs resolve or redirect to the same content |
| Gated page                  | Tester with SSO account         | Hidden logged out, visible logged in                         |
| Proprietary component count | Build owner                     | Recorded; this is the exit-cost evidence                     |

A failed knockout removes the candidate. Score differentiators with the weights fixed in the register.

## Decision record template

```
# Docs platform decision - <site>

Decision: <class> on <product>, owner <name>, live by <date>.
Trigger and root cause: <pain> -> <platform cause | routed elsewhere>.
Requirements register: <table with results per candidate>.
Classes considered: <class> - fell because <interview answer or test>.
Pilot results: <candidate> - knockouts <n/n tested>, differentiator score <x>, components to convert <n>.
Cost: standing <owner hours/month> + subscription multipliers <editors, sites, gated tier>;
      one-off <conversion, redirects, freeze window>; exit <components, export gaps, URL shape>.
Assumptions: <ASSUMED items>.
Revisit trigger: <price or plan change | editors past N | owner leaves | knockout regression>.
Handoffs: redirects and indexing, versions, locales, agent surfaces.
```

## Worked example

Input: API company, 420 pages on a self-hosted generator, OpenAPI reference, two live versions, no locales. Pain: the docs engineer left; upgrades stalled for a year; support staff (5) cannot edit. Customer-only integration guides needed. Live date: one quarter.

Output (abridged):

- Root cause: platform ownership and authoring model, both `this skill`. Findability complaints routed to the structure audit.
- Knockouts: support edit without Git; SSO-gated guides; OpenAPI renders from the spec; two versions with banners; export with assets; top 10 URLs kept.
- Class: hosted docs platform. Self-hosted generator deleted: no build owner (interview Q3). Custom build deleted: no platform team.
- Shortlist: two hosted products that import the current source format. Candidate B dropped at shortlist: gated pages only on a tier procurement refused (vendor-published).
- Pilot: candidate A passed all knockouts; 14 custom components needed conversion, recorded as exit cost.
- Cost: subscription priced as 5 support + 3 engineering editors now, 12 in a year, one site; owner 2 h/month (baseline).
- Revisit trigger: editors past 15, or any plan change on the gated tier.

```
// ✗ Bad - product first, no constraint, no test
"Use <popular generator>; it has versioning and great search."

// ✓ Good - class from a constraint, product from a pilot
"No build owner deletes self-hosting; candidate A passed 6/6 knockouts in the pilot, with 14 components to convert on exit."
```
