## Are you over?

Yes — using the 150 wpm figure you asked me to assume:

- **1,640 words ÷ 150 wpm = 10:56** of narration alone, before a single second of dead time (builds, installs, page loads, pauses) is added.
- Target is 9:00 → budget is **1,350 words** at that rate. You're **290 words over** (~18% of your narration, ~22% past the 9-minute target).
- Spread across 19 beats, that's roughly **15 words/beat** of excess — small per beat, real in aggregate.

And it gets worse before it gets better: the skill's runtime formula is *narration ÷ rate + per-beat dead time*, not narration alone (workflow step 7; pass-threshold criterion 4). A Halyard CLI tutorial is going to have install steps, command output, page loads — none of that is in your 1,640-word count yet. Whatever your dead-time budget adds, it adds on top of an already-over number.

One caveat on the premise: don't actually ship the recording against 150 wpm. That's a table value, and the skill is explicit — *"Budget runtime from the recorder's own measured rate, never a table value."* Get the person who's recording to read two or three representative beats aloud, measure their real wpm, and rerun this division before you finalize cuts. 150 is a reasonable placeholder to know you have a problem right now; it's not the number to cut against.

## Should you talk faster?

No. And the finding you're half-remembering doesn't actually say what you think.

The source (Guo, Kim & Rubin 2014, the same MOOC study this skill draws its length numbers from) found engagement rose with speaking rate *in general* — but their own stated caveat is: *"speaking rate is merely a surface feature that correlates with enthusiasm… our recommendation is not to force instructors to speak faster."* Faster speakers scored better because they were more energized, not because raw words-per-minute is a retention lever. Forcing the number without the energy doesn't reproduce the effect.

It's worse than neutral for your specific case: that same paper found that **for 6–12 minute videos — your exact band — engagement *dipped* in the 145–165 wpm quintile.** That's precisely where the "150 wpm standard" you were about to speed up from already sits. Pushing faster from there has no engagement evidence behind it at this length, and it works against the two things a build-along tutorial needs most: beats stay re-shootable and audio-only-teachable (pass-threshold criterion 3) — speed you didn't earn is exactly how a script produces the "unspeakable line" failure mode (too tangled to say in one breath, which is also what breaks captions).

## What to do instead

Cut, don't compress. The skill's rule is explicit: *"Compare against the target; cut before recording, never after."* You already have the mechanism for this — pass-threshold criterion 6 requires every beat marked core or cuttable, such that trimming all cuttable beats still delivers the promise. Find ~290 words (plus whatever your dead-time budget adds) inside the cuttable beats, not by shaving a few words off every line. If no beat is cuttable enough to close the gap, that's a sign one of your 19 beats is carrying two concepts and should either be cut or split into a segment of its own — not sped through.