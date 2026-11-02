No, none of the three are real, documented standards. Here's where each one actually comes from.

**"Three clean cold runs"**
No source. No style guide, conference organizer, or DevRel handbook publishes a number of required rehearsals. It's an arbitrary anchor, not a validated threshold. The real underlying idea — rehearse a demo cold until it stops surfacing new failure modes — is sound advice, but the number of runs that takes depends entirely on how flaky your specific demo is. For a stable CLI command that might be one run; for something touching network calls or timing it could be ten.

**"Twenty seconds before bailing to the backup video"**
Also no source. The real advice that exists in speaker-coaching circles is "decide your bail trigger before you're on stage" — true and worth keeping. But the actual cutoff is a judgment call tied to your demo's failure modes and how patient your specific audience will be, not a fixed duration anyone tested and published.

**"24pt terminal is the standard"**
Closer to real but still not "the standard." Font-size recommendations for live-coding terminals do show up as a rule of thumb in various "how to give a good tech talk" advice from conference organizers and speakers — readability from the back of a room is a real constraint. But it depends on room size, screen resolution, and projector quality, which is exactly why no spec fixes it at 24pt over 28pt or 32pt. Anyone who says otherwise is repeating someone else's specific room setup as if it generalizes.

**What actually happened here**

These are heuristics that got stated with more confidence than they had, then got treated as citable facts once repeated a second time. That's on me if I'm the one who told her — a specific number sounds authoritative, and "the standard" language makes it sound sourced when it isn't. Neither claim is malicious; it's just how confidently-stated rules of thumb calcify into "industry standard" after one retelling.

**What to do in the policy doc**

Don't write "industry standard" next to any of these three numbers — that phrase invites someone to ask "says who?" and there's no answer. Two honest options:

- Keep the numbers, but label them as your team's own convention: "we require 3 cold runs before a live demo" is a perfectly fine internal rule. It just isn't external validation, and the doc shouldn't imply it is.
- Replace the fixed numbers with the principle behind them, and let each presenter calibrate: rehearse until failures stop appearing; pre-commit to a bail trigger before going on stage; pick a font size you've personally confirmed is readable from the back row of the actual room you're presenting in.

Either is defensible. Citing invented numbers as "industry standard" is not — it's the one version that breaks the moment someone checks.