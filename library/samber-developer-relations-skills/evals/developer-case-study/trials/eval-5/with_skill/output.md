**Verdict: not yet publishable — the limitations section fails gate 3.** Two of the three lines are roadmap plans, not costs, and the third isn't a limitation at all.

## Why

The skill this case study follows draws this exact line, worked as an example:

```
Bad:  We plan to consolidate the orchestration layer into Python, and chat
      approvals are on the roadmap for next quarter.
Good: The orchestration layer is Go; the team that maintains it writes Python
      everywhere else, so every change to it goes through the two people who
      know both. Approvals still happen outside the system — the integration
      only posts notifications — so an on-call engineer still opens a second
      tool to unblock a run.
```

The EM's lines 1 and 2 are that "Bad" example almost verbatim. A limitation is a cost the reader would inherit today, not a plan for later. Publication gate 3 requires "at least one limitation, specific enough that a reader could decide against you on it" — roadmap items don't clear that bar, because a reader can't decide anything from "we plan to fix it."

Item-by-item:

- **"Consolidate two orchestration languages next year"** — tells the reader what Meridian hopes happens, not what they run into now. The real limitation is the current split: two languages in production, presumably a smaller set of engineers who can touch both, maybe a review bottleneck or a slower incident response. That's the sentence worth publishing.
- **"Chat-based approvals on the roadmap for Q3"** — same shape. The limitation is how approvals work today without that integration: extra tool, manual step, whatever the actual friction is.
- **"Extend to the claims pipeline eventually"** — this isn't a limitation at all, it's forward-looking and positively framed. It belongs in section 8, "What is next" (~70 words, roadmap language is correct there), not in Challenges.

## What to send back to the EM

Not "give us different words for the same three sentences" — ask for the mechanism behind each roadmap item, same as the interview question ladder (rungs 8–9: "what it cost" / "what's still unsolved"):

> Two follow-ups before we can finish the challenges section — not more work, just the flip side of what you already told us:
>
> 1. On the two orchestration languages: today, with both running, how many engineers can actually modify each one? Has the split ever slowed down a change or an incident? Anything an on-call engineer has to work around because of it?
> 2. On approvals: walk me through what happens today without chat integration — which tool does someone open, and has that extra step ever cost real time you remember?
>
> Give me the "as of today" version of both and I can turn the section around same day.

That's a five-minute reply for someone who already lived it — not a new review cycle.

## Section template (drop-in once the answers come back)

```
[Two-orchestration-language limitation]: The [service] runs on [language A],
while the rest of the team writes [language B] — so changes to it go through
[the N people / the team] who know both. [Concrete consequence if given: an
incident, a delayed change, an onboarding cost].

[Approvals limitation]: Approvals still happen outside the pipeline today —
[describe the manual step/tool]. [Concrete consequence: who does it, how long
it typically adds, whether it's ever caused a delay worth naming].
```

Move the claims-pipeline line to section 8 instead:

> **What's next.** Meridian's team is also looking at consolidating their two orchestration languages next year, and extending the pipeline to claims eventually.

(Q3 chat-approvals item folds in here too if it turns out you can't get a "today" cost for it — see fallback below.)

## If the EM won't give more than roadmap language

The skill has an explicit fallback for this: the customer can strike the limitations section entirely, and the study still ships — weaker, but shippable, as long as that's an explicit call and not roadmap text quietly relabeled as cost. Worth naming to the EM directly rather than defaulting to it: "if there's genuinely no current-state cost you're willing to put in writing, we drop the section rather than publish roadmap items as limitations — your call." Don't make that substitution silently; it's the one thing this skill exists to prevent.

## Gate report (limitations section only — rest of the draft not reviewed here)

| Check | Status |
|---|---|
| 3. At least one limitation, specific enough a reader could decide against you | **Fail** — all three inputs are roadmap items |
| 7. Zero unsupported superlatives | N/A, not assessed here |

Approvals-signed and alternatives-in don't unblock this — gate 3 is independent of sign-off status. Once real "as of today" cost language comes back, re-run gate 3 (and 1, since these claims also need classifying as reported/measured) before shipping.