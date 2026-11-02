## Audience and scope

Audience for this README: **both** — engineers at the evaluating banks/insurer deciding whether ledgerlink fits their stack, and their security/procurement teams deciding whether to let it in the door (Q3/Q4 of the interview: mixed audience, company-gated adoption). That mix means Step 8 (enterprise trust signals) applies directly — the security teams "asking questions" are the exact reader Step 8 is written for.

I don't have the actual repo or README text to run the mechanical audit, verify claims against the source, or execute the install path — so nothing below should be read as a scored Band A/B result. Treat the two open items (no named alternatives given, current licence not stated) as findings per the skill's own rule: unanswered interview questions are findings, not blockers.

## The foundation question first, because it's the one with a legal sign-off you can't walk back

Before any README line: **don't let the README get ahead of a board decision that hasn't happened.** Foundation affiliation is the single most expensive, least reversible item on the enterprise trust-signal list — trademark/IP assignment, legal sign-off, a quarter or more of work. The skill's own guidance is explicit: promote it when the project is being adopted as *infrastructure* or when a foundation tier is *the actual named objection you keep losing deals to* — not because it "looks credible" to a board. "Look credible" is an optics reason, and optics-driven governance moves are exactly what a security reviewer is trained to discount, because a foundation logo with no audit or disclosure process behind it yet is a sandbox-tier signal, not a graduated one.

Concretely: writing anything in the README that implies a foundation move is decided, underway, or imminent — before it's real — is a fabricated-status claim, the same failure class as writing "production ready" for a beta. It will read fine on the page and fail the moment a security reviewer asks "which foundation, what tier, when." Separate the two workstreams:

- The donation decision runs on its own timeline, owned by the board and counsel.
- The README gets fixed this week regardless of how that decision lands.

The reason this matters for this exact deal cycle: three cheaper, faster, fully reversible trust signals below are currently *unaddressed* (no SECURITY.md at all), while the board is reaching for the most expensive one. That's optimizing for the wrong end of the list while banks are mid-evaluation right now.

## Trust-signal order for this quarter

Per Step 8, ranked by return per hour, re-ranked against your actual constraint (evaluations happening *now*, not at quarter-end):

1. **Support expectation + release cadence** — one sentence each, costs nothing, needs no one's sign-off. You already have the fact: monthly releases. State it.
2. **Security policy** — costs an afternoon, no legal review, and is the one item on this list that directly answers "security teams are asking questions." This is your highest-leverage fix, full stop — cheaper than the badge row and worth more than anything else on the page right now.
3. **Governance and maintainer depth** — disclose the four-maintainer, single-employer structure honestly. Don't omit it; a security reviewer will find it in about the time it takes to check GitHub org membership or LinkedIn, and finding it themselves after the README stayed silent costs more trust than you stating it plainly with whatever mitigation is real (e.g., decision-making process, what happens if the company is acquired or a maintainer leaves).
4. **Supply-chain attestation** (SBOM, signed releases, reproducible build, dependency scanning in CI) — a week of engineering work, no legal review, and it's the item that persuades the engineer doing the actual security review, which for a ledger library matters more than the item that persuades whoever signs the contract.
5. **Named adopters** — you don't have one yet you can name. The two banks and the insurer are mid-evaluation, not confirmed logos, and naming a company requires their own marketing sign-off — doubly so mid-deal. Leave this row out entirely rather than implying customers you don't have permission to name.
6. **Foundation affiliation** — hold. See above.

## What the README should actually say

