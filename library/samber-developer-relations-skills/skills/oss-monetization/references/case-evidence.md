# Case evidence

Every case, figure and quote the skill cites, with its source, what it proves and what it does not. Revenue figures are self-reported by maintainers. Claims marked **unconfirmed** have no maintainer or vendor source behind them; never use them as planning inputs. Press-sourced rows name the outlet; treat them as reported, not verified. Aggregator revenue figures contradict each other and are never used.

## Contents

- Paid add-on on a free core
- Paid content, companion products and sponsorware
- Hosted offerings
- Commercial and dual licenses for libraries
- Support, donations, marketplaces
- Prerequisites, in practitioners' words

## Paid add-on on a free core

| Case | Facts and source | Proves | Does not prove |
|---|---|---|---|
| Sidekiq (Mike Perham, solo) | Launched 2012; closed paid layer added about six months later. Close to $80,000 a month and "about 800 customers" at $1,000/yr Pro and $2,000/yr Enterprise (Indie Hackers podcast #016, 2017). "I'm at ~$2m now. Still no employees" (Hacker News comment, December 2019; period not stated). Pro later $99/month, Enterprise from $269/month (Sidekiq wiki). About 90% of sales from referrals or free-user upgrades: **unconfirmed**. | One person can earn a large salary from one library with no license change, no CLA and no hosting. | That any library can: Sidekiq sells to companies running a distributed system they would otherwise build. |
| Faktory (same author) | Open edition AGPL. Enterprise sold in packs of 100 connections, first pack $299/month, $99 per extra pack; no key needed in development (contribsys.com, Faktory wiki). | A usage proxy (connections) can stand in for organization size; a license key in a paid edition is accepted. | Revenue: none published. |
| River Pro (Go job queue, two founders) | Pro $125/month for up to 20 developers; Enterprise custom with invoice, purchase order and a SOC 2 report. Paid code is a proprietary module served through a private Go module proxy with a per-customer secret; it wraps the open client (riverqueue.com/pro, River docs). | The add-on model ports to Go with native distribution. | Revenue: none published. Main user complaint on Hacker News: "many features are locked behind Pro". |
| Laravel Nova and Spark | One-time purchase with a year of updates, priced per project ($99 single, $299 unlimited for Nova) (laravel.com). | Per-project pricing is a working alternative to per-seat. | Indie economics: Laravel is a company today. |

Perham's boundary rule: "if a hundred percent of people need it then it should go into Sidekiq, the core" (Starting & Sustaining interview). His sales argument is build versus buy: a senior developer costs more per month than the license costs per year (Sidekiq wiki).

## Paid content, companion products and sponsorware

| Case | Facts and source | Proves | Does not prove |
|---|---|---|---|
| Tailwind UI (Adam Wathan) | "$400,000 on the first day" (2020) and over $4M in under two years; docs "an incredible distribution channel" (adamwathan.me). Later, in a GitHub pull-request comment (January 2026, reported by DevClass): docs traffic "down about 40% from early 2023 despite Tailwind being more popular than ever", revenue "down close to 80%", "75% of the people on our engineering team lost their jobs". He attributes the fall to AI assistants. Revenue ran on one-time purchases (Startups for the Rest of Us #825). Tailwind Labs later joined Shopify (tailwindcss.com blog); the framework stays MIT. | A companion product can earn far more than the project's donations. One-time purchases plus a single docs funnel are fragile. | The cause: AI is the founder's explanation, and pricing saturation and competing kits overlap the same period. |
| Caleb Porzio (Livewire, Alpine) | $1M through GitHub Sponsors: $725k premium screencasts, $200k company logo placement, $25k hourly consulting, $20k sponsorware early access, $10k other (calebporzio.com). About 73% was paid content. | Paid teaching can pay a salary. | That a sponsor button earned it: Sponsors was the payment rail for content. |
| Pest (Nuno Maduro) | Released to sponsors first; opened at 75 sponsors, as promised (Maduro's announcement, via Laravel News). | Sponsorware works for a new, eye-catching tool with a published threshold. | That it works for a project already released; Nadia Eghbal's Lemonade Stand lists both limits. |

## Hosted offerings

| Case | Facts and source | Proves | Does not prove |
|---|---|---|---|
| Plausible Analytics | MIT to AGPLv3 (2020) to stop resale as a service. Later renamed the self-hosted edition (Community Edition) because resellers used "the Plausible Analytics name and logo" (Plausible blog, Community Edition announcement, February 2024). Same announcement: eight core team members, no investors, 12,000+ paying subscribers, self-hosters donating about $300 a month in total. | Hosting a self-hostable app funds a small team; trademark separation matters as much as the license. | That hosting suits a library. |
| Ghost | Non-profit foundation shipping MIT, over $10M ARR with a staff in the thirties (founder's posts). | Hosting works without copyleft. | Anything about a 1-5 person team. |
| Cal.com | MIT to AGPL plus a commercial folder (2021), then the production code moved private (2026) (Cal.com blog). | Open-core drift under venture funding. | An indie path. |

## Commercial and dual licenses for libraries

None of these publishes revenue after the change.

| Case | Change and source | Reaction |
|---|---|---|
| FluentAssertions v8 | After a partnership with Xceed, a component vendor: Apache-2.0 to a non-commercial community license, $129.95 per developer per year, "no seat swapping" (Xceed product page, InfoQ, January 2025). The license switched in the pull request before 8.0, after prereleases shipped as Apache. Contributors were asked to consent to the new terms going forward (GitHub discussion). | Called bad faith; the AwesomeAssertions fork was built from the last free commits, and downstream projects still file issues to switch to it. The strongest fork of the wave. Vendor partnership, surprise timing and per-developer price arrived together; no single cause is proven. |
| AutoMapper and MediatR (Jimmy Bogard) | Announced three months ahead; new majors dual-licensed RPL-1.5 or commercial; earlier versions keep Apache or MIT (Lucky Penny FAQ). Free under $5M company revenue; paid tiers by developer-count band; license keys registered (launch post). | An old "never commercialize" comment resurfaced; "pin the last free version" guides circulated; no prominent fork. Trigger, in Bogard's words: companies built commercial products on them and "never sponsored or contributed". |
| MassTransit v9 (Chris Patterson) | v9 commercial, v8 open with security fixes for a stated period; target prices announced as "not set in stone" (Patterson's announcement, reported by developer blogs). | Pre-announced; reaction muted. |
| ImageSharp (Six Labors) | Split license: open for open source, non-profits and companies under $1M revenue; commercial above it for direct dependencies (Six Labors license text). | Sponsorship and support had yielded "less than a few months of developer income over a period of several years" (sixlabors.com). Left the .NET Foundation; build-time license keys followed; wrapper vendors evade the threshold. |
| Moq | Version 4.20.0 bundled a closed, obfuscated sponsorship check that hashed the developer's git email and sent it out (BleepingComputer, Checkmarx, August 2023). | Removed in the next release about a day later; the stated reason was broken restores on macOS and Linux, amid a public backlash. A contributor's same-name fork was later taken down on a copyright and trademark claim: **unconfirmed**. |
| Qt | Dual-licensed from early on with a CLA, plus a foundation agreement that frees the code if the free edition stops (kde.org). | Durable company; the CLA is the precondition for copyleft dual licensing. |
| iText | MPL/LGPL to AGPL with version 5 (2009, itextpdf.com). | Durable company and a durable fork (OpenPDF, adopted by reporting tools). |
| Sencha Ext JS | LGPL to GPL, then single seats dropped for five-packs, then subscription-only (sencha.com; press). | Revenue survived; the individual and small-team buyer did not. |

## Support, donations, marketplaces

- **Tidelift**: paid maintainers for security, licensing and maintenance assurances to subscribing companies; 19% of maintainers in its 2024 survey reported income from it, with no amounts published, and 60% of maintainers are unpaid (Tidelift 2024 maintainer report). Tidelift was acquired by Sonar in late 2024: check the program still pays before counting on it.
- **Extended security support**: commercial vendors sell backports for end-of-life versions of popular open-source frameworks; a maintainer can sell the same thing for their own old majors. No indie revenue figure is published.
- **Standalone support**: Porzio earned $25k lifetime from hourly consulting. Indie support sells best bundled into the enterprise tier (Sidekiq Enterprise, River Enterprise).
- **Babel**: set an $11,000 a month salary baseline (2018, babeljs.io); by 2021 "Babel is used by millions, so why are we running out of money?", followed by public criticism of the paid maintainer's salary (The Register). Donations invite public audits of pay.
- **core-js**: donations "many times less" than the author's previous salary; his post-install funding message stopped working once npm hid install output (core-js repository, 2023).
- **Faker and colors**: "No more free work from Marak, Pay Me or Fork This", then sabotaged releases (BleepingComputer, The Register). The community fork became the maintained package.
- **Marketplaces**: no indie library has disclosed material revenue from cloud, IDE or code-host marketplaces. Indie sales run through direct card checkout, the vendor's own billing page, or a reseller.

## Prerequisites, in practitioners' words

- **Heather Meeker, on ownership**: only "the author of the software (or a subsequent copyright owner via assignment)" can grant proprietary terms to a copyleft work; dual-licensed products need contributors to sign a CLA, and "contributors tend to balk" (heathermeeker.com, 2018). Permissive licenses such as MIT and Apache-2.0 already let anyone ship the code under other terms with notices kept.
- **Meeker, on fit**: dual licensing "only works... where... the software is mainly used in distributed products"; for software run as a service, "GPL would not drive anyone to take a proprietary license". She notes pure dual licensing "waned" in favor of the "upsell" (open core).
- **Go note**: Go links statically and most Go libraries run inside servers, where GPL creates no pressure; AGPL does, but sits on many corporate ban lists, and the module proxy keeps serving the last permissive version. Put a new license on a new major import path, so no user receives new terms through a routine update.
- **Jimmy Bogard, on thresholds**: free under "$5M USD yearly revenue. That's 5 times more than typical free tiers I researched."
- **Caleb Porzio, on guilt**: "The work is what justifies the money" (Changelog #381).
- **Mike Perham, on sustainability**: "My solution to sustainability was to make Sidekiq profitable... I settled on the open core business model" (mikeperham.com, 2022).
