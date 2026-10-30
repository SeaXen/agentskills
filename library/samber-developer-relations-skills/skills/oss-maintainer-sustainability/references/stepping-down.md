# Stepping down

Exit paths, registry mechanics, announcement templates and notice periods.

## Contents

- Exit paths
- Notice periods
- Registry mechanics
- Accounts and credentials
- Announcement templates
- Exit checklist

## Exit paths

| Path | Use when | Watch out for |
|---|---|---|
| **Freeze then archive** (default) | no vetted successor; users need time to migrate | the freeze must have an end date; known vulnerabilities stay unfixed after it, so say so |
| **Archive now** | tiny user base, or the project is already unused | dependents still need the end-of-life signal and a statement on security fixes |
| **Transfer to a custodian** | a foundation, collective or dependent company offers custody with more than one admin | the custodian's own capacity; collectives sunset too |
| **Handover to a vetted successor** | someone already passes the vetting checklist and has made a release with you | transferring the code but not the registry name |

A forge archive can be reversed, but users who migrated will not come back. Decide once.

## Notice periods

Self-set baseline; widen it when dependents are large or slow-moving.

| Dependents | Notice before archive |
|---|---|
| Personal tool, few downloads | announce and archive the same week |
| Used by other projects | about a month |
| Widely used or a transitive dependency of large projects | about a quarter or more; a collective of 71 projects gave about 9 months |

## Registry mechanics

| Ecosystem | End-of-life signal | Ownership transfer |
|---|---|---|
| PyPI | PEP 792 defines `active`, `archived`, `quarantined`, `deprecated`; owners can set `archived` today, which blocks new uploads, so set it only on the archive date. Before that, a final release whose README states the status | Add the successor as owner yourself. PEP 541 never reassigns a name against a reachable owner, and requires failed contact, no releases for 12 months and no owner activity |
| npm | `npm deprecate <pkg>@"<range>" "<message pointing at the alternative>"` prints a warning on install; nothing is deleted | `npm owner add` by the current owner; npm resolves no abandoned-package claims on request |
| Go modules | `// Deprecated: use <new path> instead.` comment above `module` in `go.mod`, published in a new version; `retract` marks bad versions | No registry; transfer the repository (forge redirects keep old import paths working until the old path is reused) or publish a new path and deprecate the old one. A vanity import path you control survives any repository move |
| crates.io, RubyGems, others | the registry's own yank or deprecation feature, plus a final release with the status in its README | add the successor as owner before you leave |
| Repository | archive (read-only, still fetchable); status in the description and README | transfer the repository to the successor or custodian account |

Check the registry's current documentation before acting; these mechanisms change.

## Accounts and credentials

With a successor or custodian, follow the governance credential inventory and hand each item over one at a time. Exit-specific points:

- Hand the security-report inbox over explicitly and update SECURITY.md.
- Move your name to an emeritus or past-maintainers list last.

Without a successor, the archive is only as safe as the accounts behind it:

- Keep the forge and registry accounts, with two-factor authentication and a recovery contact. Never delete them: a freed username or package name can be claimed, and repositories that redirected through the old name can be hijacked.
- Keep the email domain behind those accounts renewed, or move the accounts to an address you will keep.
- Revoke CI secrets and personal publish tokens; keep your own login.
- State in the README who, if anyone, can still publish an emergency fix.

## Announcement templates

Freeze then archive:

```markdown
# <project> is moving to maintenance-only, and will be archived on <date>

I've maintained <project> since <year>. I no longer have the time it needs, and I'd rather say so than let it go quiet.

**What changes:** from today, only security fixes. On <date> the repository will be archived and the package marked <deprecated/archived> on <registry>; after that, no further fixes, including security fixes.
**What keeps working:** every published version stays installable. Nothing breaks on <date>.
**What to do:** <alternative or fork>, which covers <what>. The license allows anyone to fork and continue.
**Credentials:** after <date>, nobody will publish new versions under this name.

Thank you to <contributors>.
```

Dual track, when a candidate exists but is not yet vetted:

```markdown
# <project> is moving to maintenance-only; a handover or archive follows by <date>

I'm stepping down from <project> by <date>. From today, only security fixes.
**Plan A:** <candidate> is joining as co-maintainer. If the handover is complete by <gate date>, they become the maintainer and nothing changes for users.
**Plan B:** otherwise the repository is archived on <date> and the package marked <deprecated/archived>. Every published version stays installable.
I'll post which plan applies on <gate date>.
```

Private heads-up to a large dependent, a few days before the public notice:

```markdown
Hi <maintainer> - <your project> depends on <project>, so you're hearing this before the public post on <date>: I'm stepping down by <date>. The plan is <path>. If your team would consider custody, or a named person who could co-maintain, I'd like to talk this week.
```

Handover:

```markdown
# <successor> is the new maintainer of <project>

After <N> months maintaining <project> together, <successor> takes over on <date>. They have made <release> with me and now hold release and publish rights. I'm stepping back to emeritus.

Nothing changes for users. Security reports still go to SECURITY.md, which now reaches <successor>.
```

```
// ✗ Bad - no status, no date, no pointer
"I don't have much time for this anymore, might come back later. PRs welcome!"
```

## Exit checklist

- [ ] Status chosen and written in the README and repository description.
- [ ] Announcement posted on every surface users read (README, release notes, pinned issue, docs banner).
- [ ] Registry end-of-life signal set, or registry ownership transferred and tested.
- [ ] Every credential transferred, or (without a successor) accounts kept with 2FA and tokens revoked.
- [ ] Security-report path updated or closed with a statement.
- [ ] Repository archived last, after the notice period.
