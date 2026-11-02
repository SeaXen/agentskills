# What goes in a governance page for a 2-person project — and what doesn't

The failure mode you're actually defending against isn't disagreement — it's **both of you being unreachable at once** (Nadia on leave, you mid-flight or on a client site) when a security patch or a broken build needs shipping. A governance page for a 6,000-download library should solve that, plus set expectations so contributors don't read silence as neglect. Everything else — voting rules, steering committees, RFC processes, contributor tiers — is overhead built for projects with a dozen maintainers and disagreements to arbitrate. You don't have those problems yet; don't write rules for them.

Leave out: CLA/DCO, a code of conduct enforcement committee (link an existing CoC, don't build process around it), meeting cadence, formal proposal/RFC templates, maintainer voting thresholds, tiered contributor levels. If you ever hit 4+ active maintainers, revisit.

Here's the page:

```markdown
# GOVERNANCE.md

## Maintainers

- Nadia [@handle] — npm publish, GitHub admin
- [You] [@handle] — npm publish, GitHub admin

Both maintainers hold npm publish rights and GitHub admin on this repo, at all times.
This is not a courtesy — it's the whole point of this file. If you're reading this and
only one of us has one of these, fix it before anything else here matters.

## How decisions get made

- Default: lazy consensus. Either maintainer can merge bug fixes, docs, deps, and
  anything that doesn't change public API behavior. No sign-off required.
- Breaking changes / new public API: post the proposal as an issue, tag the other
  maintainer, wait 5 business days. If no objection, ship it. If the other maintainer
  is on leave or explicitly unreachable (see below), you can proceed alone — note that
  in the issue and move on. Don't let an absent reviewer block a needed change.
- Reverting something is always allowed, by either of us, no discussion needed.

## Availability

- Nadia is on parental leave [Jan–May 2027]. During this window, treat her as
  unreachable — don't wait on her for anything, including breaking changes.
- [You] travel frequently and may be slow to respond; assume replies can take up to
  a week outside active incidents.
- If both of us go quiet on a security report or a broken release for more than
  [72 hours], [backup contact / trusted contributor] has been given [scoped access —
  e.g. merge rights on a `hotfix` branch + npm publish for patch versions only] to ship
  a fix. This is the one case where we grant emergency access ahead of time rather
  than scrambling for it during an incident.

## Security reports

- Report to [security@... or GitHub private vulnerability reporting].
- Acknowledge within [5 business days]; if the primary responder is on leave, the
  backup contact above is authorized to triage and patch alone.

## Adding a maintainer

- Sustained, useful contribution over a few months, and agreement from whoever of us
  is active. No vote, no waiting period beyond that.

## What this file doesn't cover

Code style, PR process, release steps — those live in CONTRIBUTING.md, not here.
This file is about who can act, and what happens when one of us can't.
```

The one thing to do *before* January, not after: confirm both of you actually hold npm publish and GitHub admin right now, and pick the backup contact for the overlap-risk case. That single access check is worth more than any wording in the file.