# Existing-repo push mode + credentials-scan false positives

Session-specific detail from 2026-08-22 backup run, extending `github-skills-library-backup`.

## User already has a backup repo: SeaXen/skills-backup

- Private, branch `main`, ~72 MB as of 2026-08-21 snapshot (231 repos, ~345MB, 24,437 files).
- When the user says "git push all changes" / "backup again", do NOT create a new repo. The user corrected this on 2026-08-22 by supplying the existing URL after an agent had already run `gh repo create`.
- Correct sequence:
  1. Stage per SKILL.md Stages 1–2.
  2. `git remote add origin https://github.com/SeaXen/skills-backup.git`
  3. `git fetch origin main --depth=1` — read the last commit message; it encodes what the previous snapshot held and is the changelog convention.
  4. Choose push mode — ASK THE USER:
     - **force-push**: replace history entirely with today's snapshot. Right choice after a mass trim that supersedes old content (e.g. repo clones stripped to skill files only).
     - **append commit**: add today's state as a new commit on top of prior history, preserving rollback.
- A background force-push was BLOCKED pending user consent on 2026-08-22 ("Silence is not consent"). Overwriting an existing remote requires foreground approval; never retry around the block.

## Credentials-scan false positives observed

The Stage 1 scan (`find ... -name 'credentials*'`) hits these benign paths on SeaXen's box:

| Path | What it actually is | Verdict |
|---|---|---|
| `learnables/deepseek-harness/packages/credentials/` (+ `credentials/`, `credentials-local/`) | README docs describing a credential-service architecture (dsh-credentials) — no secrets | safe, do not block |
| `**/.env.example` (several under antigravity-awesome-skills, huggingface-skills) | Template env files with placeholder keys | safe |

Rule: inspect file contents before treating a hit as a blocker; only real `.env` / `*.pem` / `*.key` / `credentials.json` with live values warrant the STOP-and-ask flow.

## Real >50MB offender found in this audit

- `research/crypto-research-alerting/browser_dashboard.log` — ~90 MB runtime log. The canonical `--exclude=*.log` rsync flag strips it automatically; staged tree dropped from 569 MB source to 365 MB.

## Post-trim library shape (context for future backups)

After the 2026-08-22 learnables trim:
- `/root/.hermes/skills/` = ~569 MB, ~27.5k files
- `learnables/` = 403 MB, 255 entries, every entry has a real SKILL.md body
- 11 former stub skills were fully re-learned from upstream sources (agent-agnostic bodies)
