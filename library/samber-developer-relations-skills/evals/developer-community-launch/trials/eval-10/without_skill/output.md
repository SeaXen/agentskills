## Recommendation: a private Slack workspace — not Discord, not GitHub Discussions, not a forum.

**Why Slack fits this specific setup:**

- 30 named partners is a closed feedback loop, not a community to grow. Optimize for signal speed to a known group, not discoverability.
- Design partners are engineering orgs. Slack is where B2B engineering teams already sit during work hours — feedback lands in a tool they already have open. That's the gap between "hours" and "days."
- Invite the 30 as (multi-channel) guests into one Duneshift-owned workspace, or use Slack Connect per org. Either way, your rota's pings hit partners' existing notification stream — Discord and GitHub Discussions both require opening a separate tool.
- Free-tier history decay (90 days) is a feature, not a limitation, here: your answers go stale in weeks anyway, so you don't want a durable archive of half-true API answers accumulating.
- Slack isn't indexed by Google. That matches "zero interest in search traffic, don't want to be indexed" directly — GitHub Discussions and any Discourse-style forum are built to be crawled and ranked, which works against that goal.
- The Berlin / São Paulo / Singapore rota maps cleanly onto Slack's status + @here model — pin a "who's on" message per shift, and a partner complaint gets a human inside hours no matter when it lands.

**Why the alternatives lose:**

- **GitHub Discussions** — async by design, optimized for durable, searchable Q&A: exactly what you don't want. Keep using GitHub *Issues* (already in place) for bug reports and breaking-change tracking; don't conflate that with the real-time feedback venue.
- **Discord** — real-time and free, but its gravity is OSS/individual-dev/gaming, not B2B engineering orgs already living in Slack. Making 30 partner companies adopt a second chat tool for one vendor burns the exact response-time budget you're optimizing for. Worth a gut-check: if this cohort skews solo OSS maintainers rather than companies, Discord wins instead — verify before deciding, don't assume.
- **Public forum (Discourse, etc.)** — built explicitly for SEO and permanence, the opposite of "don't want to be indexed" and "answers go stale in weeks."

**Structure to open with:**

- One Duneshift-owned Slack workspace, partners added as guests — avoids provisioning 30 separate Slack Connect channels.
- `#breaking-changes` — rota posts every release/breaking change here, pinned.
- `#feedback` — partners drop friction and bugs in real time; on-shift rota triages within the hour.
- `#general` — everything else.
- Pinned "who's on call" message, updated per rota handoff.
- Skip the open-community scaffolding (welcome bots, role ladders, recognition programs, engagement calendars) — that solves growth and retention problems you don't have with a fixed, already-committed roster.