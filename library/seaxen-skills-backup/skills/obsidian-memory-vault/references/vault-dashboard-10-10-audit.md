# Obsidian vault/dashboard 10/10 audit pattern

Use this when the user asks whether the Hermes Obsidian memory vault or dashboard is actually improving memory, or asks for a “10/10” judgment.

## Principle
Do not rate the vault from aesthetics or `/api/memory-health` alone. A useful vault must pass four layers:

1. **File reality** — vault path exists, canonical files exist, note/link counts are sane, no broken links, no duplicate headings, no stale test notes.
2. **Dashboard runtime** — systemd service enabled/active, port listening, root and core APIs return 200, browser has no JS errors.
3. **Recall quality** — `/api/recall-eval` has Hit@K 1.0 **and** MRR 1.0, plus real-query stress tests put the right canonical note at top-1.
4. **Memory hygiene / workflow** — review queue is clean/actionable, generated projection notes do not create review-candidate spam, backup/sync/watchdog jobs report honestly.

## Required live checks

Run or equivalent:

```bash
systemctl --user is-enabled obsidian-vault-dashboard.service
systemctl --user is-active obsidian-vault-dashboard.service
ss -ltnp | grep ':6065'
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6065/
curl -s http://127.0.0.1:6065/api/graph
curl -s http://127.0.0.1:6065/api/memory-health
curl -s http://127.0.0.1:6065/api/memory-candidates
curl -s http://127.0.0.1:6065/api/recall-eval
```

Then run representative `/api/recall?query=...` probes for:
- dashboard/design decisions
- fixes/root causes
- vault path/setup
- user preferences
- medical-study workflow
- WordPress style
- port conventions
- memory architecture
- a noise query such as `Say only OK.`

## 10/10 acceptance bar

Call it 10/10 only if all are true:

- broken links = 0
- orphans = 0 or intentionally explained/excluded
- duplicate heading groups = 0
- pending review candidates = 0 or all are valid/actionable
- `/api/recall-eval`: Hit@K = 1.0 and MRR = 1.0
- real-query stress test: important practical queries return the correct canonical note at rank 1
- Review tab renders actual candidate rows/actions, not just placeholder counters/headings
- Cron tab does not contradict backend state (e.g. mirror job OK while dashboard says mirror unknown/files 0)
- generated mirror/projection notes are excluded from memory-review candidates
- secret/key-like strings in mirror/projection notes are redacted
- backup repo privacy and sync are verified if the vault is git-backed

## Common non-10/10 findings

- **High health score but MRR < 1.0:** recall finds the right note but not first; useful, not perfect.
- **Hit@K 1.0 with bad top-1 examples:** do not hide this behind “all hits.” Report the rank misses.
- **Generated notes polluting review queue:** `Knowledge/Mnemosyne Mirror.md` and `Knowledge/Mnemosyne Triples.md` are projection/source notes; they should generally be in skip paths or otherwise prevented from producing durable-memory candidates.
- **Dashboard Review tab visually empty:** API may have candidates while UI shows only headings/dashes; call this a dashboard bug, not a healthy queue.
- **Cron mirror mismatch:** if `mnemosyne-to-vault-mirror` ran and mirror files exist but Cron tab reports mirror unknown/files 0, the dashboard status parser is incomplete or looking at the wrong state file.
- **Private repo is not a redaction policy:** a private GitHub vault still should not contain raw or partial API keys in generated notes.

## Rating language

Be blunt and numeric:
- 10/10 = all acceptance checks pass.
- 9/10 = structurally clean, top-1 recall almost perfect, review queue clean, minor UI polish only.
- 8/10 = useful and worth keeping, but recall/review/UI integration has measurable misses.
- <7/10 = unreliable as a memory aid; fix recall or hygiene before trusting it.

Always separate:
- **Does it help Hermes memory?** usually yes if recall + canonical notes work.
- **Is it Hermes’ automatic memory?** only if active integration/plugin/recall injection is actually enabled; otherwise it is a strong supporting memory layer, not seamless hot memory.
