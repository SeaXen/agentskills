# How We Cut Webhook Retry Storms by 90% — Video Script

## Before the script: what shaped it

**From your message, taken as given:** source = the 2,100-word post (7 sections, as listed); runtime ≈ 3 min; publish by the 24th, tied to the retry API's GA; team of 2; no diagram/motion-graphics skill; no video editor.

**Not stated, so marked and assumed rather than guessed** — confirm before recording:

- Viewer / decision the video should produce: `[unconfirmed]` — assumed *"an engineer running webhooks through Loomcast understands why storms happened and trusts the new default enough not to build their own workaround."` Change the CTA in beat 6 if the real goal is signup/evaluation instead.
- Audience: `[unconfirmed]` — assumed mixed existing-user + evaluator, so B2B redaction rules apply (see Recording brief).
- Face on camera vs. voiceover-only: assumed **voiceover-only** — it's the only option that doesn't need a camera setup, a second take format, or an editor to cut around a talking head.
- Exact figures behind "90%" (the cause mechanism's parameters, the benchmark's before/after numbers, whether the new behavior is default-on or opt-in): not given to me at all — I did not invent any of these. They're bracketed `[unconfirmed]` in the beats below and must come from the post itself before you shoot.

**Shape, decided out loud, not by default:**

Efficiency order is error/fix > changelog clip > short-form > feature walkthrough > concept explainer > build-along > deep dive. Your answers delete most of it:

- **No diagram/motion-graphics skill deletes the concept explainer** — which is what this content naturally wants to be (a mental model of a queueing mechanism), but the skill this needs is exactly the one you don't have. Naming that now instead of writing a script you can't shoot.
- **No video editor and a 6-day runway delete the feature walkthrough** (needs a demo environment built to survive a clean take — a week of work) **and the deep dive** (a quarter).
- **No one to keep a companion repo green deletes the build-along** — not that this content wanted one anyway.
- **The hard GA date promotes the changelog clip.**

What's left: **changelog/release clip**, structured with the error/fix shape's cause-then-fix depth rule, because "we shipped a change" alone doesn't earn 3 minutes — the before/after storm and the 90% number do. This is a deliberate stretch past the changelog clip's usual 30–90s band; the cut plan below is what protects you if that stretch turns out to be too much on the day.

Every visual below is a screen recording or a static image (charts built in a spreadsheet, screenshotted) — nothing that requires drawing or animation skill. The one visual that could tempt you into "motion graphics" (the token bucket) is specced as a plain on-screen explanation instead, with a two-slide fallback that needs zero animation ability. Assembly is straight cuts + voiceover, buildable in Loom, ScreenStudio, or QuickTime + iMovie's basic trim — none of that requires a video editor as a role, only trimming clips end to end.

---

## Header

```
Title (working):    How We Cut Webhook Retry Storms by 90%
Promise:            For an engineer running webhooks through Loomcast, this video shows the
                     old queue's retry storm, and the token-bucket fix (going GA Sept 24)
                     that stops it.
Shape:               changelog/release clip, with an error/fix cause-then-fix arc
Audience:            existing user + evaluator [unconfirmed — confirm before recording]
Surface:             loomcast.com, live by the 24th (also upload to a video platform for
                     the chapter list and search reach, if you have one)
Target runtime:      2:45–3:00
Estimated runtime:   ~2:20–2:40 (see Runtime, below — recalculate with your real speaking rate)
Recorder:            [unconfirmed — either of the two of you; pick whoever's machine has
                     the dashboards/logs already accessible]
Speaking rate:       assumed 150 wpm — replace with a timed 200-word read before you lock
                     the cut plan; do not guess this number
Companion:           the original blog post; the new retry API's docs page
Off-limits:          customer webhook URLs, tenant IDs, internal hostnames, anything in a
                     log/dashboard screenshot that isn't already public
