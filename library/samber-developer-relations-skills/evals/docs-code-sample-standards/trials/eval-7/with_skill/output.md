Not run: `scripts/sample-audit.py` (no Sablefish docs checkout here), no census, no secret scan. Every sample below is **unverified**, not passing. Owner handles, paths and language names are placeholders in `<angle brackets>`. I have none of the real ones.

## Conflict with the request

The skill's migration order is census and secret scan, then compile gates, then move samples into source, then metadata, then owners and SLAs. Your VP wants step 5 first.

1. **CODEOWNERS matches paths, not languages.** Samples are hand-pasted into about 900 Markdown pages, so one page can mix four languages. "Every language's samples to a named owner" cannot be expressed until samples live at `samples/<lang>/…`. Until then, the file can only map page sections to owners.
2. **A 48-hour fix SLA has nothing to trigger it.** Nothing is tested, so no sample can go red. The clock can only start on a reader report or a scan hit.
3. **Two SDKs have unpaid outside maintainers.** You cannot impose an SLA on volunteers. "Community-maintained" is a funding model, not a free one (Twilio contracted engineers to backstop its catalogue). I put an employed backstop on every line instead.

## 1. CODEOWNERS (merge Friday, phase A)

Last matching pattern wins. Every line has at least one employed owner. Any one listed owner can approve, so a volunteer can co-own but never blocks a merge.

```
# Code sample ownership. Policy: <docs-dir>/SAMPLE-POLICY.md
# Last matching pattern wins. Every line needs an employed owner.
# Volunteers may co-own, never solo: any one listed owner can approve.

# Default: docs leads own every page that has no narrower rule.
*                           @sablefish/docs-leads

# Adoption path: quickstart, auth, first call. Highest harm if wrong.
/<docs-dir>/quickstart/     @sablefish/docs-leads @<employed-sdk-lead>
/<docs-dir>/auth/           @sablefish/docs-leads @<employed-sdk-lead>

# Guides and API reference, by product area (not by language).
/<docs-dir>/<area-1>/       @sablefish/docs-leads @<area-1-engineer>
/<docs-dir>/<area-2>/       @sablefish/docs-leads @<area-2-engineer>

# Blog and archived posts: freeze with version banner or delete.
/<blog-dir>/                @sablefish/docs-leads

# Sample policy and the CODEOWNERS file itself.
/CODEOWNERS                 @<vp-engineering>
/<docs-dir>/SAMPLE-POLICY.md @sablefish/docs-leads
```

### Phase B: activate after samples move to compilable source

Commit this commented out. Uncomment when `samples/<lang>/` exists. Skipping that order gives owners responsibility with no mechanism.

```
# /samples/<lang-1>/        @sablefish/<lang-1-employed-team>
# /samples/<lang-2>/        @sablefish/<lang-2-employed-team>
# Outside-maintained SDKs: volunteer co-owns, employed team backstops.
# /samples/<lang-3>/        @<volunteer-lang-3> @sablefish/<backstop-team>
# /samples/<lang-4>/        @<volunteer-lang-4> @sablefish/<backstop-team>
# /samples/**/metadata/     @sablefish/docs-leads
```

Checks before merge:

1. Every listed owner has write access, or GitHub ignores that entry.
2. Teams are real and non-empty.
3. "Require review from Code Owners" stays off until the first quarter of enforcement. Otherwise a missing reviewer blocks the docs team.

## 2. SLA table

The SLA binds a surface and a role, not a person. A clock starts at triage: a reader report, a support ticket quoting a sample, or a scan hit.

| Severity | Definition | Employed-owner surfaces | Volunteer-maintained SDKs |
|---|---|---|---|
| P0 | Harms the copier: credential, destructive command, insecure default | Revoke or remove within 4 business hours. Rotate and purge history within 48 hours. | Same. The employed backstop acts, not the volunteer. |
| P1 | Does not work as written | Fix, or add a visible "known broken" banner, within 48 hours. | Triage within 48 hours by the backstop. Fix is best effort. If unfixed after 10 business days, label it community/unverified or remove it. |
| P2 | Works, violates policy | Next sprint. | Backlog. No SLA. |

Rules:

- A 48-hour fix SLA on volunteers is a promise nobody can keep. The 48 hours is the backstop's triage and mitigation duty.
- Bug fixes and security issues outrank new samples (AWS's published rule).
- The clock counts business days. State the timezone in the policy.
- Meaningful SLA reporting needs mean time from report to merged fix. You can measure that now. Per-sample CI status you cannot.

## 3. What to tell the VP

1. Friday ships: phase A CODEOWNERS, the SLA table above, and a **secret scan** of the whole docs tree. That scan is the only finding that cannot wait, and you have never run one.
2. Nothing is tested, so the Run and Compile-only tiers do not exist yet for you. Every sample is **unverified** until a pipeline exists. Building the pipeline is queue item 1 after the scan.
3. Language-level ownership arrives with step 3 of the migration. Start with the adoption path (quickstart, auth, first call), which should reach tier Run first.

Fix queue (P0 first, then ratio of readers × severity ÷ effort):

1. Secret scan over all 900 pages. Owner: docs leads. Days.
2. Compile-only CI job on the quickstart and auth samples. Owner: `<employed-sdk-lead>`. A couple of days to stand up.
3. Move the adoption-path samples into `samples/<lang>/` and publish by transclusion with snippet tags.
4. Add metadata records and schema validation.
5. Activate phase B, with the language tiers published.

Baselines to report against (self-set, not industry standards): zero P0, 100% of adoption-path samples at tier Run, at least 90% pass rate, at least 80% of the corpus tested, at least 90% parity coverage. Current values are unmeasured, not zero or passing. The one gate with a measured comparator is deprecated-API rate below 43% (Zhou and Walker, FSE 2016).

## 4. Language tiers (publish with the policy)

Choose tiers from download share and ticket volume, not from team preference.

- Tier 1: the one or two languages readers arrive with most. Every scenario, tested.
- Tier 2: entry path plus top scenarios.
- Community: the two volunteer SDKs unless they carry tier-1 traffic. Present, unowned by staff, labelled untested, with the maintenance expectation stated.

If a volunteer SDK turns out to be tier 1, fund it or demote it. Sparse columns in the parity matrix are the evidence.

## Open questions (they change the file)

1. What are the real SDK languages, and which two are volunteer-maintained?
2. What is the docs directory layout, so I can replace the `<docs-dir>` placeholders?
3. Who are the employed owners per area, individuals or teams?
4. Does CI exist for the docs repo today?
5. What is the target date for the secret scan? I recommend before the merge.

Next: run `gitleaks detect --source <docs-repo>` (or `trufflehog filesystem <docs-dir>`) before Friday's merge and paste the findings count.