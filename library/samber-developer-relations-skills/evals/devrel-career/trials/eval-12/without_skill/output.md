# First Developer Advocate: hiring kit

Before drafting anything, lock two decisions — everything else follows from them.

**1. Pick the one problem this hire solves first.** "Developer relations" as an abstract mandate produces a job posting nobody can evaluate against and a hire who drifts. For a 60-person API company with zero DevRel history, the highest-leverage default is: **reduce time-to-first-successful-call and build the content foundation** (quickstarts, tutorials, sample apps) — it compounds through search/GEO, it's measurable (activation rate, time-to-first-hello-world), and it doesn't require a team. Community and conference presence are strong *second* mandates once that foundation exists. Override this if you already know your actual bottleneck (e.g., devs are churning after signup, or a competitor is winning mindshare at conferences) — but pick one, name it in the posting, and resist scope creep.

**2. Pick the reporting line.** For hire #1, report to Engineering (you), dotted-line to Marketing. Technical credibility is the scarce resource here; a DevRel hire who reports into Marketing from day one tends to get pulled into campaign work before the technical foundation exists. Revisit at hire #2–3.

Everything below assumes the "reduce time-to-first-call / content foundation" mandate. Swap the specifics if your bottleneck is different — the structure holds either way.

---

## 1. Job posting

*(Fill in bracketed placeholders — company name, API domain, comp band, location/remote policy. Don't leave the comp band blank; transparent ranges filter out mismatches before they cost you a loop.)*

---

### Founding Developer Advocate — [Company]

**About us**
[Company] is a [X]-person team building [API/product one-liner]. [N] developers currently integrate with our API. We've grown through [word of mouth / sales-led / whatever's true] — we've never had a dedicated developer relations function, and you'll be the first.

**Why this role exists now**
Developers hit friction we can't see from the inside: unclear docs, a slow path from signup to first successful call, no canonical sample apps, nowhere to ask a question and get a fast, correct answer. This role exists to close that gap — first by making the on-ramp obviously good, then by building the community and content that make [Company] the default choice developers recommend to each other.

**What you'll do (first 6 months, concretely)**
- Rebuild or rewrite our quickstart so a new developer reaches a working call in under [X] minutes.
- Ship 3–5 sample apps / reference integrations in the languages our users actually use.
- Publish technical content (tutorials, deep-dives, changelog posts) on a regular cadence.
- Instrument and own the activation funnel metric (signup → first successful API call) — you'll report on it, not just produce content and hope.
- Show up where our developers already are (GitHub issues, Stack Overflow, Discord/Slack, relevant subreddits) and turn recurring questions into docs fixes.
- Feed structured, prioritized developer feedback back to product and engineering — not "devs are unhappy," but "here are the top 5 friction points, ranked, with repro steps."

**What we're looking for**
Must-haves:
- You can build things with our API yourself — this is a hands-on-keyboard role, not a stage-only role. Comfortable in at least one of [primary languages your API is consumed in].
- You can write and explain technical material clearly to someone who doesn't have your context.
- You've done this before in some form — as an engineer who blogged/spoke on the side, a technical writer who coded, or a prior DevRel/advocate role. We don't require the exact title, we require the evidence (see "How to apply").

Nice-to-haves:
- Experience building a DevRel function from zero, not just operating inside an existing one.
- Comfortable on camera/on stage.
- Existing relationships in [your specific developer niche/ecosystem].

**What success looks like**
- 30 days: shipped or materially improved the quickstart; met every eng team lead; has a baseline read on the activation funnel.
- 90 days: 2+ published sample apps, first piece of content live, first structured feedback report delivered to product.
- 12 months: activation rate measurably improved; a content cadence developers actually return for; you've spoken up for [Company] somewhere developers gather (conference, podcast, or an active, credible presence in an existing community).

**Compensation & logistics**
[Comp band]. [Remote/hybrid policy]. [Travel expectations — be specific: "expect ~4 trips/year to conferences" beats "some travel."]

**How to apply**
Skip the cover letter. Send us:
1. A link to 2–3 things you've built or written that you're proud of (blog post, talk recording, GitHub repo, sample app — whatever best shows your range).
2. A short note (200 words max) on the worst piece of developer documentation you've encountered recently and what you'd change about it.

We'll use this in place of a resume screen.

---

## 2. Interview loop

Five touchpoints past the recruiter screen, ~2–3 weeks end to end. Give candidates real API sandbox credentials ahead of the technical exercise — evaluating them against the actual product beats a synthetic prompt.

