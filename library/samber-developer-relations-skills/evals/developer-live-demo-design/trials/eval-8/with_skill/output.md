# Demo Runbook — Tracing Agent, Booth Floor

## What's changing from your webinar walkthrough, and why

Your 15-minute install→configure-collector walkthrough is built for a captive, seated audience with a fixed 15 minutes. A booth gets neither: dwell time ranges from 90 seconds to 20 minutes, nobody is seated, and most people decide whether to stop within seconds. Three structural fixes, not a shorter version of the same talk:

1. **Lead with the payoff, not the setup.** Install/configure-collector is the least visually interesting part of the whole product and it's currently your opening. Booth rule: *lead with the most visually obvious segment, never the setup.* Install moves to a later, optional segment for people who are already sold and asking "how do I get this."
2. **Stop writing one 15-minute script. Write Lego blocks.** A single linear walkthrough breaks the moment someone leaves at minute 2 or arrives at minute 8 of someone else's demo. Every segment below is independently enterable — no segment depends on a previous one having run.
3. **Design for the room, not just the product.** Loud floor and a window behind you are demo-breaking constraints your webinar format never had to survive. Both are addressed below.

Fill in the `< >` placeholders with your actual product's commands/UI before rehearsing — I don't have your CLI syntax or product name, so I've kept the structure concrete and the specifics parameterized. Wherever I filled a gap you didn't give me, it's marked **ASSUMED — confirm**.

---

## Header

```
Demo:          <tracing agent> booth loop
Claim:         Point this at a real running app and see exactly which call in a
               request is slow — live, with <zero manual instrumentation>.
               ASSUMED — confirm: only keep "zero manual instrumentation" if
               your agent actually auto-instruments. If it needs SDK/code
               changes, drop that clause — claiming it is faking the output,
               not hardening the setup, and an infra audience will ask.
Venue/format:  Booth floor, 3x3, big infra conference, 2 days
Budget:        Variable: 90s (walk-by) to 20 min (engaged technical visitor).
               Design as independently enterable segments, not one script.
Tier:          2 (live, fully local) for driven/engaged visitors.
               Fallback/attract mode: 3 (silent captioned loop) running
               whenever no one is actively engaged.
Network:       Offline. Fully local stack — do not depend on venue Wi-Fi for
               2 days across a hall full of other booths' demos.
Data:          Synthetic services only (e.g. "checkout-service",
               "inventory-api", "payments-api"), realistic volume, no real
               customer/company names, no real API keys.
Buddy:         <co-worker staffing the booth> — holds a second laptop with
               the identical stack pre-built, swaps in if the demo machine
               dies mid-day. ASSUMED — confirm who's on the booth with you.
Owner:         <you>
Last verified: <fill after first cold rehearsal>
Re-verify:     Before the conference, and again each morning of the 2 days
               before doors open (see "Per-day pre-flight" below).
```

**Why tier 2, not tier 3, even though tier 3 (a recording) can prove this exact claim just fine:** the ladder's default is tier 3, but the skill's own re-ranking rule promotes tier 2 whenever the same stack gets re-run many times rather than once — that's exactly a 2-day booth with dozens of walk-ups per hour. A local, seeded stack also sidesteps the single biggest venue risk at a large infra conference: Wi-Fi collapsing once the hall fills, which every other booth is hammering at the same time. Run the recorded version (tier 3) as the *ambient attract loop* when no one is engaged — see below — not as your main mode.

**Branch you need to resolve before this plan is final:** does your product's UI/backend run fully locally, or is the trace viewer a hosted SaaS console? If it's SaaS-only with no offline mode, tier 2 is not available to you ("a product with no local mode kills tier 2") and the whole plan below should shift to tier 3 as primary — a set of pre-recorded real sessions against a demo tenant, looped and re-triggered live only for visitors who explicitly ask to drive it themselves against your sandbox tenant over the venue hotspot.

---

## Segments

Independently enterable — the presenter jumps to whichever one matches who just walked up, not necessarily #1 first.

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 — Hook | A slow call in a real request is visually obvious in this tool, at a glance | pre-seeded trace view, `<checkpoint: hook-loaded>` | open the trace waterfall, point at the highlighted slow span | 30–45s | no | recorded clip `01-hook.mp4`, silent + captioned |
| 2 — Root cause | The tool tells you *why* it's slow, not just *that* it's slow | same trace, drill into the flagged span | click into span → shows `<N+1 query / slow downstream call / lock wait>` | 60–90s | no | recorded clip `02-rootcause.mp4` |
| 3 — Install | Getting this running is one line, not a project | fresh terminal, `<checkpoint: pre-install>` | paste `<agent install command>`, show it attach to the running app | 60–90s | yes | recorded clip `03-install.mp4` (sped up) |
| 4 — Collector/pipeline | This scales past a laptop demo — same pipeline in production | pre-built `<collector config file>`, `<checkpoint: collector-configured>` | show config, point at where it ships to `<storage/backend>` | 60–90s | yes | annotated architecture diagram, printed + on a tablet |
| 5 — "Try it on your stack" (only if asked) | It works outside this canned demo | `<sandbox / their own repo if they brought one>` | live, improvised | uncapped, cap by hand at ~3 min | yes | offer to follow up post-conference, take their contact |

