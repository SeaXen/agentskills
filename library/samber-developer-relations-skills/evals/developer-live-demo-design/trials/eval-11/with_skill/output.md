# Demo runbook — Grebe live migration reveal

## Assumptions I'm filling in for you (confirm with eng in week 1 — an unconfirmed field below is an untested assumption per the skill's own rule)

- Grebe's migration-writing step calls a model (local or hosted) to go from schema + intent → migration plan → execution. If it's actually deterministic/rule-based rather than model-backed, the network-dependency risk below shrinks a lot — tell me and I'll cut that mitigation.
- "Whatever schema" is scoped to relational DDL Grebe already supports (assume Postgres + MySQL) — not literally any schema in any format. Unscoped, the claim is unprovable and this skill's own rule applies: *"When a demo can only clear its claim by faking, the claim is wrong — narrow it."*
- The change applied to the drawn schema is chosen by you from a small set of patterns Grebe handles reliably (add column + backfill, add index, split table, widen a type) — the audience supplies the *schema*, not the *migration intent*. If Grebe is meant to also infer intent live from a spoken request, that's a second unscripted variable stacked on the first and roughly doubles the risk register below.
- Own event, own AV, own recording rights — no venue restriction on screen recording.
- Full engineering team = enough hands to run intake, a dedicated on-call fixer during the slot, and a buddy on stage.
- 20 minutes is a hard stop (fixed slot in a launch program), not flexible.

---

## Why tier 0, not the usual tier-3 default

This skill defaults to tier 3 (recorded screencast) and makes you earn anything below it. Grebe's demo is the named exception: *"Promote it [tier 0] anyway when the claim is the liveness itself: an audience-supplied input, a race the recording could be accused of faking, or a launch where 'we really ran this today' is the point."* That's exactly this brief — and the "cherry-picked" history means tier 3 doesn't just fail to prove the claim, it actively re-confirms the accusation you're trying to kill. Tier 2 (local but seeded) is out for the same reason: seeded fixtures are a schema you already know, which is the one thing the claim says isn't true here.

So: **tier 0-equivalent** — the schema is genuinely unknown until it's drawn, and the generation/execution pipeline runs live with no scripted outcome. The one part that *is* scripted (correctly, per tier 1) is the presenter's own actions: the command that kicks it off, the draw mechanism, the narration. You're not typing a migration by hand on stage — you're triggering a fixed sequence against a variable input. Fallback tier is 3: a full recorded run, disclosed as a recording if it's ever shown.

The trade-off, stated plainly: this is the most expensive, most rehearsal-hungry option on the ladder, and it is also the only one that answers the actual accusation. A clean tier-0 run in front of a room is worth more than any number of tier-3 recordings precisely because it's the thing people said you couldn't do. A failed tier-0 run in front of a room, with a bad recovery, actively confirms every doubt at once. Everything below exists to make the second outcome unlikely and the recovery from it non-humiliating.

---

## Header

```
Demo:          Grebe live migration reveal
Claim:         Grebe writes and safely runs a real schema migration, live, against
               a database schema drawn — unseen by anyone at the company beforehand —
               from schemas submitted by people in this room today.
Venue/format:  own launch event, stage, 20-minute fixed slot
Budget:        20:00 total slot  /  Measured: <fill after rehearsal>
Tier:          0 (unscripted live execution on unknown input)   Fallback tier: 3
Network:       offline for everything except one isolated, team-controlled,
               pre-tested link to the model endpoint (never venue Wi-Fi)
Data:          audience-submitted DDL only, pre-validated at intake; synthetic rows
               generated locally at draw time to match the drawn schema; zero
               production data, zero real customer schemas
Buddy:         <named engineer>, front row, laptop with cloned repo, deck PDF,
               and the fallback recording loaded and ready
Owner:         <DevRel/eng lead name>
Last verified: <date of last clean cold run>  on <Grebe build/commit>
Re-verify:     day before the event, and again if Grebe ships a change after that
```

---

## Segments

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 | The problem this replaces is slow/manual | recorded clip, loaded on slide | narrated screenshot | 45s | **yes** | already a static asset — nothing to fall back from |
| 2 | The schema is real, submitted by the room, unseen by us | live draw from the sealed submission pool | physical/on-screen draw + load by ID | 90s | no | pre-drawn backup ID from the same pool, drawn at the same moment behind the scenes (see below) |
| 3–5 (one atomic block) | Grebe writes the migration, runs it against a live seeded instance, and the data survives | fresh disposable DB container + warmed model connection | `grebe migrate --schema intake/<id>.sql --op <chosen-op> --target demo-db` | 5:00 | no | full recorded run of a genuinely blind-drawn schema from a rehearsal dry-run, disclosed as a recording |
| 6 | It isn't a fluke — second schema, second result | second fresh DB container | second draw, same command | up to 4:00 | **yes** — only attempted if time remains | none needed; it's the stretch segment itself |

