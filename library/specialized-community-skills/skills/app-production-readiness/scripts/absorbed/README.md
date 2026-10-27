# Absorbed scripts

These scripts were **copied verbatim** from sibling skills in
`D:\Repo\.agents\skills` so that `app-production-readiness` can run them on its own.
They are not re-implementations: every file here is byte-identical to its
original (the sha256 of each is recorded in `MANIFEST.json`).

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
| `vulnerability_security_scan.py` | `vulnerability-scanner` | Gate E - second, independent security scanner |

> `vulnerability_security_scan.py` is the `vulnerability-scanner` skill's
> `security_scan.py` under a different file name, so that this skill has only
> one `security_scan.py`.  The sha256 in `MANIFEST.json` still proves it is the
> unmodified original.

Three copies that used to live here were **removed** because they added nothing:
`playwright_runner.py` (it needs the same Playwright package as
`../capture_screenshots.py`, so it was never a fallback), and `quick_validate.py` +
`package_skill.py` (the working equivalent is `../skill_check.py`, which also
validates the frontmatter and packages the skill).  Removing them keeps the
folder honest: everything left in it is actually wired into a gate.

## Why verbatim

The gate scripts in this skill (`../design_polish.py`, `../code_quality.py`,
`../i18n_check.py`, ...) own the *judgement*: they decide pass/fail and they
are the thing you can fix.  The absorbed scripts contribute a second,
independent opinion, and they are kept byte-identical so:

* the behaviour is exactly what the source skill promised
* `verify_manifest.py` can prove nothing drifted
* a future update to the source skill can be re-copied without review

## Integrity

```bash
python scripts/absorbed/verify_manifest.py            # human readable
python scripts/absorbed/verify_manifest.py --json     # machine readable
```

Exit `0` = every file still matches its recorded sha256, `1` = drift, `2` =
the manifest itself is missing.

## Editing policy

Do **not** edit the files in this folder.  If a rule needs to change, change
the gate script that calls it, or update the original skill and re-copy it
(update `MANIFEST.json` at the same time).
