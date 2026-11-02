## Talk reuse — quick verdicts

**PyData Grenoble (Oct) → the two March events: ✅ not a problem.**
Giving the same talk at multiple conferences is completely normal — it's how a good talk earns its keep. The only real risks:

- **Audience overlap.** Different city, different community (PyData is Python/data-science-specific) — unless the March events share a big chunk of attendees with Grenoble, nobody in the room has seen it. Check each March event's expected audience once; if either draws from the same regional/PyData-adjacent crowd, refresh the framing so it doesn't read as a rerun.
- **CFP originality clauses.** A few invite-only or "debut talks only" events explicitly ask "has this been given before?" — most don't care, but check each CFP's submission form. If asked, answer honestly; disclosure isn't disqualifying, non-disclosure if later caught looks bad.
- **Staleness.** Six months old by March. Skim it once for anything time-sensitive (version numbers, screenshots of UIs that changed, stats, "as of today" claims) and refresh those specific slides — not a rewrite, a pass.

Don't bill either March talk as new/exclusive content if it isn't — just don't over-claim, and you're clear.

**Hartfield Cloud Days (closes in 3 weeks): ✅ submit the same proposal.**
Reusing a written, already-accepted-elsewhere proposal is standard "conference circuit" practice, and a proposal that already convinced two review committees is a strong submission, not a weak one. Two adjustments before you fire it:

- Retitle/reframe the abstract's first two sentences to Hartfield's stated theme/track if you can find one — committees notice a proposal that was visibly written *for* them vs. copy-pasted.
- Now you're running **three deliveries of one talk within a couple months**. That's fine logistically, but flag it to yourself as a content-fatigue risk for *you*, not the audience — rehearse enough that the third delivery doesn't sound phoned in. If any of the three is filmed and published before the next one happens, mention in the follow-up pitch that a recording exists (some organizers prefer unrecorded-elsewhere talks for their own YouTube channel — rare, but worth a one-line disclosure if their CFP asks).

---

## Narrative arc — slide skeleton

Same structure works for a 25–40 min conference slot regardless of topic. Hang your existing content on it; renumber for your actual timing.

| # | Slide | Purpose | Time |
|---|---|---|---|
| 1 | Title + you | Name, one-line credibility (not a bio dump) | 0:30 |
| 2 | The hook | A concrete, specific moment of pain — a real bug, outage, cost, or "this took us 3 weeks" — not an abstract problem statement | 1:30 |
| 3 | Why this matters now | The stakes: what breaks/costs/scales badly if this problem stays unsolved | 1:00 |
| 4–6 | The naive approach + why it fails | Show the obvious solution first, then where it cracks — this is what makes the eventual answer feel earned, not assumed | 3–4 min |
| 7–9 | The real approach | Your actual technique/architecture/idea, built up incrementally, not dumped as one dense diagram | 5–7 min |
| 10 | **Demo** | Live, see playbook below | 5–8 min |
| 11–12 | What it cost / tradeoffs | Credibility slide — no solution is free, naming the tradeoff is what makes experts trust the rest of the talk | 2 min |
| 13 | Takeaway | One sentence the audience could repeat to a colleague tomorrow. If you can't compress it to one sentence, the talk doesn't have a spine yet | 1 min |
| 14 | CTA + contact | Repo/link/handle, one clear next action (star it, try it, DM you) | 0:30 |

Two rules that matter more than slide count:
- **The hook and the takeaway should rhyme.** Open on the specific pain from slide 2, close by naming that it's now solved — gives the talk a shape instead of a list.
- **One idea per slide.** If a slide needs you to say "and also," it's two slides.

---

## Demo resilience playbook

The goal isn't "the demo never breaks" — it's "a break never stops the talk."

**Before the room:**
- Record a **backup video** of the full demo at real speed, captions optional. Put it on the slide immediately after the live-demo slide, muted, ready to unmute-and-play with one click if live fails.
- Run the demo on a **local/offline environment** if at all possible — venue wifi is the single most common conference-demo killer. If cloud is unavoidable, bring a personal hotspot as fallback network, tested in advance, not assumed.
- Use **seeded, deterministic data** — no "let me sign up live" or reliance on external APIs that can rate-limit, time out, or return different data than in rehearsal.
- **Pre-flight script**: one command that resets the demo to a known-good state. Run it the morning of, and again 10 minutes before your slot — not just once during prep days earlier.
- **Close everything else**: notifications off, browser tabs trimmed, terminal font bumped up, resolution matched to the projector aspect ratio (test this, don't assume 16:9).

**During:**
- **Narrate before you click**, not after — "I'm going to trigger X, which should produce Y" means if Y doesn't show up, the audience already knows what was supposed to happen and you can pivot without looking lost.
- Build in a **timing buffer**: rehearse the demo to run 20% under its slot. A rushed recovery reads as competence; a rushed happy-path reads as anxiety.
- **Rehearse the failure, not just the success.** Know exactly what you say and do in the first 3 seconds after something breaks ("ha, live demo — here's the recording" is a fine line, said once, then move on). The panic is what kills a demo, not the bug.
- Keep a **screenshot slide** of the expected final-state output right behind the video fallback — if even the video won't play (AV failure), you can still narrate over a static image.

**The three checkpoints that catch most failures:** test the full demo 24h before on a network like the venue's, test again the morning of, and do a silent dry run in the actual room if you get any AV time before your slot — projector color/resolution and room wifi are the two things rehearsal-at-home never catches.

---

## What I need to actually populate this

The structure and playbook above are ready to use as-is. To turn slides 2–13 into your real deck (not a template), send me:

1. **What the talk is actually about** — the specific problem/technique/system.
2. **Audience level** for each of the three (four, counting Grenoble as reference) events — general dev crowd vs. specialists changes how much slides 4–6 need to explain.
3. **What the demo does**, and its single riskiest failure point (network call? GPU/resource dependent? third-party API?) — so the resilience plan above gets tailored instead of generic.
4. **The two March events' names/themes** — lets me flag if either overlaps Grenoble's audience and tailor the opening hook per room.

Drop those in and I'll write the actual slide text, not just the skeleton.