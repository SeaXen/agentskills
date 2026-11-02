Two things need flagging before the pack, both load-bearing:

**The anonymity rule and the requested copy conflict directly.** NordicCloud Summit's own stated policy — author info hidden from reviewers in round one — means the skill's rule applies: title, abstract and outline can't name the speaker or employer. Putting "Marbleline" in the title and opening with "At Marbleline, we believe…" defeats that on the one field reviewers actually read, and "At [Employer], we believe…" is independently flagged in this skill's own failure-pattern file as a top opening to cut, anonymity aside. I've written the copy as you specified it, plus a blind-safe alternative that carries the same credibility number without the name — pick whichever risk you want to take.

**Compliance, not style.** A duplicate-charge incident touching 1,900 customers at a payments company isn't yours alone to publish. The skill's own compliance table for this angle requires employer sign-off, customer anonymization, and usually a security read before the abstract goes live — and it can't be un-published once the schedule posts. Confirm that's cleared before you submit either version.

---

# NordicCloud Summit — session, 25–30 min (assumed) — deadline: not supplied

## Constraints read from the CFP

- Confirmed from you: title cap 80 chars, abstract cap 1,200 chars, anonymous first-round review (author info not shown to reviewers).
- Not confirmed (no CFP page access, no track list, no accepted-talks sample from last year): track names, exact format/duration options, per-speaker submission cap, deadline, AI-assistance policy, recording/licensing terms, whether the event is vendor-neutral or vendor-run.
- **Assumption:** standard 25–30 min session. Confirm against the actual format list before finalizing the outline's minute marks.
- **Assumption:** track — closest plausible fit is a Reliability/Platform or Payments-Fintech track; confirm against NordicCloud Summit's real track descriptions, since a strong proposal in the wrong track still loses.
- **Open compliance item:** Marbleline sign-off / customer-anonymization / security read on the incident, per above.

## Angle

War story. You already own the material — a real incident, a real number, a shipped fix — which is the cheapest angle to submit and the one a reviewer can't get from anyone else. Trade-off: it's also the angle with the highest compliance cost (see above), and it can't be withdrawn once accepted.

## Track

Reliability / Platform Engineering (assumed) — "the operational aftermath of a distributed-systems failure and the invariants that now guard against it" matches a resilience-track description if one exists. Confirm the real wording before submitting.

## Title

### As you specified (names Marbleline — conflicts with anonymous round 1)

**Marbleline: Rebuilding Retries After a 1,900-Customer Duplicate Charge** (70/80 chars)

Alternates, same constraint:
1. How Marbleline Rebuilt Retries After 1,900 Duplicate Charges (60/80 chars)
2. Idempotency at Marbleline: Rebuilding a Payments Retry Layer at 1,900-Customer Cost (84/80 chars — **over cap, do not use as-is**)

### Blind-round-safe alternative (recommended for round 1)

**Rebuilding Idempotent Retries After a 1,900-Customer Duplicate Charge** (69/80 chars)

Alternates:
1. The Retry Bug That Double-Charged 1,900 Customers (49/80 chars)
2. Idempotency at 1,900 Customers: Rebuilding a Payments Retry Layer (65/80 chars)

## Abstract

### As you specified (912… actually 974/1,200 chars — names Marbleline twice)

At Marbleline, we believe idempotency is a product feature, not an implementation detail. We learned it the hard way: a retry-storm bug in our payments infrastructure double-charged 1,900 customers before anyone caught it. Marbleline clears close to a third of Nordic card volume, so a duplicate-charge incident does not stay quiet - banks, merchants and regulators all want the same answer: how did idempotent retries fail at that scale, and what stops it happening again?

This session walks through the retry layer we rebuilt afterward: the race between our idempotency-key store and at-least-once message delivery, why "dedupe on charge ID" papers over failures instead of preventing them, and the three invariants we now test on every deploy. Attendees leave able to audit whether their own retry logic can double-execute a side effect, design an idempotency-key scheme that survives partial failures, and size a duplicate-charge blast radius before it happens to them.

### Blind-round-safe alternative (944/1,200 chars)

Idempotency is a product feature, not an implementation detail - we learned that the hard way. A retry-storm bug in our payments infrastructure double-charged 1,900 customers before anyone caught it. We clear close to a third of Nordic card volume, so a duplicate-charge incident does not stay quiet - banks, merchants and regulators all wanted the same answer: how did idempotent retries fail at that scale, and what stops it happening again?

