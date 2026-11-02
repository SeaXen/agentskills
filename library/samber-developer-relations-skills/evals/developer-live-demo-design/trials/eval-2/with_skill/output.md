## Which way you go

Neither. Take the two-thirds version: **record the exact demo, play it back, narrate it live.** That's Tier 3 on the fidelity ladder this skill uses (0 = live typing, 4 = static screenshots). Your co-founder has the right instinct — don't run this live — but screenshots undersell the one thing your product is actually selling.

**Why not live (Tier 0/1/2):** nine days and six hours of prep is the combination this skill flags as disqualifying for anything that depends on rehearsal to become safe. A fully local/offline live build (Tier 2) alone runs roughly a week of setup work in typical practice; you don't have that. Tier 0/1 need days of drilling to survive a real room. Cut them now, not on day 8.

**Why not your co-founder's screenshots (Tier 4):** your claim isn't "this tool produces a correct answer" — it's "watch it think": the tree drawing itself, then a click producing an instant, specific fix. That's *behaviour*, and static screenshots only show an *outcome*. Tier 4 quietly proves a weaker claim than the one you actually want the room to believe. Tier 3 proves the real claim at almost the same safety margin — a recording has zero execution risk, same as a screenshot — so between two tiers that are equally safe, take the one that proves more. That's the whole decision rule: keep only the tiers that prove the claim, then take the strongest of the survivors.

One more reason Tier 3 wins specifically for a query planner: the index suggestion your tool shows depends on the query planner's live stats. A recording locks in one known-good, honest run forever. Live, you're betting that Postgres's planner produces the same plan on stage that it did in rehearsal — a bet with no upside, since the audience can't tell the difference between "recorded" and "live" if you're honest about which one they're watching.

## Your six hours

1. **Pick and freeze the query (45 min).** One slow query with an obviously fixable index problem — dramatic before/after, not subtle. This is the single highest-leverage hour you have; a boring query sinks a perfect visualizer.
2. **Harden the recording environment (30 min).** Fresh browser/OS profile, light or high-contrast theme (dark dev-tool themes wash out under a projector), big fonts, no tokens/paths on screen, tabs closed. Same hygiene as if it were live — this recording is a public artifact forever.
3. **Legibility pass on the tree itself (30 min) — your unique risk.** A plan tree has small node labels; a demo of a *visualizer* lives or dies on whether row 30 can read a node. Zoom the app, increase whatever font/label size it exposes, check it on a projector or a TV from across the room, not on your laptop at arm's length.
4. **Record 3–5 clean takes (45 min).** Real product, real run, no speed-up, no edited suggestion. Pick the cleanest. This is "hardened," not "faked" — the moment you'd sweeten the output instead of the setup is the moment it stops being a live demo and starts being a lie, and audiences that ask "is that real?" deserve a "yes."
5. **Pull one frame for the standing fallback (15 min).** The single best frame — tree fully drawn, suggestion tooltip open — as an annotated screenshot. That's your Tier 4, one level down, sitting on the next slide, silent unless you need it.
6. **Write and rehearse narration + recovery line (20 min).**
   - Narration stays live over the recorded pixels — don't pre-record your voice too, or it just becomes a video and the room checks out.
   - Recovery line, for a mirroring/playback failure: *"Let's skip straight to the punchline — here's the exact same run, one static frame,"* then advance to the screenshot slide and keep talking.
7. **Pre-flight + rehearsal reps (remaining ~2h20).** Do Not Disturb, notifications off, deck on a USB key, video embedded in the deck (not a browser tab you have to alt-tab to). Rehearse the click-to-advance for the recording at least 3 times, timed, and once at the actual venue resolution/aspect ratio if you can get it. Get a colleague to sit near the front with the deck and the video file on their own laptop — the only failure this whole plan doesn't cover is your laptop dying, and that's a five-minute conversation to fix, not a design problem.

## The one thing not to compromise on

Whatever you do, don't let the "safe" choice quietly become the "weak" choice. Screenshots-and-talk is genuinely the safest thing in the room, but it also throws away the exact 20 seconds — the tree drawing, the click landing on a suggestion — that a keynote audience will actually remember. Six hours is enough to keep that moment and still be bulletproof. Spend them on the recording, not on talking yourself out of it.