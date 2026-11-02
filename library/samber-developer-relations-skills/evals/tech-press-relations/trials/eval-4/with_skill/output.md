# Hollowbrook — becoming the name cited on supply-chain risk

**Verdict up front:** you're describing a citation asset, not a launch. Don't build a press plan around an announcement — you don't have one, and manufacturing one would waste the thing you actually have. Build a recurring, data-backed report from the telemetry you already collect, and let *that* be the vehicle. Press coverage is a byproduct of that asset existing, not the goal itself.

Below is the reasoning, the concrete plan, and the open questions I can't answer for you.

## What you already told me (mapped to the qualifying questions)

- **The news:** none, by design. No launch, no date to hit.
- **Timing:** unscheduled — this is an advantage, not a gap. It means the asset can be built right instead of fast.
- **The proof:** aggregate dependency-resolution telemetry, legal-cleared for publication. This is the one input that changes everything else.
- **The outcome you're trading for:** explicitly a compounding asset — "the name people cite... for years" — not a placement on a date. That phrase alone answers most of the angle-selection logic below.
- **Founder:** no public writing track record. This constrains *how*, not *whether*.

Still open, and they change tactics, not strategy: who has to believe this first (developers choosing tools vs. buyers/security leads vs. analysts), your effort ceiling (how much engineering and legal time you can spend per cycle), geography, and whether your adoption motion is bottom-up or enterprise. I'll flag where each one matters below.

## Step 1 — qualification, applied to the asset you're about to build

Run against the five tests, but against the *report*, not against "Hollowbrook" as a subject:

- **Newness** — yes, if the methodology produces a number nobody else can see. A registry mirror has a vantage point on dependency resolution that individual maintainers, individual companies, and most researchers don't.
- **Consequence** — yes, if the findings tell someone to do something differently: security teams re-evaluating pinning policy, maintainers seeing how long vulnerable versions keep getting pulled after a fix ships, platform teams sizing the blast radius of typosquatting or dependency confusion attempts.
- **Evidence** — the data is the evidence, by construction.
- **Conflict or shift** — supply-chain risk is a beat reporters are already covering (incident-driven, regulation-driven). You're not inventing the conversation, you're bringing the first hard numbers to it.
- **Tellability** — legal has cleared aggregate publication, so yes, once the methodology and anonymization are locked.

This passes clean, once built. It does not pass today, because today there's no report — that's the actual gap, not "no news." Close it by building the thing, not by finding a news hook to hang the company on this week.

## Step 2 — the angle, and why it breaks the normal ranking

The skill's default angle-efficiency order ranks "the number" near the bottom on effort and compliance cost — collecting proprietary data and clearing it for publication is normally the most expensive angle to run. Two explicit exceptions override that ranking, and you hit both simultaneously:

1. The data already exists as a byproduct of running the product — no collection work needed.
2. You explicitly want a compounding asset, not a placement.

When either holds, the number "beats everything above it." You have both. This isn't a close call — it's the correct angle by the skill's own logic, not a preference.

**Pressure test:** if Hollowbrook didn't exist, would a reporter still want this data? Yes — the story is the ecosystem's exposure, Hollowbrook is the instrument that made it visible. That's the shape you want: the product is evidence, not the subject.

**What this displaces:**
- *The broken system* (founder as standing voice) — highest value after the number, but it costs "a standing job defending it in public," and your founder has no track record to spend. Don't start here. Build toward it (see below).
- *The practitioner* — available (an engineer can go on record), but it's a one-time story, not a compounding one. Use it as a secondary, not the flagship.
- *The shift* — cheapest, but purely tactical. Useful for attaching edition one to whatever supply-chain story is already running the week you publish; not a strategy on its own.
- *The underdog* — no comparative claim in your brief, drop it.

## The asset itself

A recurring benchmark report — working name only, replace it: *State of Dependency Resolution Risk* or similar. The mechanism that makes this compound: "a benchmark published annually becomes a citable event that earns coverage on a schedule." Annual or semi-annual, not one-off. The first edition is the expensive one; every edition after it is cheaper and starts from an audience that already expects it.

**Before anything gets pitched, lock down:**

- **Methodology, in the open.** What counts as a "dependency-resolution event," what registries/ecosystems are in scope, what volume, over what window. Publish the query definitions and an anonymized/aggregated dataset extract even if raw logs can't be, so a stranger can rerun the analysis.
- **Anonymization threshold, confirmed with legal beyond "cleared for aggregate publication."** No org- or IP-identifying data in anything public. Get the actual k-anonymity or aggregation floor in writing before drafting a single sentence of the report — this is the compliance-review item the skill flags as the number angle's real cost, and it's the one thing that can't be fixed after publication.
- **Comparison rows where you look bad.** If the report ranks ecosystems, registries, or practices by risk, you're making a comparative claim by construction — that draws a challenge within hours unless the methodology is public and rerunnable. Decide now whether you're naming specific ecosystems/registries or staying at the pattern level (e.g., "typosquatting attempts," "time-to-remediation after CVE disclosure," "unmaintained-package pull-through") — the second is safer for edition one, the first is more citable if you can defend it.
- **Limitations section, written honestly.** You see mirror traffic, not the whole ecosystem. State that plainly — it's what lets the report survive its own comment section instead of getting picked apart for overclaiming.

