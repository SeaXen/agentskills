# Signup surfaces: placement, copy, source tags

Read this when writing the runbook for an owned-surface, archive, talk or community channel.

## Contents

1. Source-tag scheme
2. Placement and copy per surface
3. The CLI and install-output rule
4. Good and bad copy

## 1. Source-tag scheme

Give every surface its own value, so the metric sheet can rank channels on evidence. No published conversion rate exists for any of these surfaces, so the list's own per-source numbers are the only benchmark you will get.

```
source = <surface>-<placement>[-<campaign>]

docs-footer          docs-quickstart-end     readme-line
changelog-footer     release-notes-v4-2      blog-post-end
community-welcome    talk-<event>-card       pitch-<curator>-v4-2
swap-<peer>          rec-<peer>              archive-issue-page
republish-<platform> paid-<network>          in-product-invite
```

- Pass the value as a hidden form field the form copies into the subscriber record.
- Keep values short and lowercase. A value you cannot read in an export a year later is lost evidence.
- Tag the form, not only the link: a link tag disappears when someone copies the bare URL, and curators often strip tags.

## 2. Placement and copy per surface

Rank surfaces by reader intent per unit of traffic, and re-rank by where the traffic actually is (the docs analytics, the repository's traffic page):

- efficiency: quickstart end > changelog footer > docs footer > README > archive page > share line > blog post end > community welcome > dashboard toggle > talk end card

The quickstart end leads because the reader has just succeeded. The talk end card sits last only because it needs a talk; when one is booked, it costs an hour.

| Surface | Placement | Copy pattern | Notes |
|---|---|---|---|
| End of a quickstart or tutorial | after the success step | "Got it running? One email a month on releases and breaking changes." | Highest intent |
| Changelog and release-note footer | one line per entry page | "Get these in a monthly digest: [subscribe](...)" | Readers already follow release news |
| Docs footer | site-wide footer, one line | "Monthly: what shipped, what broke, what's next. Latest issue ->" | Link the latest issue too |
| README | one line under the install section | "Release notes and breaking changes by email: [subscribe](...)" | Never above the install command |
| Public archive | every issue page | subscribe form above the fold | Keeps working long after the send |
| Blog post end | after the conclusion | "If this was useful, the newsletter carries one post like it each month." | Never mid-article, never a popup |
| Community welcome message | the chat's or forum's welcome text | "Not here every day? The monthly digest covers what you missed." | A link, never an auto-subscribe |
| Product dashboard | settings or help menu, a toggle that defaults off | "Developer newsletter: monthly releases and deprecations" | Never a condition of using the product |
| Talk end card | final slide and the resources slide | short URL and QR code to a page with the talk's links and the signup | The page earns the signup; a bare QR code does not |
| Share line in the issue | one line near the end | "Know someone who'd use this? Forward it, or send them [the archive](...)." | One line, no reward |

## 3. The CLI and install-output rule

npm's terms ban packages that display ads at runtime, at installation, or through npm scripts; the ban followed public complaints about a package's postinstall message ("my installation log isn't for advertising space"). The same terms allow information on how to support a package in its documentation. Developers in every ecosystem read an unrequested prompt in their terminal the same way, whatever the registry's policy.

**Do:**
- Add one line to `--help` or the `about` output: "News and breaking changes: https://example.dev/newsletter".
- Offer an opt-in `community` or `links` subcommand that prints the newsletter, chat and docs links.
- Put the link in the docs page the CLI already points to.

**Don't:**
- Print a signup prompt on install, on first run, on every run, or after a successful command.
- Prompt for an email address inside the CLI.
- Add it to a deprecation or error message.

## 4. Good and bad copy

```
✓ Good - states cadence, content and sender, links a real issue and the privacy notice
Monthly, from the API team: releases, deprecations with dates, one deep dive.
Read the latest issue first. Privacy notice.

✗ Bad - promises nothing concrete, adds urgency
Join 10,000+ developers getting exclusive insights! Don't miss out.

✗ Bad - claims a cadence the programme does not hold
Weekly tips from our engineers.   (the charter says monthly)
```

Never put a subscriber count in signup copy unless it is the confirmed, current count.
