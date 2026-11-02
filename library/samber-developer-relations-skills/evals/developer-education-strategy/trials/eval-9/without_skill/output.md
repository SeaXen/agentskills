> Simulated council — each take is built from the advisor's published frameworks and positions, not their actual review of Fernlow.

## The question before the council

Marketing wants to gate Fernlow's learning content behind signup and launch a "Fernlow Certified" credential. You sense a mismatch but can't name it. Stakes: Fernlow's entire growth motion is 40K monthly organic docs visitors, zero sales team — the docs *are* the funnel.

## Seated: Byron Sharp, April Dunford, Alex Hormozi, Seth Godin

Sharp and Dunford diagnose the structural mismatch; Hormozi steelmans marketing's instinct instead of strawmanning it; Godin reframes what's actually being asked of the developer.

---

### Byron Sharp — mental & physical availability

Sharp's evidence (*How Brands Grow*) is that brands grow by being easy to buy and easy to notice — physical availability — not by deepening loyalty in an existing base. Gating docs is a direct attack on physical availability: it removes Fernlow from every search result, every Stack Overflow answer, every "how do I migrate X" query that currently lands an anonymous developer on your page. Google can't index a signup wall. Neither can an LLM's crawler, which is increasingly how developers now find answers.

The 40K monthly visitors aren't a "top of funnel to be converted" — for a bottom-up tool with no sales team, they *are* the business. Sharp would call the certification plan a loyalty-program instinct applied to a reach problem: it optimizes for depth of engagement with people who already found you, while doing nothing for the much larger pool who haven't yet.

**Bottom line:** you'd be trading category-wide discoverability for a smaller, slower-growing list — backwards for a company whose only real asset is reach.

### April Dunford — positioning against real alternatives

Dunford's method starts with "what would the customer use instead of you." A developer choosing a migration CLI is comparing Fernlow against three alternatives: a competitor's free tool, a hand-rolled script, or doing nothing. Every one of those alternatives has open docs. Gating yours doesn't make Fernlow look premium — it makes it look like more friction than the free competitor, at the exact decision moment you can least afford friction.

Certification is a positioning claim too, and positioning claims only work when they map to a real, externally-recognized problem. "Fernlow Certified" on LinkedIn only has value if an employer somewhere is filtering candidates on it. Right now nobody is — there's no enterprise motion pulling demand for credentialed hires. A certification with no market pull isn't a positioning asset, it's a badge nobody asked for, and cheap-looking badges cheapen the brand that hands them out.

**Bottom line:** neither move addresses "why choose Fernlow over the alternative" — they're both solved-problem-in-search-of-a-solution moves borrowed from categories where Fernlow doesn't yet compete.

### Alex Hormozi — steelmanning the ask, then pricing it honestly

Hormozi's value equation says every ask (email, signup, time) has to be justified by the value on the other side. Marketing isn't wrong that email capture has value — a list you own is worth more than a list Google owns. The mistake is *where* they're proposing to take the ask. Gating the docs charges the toll at the door, before the developer has experienced any value — that's the highest-friction, lowest-conversion place to ask for anything.

The better version of marketing's instinct: gate the stuff that's genuinely bonus, not foundational. A downloadable migration playbook, a comparison-of-approaches whitepaper, a template repo, office-hours access — content that's additive on top of docs someone already got value from, not a wall in front of the reference material they need to get unstuck. That's an email-capture mechanism with a real value exchange behind it, instead of a tax on the acquisition channel itself.

**Bottom line:** the "capture emails" goal is legitimate — the execution (gate the core product) is where the value equation breaks.

### Seth Godin — permission and the smallest viable audience

Godin's permission marketing framework: permission is earned by giving first, not extracted by withholding. A signup wall in front of learning content isn't permission marketing, it's a toll — and developers, more than almost any audience, route around tolls (mirrors, cached versions, "just use the competitor's free docs").

On certification specifically: Godin would ask who the "smallest viable audience" for it actually is. Right now it's nobody — there's no community of practice, no hiring managers, no tribe that has decided "Fernlow expertise" is a status marker worth signaling. Certification programs work when they formalize status that already exists informally (top contributors, known experts, conference speakers). Fernlow hasn't built that informal status yet, so a formal credential on top of nothing is premature — it's building the trophy case before anyone's played a game.

**Bottom line:** earn attention and status informally first — community recognition, contributor visibility, case studies — then formalize it once developers are already bragging about Fernlow unprompted.

---

## Where the council disagrees

1. **Sharp vs. Hormozi on whether gating can ever work.** Sharp's reach argument says any gate on core content is a net loss, full stop. Hormozi says the gate itself isn't the sin, the *placement* is — gate bonus content, not the entry point. What would settle it: A/B the funnel — measure organic-search-driven docs traffic and downstream conversion before and after gating anything, on a low-traffic doc page first, not the whole library.

2. **Dunford vs. Godin on what certification is actually for.** Dunford frames it as a positioning claim that needs external market pull to mean anything. Godin frames it as a status object that needs an existing community to formalize. Both converge on "not yet" but for different reasons — worth knowing which one applies, because it changes what "ready" looks like (external hiring demand vs. internal community maturity).

3. **The real tension underneath both proposals:** marketing is being asked to show a number (emails captured, certifications issued) that's legible to a report, while the thing actually driving Fernlow's growth (40K monthly organic, zero CAC) doesn't produce a dashboard marketing gets credit for. That's very likely the root of "feels off but can't articulate why" — the proposal optimizes for what's measurable to marketing, at the expense of what's actually working.

## Chair's synthesis

**Don't gate the docs. Don't ship the certification — not yet, not in this form.**

- **Keep documentation fully open and indexable.** It's the acquisition engine responsible for the entire 40K/month, zero-sales-team growth motion. Gating it doesn't make you look premium to a developer with two free alternatives one tab away — it makes you look like more friction.
- **If marketing wants an email list, gate *bonus* artifacts, not core content** — migration playbooks, comparison guides, templates, a "Fernlow in production" report. Real value exchange, zero cost to organic discovery. This is a much smaller ask than "wall off the whole learning library," and it's the version of the idea that's actually defensible.
- **Capture intent signal without a wall**, instead: optional newsletter opt-in in the CLI itself post-successful-migration (the moment of highest goodwill), a lightweight "was this helpful" + optional email on docs pages, GitHub stars/watchers as a public, frictionless proxy for reach.
- **Shelve certification until there's a reason for it to exist** — a real community of visible experts, and ideally some external pull (an employer, a partner, a hiring manager) that would actually value the badge. If you want a status mechanic now, do the cheap version first: highlight top contributors, feature power users in case studies, give conference talk slots — see if an informal "Fernlow expert" identity forms before building a formal program around it.
- **Tripwire:** if you do test gating anything, watch organic search traffic and referring-domain count on the gated pages for 60–90 days (Sharp's warning). A drop there is the actual cost of the plan, and it won't show up in "emails captured" — which is exactly the metric marketing will be watching instead.
- **Execute with:** `docs-as-marketing` for restructuring docs as an explicit acquisition/activation channel instead of a wall; `free-tier-strategy` if you want to design the bonus-content gate properly; `gtm-developer-ecosystem` (student-program arc) if certification comes back once there's real community pull behind it.