**Why 3–5 is one block, not three independently-enterable segments:** the skill's rule is "no segment may depend on a previous segment's live output" — but generation, execution and verification here are one causal chain by construction (you can't execute a plan you haven't generated, and you can't verify an execution that didn't happen). Splitting them and pretending segment 4 has its own restore point independent of segment 3 would mean either faking segment 4's input or silently reusing a stale plan — both are worse than being honest that this is one unit with one fallback. What *is* independently enterable is segment 2 (the draw itself never depends on 3–5, and always succeeds — worst case it's a physical raffle drum and a spoken ID) and segment 6 (a second, fully separate instance of the same block).

Segment 2 precondition/expected/if-not, written for the speaker:

```
Segment 2  precondition: submission pool sealed 15 min before doors open, on-screen
                          counter showing N valid submissions, draw mechanism tested
           expected:     drawn ID's raw .sql file appears on screen, untouched,
                          with its public submission timestamp visible
           if not:       announce the backup ID (see below) — do not re-draw live,
                          a visible re-draw looks like a redo
```

Segment 3–5 precondition/expected/if-not:

```
Segment 3–5  precondition: DB container freshly reset, model endpoint warmed and
                            ping-tested in the last 5 minutes, synthetic-data
                            generator ready for the drawn schema's shape
             expected:     plan diff renders in <60s, execution completes with a
                            visible live write-counter still incrementing throughout,
                            verification query prints "0 failed writes"
             if not:       one repair attempt (retry the same call, ~20s cap), then
                            switch to the recorded fallback — recovery line below
```

---

## The draw mechanism — this is the credibility engineering, not the migration engine

Given the "cherry-picked" history, the *process that produces the input* has to be as auditable as the migration itself, or you've just moved the trust problem one step upstream.

