# Webhooks Tutorial — Revision Plan

**Audit mode**, per `developer-tutorial` skill. One flag before the plan: your three notes — "a bit long," "tone is dry," "step 4 is probably where people get lost," "needs screenshots" — are the exact shape of diagnosis this skill's own audit playbook calls out as a bad hand-back, almost line for line. Reasons that matter for what you do this week:

- "Probably where people get lost" is a guess from reading, not an observation. In the one worked example this skill ships, an author guessed step 4 too — the real defect was there, but two *other* things they didn't guess (a hidden prerequisite at step 2, a wrong file reference at step 6) blocked just as many learners, and got fixed only because someone watched a cold run instead of rereading.
- In that same example, "add screenshots" and "it's a bit long" turned out to be non-issues — neither test runner hesitated on either. Spending writer-hours on them this week is a plausible way to burn the budget on the wrong fix.
- 11% reaching the last page tells you *that* the page loses people. It says nothing about *where* — reach-the-last-page is a single completion event, not a per-step one.

You said no time for user testing. Below assumes that means no formal usability study — fair. But the skill's actual verification unit is **one person, 30–45 minutes, narrating out loud while someone silently takes notes**. That's not a study, it's a coffee with a colleague. I'm giving you two tracks: what the writer can safely start today without it, and a cheap slot for it that de-risks the rest.

---

## Track A — Run this in parallel, costs ~1 hour total

Pull one backend engineer who has **not** seen this tutorial and matches its audience (used the product, never done webhooks with it). Hand them the URL and nothing else.

1. They narrate; you stay silent and take notes — don't answer questions, that erases the data point.
2. Timestamp the start of each step.
3. Log every event as one of: **defect** (command failed / output didn't match), **hidden prerequisite** (needed something "Before you begin" never mentioned), **concept gap** (did the step, can't say what it did), **friction** (hesitation, re-read, scroll-back). Anything they "figured out" counts as a defect, not a win.
4. Ten minutes after they finish, ask them to verify a signature on a *different* payload/event type you never walked them through, with only the reference docs open. Whether they can is the real test of whether step 4 teaches or just gets copy-pasted.

Feed the result into the table below — it will confirm, redirect, or add rows. Do this Monday/Tuesday so the writer isn't rewriting the wrong step by Thursday.

---

## Track B — Structural fixes the writer can start today, no cold run needed

These are checkable straight from the page against the tutorial's own template rules, independent of where the 89% actually drop off.

| # | Check | Why it matters | Action |
|---|---|---|---|
| 1 | **Objective statement.** Does the page open with a testable sentence — "receive a webhook, verify its signature, and reject a forged one" — or something like "understand webhooks"? | Untestable objectives are how tutorials drift into feature tours; a weak one also makes it impossible to write a real transfer-test later. | If missing or vague, write it first, verb-first, before touching any step content. |
| 2 | **Step count and length.** Count primary steps and substeps; time a straight read-and-type-along. | Template ceiling is 7 primary steps / 4 substeps each, 15–60 minutes end to end — sourced limits, not house style. Over 60 minutes is a split, not a trim. | If it's genuinely long because it's doing two things, split at a checkpoint into two tutorials with a stated order — don't just cut prose. If it's long because of unrelated explanation paragraphs, cut those (see #5). |
| 3 | **Step 4 concept count.** Read step 4 only: does it introduce the signature header, the secret, *and* the digest comparison all in one block? | This is the tutorial's own worked example, almost verbatim: "step introduces the header, the secret and the comparison at once" is a named concept-gap pattern, not a vague complexity problem. | Split into 4a (read/parse the signature header) and 4b (compute and compare the digest), each with its own expected output. Do this regardless of Track A's result — it's checkable from the text alone. |
| 4 | **Every checkpoint has three parts.** For each checkpoint: a command, the *exact* expected output (not "should look something like"), a recovery line. | A checkpoint without exact output or a recovery route is the #1 named cause of "double-check the previous steps" abandonment. | Rewrite any checkpoint missing a part. Recovery lines must state the failing condition ("if the secret isn't set, this returns 401"), never a verdict ("you should have set the secret first"). |
| 5 | **"Tone is dry" — locate it, don't guess at it.** Scan for: passive voice, unexplained flags, explanation paragraphs sitting on the critical path instead of linked out. | The skill's fix for dry tone isn't "add personality," it's mechanical: first-person-plural for the journey ("First, do x. Now, do y."), imperative for actions, one sentence of explanation max before linking out. | Apply the humanizer pass to prose only, never to code blocks, after the structural edits — tone fixes on top of a broken structure just make the broken structure sound friendlier. |
| 6 | **File/insertion-point naming.** Any step that says "add this to your handler" without naming the file. | Named as a real friction case in this skill's examples — learners scroll back to guess. | Name the file and insertion point on every step that edits existing code. |
| 7 | **Before you begin.** Two lists present — software with a check command, knowledge with a link each (HMAC/signing concepts assumed or taught)? | Anything discovered mid-tutorial instead of here is what Track A's hidden-prerequisite check will catch — check what's checkable now regardless. | Fill gaps now; let Track A confirm nothing's still missing. |

## Hold until Track A reports back

| Item | Why it waits |
|---|---|
| Whether step 4 (vs. some other step) is the *dominant* blocker | Your read-through and the skill's own worked example both guessed step 4 first — and in that example, a hidden prerequisite two steps earlier blocked just as many people. Don't let step-4 surgery absorb the whole week if the real leak is upstream. |
| Screenshots | Flagged in this skill's reference material as a common false lead — neither test runner in the source example hesitated for lack of one. Add them only if Track A's runner actually pauses looking for a visual reference. |
| Any further paragraph trims beyond #5/#2 | "A bit long" without a located stall point is exactly the unfalsifiable note this process replaces. |

---

## Day-by-day, this week

- **Mon/Tue:** Run Track A (1 hr) while writer starts Track B items #1, #2, #4, #6, #7 — none depend on the cold-run result.
- **Wed:** Writer rewrites step 4 per #3, informed by whatever Track A actually logged there (defect vs. concept gap changes the fix — a defect means the documented output is wrong and needs a real rerun; a concept gap means split the step, content otherwise fine).
- **Thu:** Humanizer pass on prose (#5). Re-verify every code block against a real run — an unrun expected-output block is worse than none.
- **Fri:** If Track A flagged a second blocked point, patch it. Ship. Add the two events below so the *next* revision doesn't start from a guess either.

## Instrument now, cheaply, so this doesn't repeat

- One completion event at the final checkpoint (you have this — it's your 11%).
- One event per checkpoint/step anchor, if the page has them. This alone turns "89% don't finish" into "62% drop between step 3 and step 4," which is the number that would have skipped this whole discussion.
- Copy-button clicks per code block, if you have them wired — blocks nobody copies are usually blocks nobody reaches, a second, near-free localizer.