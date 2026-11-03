# Deterministic formatting for recurring backup cron notifications

Problem shape:
- A recurring backup cron job already has a stable machine-readable producer (`SAVED ...`, `PRUNED ...`, `LABEL=...`, `SIZE_BYTES=...`) but the visible Discord post is ugly, noisy, or model-variable.
- The existing cron may use an LLM prompt only to reformat the backup script output.

Preferred fix:
- Replace the formatting-only agent cron with a small wrapper script and run it via `no_agent=True`.
- Keep the real backup script unchanged.
- Let the wrapper:
  1. execute the real backup command
  2. capture stdout/stderr
  3. parse stable lines (`SAVED`, `PRUNED`, `KEY=VALUE`)
  4. convert bytes to human size
  5. print the final Discord-ready markdown directly

Why this is the better default:
- no model-format drift
- no raw `KEY=VALUE` dump in the channel
- deterministic success/failure formatting
- easier mobile scanning
- simpler to verify locally before attaching it to cron

Good backup-channel message shape:
- strong success/failure header
- archive filename
- human-readable size (MiB/GiB)
- file count
- SQLite snapshot count if relevant
- saved destinations
- prune summary

Example output shape:
```md
## ✅ Hermes Daily Core Backup
`SUCCESS`

**Archive:** `hermes-daily-core-backup-2026-05-31_08-40-42.tar.gz.gpg`
**Label:** `daily-core`
**Size:** 536.29 MiB (0.52 GiB)
**Files:** `3735`
**SQLite snapshots:** `7`

**Saved to**
- `/path/one`
- `/path/two`

**Pruned**
- `/dest/one` → `old-backup.tar.gz.gpg`
- `/dest/two` → `old-backup.tar.gz.gpg`
```

Implementation notes:
- If the underlying command fails, print a compact failure block with exit code and a short output tail.
- For recurring operator posts, prefer direct stdout emission from the wrapper over an LLM post-processor.
- This pattern applies when the source output is already structured enough to parse reliably.
