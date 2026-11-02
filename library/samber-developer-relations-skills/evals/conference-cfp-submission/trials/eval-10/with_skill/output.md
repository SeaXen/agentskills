Two flags before the pack, both from the skill's own failure-mode table — noted, then overridden per your call, since you own the submission.

**Track.** "Platform & Infrastructure" matches this talk's content almost exactly; "The Future of Engineering" is a stretch fit picked for name recognition. That's the skill's documented "wrong track" failure mode — committees rank *within* a track, so a CI-infra talk competes against futurism pitches there instead of its natural peers. Submitting there anyway, per your instruction.

**Outline.** Pasting the abstract in again means the Outline field proves nothing a reviewer can check — no minute marks, no evidence the talk has a shape beyond its own pitch. That's the "copy-paste fields" failure mode. Done as asked below, but it's the single biggest thing dragging the self-review score down.

I also don't have the specific engineering changes behind the 40→6 drop (what actually moved the number), so I flagged that gap inline with a bracketed placeholder rather than inventing a technique — fill it in before you paste.

---

```markdown
# BuildScale Conf — proposal pack

## Constraints read from the brief

- Fields: Title (100 chars), Abstract (1,500 chars), Outline, Audience level, Track — no notes-to-reviewers, no benefit-to-community
- Tracks on offer: The Future of Engineering / Platform & Infrastructure / Culture & Craft
- Assumptions (not confirmed — check before submitting): format/slot length, deadline, per-speaker submission cap, review anonymity, AI-assistance policy

## Track

**The Future of Engineering**

Chosen for prestige rather than description match — flagged above. The content itself reads as "Platform & Infrastructure" (a specific, shipped infrastructure fix with before/after numbers), so if this gets no traction with reviewers, that's the first lever to pull.

## Title (48/100 chars)

**From a 40-Minute CI Queue to 6, Across 210 Repos**

Alternates:

1. 210 Repos, One CI Queue, and the 34-Minute Cut (46 chars)
2. The CI Queue That Cost Every Team 40 Minutes a Build, Fixed to 6 (64 chars)
3. Cutting CI Queue Wait From 40 Minutes to 6 Across 210 Repositories (66 chars)
4. From 40-Minute Builds to 6: Rebuilding CI Queueing at 210-Repo Scale (68 chars)

## Abstract (840/1,500 chars)

A 40-minute median wait before a CI job even starts turns into 40 minutes of context-switching on every pull request - and multiplied across 210 repositories sharing the same CI infrastructure, it becomes the thing engineers complain about in every retro. This session is the case study of getting that median wait down to 6 minutes. [PLACEHOLDER: name the 2-3 specific changes that moved the number - for example queue prioritization, runner pool restructuring, or build deduplication - in the order they shipped, plus whichever one looked obvious and made things worse before it was reverted.] Attendees leave able to measure where their own CI queue time actually goes without adding new tooling, tell a capacity problem from a scheduling problem, and sequence the fix most likely to pay back first across a large multi-repository fleet.

*660 characters of headroom left under the cap once the placeholder is replaced with real specifics — use it to name the one change that regressed before it was fixed.*

## Outline

*Pasted verbatim from the Abstract field, per your instruction. A reviewer sees no minute-by-minute structure here — this is the field most likely to cost the submission.*

A 40-minute median wait before a CI job even starts turns into 40 minutes of context-switching on every pull request - and multiplied across 210 repositories sharing the same CI infrastructure, it becomes the thing engineers complain about in every retro. This session is the case study of getting that median wait down to 6 minutes. [PLACEHOLDER: name the 2-3 specific changes that moved the number - for example queue prioritization, runner pool restructuring, or build deduplication - in the order they shipped, plus whichever one looked obvious and made things worse before it was reverted.] Attendees leave able to measure where their own CI queue time actually goes without adding new tooling, tell a capacity problem from a scheduling problem, and sequence the fix most likely to pay back first across a large multi-repository fleet.

## Audience level

**Intermediate** — assumes familiarity with CI/CD pipelines and build systems, no specific vendor or language required. (Dropdown wording at BuildScale Conf not confirmed — adjust to match their actual levels.)

## Self-review

- **Content — 2/5.** The abstract has a real before/after shape; the Outline field duplicates it instead of showing minutes and structure, so a reviewer has no evidence the talk itself is built.
- **Originality — 3/5.** A checkable number (40→6 min, 210 repos) is a strong start, but the abstract doesn't yet name which specific change did the work — fill the placeholder and this moves to a 4.
- **Relevance — 2/5.** Strong topic fit for the event overall, weak fit for the chosen track — "Platform & Infrastructure" would score this a 4.
- **Speaker — 3/5.** First-hand involvement is implied by the specificity of the numbers; no external evidence (repo, dashboard, post) is attached to check it.

This pack does not clear the skill's own pass threshold (Content and Originality below 4, Relevance below 3) — the two flagged items above are why. Submittable as-is if you're prioritizing the "Future of Engineering" slot and speed over rubric score.

## Before you submit

- [ ] Replace the abstract/outline placeholder with the real 2-3 changes and the one that regressed
- [ ] Confirm the Outline should genuinely mirror the Abstract, or give it real minute marks before pasting
- [ ] Confirm "Intermediate" matches BuildScale Conf's actual audience-level options
- [ ] Check BuildScale Conf's AI-assistance policy and rewrite in your own voice
- [ ] Confirm format/slot length, deadline and per-speaker cap, none of which were given here
```