| Stage | Format | Duration | Who | Tests | Pass bar |
|---|---|---|---|---|---|
| 1. Recruiter screen | Call | 30 min | Recruiter | Logistics, comp alignment, basic motivation | Go/no-go |
| 2. Hiring manager screen | Call | 45 min | You (VP Eng) | Do they understand what this role actually is; why DevRel, why now, why us | Would you trust them speaking for the company publicly, unsupervised |
| 3. Technical + writing exercise | Async take-home, capped effort | ~3–4 hrs | — | Build a small integration or sample app against our real API, plus a short accompanying post/doc explaining it | Scored against the rubric in §3 |
| 4. Teach-back | Live presentation + Q&A | 45 min | Mixed panel (2–3 eng + 1 non-technical) | Stage presence, clarity under questioning, can they simplify without dumbing down | Non-technical panelist can explain the topic back afterward |
| 5. Cross-functional panel | 2× 30 min | Eng peer + product/support stakeholder | Collaboration, empathy for developer pain, whether feedback becomes structured input or just complaints | Both panelists would want to work with this person day to day |
| 6. Final conversation | 30–45 min | You or exec | Values fit, career trajectory, close | Offer decision |

Notes:
- Stage 3 and stage 4 deliberately overlap (both test communication) — that's intentional. A portfolio can be ghostwritten or agency-polished; live Q&A can't. If stage 3 work is excellent but stage 4 falls apart, trust stage 4.
- Cap the take-home explicitly ("stop at 4 hours, tell us what you'd have done with more time") — uncapped take-homes select for people with free time, not people who are good at the job.
- Don't skip stage 5. DevRel is a glue role; a brilliant communicator who can't take engineering feedback seriously, or who can't turn "devs are confused" into something product can act on, will underperform regardless of how good stage 4 looked.

---

## 3. Portfolio / work-sample scoring rubric

Use the same rubric for the candidate's existing portfolio *and* the take-home exercise — score them separately, then look at the pair together (a strong take-home next to a weak portfolio, or vice versa, is itself a signal worth discussing).

### Dimensions and weights

| Dimension | Weight | 1 (weak) | 3 (solid) | 5 (exceptional) |
|---|---|---|---|---|
| Technical credibility | 30% | Doesn't work, copy-pasted, or falls apart under a follow-up question | Correct, functional, handles the obvious cases | Correct, handles edge cases, shows understanding beyond the spec |
| Teaching clarity | 25% | Assumes reader context, jargon-dense, hard to follow | A motivated reader can follow it through | A newcomer could follow it start to finish with no prior context |
| Evidence of impact | 20% | No metric offered, or only vanity numbers (views, likes) | Some indication the work reached or helped real people | Clear before/after metric plausibly attributable to their work (adoption, resolved-question rate, audience size with context) |
| Authentic developer voice | 15% | Reads like marketing copy; a developer would bounce off it | Reads like a builder talking to builders | Distinct voice, developers would seek out more of it |
| Product/feedback instinct | 10% | Complaints without structure ("docs are bad") | Identifies specific problems | Turns dev pain into a prioritized, actionable brief a PM could act on directly |

Weighted score = sum(dimension score × weight). Max 5.0.

### Decision rule
- **Advance:** weighted average ≥ 3.5, and no single dimension below 3.
- **Discuss as exception:** weighted average below 3.5 but technical credibility = 5 and teaching clarity ≥ 3 — a strong builder who's underdeveloped as a communicator can be coached; the reverse (great writer, can't build) is a much harder gap to close for a hands-on-keyboard role.
- **Reject:** any dimension at 1, or weighted average below 3.0.

### Watch for these false signals
- **Prolific but hollow:** a large content output where nothing links back to working code. Weight technical credibility heavily for exactly this reason — DevRel content that isn't grounded in real building erodes trust with the audience it's meant to win.
- **Portfolio built by someone else:** agency-polished blog posts, a company's design team behind their slides. This is what stage 4 (live teach-back) exists to catch — score the live session, not the portfolio, when they diverge.
- **Range mistaken for depth:** a candidate with one sample in five different formats (one tweet, one blog post, one 3-minute video, one repo, one talk abstract) can look broad and be shallow everywhere. Prefer 2–3 genuinely strong samples over five thin ones — this matters more for a *first* hire who'll be covering the on-ramp mandate alone, without a team to fill gaps.

### Scorecard template (copy per candidate)

```
Candidate: ______________________
Source: [ ] Existing portfolio  [ ] Take-home exercise

Technical credibility   (30%)  Score: __  Notes: ____________
Teaching clarity        (25%)  Score: __  Notes: ____________
Evidence of impact      (20%)  Score: __  Notes: ____________
Authentic voice         (15%)  Score: __  Notes: ____________
Product/feedback instinct (10%) Score: __  Notes: ____________

Weighted average: __ / 5.0
Recommendation: [ ] Advance  [ ] Discuss  [ ] Reject
```