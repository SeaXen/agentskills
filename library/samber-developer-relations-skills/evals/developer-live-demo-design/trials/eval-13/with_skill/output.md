Using developer-live-demo-design to build a runbook for Thursday's all-hands demo.

Given the context you gave (internal, whole company, 10 min, video call recorded to the internal drive, staging with a copy of last month's production data, explicitly not over-engineering it), I skipped the interactive interview and made the calls myself — flagged with `‹›` wherever you need to fill in your own specifics.

**Tier decision, stated up front:** Tier 1 — live execution against staging, but with commands pasted from a script rather than typed. Tier 2 (a real offline stack) is off the table on days-of-prep. Tier 0 (raw live typing) buys you nothing extra for an internal audience that already knows it's rough. Standing fallback is Tier 3: one ~2-minute screen recording of a clean run, made once during rehearsal — cheap insurance given the data risk below, not a sign you're over-building this.

**One thing worth 30 seconds of thought, unprompted:** the recording isn't just today's live session — it's a permanent internal-drive artifact showing a real copy of last month's production billing data (real customer names, real amounts) to the entire company. "Internal and rough" lowers the polish bar; it doesn't lower the data bar. Pick which records you put on screen rather than letting the presenter scroll live.

---

```
Demo:          Billing Reconciliation Service — all-hands walkthrough
Claim:         ‹Sharpen this, but as a default:› "The new reconciliation
               service automatically finds and explains billing mismatches
               across a full month of real transaction volume — work that
               used to mean a manual spreadsheet reconciliation."
Venue/format:  Internal all-hands, video call, recorded to the internal drive
Budget:        10 minutes  /  Measured: ‹fill after rehearsal›
Tier:          1 (live, scripted input, against staging)  Fallback tier: 3
Network:       Whatever gets you on the call, plus staging reachability
               (VPN/company network) — not venue Wi-Fi, so lower risk than
               a conference, but still worth one test run on the actual
               link you'll present from, not just from your desk on a
               different day.
Data:          Staging seeded with a copy of last month's real production
               billing data. Nothing synthetic — this is real customer
               data, on a recording that outlives the meeting. Pick 2-3
               specific mismatch records ahead of time; don't browse live.
Buddy:         ‹Name a co-presenter› — video-call equivalent of a front-row
               buddy: has staging open in a second window, ready to unmute
               and share their own screen if your connection or app dies.
               Also fields chat questions so you don't lose the floor.
Owner:         ‹You›
Last verified: ‹date of your one full rehearsal run›  on ‹staging build/commit›
Re-verify:     Before Thursday's call. If the reconciliation service
               changes between now and then, re-run once more the morning of.
```

## Segments

Three segments, ~90s each (this skill's default segment cap, scaled up slightly since 10 minutes is a generous slot compared to a stage demo) — leaves ~5-6 minutes for narration, intro, and questions.

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 | It finds real mismatches at real volume, not toy data | A reconciliation run already kicked off/cached against last month's dataset — **don't run the full-month job live if it takes more than ~15-20s; pre-run it and open the completed report** | Scripted command/click sequence, pasted or clicked from a written list, not improvised | 90s | No | Screen recording clip `01-run.mp4` |
| 2 | Each mismatch comes with a reason, not just a red flag | Report view, pre-filtered to 2-3 mismatches you picked in advance (not "whatever's on top") | Walk the 2-3 pre-picked records | 90s | No | Screenshot of the same 2-3 records, annotated |
| 3 | Resolving one closes the loop | One pre-selected mismatch, already open | One resolve/approve/write-off action | 60s | **Yes** — cut first if you're running long | Screenshot of before/after state |

Precondition/expected/if-not, written down so you don't have to decide mid-call:

```
Segment 1  precondition: reconciliation report for last month already generated
                          and open in a tab (not triggered live)
           expected:     report loads with a nonzero mismatch count
           if not:       one retry (re-open the tab/re-run the cached query),
                          then switch to 01-run.mp4 and keep talking

Segment 2  precondition: the 2-3 records you picked ahead of time are still
                          present and unmodified (don't touch them in your
                          rehearsal's final pass)
           expected:     each shows a reason string, not just "MISMATCH"
           if not:       skip to the annotated screenshot, same records

Segment 3  precondition: the one record for this segment is untouched
                          (separate from the 2-3 in segment 2)
           expected:     status flips from "open" to "resolved"
           if not:       narrate what should happen, show the before/after
                          screenshot, move straight to questions
```

## Fallback assets

```
01-run.mp4        ~90s screen recording of segment 1, made during rehearsal
02-mismatches.png annotated screenshot of the 2-3 picked records
03-resolve.png    before/after screenshot of the resolve action
```

Keep these open in browser tabs or as slide images in whatever you're sharing — not in a separate file browser. On a video call, "let me find that file" reads exactly as badly as it does on a conference stage.

## Reset and pre-provisioning

```
Reset:            You likely don't need one. Instead of a resettable
                   environment, pick untouched records for segments 2 and 3
                   so there's nothing to revert. If staging does have a
                   reseed script, name it here: ‹./reset-script›
Pre-provisioned:  Logged into staging with a fresh session (not a token
                   about to expire mid-call). Last month's reconciliation
                   report already generated once, before the call, so
                   segment 1 opens a finished report instead of running
                   the job live.
Never live:       The full-month reconciliation job itself, if it takes
                   longer than a few seconds — run it before the call,
                   show the finished output.
```

## Recovery lines

- Staging misbehaves / unexpected data from the real prod copy (the single most likely failure here — this is real, messy, un-battle-tested data): *"That's the joy of running this against real data instead of a clean demo set — here's a run I captured earlier that shows exactly the same thing."* → switch to `01-run.mp4`.
- Screen share or call hiccup: ‹buddy name› unmutes and shares their own already-open staging tab, you keep narrating.
- Running long: *"I'll skip the resolve step — you get the idea, and I'm happy to show it after."* → drop segment 3.

## Pre-flight checklist (video-call version)

```
[ ] Fresh staging session logged in, not a session left over from rehearsal
[ ] Segment 2's 2-3 records and segment 3's 1 record identified and untouched
[ ] Segment 1's report pre-generated and open in a tab
[ ] Screen share set to application/window, not full desktop
[ ] Only the tabs/windows this demo needs are open — no other customer
    accounts, no internal chat, no unrelated dashboards with real data on them
[ ] Notifications off, chat/mail closed
[ ] Meeting recording started before you begin sharing
[ ] Fallback clip/screenshots open in a tab, one switch away
[ ] Buddy briefed, has staging open, knows which segment to jump in on
[ ] Recovery line for "staging shows something weird" said out loud once beforehand
```

Skipped from the full stage checklist, deliberately, given this is internal and rough: adapters/mirroring tests, venue-resolution checks, USB deck copies, dedicated demo-only OS profile. None of those apply to a video call to your own colleagues. What I did **not** skip: the tab hygiene and record-selection items, because the data-exposure risk doesn't shrink just because the audience is internal.

## Rehearsal log

| Date | Run type | Time | Failures | Change made |
|---|---|---|---|---|
| ‹before Thu› | full cold run, screen-share mode on | | | |

Given the timeline, one full run-through — timed, in actual screen-share mode, using the real records you'll show — is the bar that matters here. The skill's full gate (three consecutive clean cold runs, a drill per top risk, an offline run, a venue-resolution run) is written for a stage where a bad run costs you in front of strangers; you explicitly don't need that ceremony for a rough internal walkthrough. The one thing not worth cutting: running it once, live, in the actual sharing mode, before Thursday — that's the run that catches "the real data does something weird" and "I shared the wrong window," which are your two most likely failure modes here.