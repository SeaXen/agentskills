# Cobblestone: announcement and plan (draft, not published)

I read the skill and its references before writing. I didn't run the six-question interview, so the placeholders below are assumptions for you to confirm. Your decision to stop stands. I changed the plan on one point, because the skill rules out archiving this week at your scale.

## What I changed, and why

- **Archive this week → freeze, then archive in about a quarter.** At 40M monthly downloads through two frameworks, the skill's notice period is "a quarter or more". Setting PyPI `archived` blocks all uploads. If you set it this week, you can't ship the security fix you'd owe the day after.
- **"Archived can't be compromised" is half true.** An archived package ships nothing new, so no malicious release. But known flaws stay unfixed forever, and the two frameworks inherit them. Archiving trades supply-chain risk for unpatched-vulnerability risk. "Freeze then archive" covers both.
- **The real remaining risk is the name and the accounts, not the code.** Don't delete your PyPI or GitHub accounts, and don't let the email domain lapse. Keep 2FA and a recovery contact, and revoke only CI and personal publish tokens. A freed name or username can be claimed.
- **Tell the two frameworks first.** They are the likeliest custodians, and a surprise hurts them most. Send them the private note a few days before you post.
- **A silent archive strands people.** Dependents are far more likely to migrate off an abandoned package when the end of life is stated in the README (Miller et al., ICSE 2025).

## Timeline (today is 2026-10-23)

| Date | Action |
|---|---|
| Fri 2026-10-23 | Draft the private notes. Confirm the dates and placeholders below. |
| Mon 2026-10-26 | Send the private heads-up to both frameworks. |
| Thu 2026-10-29 | Publish the announcement: README banner, pinned issue, GitHub Release. Ship a final release with the status in its README. Switch to security-fixes-only. |
| 2027-01-29 | Last-chance release if a fix is pending. Post a reminder. |
| Mon 2027-02-01 | Archive on PyPI (`archived`) and archive the GitHub repo. This is the last step. |

If a framework offers custody (more than one admin) or names a vetted co-maintainer, switch to the dual-track wording at the end of this answer.

## Public announcement

```markdown
# cobblestone is moving to maintenance-only, and will be archived on 2027-02-01

I've maintained cobblestone since <year>. I no longer have the time it
needs, and I'd rather say so than let it go quiet. No co-maintainer has
come forward, so I'm ending the project in the open.

**What changes:** from today, security fixes only. No features, no new
Python-version work beyond what a security fix needs. On 2027-02-01 the
GitHub repository will be archived and the PyPI project marked
`archived`. After that, no further fixes, including security fixes.

**What keeps working:** every published version stays installable from
PyPI. Nothing breaks on 2027-02-01.

**Who is most affected:** cobblestone is pulled in transitively by
<Framework A> and <Framework B>. If you didn't choose it, check
`pip show cobblestone` or `pipdeptree -r -p cobblestone` to see what
requires it. Please plan a replacement or a fork before February.

**What to do:**
- Migrate to <alternative>, which covers <retry, backoff, ...>. Notes:
  <link to migration notes>.
- Or fork. The license (<license>) allows anyone to fork and continue.
- If your organization depends on cobblestone and could host it with
  more than one admin, write to <email> before 2027-01-15. I'd rather
  hand it to a custodian than archive it.

**Security reports:** until 2027-02-01, report to <SECURITY.md contact>.
After that date, nobody is reading them and no fixes will ship.

**Credentials:** after 2027-02-01, nobody will publish new versions
under the name `cobblestone`. I'm keeping the accounts, with
two-factor authentication, so the name can't be claimed by someone else.
Any version of cobblestone published after that date is not mine.

Thank you to everyone who filed a good bug, reviewed a PR, or answered
a question in the tracker: <contributors>.
```

## README banner (commit with the final release)

```markdown
> **Status: maintenance-only, archived on 2027-02-01.** Security fixes
> only until then. See the [announcement](<link>) for alternatives and
> how to fork.
```

## Private heads-up (to each framework's maintainers, 2026-10-26)

```markdown
Hi <maintainer> - <framework> depends on cobblestone, so you're hearing
this before the public post on 2026-10-29: I'm stepping down from
cobblestone, with the repository and PyPI project archived on
2027-02-01. Until then it gets security fixes only. If your team would
consider custody (more than one admin), or can name a person who could
co-maintain, I'd like to talk this week. If not, the migration notes
will be in the public post.
```

## Exit checklist

- [ ] Final release published with the status in its README.
- [ ] Banner committed, pinned issue and GitHub Release posted, repo description updated.
- [ ] Both frameworks warned privately before the public post.
- [ ] SECURITY.md says security reports are read until 2027-02-01 and not after.
- [ ] CI secrets and personal publish tokens revoked on 2027-02-01. GitHub and PyPI logins kept, with 2FA and a recovery contact.
- [ ] Email domain behind both accounts renewed, or accounts moved to an address you'll keep.
- [ ] PyPI `archived` and GitHub archive done on 2027-02-01, last. Check PEP 792 and the current PyPI docs for the exact steps first.

## Dual-track variant (if a candidate or custodian appears)

Swap the opening for this and keep the rest:

```markdown
# cobblestone is moving to maintenance-only; a handover or archive follows by 2027-02-01

From today, security fixes only. **Plan A:** <candidate or org> is
joining as co-maintainer. If the handover is complete by <gate date>,
they become the maintainer and nothing changes for users. **Plan B:**
otherwise the repository is archived on 2027-02-01 and the package
marked `archived` on PyPI. Every published version stays installable. I'll
post which plan applies on <gate date>.
```

For a handover, give publish rights only after a release made together with them. Don't give them to the first volunteer who asks (event-stream, 2018).

## Review and open items

- Re-read the plan on 2027-01-15, the custody deadline. Look earlier if a vulnerability report arrives or a framework asks for more time.
- Confirm these placeholders: license, first-release year, alternative library, security contact, and the two framework names.
- If you want a shorter notice, say so. It leaves the frameworks the least time to react, and I'd mark that as your call.