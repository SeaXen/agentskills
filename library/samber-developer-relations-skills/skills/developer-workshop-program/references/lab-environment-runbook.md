# Lab environment runbook

## Contents

- Sizing a pre-built environment pool
- Testing
- Customer network checklist
- Security
- Teardown and take-home

## Sizing a pre-built environment pool

One lab-platform vendor (Instruqt) publishes sizing for pre-warmed sandbox pools. Treat its figures as vendor guidance built on its own customers' show rates, not as a study.

| Event                             | Pool size                                    | Start provisioning                | Notes                                                            |
| --------------------------------- | -------------------------------------------- | --------------------------------- | ---------------------------------------------------------------- |
| Live workshop, registration-based | 65-70% of registrations                      | at least 1 hour before            | Nearly everyone joins in the first 15-20 minutes; no auto-refill |
| Multi-day training                | 90-100% of enrolled, one pool per time block | at least 1 hour before each block | Paid or committed attendees show up                              |
| Single prospect or small group    | 1 per track, with an end date a few days out | 1 hour before sharing the link    |                                                                  |

For a single-account workshop with a confirmed attendee list, size from confirmed attendees plus two spares (baseline), not from the invitation list. Large pools provision in batches: time a test pool beforehand and claim one environment from it.

Set the environment time-to-live longer than the full session including breaks. Expired environments lose attendee work.

## Testing

Run an automated play of every checkpoint:

1. Run setup.
2. Run the check: it must fail.
3. Run the solution.
4. Run the check: it must pass.

Run it nightly or on every product release, and within 24 hours before each delivery (baseline). Keep the lab as code in a repository with a development and a production version; a field-owned repo nobody tests decays within a release or two.

## Customer network checklist

Ask in the logistics call, answer in writing before the dry run:

- Must attendees be on a corporate VPN, even on site? A VPN can block a free-tier or trial cluster outright.
- Which outbound domains and ports does the lab need, and are they allowed?
- Do IP allow-lists apply? Addresses change between home and office.
- Are laptops managed, with install rights removed?
- Can attendees sign up to an outside service with a corporate email?
- Who on the customer side can fix any of the above on the day?

Dry run on that network with one onsite attendee running the prerequisites and the first module.

## Security

- Give attendees least-privilege credentials scoped to the lab; keep admin credentials inside setup scripts only.
- Restrict cloud services and regions to what the lab uses; cloud spend bills on top of any lab platform.
- Never put customer data in a vendor-held environment without the customer's written agreement; prefer synthetic data that matches their schema.
- Never collect attendee credentials for their own systems.

## Teardown and take-home

- Destroy every environment after the session; set expiry at creation so nothing depends on someone remembering.
- Give attendees the lab content in a public or shared repository with a "run it in your own account" path and explicit cleanup steps, so nothing keeps billing.
- Offer trial credits for the take-home path when the lab costs the attendee money.
