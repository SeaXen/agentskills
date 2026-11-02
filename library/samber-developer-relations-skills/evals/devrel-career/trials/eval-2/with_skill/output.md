Read the skill and its five reference files in full. Below is the deliverable — an entry-path roadmap for the DevRel-engineer target, using the skill's routing rules and rubric.

A few inputs the skill asks for weren't stated; I made the smallest reasonable assumption on each and flagged it under **Open questions** rather than stopping to ask, since you asked for the complete answer directly.

---

# Entry-path roadmap: DevRel engineer (product-focused advocate), database niche TBD — from 9 years of CS teaching, Leeds

## Where you are

Nine years teaching high-school CS is an *adjacent* seat, not an engineering one — strong communication and pedagogy, but "Python at teaching level" is below the bar this specific sub-role screens on. You've already named the target precisely: DevRel engineer / product-focused advocate (the skill's role table treats these as the same row — home in product or engineering, core job is tooling, integrations, and carrying developer context back to product), explicitly *not* the outreach/evangelist flavour. That precision matters: the two are screened on different evidence, and picking one is a step most candidates skip. The binding constraint isn't time or money — you've removed both with the 3-year runway and no deadline — it's that the product-focused/DX track is screened on a **recent engineering background**, and no volume of content substitutes for that. That single fact reorders everything below.

## Assessment

Scored against the signals a product-focused advocate (DevRel engineer) is weighted on — code-in-public and the developer-voice artefact carry the most weight for this specific sub-role, per the rubric:

| Signal | Score now | Evidence | Gap |
|---|---|---|---|
| Code in public | 0 | none | A repo a stranger can run: an integration or sample app against a real database, not a teaching exercise |
| Developer-voice artefact | 0 | none | A published friction log on that database's onboarding, with fixes proposed |
| Public writing | 0 | none | Dated posts on the chosen database, at least one showing a result |
| Community evidence (contribution history) | 0 | none | Merged PRs / issue threads in that database's own project — this is also what proves "recent," not a job title |

One asset doesn't show up on that table but is real: nine years of explaining hard things to novices is exactly the skill a typical engineer-turned-advocate lacks and has to fake. Don't let it get folded into a vague "great communicator" line — reframe it later as one dated public teaching artefact once you have something technical to teach.

**Route decision.** Of the skill's five entry routes, two are deleted outright: internal transfer (a school has no DevRel function to transfer inside) and community volunteering (it doesn't build the coding depth this specific sub-role screens on, so it's not worth your unpaid years). Between the two coding routes, "engineer → writing → speaking" assumes you already code professionally — you don't yet. That leaves **learn to code first**, which the skill explicitly promotes to the top of the order when both are true: the target role has a hard code gate, and the candidate has years of runway and no deadline. Both are true here. It's the slowest of the five routes and the only one with no prerequisite to start — which fits someone starting from zero.

## What to do next

1. **Pick one database, in writing, by 2026-10-04.** Not "databases" — one product. Julien's rule applies: pick the one you'd use even if no one paid you. Given you're starting from Python, weight toward ecosystems with approachable OSS communities and strong Python surfaces for a first-time contributor — PostgreSQL (psycopg/SQLAlchemy), DuckDB, SQLite, or a vector store like pgvector are more tractable first footholds than a large distributed system's internals. Proof it happened: a one-paragraph niche statement, dated. *Why first:* the skill names "choosing the niche last, or never" as a named failure mode — everything else compounds on this choice.

2. **Build real engineering fluency against that database for ~6 months (2026-10 → 2027-04), using evenings, weekends and school holidays** — don't quit teaching yet. Ship one working integration or sample app in a public repo with a README a stranger can follow. Proof: the repo, plus a commit history that isn't a single dump. *Why:* this is the actual code gate; nothing else on this list substitutes for it.

3. **Starting month 2 (~2026-11), publish in parallel, not after.** One friction log on that database's onboarding (header → scenario → verbatim log → traffic-light highlights → three prioritised fixes), then roughly one post a month documenting what you're building. Proof: dated, linked posts; the friction log published as a contribution, not a takedown. *Why next rather than later:* it's the cheapest, rarest signal in the whole rubric, and it only needs whatever you've learned that month — no reason to wait for the code to be "finished."

4. **Start contributing to that database's own open-source project by month 3-4, aiming for a visible history by month 9-12 (~2027-06 → 2027-09).** Docs fixes count fully. Proof: merged PRs or issue threads under your name. *Why:* this is what makes your engineering background *recent* without a job title, and it puts your name inside the actual community the target company hires from — much DevRel hiring happens through referral and community visibility before a posting exists.

5. **At month 12 (~2027-09), re-run this six-signal check before applying anywhere.** Below roughly 6 (weighted toward code + developer-voice), keep producing — applying won't help yet. At 6-11, apply selectively where your strongest signals match the specific posting. At that point also screen any posting you consider against the two named trap patterns: an impossible-person "gatekeeper" list, or a founding "pit trap" with no ladder and no resources — both are reasons to skip, not reasons to doubt yourself. *Why last:* it's the point the skill's own threshold says the constraint shifts from production to targeting.

## Review point

- **2027-03-20 (6 months):** niche still held, one public repo exists, friction log published. If not, the fix is narrowing scope to one smaller integration, not adding new commitments.
- **2027-09-20 (12 months):** full six-signal re-score. Three branches from here: hold the current evening/holiday pace if signals are climbing steadily; spend part of the 3-year runway on a deliberate, time-boxed (3-6 month) full-time push once the constraint is clearly targeting rather than production; or change niche if that database's community turned out to be a poor fit — better to find that at month 12 than month 30.

## Open questions

- **Exact database/product** — you named "a database company" but not which technology; I gave you the decision method and a shortlist, but the pick is yours to lock by month 1.
- **Company size target** — early-stage, scale-up, big-tech-adjacent, or OSS-first/foundation. This changes the coding-depth bar and what "senior" even means there; not stated.
- **Leeds/UK meetup scene and remote tolerance** — changes whether a speaking artefact later routes through an in-person lightning talk or a recorded video only.
- **Whether the 3-year runway is a hard ceiling or just a comfort margin** — I assumed you'd rather keep teaching through month 12 and treat the runway as a later accelerant, not spend it immediately. Correct me if you'd rather front-load a full-time push now.
- **"No deadline," fully open-ended or informally bounded** (an age, a life event) — changes how hard to compress the multi-year route above.