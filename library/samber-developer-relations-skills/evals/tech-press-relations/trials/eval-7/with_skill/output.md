## Verdict

The plan has one blocking defect (the embargo time is not actually an embargo) and one high-risk gap (your own release pipeline is wired to leak itself). Fix both before Thursday. The new reporter is a real flag but not a blocker if you verify them today.

## 🔴 Fix now — "Thursday morning" is not an embargo

Per the skill: *"State day, clock time and timezone. 'Tuesday morning is not an embargo.'"* You have two different commitments live at once — internally "Thursday 14:00," externally "Thursday morning" — sent specifically because the six reporters are spread across timezones. That's the exact condition that breaks it: each reporter will silently convert "morning" to *their own* local morning, and at least some of those will fall before, at, or after your real 14:00, so they publish out of sync with each other. An embargo only works if every recipient is bound to the same instant.

**Send a correction to all six today**, same wording, one message, stating the literal lift instant in an unambiguous format — e.g. "Thursday, Sep 24, 14:00 UTC (10:00 ET / 16:00 CEST / 23:00 JST)" — not a relative phrase. Do this now, not day-of; a same-day timezone correction to people already holding a story is exactly the kind of scramble that costs relationship capital.

## 🔴 Fix now — your release process is wired to leak the embargo

The skill's leak checklist exists precisely for this setup, and your description trips four of its seven items simultaneously:

- **Tag push → CI publishes to npm** = the "package published to a registry" leak vector. npm registry publishes are public and bot-scraped the moment they land; if the tag goes out before 14:00, the release is discoverable before lift.
- **Docs site auto-deploys from main** = the "docs deploy" leak vector. If anything 4.0-shaped merges to main early, the docs site shows it immediately, with no embargo awareness.
- **Changelog PR already open on the public repo** = the "changelog entry" leak vector, plus the PR itself is visible pre-merge to anyone watching the repo (issue/PR feeds, watchers, release-tracking bots). Check its title and diff don't already spell out "4.0" to a casual observer.
- **Pricing page merged behind a flag** = the "licence or pricing file" leak vector. A flag is only as good as what it actually gates — verify it's a server-side gate, not just a client-side render toggle, and check the compiled JS bundle and the direct URL don't already expose the new pricing before flip.

**Do not push the tag and do not merge the changelog PR until the literal lift second.** Sequence per the skill's day-of runbook (owned post + press page live at lift, then coverage, then community): assign one person to trigger, in order, at 14:00 exactly — merge changelog PR → push tag → flip pricing flag → publish owned post. Treat this as one atomic action window, not three independent tasks someone gets to "whenever."

## 🟠 Handle carefully — the unverified reporter

The skill is explicit: *"Offer an embargo only to reporters with a track record of honouring one. A first contact gets the news at lift time."* Someone who cold-emailed last week has no track record with you, however credible the email sounded.

**Today, verify them like any new addition to the media map**: confirm current employer, pull their last five bylines, confirm they still cover this beat, check for a published embargo/no-pitch policy. If that checks out, keeping them in the embargo group is a defensible judgment call — but they're your highest-risk send, so don't hand them anything beyond the standard briefing pack (no early exclusive-grade material, no early access ahead of the others). If you can't verify them in time, default to the rule as written: give them the release at lift time like any other first contact, not early.

## ✅ What's fine

- Six reporters holding for one shared date is correctly an **embargo**, not an exclusive — no vocabulary confusion here, no double-promise risk.
- A major-version-with-breaking-changes announcement is the right playbook match; worth a quick check (not raised in what you described) that the briefing pack actually contains the migration guide, deprecation timeline, and affected-downstream-project count — the playbook's trap is framing the break as pure upside, and technical readers will find the migration cost with or without you.

## Before you send anything else

1. **Send the timezone correction to all six reporters now.**
2. **Verify the cold-email reporter's byline and employer today.**
3. **Lock the tag push, changelog merge, and pricing-flag flip to fire together at 14:00**, owned by one named person.
4. Confirm the press page and briefing pack are actually live, with the embargo line (date, clock time, timezone) repeated in both the email and the document — not just in your head.