```markdown
# ledgerlink

[![Go Reference](https://pkg.go.dev/badge/github.com/brightmoor/ledgerlink.svg)](https://pkg.go.dev/github.com/brightmoor/ledgerlink)
[![Latest release](<VERSION_BADGE_URL>)](<RELEASES_URL>)
[![License](<LICENCE_BADGE_URL>)](./LICENSE)
[![CI](<CI_STATUS_BADGE_URL>)](<CI_URL>)

Ledgerlink is a double-entry accounting ledger library for Go: it enforces balanced transactions,
immutable posted entries, and multi-currency accounts at the data-model level, so an application
built on it cannot construct an unbalanced ledger by mistake.

<!-- Verify against source before shipping: does it enforce balance at write-time via a constraint,
     or only expose a validation function the caller must call? Those are different claims. -->

## Why ledgerlink

<!-- Needs the maintainer: name the concrete alternatives (e.g. rolling your own ledger table in
     Postgres, a hosted ledger API, another Go accounting library) and the specific axis you win
     on - performance, no external dependency, audit trail guarantees, licence terms. A vague
     "simple and fast" here fails the differentiation check and is the single scarcest, highest-
     value section on this page (present in only 25.7% of READMEs). Also state what ledgerlink
     deliberately does not do - e.g. no multi-tenant billing, no built-in reconciliation UI - so
     a reader can rule it out fast if it's the wrong fit. -->

## Status

Actively maintained. Releases roughly monthly; see [CHANGELOG.md](./CHANGELOG.md) for the version
history and [semver policy] for what a breaking change looks like here.

<!-- State the real semver/stability guarantee - has the API changed across the last N releases?
     A bank's engineering team will ask this before touching it. -->

## Usage

<!-- Smallest complete example that opens a ledger, posts one balanced transaction, and shows
     the result or the error on an unbalanced attempt. Must exist as a runnable file in the repo
     and be run from clean before this ships - this is the check that catches the most real
     damage in any README. -->

## Install

Requires Go <VERSION>.

```bash
go get github.com/brightmoor/ledgerlink
```

## Core API

<!-- The handful of entry points a new integrator actually touches - not the full godoc surface,
     which pkg.go.dev already serves better than this file can. -->

## Security

We take reports of vulnerabilities seriously. See [SECURITY.md](./SECURITY.md) for our
disclosure process and current supported-version policy.

## Governance and maintainers

ledgerlink is maintained by four engineers employed by Brightmoor. Release and merge decisions
are made by <describe: maintainer consensus / a named lead / whatever is actually true>.
<If there is a plan to formalize this - e.g. a documented decision process, or a stated intent
around broader governance - say so honestly; do not imply a foundation move that has not happened.>

## Documentation

Full API reference: <pkg.go.dev link>. Further guides: <docs site, if any>.

## License

<Name the actual licence>, see [LICENSE](./LICENSE).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
```

Notes on what's deliberately *not* in that skeleton:

- No "trusted by leading financial institutions" line, no logo row. You don't have permission to name any of the three companies currently evaluating you, and implying validated adoption you don't have is the same failure class as "production ready."
- No foundation badge, no "on our way to becoming a CNCF/[X] project" language, until that's real.
- Badge row capped at four, all assessment signals (version, licence, Go module reference, CI status) — no "PRs welcome" or contributor-count badges; those measurably correlate with lower trust from the audience that actually reads them.
- Contribution guidelines, code of conduct, and the full security disclosure process stay out of the README itself and live in their own recognized files — inlining them only adds scroll distance before a security reviewer gets to the one line they actually need (the pointer).

## SECURITY.md — write this one first

This is the cheapest, fastest, highest-leverage thing on the whole list, and it's the one item directly named in your prompt as missing while security teams are actively asking questions. A minimal version:

```markdown
# Security Policy

## Supported versions

<Table: which released versions currently receive security fixes.>

## Reporting a vulnerability

Email <security contact> or use GitHub's private vulnerability reporting
(Security tab → Report a vulnerability). We will acknowledge reports within
<a real number you can honor> and aim to release a fix within <a real number>.

## Disclosure

<State your actual practice - coordinated disclosure, CVE issuance via GitHub
Security Advisories, whatever you can genuinely commit to. Don't promise a
formal CVE process you don't run yet.>
```

Only commit to response-time numbers you can actually honor — this is the one enterprise signal in Step 8 that, once published, obligates you publicly. That's fine; it's still cheaper and more reversible than the foundation move, and it answers the actual question your evaluators are asking this week.

## Fix order, this cycle

1. Write `SECURITY.md` and link it from the README (answers the literal question in your prompt).
2. Add the status and governance sections, stated honestly — including the single-employer fact, not hiding it.
3. Add the release-cadence sentence (monthly — you already have this fact for free).
4. Verify and write the licence line, install path, and usage example against the actual repo (run it from clean — don't ship an unverified command).
5. Get the differentiation paragraph from whoever can name the real alternatives — this is the section worth the most and currently has nothing behind it.
6. Leave named adopters and foundation affiliation out of this pass. Revisit named adopters once a deal closes and marketing sign-off exists; revisit foundation affiliation once the board decision is actually made — and when it is, that's a one-line addition to a README that's already honest, not a rescue for one that wasn't.