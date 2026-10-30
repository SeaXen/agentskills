# Release-day runbook

Read this before merging the private fix. The order is load-bearing: a step done early opens the window this whole process exists to close.

Contents: private-fork limits, backports, regression test timing, downstream notice, release order, leaks, close-out.

## Private-fork limits (code-host temporary private forks)

- CI and integrations cannot access the fork; status checks do not run. Run the full test suite locally or in a private mirror before merging.
- All open pull requests in the fork merge at once, and only one may target the default branch. Prepare backports as separate branches or in the private mirror.
- Branch protection is not enforced on that merge, so review deliberately.
- Publishing the advisory deletes the fork. Merge first.
- Hosts without private forks: use a private mirror repository with the same release tooling.

## Backports

- Patch every supported line listed in SECURITY.md in the same release window. A line patched a week later is a line disclosed a week early.
- Run each line's own tests; a cherry-pick that compiles can still miss a code path.
- Lines that are out of support get no fix and no separate identifier. Name them in the advisory as affected and unsupported.

## Regression test timing

The test that triggers the flaw is a minimal proof of concept. For High or Critical issues, land it in a follow-up commit once users had time to upgrade, unless the fix is unreviewable without it; reviewers see it in the private fork either way.

## Downstream notice

- Send only for High or Critical issues, or when packagers must rebuild.
- Recipients: packagers who must rebuild, and known users who run the affected configuration (for example a feature documented as safe for untrusted input). Each extra recipient widens the leak surface; the wider dependent population learns at publication.
- Reach recipients through their published security contact, not a salesperson or a general inbox.
- Patch: share it at release time by default. Give early fork access only to recipients who must build before release.
- Include an interim mitigation when one exists, so exposed users can act before upgrading.
- Lead time: 1-7 days; up to 30 working days only for large vendor ecosystems with slow release trains.
- Linux distribution lists (distros, linux-distros): only for software distributions package, once a fix exists or is close. Put `[vs]` in the subject and propose a public date and time; embargo 14 days maximum, under 7 preferred. When the embargo ends, post the full details to the public oss-security list. A fix already in a public repository counts as public: do not use the lists for it.
- Pure libraries consumed from a registry usually need no list; notify the largest known dependents directly if severity warrants.
- Template: the downstream embargo notice in message-templates.md.

## Release order

1. Re-run tests for every line locally.
2. Merge the fix into the default branch, and backports into their branches.
3. Tag and publish every patched version.
4. Confirm each version installs from the public registry or module proxy.
5. Publish the advisory with fixed versions, affected functions and credits.
6. Publish release notes and the announcement linking the advisory (samber/developer-relations-skills@changelog-writing for the notes).
7. Post to oss-security if distribution lists were notified.
8. Tell the reporter, with links.

Avoid Friday evenings and public holidays for the reporter's and downstreams' time zones: a release nobody is around to deploy extends the window.

## Ecosystem release checks

Step 4 differs per ecosystem. Check the one that applies, before the advisory goes public.

- **Go modules:** tag a semver version on every module path (`/v2` and later majors are separate modules), then confirm the proxy serves it: `go list -m <module>@<version>`. Never leave the fix untagged; pseudo-versions break vulnerability-database imports. A `retract` directive is optional: the vulnerability database and govulncheck are the primary signal; retract when you also want `go get` to skip the range, knowing it needs another release.
- **npm:** `npm view <package>@<version>` returns the version; consider `npm deprecate` on vulnerable versions with a message pointing to the fix.
- **PyPI:** the new version appears on the project page and installs with `pip install <package>==<version>`. Yanking hides a version from resolution, but exact pins still install it: it is not a removal.
- **crates.io:** `cargo search` or the crate page shows the version. Yanking blocks new dependency resolution while existing lockfiles keep working; open a RustSec advisory as well.
- **Maven Central:** releases can take time to sync; confirm the artifact resolves before publishing the advisory. Published artifacts cannot be removed.

Registry-side detail: `samber/developer-platform-skills@sdk-package-publishing`, when installed.

## Leaks and active exploitation

- Partial leak or early public post: move to same-day release. Publish the advisory as soon as step 4 passes.
- Fix already visible in a public branch: treat the issue as public now.
- Exploitation in the wild: same-day release; tell known commercial integrators directly. Under the EU CRA, manufacturers that ship the software must report actively exploited vulnerabilities within 24 hours of becoming aware (eu-cra.md).

## Close-out

- Advisory reviewed into the code-host database and CVE record published, or a follow-up sent once the documented review window has passed.
- Ecosystem database imports show correct ranges and affected symbols; file corrections where not.
- Credits accepted by the credited people.
- Retrospective: what slowed the timeline, which out-of-scope class to add, whether the responder roster held.
