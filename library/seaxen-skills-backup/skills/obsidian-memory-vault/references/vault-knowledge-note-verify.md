# Vault knowledge note — ad-hoc verification

After `Knowledge/<Topic>.md` + index/AGENT/daily updates:

1. Samefile: `/mnt/tb/hermes/obsedianvault` vs `/root/.hermes/obsedianvault` (`stat -c '%i'`).
2. No `^\s*\d+\|` line artifacts in markdown.
3. `GET :6065/api/recall?query=<Topic>&limit=3` — top hit = new note (`?query=` not `?q=`).
4. One daily log line when user asked to add/learn.

Use `/tmp/hermes-verify-vault-*.py` if needed; delete after. **Ad-hoc only**, not CI green.

Pair with `mnemosyne_remember` for global hot recall when user says "learn this".