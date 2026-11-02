## Why the last sprint didn't stick

A sprint ships a stock of articles. It doesn't create a *flow* that replaces the articles as they rot or catches the tickets that never had one. Six months later you're not "back where you started" from bad luck — you removed the only mechanism, then nobody rebuilt one. Fix the flow, not the stock.

## Kill the assumption: the ticket→article button is a capture tool, not a program

What it does: lets an agent turn one resolved ticket's reply into a draft KB article.

What it doesn't do:

- No dedup — doesn't check if an article already covers this and just needs a fix.
- No gap detection — only fires when an agent manually clicks it. Recurring issues that agents just answer with a canned macro (with no article behind it) leave zero trace.
- No staleness detection — an article that's gone wrong after a product change gets no signal. It just sits there being confidently wrong.
- No queue — drafts pile up in "draft" status with no one assigned to finish them. Same fate as your last sprint's leftovers.
- No quality gate — one agent's phrasing becomes public-facing documentation, unedited, unless someone deliberately intervenes.

Treat it as a "capture" affordance you configure and layer process around — not a system.

## The model: two loops, different speeds, different owners

**Capture loop** — continuous, cheap, runs on every ticket, owned by the 12 agents.
**Publish + decay loop** — batched, weekly/monthly/quarterly, owned by you.

The whole point: capture must cost an agent nothing more than 5–10 seconds per ticket. Publishing and pruning is real work, but it's yours, scheduled, and never accumulates into a "sprint" again because it never stops.

## Who writes what

| Who | Does |
|---|---|
| **12 support agents** | Flag gaps as they close tickets (one tag, one click). Drop a raw, rough answer in an internal note — not prose, just the fix. That's it. Never asked to write finished articles. |
| **You (tech writer)** | Own triage, editing, structure, publishing, taxonomy, and the decay audit. You're the only person who touches what's public. |
| **Rotating "docs champion"** (1 of the 12, rotates weekly) | Sits in your 30-min weekly triage with you. Spreads ownership past "the writer's problem," gives you a second set of eyes on what's actually recurring on the floor. Costs the team one person for 30 min/week, rotated so no one owns it permanently. |
| **Engineering** | Only pulled in for technical sign-off on a short, named list of hard/ambiguous articles per quarter — never for routine writing or for tooling. You already know they won't give you build time, so don't design a system that needs any. |

Agents write raw material. You write documentation. Nobody except you publishes.

## Zendesk mechanics — all admin-doable, zero engineering

- **Tags**: `kb-candidate` (needs a new article), `kb-gap` (existing article is wrong/incomplete), `kb-outdated` (flagged stale). Three tags, that's the whole taxonomy for capture.
- **Macro**: one macro agents apply when closing a ticket that had no good article — applies the tag and inserts a templated internal-note snippet ("Issue: __ / What fixed it: __ / Ticket: #__"). This is the entire ask of an agent. If it's more than one click plus two blanks, it will not survive week three.
- **View**: "Docs queue" — filtered on the three tags, sorted oldest-first. This is what you and the docs champion open every week. Nothing lives in your head; it lives in the view.
- **Proxy signal for silent gaps**: a trigger/automation that tags tickets solved *without* a macro reference to an existing article, in categories where one should exist. Doesn't require engineering — Zendesk triggers are admin config. This catches the gaps agents don't bother flagging.
- **Staleness**: add a custom field on articles, `review_by date`. Build a saved view/report for anything overdue. If your plan has Guide Enterprise, turn on **Content Cues** — it auto-flags articles from ticket deflection and negative feedback and does a chunk of this for you; check your plan tier before building the manual version.
- **Feedback signal**: check the thumbs-down rate on articles monthly. Automatic decay flag — you don't have to notice it by accident.

## Cadence — this is the actual habit, not the tooling

- **Ambient (every ticket)**: agent tags + drops raw note. Not a task, a byproduct of closing the ticket.
- **Weekly, 30 min, you + rotating champion**: clear the docs queue. Decide: draft, fix existing, merge, or kill. Assign priority. Queue age is your health metric — if the oldest item creeps past 2–3 weeks, the loop is breaking.
- **Monthly, half day, you**: publishing sprint. Turn the week's triaged material into 5–10 published or updated articles. Report a one-line metrics update to the support lead. This is where the writing actually happens — batched, not sporadic, so it never again requires a "big sprint" to catch up.
- **Quarterly, half day, you + 1–2 senior agents**: decay audit. Pull overdue `review_by` articles, worst thumbs-down articles, and highest-traffic articles. Rewrite, merge, or archive. This is the step that was entirely missing last time — nothing before this ever revisited old content on a schedule.
- **Annually**: taxonomy/IA pass — category structure, article naming, dead-link sweep.

## Metrics that keep it alive politically, not just operationally

- % of closed tickets linked to an article (proxy for deflection).
- Docs-queue age (oldest unaddressed item).
- Article negative-feedback rate, trended.
- Count of overdue `review_by` articles.

Report these monthly to whoever owns the support budget. This is also your evidence next time you ask engineering for anything — "62 open gaps, deflection flat for two quarters" is a stronger ask than "we need docs time."

## Why this survives where the sprint didn't

- The unit of work for agents is 5 seconds, not "write documentation" — nobody has to feel like a writer to participate.
- Publishing is a standing calendar slot, not a project with an end date, so there's no "we're done" moment to walk away from.
- Staleness has an explicit trigger (`review_by`, thumbs-down rate) instead of relying on someone stumbling onto a wrong article.
- The rotating champion means the other 11 agents see a peer taking triage seriously every week — it stops looking like solely your problem.

## First 90 days

- **Days 1–7**: create the 3 tags, the macro, the queue view, the `review_by` field. Write a one-page SOP. Run a 15-minute training with all 12 agents — show them the macro, nothing else.
- **Weeks 2–4**: capture loop runs live. Run your first two weekly triage sessions, adjust the macro/tags based on where agents get confused (there will be friction — fix the macro, don't blame the agents).
- **Day 30**: first monthly publishing sprint. Baseline your four metrics.
- **Day 60**: second sprint. Start pulling `review_by` candidates for the first quarterly audit.
- **Day 90**: first decay audit. Report the 90-day metrics trend to leadership — this is your proof point that the habit, not another sprint, is what fixed it.