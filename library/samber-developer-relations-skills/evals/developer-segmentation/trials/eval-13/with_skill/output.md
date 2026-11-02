# Dredgewater Compute — developer segment re-run, H2 2026

## The actual answer to "what should I do"

**Don't redo this from scratch. Re-run it.** You have a stored map from last September — the skill's own routing rule for that exact situation is explicit: *"Re-run our segment map, it's from last year" → steps 3-6 against the stored map, return a diff. Rebuild from step 1 only when there's no stored map.* You have one. Use it.

There's also a direct evidence reason, not just a process rule: studio share of new signups moved **18% → 31%** in the twelve months you spent building for mid-size gaming studios as primary. That's the concentration metric the whole method is designed to move. Throwing out the cut that produced that number and starting over is how a team quietly re-argues a bet it already won — the failure mode this skill calls "argument frequency": a map that's working should *end* the audience debate for a horizon, not get reopened every time someone new looks at it.

**Before you accept "redo from scratch," ask whoever's requesting it which of these actually happened** — these are the only things that legitimately reopen the cut itself, not just its sizing:

- a pricing or packaging change
- a new engine/platform target you're now shipping for
- a change in *why* the company funds this work (adoption → sales enablement, etc.)
- a competitor took mid-size studios' default choice from you

If none of these happened, what you're looking at is a **scheduled review that's three quarters overdue** (this skill's baseline cadence is quarterly; you're at four quarters), not a reason to discard the cut. Fix the cadence, don't discard the map.

One caveat: I'm reconstructing your Cut section from the three facts you gave me, not your actual stored doc. True it up against the real file before you circulate this.

---

## Diff: what the last 12 months actually show

| | |
|---|---|
| **Predictions that held** | Mid-size gaming studios as primary — signups concentrated toward the segment you built for, not away from it. VFX/animation as anti-segment — nothing you shipped touched the colour-pipeline blocker, so there's no new information to revisit that exclusion on. |
| **What moved** | Studio share of signups: 18% → 31% (+13pts, +72% relative). Two of three shipped artefacts targeted the primary segment specifically. |
| **What didn't move, and should have been tracked** | Your "studio share" metric bundles mid-size (primary) and indie (secondary) into one bucket. You cannot currently tell whether the +13pts came from mid-size studios (the segment you funded artefacts for) or from indie riding along — which matters, because if it's mostly indie, the primary bet isn't the thing that's working. **Split this metric before the next review.** |
| **A drift worth naming before it repeats** | One of the three shipped items was a general "for developers" performance guide — not aimed at mid-size studios or indies specifically. This skill's own artefact-fit measure counts anything built for "developers" generally as a miss, on purpose: it's the first symptom of effort sliding back toward the undifferentiated audience the whole exercise exists to avoid. One instance isn't a crisis. A second one is the pattern to stop. |
| **Retire / promote** | Nothing retires. Primary and secondary both hold. Anti-segment holds. |

---

## Updated map