For each segment, write the precondition/expected-screen/if-not lines the way the template asks — these are what let you jump straight to segment 4 for someone who arrived mid-conversation:

```
Segment 1  precondition: background load generator has produced a trace with
           a slow span in the last 10s
           expected:     waterfall visible, one span highlighted red/orange
           if not:       hit <checkpoint: hook-loaded> reset, or cut to clip 01
Segment 3  precondition: terminal open, target app already running unmodified
           expected:     agent attaches, next trace shows it in the waterfall
           if not:       one retry; if it fails twice, cut to clip 03
```

**Load generator is load-bearing here and isn't in the standard template — add it as its own checkpoint.** A booth demo that requires the presenter to manually trigger a request before every walk-up either goes stale (same exact trace shown 200 times, looks canned) or costs 10–20 seconds of dead air per visitor while something "warms up." Run a synthetic traffic generator continuously in the background, producing varied requests with a deliberately-injected slow span at a randomized-but-bounded interval, so segment 1 is always fresh within the last few seconds without the presenter doing anything. Verify it doesn't drift into a state where the "interesting" trace disappears for stretches — that's a rehearsal item below, not an assumption.

---

## Fallback assets

```
01-hook.mp4          silent, captioned, loops cleanly, <15-25s>, this is also
                     your ambient attract-mode video when no one's at the booth
02-rootcause.mp4     silent, captioned, <45-60s>
03-install.mp4       sped up, captioned, <30-45s>
04-architecture.png  printed A3 + on a tablet on the booth counter
qr-followup.png      links to a recorded 15-min version (your existing webinar
                     content is exactly right *here* — repurpose it as the
                     take-home asset, not the live opener)
```

Assets play on the booth screen itself or a second small display — nothing that requires alt-tabbing or hunting through a laptop's file browser while someone is standing in front of you.

---

## Reset and pre-provisioning

```
Reset (one command):   <make demo-reset> — reseeds fixtures, restarts load
                       generator, clears any state a previous visitor's
                       "try it yourself" left behind
Verified cold:         <fill after rehearsal>
Pre-provisioned:       agent binary cached locally, collector image pulled,
                       trace backend pre-warmed, fixture services already
                       built (never build/install live at the booth)
Never on stage:        install of anything not already cached, first-run
                       migrations, DNS/account verification
```

Use `scripts/demo-checkpoints.sh` from this skill to tag the few real state-transitions (pre-install → agent-installed → collector-configured) as git tags on the demo repo, so segment 3 and segment 4 can each be entered fresh without replaying the other:

```
scripts/demo-checkpoints.sh save 1 pre-install
scripts/demo-checkpoints.sh save 2 agent-installed
scripts/demo-checkpoints.sh save 3 collector-configured
scripts/demo-checkpoints.sh goto 2      # jump straight into segment 3's demo
scripts/demo-checkpoints.sh reset       # back to pre-install between visitors
```

The trace data itself (segments 1–2) doesn't need git tags — that's the load generator's job, reset via the same `make demo-reset`.

---

## Recovery lines

```
Booth-specific network/dependency failure:
  "I run this fully offline on purpose — half this hall is fighting for the
  same Wi-Fi right now. Give me one second." [hit reset, keep talking about
  what the trace would show]

Unfixable error mid-demo:
  "That's a new one — I'm not going to debug it in front of you. Here's what
  it looks like when it's behaving —" [switch to the matching clip]

Someone arrives mid-explanation of a segment that just broke:
  "Perfect timing actually — let me show you the part that matters first."
  [jump straight to segment 1 fresh, don't apologize for something they
  didn't see]

Overrun with an engaged 20-minute visitor and another prospect waiting:
  "I want to keep going but I've got someone waiting — grab my card/scan
  this and I'll send you the deep-dive recording tonight."
```

