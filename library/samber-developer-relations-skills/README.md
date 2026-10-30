# Developer relations skills

Skills for the people who run **developer relations**: documentation, open source, community, events, technical content, and the program strategy and measurement holding it together.

Written for **developer advocates, DevRel leads, community managers and OSS maintainers**. Every skill ends in **a decision or a shippable artifact**, never a list of best practices.

<img width="1904" height="640" alt="image" src="https://github.com/user-attachments/assets/d43bd887-44f1-4387-8ce4-ee692367dcfe" />

## 📚 Related Collections

- [`developer-platform-skills`](https://github.com/samber/developer-platform-skills): Platform & SDK developer experience: _for platform engineers, DX engineers, SDK authors, API product managers, DevRel engineers_
- [`dev-event-organizer-skills`](https://github.com/samber/dev-event-organizer-skills): Technical event operations: _for event organizers, conference producers, hackathon leads, community builders_

_Part of the [samber skills ecosystem](https://github.com/samber?tab=repositories&q=skills)_

## 🚀 Install

Install every skill in this repo, not just one. Skills here are atomic by design and reference each other freely: picking a single skill leaves its sibling skills uninstalled, so cross-references and routed handoffs go nowhere.

<details>
<summary><b>skills.sh</b> — universal, works with any Agent Skills-compatible tool</summary>

```bash
npx skills add samber/developer-relations-skills
```

</details>

<details>
<summary><b>Claude.ai</b></summary>

1. add as a plugin marketplace: open **Settings -> Capabilities -> Plugins**
2. click **Add -> Add marketplace -> Add from a repository**
3. enter `samber/developer-relations-skills`
4. then **Sync**

</details>

<details>
<summary><b>Claude Code</b></summary>

```bash
/plugin marketplace add samber/developer-relations-skills
/plugin install developer-relations-skills@developer-relations-skills
```

</details>

<details>
<summary><b>Codex (OpenAI)</b></summary>

```bash
codex plugin add github:samber/developer-relations-skills
```

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/samber/developer-relations-skills.git ~/.cursor/skills/developer-relations-skills
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
gemini extensions install https://github.com/samber/developer-relations-skills
```

Update with `gemini extensions update developer-relations-skills`.

</details>

### First run

```
/developer-relations-kickoff We open-sourced our SDK three weeks ago and it has four stars. I can't tell whether that's a marketing problem or a docs problem.
```

## 📦 Skills

This collection covers the full developer-relations surface.

### Start here

[`developer-relations-kickoff`](./skills/developer-relations-kickoff): Routes the current DevRel task to the right skill of this collection, or says plainly that none fits, then bootstraps or resumes the project's shared context artifact.

### Meta

- [`devrel-career`](./skills/devrel-career): Plans a DevRel career from the candidate side: portfolio audit against real hiring signals, the six-rung IC ladder, interview-loop prep, and offer evaluation.
- [`devrel-hiring`](./skills/devrel-hiring): Plans DevRel hiring from the employer side: job posting and scorecard, interview loop and question bank, portfolio scoring, and a 30-60-90 ramp plan.
- [`devrel-team-structure`](./skills/devrel-team-structure): Designs the DevRel org: the reporting line and what it starves, the team shape, the coverage map, the interlocks, and the trigger for the next re-org.
- [`devrel-radar`](./skills/devrel-radar): Builds a time-budgeted watch list of DevRel podcasts, newsletters, communities, conferences and practitioners, plus the routine that keeps it verified and fresh.

### Strategy & planning

- [`devrel-strategy`](./skills/devrel-strategy): Designs a DevRel program from the top: the business driver that funds it, the two goals it serves, the pillar mix, the staffing sequence, and a written refused list.
- [`developer-first-gtm`](./skills/developer-first-gtm): Designs the go-to-market motion for a developer product: the adoption model, the self-serve entry, the developer-to-buyer handoff rule, and the land-and-expand path.
- [`developer-ecosystem-strategy`](./skills/developer-ecosystem-strategy): Decides whether and how far a developer product opens into a platform other companies build on, and what that permanently obliges you to.
- [`developer-segmentation`](./skills/developer-segmentation): Cuts a developer audience into a few named, sized and ranked segments, ending in one primary segment, one secondary, and a written anti-segment.
- [`developer-journey-map`](./skills/developer-journey-map): Maps one segment's journey from discovery to advocacy, each stage carrying an exit event, an owner and a signal, then names the single leak worth fixing next.
- [`devrel-budget-allocation`](./skills/devrel-budget-allocation): Splits a DevRel budget into line items that each carry a cost, a return threshold, a review date and a reallocation rule, plus a ranked cut list.
- [`developer-education-strategy`](./skills/developer-education-strategy): Decides whether to invest in structured developer education (learning paths, labs, certification), then designs its operating model, staffing, refresh cadence and kill rules.
- [`developer-certification-program`](./skills/developer-certification-program): Plans a developer certification or badge program: whether a credential is worth issuing, its tier, exam format, proctoring, renewal, fees, verification and retirement.

### Measurement

- [`devrel-metrics`](./skills/devrel-metrics): Builds a DevRel measurement framework: metrics tiered from reach to business impact, each with an attribution rule, a baseline-derived target, an owner and an action.
- [`devrel-analytics`](./skills/devrel-analytics): Builds the tracking plan behind those metrics: an event taxonomy, an identity spine, link-tagging discipline, source-confidence labelling, and funnel views.
- [`developer-survey-design`](./skills/developer-survey-design): Designs a recurring developer survey, from the decisions it informs to published results that state who answered, how many, and what the numbers can claim.
- [`devrel-competitor-analysis`](./skills/devrel-competitor-analysis): Benchmarks a competitor's DevRel motion from publicly observable signals and returns a gap plan with a close, ignore or counter verdict per row.

### Content & editorial

- [`devrel-content-calendar`](./skills/devrel-content-calendar): Plans a quarter of DevRel content as dated slots with named owners and reviewers, mixed by surface, pillar and shelf life, sized against real writing capacity.
- [`engineering-blog-post`](./skills/engineering-blog-post): Writes or edits a technical post a skeptical developer audience believes: evidence behind every claim, published trade-offs, runnable snippets, and no marketing voice.
- [`devto-playbook`](./skills/devto-playbook): Runs a vendor's or maintainer's dev.to presence: fit verdict, organization setup, canonical cross-posting, tag rules, AI disclosure, and an earn-first eight-week cadence.
- [`developer-case-study`](./skills/developer-case-study): Turns a customer's production deployment into a technical case study engineers believe: measured numbers, before-and-after architecture, published limitations, cleared approvals.
- [`devrel-newsletter-program`](./skills/devrel-newsletter-program): Designs a developer newsletter as a standing programme: whether to run one at all, a cadence the team's supply can fill, a section template, an owner with a backup, and pause and sunset rules.
- [`devrel-newsletter-issue`](./skills/devrel-newsletter-issue): Writes or reviews one developer newsletter issue: sourced item write-ups, releases without hype, labelled sponsors, code that survives email clients, and a pre-send check.
- [`devrel-newsletter-deliverability`](./skills/devrel-newsletter-deliverability): Diagnoses and fixes a developer newsletter's inbox placement: aligned authentication, a sending subdomain, one-click unsubscribe, warm-up, bounce handling and a ranked fix plan.
- [`devrel-newsletter-growth`](./skills/devrel-newsletter-growth): Plans how a developer newsletter's list grows and keeps readers: ranked signup channels with source tags, a consent-safe signup contract, a churn reading and per-source metrics.
- [`devrel-newsletter-sourcing`](./skills/devrel-newsletter-sourcing): Finds and gates one newsletter issue's items: which channels to read, the window since the last issue, primary sources over commentary, and whether a thin issue ships shorter instead of padded.
- [`devrel-newsletter-sponsorship`](./skills/devrel-newsletter-sponsorship): Sells sponsor slots in a newsletter you publish: a sellability verdict, an acceptance policy, a rate card priced from human clicks, the ad label and booking terms.
- [`build-in-public`](./skills/build-in-public): Designs a sustainable build-in-public practice: how far up the disclosure ladder to go, a cadence the maintainer can hold, the platform mix, and the boundaries.
- [`technical-video-script`](./skills/technical-video-script): Writes a shooting-ready script for a technical video or motion design explainer: a 30-second hook, code-on-screen pacing, chapters, and a pre-decided cut list.
- [`tech-podcast-interview-prep`](./skills/tech-podcast-interview-prep): Prepares a guest for someone else's podcast, interview or panel: show reconnaissance, a message spine, a self-contained opening answer, and clip-safe sound bites.

### Documentation

- [`developer-docs-structure-audit`](./skills/developer-docs-structure-audit): Audits a documentation set's structure against the Diátaxis modes, scores it on a TechDocs rubric, and returns a prioritized remediation queue.
- [`developer-quickstart-guide`](./skills/developer-quickstart-guide): Writes or audits a quickstart that carries a reader from zero to one verified success: a minimal path, expected output per step, fail branches, and a cold-run time budget.
- [`developer-tutorial`](./skills/developer-tutorial): Writes or audits a teaching tutorial: one concept per step, checkpoints the learner can verify and resume from, guidance that fades, and a demonstrable skill at the end.
- [`developer-how-to-guide`](./skills/developer-how-to-guide): Writes or audits a how-to guide that takes a competent reader through one real task: checkable prerequisites, variant handling, guarded destructive steps, and a closing verification.
- [`developer-troubleshooting-docs`](./skills/developer-troubleshooting-docs): Turns support tickets and error telemetry into pages a developer finds by pasting the error string, plus an error-code catalog wired back into the product's own output.
- [`docs-code-sample-standards`](./skills/docs-code-sample-standards): Defines the policy every documentation code sample must meet, then audits the existing sample corpus against it and returns a ranked fix queue.
- [`changelog-writing`](./skills/changelog-writing): Turns raw commits, pull requests and tickets into release notes developers actually read: what shipped, what it means in practice, and what breaks.
- [`version-migration-guide`](./skills/version-migration-guide): Writes or audits a breaking-change migration guide ordered by blast radius, with per-entry detection signals, before/after code, and a deprecation timeline.
- [`coding-agent-docs-optimization`](./skills/coding-agent-docs-optimization): Makes SDK, API or protocol docs something a coding agent integrates from unattended: crawler access, machine-readable entry points, self-contained pages, a measured success rate.
- [`docs-versioning-strategy`](./skills/docs-versioning-strategy): Decides how developer docs track several product, library or API versions: whether to version at all, a docs state per version (next, current, maintained, frozen, archived) derived from the support table, a ranked topology ladder from latest-only to a version switcher, source layout, a priced doc-fix backport rule, outdated-version banners and a retirement procedure.
- [`docs-localization-strategy`](./skills/docs-localization-strategy): Decides whether and how to localize developer docs per language: evidence that the source language is the barrier, a ranked translation ladder, the page set, source-commit pins with a bundled drift check, and an ownership gate before launch.

### Discoverability & SEO

- [`docs-seo`](./skills/docs-seo): Runs on-page and technical SEO for a documentation site: indexability, canonicals and hreflang across versions and translations, redirects, and an owner-assigned fix list.
- [`developer-docs-ai-visibility`](./skills/developer-docs-ai-visibility): Gets developer docs cited at the current version in AI assistant and AI search answers: pipeline diagnosis, version signals, owned and third-party corrections, and a repeated prompt panel scoring version-correct answers.
- [`developer-keyword-research`](./skills/developer-keyword-research): Builds a prioritized keyword list for technical queries, mined from docs search logs, support tickets and issue trackers rather than keyword-tool volume.
- [`readme-optimization`](./skills/readme-optimization): Audits and rewrites a repository README into a bail-fast funnel, with every claim verified against the source and badges that earn nothing pruned.
- [`github-profile-optimization`](./skills/github-profile-optimization): Rebuilds a personal or organization profile on a code host as a DevRel surface: the profile README, the pinned items, the bio fields, and the contribution signals.

### Community

- [`developer-community-launch`](./skills/developer-community-launch): Decides whether, where and when to launch a developer community, then plans its seeding, first 90 days, go/no-go criteria and shutdown criteria.
- [`developer-community-health`](./skills/developer-community-health): Designs a community health measurement framework: activity, responsiveness, contributor-funnel and sentiment metrics, honest instrumentation, and a report ending in decisions.
- [`developer-community-moderation`](./skills/developer-community-moderation): Writes a community's code of conduct and the moderation playbook behind it: enforcement ladder, reporting channels, incident runbook, moderator roster, platform controls.
- [`developer-feedback-loop`](./skills/developer-feedback-loop): Designs how developer feedback reaches product and comes back: one record of truth, problem-first records, a product-owned decision review, public status replies including the no, and loop metrics.
- [`developer-champions`](./skills/developer-champions): Designs an unpaid, perks-only champions program: intake, published selection criteria, behaviour-based obligations, an access-first perk ladder, fixed terms, and a cohort scorecard.
- [`developer-office-hours-program`](./skills/developer-office-hours-program): Designs a recurring developer office-hours or AMA program: format choice, a slot covering the users' time zones, a capped engineer rotation, a published scope card, empty-room and recording rules, and a write-up loop turning repeat questions into docs fixes.
- [`developer-meetup-program`](./skills/developer-meetup-program): Designs a recurring developer meetup or user group: host model, format menu, cadence, speaker pipeline, in-kind sponsors, the co-organizer ladder, and a health scorecard.

### Events & speaking

- [`conference-cfp-submission`](./skills/conference-cfp-submission): Turns a talk idea into a submission-ready proposal for one specific event: track fit, title options, abstract, takeaways, credibility package, and a committee self-review.
- [`tech-talk-outline`](./skills/tech-talk-outline): Turns an accepted abstract into a rehearsable outline: the one-sentence takeaway, a narrative arc, a minute-by-minute time budget, demo placement, and a slide skeleton.
- [`developer-live-demo-design`](./skills/developer-live-demo-design): Engineers a technical demo so it survives the stage: risk triage, enterable checkpoints, a one-command reset, offline mode, and a recorded fallback, shipped as a runbook.
- [`developer-event-sponsorship`](./skills/developer-event-sponsorship): Builds a developer-event sponsorship plan: which events to sponsor at which tier, the on-site activation, and how to prove the money worked.
- [`devrel-webinar-program`](./skills/devrel-webinar-program): Designs a recurring technical webinar series for developers: the series' one job, ranked formats, seasons sized to speaker capacity, attendance diagnosis, a replay plan, and a consent-bounded handoff contract with sales.

### Open source

- [`oss-launch`](./skills/oss-launch): Plans and runs an open-source launch end to end: name and license clearance, the readiness gate, positioning, channel sequencing, the launch-day war room, and measurement.
- [`producthunt-playbook`](./skills/producthunt-playbook): Runs a developer tool's Product Hunt presence: launch-or-skip verdict, self-hunted listing, maker conduct within the vote and AI-comment rules, relaunch timing, and the product forum.
- [`hackernews-playbook`](./skills/hackernews-playbook): Runs a vendor's or maintainer's Hacker News presence: Show HN readiness, hand-written title and first comment, thread conduct, Who is hiring posts, and recovery.
- [`oss-license-strategy`](./skills/oss-license-strategy): Chooses a project's license and contribution policy as one decision: copyleft strength, dependency compatibility, DCO versus CLA, dual licensing, and relicensing fork risk.
- [`oss-governance`](./skills/oss-governance): Chooses and documents a project's governance model: decision rights, maintainer promotion, voting rules, conflict escalation, succession, trademark control, and foundation options.
- [`oss-contributor-onboarding`](./skills/oss-contributor-onboarding): Designs and verifies the path from stranger to first merged contribution: the CONTRIBUTING file, the good-first-issue queue, a cold clone-to-passing-tests command, and the review loop.
- [`oss-issue-triage`](./skills/oss-issue-triage): Designs a triage system maintainers can sustain: response targets sized to real capacity, a label taxonomy, intake cuts, triage duty, and a closing and staleness policy.
- [`oss-maintainer-sustainability`](./skills/oss-maintainer-sustainability): Plans how a maintainer carries a project without burning out, or leaves it without stranding users: time budget, published limits, co-maintainers, and a clean exit.
- [`oss-security-disclosure`](./skills/oss-security-disclosure): Runs coordinated vulnerability disclosure from the maintainer side: SECURITY.md and private reporting, triage and CVSS scoring, embargo negotiation, CVE and advisory, patched releases, downstream notice, and EU CRA checks.
- [`oss-release-policy`](./skills/oss-release-policy): Writes a project's release contract as RELEASES.md: the versioning scheme ranked for who reads the number (SemVer, 0.x, CalVer, Go major paths, PEP 440), what counts as breaking, channels, supported versions sized to maintainer hours, backports, cadence and deprecation.
- [`oss-distribution-strategy`](./skills/oss-distribution-strategy): Designs a project's ongoing distribution mix after launch: registries, discovery surfaces, curated lists, downstream packaging and release cadence, ranked against maintainer capacity.
- [`open-source-company-strategy`](./skills/open-source-company-strategy): Decides what a company open-sources and what stays proprietary, names the motive for each side of the line, says who owns the decision, and what it never closes.
- [`open-standards-strategy`](./skills/open-standards-strategy): Decides how a company engages a named standard or protocol, in which venue, under which patent-licensing mode, with a conformance plan and a kill rule.

### OSS funding

- [`oss-monetization`](./skills/oss-monetization): Chooses how one open-source project earns money for its own maintainers: the offer a company can buy, the paid boundary, ownership and license checks, and the hours it costs.
- [`oss-sponsors-fundraising`](./skills/oss-sponsors-fundraising): Designs a maintainer-side sponsorship program: the tier ladder and its pricing, rewards that stay deliverable at scale, and the invoice-and-entity path a company needs to pay.
- [`oss-sponsors-brand-strategy`](./skills/oss-sponsors-brand-strategy): Builds a company's open-source sponsorship portfolio: which projects and maintainers to fund, through which allocation model, at what amount each, and how to prove it worked.

### Business model

- [`devtools-business-model`](./skills/devtools-business-model): Chooses the business model for a developer tool, from open core to consumption metering to OEM licensing, and the go-to-market each one forces.
- [`devtools-pricing-strategy`](./skills/devtools-pricing-strategy): Designs a developer tool's pricing and packaging: the value metric, free-tier limits, the tier ladder, price points bounded by real ceilings, and a safe price-change plan.

### Brand & press

- [`tech-press-relations`](./skills/tech-press-relations): Runs press and light analyst relations for a developer product: news qualification, the angle, a reporter-to-beat media map, the pitch, embargo handling, and the press page.
- [`tech-employer-branding`](./skills/tech-employer-branding): Designs an employer-brand strategy for attracting software engineers: the engineering EVP, the channel plan, a verification-surface audit, and the measurement baseline.

## 👤 Contributors

![Contributors](https://contrib.rocks/image?repo=samber/developer-relations-skills)

## 💫 Show your support

Give a ⭐️ if this project helped you!

[![GitHub Sponsors](https://img.shields.io/github/sponsors/samber?style=for-the-badge)](https://github.com/sponsors/samber)

## 📝 License

Copyright © 2026 [Samuel Berthe](https://github.com/samber).

This project is under [MIT](./LICENSE) license.
