# July issue: item plan

I worked from the dates in your message. The system clock here reads 2026-10-30, so if that's the real date, the send and release dates below have already passed. Tell me if so.

## Summary

| Item | Verdict | Tense | Link to |
|---|---|---|---|
| (c) Free-tier limit 20 → 60 | Include, lead item | Past: "now live" | Docs limits page or changelog entry |
| (d) PG 13 image deprecation | Include, with an action | Present: "deprecated, removal 2026-10-01" | Migration or upgrade guide, plus changelog |
| (a) Logical replication slots UI | Include, as a teaser | Future: "arrives July 22" | Docs page if it's live by send time, otherwise no link |
| (b) Pooler auth bypass fix | Leave out | n/a | Nothing |
| Q4 roadmap (branching) | Leave out unless the PM gets sign-off | n/a | Public roadmap or feedback form, if you have one |

## Reasoning

**(b) Omit it entirely.**
- The advisory goes public 2026-07-24 and the newsletter sends 2026-07-16, so any mention would come eight days early.
- "A security fix is coming" or "update your pooler settings" signals that a vulnerability exists and points attackers at the pooler.
- Don't link the PR or write "security hardening". The merge date and the PR title are already public if the repo is public.
- Have the security team confirm hosted fleets are patched before 07-16. Then the August issue can carry it with a link to the published advisory.
- Don't use a vague teaser either. Advisory timing belongs to the security team.

**(c) Lead item.**
- It's shipped, simple and good news.
- Link to the user-facing limits or pricing docs, which should always show the current value (60). A changelog entry can be a second link.
- Don't link the PR, since readers don't need it.

**(d) Include it, because readers have to act.**
- Say what's deprecated, the hard date and the action: upgrade to a supported major version.
- Link to your upgrade guide first and the changelog second. If no guide exists, flag that as a gap before sending.
- Give the date in absolute form (2026-10-01).

**(a) Teaser only.**
- It ships 07-22, after the send date, so use future tense and don't say "now available".
- Link to the docs page only if it's published or scheduled to go live by 07-22. A link that 404s on send day is worse than none. Otherwise write "details in the 07-22 release notes".
- Link to the PR only if the main repo is public. I don't know that, so confirm.

**Roadmap teaser.**
- It's unannounced, and a newsletter is effectively public and permanent.
- Even a hint like "something about workflows for dev databases" can leak the feature.
- My recommendation is to say no. Offer the PM two alternatives: a "tell us what you'd like in Q4" feedback link, or save the item for the real announcement issue.
- If the PM insists, get written approval from whoever owns announcements first. Use only a theme-level line with no feature name and no date.

## Draft copy

> **Free tier: 60 connections (up from 20).** Live since July 1. Free-tier databases now accept up to 60 concurrent connections. [Limits docs →]
>
> **Postgres 13 images are deprecated.** Removal is on 2026-10-01. Databases still on 13 should upgrade before then. [Upgrade guide →] [Changelog →]
>
> **Coming July 22: logical replication slots in the dashboard.** View and manage slots without leaving the UI. Full details in the July 22 release notes. [Docs →, if live]

## Questions for you

1. Is the main repo public? That decides whether PR links are acceptable anywhere.
2. Does an upgrade guide for PG 13 exist?
3. Will the replication slots docs be live by 07-16?
4. Who owns approval for roadmap mentions: the PM alone, or also marketing and legal?