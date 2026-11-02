# Kelpwire developer call: scope card and question form

**Open decisions (needed before publishing)**
1. **Recording:** I drafted "not recorded, write-up published instead". The skill allows recording a drop-in call only with notice. Two incidents (a rate-table exposure and a production-logs request) point to no recording. Confirm, or switch to the recording notice in the skill's run-of-show reference.
2. **Destinations:** every `[link]` below is a placeholder. I need your support, sales, security, issue-tracker and feedback destinations. Kelpwire's security disclosure channel is the most important one.
3. **Cross-account rate-table finding:** it was raised live. Confirm it also reached your private security channel and that no recording or public notes of it exist.
4. **Production walkthrough with logs on screen:** this does not fit the call (see "What I did with your four asks"). Decide whether Kelpwire offers a private, contract-covered session through support or account management.

## Scope card (publish on the program page, pin in the intake thread)

> ## What to bring to the Kelpwire developer call
>
> Every other Thursday, [slot in the largest region's time zone + calendar link].
>
> **Bring:**
> - "How do I request rates for a multi-parcel shipment in one call?"
> - "Why does my rate quote differ between the sandbox and production?"
> - "What's the recommended retry and backoff strategy when the carriers API times out?"
> - "How should I cache rate responses without serving stale quotes?"
> - "Is webhook delivery for rate updates ordered, and how do I de-duplicate?"
>
> **Not here:**
> - Invoices, billing disputes, plan or contract questions → [support link]
> - Pricing, plan comparisons and Enterprise features → [sales contact]. We answer what the public docs already say about a paid feature. We say nothing about roadmap or price.
> - Anything that looks like a security problem, including seeing data that isn't yours → [security disclosure channel], privately. Never in the call, the chat or the thread.
> - A bug you can reproduce → [issue tracker]. Bring it and we'll help you write the report.
> - A feature you need → we log it live in [feedback record]. The product team decides.
> - Your own code, logs or environment → we can't see it, so no live debugging. Bring a minimal reproduction with secrets and customer data removed.
> - Your custom carrier connector or other contract-covered code → [support / account channel]. Public-API questions from the same team are welcome here.
>
> **Recording:** this call is [not recorded]. We publish a written summary within 2 business days at [where]. If we ever record, we'll say so first and tell you where it goes and how long it's kept.
>
> **Don't share** tokens, API keys, customer data or internal hostnames, in the form, in the chat or on screen.
>
> Our code of conduct applies: [link].

## Question form (six fields, nothing else)

Intro text above the form: *"Submit by [T-48h]. Don't paste logs, config, API keys or customer data. If an answer needs your code or logs, we'll point you to the right private channel."*

1. **Your question,** in one or two sentences.
2. **What you already tried,** and which docs page you read.
3. **Product, API version and endpoint** (for example, `rates/v2`).
4. **May we read your question out?** Yes / Anonymise it / No, answer me in the write-up only.
5. **Time zone** (optional). It feeds the slot review.
6. **Contact for follow-up** (optional). If you raise a feature request, may we keep your handle on it so you hear the decision? Yes / No.

## What I did with your four asks

| Your item | Decision | Why |
|---|---|---|
| Draft: "Ask us anything, no question too small" | Replaced | The skill's own example of a bad card. It invites invoice disputes, security reports and live debugging into a public call. |
| 20-minute invoice dispute | Redirected to support | Account and billing questions never belong on the call. The host stops at the card: "That needs your account, which we can't open here. [Support link], and I'll mention it to them." |
| Rate-table exposure | Security channel only | A suspected vulnerability must never be raised live, in a thread or on a recording. The fix doesn't change the rule. |
| Form asks for logs and config | **Declined** | The skill says never ask for logs, configs or screenshots in the form. They carry secrets and customer data into a tool nobody reviews, and your callers include contract customers. The form asks for a minimal reproduction instead, and the card states that scrubbing rule. Reproducible bugs go to the issue tracker. |
| Walk through a dev's production integration with logs on screen | Not on this call | It is live debugging of someone's own environment, and a screen share of production logs is the leak the recording review exists to catch. Offer them a minimal reproduction, or a private session via support or account management (open decision 4). |
| Sales wants the slot to talk up Enterprise | Declined as a pitch | The call is for answered questions. The card gives sales a named destination and allows answering what the public docs say about paid features. Roadmap and price stay with sales. The host removes an attendee who pitches after one warning. |
| Enterprise customer brings custom connector code | Redirected | Contract customers' own code goes to their support or account channel, under their contract's confidentiality terms. The card says their developers' public-API how-to questions stay welcome. |

## Host rules to keep with the card

- **Opening line:** "We can't see your systems, so no live debugging. No tokens or customer data on screen."
- **Off-scope questions:** name the destination from the card, log the question as "redirected", and mention it in the write-up. Don't answer inline.
- **Feature requests:** log them in the asker's words in [feedback record]. Copy the handle only if the asker consented, then delete the raw session log after the write-up.
- **Cadence:** fortnightly with a pinned async intake thread. Pin "no logs, keys or customer data" at its top, and give moderators a redaction path.

Everything past the pilot (at least 6 sessions, set in the charter) is provisional.