```

---

## Beats

| # | Visual | On-screen action | Narration | Starting state | Est. s | Core/cut |
|---|---|---|---|---|---|---|
| 1 | Split screen: left = old-queue dashboard during a real incident, retry volume spiking; right = same failure today, flat line | Cut left→right on "same failure today" | "This is a retry storm on Loomcast's old queue — one outage, and every failed delivery retries in the same second. Here's the same failure today, with retries capped in real time. We cut storm volume by 90%, and this ships as the default on September 24th. If you send webhooks through Loomcast, this is three minutes." | Two pre-exported chart/dashboard clips or images, cued and full-screen | 23 | core |
| 2 | Log viewer, real or reproduced retry log from an outage | Highlight the timestamp column showing many retries at the same second, then scroll to the line marking the jitter change | "Here's why storms happen: every client backs off on the same fixed schedule. When Loomcast recovers from an outage, every failed delivery retries in the same window — that's the storm, not the outage itself. **[cuttable →]** We tried random jitter first — it thinned the spike, but nothing tracked how much retry traffic a receiver was actually getting, so it still spiked." | Log file open, two lines pre-marked (sync-retry timestamps, jitter commit) | 26 | core (first sentence) / cut (jitter clause) |
| — | **Segment: The fix** | | | | | |
| 3 | Plain on-screen text/config: a rate-limit field name and value, no diagram. *(If you want a visual metaphor instead: two Keynote/Slides frames of a bar filling and draining, joined with the app's built-in "Magic Move"/morph transition — a template feature, not hand-drawn animation. Default to the config-field version; it needs nothing built.)* | Highlight the rate-limit field | "The fix caps retries with a token bucket: each receiver gets a budget of retry attempts per second. Deliveries draw from that budget — once it's empty, the retry waits instead of firing immediately. The queue can't send out more retries than a receiver can plausibly handle, storm or no storm." `[unconfirmed — confirm this matches the post's actual mechanism: is the budget per receiver, per endpoint, or per tenant? What's the refill rate?]` | Config/docs snippet open, field in view | 24 | core |
| — | **Segment: The proof** | | | | | |
| 4 | Static before/after bar chart, built in a spreadsheet, screenshotted | Zoom to the "−90%" delta | "In production, that cut retry-storm volume by 90% during the incidents we measured `[unconfirmed — pull the actual comparison from the Benchmarks section: peak retries per second, or how long a storm used to take to drain, before vs. after]`. Same failure, a fraction of the traffic." | Chart image loaded full-screen | 25 | core — never cut; this is the number the whole video is for |
| — | **Segment: What changes on the 24th** | | | | | |
| 5 | New retry API docs page | Highlight the version note / config field | "This ships as the default retry behavior when the new retry API goes GA on September 24th. If you're already on Loomcast, there's nothing to turn on. **[cuttable →]** If you're evaluating us, this is the queue your webhooks would run on starting today." `[unconfirmed — confirm default-on vs. opt-in before recording this line; if it's opt-in, replace "nothing to turn on" with the one setting to flip]` | Docs page loaded, relevant field visible, browser zoomed | 25 | core (first two sentences) / cut (evaluator line) |
| 6 | Return to the before/after split from beat 1, now labeled "Before / After Sept 24" | Hold on final frame with post link and docs link as on-screen text | "The full write-up and the benchmark numbers are linked below. If retry storms have hit your integration, September 24th is when they stop." | Same chart asset, text card overlay added | 15 | cuttable — fold "linked below" into the end of beat 5 if you drop this |

---

## Chapters

```
00:00 The retry storm on the old queue
00:23 Why retries synchronize into a storm
00:49 The token bucket fix
01:21 The 90% result
01:46 What changes on September 24th
```

Five chapters, first at `00:00`, ascending, each segment well over the platform's 10-second floor. If "your site" means an embedded player without chapter support, keep this list anyway — it doubles as the on-page table of contents and the description outline.

---

## Cut plan

```
If long by ~15s:   drop beat 6; fold "full write-up linked below" into the end of beat 5.
If long by ~30s:   also drop the jitter clause in beat 2 — keep only the synchronized-
                    retry cause, cut straight to "The fix caps retries with a token bucket."
If long by ~40s:   also drop the evaluator sentence in beat 5.
Never cut:         beat 1 (opening — problem, result, prerequisite, runtime, all in 23s),
                    beat 3 (the mechanism — this is the argument),
                    beat 4 (the 90% number — this is the proof the whole video promises).
```

Cutting everything marked cuttable removes ~50s and still delivers the full promise: storm → cause → fix → proof → GA date.

---

## Recording brief

**Starting states**

| Beat | Enter this state with | Verified |
|---|---|---|
| 1 | Two chart/dashboard clips exported and cued, played back to back | `[ ]` |
| 2 | Log excerpt file open, two lines pre-marked | `[ ]` |
| 3 | Config/docs snippet open, rate-limit field in frame | `[ ]` |
| 4 | Before/after chart image, full-screen | `[ ]` |
| 5 | Docs page loaded, relevant field visible | `[ ]` |
| 6 | Chart asset + text-card overlay ready | `[ ]` |

Each beat is one static asset or one short clip — that's deliberate. It means re-shooting beat 4 never touches beat 1, and it means assembly is straight concatenation, which any basic screen-recording tool (Loom, ScreenStudio, QuickTime + iMovie's trim) can do without a dedicated editor.

