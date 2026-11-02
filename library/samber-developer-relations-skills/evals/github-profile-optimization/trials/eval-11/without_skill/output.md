## The framework: OSPO — scaled to your size

What you're describing — "we have a public and private open-source posture and no one owns it" — is a solved problem with a name: **Open Source Program Office (OSPO)**. It's the term the Linux Foundation's **TODO Group** (the closest thing this space has to a standards body — members include Google, Microsoft, Salesforce, Comcast) uses for the function that owns a company's relationship to open source, both what you consume and what you publish. It's a name engineering leadership will recognize or can look up in five minutes, which is exactly what you want for a deck.

Two things to get right before you pitch it:

**Don't oversell the scale.** TODO Group's own guidance explicitly covers OSPO-as-a-part-time-role, not just OSPO-as-a-department. At 60 engineers and two public crates, ask for a **lightweight OSPO**: one named owner (10–20% of someone's time, not a hire), a one-page charter, and a repo/README standard — not a dedicated team. Pitching a full OSPO org to a 60-engineer shop will read as scope creep and get you a "no." Pitching "we need a named owner and a checklist" gets you a "yes" in one meeting.

**Split the problem in two**, because you actually have two different audiences complaining about two different things:

### 1. The embarrassing Forgejo org page → InnerSource Commons

If the page that's embarrassing is your internal Forgejo org — the landing spot the 60 engineers hit — that's not really an "open source marketing" problem, it's an **InnerSource** problem. InnerSource Commons (also Linux Foundation-adjacent, has its own named "patterns" library) is the standard framework for applying open-source hygiene — READMEs, CONTRIBUTING docs, ownership metadata, discoverability — to code that never leaves the building. It's the second name worth putting on the same slide, because it's the more literal fix for "our internal org page looks bad": a documented pattern set for exactly this, not something you'd invent from scratch.

Concretely, this becomes:
- A required README template per repo (owner, purpose, status, how to run it) — cheap, high leverage, fixes 90% of "embarrassing."
- A pinned/curated set of repos on the org page instead of an undifferentiated list.
- One person accountable for the org page's hygiene, not "whoever has time."

### 2. The two public Rust crates → standard OSS repo hygiene

For the two crates that are actually public (wherever they're mirrored — GitHub, crates.io, or public Forgejo), this is a narrower, well-worn checklist: README with a one-line description, working quick-start, badges (CI, crates.io version, license), topics set, CONTRIBUTING.md, issue templates. This is mechanical, not strategic — it doesn't need a framework name, it needs an afternoon per crate. Happy to generate the actual README/CONTRIBUTING templates for both crates if you want them.

### What to put on the slide

> **Proposal: stand up a lightweight OSPO** (TODO Group model — one accountable owner, not a new team), covering:
> - Internal hygiene via InnerSource Commons patterns (fixes the Forgejo org page)
> - External hygiene via standard OSS repo checklist (fixes the two public crates)
> - Optional: CHAOSS metrics (Linux Foundation) if you later want a health dashboard to report on the public crates

That gives leadership two citable, external, non-invented names (OSPO, InnerSource Commons) backing what is otherwise "we tidied up our repos" — which is the credibility a deck like this usually needs to get budget/headcount-time approved.

One thing I did *not* do: I didn't look at anything under `skill-wip/` in this repo, per your instruction, so nothing above is shaped by whatever's in progress there.