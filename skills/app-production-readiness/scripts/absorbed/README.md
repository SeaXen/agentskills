# Absorbed scripts

These scripts were **copied** from sibling skills in `D:\Repo\.agents\skills` so
that `app-production-readiness` can run them on its own.  They are not
re-implementations: each file records the sha256 of the original it came from
in `MANIFEST.json`, so drift is detectable instead of silent.

**The sibling skills are optional.**  Everything in this folder is a copy: if
`D:\Repo\.agents\skills` is deleted, every gate of `app-production-readiness` still
runs unchanged.  `verify_manifest.py` reports *"original not found (kept the
absorbed copy)"* in that case, which is a healthy state, not drift.

| File | Came from | Used for |
|------|-----------|----------|
| `ux_audit.py` | `frontend-design` | Gate C - design polish rubric (extra signal) |
| `accessibility_checker.py` | `frontend-design` | Gate S - assistive-technology contract |
| `mobile_audit.py` | `mobile-design` | Gate A+ - native mobile compliance |
| `i18n_checker.py` | `i18n-localization` | Gate R - i18n / RTL |
| `api_validator.py` | `api-patterns` | Gate N - API contract |
| `schema_validator.py` | `database-design` | Gate P - schema validity |
| `seo_checker.py` | `seo-fundamentals` | Gate G - static SEO (`../seo_static.py`) |
| `geo_checker.py` | `geo-fundamentals` | Gate G - generative-engine readiness (`../seo_static.py`) |
| `lint_runner.py` | `lint-and-validate` | Gate U - lint |
| `type_coverage.py` | `lint-and-validate` | Gate U - type coverage |
| `react_performance_checker.py` | `nextjs-react-expert` | Gate U - React render performance |
| `lighthouse_audit.py` | `performance-profiling` | Gate D - fallback Lighthouse runner |
| `test_runner.py` | `testing-patterns` | Gate H - fallback test-command detection |
| `vulnerability_security_scan.py` | `vulnerability-scanner` | Gate E - second, independent security scanner (see *Declared patches*) |

Two files in this folder are **skill-owned tooling**, not copies:
`verify_manifest.py` (integrity verifier) and `refresh_manifest.py` (re-pinning
tool).  They are excluded from the manifest on purpose - they are what checks
the manifest.

> `vulnerability_security_scan.py` is the `vulnerability-scanner` skill's
> `security_scan.py` under a different file name, so that this skill has only
> one `security_scan.py`.

Three copies that used to live here were **removed** because they added nothing:
`playwright_runner.py` (it needs the same Playwright package as
`../capture_screenshots.py`, so it was never a fallback), and `quick_validate.py` +
`package_skill.py` (the working equivalent is `../skill_check.py`, which also
validates the frontmatter and packages the skill).  Removing them keeps the
folder honest: everything left in it is actually wired into a gate.

## Why the copies stay close to their originals

The gate scripts in this skill (`../design_polish.py`, `../code_quality.py`,
`../i18n_check.py`, ...) own the *judgement*: they decide pass/fail and they
are the thing you can fix.  The absorbed scripts contribute a second,
independent opinion, and they stay close to their source so:

* the behaviour is exactly what the source skill promised
* `verify_manifest.py` can prove nothing drifted silently
* a future update to the source skill can be re-copied without review

## Declared patches

Sometimes an absorbed copy must be hardened locally - a scanner that misses a
credential format, a directory that must not be scanned.  A local edit used to
be indistinguishable from drift: the manifest only modelled byte-identity, so
any intentional change broke `skill_check.py` and seven tests.

The manifest now models the patch explicitly.  A patched entry looks like this:

```json
{
  "file": "vulnerability_security_scan.py",
  "sha256": "<hash of the file in this folder>",
  "bytes": 18275,
  "identical_to_source": false,
  "upstream_sha256": "<hash of the original it was patched from>",
  "patch_reason": "<why the local edit exists>"
}
```

`verify_manifest.py` then checks two things:

1. the file in this folder still matches its own `sha256` (the patch is intact), and
2. the original on disk still matches `upstream_sha256` - if the upstream file
   changed since the patch was applied, the verifier reports a **warning**
   ("rebase the patch"), not a failure.

A patch is therefore never silent: it is declared, justified and re-checkable.

## Re-pinning after an edit

```bash
# a copy was edited on purpose - declare the patch and its reason
python scripts/absorbed/refresh_manifest.py --file vulnerability_security_scan.py \
    --reason "why the local edit exists"

# the copy matches its upstream again - drop the patch record
python scripts/absorbed/refresh_manifest.py --file vulnerability_security_scan.py --drop-patch

# re-pin every declared patch at once (e.g. after a bulk re-copy)
python scripts/absorbed/refresh_manifest.py --all --reason "re-copied from upstream"
```

`--reason` is mandatory unless `--drop-patch` is given: an undeclared patch is
the failure mode this tooling exists to prevent.

## Integrity

```bash
python scripts/absorbed/verify_manifest.py            # human readable
python scripts/absorbed/verify_manifest.py --json     # machine readable
```

Exit `0` = every file still matches its recorded sha256 (declared patches
included), `1` = drift, `2` = the manifest itself is missing.

## Editing policy

Do **not** edit the files in this folder without saying so in the manifest.
If a rule needs to change, change the gate script that calls it, or update the
original skill and re-copy it.  When you do edit a copy on purpose, declare it
with `refresh_manifest.py` and give a `patch_reason` - an undeclared edit is
drift, and `verify_manifest.py` will say so.
