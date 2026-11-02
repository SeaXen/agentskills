## Recommendation: Don't build a dedicated Discord yet. Show up in the one that already exists.

The numbers argue against this, and it's worth saying plainly before handing over channel lists nobody will use.

### Why the case doesn't hold up

**"Our competitors run Discords with thousands of members."** Those competitors likely have thousands of *users* — free tier, OSS, self-serve signups — not thousands of paying customers. A community mirrors the top of your funnel, not the customer base. Kestrel Metrics has 40 paying customers. Even at 100% Discord opt-in, that's a server with 40 members and no critical mass. A visibly dead Discord (last message three weeks ago, "no one answered my question") reads worse to a prospect than no Discord at all — it signals an abandoned product.

**"We get support tickets."** Six a month, none repeating, all one-off integration questions. That's the opposite of the pattern a community solves. Community support works when the same 5 questions get asked by different people every week and members start answering each other. One-off questions just move from your inbox (where you control response time and quality) to a public channel (where they sit unanswered, or you answer them anyway — now in a worse-indexed, harder-to-search format than a help desk).

**"Nobody owns this."** This is the actual blocker, not a detail to fix later. "Marketing will keep an eye on it" is how every dead Discord starts. Community is a daily-tempo job — welcoming joiners, seeding discussion, answering fast so the second question ever asked doesn't sit unanswered for four days. Without a named owner with it in their actual job description, the recommendation below should be "no" regardless of the other numbers.

**The one real signal:** an ecosystem Discord for the monitoring space already has thousands of members, including at least three of your own customers. That's where the audience and the critical mass already live. Competing with it by building a parallel, empty space is the expensive path; showing up in it is the cheap one.

---

### What to do instead, starting now

| Action | Owner | Effort |
|---|---|---|
| Identify the ecosystem Discord's channel structure and rules (some ban vendor self-promo) | Marketing | 30 min |
| Get the 3 known customers to confirm they're active there (don't cold-DM them for this — ask at next support touch or QBR) | CS/Marketing | Low |
| Create one account, post a genuine intro (not a pitch), engage in #help-style channels for 2–4 weeks before mentioning Kestrel at all | Whoever owns support tickets | ~1 hr/week |
| Answer observability/integration questions there when Kestrel is genuinely relevant — same expertise already spent on the 6 monthly tickets, redirected to a bigger room | Support/eng | Folds into existing work |
| Track: does this produce leads, does it reduce ticket volume, do more customers surface there organically | Marketing | Monthly check-in |

This costs an hour a week, tests the actual hypothesis (does Discord-shaped engagement help us), and has a natural off-ramp if it doesn't pan out — no server to quietly kill later.

---

### When a dedicated Discord would actually make sense

Revisit only if two or more of these become true:

- Customer count is 5–10x higher (200+), so a server has enough members to feel alive
- Support tickets start repeating — same question from multiple customers, which a community can absorb
- Someone requests ownership, not gets assigned it as a side task
- The ecosystem Discord engagement (above) is working and customers are asking "do you have your own space?"

---

### If leadership wants to launch anyway

If the CTO's conviction wins out regardless, here's the minimal version — small on purpose, since an oversized channel list on a 40-person server is its own failure mode:

**Channels (8, not the usual 15+):**

| Channel | Purpose |
|---|---|
| #welcome | Rules, links, one-line pitch |
| #announcements | Product updates, admin-only posting |
| #general | Main discussion |
| #help | Integration questions — replaces/supplements the support inbox |
| #feature-requests | Roadmap input |
| #show-and-tell | Customers share dashboards/setups |
| #introductions | New member intros |
| #off-topic | Optional, add only if #general gets crowded |

Skip #jobs, #backend/#frontend/#devops splits, and multiple support sub-channels — 40 people can't sustain that many rooms; it just scatters the few messages you do get.

**Launch plan (4 weeks):**

| Week | Milestone |
|---|---|
| 1 | Name an actual owner (job description line item, not a Slack aside). Stand up server, write CoC, seed #show-and-tell and #help with 2–3 real examples from support history so it isn't empty on day one |
| 2 | Soft-launch to the 40 customers via email/in-app, framed as "come talk to the team directly," not "join our community." Personally invite the 3 users already active in the ecosystem Discord |
| 3 | Owner runs daily 10-minute check-ins: answer anything open, react to posts, no post left unanswered >24h |
| 4 | Review: members joined, messages sent, tickets deflected, owner's actual time spent. Decide keep/kill against the health thresholds below — don't let it drift into a slow, silent shutdown |

**Non-negotiable before day one:** a named owner with community time budgeted into their week, and a 30-day kill criterion written down in advance (e.g., <15 active members or <5 owner-outside messages/week → shut it down, don't let it rot). Set the exit condition before launch, while it's still an abstract number — after launch, sunk-cost thinking makes that call much harder.