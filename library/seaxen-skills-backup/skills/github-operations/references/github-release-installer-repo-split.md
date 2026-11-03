# GitHub release installer repo-split check

Use this when a project's docs/repo/install flow does not line up cleanly.

## Pattern
A public docs page or source repo can point to one GitHub org/repo while the shipped install script actually downloads release artifacts from a different repo owner via an internal default such as:

```bash
REPO="castai/kimchi"
```

This can make the project look inconsistent unless you inspect the installer body directly.

## Verification recipe
1. Read the installer script body, not just the one-line `curl | bash` snippet.
2. Check any embedded repo selector/default such as `REPO=...` or `*_REPO_OVERRIDE`.
3. Compare:
   - docs repo owner
   - public source repo owner
   - release artifact owner used by installer
4. Verify release/auth endpoints separately from CLI UX.

## Kimchi example
Observed split:
- Docs/source repo presented as `getkimchi/kimchi`
- Installer defaulted to `castai/kimchi`

Operationally this explained why docs/repo identity and installed artifact source looked mismatched.

## Practical lesson
When a CLI installs correctly but auth/model discovery behaves oddly, separate these layers:
- installer/release source
- saved config/API key state
- backend endpoint validity
- CLI UX/state machine

Do not collapse them into one diagnosis.