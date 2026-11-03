# Hermes `no_agent` cron success notifications

Problem shape:
- A cron job shows `last_status: ok` and the underlying script succeeds, but the Discord/Telegram channel receives no message.
- Common with backup/watcher jobs that use `script=...` and `no_agent=True`.

Core rule:
- In Hermes cron `no_agent=True` mode, **stdout is the delivered message**.
- **Empty stdout means silent success**.
- Non-zero exit or stderr-triggered failure surfaces as an error alert, but a clean `exit 0` with no stdout posts nothing.

Diagnostic sequence:
1. Confirm the cron job uses `no_agent: true`.
2. Check `deliver` target matches the intended channel/thread.
3. Inspect the script itself for `print(...)` / stdout behavior.
4. Run the script manually.
   - If `EXIT=0` and `STDOUT_BYTES=0`, the missing notification is explained.
5. Patch the script to print a concise success line on successful completion.

Good success message shape for backup jobs:
- status emoji/text
- artifact filename
- size
- hash or short hash
- retention count
- optional timestamp if the filename does not already encode it

Example output:
```text
Mnemosyne backup OK | file=mnemosyne-backup-2026-05-30_19-07-49Z.sqlite.gz | size_mb=0.43 | sha256=3eaf93322b195d17aa4365df257c1286a328ef253d7cb045128911e152e0bdba | kept=14
```

Practical lesson:
- `last_status: ok` proves the job ran successfully.
- It does **not** prove a human-visible notification was sent.
- For operator-facing backup channels, default to emitting a compact success line rather than relying on silent success semantics.
