## Script review: webhook-signing narration (5 lines, no beat table yet)

**Verdict: No — not ready to record, on two separate grounds.**

### 1. Every line is deictic — this fails the pass threshold before accessibility even enters the picture

Pass-threshold gate 3 requires: *"The audio-only read still teaches the thing — zero deictic sentences remain."* All five lines fail it:

| # | Line | Problem | Risk |
|---|------|---------|------|
| 1 | "Okay so as you can see here we've got the handler." | "As you can see here" — names nothing. Which handler? What language, what file? | High |
| 2 | "Now I'll just change this to that." | "This to that" carries zero information without the picture. | High |
| 3 | "Click here, and then over here." | Positional, not named. Breaks the moment the UI is redesigned, and means nothing off-screen. | High |
| 4 | "And there we go, it works now." | Asserts a conclusion instead of stating the evidence (what response, what status code, what changed). | High |
| 5 | "This function does a bunch of stuff under the hood." | The one sentence the viewer came for, replaced with nothing. | High |

Rewrites, keeping your originals for comparison rather than overwriting them:

| Original | Rewrite |
|---|---|
| "Okay so as you can see here we've got the handler." | "Here's the Express webhook handler — right now it trusts the request body completely." |
| "Now I'll just change this to that." | "I'm replacing the raw `req.body` read with `verify(rawBody, signature, secret)`." |
| "Click here, and then over here." | "Open Settings, then the Webhooks tab, and copy the signing secret." |
| "And there we go, it works now." | "The same forged request now returns 403 with `invalid_signature`." |
| "This function does a bunch of stuff under the hood." | "`verify()` recomputes the HMAC over the raw body and compares it in constant time." |

This isn't a style nitpick — every one of these is the skill's own canonical negative example for this exact rule, in this exact domain (webhook signature verification), which is a signal this pattern is common enough to be worth catching every time.

### 2. Legal's plan has the sequence backwards, not just the budget

You're treating audio description as a bolt-on: lock the edit, then record a separate description track over it. Two problems with that order, independent of the accessibility requirement itself:

- **The vague lines above give the description track nothing to anchor to.** "This to that," "here, then over here," "it works now" — an AD writer working from the locked video will have to reverse-engineer what the field, the button, and the result actually were, then narrate all of that in whatever silence exists in the original track. That's strictly more work than writing it once, correctly, now.
- **Standard audio description has to fit in existing pauses without re-timing the program audio.** If these five lines are the whole narration and none of them leave a scripted gap (per this skill's "hold the frame after a result" rule), there may not be room to insert descriptions after the fact without extending the runtime — which turns a standard AD pass into an *extended* AD pass: re-cutting, re-timing, effectively a second edit. That's the expensive path the skill flags directly: *"write the visual information into the main narration, then verify the audio alone still teaches the thing — doing it at script time is far cheaper than bolting a separate description track onto a finished recording."*

Fix the five lines to name what's on screen (as above), and the audio-only pass — required anyway, before recording — verifies whether a separate AD track is still needed at all. It usually shrinks to almost nothing once the narration stops depending on the picture. That also happens to be the same fix that makes your auto-generated captions usable, since deictic lines are exactly what breaks a caption track too.

### What's still missing to call this shootable

This is five narration lines, not a script. Before it clears the pass threshold you still need, per beat: visual, on-screen action, starting state, estimated seconds, and core/cuttable — plus chapter titles and a cut plan. None of that exists yet, so gates 2, 4, 5, and 6 aren't evaluable. Fix the deictic language first — it's the cheapest change and it's the one legal's accessibility ask is actually blocked on — then build out the beat table around it.