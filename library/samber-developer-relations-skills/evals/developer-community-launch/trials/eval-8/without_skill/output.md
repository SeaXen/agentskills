## What to build: a private, invite-only Slack Connect group — not a community platform

Given the constraints, the right unit isn't "a community," it's a **curated practitioner channel with account-level privacy options**, run inside Slack Connect. Here's why, then the build.

### Why this shape, not the others

- **Public forum/Discourse/Discord: ruled out.** Your buyers (VPs of Data) won't post there, so it doesn't help renewals. Your regulated accounts (banks, insurers) have security policies that ban pasting code/architecture into anything public — a "private" Discord server still reads as a new, unapproved tool category to their IT/security review, and some will just block it outright. You'd be building something a meaningful slice of your own user base can't legally join.
- **Slack: not ruled out.** Most enterprise accounts already have Slack approved for external vendor collaboration (Slack Connect is a known, reviewed pattern at banks and insurers — unlike standing up new infrastructure). You're not asking their security team to approve a new category, just a new channel inside a tool they've likely already cleared.
- **One shared community for everyone: wrong shape.** Three of your largest accounts explicitly asked for a *dedicated, private* channel — not to be pooled with 27 other companies, some of which could be competitors to each other. Respect that ask; don't force them into a shared room to save yourself a channel.
- **30 separate 1:1 channels: wrong shape too.** Your actual demand signal is 8-9 *recurring* pipeline-tuning questions showing up across *different* accounts, plus two customers who already found value swapping notes directly. That's leverage — the same answer serves multiple accounts — and it disappears if everyone is siloed.

The answer is both, in one workspace: a shared channel for the leverage, dedicated channels for the whales who asked.

### The build

**One Slack workspace, three channel types:**

1. `#pipeline-practitioners` — shared, invite-only, Slack Connect, the 30 named invitees (data engineers only, no VPs). This is where the 8-9 recurring tuning questions get asked, answered once, and pinned. This is the actual value driver.
2. Three dedicated 1:1 Slack Connect channels for the three accounts that asked — private, just Northkeep + that one customer. Route account-specific or sensitive questions here instead of the shared channel.
3. `#solved` or a pinned canvas in the shared channel — Marcus converts resolved threads from the 8-9 recurring topics into short standing answers. This is what compounds over time and is what actually reduces repeat-question load, not the live discussion itself.

**Membership rule, stated up front in every channel:** no pasting logs, schemas, credentials, or customer data — discuss config patterns and abstractions only. Get this in writing from each invited account's security contact before they join, even for accounts without an explicit policy. Don't rely on the customer to self-police a boundary you never stated.

**Naming matters.** Call it a "customer practitioner channel" or "advisory group," not a "community" — the word "community" triggers heavier security/legal review at some accounts than a working Slack channel does.

### Marcus's 10 hours/week, spent as:

- **2h** — triage and route: keep the shared channel on-topic, redirect account-specific asks to the right dedicated channel.
- **2h** — seed one thread a week from the known 8-9 recurring topics (rotate through them; you'll cover the list every ~2 months).
- **2h** — tend the three dedicated channels: proactive tips, check-ins, nothing reactive-only.
- **2h** — convert resolved threads into `#solved` reference posts. This is the highest-leverage hour of the week — it's what turns 10 hrs/week into decreasing support load over time instead of flat load forever.
- **1h/month, amortized** — monthly optional office hours (async-first; don't force live attendance).
- **1h** — buffer, plus a short monthly note to CS/sales summarizing which accounts are active, for QBR ammunition (see below).

Don't add roles, badges, gamification, or onboarding bots. That's built for 500-person open communities, not a 30-person invite list — it's overhead with no payoff at this scale.

### Renewal linkage, without asking VPs to show up

VPs of Data won't post here, so the channel isn't a renewal lever by itself. Make it one indirectly: Marcus's monthly note feeds CS/AE prep for QBRs — "your engineers asked about X, here's the answer we gave, here's what two other accounts are doing differently." That turns grassroots engagement into an artifact the economic buyer sees and credits, without requiring their participation.

### Pilot, not launch

Start with the named 30 across: the three accounts that asked, plus the accounts already showing organic cross-pollination (the two that swapped notes on a call), plus whoever else is generating the recurring tuning questions. Run it 90 days. Decide whether to expand past 30 based on:

- distinct accounts posting/answering in the shared channel (not raw message count — one chatty account isn't the signal),
- drop in repeat support tickets on the 8-9 known topics,
- whether the three dedicated-channel accounts report it as valuable at their next QBR.

If those don't move, the fix is narrowing scope further, not adding a platform.