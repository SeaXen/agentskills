**Do neither.** Send one templated reply: no bounty, here is how to report. Triage the claim on its merits anyway.

## Why not Dario's $100

- You pay for silence about a claim with no version, component or PoC. You can't tell whether it's real.
- You set a precedent. The next email asks $500, then $1000.
- Payment doesn't buy a fix. If the flaw is real, it stays unfixed and the sender knows it.
- The skill rule is "never negotiate money, never pay for an extension."

## Why not the extortion threat

- The skill rule is "never threaten the reporter." A threat becomes the public story: "maintainers threatened researcher."
- "Pay or I publish" is a known beg-bounty pattern. It is not a clear crime, and the answer depends on jurisdiction. Whether it legally counts as extortion is a question for a lawyer, not for us.
- A hosting provider has no leverage here. The sender's blog is their own, and the email names no host.
- If the sender escalates to real threats or harassment, report to the blog or code host and to whoever handles conduct. That is a later step.

## Do now (about 30 minutes)

1. **Keep the original email.** Don't forward it to any list or chat. Send it only to the other responders. Re-check the dates: the 48h clock started at the send time, so write the deadline with its time zone in the private note.
2. **Send the internal note** (template 0) to Dario and one other maintainer, by direct email. Say: don't discuss in public issues or chat, and don't reply on your own.
3. **Send the reply below once.** Don't send a second one. Send it only to the sender, never to the list.
4. **Spend 1 to 2 hours on a code read.** Check the auth and session code paths in the latest release, and look at recent commits for anything touching them. "Account takeover" is odd for a cache library, so also check whether any component handles credentials or tokens. Treat the claim as pending until you reproduce it.
5. **Open no public issue, PR or commit mentioning this.** Don't write about it in memory files or notes either.
6. **Prepare a fast-track plan, but don't publish.** If the sender goes public, fix, release and advisory happen the same day. Pre-draft the publication notice (template 8) with `<<late: ...>>` fields.

## Reply to send

```
Subject: Re: Security report for lattice-cache

Thank you for contacting us. lattice-cache does not run a bug bounty and does
not pay for reports; our process is described in <SECURITY.md link | private
reporting link>. We will assess the issue you describe on its merits and credit
you in any resulting advisory.

To proceed, please submit through <channel>: the exact affected version, the
affected component, and a minimal proof of concept that runs against a released
version on Maven Central. We cannot assess a report without them.

We will confirm receipt within <X> business days of your submission and give
you a triage decision by <date, time zone>. Please keep the details private
until a fix is released.
```

Fill each `<...>` before sending. Pick a real channel: GitHub private vulnerability reporting if the repo is public, or a two-person alias. If neither exists, enable one today. That is the main fix this incident shows you need.

## Decide after the code read

| Outcome | Action |
|---|---|
| Real flaw found | Fast fix, backports, release, then advisory. Credit the sender only if they provide details. Request a CVE through the code host once accepted. |
| Nothing found, no reply from sender | Close it. Keep private notes of the reasoning, with date and what you checked. |
| Sender publishes without details | No public reply. If they add details, switch to the fast track. |
| Sender replies with a real PoC | Reproduce only in a disposable VM with networking off. Read it before running it. |

## Open questions

- When did the email arrive? That sets the 48h deadline.
- Who besides you and Dario can publish releases and advisories?
- Are there supported release lines, and how do you cut a release?
- Is the project company-run or monetised? If so, check the EU CRA role with a lawyer.

**Next:** reply to Dario with "no payment, no threat, one templated reply." Then send the internal note to the second maintainer.