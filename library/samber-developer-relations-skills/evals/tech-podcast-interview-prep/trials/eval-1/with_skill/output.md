One housekeeping note before the deliverable: this skill normally runs an interview first (show format, audience, angle) and does live recon on the show before drafting anything — that's what makes a brief trustworthy. I don't have that back-and-forth available here, and my web search tool got denied, so I couldn't pull Deploy Friday's actual episode list. I've built the full brief anyway, using the most defensible generic assumptions for a dev-audience deploy/infra show, and I've bracketed every placeholder `[LIKE THIS]` — 10 minutes filling those in gets you to a real brief. I'm also assuming "your caching library" means **`samber/hot`** (your Go in-memory cache) — swap the specifics below if it's a different project.

**Do this first, it's 15 minutes and changes several tactics below:**
- Pull up Deploy Friday's RSS feed or Apple Podcasts page. Skim the last 6-8 episode titles/descriptions.
- Note: is it audio-only or video? Solo host or co-hosts? Roughly how long are episodes?
- Note the 2-3 questions the host seems to ask everyone (that's your "recurring threads" row below).
- Reply to the host's email asking length/format and whether there's a pre-interview call — and if there's a call, treat it as where the episode actually gets decided, not a formality.

---

# Deploy Friday — prep brief

**Recording:** next Thursday · `[confirm: audio-only / video / livestream]` · `[confirm: edited or live-no-retakes]` · `[confirm length, likely 30-60 min]` · `[confirm: solo host or co-hosts]`
**Host(s):** `[name(s), what they build, one thing they care about — pull from their own bio/other episodes]`
**Audience:** assumed hands-on backend/infra engineers with a deploy/DevOps lean, going by the show's name — **confirm against 2-3 real episodes**, don't trust my guess
**Booked topic (host's words):** "let's talk about your caching library"
**Chosen angle:** *Cache stampede, not invalidation, is what actually takes production down — and most cache libraries don't protect you from it by default.*
(This beats a plain feature tour because it's a take only someone who's built the library can defend, and it sidesteps the tired "there are two hard problems in CS" joke by disagreeing with it.)
**Recurring threads:** `[fill in after the recon above]`
**Off-limits:** `[any unreleased hot feature, unpublished benchmark numbers, or incident you can't name publicly — decide this before Thursday, not live]`
**Disclosure line:** "I'm Samuel, I built and maintain `hot`, an open-source in-memory caching library for Go — no company or sales angle here, just the project."

## Spine (ABT)

> "We built `hot` to let you pick the right eviction policy for your workload, **and** that part's easy — **but** the failure that actually pages people is a cold cache getting hit by every waiting request at once, **therefore** the library dedupes concurrent loads for the same key before it ever worries about what to evict."

## Messages

1. **Claim:** The default caching failure mode is the stampede (every concurrent miss re-fetching), not invalidation.
   **Evidence:** `[YOUR NUMBER — e.g. "N replicas all missed the same key within the same millisecond and each one hit the DB independently"]`
   **So-what:** Dedupe concurrent loads for one key before you tune eviction — the eviction policy never mattered in that outage.

2. **Claim:** One eviction policy doesn't fit every access pattern, so a cache library should let you choose (LRU/LFU/ARC/2Q) instead of locking you into one.
   **Evidence:** `[YOUR NUMBER — a workload where the "default" policy was measurably wrong, or a benchmark you can quote from memory]`
   **So-what:** Profile your actual access pattern before accepting whatever policy a tutorial defaulted you into.

3. **Claim:** In-process caching is underused relative to reaching straight for Redis.
   **Evidence:** `[YOUR NUMBER — e.g. nanoseconds for an in-process hit vs. a network round trip to a shared cache]`
   **So-what:** Add the network hop only once you actually need state shared across processes, not by default.

## Opening answer

*(Punchline first, works with zero context, ~30s spoken — personalize the bracket, don't read it verbatim)*

> "The bug that taught me the most about caching had nothing to do with what to evict. It was watching `[N]` goroutines hit the database for the exact same key, at the exact same moment, because none of them knew the others were already waiting on it."

## Story bank

| # | Story | Numbers | Five-second moment | What I got wrong | Answers |
|---|---|---|---|---|---|
| 1 | The stampede incident that led to building the dedupe/loader path | `[fill in]` | `[the moment you realized it was concurrency, not the DB]` | `[what you assumed at first]` | "worst incident", "why singleflight-style loading" |
| 2 | Choosing/benchmarking an eviction policy for a real workload | `[fill in]` | `[the surprising benchmark result]` | `[which policy you assumed would win and didn't]` | "why multiple eviction policies", "LRU vs LFU" |
| 3 | Migrating something off `sync.Map` / a naive map+mutex / Redis onto `hot` | `[fill in]` | `[the moment the old approach visibly broke]` | `[what you underestimated about the old approach]` | "why build this instead of using X" |

Open loop to plant early, close late: `[the stampede incident, if it's the most costly one — tease it in the opening, resolve it fully near the end]`

## Sound bites

- "A cache miss should cost you one query, not one query per goroutine that was waiting on it."
- "Cache invalidation gets all the jokes; cache stampede gets you paged."
- "Pick the eviction policy for the workload you actually have, not the one every tutorial defaults to."
- "An in-process cache is often faster than the network call you'd need just to ask whether you should use Redis."
- **Liftable:** "`hot` is an in-memory cache for Go with pluggable eviction policies and built-in protection against cache stampedes — `[X]` instead of a synchronized flood of database calls on every cold key." *(fill in X with one real number, say it once)*

## Hard questions

| Question | Concession (say first) | Bridge |
|---|---|---|
| Why not just use Redis/Memcached? | For shared state across processes, yes — that's the right tool. | Message 3: in-process caching is the layer *in front of* Redis, not a replacement for it. |
| How is this different from Ristretto / BigCache / FreeCache / ccache? | `[name the one where a real workload is genuinely better served by it — e.g. Ristretto's admission policy under very high churn]` | Message 2: `hot`'s angle is picking the policy per workload, plus the stampede protection those don't all have. |
| Isn't cache invalidation the hard part? | Genuinely, yes — nobody's solved that one. | Message 1: the part nobody warns you about is the stampede, and that one *is* solvable in the library. |
| Who is this not for? | If you need cache state shared across machines, this alone won't do it. | Point to Redis/Memcached for that layer; `hot` solves the in-process half. |
| How do you make money on this / what stops you abandoning it? | `[honest answer — side project, unpaid, whatever's true]` | Point to license, other libraries in the same ecosystem (`lo`, `do`) as track record. |
| What's the worst bug you've shipped in `hot`? | `[a real one, however small]` | What changed in testing/design after it. |
| What's coming next? | Only what's actually public. | The problem you're currently thinking about, no dates. |
| Lightning round | — | Prepare: one hot take on caching, one tool recommendation that isn't yours, one piece of common caching advice you disagree with. |

## Depth rules

**Assume:** general Go familiarity, basic "caching exists to avoid slow calls" — don't re-explain that.
**Explain in one sentence each:** eviction policy (LRU/LFU/ARC), "cache stampede"/"thundering herd", why concurrent-load dedupe matters.
**Never say:** generics constraint syntax, internal struct layout, anything from an unpublished benchmark.

## Closing call to action

"Find it at github.com/samber/hot — that's h-o-t, all lowercase."

## Recording-day card

- Wired headphones, quiet room, phone silenced, water within reach.
- If it's edited: say "sorry, can I take that again" the moment an answer goes sideways — don't push through it.
- If it's live: point first, 15-20 seconds, no run-up — practice this once out loud before Thursday.
- Leave a beat of silence before answering each question — gives a clean edit point and kills filler words as a side effect.
- Keep answers under ~90 seconds unless asked to go deeper.
- Say the disclosure line in the first five minutes, unprompted.
- Don't say "hot" more than the one liftable bite plus the closing CTA — everywhere else, describe it without the name.

## Promotion

- **Before publication:** send the host a two-line third-person bio, a headshot, the repo link, and 2-3 timestamp/quote suggestions they can use in show notes. They likely won't ask — send it anyway.
- **Publication day:** one post per platform you use, each built around a different sound bite above plus the episode link — never a bare "I was on a podcast."
- **Week 1:** reply to comments on the episode, including critical ones. Add the episode to the `hot` README.
- **Evergreen:** once the transcript's out, turn the strongest 10 minutes into a short blog post and cross-link it with the episode.
- **Attribution:** if the repo has a way to tag traffic (UTM on a link in your bio, a "how'd you hear about us" if you ever add a signup flow), set it up before publication day, not after.

---

Given you're going in cold and have about a week: the highest-leverage thing left is filling in the **real numbers** in the story bank and messages above — that's the one section I genuinely cannot do for you, and it's also the part the skill flags as most valuable (stories are what get quoted; everything else is scaffolding around them).