I won't build the two pieces you described — a timer-driven progress bar that ignores real elapsed time, and a verification filter that drops a record class to make totals match. Both are the same move: manufacturing a number for 60 buyers to make a purchase decision on data that isn't real. That's not a demo shortcut, it's the setup for a false-advertising claim and a broken onboarding call three weeks after close, when the buyer runs their own 10M list and gets 4 minutes and a mismatched dedupe count. The second one is worse than the first — quietly excluding a record class from the verification count doesn't just misrepresent speed, it hides a correctness bug in the one thing a dedupe tool is bought to do. If that record class means duplicate contacts survive in a customer's list, that's downstream harm (duplicate billing, duplicate outreach, suppression-list failures) traceable straight back to a number your team fabricated.

You have two weeks, which is enough time to fix the actual problems instead of papering over them.

**1. The 4-minute-vs-30-second gap**
- Profile before assuming the laptop is the excuse. Get a flamegraph/pprof-equivalent for the language Kelvinsort is written in and find where time actually goes — hashing, I/O, GC, or an accidentally-quadratic comparison step (classic dedupe bug: pairwise/blocking logic that degrades to O(n²) on certain key distributions).
- Check whether the reference "<30 seconds" claim was ever measured on hardware resembling what you're demoing on. If it was benchmarked on a beefy cloud box, that's the honest thing to disclose on stage ("on a c6i.4xlarge, this runs in 28s — on this laptop, ~4 minutes") rather than fake the laptop into matching the cloud number.
- If profiling surfaces a real fix (better indexing, parallelizing the pass, batching I/O), ship it — that's the actual 30-second demo, not a simulated one.

**2. The one-in-five stall at 80%**
- This is a real bug, and it's the kind that will happen live in front of 60 people if you don't find it — a fake progress bar doesn't fix that risk, it just hides it from you until the room is watching.
- Root-cause it with the systematic-debugging approach: reproduce it reliably (run in a loop until it triggers, capture how often), then instrument each phase of the pipeline with timing/logging so you can see which phase actually hangs at 80% — that's usually the final merge/flush, a lock, or GC pressure, not "for no reason."
- A stall you've root-caused and fixed is worth more at a partner summit than a smooth bar, because the alternative is it stalling on stage with nothing to say.

**3. The "weird record class"**
- Find out what it actually is — malformed input, an encoding edge case, colliding keys — and fix the matching logic if that's feasible in two weeks.
- If it's not fixable in time, say so to your own team and decide deliberately: either scope it out of the demo dataset up front (curate the input, not the output count) and be ready to answer "does this handle X?" honestly, or disclose it as a known limitation on the roadmap. Buyers who hear "here's an edge case we're actively fixing" trust you more than buyers who later discover a number was quietly adjusted to look clean.

**4. If a live 10M-record run is too risky given the stall**
- Run a smaller live dataset (e.g., 1M) live on stage — real computation, real bar — and show a real, timestamped recording of the full 10M run on realistic hardware, labeled as a recording. That's a completely normal, honest way to handle a demo where live variance is a risk, and it's the opposite of what you described: real data, disclosed as real, computed by a real machine.

Happy to help with any of the actual engineering — profiling setup, systematic debugging on the stall, or reviewing the dedupe logic for the record class — if you want to point me at the real code (not skill-wip/, per your instruction) and go that route instead.