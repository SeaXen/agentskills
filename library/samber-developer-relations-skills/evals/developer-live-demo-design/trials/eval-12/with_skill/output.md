# Demo Reliability Runbook — AE Product Walkthrough

## Root cause (working backwards from the failure)

Two reps hit a screen that no longer exists mid-call. That's not bad luck — it's the predictable output of a runbook with **no owner and no last-verified date**, built by someone who's since left. This maps directly to a known failure mode: *"Runbook's commands no longer match the product → no owner, no last-verified date → date every clean cold run, re-verify before each event."* Nobody was on the hook to notice the product shipped a UI change that broke the script, so it sat broken until it failed live, in front of a buyer, with no fallback and no recovery line.

The secondary flaw: this was clearly one continuous scripted flow, not independently-enterable segments — if it were segmented, a rep could skip the dead screen and keep going instead of winging the whole call.

Fixing this "properly" means fixing both: the missing ownership process (so it can't silently rot again) *and* the missing architecture (so the next rot event, which will happen, costs one segment instead of the whole call).

## Assumptions made in place of the interview

This skill normally runs a one-at-a-time interview before building anything. Producing the complete deliverable in one pass means these are inferred rather than confirmed — check them before rollout:

| # | Interview question | Assumption used |
|---|---|---|
| Claim | What must the audience believe? | Placeholder: *"[Product] solves [buyer's core pain] and a buyer can see their own workflow in it within the call."* Replace with your actual one-sentence claim — everything below hangs off this. |
| Venue | Where does it run? | Sales/customer calls, screen-shared over video conferencing, 1:1 or small buyer group. |
| Time budget | Minutes allowed | 10–15 min demo block inside a 30–45 min call. |
| Touches | What does it touch? | A live or sandbox product tenant, not local-only — SaaS product, can't fully air-gap. |
| Network | Venue control | No control — buyer's corporate network, VPN, and firewall are all unknowns per call. |
| Audience | Who's watching | Buyer + technical evaluator, mixed sophistication, per the **B2B/enterprise** and **sales-call** variants both applying. |
| What broke before | — | Exactly this: a screen removed/redesigned by product, script never re-verified. |
| What exists | — | A deck + a scripted walkthrough, ~8 months old, ownerless. |
| Constraints | — | Assume no embargoed features and no real customer data is *supposed* to appear, but flag this for confirmation — sandbox hygiene below covers it either way. |
| Event date | — | "Before Q1" — today is 2026‑09‑19, so target hardening complete and rehearsed by **mid-November 2026**, leaving buffer before Q1 kickoff. |
| Kit vs one-off | — | Re-run kit — every AE runs it, repeatedly, all quarter. This strongly promotes investment in a pinned sandbox tenant (tier 2-leaning) over a one-off effort. |
| Rehearsal hours / owner | — | Unknown — assign explicitly in the rollout plan below; this is the actual root-cause fix, not optional. |

Get real answers to these from whoever owns AE enablement now, and correct the runbook below before AEs rely on it.

## Fidelity tier decision

Filtering the ladder against the claim: a sales-call demo's value is answering "can you show me X" live — that rules out defaulting to tier 3/4 as the *primary* mode, per the sales-call variant ("open on what they came to see instead of the fixed sequence; there's no slide deck to retreat to"). But this is a re-run kit, not a one-off keynote, and the buyer's network is never under your control — both push toward pinning a sandbox environment rather than running the literal live network-dependent path.

**Recommendation: Tier 1 as the primary mode — live execution against a pinned demo/sandbox tenant, scripted/checkpointed paths, real interactivity preserved so reps can still answer off-script questions — with Tier 3 (a short recorded clip per segment) as the standing fallback for whichever segments are most exposed to product change.** This is a filtered top-2, not a forced choice — confirm it with whoever owns the sandbox tenant before building further; a fully offline tier‑2 build is worth it later if reps keep losing time to buyer-side VPN/firewall issues, but it's a week of build effort this plan doesn't assume you have before Q1.

Deleted from consideration and why: tier 0 (fully live prod) — a buyer's network and a live production account are exactly the two things that just caused this failure; no reason to keep both in play. Tier 4 (static screenshots) — undersells a live product to a technical evaluator and answers zero "can you show me" questions.

## Risk register (filtered to this demo)

| Risk | Likelihood × visibility | Mitigation |
|---|---|---|
| Scripted screen no longer exists (the actual incident) | High × high | Segment architecture below + owner + last-verified date + re-verify trigger on product releases |
| Buyer's corporate network/VPN blocks or throttles the tenant | Medium × high | Pinned sandbox tenant reachable over standard HTTPS; hotspot as backup only, not the plan |
| Rep can't recover because one segment depends on the previous segment's live output | High × high (this is likely also happening today) | Every segment gets its own restore point — saved view, bookmark, or sandbox reset — independently enterable |
| Real or stale customer-looking data shown to a buyer | Medium × high (B2B/enterprise stakes) | Synthetic, domain-realistic seed data in the sandbox tenant only, read-only credentials |
| Rep freezes mid-call with no recovery line | High × medium | Pre-written recovery lines rehearsed out loud, one repair attempt then switch |
| Demo overruns and eats the rest of the call | Medium × medium | Segments under ~90s, budget at 2× rehearsed length, droppable segments marked |

## The runbook

```
Demo:          AE product walkthrough (customer calls)
Claim:         [ONE SENTENCE — fill from your actual claim, see Assumptions above]
Venue/format:  Sales / customer call, screen-shared, 1:1 or small group
Budget:        10-15 min   /  Measured: <fill after first rehearsed run>
Tier:          1 (live, scripted, pinned sandbox)   Fallback tier: 3 (recorded clip per segment)
Network:       Sandbox tenant over standard HTTPS; hotspot backup only, tested against a
               guest/VPN-restricted network before relying on it
Data:          Synthetic seed data, read-only sandbox credentials; no real customer names,
               logos, or figures may appear on screen
Buddy:         N/A for 1:1 sales calls — see Recovery lines below for the no-buddy equivalent
Owner:         [NAME — assign this week; this field was empty before, which is the root cause]
Last verified: [DATE OF FIRST CLEAN REHEARSED RUN]  on <product version/release tag>
Re-verify:     Before every event this skill's checklist would normally say — for a re-run
               sales kit, read that as: on every product release that touches a demoed
               screen, and on a fixed monthly cadence regardless
```

### Segments

Replace these rows with an audit of your actual current deck — the shape matters more than the content. Each row must be enterable **without** running the row above it; if any current step in your deck reads "continues from the last screen," that's the exact defect that caused last week's failure and needs fixing here, not carried forward.

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 | [First claim-supporting capability] | Saved view / bookmark A in sandbox tenant | Scripted click-path 1 | 60s | no | Recorded clip `01-<name>.mp4` |
| 2 | [Second claim-supporting capability] | Saved view / bookmark B (NOT dependent on segment 1's output) | Scripted click-path 2 | 60s | no | Recorded clip `02-<name>.mp4` |
| 3 | [Capability tied to newest/most volatile UI area — highest risk of drifting again] | Saved view / bookmark C | Scripted click-path 3 | 75s | yes | Recorded clip `03-<name>.mp4` |

Speaker-notes format per segment (fill for each row above):

```
Segment 1  precondition: sandbox tenant reset, logged in as demo persona, bookmark A loaded
           expected:     [what the rep should see — exact labels, not "the dashboard"]
           if not:       one retry (reload bookmark), then switch to 01-<name>.mp4
```

### Fallback assets

```
01-<name>.mp4   recorded <date>, <length>s, one keystroke/click away in the screen-share window
02-<name>.mp4   recorded <date>, <length>s, same
03-<name>.mp4   recorded <date>, <length>s, same — this is the segment most likely to need
                re-recording after the next product release, given it covers the newest UI
deck.pdf        key frames embedded, available to share instead of the live app if the whole
                tenant is unreachable
```

Because there's no buddy in a 1:1 sales call, these assets must be reachable inside the same screen-share window (a browser tab, or embedded in the deck) — not a file-browser alt-tab, and not "I'll send it after the call."

### Reset and pre-provisioning

```
Reset (one command / action):   [Sandbox tenant reset script, or "restore snapshot X" if the
                                 product/platform doesn't expose a git-taggable state — see
                                 note below]
Verified cold:                  [ ] not yet — this is the first gate to clear before any rep
                                 relies on this runbook again
Pre-provisioned:                Sandbox persona logged in, seed data loaded, bookmarks A/B/C
                                 saved, recorded clips uploaded and linked
Never live on a call:           account creation, first-run setup, any step that waits on an
                                 external integration to sync
```

If the sandbox lives in a git-backed environment (e.g., a demo repo driving a local instance), `scripts/demo-checkpoints.sh save/goto/reset` gives you the tag-based version of this directly. For a hosted multi-tenant SaaS product, the same pattern still applies — it just takes the form of saved views/bookmarked deep-links per segment plus a tenant-reset action (admin script, seed-data re-import, or a "restore to baseline" feature if the product has one) instead of git tags.

### Recovery lines

Write these out; the two reps who winged it last week didn't have them.

- **Screen doesn't match / feature moved:** *"That moved in a recent update — let me show you where it lives now."* Then pivot to the next segment's claim rather than hunting for it live. Since there's no slide deck to retreat to on a sales call, the *next segment* is the retreat.
- **Sandbox unreachable / buyer's network blocks it:** *"Your network's being cautious with this — I've got the exact same flow recorded from yesterday, let's watch that and I'll narrate."* Switch to the relevant clip.
- **Genuinely broken, can't explain in one sentence:** *"That's a new one — I'm not going to debug it live. Here's what it looks like when it works —"* then switch.
- **Running long:** *"I'll skip [droppable segment] — happy to come back to it if it's relevant to what you're solving for."*

### Pre-flight checklist (per call)

```
[ ] Sandbox tenant reset and re-provisioned this week, not carried over from the last call
[ ] Bookmarks A/B/C load correctly — actually click them, don't assume
[ ] Fallback clips open and playable inside the screen-share window
[ ] Fresh browser profile: demo tabs only, no other client's tab, history/autofill empty
[ ] Notifications, chat, mail, calendar off for the call
[ ] Share mode: application/window, not full desktop
[ ] No real customer name, logo, or figure anywhere in the sandbox tenant
[ ] Recovery lines re-read once before the call
[ ] Last-verified date on this runbook is within the re-verify cadence below — if not, stop
    and re-run the rehearsal protocol before the call, don't wing it a third time
```

### Rehearsal log

Empty until the first pass — this is the evidence that the fix actually holds, not a feeling:

| Date | Run type | Time | Failures | Change made |
|---|---|---|---|---|
| | segment-by-segment | | | |
| | cold, full run | | | |
| | drill: sandbox unreachable mid-segment | | | |

## Pass threshold before any AE relies on this again

Scaled from this skill's baseline gate to a sales-call context:

- Three consecutive cold runs (tenant reset, bookmarks only, no manual repair) complete inside budget.
- Every segment entered directly from its own bookmark at least once, without running the segments before it.
- The screen-doesn't-match and sandbox-unreachable risks each drilled: trigger it, switch, keep talking, under 20 seconds.
- One full run rehearsed against a throttled/VPN-restricted network, since that's the buyer-side condition you can't control.
- Total time measured, under half the call's demo budget.

Don't compensate for a failed gate with more reps — change the design (drop a segment, pin a different bookmark, re-record a clip) and re-run.

## Rollout plan to actually land this before Q1

1. **This week:** assign an explicit owner for this runbook. This single field being empty is the root cause — don't ship the rest of this plan without it.
2. **Next 1–2 weeks:** owner audits the current deck screen-by-screen against the live product, flags every stale reference (not just the one that broke), and fills in the real segments/claim above.
3. **Weeks 3–4:** build the sandbox tenant + bookmarks + reset action if they don't already exist; record the three fallback clips.
4. **Weeks 5–6:** run the rehearsal protocol above with 2–3 AEs (not just the owner) until the pass threshold holds; log every run.
5. **Before Q1 kickoff:** short session with the full AE team — walk the recovery lines out loud, not just read them.
6. **Ongoing, starting Q1:** owner re-verifies on a monthly cadence and whenever product ships a change touching a demoed screen — ask product/PMM to loop the demo owner into release notes or design reviews for the demoed surfaces, so the next UI change surfaces *before* a call, not during one.

Store the claim, chosen tier, segment list, and reset action wherever this team keeps living documentation — re-deriving them from scratch next quarter, under time pressure, is exactly how this runbook went eight months without an owner the first time.