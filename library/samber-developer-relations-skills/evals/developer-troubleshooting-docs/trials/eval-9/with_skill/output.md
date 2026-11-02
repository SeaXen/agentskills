## Using developer-troubleshooting-docs on the Pilcrow batch

Applying Step 7 (verify before publishing) and Step 8 (findability/credential rules) from `developer-troubleshooting-docs` to your 9 drafts. Four things need to happen before Monday, in this order.

### ❌ 1. Stop-ship: the credential leak isn't a Monday problem, it's a now problem

The entry with the curl example carrying the customer's bearer token and org ID does not ship with your manager's deadline as an excuse — this is independent of the verification debate below.

- Redact both from the drafted page: `Authorization: Bearer <TOKEN>`, `orgId=<ORG_ID>`. Copy the *shape* of the call from the ticket, never the literal values (entry-templates.md, "Quoting the error text": *"Redact secrets in every example, and say so."*).
- Treat the source, not just the draft: if that ticket text with the live token is sitting in a shared doc, wiki page, or PR description anywhere outside the ticketing system's own ACL, flag it to whoever owns customer credential hygiene so the token can be rotated. A live bearer token that's been copy-pasted into a drafting artifact is a credential-exposure question, not a docs-style question — don't let it ride along as a formatting fix.
- This also matches your own CLAUDE.md security rule: never disclose customer-identifiable detail. An org ID is exactly that.

### ⚠️ 2. Your manager's verification bar is wrong — say so, with the skill's actual bar

"A fix that worked for a real customer is verified by definition" isn't what any of the four frameworks this skill runs on call verification. A resolved ticket confirms the fix worked *once, for that customer's specific environment, as executed live by whoever was on the call.* It confirms nothing about:

- whether the written-down steps reproduce the same result cold, from a clean starting state (verification protocol point 1-2: *"Publish nothing that has not been run... from the state the reader is in, not from your already-configured machine"*)
- whether it holds across the version range you actually support (point 4: *"Check applicability at both edges: the oldest supported version and the current one"*) — you support 3.0-3.4, you tested 3.4
- whether someone other than the ticket's resolver can follow it (point 5)

The framing to use with her: **"verified" and "resolved a real customer's ticket" are different claims, and this skill's own citation for why is Write the Docs' rule — "consider incorrect documentation to be worse than missing documentation."** A page that says "do X" with unearned confidence, when X only worked once under conditions we haven't pinned down, actively costs more support time than no page at all when a second customer runs it and it doesn't work.

This doesn't mean delay to Monday — it means **label honestly**, which the skill explicitly allows as a shipping path (see the disposition table below). Nothing here requires blocking the release.

### Disposition for all 9

| # | Status you gave me | What the skill says to do | Ships Monday? |
|---|---|---|---|
| 1-6 | Reproduced on 3.4 | Reproducible ✅, but "Applies to: 3.0-3.4" is an unverified claim if only 3.4 was run. Either spin up a 3.0 instance today and confirm behavior/error text is identical, or narrow the page to **"Applies to: 3.4, confirmed. Not yet verified on 3.0-3.3."** Do not silently write the full supported range because it's convenient. | Yes, either fully verified or honestly scoped |
| 7 | Needs air-gapped install | Environment-specific, matches the protocol's named exception exactly. Publish with **"Reported under these conditions, not reproduced here"** stated in the Cause section, not buried in a footnote. If Pilcrow has any way to fake an air-gapped network (isolated VPC, no egress rules) before Monday, spend the hour — this one is reproducible in principle, unlike the next two. | Yes, with the explicit caveat, or fully verified if you get the hour |
| 8 | Only behind a specific customer F5 config | Same exception, plus it's third-party-dependent, so full reproduction may never be possible on your side. Ship as a **known-issues** shape ("Applies to: deployments behind F5 load balancers configured as `<X>`"), not an error-reference page implying a general fix — you're documenting one customer's confirmed workaround, not a validated fix for the failure class. | Yes, as known-issues with the caveat |
| 9 | Intermittent, seen once | Two separate checks, not one: (a) verification — this gets the "not reproduced here" note like #7/#8; (b) **does it even clear the queue bar** — Step 2's script default is `--min-count 3`, and one ticket normally doesn't rank. It only survives if you're promoting it under the rare-and-expensive/contract-bound-production rule. Confirm with your manager explicitly that's why it's in the batch, rather than letting a one-off ride in at the same confidence as the six reproduced ones. | Yes, but as a known-issues entry with the caveat, and only if you and your manager agree it's promoted, not defaulted-in |

### One more gate before you call any of these done

Verification protocol point 5, unmet for all 9 so far: *"Have someone who did not write the entry follow it cold."* You wrote all 9 from the ticket notes yourself. Get one teammate to run the fix steps on #1-6 verbatim before Monday — their first hesitation is the step with an unstated assumption baked in from your already-configured machine.

### What to actually tell your manager

> The 6 reproduced entries ship as-is once we confirm 3.0 behavior or scope the "Applies to" line to 3.4. The 3 you flagged ship too — as known-issues entries with an explicit "reported, not reproduced" line, which is the standard way this format handles a customer-confirmed-but-unreproduced fix. That's not a downgrade, it's what keeps a page from teaching someone to run a fix that doesn't apply to their setup. Separately, the F5-behind-load-balancer curl example has a live customer token and org ID in it — pulling that now regardless of the Monday date.