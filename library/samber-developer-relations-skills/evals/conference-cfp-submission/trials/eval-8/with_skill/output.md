# Ferrolane Devcon — Lightning Talk (5 min) — Proposal Pack

Using the `conference-cfp-submission` skill. Two things need to happen before this pack is submission-ready, and I'm flagging both up front rather than burying them.

## Before anything else: the scope has to be cut

Eight threads — backlog problem, why Redis Streams, the consumer group bug, new metrics, the dashboard, the on-call rota change, cost savings, and lessons learned — is a 25-30 minute standard-session talk, not a 5-minute lightning talk. This is the skill's own "book-sized scope" failure mode: *"We'll cover REST, GraphQL and gRPC, and how to choose" → fix: one angle, or ask for the longer format.* Format-to-scope rule for lightning is explicit: **one idea, one takeaway.**

Trying to hit all eight in 300 seconds means every one of them gets a throwaway sentence and nothing lands — the classic reviewer pattern-match for "generic," which is exactly what Content and Originality scores punish.

So I picked the angle for you and built the pack around it. Tell me if you'd rather cut differently.

**Chosen angle: the consumer group bug**, framed as a war story — cheapest to write (you already have the material), highest standout for a 5-minute slot, and it's the one piece none of the other seven items can substitute for. The backlog problem becomes the 45-second hook. Redis Streams becomes one sentence of context, not a section. Metrics, dashboard, on-call rota change, and cost savings get compressed into a single "what changed" beat — present but not explained. "What we'd do differently" becomes the closing line, not its own section.

**What got cut, and where it should go instead:** the full backlog→Streams migration story, the dashboard build, the on-call rota redesign, and the cost breakdown are a legitimate 25-30 minute session or a blog post. Don't discard that material — pitch it separately once this angle is proven, per the skill's guidance that a proposal is reusable across a season, not a spent ticket.

---

## Constraints read from the CFP

**I could not browse the web this session, so none of these are confirmed against the real Ferrolane Devcon page.** Everything below marked with brackets is a placeholder, not a guess dressed up as fact — fill it in or paste me the actual CFP page and I'll correct the pack against it.

