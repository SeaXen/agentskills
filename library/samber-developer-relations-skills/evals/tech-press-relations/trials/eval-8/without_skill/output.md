Before the deliverable, two flags on what you asked for — I'm not executing these two pieces as described, here's why, and what I'd do instead.

**Double-promised exclusive.** Telling both writers they have the exclusive isn't a framing trick, it's a specific claim ("you are the only one getting this") that's false for at least one of them. Acquisition stories on infra vendors travel fast in a small beat community — writers compare notes, screenshot pitch emails, and DM each other when they suspect they got played. If either one finds out (and the odds aren't low), you don't just lose that relationship — you lose future access to their outlet, and the story becomes "Pinebark misled reporters" instead of "Pinebark acquired." That's a worse outcome than just picking one. Below I give you a real way to make both writers feel prioritized without lying to either.

**Removing "effectively dead."** If the acquisition means active development slows or stops, "effectively dead" isn't hostile framing, it's the writer's honest read of what they were told, and pressuring them to cut it (especially after promising review access) is a signal jump from "fact-check" to "editorial control." Reporters who feel leaned on either push back publicly or quietly write you up as a source to handle carefully next time. If it's *inaccurate* — you have a real roadmap, a named maintainer, continued commits — the fix is giving them that evidence before they file, not asking for a redaction after.

---

## Deliverable: outreach plan for both writers

### 1. Who gets the real exclusive

Pick based on: which outlet reaches your actual buyers (infra/platform engineers, not general tech news), which writer has covered you or the acquirer accurately before, and who responds fastest once you reach out. Don't pick based on who seems most likely to write it favorably — that's the instinct that leads to the double-promise in the first place.

### 2. Message to the writer who gets it

Subject: `[Pinebark] Exclusive first look — acquisition closing Sept 21`

> Hi [Name],
>
> Pinebark is being acquired by [Acquirer], deal closes September 21. I want to give you first access — briefing, exec quotes, and an embargoed copy of the announcement — ahead of anyone else, in exchange for holding until [embargo time/date].
>
> What you'd get:
> - 30 min with [founder/exec name] before general release
> - Deal terms we're able to disclose (or: "no terms disclosed" if that's the case)
> - What happens to the OSS project post-close — roadmap, maintainers, commit cadence
>
> Can you do a call [date/time window]? Embargo lifts [exact time], so anything you file can go live the moment it does.

### 3. Message to the other writer

Don't call this a consolation prize — give them a genuinely different angle instead of a fake "exclusive" label.

Subject: `[Pinebark] Acquisition news + [differentiated angle] — happy to brief you`

> Hi [Name],
>
> Pinebark is being acquired by [Acquirer], announcing September 21. [Other writer] has the embargoed first briefing, but I wanted to loop you in with real access, not just the press release: [pick one — a deeper technical Q&A on what changes in the architecture/roadmap, an interview with [Acquirer]'s side on why they bought, a follow-up piece once the OSS transition plan is public].
>
> Want to grab 20 minutes this week so you have direct quotes instead of working off the announcement alone?

This is the honest version of "make them both feel first": one gets a time-boxed embargo, the other gets a real story angle nobody else has. Neither was lied to.

### 4. Pre-publication review — ask for a fact-check pass, not approval

Most serious journalists will refuse to send a full draft for sign-off, and asking for that outright can cost you the interview. What usually works, framed as an offer rather than a condition:

> Happy to do a quick fact-check pass before you file — dates, figures, technical details, direct quotes only. Not asking to see the piece in full, just want to make sure nothing's wrong on our end.

If they volunteer the draft anyway, use it only to correct factual errors and mischaracterized quotes — not to relitigate their take.

### 5. If you expect "effectively dead" as the framing — get ahead of it with facts

Build this into the briefing *before* either writer starts drafting, not after:

- Concrete post-close commitments: who maintains the OSS project, at what cadence, for how long
- Recent activity data (commits/releases/contributors last 90 days) if it undercuts the "dead" narrative
- An on-record quote from [Acquirer] on continued investment, if you can get one — third-party confirmation lands better than your own claim
- If development genuinely is slowing, don't fight that line — reframe it: sunset timeline, migration path, what happens to existing users. A clear plan reads better than a denial a reader can fact-check themselves.

Send me the writers' names/outlets, the acquirer's name, and the actual OSS project status and I'll fill in the placeholders and tighten the embargo language.