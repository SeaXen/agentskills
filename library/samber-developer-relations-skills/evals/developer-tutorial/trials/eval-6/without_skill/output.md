Revision plan below — hand as-is to the writer. Normal English throughout (this is the artifact itself, not chat).

---

# Webhooks Tutorial Revision Plan — docs.trelvin.io

**Goal:** lift completion rate above 11% within this revision cycle. **Timebox:** one week, no user testing — working from traffic data (4,000 visits/mo) and a structured author read-through.

## Diagnosis

- 89% of readers leave before the last page. That's a funnel problem, not a typo problem.
- Three independent signals point at Step 4 (signature verification) as the main leak: it's flagged as the hardest concept, tutorials typically lose readers at their first cryptography/security step, and it sits mid-tutorial where fatigue from length compounds the difficulty spike.
- Length and dry tone are drop-off multipliers, not root causes — they make readers less willing to push through the hard step once they hit it.
- Treat this as a hypothesis, not a confirmed cause (see "Cheap substitute for testing" below to start closing that gap for next cycle).

## Priority order (do in this order if the week gets compressed)

1. Step 4 rewrite — highest hypothesized impact, do first
2. Screenshots — cheap, high perceived-quality gain, do in parallel with #1
3. Tone pass — full-document, do after structure is settled
4. Length cut — do last, so you're trimming a fixed final draft, not a moving target

## 1. Step 4: Signature Verification

This step almost certainly fails for one or more of these reasons. Audit against each and fix what applies:

- **Missing "why."** Readers who don't understand *why* they're hashing a secret against a payload will copy-paste blind and give up at the first error. Add 2-3 sentences before the code: what a forged webhook looks like, why HMAC stops it.
- **Raw-body trap.** The #1 real-world bug in signature verification: framework JSON middleware parses the body before the signature check runs, so the re-serialized body no longer byte-matches what the sender signed. If the draft doesn't call this out explicitly, add a callout box — this single miss causes more support tickets than any other step.
- **No worked failure example.** Show a deliberately wrong signature and the exact error/behavior it produces. Readers debug by pattern-matching against what they see on screen.
- **Timing-safe comparison unexplained.** If the code uses a constant-time compare function, say why (`==` on strings leaks timing information) in one sentence — don't just drop the function name in.
- **One checkpoint, not zero.** End the step with a "you should now see X" checkpoint (per the tutorial-structure standard: checkpoints every 3-5 steps). If Step 4 currently ends on a wall of code, that's the fix.

**Writer deliverable for this section:** rewritten Step 4 with an explicit why-paragraph, a raw-body callout (if applicable), a worked failure case, and a checkpoint.

## 2. Screenshots

- Minimum: one screenshot per major checkpoint (webhook created in dashboard, test event received, signature check passing/failing in terminal). Target 4-6 total — more than that re-adds the length problem.
- Every screenshot needs a one-line caption stating what the reader should see, not what the screenshot is ("Your webhook endpoint now shows `Active`" — not "Screenshot of dashboard").
- Annotate (arrow/box) the one field or line that matters. Don't ship a bare unannotated screenshot of a full UI.
- Priority placement: Step 4 first (it's the trouble spot — a screenshot of a correct vs. failed signature check response is worth more here than anywhere else in the doc), then the final "it works" moment.

## 3. Tone Pass

- Dry tone reads as: passive voice, no second person, no acknowledgment of difficulty. Fix pattern:
  - Before: "The signature must be verified before the payload is processed."
  - After: "Verify the signature before you touch the payload — skip this and anyone can forge a webhook call to your endpoint."
- Add one line of encouragement right before Step 4 specifically ("This is the fiddly part — most of the tutorial is copy-paste, this step is the one to slow down on"). Naming the difficulty up front reduces abandonment more than hiding it.
- One tone pass, full document, after structure/screenshots are locked — don't tone-edit paragraphs you're about to cut.

## 4. Length Cut

- Cut in this order, not proportionally across the whole doc: (1) redundant preamble/history before Step 1, (2) any paragraph explaining something the code already shows, (3) optional/advanced asides — move these to a linked "Advanced" section instead of deleting, so power users don't lose them.
- Do not cut example code comments or the Step 4 explanation you just added — length and clarity are in tension there and clarity wins.
- Target: readable in under 10 minutes at normal reading speed. Time it by reading the final draft aloud.

## Cheap substitute for user testing

No time for a usability round this cycle, but skip it silently and the next revision is guessing again. Two low-effort additions:

- Add a "Was this step clear?" thumbs up/down at the bottom of each step (not just end of page). Takes a writer/dev under an hour to wire up, gives step-level signal instead of only page-level.
- If analytics allow it, add scroll-depth or per-heading tracking so next month's data shows *which* step readers stall on instead of inferring it from a read-through.

## Timeline (5 working days)

1. **Day 1:** Step 4 rewrite (why-paragraph, raw-body callout, failure example, checkpoint)
2. **Day 2:** Screenshots — capture, annotate, caption (all 4-6)
3. **Day 3:** Tone pass, full document
4. **Day 4:** Length cut against the locked draft
5. **Day 5:** Final read-aloud QA + ship the thumbs-up/down widget if time allows

## Definition of done

- Step 4 has: why-paragraph, raw-body callout (if applicable), failure example, checkpoint
- 4-6 annotated, captioned screenshots, one covering Step 4's success/failure states
- No passive-voice paragraph survives the tone pass unchanged
- Full read-aloud takes under 10 minutes
- Feedback widget live (or explicitly deferred with owner + date)

**Next check-in:** pull the completion-rate number 30 days post-publish and compare against the 11% baseline — that's the real verdict on this plan, not the read-through.