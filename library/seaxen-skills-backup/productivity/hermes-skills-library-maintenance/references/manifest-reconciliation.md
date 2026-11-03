# Manifest reconciliation — full reference

## When the manifest drifts

The ledger file is `~/.hermes/skills/learnables/_verbatim-manifest.json`. It maps
each repo to its summary card status and verbatim leaf count.

Three sources of drift:

1. **Pre-schema adoption**: learnables created before the manifest schema was in use
2. **Renames/merges**: a repo dir like `headroom-hermes-integration` gets renamed to
   `headroom`. The manifest keeps the old key; the dir is gone.
3. **Missed commits**: a prior batch commit missed updating the manifest.

## Detecting drift

```bash
python3 ~/.hermes/skills/productivity/hermes-skills-library-maintenance/scripts/reconcile_manifest.py
```

Sample output (drift case):

```
Disk summary cards: 184
Tracked in manifest: 163
Untracked: 22  Orphans: 1  No-card: 0

== UNTRACKED (will be added) ==
  + caveman  (7 verbatim leaves)
  + rtk  (12 verbatim leaves)
  ...

== ORPHANS (will be REMOVED — ls-verified missing) ==
  - headroom-hermes-integration
      NOTE: case-mismatch? Found similar: ['headroom']
```

## Applying

```bash
python3 ~/.hermes/skills/productivity/hermes-skills-library-maintenance/scripts/reconcile_manifest.py --apply
```

The script:
1. Adds each untracked entry with `{summary_card: True, verbatim_count: N, verbatim_skills: [...]}`
2. Removes each orphan **only after** showing similar dir names to catch case-mismatches
3. Writes the manifest back

## After reconciliation

```bash
# Verify
python3 -c "import json,os; m=json.load(open(os.path.expanduser('~/.hermes/skills/learnables/_verbatim-manifest.json'))); d=[x for x in os.listdir(os.path.expanduser('~/.hermes/skills/learnables')) if not x.startswith('_') and os.path.exists(os.path.expanduser(f'~/.hermes/skills/learnables/{x}/SKILL.md'))]; print('manifest:', len(m['repos']), 'disk:', len(d), 'drift:', set(m['repos'])^set(d))"
# expect: drift: set() (empty)
```

## Why this matters

When the manifest drifts, anything that reads it under-counts. The INDEX.md
reads the disk directly so it's fine, but the bookkeeping ledger used for
auditing and bulk operations lies. Drift compounds — fix as soon as you notice.
