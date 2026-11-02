No — this narration is not ready to record as an audio description (AD) track. It's written as informal presenter voice-over, and every line relies on the listener already seeing the screen. AD exists specifically for the audience that can't do that, so this script currently defeats its own purpose.

**Verdict: ❌ not ready.** Rewrite required before recording.

## Line-by-line problems

| # | Line | Problem |
|---|------|---------|
| 1 | "Okay so as you can see here we've got the handler." | "as you can see" and "here" both presuppose sight. No indication *which* handler, in what file, doing what. |
| 2 | "Now I'll just change this to that." | "this"/"that" carry zero information without vision. The actual code change (before → after) is completely absent. |
| 3 | "Click here, and then over here." | Pure deixis, twice, with no named UI element, label, or screen location. Unusable. |
| 4 | "And there we go, it works now." | Doesn't say what result appeared — a passing test, a 200 response, a green checkmark, log output. "It works" describes nothing visible. |
| 5 | "This function does a bunch of stuff under the hood." | Actively withholds the one thing AD is supposed to supply: what's on screen. "A bunch of stuff" is the opposite of a description. |

## What AD needs instead

WCAG 1.2.5 (Audio Description, prerecorded) requires the description to convey visual information the primary audio doesn't already state — concretely and without relying on prior sight of the screen. Replace deictic filler with named, specific content:

1. "The webhook handler function, `HandleWebhook`, is open in the editor."
2. "The signature check is changed from a plain string comparison, `sig == expected`, to a constant-time comparison using `hmac.Equal`."
3. "Clicking the Run Tests button in the toolbar, then the Terminal tab to view output."
4. "The terminal shows three tests passing, marked with green checkmarks."
5. "The function reads the request body, computes an HMAC-SHA256 digest using the shared secret, and compares it to the signature header."

(Exact wording should match what's actually on screen in the locked edit — these are placeholders showing the required level of specificity, not final copy.)

## One process risk worth flagging to legal/production

Recording AD only after the edit is locked is common, but it assumes the locked cut leaves enough silent gaps to fit real descriptions (line 3 alone needs roughly 3x the runtime of "Click here, and then over here."). If the primary narration talks over every action with no pauses, standard (non-extended) AD won't fit, and you'd be forced into extended AD — which pauses the video, changing its runtime. Worth a quick pacing check against the locked cut before the AD recording session is scheduled, not after.