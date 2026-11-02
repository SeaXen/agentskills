## Time reality check first

A "10-minute lightning slot" is rarely 10 minutes of talking. Walk-on, clicker fumble, laugh lines, and an MC who cuts the mic on the second means your actual content budget is **~8 minutes**. Treat 8, not 10, as your target.

## The rule: cut a section, don't compress three

The instinct is to speed-run all three sections + demo at 3x speed. That's the standard lightning-talk failure mode — nobody retains a rushed tour of three ideas. At 8 minutes you get **one idea, well told**, not three ideas badly told.

So: pick the single section with the best hook-to-payoff ratio (usually "why naive `json.Unmarshal` allocates and what that costs you" — it's the most relatable pain point) and cut the other two sections outright. Don't shrink them to bullet points as a "quick mention" — a mentioned-but-unexplained idea wastes seconds and lands nowhere.

## Kill the live demo, keep the number

Live benchmark demos don't survive a lightning slot — no time to build/run, and the audience can't absorb `benchstat` output flashed for 4 seconds. Replace the demo with **one static slide**: the headline number you already generated for the 30-min version (e.g. "0 allocs/op vs 12, 3x throughput"). State it, don't run it. Point to the repo/blog post for the methodology.

## Suggested 8-minute shape

1. **Hook** (15s) — the pain: "this JSON decoder does 12 allocations per request and your GC feels it."
2. **The one technique** (5-6 min) — pick your strongest single lever from the 30-min talk (e.g. avoiding `interface{}` boxing via a custom decoder, or reusing buffers with `sync.Pool`). Show one code snippet, before/after.
3. **The number** (30-45s) — static benchmark slide, no demo.
4. **CTA** (15-20s) — "full version with two more techniques and a live benchmark at [conference/blog/repo] — come find me after."

That last line does double duty: it's honest about what got cut, and it's a natural teaser for the 30-min and 40-min versions.

## How to actually build it (don't fork the deck)

Since this is the same talk shown four times, don't maintain four decks — you'll drift and forget which one has the fixed typo. Instead:

- Keep **one master deck**, organize slides into named sections (Hook / Section A / Section B / Section C / Demo / Close) using your slide tool's section markers.
- Build each event's version by **hiding sections**, not deleting or rewriting slides — the lightning version is "Hook + Section A + Close" with everything else toggled hidden.
- For the two 40-min internal sessions, go the other direction: same 30-min section set, but un-hide extra depth slides (edge cases, customer-specific Q&A prompts) you keep parked at the end of each section specifically for the longer slots.
- This way a fix to Section A's code snippet propagates to all four versions automatically, instead of needing to be re-applied three times.

## Rehearse the cut version standalone

Time it on its own, not as "the first third of the 30-min talk mentally paused." A section that flows fine as part 1 of 3 often needs its own transition sentences once the sections before/after it are gone — the connective tissue you cut needs replacing, not just deleting.