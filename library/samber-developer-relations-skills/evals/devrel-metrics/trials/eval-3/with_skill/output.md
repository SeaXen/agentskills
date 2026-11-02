**Do first: add one question to your signup form.** "How did you first hear about Thistledown?" Seven fixed options plus free-text Other. About one hour including form change. This, not UTM hygiene, is the instrument that answers your head of DevRel's question.

## Verdict on the plan

Half right. Keep UTMs, scope them way down. UTM-everything as the backbone for channel totals fails. Structural reasons — more tagging fixes none of them:

1. Tagged links see taggable clicks only. Hallway conversation, podcast, colleague recommendation, AI assistant: no pixel exists for any. DevRel touches sit early and off-web.
2. Referrers strip. Aggregators, chat clients, privacy browsers, PDF and slide links. Roughly 70% of AI-assistant traffic arrives with no referrer and lands "direct" (one newsletter's figure, directional). Large direct bucket = normal, not bug.
3. Developer audience blocks client-side analytics. Plausible measured 58% of a tech audience blocking Google Analytics, 82.3% on Linux, 88.3% on Firefox (August 2021, HN/Reddit-heavy site, directional). Web-analytics channel totals compare tracking coverage, not channel performance.
4. Your conversion event carries no UTM. Real adoption = `npm install` or first reconciled transaction. Installs and clones have no referrer. UTMs on repo links measure GitHub page visits, one step removed. npm downloads are request counts (CI and mirrors included), not people; npm itself treats under ~50/day as mostly automation.
5. Effort math fails. "Everything" = naming convention plus per-campaign tag discipline on every surface, forever. Your 3h/week goes to tag hygiene, nothing left for analysis. Classic failure mode: instrumenting before deciding what deserves a target.

Scope note: which numbers may claim what = metrics layer, this answer. Building the tag taxonomy and event tracking once metrics chosen = separate analytics layer (`devrel-analytics` in this collection). Hand instrumentation there.

## What UTMs stay for

Artifact-vs-artifact comparison. Which talk's QR drove more docs sessions. Which newsletter issue pulled more clicks. Never program totals. Rules: one short URL per talk or event, never reused. Record the destination's pre-period baseline, or no lift claim possible.

## First month, inside 3h/week

1. Week 1, ~1h: signup attribution question. Options, frozen all year: search engine or AI assistant; a colleague or friend; conference talk, meetup or workshop; podcast, video or livestream; blog post or newsletter; open-source project or repository; social media; Other free-text. One question only. Read the free text quarterly, not just the counts.
2. Week 1, ~30min: start monthly snapshot of the GitHub repo traffic panel plus npm stats. GitHub keeps traffic 14 days only. Registry series last months, not years. Snapshot the day a metric enters the sheet.
3. Week 2, ~1h: one-page UTM convention. Scope: talk QRs, newsletters, plus one persistent docs-vs-GitHub source tag. Not every repo link.
4. Week 3, ~1h: write the attribution rule down, before the period starts. Name methods in use, what each may claim, lookback window, blind spots. Rule invented after the quarter = narrative.
5. Week 4: first monthly read. Channel mix from the signup question, labeled "self-reported first touch". Tagged links beside it as artifact comparison only.

Caution: at your volume, monthly counts per channel run small. Below ~30 events per period (borrowed convention, not a measured cutoff): report the raw list with dates, not a rate. Small-N percentages swing wild and trigger bad decisions.

## Answer five things before the full framework

1. What decision do channel totals feed? Kill a channel, shift effort, renew budget? Number with no decision attached gets cut.
2. Funded driver, in the budget-holder's words: adoption, enablement, ecosystem, product input?
3. Adoption motion. Payments reconciliation smells company-led: developer evaluates, security or finance signs. If so, count accounts alongside people; pipeline answers 2-4 quarters late; name a leading indicator for the interim.
4. Data on hand with zero new engineering: product analytics, CRM, docs analytics? Sales-ops cooperation? No cooperation deletes influenced pipeline outright — named in blind spots, not parked at bottom of sheet.
5. Hard date first numbers must land? Deadline inside one quarter promotes whatever reads now.

Decide explicitly: budget from a sales or marketing line makes influenced pipeline live (shared credit, word "influenced" never drops). Other owner: route connections to teams instead, no sales metric on DevRel.

Then the framework proper: 5-8 metrics, six fields each (definition, source, baseline, threshold, owner, action), at least one product or business impact tier, spine picked with you. Built section by section, you approve each.

## Blind spots to publish on day one

Docs readers who never sign up. AI assistants answering from your docs without a visit. Word of mouth inside companies. Installs with no person attached. Stating the gaps up front is what makes the rest believable.

Next action, under 2 minutes: open a ticket for the signup question, paste the seven options plus Other, mark the list frozen for the year.