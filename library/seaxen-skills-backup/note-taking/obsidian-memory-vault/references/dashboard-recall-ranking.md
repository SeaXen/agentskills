# Dashboard Recall Ranking

Use this when tuning Obsidian dashboard recall quality without bloating Hermes prompt memory.

## Scope

Target file:

- `/mnt/tb/hermes/obsidian_dashboard.py`

Primary function:

- `query_hybrid_recall()`

## Safe change pattern

Prefer small ranking patches over rewrites.

1. Keep existing hybrid signals intact.
2. Add narrow intent detection for memory-critical classes:
   - decision
   - fix / root-cause
   - setup / config / path
   - preference
3. Add modest boosts for canonical note families:
   - `Memory/decisions.md`
   - `System/Assistant/issues-fixes-log.md`
   - `Work/Obsidian Vault Setup.md`
   - `AGENT.md`
   - `System/Assistant/environment.md`
   - `System/Assistant/preferences.md`
4. Add low-information-query suppression so trivial prompts do not emit recall.
5. Do not overfit broad browsing queries like `dashboard` — optimize memory-critical retrieval first.

## Validation

After patching:

1. `python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py`
2. restart `obsidian-vault-dashboard.service`
3. verify `/api/recall` on representative queries:
   - decision query
   - fix query
   - setup query
   - preference query
   - noise query (`Say only OK.` or equivalent)
4. run fresh `hermes chat -Q` for:
   - one targeted recall query
   - one noise/leakage query

## Expected good outcomes

- decision queries rank `Memory/decisions.md` above generic dashboard notes
- fix queries rank `System/Assistant/issues-fixes-log.md` first
- setup queries rank setup/environment notes first
- preference queries rank `System/Assistant/preferences.md` first
- trivial/noise queries return no recall results

## Pitfalls

- Do not rewrite the whole recall engine just because top-1 is imperfect.
- Do not boost note families so hard that normal browsing becomes useless.
- Do not judge success only by `/api/recall`; verify fresh Hermes chat too.
- If plugin-backed Hermes recall already calls `/api/recall`, dashboard-service restart is enough for ranking updates; Hermes gateway restart is not automatically required.
