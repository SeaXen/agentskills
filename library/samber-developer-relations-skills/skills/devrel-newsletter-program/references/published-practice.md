# Published practice from real developer newsletters

Every figure the skill quotes, its source, and how far it can be pushed. Operator figures come from sales material and media kits; benchmark figures come from email-platform aggregates across all industries. Handoff and shutdown evidence is first-person account, not measurement.

## Contents

1. Start decision and supply
2. Cadence in the field
3. Cadence versus engagement
4. Inclusion rules curators publish
5. Section templates
6. Ownership models
7. Handoffs, pauses and shutdowns
8. Metrics after mail-privacy features
9. Consent and stream separation

## 1. Start decision and supply

- **This Week in Rust (TWiR):** its editor reported about 7-10 link submissions per issue when she started in early 2020, and 40+ pull requests per week six years later. Supply became abundant; editor time became the constraint.
- **Supabase:** announces features in a monthly update "often limited to a blast radius containing existing users", and does top-of-funnel work during Launch Week. The newsletter is a retention channel, and the same update is also posted to the changelog and community discussions.
- **incident.io:** published 200+ weekly changelogs over four years. Weekly posts into customer chat channels were "a little noisy for some", so the team added less frequent customer changelogs covering several weeks. The changelog is the supply; the digest is the newsletter layer.
- **Swift Weekly Brief:** started because the Swift Evolution mailing list was overwhelming to follow. Its founder expected the new Swift Forums to reduce that need. A newsletter's case weakens once native channels become easy to follow.
- **Console.dev:** reports that 68% of readers signed up to a featured tool and 77% have coded for 5+ years. This is the kind of demand evidence that justifies an email channel.
- **Cloudflare's blog email** is a daily automated post notification, not a curated newsletter. Feed-only is a real shape large vendors use.

## 2. Cadence in the field

| Newsletter | Owner | Cadence | Rhythm it rides |
|---|---|---|---|
| This Week in Rust | volunteer editors | weekly | Rust project's weekly PR, RFC and Final Comment Period cycle |
| Golang Weekly | commercial curator (Cooperpress) | weekly, breaks announced in the editor's note | ecosystem news |
| KubeWeekly | CNCF community editors | weekly | CNCF ecosystem and events |
| Last Week in Kubernetes Development | Kubernetes contributor-experience group | weekly | code changes and release schedule |
| Console.dev | independent | weekly | 2-3 tool reviews per issue |
| GitHub Insider | vendor | twice monthly (monthly at its 2023 relaunch) | product deep dives |
| Stripe Developer Digest | vendor | monthly | API, SDK and product updates |
| HashiCorp | vendor | two monthly letters, developers and tech leaders | product and events |
| Supabase Developer Update | vendor | monthly | launch weeks, previewed then recapped |

Community digests ride the project's own weekly governance process. Vendor newsletters ride the launch calendar, mostly monthly or twice monthly.

## 3. Cadence versus engagement

MailerLite's sending-frequency guide (cross-industry, not developer-specific, a different sample from its annual benchmark):

| Frequency | Open | Click |
|---|---|---|
| under 1 per month | 35.11% | 3.74% |
| 1-3 per month | 33.48% | 4.32% |
| weekly | 33.22% | 4.87% |
| daily | 30.04% | 4.97% |

Clicks rise with frequency and opens fall slightly. These click rates sit far above the same vendor's 2.09% all-industry median, so the samples differ. Read the direction, not the numbers. Higher frequency only helps when supply fills it.

No measured study of irregular sending exists for developer newsletters. The field evidence is qualitative:

- incident.io's first changelog principle is "We write an update every week. No exceptions," and it tracks delays.
- Golang Weekly announces planned breaks rather than skipping silently.
- Swift Weekly Brief's archive shows a six-month gap before its final issue: the usual decay shape is widening gaps, then silence.

## 4. Inclusion rules curators publish

- **KubeWeekly (CNCF):** content must interest the community "as a whole, not just the users of a single commercial platform"; a commercial announcement that does not explain benefits or usage is not appropriate; no gated content outside the webinar section; editors need a vendor-neutral perspective.
- **This Week in Rust:** excludes paywalled content and anything that requires sharing an email address. It moved project and tooling links to a community forum feed once reviewing them by pull request became unsustainable for volunteer editors.
- **Console.dev:** no sponsored reviews; advertising is clearly marked and separate, and sponsors must meet the same selection criteria.
- **Cooperpress (Golang Weekly, JavaScript Weekly):** sponsored links carry a "sponsored" tag, and sponsor copy is reviewed for tone.
- **TLDR:** its founder's rule, reported by Inc. in 2025: "If you wouldn't forward this to your colleagues in Slack, don't put it in the newsletter."
- **Vendors** publish no numeric own-versus-external ratio. Stripe's digest mixes own updates with a community-tutorial slice and a submission call; GitHub Insider is almost entirely GitHub content; HashiCorp mixes product, events and some industry news.

## 5. Section templates

**This Week in Rust:** community updates (official, foundation, project and tooling, observations, walkthroughs, research), crate of the week, call for participation, updates from the Rust project, approved RFCs and final comment period, upcoming events, jobs, quote of the week, editors.

**Golang Weekly:** signed editor's note, primary sponsor, lead items with 1-3 sentence summaries, labelled sponsor block, in-brief bullets, more articles and quick links, code and tools, classifieds, elsewhere in the ecosystem, footer with curators and unsubscribe. Section names drift slowly; the order stays.

