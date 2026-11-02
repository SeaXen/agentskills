# Loamside — DevRel Hiring Kit + Quarterly Budget Narrative

Followed `developer-relations-kickoff`. Routing, then the two deliverables in full.

## Routing note

- **Cold start** — no `devrel-context.md` in this workspace, nothing to resummarize.
- You asked for the finished deliverable, not a Q&A, so I skipped the interview and used stated defaults instead (below). Override any of them and I'll adjust the artifacts they touch.
- **Ask 1 → `devrel-hiring`** — exact scope match (job posting, scorecard, interview loop for a DevRel role).
- **Ask 2 → no single skill.** The collection names this gap verbatim: *"the exec-facing DevRel report narrative and budget defense."* Chain used instead: `devrel-metrics` (what you're allowed to claim) → `devrel-budget-allocation` (the line-item table and its own "five-sentence narrative") → the actual deck arc and talk track, which nothing in the collection owns — built below from general exec-narrative craft, flagged as such.
- **Not now:** `devrel-team-structure` (org design — not in question here), `devrel-strategy` (assumed already set, since a hiring panel and a recurring budget cycle both already exist).
- I'm not writing `devrel-context.md` to disk — this session isn't running inside Loamside's own repo. The assumptions block below is that artifact's content; paste it into your own project if you want warm starts next time.

**Assumptions (stated once, used in both deliverables — say which ones are wrong):**

| # | Question | Assumed answer |
|---|---|---|
| 1 | Company type | Growth-stage (B–D) |
| 2 | Role target | Developer Advocate, senior, outreach-primary with real product-input weight |
| 3 | Funded driver | Developer adoption (primary) + product input (secondary) |
| 4 | GTM motion | Product-led growth, sales-assist on larger accounts |
| 5 | Coding depth | Medium — ships sample code, reads API diffs; doesn't own core product |
| 6 | Hire type | Repeatable — a panel and prior hires already exist |
| 7 | Comp | Publishing a range (placeholder below — confirm your jurisdiction's pay-transparency rule) |
| 8 | Deadline | This quarter |
| 9 | Budget cycle | Quarterly exec review; last quarter's cut was narrative failure, not a performance failure |

---

# Part 1 — Hiring the Senior Developer Advocate

## Scorecard

**Mission:** Cut time-to-first-successful-integration for self-serve developers and turn developer trust into qualified pipeline in accounts with an active developer footprint — funded as a developer-adoption and product-input role.

**Outcomes** (ranked, quantified — this is what the posting, the loop, and the ramp plan all point at):

1. Ship 12 technical artifacts in year one (talks, posts, or reference integrations), each tied to a named downstream action — a signup, a PR, or a qualified conversation. Replaces "produces content" as a line item.
2. Cut the top three recurring "how do I…" support/community threads by 25% within two quarters via a shipped docs or sample-code fix, evidenced by a published friction log.
3. Source or influence 15 qualified sales conversations in accounts with an active developer footprint within two quarters — tagged as influenced, never claimed as sourced revenue.
4. Deliver a quarterly developer-feedback synthesis that changes at least one named, dated product-roadmap decision.
5. Get accepted to speak at 4 conferences where Loamside's actual buyer or user persona is in the room, within 12 months.

**Competencies** (weighted, feed the interview loop 1:1):

| Competency | Weight | Why it's weighted this way |
|---|---|---|
| Technical writing & sample-code craftsmanship | 25% | Outreach+product blend — the artifact has to survive a skeptical developer reader |
| Developer-empathy interviewing | 20% | This is the "cut support threads" outcome in practice |
| Public speaking & audience read | 20% | 4 CFP acceptances is a scored outcome, not a nice-to-have |
| API literacy / can file a credible product-feedback ticket | 15% | Feeds outcome 4 — feedback that actually lands |
| Cross-functional influence without authority | 10% | No formal authority over product or sales; has to earn the roadmap change |
| Metrics literacy — states what a number can honestly claim | 10% | Ties directly to Part 2 — this hire should make your next budget deck easier, not harder |

## Job posting

> **Senior Developer Advocate — Loamside**
> *Developer adoption & product-input pillar*
>
> Loamside funds this role to cut the time between a developer's first `npm install`/`pip install` and their first working integration, and to make sure what developers tell us actually reaches the roadmap. This is not a "wear every hat" founding role — you're the second dedicated DevRel hire, joining an existing panel and existing programs.
>
> **You will be measured on, in this order:**
> 1. 12 shipped technical artifacts in year one, each tied to a signup, a PR, or a qualified conversation.
> 2. A 25% cut in our top three recurring support threads within two quarters, via a shipped fix you ship yourself.
> 3. 15 qualified conversations sourced or influenced in developer-active accounts within two quarters (we track this as *influenced*, never as sourced revenue — that distinction matters to us and it should to you).
> 4. One named, dated product-roadmap decision changed by a feedback synthesis you deliver quarterly.
> 5. 4 conference acceptances in front of our actual buyer/user persona within 12 months.
>
> **What we need you to already be good at:**
> - Writing sample code and docs a stranger can run without asking you a follow-up question.
> - Turning a frustrated developer's complaint into a fix, not just a sympathetic reply.
> - Standing in front of a room (or a camera) and handling a question you didn't prep for.
> - Reading an API diff and writing a product ticket an engineer would actually act on.
>
> **What we don't need:** a full engineering career across multiple stacks, a personal following of any particular size, or event-logistics experience. If a past posting asked you for all of that at this level, that posting was broken, not you.
>
> **Resourcing, stated plainly:** you report to [Head of DevRel], have a existing docs/content budget line, and inherit a live community channel — you are not building any of these three from zero.
>
> **Compensation:** [$X–$Y base] + equity + standard benefits. *(Placeholder — confirm against your hiring jurisdiction's pay-transparency requirement before publishing; never ship "competitive" with no figure.)*
>
> **Process:** portfolio review → a talk you choose to give us → a working session with a product stakeholder → a conversation about how you think about the job itself. No unpaid spec work — if your public portfolio already answers a round, we skip it.

*Self-audit run before publishing:* no off-core skills list, every line traces to a scored outcome, "senior" is backed by a real level of resourcing (not a first-hire pit-trap), comp gate flagged not silently skipped. Passes.

## Interview loop — what each stage is actually testing

Four scored stages, portfolio review first (so a strong public track record can shorten the rest), no live work sample unless the portfolio comes back thin.

| Stage | Format | Duration | Panel | What it's *actually* testing | Strong signal | Red flag |
|---|---|---|---|---|---|---|
| 0 — Screen | Recruiter call | 20 min | Recruiter | Logistics + comp alignment only — **not scored**, keep it out of the scorecard | — | — |
| 1 — Portfolio | Async scoring, six-signal rubric | 30 min panel time | Hiring manager + 1 IC | Whether the shipped public work (writing, speaking, code, community role, teaching, a friction log) already answers most of the scorecard — weighted here on signals 1+2 (writing, speaking) since this is outreach-primary | A published post with a stated result; two+ talks with links; a friction log that named a real fix | Follower count with no substance; content only about the candidate, never the developers they served; can't name a specific developer they helped |
| 2 — Presentation round | Candidate presents a technical topic of their choosing, 15 min + Q&A | 45 min | 2 panelists | Public speaking + audience read + handling a question they didn't prep — the actual public artifact of this job | Adjusts explanation when a panelist looks lost; admits a trade-off unprompted; handles an injected hostile question without deflecting | Reads slides; can't handle one unscripted question; over-claims certainty on a topic they clearly don't know well |
| 3 — Cross-functional working session | Review a real (anonymized) support thread or feature request, propose the fix/ticket live | 45 min | Product or eng stakeholder | Developer-empathy interviewing, API literacy, cross-functional influence — this is outcome 4 in miniature | Roots the complaint in an actual cause, not just sympathy; writes a ticket an engineer would act on without translation | Pure sympathy with no diagnosis; can't translate developer language into a product ask |
| 4 — DevRel-opinion round | Conversational, no memorized right answer | 30 min | Hiring manager + senior IC | DevRel philosophy, metrics literacy, whether they can name a funding driver and refuse a vanity ask | Names what they'd refuse to be measured on; distinguishes influenced pipeline from sourced revenue unprompted | Recites a generic definition of DevRel; treats follower count or star count as a real target |

**If the portfolio (Stage 1) scores under 6 on the six-signal rubric:** replace Stage 2 with a paid, scored work sample — a 5-minute lightning talk on a topic they pick — rather than judging by resume. Never unpaid spec work.

## Scoring mechanics — this is what actually stops the "gut feel" arguments

The failure mode you're describing (panel argues after the fact) is almost always a missing mechanism, not a missing rubric. Fix the mechanism:

1. **Every interviewer scores independently, in writing, with one evidence note per competency, before anyone talks to anyone else.** No shared doc open during interviews, no "so, what did everyone think?" before scores are submitted.
2. **Combine mechanically against the pre-set weights above** — 0–3 per competency × weight, summed. The debrief's only job is to calibrate what a "2" meant to each scorer, never to move a score.
3. **Set an advance threshold before the loop starts**, not after you see who applied (e.g., ≥ 2.0 weighted average to proceed past Stage 2, ≥ 2.3 to get an offer). Write it down where the whole panel can see it before the first candidate.
4. **A tie or a split panel is resolved by re-reading the evidence notes against the weights, not by a re-vote.** If the evidence notes don't resolve it, the rubric was ambiguous — fix the rubric for the next candidate, don't patch this decision with a gut call.
5. **Negative signals from the portfolio rubric are named, not softened**: no shipped code for a role that needs it, exaggerated or dismissed metrics, ghostwritten content the candidate can't defend live. Name these explicitly in the evidence note — "gap" and "red flag" are different notes and get treated differently downstream.

Quality-gate check on this kit: 5 outcomes quantified and ranked (✅), gatekeeper/pit-trap audit passed (✅), every interview question maps to a named competency (✅), no unpaid spec work when a public portfolio exists (✅), independent-then-mechanical scoring specified (✅), comp stance flagged rather than silently "competitive" (✅ — pending your real number).

---

# Part 2 — The Quarterly Exec Narrative Deck

**Named gap, said plainly:** no skill in this collection owns "how to tell the story." `devrel-metrics` decides what you're honestly allowed to claim; `devrel-budget-allocation` gives you the line-item table and forces a five-sentence narrative out of it. Neither one hands you a deck or a talk track — that part is general narrative craft, built below, not a packaged framework.

## Why last quarter's cut probably wasn't about performance

Grounded in the two skills' own documented failure modes — check which of these you actually did:

- **Activity log presented as a report.** "14 talks, 40 posts, 3 events" is effort, not outcome — it survives exactly one review, and you're describing the second one.
- **Reach relabeled as impact.** Impressions and follower counts renamed "developer reach" don't change what tier they're in. If your top slide led with a reach number, that's very likely what got cut.
- **No "so what."** If a number moved 20% and nobody in the room could say what they'd do differently, it wasn't a metric — it was decoration.
- **No pre-committed threshold.** If the ask for renewal came *after* the number, the panel reads it as a narrative invented to fit the ask, not a result.
- **No stated blind spot.** An exec who spots an unstated gap on their own discounts every other number on the page — including the honest ones.

If any of these lands, the fix isn't better slides — it's a different structure. Here's one.

## The deck — 8 slides, in this order, with the talk track

Use real Loamside numbers where I've marked `[ILLUSTRATIVE]` — everything else is the structure, which is the actual product here.

---

**Slide 1 — The one-sentence thesis**

> *Slide text:* "This quarter, [$X / hours] bought [enablement outcome], moved [product/business outcome], and one bet didn't pay off — here's what we did about it."

*Say it exactly like this, first, before any table.* You are pre-stating the entire deck's verdict in one sentence so nobody in the room has to wait 20 minutes to find out if this went well. This is the single highest-leverage sentence in the meeting — rehearse it until it's automatic.

---

**Slide 2 — The business risk this budget serves**

> *Slide text:* Tie the funded driver to a priority the exec team already tracks — not a DevRel priority, *their* priority. `[ILLUSTRATIVE]`: "Self-serve signups convert to paid at 3.1×; developer relations is the only function that touches that funnel before finance sees a contract."

*Talk track:* "Before the numbers — why this budget exists at all: [funding driver], tied to [the company OKR it feeds]. Everything on the next four slides is in service of that, nothing else."

This slide is what a reach-led deck skips, and it's why that deck reads as busywork instead of a program.

---

**Slide 3 — What we spent, plainly**

> *Slide text (from `devrel-budget-allocation`'s envelope):* Cash `[$X]`, hours `[Y FTE-equivalent]`, split committed / discretionary / borrowed / in-kind.

*Talk track:* "We spent [$X] and [Y hours]. [Z%] was already committed before the quarter started — the real decision this room is making is about the [remaining %]."

Naming the committed portion up front kills the "why can't you just cut everything 20%" reflex before it starts.

---

**Slide 4 — What it bought, tiered honestly**

One line at reach/engagement for context, then stop — spend the slide on enablement and one product- or business-impact number, each tagged.

> `[ILLUSTRATIVE]`
> - Reach (context only): 40K talk views — *not the point of this slide.*
> - Enablement: first-success rate 22% → 29% (**baseline**, 3rd period trend)
> - Product impact: 30-day retention of the cohort that used the new quickstart, +6pts vs. control (**baseline**)
> - Business impact: 15 qualified conversations *influenced* in developer-active accounts (**baseline** — never "sourced")

*Talk track:* "We could show you reach — we had it — but it doesn't answer your actual question, so here's what does." Then read the tags out loud: "This one's a baseline against our own history, not an industry number — I'll say that every time, because the day I don't is the day you should stop trusting the rest of this deck."

---

**Slide 5 — The line-item scoreboard**

> *Slide text:* Reuse `devrel-budget-allocation`'s table verbatim — Line / Cost / Threshold set *before* the quarter / Hit or miss / Action.

*Talk track:* "Every line here had a number it had to clear, written down before the quarter started — not chosen to fit what happened. [N] of [M] cleared theirs."

This is the slide that ends "gut feel" pushback from the exec side the same way the scorecard ends it on your hiring panel — pre-committed thresholds, not after-the-fact justification.

---

**Slide 6 — The miss, named first**

> *Slide text:* Name the one line that missed its threshold, and the action already taken — not planned, *taken*.

*Talk track:* "[Line] missed its threshold. We [cut it / renegotiated it / are running it one more quarter as an experiment with a fixed end date] — here's why that's the right call, not a excuse."

Volunteering the miss before anyone asks is the single biggest credibility move in the deck. A deck with zero misses reads as filtered, not as a good quarter.

---

**Slide 7 — The ask**

> *Slide text:* One number, one business outcome it buys, one date it lands by. Not a wish list.

*Talk track:* "Next quarter, [$X] buys [specific outcome], readable by [date]. If it doesn't clear [threshold] by then, here's what we cut ourselves — you won't have to ask."

Pre-committing your *own* next kill rule, out loud, is what makes the ask land as a plan instead of a defense.

---

**Slide 8 — Appendix: what we can't prove yet**

> *Slide text:* The blind spots, named — e.g., "no CRM touch field yet, so influenced pipeline is a manual pull, not a live number" or "cohort sample is under 30 in two segments, reporting raw counts, not rates there."

*Talk track (only if asked, otherwise leave it up during Q&A):* "Two things we're honest we can't fully back yet: [X], [Y]. Here's what closing that gap would take."

---

## Objection handling — the four questions that actually come up

| They ask | The one-line answer |
|---|---|
| "Why isn't this just pipeline?" | "We tag it *influenced*, never *sourced* — two teams claiming the same revenue as sourced is the fastest way to make every number in this room untrustworthy." |
| "Why should I believe this number over last quarter's?" | Point at the tag: "It's a **baseline** against our own history — I'm not claiming it against an industry figure, because there mostly isn't a real one for this." |
| "Why did you miss on [line]?" | You already answered this on Slide 6, before they asked. If it's a follow-up: state the action taken, not a plan to take one. |
| "What's the actual return on this whole function?" | "The line that answers that is [product/business impact number] — everything above it in the deck is what makes that one number possible, not padding." |

## Before you walk in — a checklist

- [ ] Slide 1's sentence is memorized, not read off the slide.
- [ ] No metric above Slide 4's "context only" line is a raw reach number presented as a result.
- [ ] Every number on Slides 4–5 is tagged sourced / baseline / hypothesis, said out loud.
- [ ] The miss (Slide 6) is named before Q&A, not extracted during it.
- [ ] The ask (Slide 7) has a number, a date, and your own kill rule attached.
- [ ] You can name one thing you're not yet measuring (Slide 8) without being asked.

---

**Two routines worth setting, dry-run only — say yes and I'll detail either:**

1. **Quarterly re-invocation of this kickoff**, timed to your budget cycle, so the deck and the scorecard both get re-validated against whatever changed instead of going stale.
2. **A measurement read** (`devrel-metrics` cadence) the month before each exec review, so Slide 4's numbers are never assembled the week of the meeting.