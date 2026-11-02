⚠️ Before the brief: the plan as described trips a named failure mode in devrel-hiring — **"unpaid spec-work audition."** Two candidates already have public blogs and conference talks; the skill's rule is explicit: *"never request unpaid spec work when a public portfolio already exists — offer a paid live working session instead"* (quality gate #5), and *"if a live work sample was designed, it is scored on a fixed rubric and paid, never treated as free trial work"* (quality gate #8). "Everyone in this industry does this" is the exact rationalization the skill's failure-mode table exists to catch, not a defense of it.

So the three candidates don't get the identical treatment you described. Here's the differentiated design, plus the rubric.

**Assumptions I made (flag if wrong):** growth-stage/Series B → sub-role is a product-focused Developer Advocate (coding-heavy, tutorial-writing, API-facing), not a pure outreach role. Funding driver is developer adoption or product input — you didn't state it; pick one, since it decides what the exercise is scored on. Comp stance / stipend amount is yours to set; I've left it as a placeholder.

---

## 1. Segment the three candidates — don't run one uniform stage

| Candidate | Existing evidence | What to run |
|---|---|---|
| A & B (public blog + talks) | Portfolio evaluation *is* the evidence — score it first (six-signal table below) before asking for anything new | If the portfolio alone answers "can they teach our API," skip a fresh exercise entirely. If you still need API-specific evidence, replace the 6-8h asset with a **paid, ~90-minute live session**: screen-share, walk them through an unfamiliar endpoint, have them narrate it as if teaching a developer. Pay a flat session fee. |
| C (career-changer, no public work) | None to evaluate | Run the tutorial + Loom exercise as designed — it's the right instrument when there's no shipped work to judge instead. **Paid**, scored on the fixed rubric below. |

Reasoning, per the skill: *"place the portfolio evaluation before any new work is requested — judging existing public work first often removes the need for a content or coding take-home entirely."* Commissioning fresh unpaid content from A and B when they've already shipped equivalent public work isn't a fair test of skill — it's free labor for a company that happens to also be their prospective employer, which is the specific pattern the industry gets criticized for.

---

## 2. The brief (for Candidate C, and offered to A/B if they'd rather do fresh work than walk through an existing piece)

> **Quilt Metrics — Developer Advocate take-home**
>
> **Task:** Write a ~1,200-word tutorial that shows a developer how to instrument [pick one real, scoped flow — e.g. "emit usage events from a sample billing integration and read them back via the Usage API"], using a sandbox API key we'll provide. Record a 5-minute Loom walking through the tutorial as if presenting it to a developer who's never used Quilt Metrics — not to a judge.
>
> **Deliverable must:**
> - Run against the real sandbox API — no fabricated responses.
> - Name at least one real trade-off or limitation of the approach you chose (a rate limit, an eventual-consistency lag, a case where a different endpoint would fit better).
> - Read like documentation a developer would trust, not marketing copy.
>
> **Logistics:**
> - Time-boxed at 6-8 hours. Stop at 8 hours even if unfinished — send us what you have; we score the work, not your stamina.
> - Deadline: [date, 5+ business days out].
> - **Compensation: $[stipend] flat fee, paid on submission regardless of outcome.** This is paid work, not an audition.
> - You retain rights to the tutorial. We won't publish it without a separate agreement.
> - Questions about the API during the exercise go to [contact] — asking for help is not penalized; we're evaluating how you'd actually work here.

---

## 3. Scoring rubric

Every interviewer scores independently with a written evidence note per row, before any debrief — the debrief calibrates interpretation, it never originates a score (per the skill's scoring mechanics, which cites this as a general structured-interview finding, not DevRel-specific).

| Competency | 0 | 1 | 2 | 3 | Weight |
|---|---|---|---|---|---|
| Technical accuracy | Code doesn't run / API misused | Runs with errors uncaught | Runs correctly, matches current API | Runs correctly + anticipates a real edge case | 3 |
| Trade-off honesty (developer-voice signal) | No trade-off named | Trade-off named but generic/hedged | Names a real, specific trade-off | Trade-off shapes a concrete recommendation | 2 |
| Structure & pedagogy (teaching-artefact signal) | No clear progression | Progression present, gaps a novice would trip on | Clean checkpoints, followable by a target-persona novice | Anticipates and pre-empts the likely stuck-point | 2 |
| Developer voice vs. marketing voice | Reads as promotional | Mostly neutral, some sales language | Consistently developer-to-developer | Voice a developer would explicitly trust more than our own docs | 2 |
| Loom communication | Reads a script, no eye on the audience | Clear but flat | Clear, paced, handles the material at ease | Handles an unscripted moment (a slip, a tangent) well | 1 |
| Root-cause instinct (bonus, not required) | — | — | Surfaces an actual API/docs gap while building | Gap is specific enough to file as a real ticket | +1 |

Combine mechanically against these weights — no holistic gut score. Total possible: 10 (11 with bonus). Freeze this rubric for the quarter so any future Developer Advocate hire is scored against the same bar.

For A and B, fold this same rubric into the **six-signal portfolio score** instead of running it fresh: signal 1 (public writing) and signal 5 (teaching artefact) come from their existing blog; signal 3 (code in public) and signal 6 (developer-voice artefact) come from their existing repos/talks if present. Score 0-3 per signal (0 absent, 1 claimed-unevidenced, 2 evidenced, 3 evidenced-with-outcome); weight signals 3+6 higher given this is a product-focused seat. Name negative signals explicitly if you see them — follower count with no substance, content that talks about the candidate rather than the developers served, metrics exaggerated or dismissed when asked — rather than only listing gaps.