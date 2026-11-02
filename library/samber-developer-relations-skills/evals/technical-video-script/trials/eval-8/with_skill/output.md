## Reviewing the plan (not a script yet — that's finding #1)

You've booked the expensive, hard-to-reverse part (crew, rig, two days) before doing the cheap, high-leverage part (writing the beats). In the largest study of instructional-video engagement, producers rated pre-production as the phase with the most impact on outcome — a 4K sensor doesn't fix a script that doesn't exist yet. Here's what the plan as described gets wrong, graded by how likely it is to lose the viewer or the shoot day:

| Risk | Finding |
|---|---|
| 🔴 | **The payoff is at the end, not the opening.** "Type it all, then run it" means nothing works on screen until minute 3-4+. The platform measures retention at 30 seconds; a viewer who hasn't seen the result running by then is gone. Show the integration working *first*, then unpack how — not the reverse. |
| 🔴 | **One continuous take with no checkpoints.** If a typo lands at line 47, you retype from line 1 — nothing is re-enterable mid-take. Published screencast practice (egghead, Lindquist) explicitly rejects this: record in short takes, "a take can be as small as a single sentence," cut between them. Sixty live-typed lines as one take is the opposite of that, and it's the fastest way to burn two paid crew days on retakes of the same block. |
| 🔴 | **Typing lines that aren't the lesson.** Imports and boilerplate are exactly what the format says to pre-supply, paste, or snippet-expand — never type live. Somewhere in those 60 lines are maybe 3-5 lines that *are* the integration point; the rest is scaffolding the viewer doesn't need typed in front of them. |
| 🟠 | **"Never any dead air" removes the pause that makes output legible.** Silence after a result appears is a scripted beat, not a gap to fill — filling it with talk is called out as *the most common pacing defect in developer video*. Continuous narration over continuous typing also violates "narrate before, not during": say what a block does, then let the viewer read it. |
| 🟠 | **Studio lighting and a cinema rig are the lever that doesn't move this format.** In the same study, code screencasts sat in the *weaker* engagement bucket versus drawn/annotated tutorials, and the authors found studio production values changed nothing. The levers that do compensate — motion, zoom, annotation, a face cut in at deliberate moments — cost editing time, not camera gear. Right now the budget is pointed at the wrong line item. |
| 🟢 | Wanting continuous energy in delivery is fine — the same research found engagement rising with speaking rate. Just don't confuse "no dead air" with "no scripted pauses"; those are different things. |

## What's still unconfirmed

Nothing here has been decided, and the skill won't let me invent it:

- **Promise** — one sentence: for *which viewer*, this video shows *what specific thing* working?
- **Viewer** — an evaluator deciding whether to try Rowan, an existing user learning it, or a buyer-adjacent watcher?
- **Shape** — a launch usually has a hard date, which normally promotes a changelog clip or error/fix video and drops a full walkthrough. But if evaluators genuinely need to see it built before they'll try it, a **feature/product walkthrough** (not a raw type-along) is the better fit — outcome shown first, one path, no options tour. Which one applies depends on the date and whether this is a one-off launch moment or a compounding asset.
- **Runtime target** and **speaking rate** (measured, not guessed).
- **Companion repo** — is there one the viewer can clone, so the boilerplate can live there instead of on screen?
- **Off-limits** — any pre-release API surface, internal hostnames, or real keys that must not appear across two days of 4K footage.
- **Who edits the 4K footage after**, and on what timeline — this determines how much the shoot day can lean on B-roll/inserts (diagram, zoomed diff) versus a clean single pass.

## Redesign, once the shape is picked

1. **Open on the result.** First 30 seconds: the integration already running, the one-sentence problem it solves, prerequisites, runtime. Setup and imports move to *after* the payoff or into the companion repo — never before it.
2. **Cut the 60 lines into beats, one claim per beat**, each with its own starting state (a git ref, a file already open at a line) so any single beat can be re-shot alone. That's what actually protects two days of expensive crew time — not one perfect uninterrupted performance.
3. **Pre-supply everything that isn't the lesson.** Boilerplate and imports: pasted or already in the file, scrolled past with one sentence ("the client setup is in the starter repo, nothing here is Rowan-specific"). Type live only the handful of lines that are the actual integration call.
4. **Script the pauses.** After each meaningful output, a beat that's silence-then-one-sentence, not commentary filling the gap.
5. **Use the two days for coverage, not one continuous pass**: day one — environment rehearsal + segment-by-segment recording in short takes; day two — pickups, inserts (zoomed diff, a face cut-in explaining the "why," any diagram), room tone. That's where cinema-quality footage actually earns its keep — as B-roll and annotation material, not as a longer clean take.
6. **Write the cut list before recording** — decide now which beats fall out first if the edit runs long. A script with no cut list is how a 3-minute integration demo becomes 14 minutes because nobody could decide what to lose at edit time.

Once you give me the promise, the viewer, the launch date, and which 3-5 lines of that file are the actual lesson, I can turn this into the full beat table, chapter list, and recording brief — right now there's a shoot plan but no script, and the script is the artifact this format actually gets graded on.