```
# Developer segment map — Dredgewater Compute, H2 2026 (re-run of Sep 2025 map)

## Cut
Dimensions: sector/workload (real-time game rendering vs. colour-managed
VFX/animation pipelines) × firmographic company size (mid-size studio vs. indie).
Carried forward unchanged from the Sep 2025 map — no trigger this horizon
(pricing, platform target, funded driver, competitive loss) justifies reopening it.
Confirm exact original wording against the stored doc; reconstructed here from
the three headline facts on hand.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| Mid-size gaming studios | ~20-500 employees, real-time engine workloads, dedicated tools/pipeline team | ~30k-90k engineers, inferred (analogy to overall professional game-dev population split by studio-size tier; no lookup run this session) | user/engineer evaluates, tech director or studio CTO approves | reference architecture, engine-specific integration, migration path from incumbent, named studio references | GDC, Unity/Unreal-adjacent forums and Discords, engine-specific communities | measured: signup share 18%→31%, 2 dedicated artefacts shipped and adopted |
| Indie game developers | 1-15 person teams, self-serve, price-sensitive | ~1M-3M, inferred (analogy to commonly cited indie/hobbyist dev population; no lookup run this session) | user = buyer, or no purchase | quickstart, free tier, artefacts primary already funds — no dedicated build this horizon | itch.io, indie Discords, game jams | not separately measured — folded into the 18%→31% studio figure; needs its own split |
| VFX and animation houses | colour-managed rendering pipelines (film/animation, not real-time) | not sized this round — anti-segment status unchanged | would add a pipeline/colour-science approver | ACES/OCIO-class colour-pipeline support — unbuilt | VES/animation-industry circles, colour-science forums | anti-segment carried forward, no new evidence either way |

## Primary
Mid-size gaming studios. Held from last year on measured concentration evidence
(18%→31% signup share) plus two artefacts built and adopted. Score
(assumed funded driver: developer adoption/revenue via self-serve signups —
confirm this if it's actually sales enablement or something else, the ranking
below would shift): size 2, reachability 3, fit 3 (signup data confirms it directly),
value 3, effort 2 (declining — two artefacts already paid down), competitive
position unscored (no data given this round), compounding 3 (named-studio
references travel through GDC talks and engine communities). Beats indie on
value; beats VFX outright, since VFX still needs an artefact you haven't built.

## Secondary
Indie game developers — still served only by artefacts the primary already
funds (no dedicated spend this horizon). Open question: is the guide that
shipped generic actually the thing pulling indie signups in, via search rather
than the two studio-specific artefacts? Worth a cheap attribution check — see
Hypotheses.

## Anti-segment
VFX and animation houses. Unchanged: reachable, plausibly valuable, but still
blocked on the colour-pipeline artefact — unfunded, three-quarters-of-a-build
problem, same as last year. Revisit only if colour-pipeline work gets funded
for an unrelated reason.

## Hypotheses
1. "Studio signup growth is driven by the primary segment, not the secondary."
   Currently unfalsifiable — the metric doesn't split mid-size from indie.
   Test: re-cut new-signup data by company-size band for this window before
   the next review. Below the evidence floor until split.
2. "The generic 'for developers' guide is what's actually pulling in indie
   signups, not the two studio-targeted artefacts." Test: pull referral/campaign
   source on the last quarter's studio-bucket signups, see what share arrived
   via the generic guide vs. the two targeted pieces vs. organic engine-community
   channels. Cheap, days not weeks. If confirmed, the generic guide isn't drift —
   it's an intentional indie-acquisition channel and should be named as such
   rather than accidentally shipped as an untargeted artefact.

## Implications
Build: nothing new funded for VFX (artefact list unbuilt). Continue the two
studio-facing artefact lines that are already working — do not divert their
follow-on work into another generic guide.
Publish: keep concentrating in engine-specific/GDC-adjacent channels, not
general developer channels.
Prove: name the studios behind the 18%→31% move as references — the skill's
own compounding rule says proof travels inside a segment, not spread across one.
Stop: producing a third general "for developers" piece before hypothesis 1 and
2 above are resolved — you can't tell right now whether it helps or dilutes.

## Review
Re-read in one quarter (reset to quarterly cadence — this run was 3 quarters
late). Early re-read if: pricing/packaging changes, a new engine/platform
target is added, the funded driver changes, a competitor takes mid-size
studios' default position, or the split-metric test in Hypothesis 1 comes back
showing indie (not mid-size) drove the move.
```

---

## Quality gate

- **3-5 segments** — 3. Pass.
- **Every segment differs on artefact/channel/proof from siblings** — yes (engine-integration vs. quickstart-and-free-tier vs. unbuilt colour pipeline). Pass.
- **Every size carries range + method + date + confidence** — gaming/indie sizes are inferred with method stated but no fresh lookup performed this session (no web access this run). **Fails the "estimated" bar, passes as labelled inferred** — upgrade before this goes external.
- **Decision unit named or explicitly absent** — mid-size and indie stated; VFX not applicable (anti-segment). Pass.
- **≥half of funded segments clear the evidence floor** — mid-size studios clears it (measured signups + 2 shipped, adopted artefacts). Indie does not — it's riding on an unsplit metric. 1 of 2 funded segments clears it: exactly half. Pass, barely — close the metric-split gap fast.
- **Anti-segment non-empty, includes something the team wanted to keep** — VFX/animation, plausibly attractive. Pass.
- **Segments in their own language** — mostly; "mid-size gaming studios" and "indie game developers" are how they'd describe themselves. Pass.
- **Two pages, named review date** — fits, review date set to one quarter out. Pass.

## What would upgrade this before you present it

1. Run the SlashData games-sector estimate and a GDC/Newzoo State of the Game Industry studio-size breakdown to move mid-size and indie sizing from *inferred* to *estimated* — I had no web access this session, so those numbers above are judgment, not lookup.
2. Split "studio share of signups" into mid-size vs. indie for the last 12 months — this is the single highest-value fix here; right now your best evidence for the primary segment is contaminated by the secondary.
3. Run the attribution check on the generic guide before deciding whether it was drift or an accidental indie-acquisition win.
4. True up the Cut section's wording against your actual stored September doc — I reconstructed it from three facts, not the file.