One repair attempt, ~20 seconds (this skill's baseline), then switch — over 2 days you will hit this dozens of times, so the switch has to be reflexive, not a decision you make fresh each time.

---

## Pre-flight checklist

Booth-specific additions are marked; the rest is the skill's standard list.

```
[ ] Machine plugged in, sleep/screensaver off — for the FULL 2 DAYS, not just
    a rehearsal session
[ ] Load generator running and producing a fresh slow-span trace within the
    last 10s — BOOTH-SPECIFIC, this is your segment-1 precondition
[ ] Demo profile only — no daily-driver mail/chat/calendar, fresh browser
    profile, extensions off
[ ] Shell history and editor recents cleared; custom prompt set
[ ] Terminal 24pt+, high-contrast/light theme, block cursor
[ ] Monitor angle checked against the window — BOOTH-SPECIFIC, see below
[ ] No audio-dependent cues anywhere in the demo — BOOTH-SPECIFIC, floor is
    loud; every "it worked" signal is visual (color/highlight), not a sound
[ ] Ambient/attract loop (clip 01, silent, captioned) set to auto-replay when
    idle — BOOTH-SPECIFIC
[ ] Reset command run once; demo left at segment-1-ready state
[ ] Hotspot on and paired anyway, as backup only — not the plan
[ ] Fallback clips one keystroke away, not behind a file browser
[ ] Synthetic data only — no real company/customer names, no real keys,
    `.env` holds placeholders only
[ ] Nothing embargoed or unreleased visible on any screen, including
    dropdowns and the "try it yourself" path if visitors get hands-on
[ ] Buddy briefed, second laptop identically built, sitting at/near the booth
[ ] Business cards / lead capture (QR to the recorded walkthrough) within
    arm's reach — this is where your original 15-minute content lives now
```

**Window/glare item, spelled out:** a big window behind the booth means the light hitting your screen changes across the day and across the two days — morning sun is not afternoon sun. Check monitor angle and brightness against the window at more than one time of day during setup, not just once. If the screen faces the window, either angle it away, add a hood/backdrop, or crank brightness well past what looked fine indoors during rehearsal at your desk. This is a legibility risk the standard "check from the back row" checklist doesn't cover, because it assumes a stage with controlled lighting, not a booth with direct daylight — add it as its own gate, not a subset of the font-size item.

### Per-day pre-flight (day 2 specifically)

The standard checklist assumes one clean run before one slot. You're running this continuously across two days, which is its own failure class:

```
[ ] Overnight reboot/update didn't silently change display settings,
    disable the profile, or resize the terminal
[ ] Re-run the one-command reset cold before doors open, don't trust
    yesterday's end-of-day state
[ ] Re-check monitor angle against the window — the booth may not be in the
    same physical spot relative to the sun as when you first checked
[ ] Load generator still running, still producing fresh traces
[ ] Buddy's second laptop still in sync (same reset run on it too)
```

---

## Rehearsal and pass threshold

Standard gate plus two additions this scenario needs that the default list doesn't cover — noted as additions, not swaps:

- Three consecutive cold runs complete inside budget (baseline: your tightest realistic slot, ~90s, not the 20-minute ceiling).
- Every segment entered directly from its own restore point, without playing the segments before it.
- Top risks drilled: network dependency, agent-install failure, load-generator going stale — each switched to fallback in ~20s or less.
- One full run with the network disconnected.
- One full run at booth-like lighting — near an actual bright window, or with a lamp simulating it, at more than one simulated time of day. *(Addition: the default gate's "venue resolution" item doesn't cover ambient daylight; this scenario needs it.)*
- One full run in a genuinely loud environment (café, music) to confirm every "it worked" signal is visible, not just audible. *(Addition, same reason — loud floor is a new failure class the default gate assumes away.)*
- **Soak test: run the full loop unattended for 2+ hours**, confirming the reset survives many consecutive visitor cycles and the load generator doesn't drift into a boring state. *(Addition — a single conference slot never needs this; two days of continuous operation does.)*
- Total demo time for the shortest segment (segment 1 alone) measured well under 90 seconds — that's the version most walk-bys actually see.

```
| Date | Run type | Time | Failures | Change made |
|------|----------|------|----------|-------------|
| TBD  | segment-by-segment | - | - | - |
| TBD  | cold, offline | - | - | - |
| TBD  | cold, offline | - | - | - |
| TBD  | cold, window-glare simulated | - | - | - |
| TBD  | cold, loud environment | - | - | - |
| TBD  | soak, 2hr unattended loop | - | - | - |
| TBD  | drill: network killed mid-segment 1 | - | - | - |
```

Fill this in as you rehearse over the next month; don't ship the runbook to the booth with this table still empty.

---

## Risks kept from the taxonomy (others filtered out as not live here)

| Risk | Why it fires here | Mitigation already designed above |
|---|---|---|
| Venue Wi-Fi collapses once the hall fills | 2-day infra conference, every booth demoing something | Fully local stack, tier 2 |
| Ambient noise defeats an audio-dependent cue | You told me the floor is loud | No sound-dependent signals; visual only |
| Screen unreadable due to window light | You told me there's a window behind you | Angle/brightness check at multiple times of day, added pre-flight item |
| A segment can't start because the previous one failed | Booth visitors arrive mid-sequence constantly, more than any stage talk | Every segment has its own restore point, checkpoint-tagged |
| Demo looks stale/same to repeat passersby or staff over 2 days | Continuous multi-hour operation, unique to this format | Background load generator producing varied fresh traces |
| Real customer/company data visible | Public show floor, anyone can see the screen | Synthetic service names and data only |
| Laptop dies mid-conference | Two full days of continuous run, not one slot | Buddy with an identical second laptop |

Everything else in the taxonomy (third-party API rate limits, corporate VPN reconnects, embargoed features) is filtered out unless you tell me it applies — say so if your collector genuinely needs to reach a real third-party endpoint or an unreleased feature will be visible, and I'll fold it back in.