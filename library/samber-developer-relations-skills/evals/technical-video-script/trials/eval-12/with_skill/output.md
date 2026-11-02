## Shape & context (decided before anything else, per the skill)

- **Shape:** Feature/product walkthrough — 5 min sits inside its 2-5 min band.
- **Audience:** Sales-led B2B, enterprise, buyer-adjacent. Per the skill's own audience rules for this shape: "a screen recording is a durable, forwardable document," and it will be "replayed in a procurement or security review where 'it depends' is not visible."

That audience framing is why two things need fixing *before* she presses record — not scripting choices, blockers.

### Blocker 1 — the version mismatch is a claim you can't keep

Staging runs v7.4-rc; you ship v7.3 next month. Anything v7.4-only that ends up on screen — a UI element, an error string, a behavior — becomes a claim a prospect can't reproduce the moment they actually get v7.3. That's a direct fail of this skill's pass-threshold #7: *every factual claim on screen must be one the recorder can reproduce on the recording machine* — and by extension, one the buyer can reproduce on theirs.

In order of preference:
1. **Pin the demo tenant to the real v7.3 build** (or the closest v7.3 RC) before she records. This removes the risk outright — do this if at all possible.
2. If that's not feasible in time, **feature-flag off every v7.4-only surface** on the current tenant so nothing shown exceeds what v7.3 will actually do.
3. Last resort only: keep v7.4-rc, but have her say on camera, verbatim, "You're watching Northgate Ledger v7.3" is *not* an option here unless it's true — if you can't pin the build, script an explicit disclaimer instead ("recorded on a pre-release build") and treat this as a throwaway video that gets re-shot against real v7.3 once it ships.

Whichever you pick: **hide the build/version string in the footer or About panel** before recording — an on-screen v7.4-rc tag will contradict whatever the narration claims.

### Blocker 2 — real pilot customer data is the bigger risk

The staging tenant has three real pilot customers' data loaded. A reconciliation-software walkthrough will show real account names, counterparties, balances, transaction records — on a video whose entire audience context is "this gets forwarded into someone else's procurement or security review." One pilot's real financial data landing in front of a different prospect evaluating whether to trust you with *their* financial data is a confidentiality problem independent of anything scripting can fix in the edit.

**Don't let her record against that tenant.** Hand her instead:
- A **separate seeded demo tenant**, on the corrected v7.3 (or flagged) build, loaded with synthetic data shaped like the pilots' use cases but containing no real names, tenant IDs, account numbers, or counterparties.
- A **one-command reset script** for that tenant, so she re-enters the same starting state between takes instead of carrying over whatever the last take left behind.
- Sign-off that the synthetic tenant was actually checked against the off-limits list below — ideally from whoever owns the pilot contracts (legal/customer success). This is the one item a later edit pass can't undo if it's missed.

## What to hand her before she records (recording brief)

**Starting state** — one command, run from a cold, freshly-booted machine (not one that already ran the demo, which hides warm caches/sessions):
`[seed command for the synthetic, v7.3-pinned tenant]` → reset before *every* take, not once at the start.
`[unconfirmed — you'll need to name the actual seed script; not something to guess]`

**Machine hygiene (her personal work laptop):**
- OS-level notifications, calendar, chat badges off — not minimized. A Slack/email popup naming a real customer is the single most common accidental disclosure.
- Clean browser profile for the recording: no personal bookmarks, no autofill history, no other signed-in tabs.
- Close every unrelated app/tab; no file tree, no inbox badge.
- Terminal ≥24pt, app UI readable at 20pt-equivalent zoom, high-contrast theme, window at 16:9.
- Shortened shell prompt — no path containing a customer, tenant, or internal hostname.
- Any staging credentials on screen: throwaway, rotated right after recording.
- Everything slow (login, first load, index rebuild) happens before "record" — dead air here kills the 30-second opening.

**Off-limits list for this specific shoot:**
- The three pilot customers' names, logos, tenant IDs, subdomains
- Any real account number, counterparty name, balance, transaction record
- Internal hostnames, ticket numbers, internal Slack/Jira
- Pricing
- Any v7.4-only feature, UI element, error string, or build number not present in v7.3
- Colleague names/avatars in any visible sidebar or notification

**The opening beat, inside its 30-second budget** — this is what retention lives or dies on:
1. Name the reconciliation problem in the viewer's words.
2. Show the result already working, not a promise of it.
3. State prerequisites (edition/plan, data assumptions) so the wrong viewer opts out at second 20, not minute 4.
4. State runtime and version aloud — `[verbatim]`: "You're watching Northgate Ledger v7.3" — the one sentence that keeps this video honest once v7.3 actually ships.

**Cut list** — decide now which beats are core vs. cuttable, so nobody improvises a cut at edit time.
`[unconfirmed — needs the actual reconciliation workflow she's demoing before this can be filled in]`

**Caption/description pack:**
- Auto-caption, then correct against narration for domain terms ("reconciliation," product nouns) — never re-transcribe.
- Description opening: the problem statement from beat 1 plus the promise.
- Prerequisites line, verbatim, from the opening beat.
- Every link named in narration (docs, signup, contact-sales) present in the description.

## How you'll know afterward whether it worked

Compare every number against Northgate's own past walkthrough-shape videos — never an outside benchmark.

- **Intro retention** (% still watching after 30s) grades the opening beat alone. Low here means one of the four opening jobs above didn't land — nothing else in the video is at fault.
- **Average % viewed**, vs. past 2-5 min walkthroughs: watched like a 90-second changelog clip means it's mis-shaped, not mis-titled.
- **Dip locations mapped to specific beats**: wherever the curve drops, read that beat's narration aloud with the screen off — it's a logic break, a density drop, or an unspeakable line.
- **Chapter usage**: heavy direct-entry into one chapter (skipping the open) means it's being used as reference, not watched start to finish — expected for a walkthrough, not itself a failure signal.
- **Companion-link clicks, and what they lead to**: for this audience the real signal isn't the click, it's whether a rep reports the video got attached to a deal or a security-review packet — ask sales directly, analytics won't surface that.
- **Takes per beat during recording**: log it live. 5+ takes on one beat is a starting-state defect (usually the seed script leaving the tenant inconsistent), not a performance problem — fix the seed script, don't re-shoot harder.
- **The KPI unique to this shoot**: once real v7.3 ships, re-verify every on-screen claim against the *actual running software*, not the recording — this is the "claims to re-verify before publish" step, and it's load-bearing here because you recorded against a release candidate. If anything shown doesn't match shipped v7.3, re-record that segment before this reaches a single prospect. This is exactly where the shape is riskiest: in a security review, where "it depends" isn't acceptable.

Treat a rewatched segment with suspicion either way — check sales/comment feedback before assuming a spike means "that landed"; it can just as easily mean "I had to watch that part three times."

Two `[unconfirmed]` items above still need your input before this brief is actually complete: the real seed/reset command for the synthetic tenant, and the specific reconciliation workflow the walkthrough proves. Everything else here is ready to hand her as-is.