# Demo Script Recovery Plan — Fix Before Q1

## Root cause

The deck failed because it had **one owner and zero triggers**. It was built once, by one person, as a static artifact (fixed screenshots baked into slides, a linear script assuming today's UI stays today's UI forever). When that person left, nothing else changed — no review cadence, no link between "product ships a change" and "someone updates the deck," no owner to notice the drift. It didn't break suddenly; it went stale silently for eight months until two reps hit the gap live.

Patching the current deck fixes this call. It doesn't fix the next one. Below is both: a rebuilt script structure that survives product changes better, and a process that makes staleness visible before a rep finds out on a call.

---

## Part 1 — Governance model (prevents recurrence)

| Element | Requirement |
|---|---|
| **Owner (DRI)** | One named person, not "sales enablement" as a team. Their name is on the doc header. If they leave, reassignment is a same-week task, not a gap. |
| **Trigger for review** | Tie the deck to your release process, not the calendar. Whoever owns "what shipped this sprint" (PM or eng lead) flags UI/flow changes; enablement owner updates the affected scene only — not a wait until Q3. Formalize into whatever process already ships change logs (PR template checkbox, release-notes ritual). |
| **Backstop cadence** | Even with a trigger in place, triggers get missed. Add a **monthly 30-minute dry run**: DRI or a rep walks the live script against the live product, screen by screen. This is the check that would have caught this deck at month 2, not month 8. |
| **Version + changelog** | Add a one-line changelog block at the top of the script (date, what changed, who changed it). Anyone opening it can tell in 5 seconds whether it's current. |
| **Kill switch for reps** | Every rep gets a single Slack channel or inbox to flag "this doesn't match anymore" the moment they see it live, mid-quarter, not saved for a retro. Route straight to the DRI. Two reps hit this same gap last week and had no formal way to report it before improvising — that's the actual process failure, independent of the deck itself. |

**Before Q1, assign the owner and the trigger.** Everything below is worth less if nobody's job is to keep it true in March.

---

## Part 2 — Rebuilt script structure

The old deck likely failed structurally, not just contentwise: a linear, screen-by-screen script means *any* single UI change breaks the whole sequence, and the rep has no graceful way back in. Rebuild around **workflows, not screens** — each workflow is a self-contained block a rep can execute independently, skip, or reorder live.

### Scene template (repeat per workflow — aim for 3-4 workflows total)

```
WORKFLOW [N]: [Name — tied to a buyer pain, not a feature name]
Maps to pain: [what discovery should have surfaced before this gets used]
Time: [X min]

Entry line (talk track):
  "[1-2 sentences bridging from discovery into this workflow]"

Steps:
  1. [Action] → [What the prospect should notice] → [Question to ask]
  2. [Action] → [What the prospect should notice] → [Question to ask]
  3. [Action] → [What the prospect should notice] → [Question to ask]

Interaction point:
  [A question planted mid-workflow, not saved for the end —
   "does this match how your team currently handles X?"]

If the screen doesn't match what's written here:
  [See Recovery Playbook below — do not read this scene word-for-word
   if step 2's screen has moved. Narrate the OUTCOME, not the click path.]

Proof point available: [metric / logo / quote, if one exists for this workflow]
```

**Why "outcome, not click path":** the thing that broke on the call wasn't the value story, it was a literal screen reference ("click the blue button top-right"). Script the *what and why* of each step in full sentences; keep the *exact UI path* (button names, menu locations) in a separate, clearly-labeled sidebar that's cheap to update without touching the narrative. When the UI moves, you edit one line in a sidebar instead of rewriting a scene.

### Opening and close (unchanged shape, still needed)

- **Opening (2 min):** context, agenda, confirm the goals for this specific call.
- **Discovery recap (3 min):** reflect back what you heard; confirms you're demoing the right 3-4 workflows, not all of them.
- **Close (5 min):** summarize value against their stated pain, propose next step with a date attached.

---

## Part 3 — Mid-call recovery playbook (fixes what actually happened last week)

Give reps this explicitly — it's the direct fix for "had to wing it":

1. **Don't defend or apologize at length.** One line: *"That's moved since I last had this queued up — let me show you where it actually lives now."* Then move on. A missed screen is not a credibility event; fumbling it live is.
2. **Fall back to the outcome, not the path.** If you can't find the exact click, say what the workflow accomplishes and why it matters to their stated pain — that's the part the script protects regardless of UI drift.
3. **Bank it, don't burn the call on it.** One line in the follow-up notes to the DRI's kill-switch channel: which scene, which screen, what changed. That closes the loop that failed last time — nobody reported it forward before it hit two reps in one week.
4. **Know which workflows are demo-safe vs. narrated-only.** The monthly dry run (Part 1) should tag each workflow green (verified this month) or yellow (unverified, narrate at a higher level, don't click live). Reps should be able to see this tag before they open the call.

---

## Part 4 — Q1 rollout checklist

| Step | Owner | Target |
|---|---|---|
| Assign DRI for the demo script | Sales enablement lead | This week |
| Full re-walk of current deck against live product; mark every stale scene | DRI + 1 top-performing AE | Week 1 |
| Rebuild flagged scenes into the workflow template above | DRI | Weeks 2-3 |
| Wire release-change trigger into existing PM/eng change-log process | DRI + PM | Week 3 |
| Set recurring monthly 30-min dry-run on the calendar | DRI | Week 3 |
| Stand up the rep-facing kill-switch channel | DRI | Week 3 |
| Test new script live with 2 reps (including the 2 who hit the gap) before wider rollout | DRI | Week 4 |
| Roll out to full AE team with the recovery playbook attached | Sales enablement lead | Before Q1 kickoff |

The two reps who hit the stale screen are your best test audience for the rebuild — they already know exactly where it broke.