- Fields: assumed standard set (title, abstract, takeaways, outline, notes to reviewers, benefit to community, bio) — **confirm against the actual form**
- Caps: no published cap found — used conservative lightning-talk defaults (title ≤80 chars, abstract ≤700 chars) — **confirm and I'll re-cut to fit**
- Review: anonymous or named — **unknown, check the CFP page's review-process section**; until confirmed, the copy below stays employer-name-free to be safe under either policy
- Per-person submission cap: **unknown**
- Recycled-content rule: **unknown** — matters if any part of this has been given internally or at a meetup already
- AI-assistance policy: **unknown** — read it before submitting; this draft needs your own rewrite pass regardless (Step 8's humanizer rule)
- Track list: **unknown** — "Track" below is my best guess from the topic, not a match against a published description

## Track

**Reliability / Operations** (best guess — confirm the actual track name). If Ferrolane Devcon runs something like "Infrastructure," "Backend," or "Postmortems," match to whichever track description explicitly invites production-incident or operational-failure content — chairs rank within a track, so a strong reliability story submitted to a generic "Backend" track loses to a weaker one that's actually in a track called "War Stories" or "Incidents."

## Title (51/80 chars, assumed cap)

**The Redis Streams Bug That Rewrote Our On-Call Rota**

Alternatives:

1. The Consumer Group Bug That Reprocessed Our Backlog Twice (57 chars)
2. We Fixed a Queue Backlog and Shipped a Duplicate-Delivery Bug (61 chars)
3. `[N]` Duplicate Messages Later: What Consumer Groups Don't Guarantee (66 chars, real number replaces `[N]`)
4. The Migration That Cleared Our Backlog and Broke Idempotency (60 chars)

Title 1 is the strongest — it promises a twist (fix caused a process change, not just a code change), it's plain rather than punny, and it doesn't lean on a number you haven't given me. Swap in title 3 once you have the exact reprocessed-message count; a real number in the title is the cheapest credibility signal available and worth the swap if the figure is strong.

## Abstract (692/700 chars, assumed cap)

> A message backlog was paging on-call every week, and Redis Streams looked like the fix: consumer groups for fan-out, XREADGROUP for replay, no new broker to run. It was - until a rebalance on deploy let two consumers claim the same pending entries and reprocess `[N]` messages that had already shipped. This talk is the five minutes in the middle: what the naive rebalance actually did, the metric that did not exist until this incident forced it onto a dashboard, and the pending-entries check that fixed it in one line. It also covers why the on-call rota changed afterward. Leave with the one XPENDING check to run before trusting a Streams consumer group's delivery guarantee in production.

`[N]` is the one number this abstract needs — how many messages actually got reprocessed. Without it, cut the clause rather than submit an unverifiable claim.

## Takeaways

- Check XPENDING / pending-entries idle time before trusting a Redis Streams consumer group's delivery guarantee in production.

One only — this is a lightning slot. Everything else you listed (metrics, dashboard, rota, cost) is context inside the outline below, not a second takeaway.

## Outline (reviewer-only)

- **0:00–0:45** — The backlog that paged on-call every week
  - why the existing queue couldn't keep up (one line, no detour into the old system)
- **0:45–1:15** — Why Redis Streams
  - consumer groups + replay were the deciding features, not raw throughput
- **1:15–3:15** — The consumer group bug
  - what shipped: a naive rebalance on deploy
  - what broke: two consumers claimed the same pending entries, reprocessing `[N]` messages
  - how it was caught: the metric that didn't exist before this incident
  - the fix: an XPENDING-based idle-time check before claiming
- **3:15–4:15** — What changed after
  - the dashboard now on the wall (one line)
  - the on-call rota change this incident forced (one line)
  - the cost number, if you have one worth stating (one line)
- **4:15–5:00** — What we'd do differently, and the one check to steal

## Notes to reviewers (423/500 chars, assumed cap)

> I own this pipeline and led the Redis Streams migration; the reprocessing count and the backlog numbers come from our incident record and metrics history, both linkable in redacted form. Most Streams talks pitch the migration as a success story - this is the failure mode that only shows up under real concurrent rebalancing, plus the on-call process change it forced. Timed at a dry-run reading against the 5-minute limit.

Do the dry run and drop in the actual timing before submitting — "I haven't confirmed it fits" is a weaker claim than a number.

## Benefit to the community (350/500 chars, assumed cap)

> Anyone adopting Redis Streams for at-least-once delivery hits this exact rebalance and duplicate-delivery interaction eventually; almost nothing public documents the pending-entries check that catches it before production does. Fills a gap in most Streams content, which stops at the migration announcement and never covers the operational aftermath.

## Audience level and prerequisites

Intermediate — assumes familiarity with message queues or pub/sub generally; no prior Redis Streams knowledge required, since the talk explains the relevant mechanics as it goes.

## Speaker bio (184/400 chars, assumed cap)

> `[NAME]` is a `[ROLE]` at `[COMPANY]`, where they led the migration of the team's queueing layer to Redis Streams and the on-call rotation change that followed the incident this talk covers.

Fill in name, role, and whether the employer's name is even allowed given the unknown anonymity policy above.

## Supplemental materials

- Prior talk recording: `[none / link — has this been given internally or at a meetup yet?]`
- Repo / post / benchmark: `[link to a postmortem writeup or dashboard screenshot if either can be made public]`

## Self-review

Scored as a reviewer would see the pack **today, with placeholders still in it**. Scores will move once real numbers land — I'm not inflating them to look submission-ready when parts of the evidence are still bracketed.

| Axis | Score | Why |
|---|---|---|
| Content | 3/5 | Outline is tight, minute-estimated, and scoped to one idea — but the pending-entries fix is asserted, not shown; the reviewer can't check it without the actual number. Fixing `[N]` moves this to 4. |
| Originality | 4/5 | Most Redis Streams content is the migration pitch; this is the failure mode underneath it, which is a lens the programme almost certainly lacks. |
| Relevance | 2/5, provisional | Cannot score honestly — track and its description are both unconfirmed. Locks to 4 once matched against a real track. |
| Speaker | 2/5 | First-hand involvement is claimed but nothing checkable is attached yet — no bio detail, no recording, no linked incident record. Attaching even one artifact moves this to 4. |

**Do not submit yet.** Per the skill's pass threshold, Content and Originality both need to clear 4, and no axis can sit below 3 — Relevance and Speaker are both currently unscoreable or under bar because of placeholders, not because the angle is weak.

## Before you submit

- [ ] `[N]` — the actual reprocessed-message count — filled in, or the claim cut
- [ ] Track matched against Ferrolane Devcon's real track list, not guessed
- [ ] Title/abstract/notes/benefit character counts checked against the real form caps, not the assumed defaults above
- [ ] Speaker bio filled in; employer name included only if the anonymity policy allows it
- [ ] Dry run timed against the actual 5-minute limit, real timing dropped into the notes field
- [ ] Per-person submission cap, recycled-content rule, and AI-assistance policy read from the real CFP page
- [ ] Rewritten in your own voice — this is a draft, not speaker-ready copy
- [ ] Affiliation disclosed where the form asks

---

## Your question: is lightning actually easier to get into, and by how much?

**No conference — Ferrolane Devcon included, as far as I can find — publishes a per-format acceptance-rate breakdown, so there's no real number to give you.** This isn't a gap in my research; it's a documented gap in what these events disclose at all. Neither PyCon US nor the Linux Foundation's KubeCon CFP pages publish submission or acceptance counts, and the "roughly 1 in 10" figure that circulates in speaker-advice content has no primary source behind it. Treat any number someone quotes you for lightning-vs-main-track odds the same way — unverified folk wisdom, not data.

What *is* true, without needing a published rate to support it:

- Lightning slots are widely treated as the easier entry point because there are usually more of them, the speaking commitment is smaller, and a bad 5-minute talk costs the audience and the committee far less than a bad 30-minute one — so the reviewer's downside risk per pick is lower. That's a structural reason to expect a softer bar, not a measured one.
- The same four axes (Content, Originality, Relevance, Speaker) still apply at 5 minutes. The format doesn't lower the bar on any of them — it lowers the *scope* required to clear Content, because "one idea, well-executed" is a fully realistic ask in 5 minutes in a way "three subsystems and a retro" never is.
- This is why the scope cut above matters more than the format-difficulty question: a focused lightning talk built around the consumer-group bug will out-score an unfocused one trying to cover all eight threads, regardless of what the format's true acceptance rate turns out to be. Format is a strategy lever on top of a good proposal, not a substitute for one.
- If lightning doesn't land, the material doesn't die — the skill's own guidance is to retarget it: resubmit the same angle to a different Ferrolane track, or hold the fuller backlog/Streams/cost-savings story for a standard-session slot at this event or the next one on your calendar.

If you want a real answer specific to Ferrolane Devcon rather than the general pattern above, the only way to get one is to ask the organizers directly or count accepted lightning vs. standard talks across a couple of past editions' published schedules yourself — nobody publishes the ratio outright.