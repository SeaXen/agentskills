**Don't touch the hero or the video yet. Instrument the gap between step 71% and day-30 3% first — that's where the real problem lives, not on the page.**

## Why 71%→3% kills the marketing theory

71% completion means page teaches fine. Already cold-run, clean, fast. Marketing's fix (hero, video) moves attention and bounce at page entry — top of funnel. Flat 3% for a full year, unmoved by an already-good page, means bottleneck sits downstream of the tutorial, not on it. Rewriting entry copy attacks a stage that isn't broken.

Two different metrics got merged into one problem:
- **Completion (71%)** = tutorial UX quality.
- **Activation (3%, 30-day)** = real product adoption.

No causal link between them once completion is already this high. Moving the first won't move the second.

## Likely real gap (rank order, needs data to confirm)

1. **Tutorial success is fake success.** Sandbox flag, toy example, canned SDK key — reader never touches own app, own environment, own real flag. "It worked" and "I now use this at work" are different actions, and nothing bridges them.
2. **No next step after the last screen.** Getting-started ends at "you did it," not at "here's how this becomes real in your codebase." Reader closes tab with zero prompt to return.
3. **No re-engagement between session 1 and day 30.** No email, no in-app nudge, nothing pulling a stalled user back before the 30-day window closes.
4. **Traffic quality.** If docs SEO or a launch pushed a lot of curious-but-not-buying traffic (students, competitor scouting, researchers), high completion + low activation is exactly the signature — they can finish a 6-minute tutorial with zero intent to adopt.

## Action plan

1. **Today: instrument the funnel between "finish tutorial" and "30-day activation" into real micro-steps** — installs SDK in own repo, creates real API key, creates a flag outside the tutorial, evaluates that flag from real code, returns for a second session, invites a teammate. Find which step the 71% actually collapses at. Without this, any redesign is a guess.
2. **This week: talk to 8-10 people who finished the tutorial but never activated.** Ask what they did right after finishing and what stopped them. Also talk to 3-5 who did activate — what they did differently in the first hour. Cheap, fast, tells you which hypothesis above is real.
3. **In parallel, ship one small, reversible change** — not a redesign. Replace the generic "next steps" footer with one CTA tied to whichever hypothesis looks strongest (e.g. "add this flag to your own repo now," pre-filled with their real key). Measure the specific micro-metric from step 1, not full 30-day activation — that's too slow to iterate against.
4. **Once data names the actual drop point, decide what marketing's video is for.** If the gap is "tutorial success doesn't bridge to real usage," a video helps — but placed *after* the "you did it" moment, showing real integration, not on the entry hero.
5. **Let marketing run hero/video anyway if they want, but track it against signup rate or bounce, not activation.** It's a legitimate lever for a different metric. Scoring it against the 3% number will produce a false win or false failure either way.

Time cost: instrumentation + interviews ≈ 1 week before any redesign decision. Full hero/video rewrite without this is weeks of design and dev work aimed at a stage of the funnel that isn't the problem.

**Next: pull current analytics/event tracking for the getting-started page and check whether any post-tutorial or SDK-install event already exists to instrument step 1 against.**