- Submissions open via QR code at doors-open, close 15 minutes before the talk. One submission per badge, to stop pool-stuffing with an easy schema.
- Every submission is validated automatically **without anyone seeing its contents**: syntactically valid Postgres/MySQL DDL, under a size cap, DDL-only (reject anything containing `INSERT`/`COPY`/literal data — you're not vetting *which* schema goes in, you're vetting *that it's a schema*, which is hardening the setup, not the output).
- A live, public counter ("47 valid submissions") runs on a lobby screen before the talk — visible proof the pool existed and grew before anyone knew what would be drawn from it.
- On stage: an independent person the audience has reason to trust more than you do — a named external engineer, a community skeptic, whoever's plausible for your room — pulls the ID, not the presenter.
- Immediately after the event: publish the full unedited recording, the submission timestamps, and the demo harness code itself. The point isn't "trust us" — it's "here's how to check."
- **The backup ID for segment 2's fallback is drawn from the same sealed pool, at the same moment, by the same process** — not a pre-chosen "safe" schema. If the primary draw mechanism physically jams, you're still drawing blind, just from a second slip already in an envelope.

This is the one part of the runbook that exists specifically because of the reputational history in the brief, not because the base skill demands it — flagging that so it doesn't read as a generic checklist item.

---

## Fallback assets

```
00-pain-point.mp4        recorded, narrated screenshot of the manual process, slide 4
recorded-blind-run.mp4   a genuinely blind-drawn schema from a week-3 rehearsal
                          dry-run, timestamped, submission-pool evidence attached
                          on the same slide so the disclosure is visible, not buried
deck.pdf                 includes all key frames, on USB key and buddy's laptop
```

No fallback asset exists for the draw itself (segment 2) beyond the second sealed envelope — there is nothing to "play" for a live physical draw, which is correct; that segment's only failure mode is mechanical, not computational.

---

## Reset and pre-provisioning

```
Reset (one command):   ./grebe-demo reset        # tears down + recreates the DB
                                                  # container, reseeds nothing
                                                  # (seed happens post-draw), re-pings
                                                  # the model endpoint
Verified cold:         <fill after rehearsal>
Pre-provisioned:       Grebe binary/build pinned, DB images pre-pulled, model
                       endpoint connection warmed and kept alive (not established
                       cold on stage), synthetic-data generator warmed against a
                       range of schema shapes in advance, intake validator running
                       since doors-open
Never on stage:        installing anything, pulling an image, cold-starting the
                       model connection, first-run auth
```

The one thing this skill's checkpoint pattern assumes and this demo breaks: you cannot pre-seed the database, because you don't know the schema until segment 2. That means the synthetic-data generator that fills the drawn schema with plausible rows is itself now a load-bearing, must-rehearse-against-many-shapes component — put it through the same corpus-testing as Grebe itself (see rehearsal plan), because a generator that chokes on an unusual schema shape fails the demo before Grebe even starts.

---

## Recovery lines

Written out, not improvised:

- **Model endpoint fails / times out:** *"That call just came back empty — rather than stare at a spinner together, here's the same schema, drawn the same way, from a dry run we filmed last week. Same code, same process, and we'll tell you exactly when the tape starts."* → switch to `recorded-blind-run.mp4`, and say the words "this is a recording" out loud before playing it. Never let a recording run under live narration that implies otherwise — that's the exact failure mode the "cherry-picked" complaint was about.
- **Drawn schema breaks something Grebe genuinely can't handle:** *"That's a real gap, and I'd rather show it to you than hide it — that's [specific limitation] and it's on our list. Let's draw again from the same sealed pool so you can see it's not rigged."* Only use this if the failure is instructive and explainable in one sentence; otherwise switch straight to the recording.
- **Overrun going into segment 6:** *"We've got time for one more if the room wants it — otherwise the full recording's on our site tonight, unedited, timestamps and all."* — segment 6 is explicitly droppable; say so rather than silently cutting it.

One repair attempt, ~20 seconds, then switch — no second attempt live. A second visible retry reads as "it doesn't really work," which is worse than one clean switch to a disclosed recording.

---

## Pre-flight checklist

```
[ ] Machine plugged in, sleep/screensaver off, Do Not Disturb on
[ ] Demo profile only — no daily-driver accounts, mail, chat, calendar
[ ] Fresh browser profile, fixed tab set, extensions off
[ ] Shell history and editor recents cleared; custom prompt; clear run
[ ] Terminal 24pt+, editor 20pt+, high-contrast theme, verified from back row
[ ] Display at venue resolution/aspect ratio; mirroring tested; adapters tested
[ ] Model endpoint connection warmed and ping-tested in the last 5 minutes,
    over the team's own controlled link — not venue Wi-Fi, not a shared hotspot
[ ] Submission pool sealed; public counter frozen; backup envelope drawn and set aside
[ ] ./grebe-demo reset run once; DB container confirmed empty/fresh
[ ] Fallback recording loaded, one keystroke away, disclosure line rehearsed
[ ] Deck PDF on USB key and with the buddy
[ ] No production credentials, no real customer schema, anywhere on this machine
[ ] Share mode: application window, not full desktop; rehearsed on this platform
[ ] .env / any visible config holds placeholders only
[ ] Safe screen ready on a known hotkey; stop-sharing key known
[ ] Buddy briefed, seated front row, clone of everything on a working laptop
```

---

## Rehearsal plan across the 4 weeks (full eng team, so scale depth, not headcount waiting around)

**Week 1 — build the parts that don't exist in a normal Grebe demo yet.** Intake form + validator (DDL-only, size-capped, dialect-checked, one-per-badge). Synthetic-data generator that can seed *any* validated schema shape fast. Isolated, team-controlled path to the model endpoint that never touches venue infrastructure. Assemble a corpus of 50–100 real-world schemas (open-source projects, generated variety — weird types, circular FKs, huge tables, multiple dialects) to stand in for "the room" before the room exists.

**Week 2 — headless corpus runs, not stage rehearsal yet.** Run the whole pipeline against the corpus automatically, unattended, dozens of times. This is where you find the schema shapes that time out, the generator edge cases, the migrations Grebe writes but shouldn't run unattended. Fix the architecture, not the odds — a segment that fails on 1 schema in 20 needs a design change (tighter scoping of supported dialects, a faster timeout with a cleaner fallback trigger), not more rehearsal reps.

**Week 3 — first full dress rehearsals, at venue resolution, with genuinely blind draws.** Recruit colleagues *outside* the demo team to submit real schemas without telling you which. Run the actual on-stage sequence end to end, cold, from `./grebe-demo reset`. Film at least one of these as the disclosed fallback recording — and keep its submission-pool evidence, since that recording's credibility depends on it also being genuinely blind-drawn. Drill the top risks below explicitly: kill the model connection mid-run, feed a schema the validator should reject, force a timeout.

**Week 4 — freeze and go/no-go.** Code freeze on the intake pipeline except critical fixes. Final venue tech check: resolution, adapters, the actual isolated network link tested in the actual room (not the lobby). Buddy briefing. A leadership go/no-go checkpoint 48 hours out, explicitly checking the pass threshold below — given what a public failure would cost against a year of "cherry-picked" accusations, this decision point is worth naming out loud rather than assuming the calendar date decides it for you.

**Pass threshold before it goes on stage** (this skill's own designed gate — say so if anyone asks whether it's a published standard, it isn't):

- Three consecutive cold runs, reset-command-only, complete inside budget — across *different* drawn schemas each time, not the same one three times.
- The top three risks below have each been drilled: trigger it, switch, keep talking, under 20 seconds.
- One full run done with the model-endpoint link disconnected (proves the offline/isolated design actually holds).
- One full run done at venue resolution, read from the back of the room.
- At least 10 corpus schemas per dialect supported, not just the ones that happened to demo well.
- Measured time for the load-bearing block (segments 3–5) comes in under half its budget across those three cold runs.

If any of these doesn't hold four weeks in, the fix is a design change — narrow the supported dialects, cut segment 6 entirely, drop to a hybrid where the *schema* is audience-drawn but the *change request* is fixed to one proven pattern — not more rehearsal hours thrown at the same design.

---

## Risk register, ranked for this demo specifically

| Risk | Likelihood × visibility | Mitigation |
|---|---|---|
| Model/inference call fails, hangs, or is rate-limited mid-generation | high — this is the single largest risk in the whole demo | Isolated, team-controlled, pre-tested link (never venue Wi-Fi or a shared hotspot); hard client-side timeout tuned from corpus testing; one retry, then disclosed recorded fallback |
| Drawn schema is outside what Grebe actually supports (exotic dialect, unsupported type, malformed) | medium — this is exactly the input you can't control | Intake validator rejects unsupported input *before* it enters the pool, without anyone seeing which submissions were rejected or why — bounds the blast radius without touching who gets drawn |
| Someone submits a schema containing real data, secrets, or an embarrassing/hostile payload | medium, high visibility if it lands | Validator strips anything that isn't pure DDL; one-per-badge cap; explicit submission terms disclosed at intake ("this will be shown live and published") |
| Synthetic-data generator can't produce plausible rows for an unusual drawn shape | medium — new component, no track record yet | Corpus-test it as hard as Grebe itself in weeks 1–2; it's now a load-bearing dependency, not a helper script |
| Live migration completes but visibly loses writes or breaks the "safely" claim | low if the product actually works, catastrophic if it fires | Concurrent seeded writer process running throughout, visible on screen, so "zero failed writes" is checked live, not asserted; never filter the verification query's failure case out of the WHERE clause — that crosses into faking |
| Recovered-to recording gets mistaken for a second live run | medium, and it's the exact accusation you're trying to kill | Say "this is a recording" out loud before playing it, every time, no exceptions |
| Draw mechanism itself is questioned as rigged | medium, and undermines the whole point if unaddressed | Independent, non-employee draws it; public pre-talk submission counter; publish full unedited recording + timestamps + harness code afterward |
| Laptop or display dies | low, high visibility | Buddy in front row with full clone, ready to hand off |
| Segment 1 (context clip) overruns and eats into the load-bearing block | low | Segment 1 is explicitly droppable; cut it first if running behind |

---

## Hardened vs. faked, applied to this demo specifically

```
Hardened — keep                        Faked — never ship
--------------------------------      --------------------------------
Pre-validating submissions for        Pre-selecting which valid
syntax/size/dialect without ever      submission gets drawn, or
seeing which one gets drawn           quietly re-running a failed
                                       draw until one "works"

An isolated, team-controlled,         Claiming the model call ran
pre-tested link to the model          over venue Wi-Fi when it
endpoint                              actually ran over a private,
                                       undisclosed backchannel

A verification query that checks      A verification query with the
real write counts against a live      failure case filtered out of
concurrent writer                     the WHERE clause

A disclosed recorded fallback,        The same recording played
announced as a recording before       while the presenter narrates
it plays                              it as if still live

Publishing the unedited recording     Publishing a recording that
and the harness code afterward        cuts the one run that struggled
```

The test from the skill applies directly here: if someone in the room asks "was that schema really unseen by you before now?", every design choice above has to survive being answered "yes, and here's the log that proves it." Anything that can't survive that question is faking, and given the specific accusation you're already fighting, getting caught once here costs more than never having done it live at all.