## The founder problem — solve it through the asset, not around it

He doesn't need to be a writer to be the spokesperson for edition one. Two roles, sequenced:

- **Edition one:** the engineer or data lead who ran the analysis authors the piece and does the technical interviews. The founder gives two or three on-record quotes — a position, not a personality — prepared and rehearsed, including the honest answer to the hardest question a security reporter will ask (what this data *can't* tell you). That's a far lower bar than an op-ed, and it's the only role the skill treats as load-bearing for a first outing.
- **Editions two onward:** once the report is being cited unprompted, the founder has standing he didn't have before — earned by the data, not asserted. That's the on-ramp to the broken-system angle: a founder who's spent a year publishing the numbers on typosquatting or remediation lag has a defensible position to argue in public. Trying to install him as a thought leader before that exists gets ignored — an opinion with no track record behind it is exactly what a technical reporter discounts on sight.

This is the actual mechanism for "the name people cite" — it's earned across editions, not declared in edition one.

## Distribution for edition one

No embargo mechanics needed — nothing here is time-sensitive, and an embargo only pays for itself when you need several outlets bound to one moment. Two lighter-weight options instead:

- **Publish on your own surface first**, then pitch it as existing, citable work. Lowest coordination cost, no leak risk to manage.
- **Optionally, one exclusive** to a single reporter whose readership is exactly the audience that has to believe this (developer-native trade press or a security-focused outlet, once you've identified one through real verification — see below), if the story needs reporting time only a committed journalist will invest. Offer it, give them a deadline to answer, move to open publication if they pass.

**On the media map:** I'm not going to hand you a list of reporters — inventing names or guessing contact addresses is exactly the failure mode this skill exists to prevent, and a wrong send burns the outlet for the next cycle. The process: pull the last five articles on supply-chain risk from the outlet classes that matter here (developer-native trade press, security trade press, and — since regulation is part of this story — enterprise-IT trade press), read the last five bylines of each candidate reporter, confirm they still cover the beat, score on beat match first. Twenty to forty verified names, not a database purchase. This is a few hours of real work, and it's worth doing once you have a draft report in hand, not before.

## Between editions — this is what actually compounds it

An annual report earns coverage on a schedule. The faster path to "the name people cite" is being the standing source *between* editions: when a supply-chain incident breaks — a compromised package, a new CVE with real blast radius, a registry incident — your data team can say something specific within the first day, because you have the dataset already sitting there. That's the highest-leverage move available to you, and it costs nothing to set up beyond deciding in advance who's allowed to speak fast. Publish the same point on your own site the same day, so there's a trail independent of whether the reporter uses it.

This only works if the underlying telemetry pipeline and legal sign-off are already standing infrastructure, not something rebuilt per incident — another reason to invest in the methodology now rather than per-story later.

## Analyst relations

Supply-chain risk sits at the intersection of developer-facing and buyer-facing concern — SBOM requirements, procurement security questionnaires, compliance posture. Worth a briefing with both a practitioner-focused analyst and a buyer-side research firm once the first report exists: bring the engineer, spend the time on the problem and the evidence rather than a product walkthrough, and ask what they're seeing in the category — that's the part you take home. Be explicit with your team that a briefing buys a correct mental model in procurement conversations, nothing more; it does not buy placement in any evaluation.

## Measurement — tied to the actual goal

You're not optimizing for a traffic spike. Track:

- Whether the report gets cited, unprompted, in later articles about supply-chain risk — this is the direct signal for "the name people cite."
- Whether it surfaces when you ask an AI assistant a category question — spot-check this per edition.
- Referring domains and authority from coverage — durable, unlike a traffic bump.
- Inbound from analysts, other reporters, and partners you couldn't have reached otherwise.

Capture your branded search, direct traffic, and docs/registry traffic baseline *before* the first edition ships — otherwise nothing afterward is attributable. Compare against your own baseline, never an industry average; the reply-rate and pitch-volume statistics that circulate in PR content are largely uncited and often contradictory. And if anyone proposes measuring this with advertising-value-equivalency, refuse it — that's not a house preference, it's the industry's own standing position (AMEC's Barcelona Principles).

## What would blow this up

- Shipping a "look how much traffic our mirror sees" post before the methodology is solid — reads as an announcement, not a finding, and won't survive scrutiny.
- Naming specific ecosystems or registries as risky without a public, rerunnable harness — invites a comparative-claims fight you can't unpublish your way out of.
- Putting the founder in front of a reporter as an opinion voice before edition one exists — an untested spokesperson with no data behind him gets a polite pass, not a story.
- Treating this as a one-time report instead of a cadence — the entire value of "for years" comes from the schedule, not any single edition.

## Still need from you before this gets fully specific

- Effort ceiling: how much engineer and legal time per cycle — this decides whether the first edition ships in weeks or over a quarter.
- Primary audience ranking: security/compliance buyers, individual developers, or analysts first — changes which outlet classes and which analyst firms to prioritize.
- Geography and language.
- Whether your adoption motion is bottom-up or enterprise-led — changes whether the report leans toward practitioner detail or procurement-relevant framing.

Answer those and the plan above turns into a dated build schedule for edition one. Until then, the direction doesn't change: build the report, let the founder earn his voice off the back of it, and treat every incident in the news between editions as a chance to be the source reporters already know will have the number.