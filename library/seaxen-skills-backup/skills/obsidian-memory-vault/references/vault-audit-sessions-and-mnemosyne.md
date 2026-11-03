# Vault audit: sessions + Mnemosyne vs Obsidian

When the user asks whether anything should be added to the vault, or after a major Hermes/Mnemosyne ops session.

## Sources (use both)

1. **`session_search`** — browse recent sessions; FTS may return empty for hyphenated or very new phrases — try `OR` queries, browse mode `session_search()` with no query, or scroll a known `session_id`.
2. **`mnemosyne_recall`** — hot memory, conversation captures, global insights (e.g. third-party evals). Not a substitute for vault canonicals.

Do not dump session transcripts into the vault.

## Gap checklist

| Signal in memory/sessions | Vault destination |
|---------------------------|-------------------|
| Major upgrade / verified fix | `Knowledge/<System> Operations.md` or `issues-fixes-log.md` |
| Durable decision contradicting old `decisions.md` | New decision entry **superseding** old intent (do not delete history) |
| Stale sizes/paths in `context.md` or Backup doc | Patch canonical with live `ls` / `mnemosyne stats` |
| Third-party eval (install deferred) | `Knowledge/<Name>.md` + `decisions.md` defer entry |
| User thermal / pacing preference | `preferences.md` if ops-related |

## Already covered elsewhere

- Mnemosyne pip/vec0/reindex detail → skill `sagar-hermes-ops` → `references/mnemosyne-upgrade-debian-pitfalls.md`
- Procedures → Hermes skills; vault holds **facts** and **routing** (bridge decision 2026-06-25)

## After audit writes

1. `Knowledge Index.md` + `AGENT.md` links for new Knowledge notes.
2. `Daily/YYYY-MM-DD.md` log line (append-only).
3. Ad-hoc verify: `scripts/vault-audit-verify.py` or curl recall for new note title.
4. Optional: run `scripts/mnemosyne_to_vault.py` if hot DB changed materially (mirror timestamp stale).

## Pitfall: stale canonical decisions

Example: `decisions.md` said "Mnemosyne sandbox only" while live config uses `memory.provider: mnemosyne`. Add a **new** dated decision that supersedes intent; link [[Mnemosyne Operations]].