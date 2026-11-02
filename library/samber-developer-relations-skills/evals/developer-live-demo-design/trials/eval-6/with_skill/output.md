## Verdict

This plan has the same structural shape as this skill's own "done badly" example: no stated claim, every step chained to the previous step's live output, and rehearsal that measures nothing about Thursday's actual conditions. "Works every time" at your desk is not evidence it survives DataConf — it's evidence your desk network and warm caches are reliable.

## Findings, ranked by likelihood × how visibly it breaks

**1. No claim written down.**
Nothing says what the audience should believe afterward. Right now the plan proves five things at once (scaffolding works, deploy works, the dashboard is real, hot reload works, you have pricing) — a demo that shows five features proves none of them. Write the one sentence first; everything that doesn't serve it is a cut candidate. My guess is the claim is something like "one command takes you from zero to a live, editable deployment" — if so, step 5 doesn't serve it at all (see #5).

**2. Every step depends on the previous step's live output — the single riskiest pattern this skill flags.**
- Step 2 requires step 1 to have actually scaffolded a working project (`cd into what step 1 made`).
- Step 3 requires step 2's `deploy` to have succeeded and printed a real, resolvable URL.
- Step 4 requires step 3's deployment to still be live and re-deployable in the same state.

If `init` hangs, or `deploy` times out, or the preview URL is slow to resolve (DNS propagation is a named failure mode), you don't lose one segment — you lose the whole remaining demo, live, in front of the room. **Fix (design, not rehearsal):** give each step its own restore point — a pre-scaffolded project as a fallback if `init` misbehaves, a pre-deployed known-good URL you can jump to if `deploy` misbehaves — so a bad step is skippable, not fatal.

**3. No fidelity tier was chosen — it defaulted to tier 0 by omission.**
This is live typing against a live system with a real network call (`deploy` hitting whatever hosts the preview). Tier 0 is the tier with the most failure modes and the least mitigation in your plan. Unless the claim genuinely requires proving "this works live, right now" (audience-supplied input, a race, a real-time claim), a recorded screencast (tier 3) or scripted-input execution (tier 1) proves "one command scaffolds and deploys" just as well, with a fraction of the stage risk. Nothing in the plan suggests you deliberately paid the tier-0 cost — it looks like the default nobody chose against.

**4. `deploy`'s network dependency is unaddressed.**
Register entries this hits directly: venue Wi-Fi unusable or captive-portal, corporate VPN reconnect, and — worth taking seriously given the format — **the audience hitting your preview URL the moment it's on screen at a data conference.** There's no offline mode, no hotspot tested in the actual room, no local mock of whatever `deploy` calls out to.

**5. Step 5 ("show pricing page") is an unrelated fourth topic riding along on the technical claim.**
This is the exact "new UI we shipped last week" problem from this skill's worked bad example — a segment with no relationship to whatever the technical claim is. If the point is to close on pricing, that's a slide, not a live browser tab switch competing for your remaining seconds after a live deploy.

**6. Hot reload (step 4) doubles your exposure to the riskiest action in the demo.**
You're running the one operation with a network dependency (`deploy`) twice, back-to-back, with the second call depending on the first deployment's state still being intact. Whatever `deploy`'s solo failure rate is, you're now paying it twice in six minutes.

**7. Rehearsal doesn't clear this skill's pass threshold — not close.** Four desk runs satisfy none of these (baselines this skill sets, not industry standard, but they're the cheapest tests that catch each failure class):
- Not **cold**: your desk has warm caches, warm DNS, a warm deploy target. A cold run — fresh machine state, reset command only — is what would have caught a slow `init` or a cold-start deploy.
- Not on the **venue network**, and never run with the network **disconnected**. You have zero data on what happens when DataConf's Wi-Fi does any of the things conference Wi-Fi reliably does.
- Not verified at **venue resolution from the back row**. You don't know yet if the dashboard, the config file, or the terminal is readable past row five.
- No **drill of a failure and the switch to a fallback** — you have no fallback to switch to, so this can't exist yet.
- No **measured time** reported. Target is under half your 6 minutes (baseline, tune it) to leave room for one recovery plus questions. A live deploy with no fallback plan has no ceiling — if it hangs, it can eat the whole slot.

**8. No fallback assets, no reset command, no recovery lines.**
If any step misbehaves on stage, the only option in this plan is debugging live in front of the audience — the exact failure mode this skill's recovery plan exists to prevent.

**9. Public-safe surface, unaddressed.** Is the browser a dedicated demo profile, or your daily driver? A live dashboard and a live preview URL on a conference livestream/recording is exactly where a stray notification, an open personal tab, or a non-sandbox account becomes the story instead of your demo.

## What I'd fix before Thursday, in order

1. Write the claim. Use it to decide whether step 5 survives at all.
2. Give steps 1-4 independent restore points (pre-scaffolded project, pre-deployed URL) so a bad step is skippable, not fatal.
3. Decide the tier deliberately — if the claim doesn't require live-right-now proof, drop to tier 3 or 1 and keep tier 0 only for what actually needs it.
4. Record a fallback (screencast or recorded clip) for the deploy + hot-reload segments regardless of tier — that's your 20-second-switch when the network doesn't cooperate.
5. Re-rehearse: one cold run, one offline run, one at DataConf's actual resolution if you can get into the room early. Measure the time; don't estimate it.

Not a rehearsal problem — a design problem, same as this skill's own bad example. More reps at your desk won't touch any of the nine items above.