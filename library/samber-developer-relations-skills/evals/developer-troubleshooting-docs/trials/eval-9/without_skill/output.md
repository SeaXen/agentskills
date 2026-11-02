## Before anything else: the leaked credential is a stop-ship, not a line item

One of the 9 entries has a live customer bearer token and org ID in a curl example. This isn't a style nit to clean up during copyedit — it's a credential exposure. Treat it exactly like a security incident, not a documentation task:

- **Redact now**: replace the token with `Authorization: Bearer <TOKEN>` and the org ID with `<ORG_ID>` (or a fake example org) before this entry goes anywhere near a merge, draft PR, or shared doc.
- **Check exposure radius**: if this draft has already been committed, pushed, or pasted into any tool (Slack, a doc, a PR description, a ticket comment visible outside your support tooling), the token should be treated as compromised — flag it to security/the customer's account owner so it can be rotated. Don't rely on "we'll redact it before merge" if it already left the support ticket.
- This blocks that one entry independently of the reproducibility question below. A fully-reproduced, well-written fix is still not mergeable with a real customer's credentials embedded in it.

## Where your manager's reasoning breaks

"A fix that worked for a real customer is verified by definition" collapses two different claims:

- **"The customer's symptom went away"** — true, and worth recording.
- **"This documented root cause and fix generalizes to other customers on our supported versions"** — not established by one resolved ticket, and is what a KB/runbook entry actually asserts to its next reader.

A support resolution confirms the fix worked *in that specific customer's environment, at that moment*. It doesn't confirm the root cause is what the ticket says (correlation vs. causation — the issue could've cleared for an unrelated reason), and it doesn't confirm the fix applies across every version you claim to support. Publishing all 9 with equal confidence trades a one-day schedule slip for a KB that sends the next customer down a wrong path — which costs support more time than it saves now.

The fix isn't "block everything until fully reproduced everywhere." It's **label confidence honestly** so the reader knows what they're getting. That costs almost no time and still ships Monday.

## Disposition for all 9, ready for Monday

**The 6 reproduced on 3.4** — ship these, with one correction: "reproduced on 3.4" is not the same as "confirmed on 3.0–3.4." Before labeling any of them as applying to the full 3.0–3.4 range, check whether the underlying code path is actually shared across those versions. If it is, say so explicitly ("root cause present in 3.0–3.4, verified against 3.4"). If you haven't checked, scope the entry to what you actually know: "Confirmed on 3.4. Applicability to 3.0–3.3 unverified." Don't let the support ticket's "the customer was on 3.4" silently become a claim about the full version matrix — that's a second, smaller version of the same overclaiming problem as the manager's, and it's an easy one to fix before Monday.

**The 3 unreproduced — don't treat as one bucket, they're different risk levels:**

- **Air-gapped install**: legitimate, just expensive to test. Publish, but caveat: "Reported to resolve this issue in air-gapped installs; not independently reproduced in-house." This is honest and still useful — readers in that exact situation self-select in.
- **F5-specific load balancer**: same treatment. Name the trigger condition explicitly ("observed behind F5 load balancers with [config detail from the ticket]") so readers can tell if it applies to them, and caveat it as unverified in-house. Specificity here does the verification work you can't.
- **Intermittent, seen once**: this is the weakest evidence of the 9 — a single occurrence of an intermittent issue doesn't distinguish "we fixed it" from "it stopped happening on its own." Recommend holding this one out of Monday's batch, or if it must ship, caveat hardest: "Reported once; root cause and fix unconfirmed — if this doesn't resolve your issue, contact support" and flag it internally for re-confirmation if it recurs. This is the one entry where shipping it as authoritative is most likely to burn a future customer's time.

## What to send your manager

"All 6 reproduced-on-3.4 entries and the 3 unreproduced ones can ship Monday — I'm not blocking the timeline. Two changes first: the credential in entry [X] gets redacted (that one's non-negotiable regardless of deadline), and the 3 unreproduced entries get a one-line 'reported, not independently verified' caveat instead of being presented the same as the confirmed ones. Same ship date, and the KB doesn't overpromise on the entries we haven't actually confirmed."