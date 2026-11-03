# Hermes TUI over SSH + secret redaction

## TUI input appears dead over SSH

Use this when Dr. Sagar reports that Hermes TUI opens over SSH but typing does nothing.

### Fast classification
1. Verify whether the problem is the Hermes TUI itself or the SSH terminal/PTY path.
2. Launch `hermes --tui` in a real PTY on the host and inject a short string like `hello`.
3. If the text appears in the TUI input area, treat the server-side TUI as healthy and pivot to SSH/client diagnosis.

### High-yield causes
- No real TTY allocated (`ssh host "hermes --tui"` instead of `ssh -t host` then run Hermes interactively)
- Remote/editor terminals with weak raw-mode support (VS Code Remote SSH, Cursor terminal, browser SSH, some embedded terminals)
- Stale terminal state after a crash (`reset`, `stty sane`)
- tmux/screen/TERM mismatch

### Practical operator answer
- Say plainly when the TUI works locally and the likely fault is the SSH terminal path.
- Ask for `tty`, `$TERM`, and Python `isatty()` output from the broken session.
- Ask which client is in use: normal terminal, VS Code, Cursor, browser SSH, PuTTY, etc.
- Offer `hermes --cli` or plain `hermes` as the immediate workaround if the host config already defaults to CLI.

## Secret redaction for Dr. Sagar

### Preference
Dr. Sagar wants Hermes secret redaction enabled by default.

### Meaning of the warning
If `security.redact_secrets` is false, Hermes may print secrets verbatim in chat output, session JSON, and logs.

### Correct action
Enable with:

```bash
hermes config set security.redact_secrets true
```

Then start a fresh session or restart the relevant Hermes process.

### Important caveat
Turning redaction back on protects future output only. It does not scrub already-written logs or prior session history, so previously exposed tokens may still need rotation.
