# Portwell demo — root cause and the rebuild

## What actually killed the segment

The container failure itself is not the design flaw — containers fail. The flaw is that the failure cost 2:40 instead of ~20 seconds. Two independent design gaps stacked to produce that:

1. **The reset was not idempotent across state, only across screen.** Running the demo twice in the green room left a named volume behind (old data directory, old schema, a container name already bound to a port — the recording doesn't say which, but "stale volume" always means the same thing: something from run N survived into run N+1). Whatever reset command exists either wasn't run between the two green-room reps, or it stops/restarts containers without destroying their volumes. This is called out by name in the skill this runbook follows: *"the reset command, rehearsed from a cold machine — not from the machine that has already run the demo twice."* That's exactly the machine state you walked on stage with.
2. **There was no recovery rule.** When the container didn't come up, the default behavior was to debug it live, out loud, for 2:40. That's not a discipline failure — it's what happens when no fallback asset exists and no one-repair-then-switch rule was rehearsed. "Talking over yourself" is the sound of an unscripted decision being made in real time.

Fix both. Fixing only #1 means the next never-seen-before error (there will be one) costs another 2:40. Fixing only #2 means you'll be narrating a recorded clip at every event instead of ever showing Portwell live again.

## Fix 1 — reset that actually resets

Whatever your current reset does, it's leaving volumes intact. Replace it with one command that destroys and recreates everything, including volumes:

```bash
#!/usr/bin/env bash
set -euo pipefail
docker compose -f demo/docker-compose.yml down --volumes --remove-orphans
docker compose -f demo/docker-compose.yml up -d --force-recreate
until docker compose -f demo/docker-compose.yml exec -T app curl -sf localhost:PORT/health >/dev/null 2>&1; do
  sleep 1
done
echo "ready"
```

`down --volumes` is the one flag that was almost certainly missing. `--force-recreate` stops a stopped-but-not-removed container from silently reusing its old filesystem layer. The health-check loop replaces "looks like it's up" with a command that says so — that loop is what should have run in the green room instead of eyeballing it.

Pin this down before the next event:

- [ ] Reset script lives at a fixed path, is executable, and is bound to a hotkey or written on a sticky note.
- [ ] Images are pre-pulled and pinned to a version — `--force-recreate` should take low single-digit seconds, not trigger a pull.
- [ ] Reset is verified idempotent from a **dirty** state, not just a cold boot: run the full demo twice back-to-back with no manual cleanup, run reset, run the demo a third time, confirm run 3 looks identical to run 1. That drill is the one your rehearsal protocol was missing — a plain cold-boot test would never have caught this, because the bug only appears after a prior run leaves something behind.

## Fix 2 — a rule for the next unknown failure

You won't always be able to name the next bug in advance. You can always bound how long you'll fight it.

- **One repair attempt, ~20 seconds, then switch.** In practice: run the reset script once. If it isn't confirmed healthy by the time you'd finish saying the recovery line below, you're already switching — not starting a second attempt.
- **Fallback asset**: a recorded clip of this segment, embedded in the deck (not in a file browser you'd have to alt-tab to), one keystroke away. If this doesn't exist yet, record it this week — a 45–90 second screen capture of the segment running clean is the whole job.
- **Recovery line, written down and rehearsed out loud, not improvised**:
  > "That's a new one, and I'm not going to debug it at you — here's what it looks like when it behaves." *(switch to clip, keep talking over it as if it were live commentary)*
- **Rehearse the switch itself as its own drill**, separate from rehearsing the demo. Trigger the failure on purpose, time the switch, confirm it lands under 20 seconds. The 2:40 you lost was almost entirely the cost of never having run this drill — the failure itself would have cost seconds if a switch had existed to make.

## What to add to the runbook

```
Reset (one command):   ./demo/reset.sh   (down --volumes, up --force-recreate, health-checked)
Verified cold:         [ ] fresh boot   [ ] after 2 consecutive runs with no manual cleanup
Never on stage:        image pull, first-run migration, manual volume cleanup

Fallback for this segment: recorded clip, [duration], embedded on slide [n]
Recovery line: "That's a new one, and I'm not going to debug it at you — here's what it
                looks like when it behaves."
Repair budget: one attempt, ~20s (this skill's baseline — tune it, don't defend it as a rule),
               then switch. No second attempt.
```

Add one line to the pre-flight checklist that exists specifically because of yesterday:

```
[ ] Reset script run after every rehearsal rep, including green-room reps — never walk on
    stage from a machine that has run the demo more than once since the last reset.
```

## Before the next two events

- Rehearsal gate to clear before each: three consecutive clean cold runs, **plus** the dirty-state drill above, **plus** one timed drill of the container-failure switch. Three cold runs alone would not have caught yesterday's bug — it only shows up after a prior run, so the dirty-state variant is the one that matters here.
- Fill in and date the runbook header (claim, venue, budget, owner, last-verified) so it doesn't rot between now and event two — a runbook with no date is the failure mode that lets this exact bug come back unnoticed.
- If the two upcoming events have shorter green-room windows than yesterday's, that's an argument for rehearsing the reset+drill combination somewhere other than the green room the day before, not for skipping it under time pressure.

The 20-second repair budget and the three-clean-runs threshold above are this skill's own baselines, not published standards — adjust them to your slot, but don't skip the dirty-state drill specifically, since it's the one shaped like your actual failure.