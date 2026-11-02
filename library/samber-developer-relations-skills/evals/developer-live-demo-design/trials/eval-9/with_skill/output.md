## Short answer

Mostly sound — pre-staging the account, the CLI auth, and the project is exactly right. That's this skill's core rule in practice: **harden the setup, never the output.** You're not fabricating anything by skipping install/login on stage; you're removing variance nobody needed to watch.

But "log in beforehand, then show three commands" isn't a full plan — it's a tier choice with no fallback behind it. At 10 minutes in front of 40 people, one stuck command with no exit costs you a third of the slot. Two gaps to close before this is demo-ready:

- ⚠️ **No fallback.** If a command errors, hangs, or the venue Wi-Fi does something venue Wi-Fi does, your options right now are "debug it live" or "abandon the demo." Neither is a plan.
- ⚠️ **No claim.** "Three interesting commands" isn't what the audience should believe afterward — it's what you're going to type. Without a one-sentence claim, you have nothing to cut when the clock slips, and nothing to tell you which command is droppable if one runs long.

Everything else below is fixing those two things, sized for a meetup, not inflated into conference-grade ceremony — no sandbox tenant, no compliance review, no speaker buddy. Hobbyists and students aren't auditing your security posture; they're asking "can I run this tonight."

## The plan, closed

**Claim** — fill this in, one sentence: what should someone believe about Tinderbox after 10 minutes that they didn't believe walking in? "Three commands" is the mechanism, not the claim. If one of the three commands is *creating* a project, don't pre-create it — that would hide the exact thing you're trying to prove.

**Tier: 1** (live execution, pasted input), not raw live typing. Your claim doesn't need "watch me type it from memory" — it needs the commands to run for real. Script them into a file you paste from. You lose nothing an audience of devs cares about, and a dropped flag or a fumbled path stops being a risk at all. Fallback tier if a command hard-fails: 3, a ~60-second screen recording of the same three commands, made this week.

**Segments** — one per command, each independently enterable so a failure in command 2 doesn't strand commands 1 and 3:

| # | Proves | Enter from | Budget | Droppable | Fallback |
|---|---|---|---|---|---|
| 1 | *(what command 1 demonstrates)* | pre-authed CLI, project already created | ~60–90s | no | recorded clip, segment 1 |
| 2 | *(what command 2 demonstrates)* | its own restore point — not "command 1 just ran" | ~60–90s | maybe | recorded clip, segment 2 |
| 3 | *(what command 3 demonstrates)* | its own restore point | ~60–90s | yes | screenshot of expected output |

3 × 90s = 4.5 minutes of execution inside a 10-minute slot — comfortable, leaves room for narration and questions. Target measured time in rehearsal under 5 minutes total; that's this skill's own half-budget baseline, not a rule, but it's the margin that absorbs one hiccup without eating your Q&A.

The "own restore point" line is the part your current plan skips: if command 2 depends on command 1 having just succeeded, one failure takes out two-thirds of your demo. Check now whether that's true. If it is, either reset state between commands (a project snapshot, a seeded second project) or reorder so each command can be entered cold.

**Reset** — one command, run once before you go on, idempotent. If you're going to rehearse this more than once (you should — see below), you need to get back to "logged in, project created, nothing run yet" without replaying the whole setup by hand each time.

**Recovery line** (write it, don't improvise it): *"That's not behaving — here's what it looks like when it does,"* then switch to the clip and keep talking. One repair attempt, ~20 seconds, then switch — don't debug a stranger's terminal error live for a room of 40 people.

**Pre-flight, trimmed for a meetup** (skip the tenant/compliance items — not your audience):

```
[ ] Terminal 24pt+, high-contrast theme, block cursor
[ ] Do Not Disturb on; chat, mail, calendar quit
[ ] Shell history cleared, clear run, custom prompt (no personal path/hostname)
[ ] CLI session confirmed still authed (tokens can expire between rehearsal and showtime)
[ ] Reset run once; state confirmed clean
[ ] Fallback clip open or one keystroke away
[ ] Venue Wi-Fi tested in the actual room, or hotspot paired as backup — only if any command calls out to a hosted service
```

## One thing to nail down

ℹ️ "Account already logged in" implies at least one command talks to a hosted service, not a fully local stack. That's the one dependency your pre-staging doesn't protect against — a flaky meetup router can still kill the demo. If you can, test the room's Wi-Fi ahead of time or carry a hotspot; either way, that's exactly what the recorded fallback for segment 1 is insurance against. If everything actually runs local/offline, ignore this — you're already at the safest tier for a meetup.

Run the three commands cold, end to end, twice before the night. That's the whole test: does it complete inside 5 minutes with no manual fixing, and does each command survive being entered on its own. If yes, you're done — this doesn't need more than that for a 10-minute meetup slot.