# Arbordyne — account rollup & DevRel attribution: what's actually broken

Three separate defects are stacked here, and the sales ask can't be met until all three are fixed. Patching only the report layer will just produce a confident, wrong number.

## Bug 1: domain-match rollup has no validity check

A 4,100-person "account" is not a company, it's a collision. Two likely causes, and you need to know which before fixing anything:

- **A consumer/free domain is being treated as a company domain** (gmail.com, outlook.com, a regional ISP, a university). This is the far more common cause at PLG-style dev tools where individuals self-serve sign up with personal email. Check first — pull the domain, run it against a maintained free-email blocklist (e.g. the `free-email-domains` list, or HubSpot/Clearbit's equivalent). If it's on the list, this isn't one account, it's thousands of unrelated people who happen to share an email provider.
- **A real domain shared by a large, structurally fragmented org** (a huge enterprise, a government domain, a university with departments that buy independently). If firmographic data (LinkedIn employee count, Clearbit) confirms the company is genuinely that large, the rollup is directionally correct but operationally useless — sales can't run one motion against 4,100 undifferentiated engineers.

The long tail of one-person accounts is the mirror-image failure: real companies fragmented across domain variants (mail subdomains, regional TLDs, an acquired brand's old domain, a typo) that literal string-match on the sending domain never merges.

**Fix:**
- Exclude free/consumer domains from auto-rollup entirely. Route those signups to person-only records with no company rollup until a real signal (billing email domain change, self-reported company field, enrichment hit) promotes them.
- Replace literal domain-string matching with a firmographic identity-resolution provider (Clearbit, ZoomInfo, 6sense) that maps domain → canonical parent company and merges known subsidiary/regional domains.
- Add a rollup-size guardrail: any auto-merged account crossing a threshold (50–100 people is a reasonable trip wire for a B2B dev tool) gets flagged for manual review instead of silently growing. That threshold would have caught this account months before it hit 4,100.
- Re-run identity resolution against the singleton long tail specifically — that's where the highest-value hidden real accounts are sitting misclassified as noise.

This has to happen before the DevRel report, because "account" is the join key the report depends on. Build the report on the current account model and you'll either wildly undercount (one devrel touch lost inside 4,100 rows) or wildly overcount (report says "the account was touched" when it means one stranger who shares a Gmail domain with 4,099 other strangers).

## Bug 2: lead source can't answer a sequencing question

This is the part sales actually asked about, and the honest answer is: **it can't be built on a lead source field, full stop, regardless of how the field is populated.** Reasons, all structural, not data-quality:

- Lead source is a single value on a person record, usually captured once and frequently overwritten by whatever touch fires next through your MAP. It encodes neither "first" nor "last" reliably — it encodes "whatever last wrote to that field."
- It's person-level. The report needs account-level: "did *any* of the people now rolled into this account get touched by DevRel *before* the opportunity existed." One field on one contact can't answer a question about a set of contacts over time.
- It has no timestamp relative to opportunity creation. Even if it correctly said "DevRel," you still can't tell if that touch happened before or after the opportunity was opened without a date to compare against `Opportunity.CreatedDate`.
- It almost certainly has no DevRel-specific value in it at all. DevRel touches — conference talks, GitHub engagement, Discord/community activity, docs/tutorial content, meetup attendance — typically live in tools that never write to the CRM (event platforms, Discord, GitHub, video analytics). If nothing captures these as identifiable, timestamped events tied to a person, the report has no raw material to work from, independent of what fields exist downstream.

**Fix — stop trying to fix this with a field, build a touch log:**

1. Instrument every DevRel-owned surface to emit a person-identified, timestamped, channel-tagged event: conference/meetup registration or badge scan, community (Discord/Slack) join and activity, GitHub org/repo interaction, docs or tutorial engagement, webinar attendance. Each needs a stable identity key (email, or an OAuth-linked handle resolved to email) — this is the same identify()/merge problem as first-party marketing attribution: an anonymous touch is worthless until it's joined to a real person, and a lot of DevRel touches happen on surfaces you don't own (GitHub, Discord, an event platform's own site), so each needs its own capture point: ask for work email at CFP/RSVP, badge scan, OAuth GitHub linkage, community bot capturing verified email on join.
2. Write every touch to a central touch log keyed on person, not into a single overwritable CRM field. Person rolls up to the corrected account (Bug 1's fix) for the account-level view.
3. Keep every touch type distinguishable — you want to be able to say "DevRel" specifically, not "marketing, undifferentiated."

## Bug 3: the report itself should be a computed query, not a stored field

Once the touch log and the corrected account model both exist, the report is a straightforward join, not a manual data-entry problem:

```
For each (corrected) account:
  first_devrel_touch = MIN(touch.timestamp)
                        WHERE touch.channel = 'devrel'
                        AND touch.person IN account.members
  opp_created = Opportunity.CreatedDate for that account
  → qualifies if first_devrel_touch IS NOT NULL
             AND first_devrel_touch < opp_created
```

Use first-touch logic here, not last-touch — sales is asking about causality/sequencing ("before they became an opportunity"), which is a first-touch-shaped question, not a "what closed it" question. Report it as a dashboard/saved view refreshed from the touch log, not a static field someone updates by hand — the underlying data changes as new touches land and as opportunities open, and a stored field will drift stale the way lead source already has.

Also surface **count of touched people per account**, not just a binary flag. One DevRel-touched engineer out of a 4,100-person enterprise and 40 touched engineers out of the same account are very different signals for a procurement conversation, and sales will want that distinction the first time they use this report.

## Backstop: self-reported, because DevRel touches are disproportionately dark

A lot of real DevRel influence is structurally invisible even after instrumentation — a talk watched on YouTube outside any tracked session, a blog post shared in a private Slack, "I saw you at a meetup two years ago." Add a lightweight "how did you first hear about us" capture at signup or as a discovery-call question logged by the AE, free-text plus a pick-list including DevRel-specific options (conference, GitHub, community, docs/tutorial). Use it as a cross-check against the touch-log-derived report, not a replacement for it — where the two disagree, that gap is itself useful information about what your instrumentation still isn't catching.

## Order of operations

1. Diagnose and fix account identity resolution (Bug 1) — nothing downstream is trustworthy until "account" means something real.
2. Stand up the DevRel touch log with identity capture at each surface (Bug 2) — this is new engineering work, not a CRM config change, and it's the actual blocker on the sales ask.
3. Build the report as a computed join over corrected accounts + touch log + opportunity dates (Bug 3).
4. Add the self-reported field as ongoing corroboration.

Until step 2 is done, the report sales wants does not exist in any form — the data was never collected. Say that plainly rather than shipping a report built on lead source that will look authoritative and be wrong.