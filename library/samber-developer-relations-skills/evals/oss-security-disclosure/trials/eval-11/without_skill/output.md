**Do first (2 min):** Don't send anything to the 400 packages or to linux-distros yet. Four parts of the plan would cause harm or fail as written.

## Problems in the plan

1. **"Checks green" likely isn't a CI pass.** GitHub doesn't run Actions in temporary private forks, so a green mark may mean nothing ran. Check whether the checks list shows real workflow runs. If not, run `npm test` and the build on both fix branches locally.
2. **Publish-then-merge is backwards.** Publishing the advisory deletes the temporary fork, and the three PRs go with it. Merge from the advisory page first, then publish. Verify this in the GitHub docs before Tuesday.
3. **Emailing 400 packages with the patch attached 5 days early.** Five days before Tuesday 2026-10-27 is Thursday 2026-10-22, which has already passed.
   - You cannot keep an embargo across 400 parties.
   - An auth-bypass patch is a roadmap to the exploit.
   - The fix is not yet on npm, so recipients can't do anything useful with it.
   - Instead, send a pre-notice to a short list of known critical dependents. The email is below.
4. **linux-distros.** That list is for software that Linux distributions package. An npm library probably doesn't qualify. The list also caps embargoes at 14 days and has its own posting rules. Skip it unless a distro ships `pelmont-sso`.
5. **Yuki agreed to the date, not to the pre-notice.** Tell Yuki about the pre-notice list before you send it.
6. **Exploit test in the fix PR.** A regression test is normal, but keep it minimal and not a ready-made exploit.
   - Exclude `test/` from the npm tarball (`files` in `package.json`).
   - Run `npm pack --dry-run` to confirm.

## Release checklist (Tuesday 2026-10-27)

**Before (today to Monday)**
1. Run tests and build locally on the 6.x and 5.x fix branches. Both must pass (~20 min).
2. Confirm the advisory lists the affected ranges for both lines and the patched versions.
3. Request the CVE through the GitHub advisory (GitHub is the CNA).
4. Message Yuki: the date, the pre-notice list, and how to credit them.
5. Pick the pre-notice recipients, capped at about 10. Use security contacts you can name. Send the email below on Monday.
6. Bump versions on both branches (needs your OK per the repo rules). Write the changelog entry without exploit details.
7. Check that `npm whoami` works, 2FA is on, and you hold publish rights.

**Release day**
1. Merge the fix PRs from the advisory page: first the 6.x PR to `main`, then the 5.x PR to `release-5.x`, then the docs PR.
2. Publish 6.x with `npm publish`.
3. Publish 5.x with `npm publish --tag release-5.x`. Without `--tag`, it moves `latest` back to 5.x.
4. Run `npm view pelmont-sso dist-tags --json`. Confirm `latest` points to the 6.x release.
5. Publish the advisory right after both versions are on npm.
6. Run `npm deprecate` on the vulnerable ranges with a pointer to the advisory.
7. Send the public notice below and pin it in the repo's Discussions.
8. Reply to Yuki and confirm credit.

**After**
1. Re-test a clean install of each fixed version.
2. Check that `npm audit` flags the old ranges.
3. Write a short post-mortem note.

## Email 1: pre-notice (Monday, to the short list)

**Subject:** [CONFIDENTIAL, embargo until Tue 2026-10-27 [HH:MM] UTC] Critical security fix in pelmont-sso

Hello [Name],

We will release a fix for a Critical authentication bypass in `pelmont-sso` on Tuesday 2026-10-27 at [HH:MM] UTC. You get this notice because your project depends on `pelmont-sso`.

- **Affected:** 6.x before [6.x.y] and 5.x before [5.x.y]
- **Fixed in:** [6.x.y] and [5.x.y]
- **Impact:** an attacker can bypass authentication [one line, no exploit detail]
- **Action:** plan to upgrade on release day. No action is possible before then.

Please keep this confidential until the release time. Don't open public issues, PRs, or commits about it. Reply to confirm you received this, and tell us who else on your team should be told.

The patch and advisory will be public at the release time. If you need the patch earlier to prepare, reply and we will share it through a private channel.

[Name], pelmont-sso maintainers
[security contact]

## Email 2: public notice (release day, to dependents)

**Subject:** Security release: upgrade pelmont-sso to [6.x.y] or [5.x.y] now

Hello,

We released fixes for a Critical authentication bypass in `pelmont-sso` (CVE-[ID]).

- **Affected:** 6.x before [6.x.y] and 5.x before [5.x.y]
- **Upgrade:** `npm install pelmont-sso@[6.x.y]` or `npm install pelmont-sso@[5.x.y]`
- **Advisory:** [GHSA link]
- **Workaround:** [none, or describe]

Treat this as urgent. If you cannot upgrade today, tell us at [security contact] and we will help.

Thanks to Yuki [surname or handle] for the report and the coordinated disclosure.

[Name], pelmont-sso maintainers

**Next:** run the tests locally on both fix branches. If they pass, send me the pre-notice recipient list and I'll tighten Email 1.