**Machine hygiene**

- Notifications off at the OS level before recording any dashboard or log screen.
- Redact or fake any real customer webhook URL, tenant ID, or internal hostname that shows up in a real incident's logs or dashboard — pull from a staging incident or a sanitized replay if the real one has customer data in it.
- Terminal/log viewer at 24pt+, docs page zoomed so text reads at phone size.
- Record voiceover and screen separately if that's easier for two people — the narration column above stands alone in audio, so either order works.

**Off-limits**

- Customer names, tenant IDs, internal hostnames, ticket numbers.
- Anything from the new retry API that isn't true yet — don't publish before the 24th even if you record earlier. If GA slips, beat 5 and beat 1's "ships … on September 24th" both need a re-record, not a mute-and-patch.

**Take plan**

- Shoot beat by beat, not as one continuous pass — with no editor, straight cuts between clean individual takes is far less work than cutting mistakes out of one long recording.
- Say the beat number out loud before each take so files sort themselves.
- Record 3–5 seconds of silence once, to patch any gap in the edit.

**Publication checks**

1. Captions generated and corrected against the narration column above — required for prerecorded audio under WCAG Level A.
2. Every link named in narration (the post, the docs page) is actually in the description.
3. Played with the screen off, the video still makes sense (re-run the audio-only pass on the real recording, not just this script).
4. No customer identifier visible in any frame — scrub the dashboard and log beats at 4x speed specifically.

---

## Runtime

Narration ≈ 265 words (all beats, cuttable clauses included) ÷ 150 wpm *(placeholder — replace with your own measured rate: time yourself reading 200 words aloud once)* ≈ 1:46 of speech, + roughly 45–50s of dead time across six beats (chart holds, zooms, page loads) ≈ **2:30–2:40 estimated**, against a 2:45–3:00 target. That lands inside the target with 10–20s of slack — recompute once you have a real speaking-rate number; don't lock the cut plan against the 150 wpm placeholder.

---

## Before you shoot: outstanding gaps

The script is structurally complete but not yet fully shootable — three `[unconfirmed]` items above need real numbers from the post before beat 3 and beat 4 are said on camera as fact:

1. The exact token-bucket mechanism (per-receiver? refill rate?) — from "The token bucket fix" section.
2. The actual before/after benchmark comparison behind "90%" — from "Benchmarks."
3. Whether the new behavior is default-on or opt-in at GA — this changes one sentence in beat 5.

Nothing else is inferred beyond what your message stated.