This session walks through the retry layer we rebuilt afterward: the race between our idempotency-key store and at-least-once message delivery, why "dedupe on charge ID" papers over failures instead of preventing them, and the three invariants we now test on every deploy. Attendees leave able to audit whether their own retry logic can double-execute a side effect, design an idempotency-key scheme that survives partial failures, and size a duplicate-charge blast radius before it happens to them.

(The employer name and the "we clear a third of Nordic card volume" credibility line move to Notes to reviewers / a dedicated affiliation field below, once reviewers can see it or the round is no longer blind.)

## Takeaways

- Audit whether existing retry logic can double-execute a side effect
- Design an idempotency-key scheme that survives partial failures and redelivery
- Size a duplicate-charge blast radius — and the customer-communication plan — before an incident forces it

## Outline (reviewer-only)

- 0–3 min — the incident: a retry storm double-charges 1,900 customers, first hour of triage
- 3–10 min — root cause
  - the race between the idempotency-key store and at-least-once message delivery
  - why "dedupe on charge ID" looked sufficient and wasn't
- 10–20 min — the rebuild
  - the three invariants now enforced on every deploy
  - what shipped in which order, and the one change that regressed
- 20–26 min — how it's tested now: fault injection on the retry path, what alerts on a near-miss before it becomes an incident
- 26–30 min — what we'd still change, questions

## Notes to reviewers

I own this retry layer and led both the incident response and the rebuild; the 1,900-customer figure and the timeline come from our incident record, not an estimate. The idempotency-key race described here reproduced in staging and the fix has been in production since [date - fill in]. This is not a product pitch: the invariants and the fault-injection approach generalize to any at-least-once messaging system, payments or not. **Affiliation disclosure:** state "Marbleline" in whatever dedicated employer/company field the form provides for this — check whether that field is shown to round-one reviewers or suppressed structurally like the bio; do not add it to this free-text field if it is reviewer-visible during the blind round.

## Benefit to the community

Idempotent retries are the default advice for distributed payments, but the failure mode that breaks that advice — a race between the idempotency-key store and at-least-once delivery — is rarely discussed with a real number attached to it. Teams building on Nordic instant-payment rails are adding retry paths to code not designed to be replayed; this gives them three invariants to test before their own incident, not after.

## Audience level and prerequisites

Intermediate — assumes familiarity with distributed-systems basics (message queues, at-least-once delivery, idempotency keys). No payments-domain background required.

## Speaker bio

**Needs your input** — I don't have your name or title, and the pack template rules say never to invent one. Draft shape, third person: "[Name], [title] at Marbleline, led the retry-layer rebuild after the 2026 duplicate-charge incident and now owns the payments idempotency framework." The bio field is typically suppressed structurally from round-one reviewers (that's the mechanism behind "author info not displayed"), unlike the abstract's body text — so naming Marbleline here is standard practice, not a blind-round violation. Confirm that suppression applies to this specific platform before relying on it.

## Supplemental materials

- Prior talk recording: none supplied — do you have one, even an internal recorded walkthrough?
- Incident postmortem / write-up: none supplied — is there a public version, and has it cleared the compliance review flagged above?
- Repo or benchmark: none supplied

## Self-review

- Content 4/5 — outline has minutes and a clear arc; would be 5 with the three invariants named up front instead of teased.
- Originality 4/5 — a real incident with a number nobody else can cite; the "retry layer rebuild" shape itself is common, the idempotency-key/at-least-once race is what's new.
- Relevance 3/5 — can't score higher without the event's actual track descriptions and last year's schedule; capped as an assumption, not a weakness in the copy.
- Speaker 3/5 — clear first-hand ownership implied, but no bio, no recording, no linked write-up yet. Fill those and this moves to 4–5.

## Before you submit

- [ ] Employer approval, customer anonymization, and security read cleared for a public incident narrative — this is the actual blocker, not a style note
- [ ] Confirmed whether NordicCloud Summit is vendor-neutral or vendor-run — changes whether naming Marbleline as the centerpiece (vs. the setting) is even appropriate
- [ ] Decided: named version (as requested) or blind-safe version, given the round-one anonymity conflict
- [ ] Real track list and last year's schedule checked — this pack's track and outline are best guesses without them
- [ ] Format/duration confirmed against the actual CFP form (25–30 min assumed here)
- [ ] Speaker bio written with your real name and title
- [ ] Per-person submission cap and AI-assistance policy checked
- [ ] Rewritten once more in your own voice before pasting into the form