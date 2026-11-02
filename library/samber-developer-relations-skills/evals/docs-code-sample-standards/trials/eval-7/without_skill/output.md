Next action: send the VP the three decisions at the bottom. The file and table below are drafts. Three inputs are missing, so I marked every guess `ASSUMED`.

## Two problems with the ask

1. **CODEOWNERS matches paths, and your samples have none.** They sit inside about 900 Markdown pages with no snippet tags. Friday's file can own SDK directories and docs sections. It cannot own "every language's samples" until samples are extracted into files.
2. **A 48-hour SLA cannot bind unpaid volunteers.** Put the SLA on a Sablefish employee for every SDK. Volunteers get best effort, with a paid backstop.

## Draft CODEOWNERS

```
# CODEOWNERS - last matching pattern wins. Keep specific rules BELOW general ones.
# Every owner needs write access to the repo, or the rule is silently ignored.
# Every rule lists @sablefish/docs-eng as co-owner, so a volunteer
# who goes silent can never block a merge.

# Default: whole repo
*                              @sablefish/docs-eng

# Docs pages (ASSUMED path)
/docs/                         @sablefish/docs-eng

# Samples embedded in docs pages, by language.
# No tags yet, so ownership is by section. Refine after snippet extraction.
/docs/**/python/               @PY_OWNER_HANDLE    @sablefish/docs-eng
/docs/**/typescript/           @TS_OWNER_HANDLE    @sablefish/docs-eng
/docs/**/go/                   @GO_OWNER_HANDLE    @sablefish/docs-eng
/docs/**/java/                 @JAVA_OWNER_HANDLE  @sablefish/docs-eng

# SDK source (ASSUMED paths and languages)
/sdks/python/                  @PY_OWNER_HANDLE    @sablefish/docs-eng
/sdks/typescript/              @TS_OWNER_HANDLE    @sablefish/docs-eng
/sdks/go/                      @GO_OWNER_HANDLE    @sablefish/docs-eng
/sdks/java/                    @JAVA_OWNER_HANDLE  @sablefish/docs-eng

# Security-sensitive files: always a Sablefish employee
/.github/                      @sablefish/security @sablefish/docs-eng
/CODEOWNERS                    @sablefish/docs-eng
```

Handle placeholders to replace:
- Paid SDKs: use the maintainer's employee handle.
- Volunteer SDKs: use the volunteer's handle, with the paid backstop in the SLA table as co-owner.

## SLA table

The clock starts when a confirmed report is triaged. It does not start at report time. Nothing is tested today, so nothing detects a broken sample on its own.

| SDK | Owner type | Owner of record | 48h fix SLA applies to | Backstop |
|---|---|---|---|---|
| SDK 1 (ASSUMED paid) | Employee | `@PY_OWNER_HANDLE` | Owner | `@sablefish/docs-eng` |
| SDK 2 (ASSUMED paid) | Employee | `@TS_OWNER_HANDLE` | Owner | `@sablefish/docs-eng` |
| SDK 3 (ASSUMED volunteer) | Outside contributor | `@GO_OWNER_HANDLE` | Best effort, 5 business days | Named employee `@BACKSTOP_GO` takes the 48h SLA |
| SDK 4 (ASSUMED volunteer) | Outside contributor | `@JAVA_OWNER_HANDLE` | Best effort, 5 business days | Named employee `@BACKSTOP_JAVA` takes the 48h SLA |

Severity tiers, so "fix" has one meaning:

| Severity | Example | Time to fix or mitigate |
|---|---|---|
| Critical | Live secret in a sample, or a sample that destroys data | 4 hours: remove or redact, then rotate |
| High | Sample does not compile or run | 48 hours |
| Normal | Outdated, cosmetic, or wrong output | 5 business days |

Rules for the SLA:
- **Fix** means the page shows a correct sample or the broken sample is removed. A removed sample counts as a fix, since you cannot test the replacement yet.
- The backstop covers the 48h clock on volunteer SDKs. If the volunteer has not acted by hour 24, the backstop takes the fix.
- Report SLA misses per owner, with the clock start time.

## Gaps this does not close

- No secret scan has ever run. Run one before Friday, because pasted samples are a classic place for live keys. Use `gitleaks detect` or `trufflehog filesystem ./docs`. One hit would make the 48h SLA the wrong tier.
- Branch protection with "require review from code owners" can block merges when a volunteer is the only owner. The `@sablefish/docs-eng` co-owner on every line prevents this.
- Ownership by path will go stale. Plan to replace the section-based rules with per-snippet rules after extraction.

## Decisions for the VP

1. Accept an SLA on paid owners and backstops, with best effort for volunteers? Recommended: yes.
2. Approve a snippet-extraction and CI-test project, so ownership and the SLA can be measured? Recommended: yes. About 900 pages is a multi-week job.
3. Who are the four owners, the two backstops, and the real repo paths?

Next: send me the real SDK languages, repo paths, and owner handles. I will fill the placeholders in about 5 minutes.