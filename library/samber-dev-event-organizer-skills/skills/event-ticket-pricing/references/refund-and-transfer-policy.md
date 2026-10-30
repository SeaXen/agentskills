# Refund and transfer policy: four examples and a checklist

Treat the four worked examples below as examples, never as an industry norm: community technical events have no single standard refund, transfer, or cancellation practice. They share one structural trait - see "What they agree on" - but every other term is answered differently by every one of them. Where the checklist below asks a question the examples do not answer, the organizer decides - do not present a default as though it were a standard.

## Contents

- The four worked policies
- What they agree on
- Decision checklist
- Writing the published wording

## The four worked policies

**PyCon US 2026** (`us.pycon.org/2026/attend/information/`):

- Refunds available until **1 May 2026**, minus a **$50** administrative fee.
- The fee drops to **$25 for student tickets** - the fee itself is tiered to the ticket, not flat across the ladder.
- The fee is **waived entirely** for health and visa reasons.
- **Transfers within the same organization**: allowed at any time.
- **Transfers to a different person outside the organization**: allowed before 1 May 2026; a **$50 fee applies if the two tickets' prices differ**, which is the mechanism that stops a corporate ticket being resold as an individual one.

**EuroPython 2026** (`ep2026.europython.eu/tickets/`):

- Full refund until **7 June 2026**. No administrative fee stated.
- No transfer policy stated on the page at all - silence, not a prohibition.

**RustConf 2026** (`rustconf.com/faq`):

- Refunds available until **23 August 2026** - 15 days before the 8-11 September event - full refund including processing fees.
- A separate, later deadline of **5 September 2026** applies to visa or travel issues only, with the same full-refund terms: hardship gets an extended window instead of a fee waiver.
- Requests received from **24 August 2026** onward: no refund at all, not a reduced one.
- Tickets are **generally non-transferable**; the organizer reviews a transfer only case by case, on request, for "special circumstances."

**KubeCon + CloudNativeCon North America 2026** (`events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/`):

- Refunds available until **26 October 2026** - two weeks before the 9-12 November event.
- A flat **6% processing fee** is deducted from every refund issued in that window - there is no fee-free period, unlike PyCon US or RustConf.
- Refunds are credited only to the original payment card, 7-10 business days after cancellation.
- **Transfers ("Transfer Registration")** are free, self-service, and offered as the default alternative to canceling: attendees sign into their registration and hand the ticket to another named person, no fee and no case-by-case review.

## What they agree on

- **A single dated cutoff.** All four events pick a calendar date (RustConf effectively two: a standard one, and a separate later one carved out for visa and travel issues) after which the ordinary refund terms stop. None of the four grades the refund by how many days out the request lands - there is no sliding scale anywhere in the sample.

That is the only point all four agree on. Everything else is answered differently by every one of them:

- **Fee on refund**: PyCon US and KubeCon both retain one ($50, or $25 for students; 6% of price). EuroPython states none. RustConf charges nothing before its cutoff and refunds nothing after it - the cutoff itself does the job a fee does elsewhere.
- **Hardship accommodation**: PyCon US waives its fee for health and visa reasons. RustConf gives visa and travel issues a later deadline instead of a fee waiver - a different mechanism aimed at a similar risk. EuroPython and KubeCon make no hardship exception at all.
- **Transfers**: KubeCon actively offers a free, self-service transfer as the default alternative to a refund. PyCon US allows transfer with conditions (free within an organization, a fee if the two ticket prices differ). RustConf calls tickets "generally non-transferable" and handles exceptions case by case. EuroPython says nothing about transfers at all.

Four events is still not a distribution large enough to call anything but the dated-cutoff point a default. Treat the rest as a demonstrated range of options, not a ranked list of which is more common.

## Decision checklist

Answer each of these explicitly before tickets go on sale. Record the answer even when it is "none" - a stated silence is a decision; an unstated one is a surprise.

1. **Refund deadline**: which date, and what does it line up with - the catering headcount, the badge print run, the venue's own cancellation curve? All four sourced events use a single dated line, not a formula based on days-out; the cutoffs in the sample sit anywhere from two weeks (KubeCon) to roughly 15 days (RustConf) to a month or more (PyCon US, EuroPython) before the event.
2. **Administrative fee**: retained or not, flat or tiered by ticket price, or a flat percentage of price (KubeCon's 6%) instead of a flat amount.
3. **Hardship waiver**: which reasons waive the fee entirely and who decides, or - as RustConf does it - which reasons get a later deadline instead of a waiver. PyCon US names health and visa refusal; RustConf names visa and travel issues.
4. **Post-deadline requests**: refused outright (RustConf, after its cutoff), or converted into something. KubeCon converts a late cancellation into a free transfer instead; PyCon US and EuroPython offer no credit at all. None of the four sourced events offers a credit toward the next edition - if you do, you invented it, so say so.
5. **Transfer to another person**: allowed, and until when. The sourced range runs from actively encouraged and free (KubeCon) to allowed with an anti-arbitrage fee (PyCon US) to generally disallowed with case-by-case exceptions (RustConf) to unstated (EuroPython). Note the price-difference case explicitly, or a top-tier ticket becomes a resale of a cheaper one.
6. **Transfer within a company**: often looser than person-to-person, since the buyer has not changed. PyCon US allows it at any time.
7. **Scholarship and comp tickets**: transferable or not. A need-gated ticket transferred to someone else defeats the review it went through. Say so on the application page, not afterwards.
8. **Organizer cancellation**: what attendees get if the event does not happen. This is a different question from an attendee changing their mind, and it interacts with contracts and insurance - the term-sheet and risk work lives in `samber/dev-event-organizer-skills@event-sponsor-agreement` and `samber/dev-event-organizer-skills@event-risk-management`, and neither this reference nor this skill gives legal advice.
9. **Where the policy is published**: on the registration page beside the price, not in a confirmation email. A refund policy the buyer sees only after paying is a policy they will argue with.

## Writing the published wording

- One paragraph, one date, one fee, plainly stated. All four sourced policies fit in a few lines each.
- Give the deadline as a calendar date, never a relative window like "30 days before" - unless, like RustConf, the policy genuinely needs two calendar-anchored deadlines for two different causes, in which case state each on its own line.
- State the fee as an amount or a percentage (KubeCon's 6% of price) and name the cases that waive it or get their own deadline, so no one has to ask whether their case counts.
- If transfers are not offered, write that they are not offered. Silence reads as "ask us", and every ask becomes a case-by-case decision an organizer makes under pressure the week of the event.
