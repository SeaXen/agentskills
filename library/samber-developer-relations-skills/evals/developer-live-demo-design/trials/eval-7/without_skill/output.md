Fix root cause. Isolate rehearsal from live run. Add recovery drill. Skip live troubleshoot entirely — never debug on stage.

## Root cause

Stale volume from green-room rehearsal broke live container. Rehearsal and live shared same environment, so rehearsal left dirty state behind.

## Fixes, in order of impact

1. **Wipe environment after every rehearsal.** `docker compose down -v` (kill containers + volumes) right after green-room run, before walking to stage. One command, ~5 sec.
2. **Script a hard-reset command you can run live, no thinking.** One line: `docker compose down -v && docker compose up -d`. Bind it to a terminal alias or snippet (e.g. `demo-reset`). If container fails on stage, run this once, no diagnosis attempt.
3. **Set a 20-second failure clock.** Decide now: if container not healthy 20 sec after `demo-reset`, abandon and cut to slides. Say it out loud to yourself in rehearsal so it's reflex, not a decision made live.
4. **Rehearse the failure path, not just the happy path.** Once before each event: deliberately leave a stale volume, run the talk, hit the bug, execute `demo-reset`, recover. Muscle memory beats improvisation.
5. **Pre-warm a fallback: recorded screen capture of the working demo**, cued up and ready to play if reset also fails. Second-layer safety net, costs one export, saves the talk if #2 fails too.

## What NOT to do

Never debug live (read logs, `docker ps`, guess at fixes) in front of audience. That's what cost you 2:40 — diagnosis time, not fix time. Reset-or-abandon removes diagnosis entirely.

Next: add `demo-reset` alias to your talk repo's README now, so it's there before event 1.