**Stripe Developer Digest:** updates, learn, community, stay connected, submission call.

Why the template matters:

- Readers navigate by section: TWiR readers say they read specific sections more than others.
- Templates make the work divisible: TWiR recruits editors per section and keeps a publishing guide in its repository.
- Templates make tooling and handoff possible: Swift Weekly Brief's docs and automation let a successor take over within weeks.

## 6. Ownership models

| Model | Example | Observed risk |
|---|---|---|
| Single founder-editor | Python Weekly (one curator for 10+ years), Console.dev | key-person risk, no published succession |
| Paid curator team | Cooperpress titles; TLDR (22 full-time staff plus ~30 part-time writers, 2025) | titles paused or closed when economics faded |
| Volunteer editorial team | TWiR (11 editors in 2026); KubeWeekly (editors commit one year, 1-2 hours a week) | submission volume can outgrow volunteers |
| Vendor-run | GitHub Insider, Stripe, HashiCorp, Supabase | public archives lapse quietly when the owner moves on |
| Duo-run media | Changelog News | one co-host left in 2026 after 452 newsletters; the other continued |

Runbook elements operators publish:

- incident.io: a seven-step checklist with draft location, a fixed design deadline, publishing step, a rota of product managers for review, a social-card check, automated reminders and pre-assigned authors.
- TWiR: submission guide, written inclusion criteria, a reproducible build, per-section editors.
- KubeWeekly: written editor requirements and a submission form.

## 7. Handoffs, pauses and shutdowns

| Newsletter | When | What happened | Stated reason |
|---|---|---|---|
| Swift Weekly Brief, first editor | Jan 2018, issue 100 | stepped down, community handoff, cadence cut to biweekly | burnout from the weekly pressure; forums reducing the need |
| Swift Weekly Brief, second editor | Sept 2020 | mailing list shut after issue 170, web edition continued | editor moving on; the list was a cost covered by sponsors |
| Swift Weekly Brief | June 2022, issue 201 | archive stops; the domain later lapsed | none stated |
| DB Weekly (Cooperpress) | June 2021, issue 360 | announced "going into hiatus" | not stated |
| Mobile Dev Weekly (Cooperpress) | Dec 2021, issue 383 | closed after ~8 years | not stated |
| This Week in Rust | 2026 | restructured intake instead of closing | volume beyond volunteer capacity |

Lessons the record supports:

- Each Swift Weekly Brief handoff cut cadence or distribution: weekly, then biweekly, then web-only, then stale. Docs and automation preserved the site for a time, never the list or its funding.
- The first editor paid for the mailing list personally, so the list was the first thing at risk in a handoff.
- No operator publishes formal kill criteria. The triggers in the skill's sunset table generalize the reasons stated above.

## 8. Metrics after mail-privacy features

- Apple Mail Privacy Protection launched on 20 September 2021 and pre-fetches messages, which registers opens nobody made. Twilio SendGrid reported MPP triggered 18.2% of unique opens it processed from launch.
- Omeda measured unique open rates rising from 15.2% to 29.0% six months after launch, with click rates unaffected.
- Cooperpress footnoted in 2022 that its open rate was "approximately 0.8-3.7% inflated", a small effect, plausibly because developer audiences use fewer Apple Mail clients.
- Golang Weekly's media kits report opens alongside multi-issue reach: about 68% of subscribers opened at least one of the last five issues (2024 kit), with a single-issue open rate near 49%, far above platform averages, as is typical for niche developer weeklies. Both are open-based, so any subscriber whose mail client pre-fetches counts every time: copy the idea with clicks (unique clickers across the last N issues), not with opens.

Platform benchmarks (all industries, not developer-specific):

| Source, period | Segment | Open | Click | Click-to-open | Unsubscribe |
|---|---|---|---|---|---|
| MailerLite, Dec 2024 - Nov 2025, medians | all | 43.46% | 2.09% | 6.81% | 0.22% |
| MailerLite, same | software and web apps | 39.31% | 1.15% | 5.4% | 0.2% |
| Mailchimp, data as of Dec 2023 | all | 35.63% | 2.62% | n/a | 0.22% |

- MailerLite's median unsubscribe rate rose from 0.08% to 0.22% between 2024 and 2025, which it attributes to Gmail letting people unsubscribe without opening the email, under the 2024 bulk-sender rules. An unsubscribe rise across that window is not, alone, a content signal.
- No developer newsletter publishes reply rates. Track replies and forwards as qualitative evidence.

## 9. Consent and stream separation

- **US, CAN-SPAM (FTC):** a message mixing commercial and transactional content counts as commercial if the subject line suggests a commercial message, or if the transactional part does not come first. Commercial mail needs an opt-out and a postal address. Keep newsletter content out of billing, security and account email.
- **UK, PECR (ICO):** marketing email to individuals needs specific consent, except the soft opt-in for existing customers about similar products, with an opt-out offered at collection and in every message. Consent to receive a receipt does not cover marketing. Corporate addresses fall outside the consent rule, but the ICO still advises an opt-out.
- **EU, ePrivacy Directive:** prior opt-in for individuals, as a separate checkbox never bundled with terms, except the Article 13(2) soft opt-in for existing customers about similar products, with an opt-out at collection and in every message. Rules for business addresses vary by member state; Germany, for example, requires consent for them too.
- **Double opt-in** is not legally mandated in these regimes; it is the usual way to evidence consent.
- Community curators refuse links that capture email addresses, so a vendor newsletter used as a gated-content funnel loses ecosystem credibility.
