# Pushback first: archiving doesn't make you safe

Your premise is wrong in a way that matters for the announcement.

- **Archived PyPI projects stay installable.** "Archived" makes the project read-only, so no new releases or uploads. All 40M monthly downloads keep resolving to the last version.
- **Archiving removes your ability to patch.** If a vulnerability turns up in a retry library that sits in the request path of two big frameworks, nobody can ship a fix.
- **Abandoned packages are a classic target.** The usual attacks are account takeover on a dormant maintainer account, expired-email password resets, and "can I take over this name?" requests. Archiving doesn't remove those risks.
- **Your downstream is the hard constraint.** A "this week" archive gives the two frameworks and their users no time to swap you out.

Safer sequence:

1. Tell the two framework projects privately, today.
2. Publish a final release with a `DeprecationWarning`.
3. Keep 2FA and trusted publishing on until the PyPI archive.
4. Archive only after the frameworks have dropped you or taken over.

The announcement below follows that sequence. Fill in the `[brackets]`. I haven't verified any dates or framework names.

---

## Announcement: cobblestone is being wound down

**Status: end of life planned for [DATE, suggest 2027-04-30]. Please do not start new projects with cobblestone.**

cobblestone has been a one-person project, and I can no longer maintain it. I looked for a co-maintainer or successor and found none. Rather than let it decay silently, here is exactly what will happen and when.

### What this means for you

- **Direct users:** plan to migrate before [DATE]. Alternatives to evaluate: [`tenacity`, `urllib3.util.Retry`, `stamina`, or whichever you verify fits]. A migration note is at [LINK].
- **Indirect users (you never installed cobblestone yourself):** you likely get it through [Framework A] or [Framework B]. Those projects have been notified. Watch their release notes. You don't need to act yet.
- **Security:** I will ship fixes for security issues until [DATE]. Report privately via [SECURITY CONTACT / GitHub private advisory link].

### Timeline

| Date | What happens |
|---|---|
| [2026-10-23] | This announcement. Framework maintainers contacted. |
| [2026-11-06] | Final release `X.Y.Z`. It emits a `DeprecationWarning` at import and links to the migration notes. No new features. |
| [2026-11-06 → DATE] | Security fixes only. |
| [DATE] | Repository archived on GitHub. PyPI project marked archived. |

The archive date will move later if [Framework A] or [Framework B] still depends on cobblestone and asks for more time. It will not move earlier.

### Want to take it over?

If you or your organization can commit to maintaining cobblestone, contact me at [EMAIL] before [DATE]. I will consider handing over the repository and PyPI project to a maintainer with a track record and a second maintainer. I won't hand them to an anonymous requester.

What I'd look for:

- Public history of maintaining widely used packages.
- At least two people with release rights.
- Commitment to 2FA and PyPI trusted publishing.

### What I'm asking of downstream projects

- Pin or constrain `cobblestone` only if you must. Otherwise let the final release flow through.
- Plan the replacement now. Archived packages receive no fixes.
- Don't pull cobblestone from mirrors or vendor an unreviewed fork under the same name.

Thank you to everyone who filed issues, sent patches, and relied on this library.

— [NAME]

---

## Before you publish: checklist

1. **Email the two framework maintainers privately** with the timeline, before the public post. They are the real blast radius.
2. Confirm 2FA and trusted publishing are on for the PyPI account until the archive date.
3. Ship the final release with the deprecation warning, and check it doesn't break users running `-W error`.
4. Pre-write the migration notes at the linked page.
5. Pin the announcement as a GitHub issue or discussion, and put a banner at the top of the README.

If you'd rather archive this week anyway, say so and I'll cut the timeline down. I'd then drop the "security fixes until" line, since it would no longer be true.