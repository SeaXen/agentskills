# Getting stuck participants unstuck at Marlowe Devdays: ranked

I haven't seen the workshop content, so I assumed it needs a local setup (install, config, run). If it's browser-only, option 2 shrinks and option 1 matters even more.

**Do first: option 1, this week. It takes about 2 hours.**

## Ranking

| # | Option | Cost | Why this rank |
|---|---|---|---|
| 1 | Interview the instructor and build a failure-mode playbook | ~2h now | Her monthly runs are your best data. Everything below depends on it. |
| 2 | Remove setup failures: prebuilt environment plus a pre-flight check | Medium, one-off | Setup is usually the biggest cause of stuck people (my assumption, so ask her). |
| 3 | Checkpoints: one snapshot per step, with a skip-ahead path | Medium, one-off | A stuck person rejoins in 2 minutes instead of losing the session. |
| 4 | Visible help signal plus a 5-minute rule | Near zero | Stuck people stop waiting silently. The helper sees the queue. |
| 5 | Pair or trio seating, neighbors first | Zero | Peers resolve about half of the small problems before any helper is needed. |
| 6 | The extra person as a briefed floater | Your one budget slot | Without 1–4 they re-solve the same problems live. With them, one person is enough. |
| 7 | "You should see…" expected output after every step | Low, writing time | Stuck people can self-diagnose. It's cheap, but it only catches the failures you already know about. |
| 8 | Stuck log for the next edition | Near zero | Pays off from year 2, since you're running this annually. |

## What each one means

1. **Playbook.** Ask her three things:
   - What are the top 10 ways it breaks, and at which step?
   - What is the 60-second fix for each?
   - What does she wish participants had done beforehand?

   Output: a one-page sheet the helper carries.

2. **Environment.** Ship one standard setup (container or cloud dev environment) and a single check command. Participants run it the day before, and the helper runs it again at a setup desk 30–45 minutes before the session. Fix environment problems before the session starts, not during it.

3. **Checkpoints.** Give every step a tag or branch holding the correct end state. Rule: still stuck after 5 minutes means jump to the checkpoint and keep going. They lose one step, not the session.

4. **Help signal.** Use a red/green cup or card per seat. For remote help, add a chat channel. The rule: stuck for 5 minutes means flag it. Nobody has to ask permission.

5. **Pairing.** Seat people in pairs on purpose, and tell the room that asking your neighbor comes before flagging a helper. At 25–30 people, that cuts the queue a lot.

6. **Extra person.** One person can't cover 28 seats during live work alone, which is why options 2–5 come first. Choose someone who can fix problems, not just notice them. A previous attendee who is technically strong, or a colleague who has run the setup, both work. Brief them with the playbook and have them shadow one of her sessions, so you may need to decide this early. Keep the instructor at the front, and don't have her fix problems at seats.

7. **Expected output.** Add a short "you should see…" line after each step in the guide.

8. **Stuck log.** The helper tallies each incident as step number, cause, and time lost, on one sheet. In year 2 you start from data instead of memory.

## Suggested timeline (5 months)

- **Weeks 1–2:** Option 1. Draft options 4, 5 and 7 from it.
- **Months 1–3:** Build options 2 and 3. Test them on someone who has never seen the workshop.
- **Month 3–4:** Pick and brief the extra person (option 6). Have them shadow one commercial run.
- **Month 4–5:** Run a dress rehearsal with 5–8 testers. Fix the environment problems it exposes.
- **Event day:** Setup desk 45 minutes before, then live floater, with the log running (option 8).

## Questions that would change the ranking

1. Is the workshop local-install or browser/cloud-based? Local raises option 2's rank. Cloud lowers it.
2. Does she already have a failure list or a checkpoint repo? If so, options 1 and 3 get much cheaper.
3. Who is the candidate for the extra seat: a colleague, a hire, or a volunteer?