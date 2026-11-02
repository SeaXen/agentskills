Quick caveat up front: I don't have live access to research the actual "Deploy Friday" show or pull the current README from your caching library's repo in this session, so I can't tell you the host's style or verify current benchmark numbers. I'm assuming the library is **samber/hot** (your Go caching library) since that's what you're known for — swap in specifics if it's a different project. Two things worth doing yourself before Thursday, 5 minutes each: skim the last 3 episode titles/descriptions of Deploy Friday (Apple Podcasts or Spotify) to see if it's deep-technical or casual-chat, and re-read your own README once so exact numbers are fresh.

Here's your prep.

## The mindset (read this first)

You weren't invited to give a lecture. The host wants a conversation about a thing you built. "Let's talk about your caching library" is an *opening*, not an agenda — they'll steer with questions, you bring stories and specifics. Nobody expects a polished monologue from a first-timer, and hosts actively don't want one. Answer, then stop talking. If you don't know where an answer is going, land it in two sentences and let the host ask the follow-up.

## Your throughline (memorize this shape, not a script)

Three beats, in order, that any caching-library conversation will naturally move through:

1. **The itch** — what problem made you build this instead of using something else.
2. **The design** — the two or three decisions you'd defend in an argument (eviction strategy, API shape, concurrency model).
3. **The payoff** — who uses it, what it's for, what's next.

If you only remember one thing walking in: you can always return to "the itch" when a question stumps you. "That connects back to why I built this in the first place — ..." buys you time and reorients to ground you know cold.

## Talking points bank

### 1. Origin ("So how'd this happen?")
- What you were working on when existing options fell short. Name the actual pain: too slow, wrong eviction policy, no generics, allocation-heavy, wrong concurrency guarantees — pick the real one.
- Why "just use Redis" or an existing in-process cache (Ristretto, BigCache, groupcache, ccache) wasn't the answer for that case. Frame as trade-offs, not trash-talk — every one of those is a fine library solving a different constraint.
- The moment it went from "personal itch" to "worth open-sourcing."

### 2. What it actually is (be ready to explain in one breath)
- One-liner: an in-memory (or pluggable/distributed) Go cache with generics, safe for concurrent use, supporting multiple eviction algorithms.
- Which eviction algorithms it supports (LRU / LFU / ARC / 2Q / whatever's current — confirm exact list from your own README before Thursday) and *why more than one matters*: different access patterns (scan-heavy, recency-biased, frequency-biased) need different eviction logic, and forcing everyone onto LRU is the default mistake most cache libraries make.
- Generics: why `Cache[K, V]` matters over `map[interface{}]interface{}` — type safety, no reflection/boxing overhead, better ergonomics.

### 3. Design decisions worth defending
Pick 2-3 you can talk about for 90 seconds each, with a concrete "here's the alternative I rejected and why":
- Concurrency model — sharding vs single mutex vs lock-free, and what that trades off (throughput vs simplicity vs memory).
- API surface — why it looks the way it does (functional options? `Get`/`Set`/`GetOrSet`? TTL support built in?).
- Benchmarks — if you have numbers vs stdlib map+mutex, or vs Ristretto/BigCache, have the actual figures ready, not "it's really fast." Specific beats vague every time on a technical podcast.
- Anything you got wrong in v1 and fixed later — hosts and listeners love an honest "I designed this wrong the first time" story more than a highlight reel.

### 4. War story (have one ready)
The hardest bug or design reversal during development. Concrete detail sells it: what broke, how you found it, what you changed. This is usually the most memorable 90 seconds of the whole episode — don't skip prepping it just because it wasn't explicitly asked for.

### 5. Who's it for / real usage
- What kind of system benefits most (high-throughput API layer, computed-value memoization, rate limiters, whatever's true for `hot`).
- If you know of real adoption (stars, known users, a case where it solved something specific), mention it — concrete beats "people seem to like it."

### 6. Where it's going
- One or two things on the roadmap. Doesn't need to be a promise, just "here's what I'm thinking about." Gives the host a natural closing question and gives you a reason for people to come back and check the repo.

### 7. Close / CTA
Have this ready verbatim, since it's the one part you fully control:
> "If you want to try it, it's `github.com/samber/hot` — open an issue if something's confusing, I read all of them."

Simple, no hard sell. A caveman-mode plug beats a marketing pitch on a dev podcast.

## Likely curveballs, pre-answered
- **"How is this different from [Ristretto/BigCache/groupcache]?"** — Answer with trade-offs, not superiority. "Different defaults for different access patterns" is both true and safe.
- **"Would you use this in production at scale?"** — Answer honestly. If yes, say where/how. If it's more for certain workloads, say that.
- **"What don't you like about it / what would you change?"** — Have a real answer. Feigning "it's perfect" reads as inexperience; naming a real limitation reads as expertise.
- **"What's next for you?"** — Doesn't have to be about this library. Fine to mention other projects (lo, do, oops, mo) briefly if it comes up naturally — don't force it.

## Mechanics, since it's your first time
- Ask the host beforehand (if not already told): rough length, whether it's a Q&A or free-flowing chat, whether they'll share topics/questions in advance.
- Have a glass of water nearby, headphones in, sit somewhere quiet, close Slack/notifications.
- It's fine to pause and think mid-answer — dead air edits out cleaner than a rushed non-answer.
- If you don't know something, say "good question, I haven't thought about that" — real, and better than guessing on record.
- Don't try to hit every bullet above. Pick your best 2-3 stories; let the host's questions surface the rest.

## The one-liner, memorized cold
> "It's a Go caching library — in-memory, generics-first, and it lets you pick your eviction strategy instead of forcing LRU on everything."

That's your answer to "so what is it" if asked cold, in any context, half-asleep. Everything else in this doc is elaboration on that sentence.